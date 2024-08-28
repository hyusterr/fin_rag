import json
import random
import pandas as pd
from pathlib import Path
from pprint import pprint
from typing import List
from collections import Counter

from utils.utils import read_jsonl


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

