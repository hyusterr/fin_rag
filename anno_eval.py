# evaluate the annotation quality of the dataset
import string
from typing import List
from annotation.aggregate_annotation import read_jsonl, TOPIC_MAP, SUBTOPIC_MAP, TYPE_MAP
import argparse
from collections import defaultdict, OrderedDict
from itertools import combinations, permutations, product
import pandas as pd
import numpy as np
from statsmodels.stats.inter_rater import fleiss_kappa, aggregate_raters



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

# use id to prevent token are accidentally matched
def exact_span_agreement(span1: List[int], span2: List[int]):
    return int(span1 == span2)

def overlap_span_agreement(span1: List[int], span2: List[int]):
    # TODO: check if this is correct
    # I guess should use token id instead of token itself
    return int(len(set(span1) & set(span2)) > 0)

def one_bound_span_agreement(span1: List[int], span2: List[int]):
    # TODO: check if this is correct
    return int(span1[0] == span2[0] or span1[-1] == span2[-1])


def evaluate_annotation(annotation_files):
    annotator_annotations, sample_id_set = preprocess_annotations(annotation_files)
    annotators = list(annotator_annotations.keys())

    # check for bugs
    for annotator, annotation in annotator_annotations.items():
        # missing samples
        missing_samples = sample_id_set - set(annotation.keys())
        if len(missing_samples) != 0:
            print(f'[MISSING SAMPLE] {annotator}, {missing_samples}')
        # extra samples
        extra_samples = set(annotation.keys()) - sample_id_set
        if len(extra_samples) != 0:
            print(f'[EXTRA SAMPLE] {annotator}, {extra_samples}')
        
        # check for multiple signal types, topics, sub_topics
        for sid, sample in annotation.items():
            # can only have 1 type of signal
            if len(sample['signal_type']) > 1:
                print(f'[MULTIPLE SIGNAL] {annotator}, {sid}')
            signal_type = TYPE_MAP[sample['signal_type'][0]] if len(sample['signal_type']) == 1 else None
            
            sample['SIGNAL'] = signal_type

            # if signal_type = [0], then the sample should not have any highlights
            # print(sample['signal_type'], sum(sample['binary_labels']))

            if len(sample['signal_type']) == 0:
                print(f'[NO SIGNAL ANNOTATION] {annotator}, {sid}')

            elif sample['signal_type'][0] == '0' and sum(sample['binary_labels']) != 0:
                print(f'[TRIVIAL BUT HAS HIGHLIGHT] {annotator}, {sid}')
            elif sample['signal_type'][0] != '0' and sum(sample['binary_labels']) == 0:
                print(f'[SIGNAL BUT NO HIGHLIGHT] {annotator}, {sid}')

            # can be multiple topics
            # check if # of topic != 1
            if len(sample['topic']) != 1:
                print(f'[MULTIPLE TOPIC] {annotator}, {sid}')
            topics = [TOPIC_MAP[t] for t in sample['topic']]
            sample['TOPIC'] = topics


            # check if # of sub_topic <= 1
            if len(sample['sub_topic']) > 1:
                print(f'[MULTIPLE SUBTOPIC] {annotator}, {sid}')
            sub_topic = [SUBTOPIC_MAP[t] for t in sample['sub_topic']]
            sample['SUBTOPIC'] = sub_topic

    sample_id_list = list(sample_id_set)
    n_samples = len(sample_id_list)
    inter_annotator_metrics = defaultdict(list)
    agreement_2_sids = []
    # check for agreement
    # inter-annotator agreement, loop over samples
    for id_ in sample_id_list:
        sample_from_annotators = [annotator_annotations[a][id_] for a in annotator_annotations.keys()]
        # for s in sample_from_annotators:
        #     print(s)
        # token-level agreement
        # strict agreement: all annotators agree on the same label
        strict_agreement_on_tokens = 0
        no_agreement_on_tokens = 0 
        len_tokens = len(sample_from_annotators[0]['binary_labels'])
        for i in range(len(sample_from_annotators[0]['binary_labels'])):
            # iterate over tokens
            labels = [s['binary_labels'][i] for s in sample_from_annotators]
            # highlights
            if len(set(labels)) == 1:
                strict_agreement_on_tokens += 1
            if len(set(labels)) == 2: # at most 2 labels
                no_agreement_on_tokens += 1
        strict_agreement_on_tokens /= len_tokens
        no_agreement_on_tokens /= len_tokens
        inter_annotator_metrics['strict_agreement_on_tokens'].append(strict_agreement_on_tokens)
        inter_annotator_metrics['no_agreement_on_tokens'].append(no_agreement_on_tokens)

        # span-level agreement
        annotator_pairs = list(permutations(range(len(annotators)), 2))
        for a1, a2 in annotator_pairs:
            # List of List[int]
            span1_ids = sample_from_annotators[a1]['span_ids']
            span2_ids = sample_from_annotators[a2]['span_ids']
            if len(span1_ids) == 0 or len(span2_ids) == 0:
                # NOTE: this will only count the number of samples that have highlights
                continue

            for span1, span2 in product(span1_ids, span2_ids):
                exact_agreement = exact_span_agreement(span1, span2)
                overlap_agreement = overlap_span_agreement(span1, span2)
                one_bound_agreement = one_bound_span_agreement(span1, span2)

                inter_annotator_metrics['span_exact_agreement'].append(exact_agreement)
                inter_annotator_metrics['span_one_bound_agreement'].append(one_bound_agreement)
                inter_annotator_metrics['span_overlap_agreement'].append(overlap_agreement)
        

        # iterate over sample
        types = [s['SIGNAL'] for s in sample_from_annotators]
        if len(set(types)) == 1:
            inter_annotator_metrics['strict_agreement_on_types'].append(1)
            inter_annotator_metrics['no_agreement_on_types'].append(0)
            inter_annotator_metrics['2_agreement_on_types'].append(0)
        elif len(set(types)) == len(types):
            inter_annotator_metrics['no_agreement_on_types'].append(1)
            inter_annotator_metrics['strict_agreement_on_types'].append(0)
            inter_annotator_metrics['2_agreement_on_types'].append(0)
        else:
            agreement_2_sids.append(id_)
            inter_annotator_metrics['2_agreement_on_types'].append(1)
            inter_annotator_metrics['strict_agreement_on_types'].append(0)
            inter_annotator_metrics['no_agreement_on_types'].append(0)
            print(f'[2 AGREEMENT] {id_}')
            print(sample_from_annotators[0]['binary_labels'], sample_from_annotators[0]['SIGNAL'], annotators[0], sep='\t')
            print(sample_from_annotators[1]['binary_labels'], sample_from_annotators[1]['SIGNAL'], annotators[1], sep='\t')
            print(sample_from_annotators[2]['binary_labels'], sample_from_annotators[2]['SIGNAL'], annotators[2], sep='\t')

    # concat all token labels from each annotator, seperate by annotator
    df_all_tokens = pd.DataFrame({a: np.concatenate([annotator_annotations[a][sid]['binary_labels'] for sid in sample_id_list]) for a in annotator_annotations.keys()})
    print(df_all_tokens.shape)
    df_all_tokens.to_csv('all_tokens.csv')
    arr, categories = aggregate_raters(df_all_tokens)
    print(arr.shape)
    print(categories)
    kappa = fleiss_kappa(arr, method='fleiss')
    inter_annotator_metrics['fleiss_kappa_all_tokens'].append(kappa)
    
    '''
    df_all_types = pd.DataFrame({a: [annotator_annotations[a][sid]['SIGNAL'] for sid in sample_id_list] for a in annotator_annotations.keys()})
    arr, categories = aggregate_raters(df_all_types)
    kappa = fleiss_kappa(arr, method='fleiss')
    inter_annotator_metrics['fleiss_kappa_all_types'].append(kappa)
    
    
    df_2_agreement_tokens = pd.DataFrame({a: np.concatenate([annotator_annotations[a][sid]['binary_labels'] for sid in agreement_2_sids]) for a in annotator_annotations.keys()})
    arr, categories = aggregate_raters(df_2_agreement_tokens)
    kappa = fleiss_kappa(arr, method='fleiss')
    inter_annotator_metrics['fleiss_kappa_2_agreement_tokens'].append(kappa)
    '''

    for metric, values in inter_annotator_metrics.items():
        print(f'{metric}: {np.nanmean(values)}') 


    # soft agreement, see: https://en.innovatiana.com/post/inter-annotator-agreement
    # Fleiss' kappa on highlights

    # intra-class correlation on highlights

    # Krippendorff alpha on type

    # Krippendorff alpha on topic

    # intra-annotator agreement

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--annotation_files', '-as', type=str, nargs='+', help='List of annotation files')
    args = parser.parse_args()
    evaluate_annotation(args.annotation_files)
