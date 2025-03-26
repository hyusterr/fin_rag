import json
import random
import pandas as pd
from pathlib import Path
from pprint import pprint
from typing import List
from collections import Counter
import torch
import torch.nn.functional as F
from transformers import DataCollatorForTokenClassification
from transformers.data.data_collator import DataCollatorMixin, pad_without_fast_tokenizer_warning

from utils.utils import read_jsonl
DATA_DIR = Path('annotation/annotated_result/all/setting2/')
TRAIN_DATA = DATA_DIR / 'train.jsonl'
VALID_DATA = DATA_DIR / 'valid.jsonl'
TEST_DATA = DATA_DIR / 'test.jsonl'
EXPERT_DATA = DATA_DIR / 'expert.jsonl'
AGG_MAP = {
    'strict': 0,
    'complex': 1,
    'harsh': 2,
    'naive': 3,
    'loose': 4,
    # 'expert': 5
}
LABEL_LIST = ['0', '1']
ID2LABEL = {i: label for i, label in enumerate(LABEL_LIST)}
LABEL2ID = {label: i for i, label in ID2LABEL.items()}

def illustrate_a_sample(tokenized_datasets, model, data_collator, index=0):
    import torch.nn.functional as F
    # prepare case study samples
    model.eval()
    model.to('cpu')
    train_sample = data_collator.torch_call([tokenized_datasets['train'][index]])
    train_sample_label = train_sample['labels'].tolist()
    valid_sample = data_collator.torch_call([tokenized_datasets['valid'][index]])
    valid_sample_label = valid_sample['labels'].tolist()
    expert_sample = data_collator.torch_call([tokenized_datasets['test'][index]])
    expert_sample_label = expert_sample['labels'].tolist()

    train_pred = F.sigmoid(model(**train_sample).logits[0]).max(1).indices.tolist()
    valid_pred = F.sigmoid(model(**valid_sample).logits[0]).max(1).indices.tolist()
    expert_pred = F.sigmoid(model(**expert_sample).logits[0]).max(1).indices.tolist()
    print('Train Sample:')
    print(f'Label: {train_sample_label}')
    print(f'Prediction: {train_pred}')
    print('Valid Sample:')
    print(f'Label: {valid_sample_label}')
    print(f'Prediction: {valid_pred}')
    print('Expert Sample:')
    print(f'Label: {expert_sample_label}')
    print(f'Prediction: {expert_pred}')



# load the data
def read_setting2_data():
    train_data = read_jsonl(TRAIN_DATA)
    valid_data = read_jsonl(VALID_DATA)
    test_data = read_jsonl(TEST_DATA)
    expert_data = read_jsonl(EXPERT_DATA)
    return train_data, valid_data, test_data, expert_data


def data_generator_mix_all(data_list, aggregation_labels=['strict_aggregation', 'complex_aggregation', 'harsh_aggregation', 'naive_aggregation', 'loose_aggregation']):
    '''
    this means that one input data can have multiple aggregation labels
    x --> y1, y2, y3...
    if use in the validation set, it will be weird since a model can never predict right on multiple labels simultaneously
    '''
    
    for data in data_list:
        tokens = data['tokens']
        for key in data:
            if 'aggregation' in key:
                if key not in aggregation_labels:
                    continue
                labels = data[key]['label']
                yield {'tokens': tokens, 'labels': labels, 'aggregation': key.split('_')[0]}

def data_generator_expert(data_list):
    for data in data_list:
        id_ = list(data.keys())[0]
        tokens = data[id_]['tokens']
        texts = data[id_]['text']
        labels = data[id_]['binary_labels']
        yield {'id': id_, 'tokens': tokens, 'texts': texts, 'labels': labels, 'aggregation': 'expert'}

def tokenize_and_align_labels(examples, tokenizer):
    # parallel pre-process in cpu
    tokenized_inputs = tokenizer(examples["tokens"], truncation=True, is_split_into_words=True) # let the collate_fn to pad inside batches so don't need to pad here

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

            # [NOTE] for now, do not abadon the label from the second subword, just follow what YH's code does 
            # [2025.3.20 Change] Follow huggingface's tutorial, abandon the label from the second subword
            elif word_idx != previous_word_idx:  
                # Only label the first token of a given word. if the second subword is lablled will cause the output label amount larger than annotated label amount (= number of words)
                label_ids.append(label[word_idx])
            else: # for the second subword
                label_ids.append(-100)
            previous_word_idx = word_idx
        labels.append(label_ids)

    tokenized_inputs["labels"] = labels
    # operate dictionary in this stage instead of gpu
    tokenized_inputs['aggregation'] = [AGG_MAP[agg] if agg in AGG_MAP else 0 for agg in examples['aggregation']]

    return tokenized_inputs

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
        agg_labels = F.one_hot(torch.tensor(agg_labels), num_classes=len(AGG_MAP)).float()
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



