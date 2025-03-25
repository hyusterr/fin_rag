# from highlighter.base import BERTHighlighter
from utils.utils import read_jsonl
from torch.utils.data import DataLoader
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import DataCollatorForTokenClassification, TrainingArguments, Trainer, EarlyStoppingCallback
from transformers.data.data_collator import DataCollatorMixin, pad_without_fast_tokenizer_warning
from highlighter.agg_highlighter import AggHighlighter
from datasets import Dataset, load_dataset, DatasetDict
import evaluate
from pathlib import Path
import numpy as np
from scipy.special import softmax

import multiprocessing
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from tqdm import tqdm

from sklearn.metrics import (
    f1_score,
    precision_score,
    recall_score,
    accuracy_score
)
from evaluation.metrics import (
    get_observed_disorder, 
    get_auprc, 
    get_r_precision, 
    get_correlation
)
from data_utils import (
    data_generator_mix_all, 
    data_generator_expert, 
    tokenize_and_align_labels,
    read_setting2_data,
    AggDataCollatorForTokenClassification,
    ID2LABEL,
    LABEL2ID
)

import warnings
warnings.filterwarnings('ignore')
'''
import logging
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("datasets").setLevel(logging.ERROR)
logging.getLogger("torch").setLevel(logging.ERROR)
logging.getLogger(__name__).setLevel(logging.INFO)
'''


def compute_metrics(p):
    '''
    p: transformers.EvalPrediction or tuple of predictions and labels
    - EvalPrediction: utility of transformers, is default output type of Trainer
    - see: https://github.com/huggingface/transformers/blob/a22a4378d97d06b7a1d9abad6e0086d30fdea199/src/transformers/trainer.py#L365
    - see also: https://huggingface.co/docs/transformers/internal/trainer_utils#transformers.EvalPrediction
    '''

    # label: ground truth, -100 is ignored (special token or ##subword)
    predictions, labels = p # nd.array
    predictions_bin = np.argmax(predictions, axis=2)
    predictions_prob_pos = softmax(predictions, axis=2)[:, :, 1]

    
    true_predictions_bin = [
        [p for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions_bin, labels)
    ]
    true_labels = [
        [l for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_predictions_prob_pos = [
        [p for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions_prob_pos, labels)
    ]


    disorder = []
    for l, p in tqdm(zip(true_labels, true_predictions_bin)):
        disorder.append(get_observed_disorder(l, p))
        

    
    # do not use seqeval since it's not a NER task
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
        "num_nan_disorder": np.sum(np.isnan(disorder)),
    }



if __name__ == '__main__':

    # multiprocessing.set_start_method('spawn', force=True)
    train_data, valid_data, test_data, expert_data = read_setting2_data()
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")   

    import os
    os.environ["WANDB_PROJECT"]="fin.highlight"
    import wandb
    wandb.login()

    def tokenize_and_align_labels_wrapper(examples):
        return tokenize_and_align_labels(examples, tokenizer=tokenizer)

    for agg_type in ['naive', 'loose']: # ['strict', 'complex', 'harsh', 'naive', 'loose']:
        print('[START] training for', agg_type)
        train_dataset = Dataset.from_generator(data_generator_mix_all, gen_kwargs={'data_list': train_data, 'aggregation_labels': [f'{agg_type}_aggregation']})
        valid_dataset = Dataset.from_generator(data_generator_mix_all, gen_kwargs={'data_list': valid_data, 'aggregation_labels': [f'naive_aggregation']})
        test_dataset = Dataset.from_generator(data_generator_mix_all, gen_kwargs={'data_list': test_data, 'aggregation_labels': [f'naive_aggregation']})
        expert_dataset = Dataset.from_generator(data_generator_expert, gen_kwargs={'data_list': expert_data})
        highlight_dataset = DatasetDict({'train': train_dataset, 'valid': valid_dataset, 'test': test_dataset, 'expert': expert_dataset})
        tokenized_datasets = highlight_dataset.map(tokenize_and_align_labels_wrapper, batched=True)
        data_collator = AggDataCollatorForTokenClassification(tokenizer=tokenizer)
        model = AutoModelForTokenClassification.from_pretrained("bert-base-uncased", num_labels=2, id2label=ID2LABEL, label2id=LABEL2ID)
        # model = AggHighlighter()

        # https://discuss.huggingface.co/t/indexerror-invalid-key-16-is-out-of-bounds-for-size-0/14298/11
    # that's why sometimes I don't like the huggingface's API, it's not clear and not easy to debug
        training_args = TrainingArguments(
            output_dir=f"checkpoints/{agg_type}_agg_naive_valid_setting2",
            run_name=f"{agg_type}_agg_naive_valid[setting2]",
            learning_rate=2e-5,
            per_device_train_batch_size=16,
            per_device_eval_batch_size=16,
            num_train_epochs=50,
            weight_decay=0.01,
            label_names=['labels'],
            eval_strategy="epoch",
            save_strategy="epoch",
            load_best_model_at_end=True,
            remove_unused_columns=False,
            report_to="wandb",
            metric_for_best_model='valid_disorder',
            greater_is_better=False,
            # dataloader_num_workers=0,
            # eval_accumulation_steps=1,
            # save_safetensors=False,
            # save_total_limit=3,
            # batch_eval_metrics=True,
            # eval_do_concat_batches=False, # trainer by default will concatenate the batches before the evaluation, leads to torch.cat error
            # dispatch_batches=True # another weird bug: https://github.com/huggingface/transformers/issues/26548 
        )
        # there is a very weird behavior in trainer, it will collect all kinds of outputs from the model, including logits, hidden states, attentions, etc. batch by batch
        # and then concatenate them, which will lead to the error: `RuntimeError: Sizes of tensors must match except in dimension 0. Got 16 and 0 in dimension 1` since the criterion to decide if it is need to adjust padding size is tensor.shape[1] are all the same.
# but the shape[1] of attentions are all the same (12=layers), so it will raise the error when concatenate them directly...

        # about specify devices: https://github.com/huggingface/transformers/issues/12570#issuecomment-876009872
        # "If you have multiple GPUs available, the Trainer will use all of them, that is expected and not a bug."
        # `CUDA_VISIBLE_DEVICES=2 python main.py...` to specify the GPU

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=tokenized_datasets["train"],
            eval_dataset={
                'train': tokenized_datasets["train"],
                'valid': tokenized_datasets["valid"], 
                'test': tokenized_datasets["test"], 
                'expert': tokenized_datasets["expert"]
            },
            # processing_class=tokenizer,
            data_collator=data_collator,
            compute_metrics=compute_metrics,
            callbacks = [EarlyStoppingCallback(early_stopping_patience=5)],
        )
        # trainer.evaluate(ignore_keys=['attentions', 'hidden_states'])
        trainer.train(ignore_keys_for_eval=['attentions', 'hidden_states'])
        trainer.evaluate(trainer.train_dataset, ignore_keys=['attentions', 'hidden_states'])
        print('[FINISH] training for', agg_type)
        wandb.finish()
        print('=====================')
