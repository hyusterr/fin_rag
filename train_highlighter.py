import os
import random
import numpy as np
import torch
from tqdm import tqdm
from pathlib import Path
from datasets import Dataset, DatasetDict
from transformers import (
    AutoTokenizer,
    AutoModelForTokenClassification,
    TrainingArguments,
    Trainer,
    EarlyStoppingCallback,
    set_seed
)
from scipy.special import softmax
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score

from evaluation.metrics import (
    get_observed_disorder,
    get_auprc,
    get_r_precision,
    get_correlation,
)

import wandb


def set_global_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    set_seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def compute_metrics(p):
    predictions, labels = p
    predictions_bin = np.argmax(predictions, axis=2)
    predictions_prob_pos = softmax(predictions, axis=2)[:, :, 1]

    true_predictions_bin = [
        [p for (p, l) in zip(pred, label) if l != -100]
        for pred, label in zip(predictions_bin, labels)
    ]
    true_labels = [
        [l for (p, l) in zip(pred, label) if l != -100]
        for pred, label in zip(predictions, labels)
    ]
    true_predictions_prob_pos = [
        [p for (p, l) in zip(pred, label) if l != -100]
        for pred, label in zip(predictions_prob_pos, labels)
    ]

    disorder = [get_observed_disorder(l, p) for l, p in tqdm(zip(true_labels, true_predictions_bin))]
    f1 = [f1_score(l, p, pos_label=1, average='binary') for l, p in zip(true_labels, true_predictions_bin)]
    precision = [precision_score(l, p, pos_label=1, average='binary') for l, p in zip(true_labels, true_predictions_bin)]
    recall = [recall_score(l, p, pos_label=1, average='binary') for l, p in zip(true_labels, true_predictions_bin)]
    accuracy = [accuracy_score(l, p) for l, p in zip(true_labels, true_predictions_bin)]
    auprc = [get_auprc(l, p) for l, p in zip(true_labels, true_predictions_prob_pos)]
    r_precision = [get_r_precision(p, l) for l, p in zip(true_labels, true_predictions_prob_pos)]
    correlation = [get_correlation(l, p) for l, p in zip(true_labels, true_predictions_prob_pos)]

    return {
        "f1": np.nanmean(f1),
        "precision": np.nanmean(precision),
        "recall": np.nanmean(recall),
        "accuracy": np.nanmean(accuracy),
        "auprc": np.nanmean(auprc),
        "disorder": np.nanmean(disorder),
        "r_precision": np.nanmean(r_precision),
    }


def run_highlight_experiment(
    agg_types,
    train_data,
    valid_data,
    test_data,
    expert_data,
    tokenizer_path="bert-base-uncased",
    model_path="bert-base-uncased",
    tokenizer_fn=None,
    model_fn=None,
    aggregation_label_fn=None,
    train_model=True,
    output_dir_root="checkpoints",
    wandb_project="highlight_project",
    num_train_epochs=20,
    seed=42,
    train_agg_types=None,
):
    set_global_seed(seed)
    os.environ["WANDB_PROJECT"] = wandb_project
    wandb.login()

    tokenizer = tokenizer_fn(tokenizer_path) if tokenizer_fn else AutoTokenizer.from_pretrained(tokenizer_path)

    def default_tokenize_fn(examples):
        from data_utils import tokenize_and_align_labels
        return tokenize_and_align_labels(examples, tokenizer=tokenizer)

    tokenize_and_align_labels_wrapper = default_tokenize_fn

    for agg_type in agg_types:
        print("[START]", agg_type)

        from data_utils import data_generator_mix_all, data_generator_expert, AggDataCollatorForTokenClassification, ID2LABEL, LABEL2ID

        train_agg_labels = [f"{agg_type}_aggregation"] if not train_agg_types else [f"{t}_aggregation" for t in train_agg_types]

        train_dataset = Dataset.from_generator(
            data_generator_mix_all,
            gen_kwargs={"data_list": train_data, "aggregation_labels": train_agg_labels},
        )
        valid_dataset = Dataset.from_generator(
            data_generator_mix_all,
            gen_kwargs={"data_list": valid_data, "aggregation_labels": ["naive_aggregation"]},
        )
        test_dataset = Dataset.from_generator(
            data_generator_mix_all,
            gen_kwargs={"data_list": test_data, "aggregation_labels": ["naive_aggregation"]},
        )
        expert_dataset = Dataset.from_generator(
            data_generator_expert, gen_kwargs={"data_list": expert_data}
        )

        raw_datasets = DatasetDict({
            "train": train_dataset,
            "valid": valid_dataset,
            "test": test_dataset,
            "expert": expert_dataset,
        })

        tokenized_datasets = raw_datasets.map(tokenize_and_align_labels_wrapper, batched=True)
        data_collator = AggDataCollatorForTokenClassification(tokenizer=tokenizer)

        if model_fn:
            model = model_fn()
        else:
            model = AutoModelForTokenClassification.from_pretrained(
                model_path, num_labels=2, id2label=ID2LABEL, label2id=LABEL2ID
            )

        output_dir = Path(output_dir_root) / f"{agg_type}_agg_naive_valid"
        training_args = TrainingArguments(
            output_dir=str(output_dir),
            run_name=f"{agg_type}_agg_naive_valid",
            learning_rate=2e-5,
            per_device_train_batch_size=16,
            per_device_eval_batch_size=16,
            num_train_epochs=num_train_epochs,
            weight_decay=0.01,
            label_names=['labels'],
            evaluation_strategy="epoch",
            save_strategy="epoch",
            load_best_model_at_end=True,
            remove_unused_columns=False,
            report_to="wandb",
            metric_for_best_model='valid_disorder',
            greater_is_better=False,
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=tokenized_datasets["train"] if train_model else None,
            eval_dataset={
                "train": tokenized_datasets["train"],
                "valid": tokenized_datasets["valid"],
                "test": tokenized_datasets["test"],
                "expert": tokenized_datasets["expert"],
            },
            data_collator=data_collator,
            compute_metrics=compute_metrics,
            callbacks=[EarlyStoppingCallback(early_stopping_patience=5)] if train_model else [],
        )

        if train_model:
            trainer.train()

        print("[EVALUATE]", agg_type)
        trainer.evaluate(tokenized_datasets["test"], ignore_keys=['attentions', 'hidden_states'])
        wandb.finish()
        print("[FINISH]", agg_type)
