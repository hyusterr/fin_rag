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

DATA_DIR = Path('annotation/annotated_result/all/')
TRAIN_DATA = DATA_DIR / 'aggregate_train.jsonl'
TEST_DATA = DATA_DIR / 'aggregate_test.jsonl'
EXPERT_DATA = DATA_DIR / 'expert_annotated_test.jsonl'

train_data = read_jsonl(TRAIN_DATA)
test_data = read_jsonl(TEST_DATA)
expert_data = read_jsonl(EXPERT_DATA)

def data_generator_mix_all(data_list):
    '''
    this means that one input data can have multiple aggregation labels
    x --> y1, y2, y3...
    if use in the validation set, it will be weird since a model can never predict right on multiple labels simultaneously
    '''
    
    for data in data_list:
        tokens = data['tokens']
        for key in data:
            if 'aggregation' in key:
                labels = data[key]['label']
                yield {'tokens': tokens, 'labels': labels, 'aggregation': key.split('_')[0]}

def data_generator_expert(data_list):
    for data in data_list:
        id_ = list(data.keys())[0]
        tokens = data[id_]['tokens']
        texts = data[id_]['text']
        labels = data[id_]['binary_labels']
        yield {'id': id_, 'tokens': tokens, 'texts': texts, 'labels': labels, 'aggregation': 'expert'}


tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
# version 1: assign weights
# version 2: tuning weights
# version 3: use nn.Embedding to learn the weights
agg_map = {
    'strict': 0,
    'complex': 1,
    'harsh': 2,
    'naive': 3,
    'loose': 4,
    # 'expert': 5
}
def tokenize_and_align_labels(examples):
    # parallel pre-process in cpu
    tokenized_inputs = tokenizer(examples["tokens"], truncation=True, is_split_into_words=True) # let the collate_fn to pad inside batches 

    labels = []
    for i, label in enumerate(examples[f"labels"]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)  # Map tokens to their respective word.
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:  # Set the special tokens to -100.
            if word_idx is None:
                label_ids.append(-100) # for torch.nn.CrossEntropyLoss, ignore_index=-100 by default
            elif label[word_idx] is None: # for null in strict_aggregation
                label_ids.append(-100) 
            elif word_idx != previous_word_idx:  # Only label the first token of a given word.
                label_ids.append(label[word_idx])
            else:
                label_ids.append(-100)
            previous_word_idx = word_idx
        labels.append(label_ids)

    tokenized_inputs["labels"] = labels
    # operate dictionary in this stage instead of gpu
    tokenized_inputs['aggregation'] = [agg_map[agg] if agg in agg_map else 0 for agg in examples['aggregation']]

    return tokenized_inputs


seqeval = evaluate.load("seqeval")
label_list = ['0', '1']
'''
def postprocess(predictions, labels):
    predictions = predictions.detach().cpu().clone().numpy()
    labels = labels.detach().cpu().clone().numpy()

    # Remove ignored index (special tokens) and convert to labels
    true_labels = [[label_list[l] for l in label if l != -100] for label in labels]
    true_predictions = [
        [label_names[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    return true_labels, true_predictions
'''