def get_statistics(data_path: str):
    '''
    file format: JSONL, e.g.
    {
        "id": "20221028_10-K_320193_part2_item7_para1",
        "text": "The Company is a leading global provider of technology solutions for the energy industry...",
        "tokens": ["The", "Company", "is", "a", "leading", ...],
        "highlight_probs": [0.0, 0.0, 1.0, 0.33, 0.0, ...],
        "highlight_labels": [0, 0, 1, 1, 0, ...],
        "highlight_spans", ["is a leading global", "energy industry", ...]
        "type": "0" # or "1", "2", "3", "4"
        "topic": "1" # or "2", "3", "4", "5", ....
        "subtopic": "7-2" ... # might be empty
    }
    '''
    statistics = {}

    # get data
    data = read_jsonl(data_path)

    # get type statistics
    type_count = Counter([item['type'] for item in data])
    ratio = {k: v/len(data) for k, v in type_count.items()}
    statistics['type'] = {
        'count': type_count,
        'ratio': ratio
    }

    # get topic statistics
    topic_count = Counter([item['topic'] for item in data])
    ratio = {k: v/len(data) for k, v in topic_count.items()}
    statistics['topic'] = {
        'count': topic_count,
        'ratio': ratio
    }

    # get subtopic statistics # need to count for None
    subtopic_count = Counter([item['subtopic'] for item in data if item['subtopic']])
    ratio = {k: v/len(data) for k, v in subtopic_count.items()}
    statistics['subtopic'] = {
        'count': subtopic_count,
        'ratio': ratio
    }

    # get length statistics, spans/all tokens
    length = [len(item['tokens']) for item in data]
    statistics['length'] = {
        'min': min(length),
        'max': max(length),
        'mean': sum(length) / len(data),
        'median': pd.Series(length).median()
    }

    # span length
    span_length = [len(span.split()) for item in data for span in item['highlight_spans']]
    statistics['span_length'] = {
        'min': min(span_length),
        'max': max(span_length),
        'mean': sum(span_length) / len(span_length),
        'median': pd.Series(span_length).median()
    }

    # number of spans
    num_span = [len(item['highlight_spans']) for item in data]

    # get the signal density statistics
    signal_density = [sum(item['highlight_probs']) / len(item['highlight_probs']) for item in data]
    statistics['signal_density'] = {
        'min': min(signal_density),
        'max': max(signal_density),
        'mean': sum(signal_density) / len(data),
        'median': pd.Series(signal_density).median()
    }

    # return dictionary
    return statistics


def slice_data(
        data_path: str, 
        ratio: List[float], 
        target_dir: str = None,
        seed: int = 666
    ):
    '''
    data_path: str
    ratio: ratio for training, validation, test, e.g. [0.8, 0.1, 0.1]
    target_dir: str
    seed: int
    '''
    data_path = Path(data_path)
    # set seed
    random.seed(seed)

    # get data
    data = read_jsonl(data_path)

    # shuffle data
    random.shuffle(data)

    # get number of each split
    total = len(data)
    train_num = int(total * ratio[0])
    test_num = int(total * ratio[2])
    valid_num = total - train_num - test_num

    # slice data
    data_splits = {
        'train': data[:train_num],
        'valid': data[train_num:train_num+valid_num],
        'test': data[train_num+valid_num:]
    }

    # assert total number of data
    assert len(data_splits['train']) + len(data_splits['valid']) + len(data_splits['test']) == total

    # save data
    if not target_dir:
        target_dir = f'{data_path.parent}/slice_seed{seed}'
    target_dir = Path(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    for i, split in enumerate(['train', 'valid', 'test']):
        split_data_path = target_dir / f'{split}.jsonl'
        with open(split_data_path, 'w') as f:
            for item in data_splits[i]:
                f.write(json.dumps(item) + '\n')

    return data_splits


def read_slice_data(data_dir: str):
    data_dir = Path(data_dir)
    data_splits = {}
    for split in ['train', 'valid', 'test']:
        split_data_path = data_dir / f'{split}.jsonl'
        data_splits[split] = read_jsonl(split_data_path)
    return data_splits


if __name__ == '__main__':
    data_path = 'annotation/annotated_result/all/aggregate_qlabels.jsonl'
    statistics = get_statistics(data_path)
    pprint(statistics)

