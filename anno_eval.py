# evaluate the annotation quality of the dataset
from annotation.aggregate_annotation import read_jsonl, TOPIC_MAP, SUBTOPIC_MAP, TYPE_MAP
import argparse
from collections import defaultdict
import pandas as pd
import numpy as np
from statsmodels.stats.inter_rater import fleiss_kappa, aggregate_raters

def preprocess_sample(sample):
    sample_id = sample['id']
    text = sample['text']
    tokens = text.split()
    binary_labels = [0] * len(tokens)
    signal_type = [k for k, v in sample['type'].items() if v == 1]
    topic = [k for k, v in sample['topic'].items() if v != 0]
    sub_topic = [f'{k}-{v}' for k, v in sample['topic'].items() if v not in [0, 1]]
    if len(sample['highlight']) != 0:
        highlight_spans = sample['highlight'].split(' ||| ')
        span_tokens = [s.strip().split() for s in highlight_spans] # list of list of tokens
        span_tokens = [s for s in span_tokens if len(s) > 0] # filter out empty spans
        
        span_already_checked = 0
        i = 0
        while i < len(tokens):
            if span_already_checked == len(span_tokens):
                break

            if tokens[i] == span_tokens[span_already_checked][0]:
                if tokens[i:i+len(span_tokens[span_already_checked])] == span_tokens[span_already_checked]:
                    for j in range(i, i+len(span_tokens[span_already_checked])):
                        binary_labels[j] = 1
                    i += len(span_tokens[span_already_checked])
                    span_already_checked += 1
                else:
                    i += 1
            else:
                i += 1
    
    return {
        sample_id: {
            'text': text,
            'tokens': tokens,
            'binary_labels': binary_labels,
            'signal_type': signal_type,
            'topic': topic,
            'sub_topic': sub_topic
        }
    }

def preprocess_annotations(annotation_files):
    annotations = [read_jsonl(f) for f in annotation_files]
    annotators = [f.split('/')[-1].split('.')[0].split('_')[0] for f in annotation_files]
    sample_size = len(annotations[0])

    annotator_annotations = {a: dict() for a in annotators}
    sample_id_set = set()
    for annotator, annotation in zip(annotators, annotations):
        for sample in annotation:
            preprocessed_sample = preprocess_sample(sample)
            annotator_annotations[annotator].update(preprocessed_sample)
            sample_id_set.update(preprocessed_sample.keys())

    return annotator_annotations, sample_id_set


def evaluate_annotation(annotation_files):
    annotator_annotations, sample_id_set = preprocess_annotations(annotation_files)

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
    # check for agreement
    # inter-annotator agreement, loop over samples
    for id_ in sample_id_list:
        sample_from_annotators = [annotator_annotations[a][id_] for a in annotator_annotations.keys()]
        # for s in sample_from_annotators:
        #     print(s)
        
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
            inter_annotator_metrics['2_agreement_on_types'].append(1)
            inter_annotator_metrics['strict_agreement_on_types'].append(0)
            inter_annotator_metrics['no_agreement_on_types'].append(0)

        df_kappa = pd.DataFrame([s['binary_labels'] for s in sample_from_annotators]).T
        arr, categories = aggregate_raters(df_kappa)
        kappa = fleiss_kappa(arr, method='fleiss')
        if np.isnan(kappa):
            print(f'kappa is nan for {id_}')
            print([s['binary_labels'] for s in sample_from_annotators])
        inter_annotator_metrics['fleiss_kappa'].append(kappa)

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