def compute_metrics(p, compute_result=False):

    # print(type(p))
    '''
    if compute_result:
        #  When set to True, you must pass a compute_metrics function that takes a boolean argument compute_result, which when passed True, will trigger the final global summary statistics from the batch-level summary statistics you’ve accumulated over the evaluation set.
        print(p)
        # return p
    '''

    predictions, labels = p
    # print(len(predictions))
    # print(predictions[0])
    # predictions = predictions[0].detach().cpu().clone().numpy()
    # labels = labels.detach().cpu().clone().numpy()
    predictions = np.argmax(predictions, axis=2)

    true_predictions = [
        [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_labels = [
        [label_list[l] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]

    results = seqeval.compute(predictions=true_predictions, references=true_labels)
    return {
        "precision": results["overall_precision"],
        "recall": results["overall_recall"],
        "f1": results["overall_f1"],
        "accuracy": results["overall_accuracy"],
    }


# see: https://github.com/huggingface/transformers/blob/v4.47.1/src/transformers/data/data_collator.py#L288
# see: https://huggingface.co/docs/transformers/main_classes/data_collator#transformers.DataCollatorForTokenClassification
# see: https://pytorch.org/docs/stable/data.html
# see: https://pytorch.org/docs/stable/_modules/torch/utils/data/_utils/collate.html#default_collate
# see: carefully check the relation between collate_fn and batch and model input, you can do it!

class AggDataCollatorForTokenClassification(DataCollatorForTokenClassification):
    # collate funtion: the collate_fn argument is used to collate lists of samples into batches.
    # make sure the output of collate_fn is the input of model, which should only contains tensors

    def __init__(self, tokenizer, padding=True, max_length=None, pad_to_multiple_of=None, label_pad_token_id=-100, return_tensors="pt"):
        super().__init__(tokenizer=tokenizer, padding=padding, max_length=max_length, pad_to_multiple_of=pad_to_multiple_of, label_pad_token_id=label_pad_token_id, return_tensors=return_tensors)
    
    # overwrite torch_call only
    def torch_call(self, features):
        # features: a list of dict
        # print(features)
        # print(features[0].keys())
        import torch
        label_name = "label" if "label" in features[0].keys() else "labels"
        labels = [feature[label_name] for feature in features] if label_name in features[0].keys() else None
        no_label_features = [{"input_ids": feature["input_ids"], "attention_mask": feature["attention_mask"]} for feature in features] 
        batch = pad_without_fast_tokenizer_warning(
            self.tokenizer,
            no_label_features,
            max_length=self.max_length,
            pad_to_multiple_of=self.pad_to_multiple_of,
            return_tensors="pt",
        )
        agg_labels = [feature["aggregation"] for feature in features]
        agg_labels = F.one_hot(torch.tensor(agg_labels), num_classes=len(agg_map))
        batch["aggregation"] = agg_labels # torch.tensor(agg_labels)
        if labels is None:
            return batch
        
        sequence_length = batch["input_ids"].shape[1]
        padding_side = self.tokenizer.padding_side
        
        def to_list(tensor_or_iterable):
            if isinstance(tensor_or_iterable, torch.Tensor):
                return tensor_or_iterable.tolist()
            return list(tensor_or_iterable)

        if padding_side == "right":
            batch[label_name] = [
                to_list(label) + [self.label_pad_token_id] * (sequence_length - len(label)) for label in labels
            ]
        else:
            batch[label_name] = [
                [self.label_pad_token_id] * (sequence_length - len(label)) + to_list(label) for label in labels
            ]

        batch[label_name] = torch.tensor(batch["labels"], dtype=torch.int64)
        return batch
        





train_dataset = Dataset.from_generator(data_generator_mix_all, gen_kwargs={'data_list': train_data})
test_dataset = Dataset.from_generator(data_generator_mix_all, gen_kwargs={'data_list': test_data})
expert_dataset = Dataset.from_generator(data_generator_expert, gen_kwargs={'data_list': expert_data})
highlight_dataset = DatasetDict({'train': train_dataset, 'test': expert_dataset})
tokenized_datasets = highlight_dataset.map(tokenize_and_align_labels, batched=True)

# train_dataset.set_format(type='torch')
# print(tokenized_datasets['train'][0])
# collate_fn: input a list of samples from the dataset and collate them into a batch of data
data_collator = AggDataCollatorForTokenClassification(tokenizer=tokenizer)
# train_dataloader = DataLoader(tokenized_datasets['train'], batch_size=16, shuffle=True, collate_fn=data_collator)
# instance = next(iter(train_dataloader))
# print(instance)

# model = AutoModelForTokenClassification.from_pretrained("bert-base-uncased", num_labels=2)

model = AggHighlighter()
# print(model(instance))

# https://discuss.huggingface.co/t/indexerror-invalid-key-16-is-out-of-bounds-for-size-0/14298/11
# that's why sometimes I don't like the huggingface's API, it's not clear and not easy to debug
training_args = TrainingArguments(
    output_dir="checkpoints/agg_highlight",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=20,
    weight_decay=0.01,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    remove_unused_columns=False,
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
    eval_dataset=tokenized_datasets["test"],
    # processing_class=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
    callbacks = [EarlyStoppingCallback(early_stopping_patience=5)]
)
# trainer.evaluate(ignore_keys=['attentions', 'hidden_states'])
trainer.train(ignore_keys_for_eval=['attentions', 'hidden_states'])
