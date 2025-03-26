import os
import random
import warnings
from pathlib import Path
from typing import List, Optional

import numpy as np
import torch
import torch.nn.functional as F
from datasets import Dataset, DatasetDict
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
from tqdm import tqdm
from transformers import (
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    EarlyStoppingCallback,
    pipeline,
)
import evaluate

# Import your custom modules (adjust the import paths as needed)
from data_utils import (
    data_generator_mix_all,
    data_generator_expert,
    tokenize_and_align_labels,
    AggDataCollatorForTokenClassification,
    read_setting2_data,
    ID2LABEL,
    LABEL2ID,
)
from evaluation.metrics import (
    get_observed_disorder,
    get_auprc,
    get_r_precision,
    get_correlation,
)
from highlighter.agg_highlighter import AggHighlighter

# Suppress warnings
warnings.filterwarnings("ignore")


def compute_metrics(p):
    """
    Compute evaluation metrics for the Trainer.
    p: (predictions, labels), where predictions is a numpy array.
    """
    predictions, labels = p  # predictions: ndarray; labels: ndarray (with -100 indicating ignore)
    predictions_bin = np.argmax(predictions, axis=2)
    # Compute probabilities with softmax over the last axis
    predictions_prob_pos = softmax(predictions, axis=2)[:, :, 1]

    # Filter out ignored tokens (-100)
    true_predictions_bin = [
        [pred for (pred, lab) in zip(pred_seq, lab_seq) if lab != -100]
        for pred_seq, lab_seq in zip(predictions_bin, labels)
    ]
    true_labels = [
        [lab for lab in lab_seq if lab != -100] for lab_seq in labels
    ]
    true_predictions_prob_pos = [
        [prob for (prob, lab) in zip(prob_seq, lab_seq) if lab != -100]
        for prob_seq, lab_seq in zip(predictions_prob_pos, labels)
    ]

    # Compute the disorder metric for each sequence
    disorder = []
    for l, p in tqdm(zip(true_labels, true_predictions_bin), total=len(true_labels), desc="Computing disorder"):
        disorder.append(get_observed_disorder(l, p))
    # print('Number of NaN disorder:', np.sum(np.isnan(disorder)))

    # Compute standard metrics
    f1 = [f1_score(l, p, pos_label=1, average='binary') for l, p in zip(true_labels, true_predictions_bin)]
    precision = [precision_score(l, p, pos_label=1, average='binary') for l, p in zip(true_labels, true_predictions_bin)]
    recall = [recall_score(l, p, pos_label=1, average='binary') for l, p in zip(true_labels, true_predictions_bin)]
    accuracy = [accuracy_score(l, p) for l, p in zip(true_labels, true_predictions_bin)]
    auprc = [get_auprc(l, p) for l, p in zip(true_labels, true_predictions_prob_pos)]
    r_precision = [get_r_precision(p, l) for l, p in zip(true_labels, true_predictions_prob_pos)]
    # You can also add additional metrics (e.g., correlation) if needed

    return {
        "f1": np.nanmean(f1),
        "precision": np.nanmean(precision),
        "recall": np.nanmean(recall),
        "accuracy": np.nanmean(accuracy),
        "auprc": np.nanmean(auprc),
        "disorder": np.nanmean(disorder),
        "r_precision": np.nanmean(r_precision),
        "num_nan_disorder": np.sum(np.isnan(disorder)),
    }


