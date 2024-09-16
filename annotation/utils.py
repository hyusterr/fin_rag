import json
import string
import argparse
from typing import List
from tqdm.auto import tqdm
from collections import OrderedDict, defaultdict, Counter
from itertools import combinations, permutations, product

import pandas as pd
import numpy as np
from statsmodels.stats.inter_rater import fleiss_kappa, aggregate_raters


TOPIC_MAP = {
        "1": "Overview",
        "2": "Industry",
        "3": "Risk",
        "4": "Legal",
        "5": "Financial Status",
        "6": "Strategy",
        "7": "Operation",
        "0": "Others",
}

SUBTOPIC_MAP = {
        "3-2": "Government",
        "7-2": "Capital",
        "7-3": "Accounting",
}

TYPE_MAP = {
        "0": "trivial",
        "1": "company-specific",
        "2": "change/action",
        "3": "reason",
        "4": "redirect",
}

def read_jsonl(file):
    '''
    file: file to read
    '''
    with open(file, "r") as f:
        return [json.loads(line) for line in f]

def read_trec(file):
    '''
    file: file to read
    '''
    with open(file, "r") as f:
        return [line.strip().split() for line in f]



def preprocess_sample(sample):
    sample_id = sample['id']
    text = sample['text']
    tokens = text.split()
    normalized_tokens = [t.translate(str.maketrans('', '', string.punctuation)).lower() for t in tokens]    
    binary_labels = [0] * len(tokens)
    signal_type = [k for k, v in sample['type'].items() if v == 1]
    topic = [k for k, v in sample['topic'].items() if v != 0]
    sub_topic = [f'{k}-{v}' for k, v in sample['topic'].items() if v not in [0, 1]]
    span_ids = []

    if len(sample['highlight']) != 0:
        highlight_spans = sample['highlight'].split('|||')
        span_tokens = [s.strip().split() for s in highlight_spans] # list of list of tokens
        span_tokens = [s for s in span_tokens if len(s) > 0] # filter out empty spans
        normalized_span_tokens = [[t.translate(str.maketrans('', '', string.punctuation)).lower() for t in s] for s in span_tokens] # span tokens without punctuation
        # print(normalized_span_tokens)
        # print(span_tokens)

        span_already_checked = 0
        i = 0
        while i < len(tokens):
            if span_already_checked == len(span_tokens):
                break

            if normalized_tokens[i] == normalized_span_tokens[span_already_checked][0]:
                for j in range(i, i+len(span_tokens[span_already_checked])):
                    '''
                    print(j, i, j-i)
                    print(len(normalized_tokens), len(tokens))
                    print(len(normalized_span_tokens[span_already_checked]))
                    '''
                    # WTF is happening here?
                    if j - i >= len(normalized_span_tokens[span_already_checked]) or j >= len(normalized_tokens):
                        break
                    if normalized_tokens[j] == normalized_span_tokens[span_already_checked][j-i]:
                        binary_labels[j] = 1
                i += len(span_tokens[span_already_checked])
                span_already_checked += 1
            else:
                i += 1

        span_tmp = []
        for index, label in enumerate(binary_labels):
            if label == 1:
                span_tmp.append(index)
            elif len(span_tmp) != 0:
                span_ids.append(span_tmp)
                span_tmp = []

    
    
    return {
        sample_id: {
            'text': text,
            'tokens': tokens,
            'binary_labels': binary_labels,
            'signal_type': signal_type,
            'topic': topic,
            'sub_topic': sub_topic,
            'span_ids': span_ids
        }
    }

def preprocess_annotations(annotation_files):
    annotations = [read_jsonl(f) for f in annotation_files]
    annotators = [f.split('/')[-1].split('.')[0].split('_')[0] for f in annotation_files]
    sample_size = len(annotations[0])

    annotator_annotations = OrderedDict({a: OrderedDict() for a in annotators})
    sample_id_set = set()
    for annotator, annotation in zip(annotators, annotations):
        for sample in annotation:
            preprocessed_sample = preprocess_sample(sample)
            annotator_annotations[annotator].update(preprocessed_sample)
            sample_id_set.update(preprocessed_sample.keys())

    return annotator_annotations, sample_id_set