def set_global_seed(seed: int):
    """Set random seed for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

def AggTrainer(Trainer):
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    '''

    def compute_loss(self, model, inputs, return_outputs=False):
        """
        Compute the loss for the model.
        """
        current_epoch = self.state.epoch if self.state is not None else 0
        inputs["epoch"] = current_epoch
        return super().compute_loss(model, inputs, return_outputs=return_outputs)


def train_highlighter(
    model,
    tokenizer,
    train_agg_types: List[str] = ["naive"],
    validate_agg_type: str = "naive",
    compute_metrics_fn=compute_metrics,
    metric_for_best_model: str = "valid_f1",  # e.g., "valid_f1", "disorder", etc.
    greater_is_better: bool = True,
    training_args_kwargs: Optional[dict] = None,
    train_model: bool = True,
    seed: int = 42,
    data_collator: Optional = None,
    inference_module: Optional[object] = None,
):
    """
    Train (or run inference) using the HuggingFace Trainer framework.

    Args:
        model: HuggingFace model instance.
        tokenizer: HuggingFace tokenizer instance.
        train_agg_types: List of aggregation types (e.g., ["naive", "loose"]) to be used as training labels.
        compute_metrics_fn: Function to compute evaluation metrics.
        metric_for_best_model: Metric used for best model selection.
        greater_is_better: Whether a higher metric value is better.
        training_args_kwargs: Dictionary for overriding default TrainingArguments.
        train_model: If False, skip training and run inference only.
        seed: Random seed.
        data_collator: Custom data collator; if None, a default AggDataCollatorForTokenClassification is used.
        inference_module: Optional module for specialized inference (e.g., attn_highlighter).
    Returns:
        If training: the Trainer instance after training.
        If inference-only: inference outputs.
    """
    # Set the random seed for reproducibility
    set_global_seed(seed)

    # Load data directly using read_setting2_data()
    train_data, valid_data, test_data, expert_data = read_setting2_data()

    # Prepare aggregation labels, e.g., "naive_aggregation", "loose_aggregation", etc.
    agg_labels = [f"{agg}_aggregation" for agg in train_agg_types]
    validate_agg_type = f"{validate_agg_type}_aggregation"
    train_dataset = Dataset.from_generator(
        data_generator_mix_all,
        gen_kwargs={'data_list': train_data, 'aggregation_labels': agg_labels},
    )
    valid_dataset = Dataset.from_generator(
        data_generator_mix_all,
        gen_kwargs={'data_list': valid_data, 'aggregation_labels': [validate_agg_type]},
    )
    test_dataset = Dataset.from_generator(
        data_generator_mix_all,
        gen_kwargs={'data_list': test_data, 'aggregation_labels': [validate_agg_type]},
    )
    datasets = {"train": train_dataset, "valid": valid_dataset, "test": test_dataset}
    expert_dataset = Dataset.from_generator(
        data_generator_expert, gen_kwargs={'data_list': expert_data}
    )
    datasets["expert"] = expert_dataset
    dataset_dict = DatasetDict(datasets)

    # Tokenize and align labels
    def tokenize_and_align_labels_wrapper(examples):
        return tokenize_and_align_labels(examples, tokenizer=tokenizer)

    tokenized_datasets = dataset_dict.map(tokenize_and_align_labels_wrapper, batched=True)

    # Use a default data collator if none is provided
    if data_collator is None:
        data_collator = AggDataCollatorForTokenClassification(tokenizer=tokenizer)

    # Set up TrainingArguments with defaults (overridable via training_args_kwargs)
    training_args_kwargs = training_args_kwargs or {}
    training_args = TrainingArguments(
        output_dir=training_args_kwargs.get("output_dir", "checkpoints/highlighter"),
        run_name=training_args_kwargs.get("run_name", "highlighter_training"),
        learning_rate=training_args_kwargs.get("learning_rate", 2e-5),
        per_device_train_batch_size=training_args_kwargs.get("train_batch_size", 16),
        per_device_eval_batch_size=training_args_kwargs.get("eval_batch_size", 16),
        num_train_epochs=training_args_kwargs.get("num_train_epochs", 50),
        weight_decay=training_args_kwargs.get("weight_decay", 0.01),
        label_names=["labels"],
        eval_strategy=training_args_kwargs.get("eval_strategy", "epoch"),
        save_strategy=training_args_kwargs.get("save_strategy", "epoch"),
        load_best_model_at_end=True,
        remove_unused_columns=False,
        report_to=training_args_kwargs.get("report_to", "wandb"),
        metric_for_best_model=metric_for_best_model,
        greater_is_better=greater_is_better,
    )

    # Inference-only mode: skip training and run inference on sample texts.
    '''
    if not train_model:
        sample_texts = ["This is a sample input text for highlighting inference."]
        if inference_module is not None:
            # Expecting the module to have a method `highlighting_outputs`
            return inference_module.highlighting_outputs(sample_texts)
        elif hasattr(model, "encode"):
            return model.encode(sample_texts)
        else:
            # Fallback: use a token-classification pipeline.
            pipe = pipeline("token-classification", model=model, tokenizer=tokenizer)
            return pipe(sample_texts)
    '''

    # Initialize the Trainer
    trainer = AggTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset={
            "train": tokenized_datasets["train"],
            "valid": tokenized_datasets["valid"],
            "test": tokenized_datasets["test"],
            "expert": tokenized_datasets["expert"]
        },
        data_collator=data_collator,
        compute_metrics=compute_metrics_fn,
        callbacks=[
            EarlyStoppingCallback(
                early_stopping_patience=training_args_kwargs.get("early_stopping_patience", 5)
            )
        ],
    )

    # Train and then evaluate the model
    if train_model:
        trainer.train(ignore_keys_for_eval=["attentions", "hidden_states"])
    trainer.evaluate(trainer.train_dataset, ignore_keys=["attentions", "hidden_states"])
    return trainer


# ===== Example usage =====
if __name__ == "__main__":
    # Load your default model and tokenizer (or plug in any alternative)
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    from transformers import AutoModelForTokenClassification
    model = AutoModelForTokenClassification.from_pretrained(
        "bert-base-uncased",
        num_labels=2,
        id2label=ID2LABEL,
        label2id=LABEL2ID,
    )

    # Optionally, you can prepare an inference module (e.g., an attn_highlighter instance)
    inference_module = None  # Replace with your module instance if needed

    # Call the training function.
    # Set train_model=False to run in inference-only mode.
    trainer_obj = train_highlighter(
        model=model,
        tokenizer=tokenizer,
        train_agg_types=["strict"],
        metric_for_best_model="f1",
        greater_is_better=True,
        training_args_kwargs={
            "output_dir": "checkpoints/highlighter_strict",
            "run_name": "highlighter_strict",
            "learning_rate": 2e-5,
            "num_train_epochs": 30,
            "early_stopping_patience": 5,
        },
        train_model=True,  # Change to False for inference-only mode
        inference_module=inference_module,
    )

    # If training, trainer_obj is the Trainer instance.
    print("Training complete.")

