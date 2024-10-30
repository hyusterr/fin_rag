import json
import string
import argparse
from tqdm.auto import tqdm
from collections import OrderedDict, Counter, defaultdict
import numpy as np
import pandas as pd
from pprint import pprint
from termcolor import colored, cprint

from utils import read_jsonl, read_trec, preprocess_annotations
from utils import TYPE_MAP, TOPIC_MAP, SUBTOPIC_MAP

import random
random.seed(42)

NUM_OF_TEST = 100

def print_colored_highlight(labels, tokens):
    for i, label in enumerate(labels):
        if label == 1:
            cprint(tokens[i], 'white', 'on_yellow', end=' ')
        elif label == 0:
            cprint(tokens[i], 'light_grey', end=' ')
        else:
            cprint(tokens[i], 'light_blue', end=' ')
    print()

def get_highlight_spans(labels, tokens):
    spans = []
    span_ids = []
    i = 0
    while i < len(labels):
        if labels[i] == 1:
            start = i
            tmp_sid = []
            while i < len(labels) and labels[i] == 1:
                tmp_sid.append(i)
                i += 1
                # when jump out of the inner while loop, i is the first index that is not 1
            span_ids.append(tmp_sid)
            end = i
            spans.append(" ".join(tokens[start: end]))
        else:
            i += 1
    return {"spans": spans, "span_ids": span_ids}

def aggregate_highlights(annotation_files, output_file, agreement_threshold=0.5, verbose=False):
    # tentative aggregate settings:
    # 0. naive: just average the probabilities by tokens
    # 1. based on agreement level of types:
    #     a. all agree on type --> use it as label
    #     b. some agree on type --> P(token|type); something like empirical bayes sum of probabilities?
    # 2. based on agreement level of tokens: what if we only use the tokens that have high agreement level?
    #     a. pick the highest agreed tokens (on 0 or 1) as "signal/non-signal center", which are an atomic-level annotation, and then expand the centers

    # initialize
    annotator_annotations, sample_id_set = preprocess_annotations(annotation_files)
    type_stats = Counter()
    signal_stats = defaultdict(Counter)
    total_num_of_tokens = 0
    result = []

    for sample_id in sample_id_set:
        samples = [annotator_annotations[annotator_id][sample_id] for annotator_id in annotator_annotations.keys()]
        tokens = samples[0]['tokens']
        texts = samples[0]['text']
        types = [s['signal_type'][0] if s['signal_type'] else None for s in samples]
        if None in types:
            print('[ERROR] signal_type not found: ', sample_id)
            type_stats['signal_type_not_found'] += 1
            
        topics = [s['topic'][0] if s['topic'] else None for s in samples]
        if None in topics:
            print('[ERROR] topic not found: ', sample_id)
            type_stats['topic_not_found'] += 1
        subtopics = [s['subtopic'][0] if s['subtopic'] else 'None' for s in samples]

        # collect information about signal types
        type_agreement = len(set(types)) # how many types are there
        type_stats[f"{type_agreement}_on_types"] += 1
        types_counter = Counter(types)
        voted_type = max(types_counter, key=types_counter.get)
        voted_topic = max(Counter(topics), key=Counter(topics).get)
        voted_subtopic = max(Counter(subtopics), key=Counter(subtopics).get)
        
        
        # all different types of span aggregation
        voting_label = np.mean([s['binary_labels'] for s in samples], axis=0)
        naive_label = [1 if v > agreement_threshold else 0 for v in voting_label]
        loose_label = [1 if v != 0 else 0 for v in voting_label]
        strict_label = [int(v) if v == 1 or v == 0 else None for v in voting_label]
        harsh_label = [1 if v == 1 else 0 for v in voting_label]
        complex_label, marker, ticker = [], 0, []
        for i, label in enumerate(strict_label):
            if label is not None:
                if ticker:
                    if marker and label:
                        complex_label.extend([1] * len(ticker))
                    else:
                        complex_label.extend([0] * len(ticker))
                    ticker = []
                complex_label.append(label)
                marker = label
            else:
                ticker.append(i)
        if ticker: # deal with the last part
            complex_label.extend([0] * len(ticker))
        assert len(voting_label) == len(naive_label) == len(loose_label) == len(strict_label) == len(complex_label) == len(harsh_label), f"Length not equal: [VOTE]{len(voting_label)}, [NAIVE]{len(naive_label)}, [LOOSE]{len(loose_label)}, [STRICT]{len(strict_label)}, [COMPLEX]{len(complex_label)}, [HARSH]{len(harsh_label)}"

        # collect output
        this_sample = {
            "sample_id": sample_id,
            "text": texts,
            "tokens": tokens,
            "types": voted_type,
            "topics": voted_topic,
            "subtopics": voted_subtopic,
            "highlight_probs": [round(v, 4) for v in voting_label],
            "naive_aggregation": {
                "label": naive_label,
                "highlights": get_highlight_spans(naive_label, tokens) # spans, span_ids
            },
            "loose_aggregation": {
                "label": loose_label,
                "highlights": get_highlight_spans(loose_label, tokens)
            },
            "strict_aggregation": {
                "label": strict_label,
                "highlights": get_highlight_spans(strict_label, tokens)
            },
            "harsh_aggregation": {
                "label": harsh_label,
                "highlights": get_highlight_spans(harsh_label, tokens)
            },
            "complex_aggregation": {
                "label": complex_label,
                "highlights": get_highlight_spans(complex_label, tokens)
            },
        }
        result.append(this_sample)


        # [TODO] collect statistics
        num_of_tokens = len(tokens)
        total_num_of_tokens += num_of_tokens
        for method in ["naive", "loose", "strict", "harsh", "complex"]:
            num_of_highlight_spans = len(this_sample[f"{method}_aggregation"]['highlights']['spans'])
            replace_output_label = [v if v is not None else 'None' for v in this_sample[f"{method}_aggregation"]['label']]
            token_type_couter = Counter(replace_output_label)

            signal_stats[method]['num_of_highlight_spans'] += num_of_highlight_spans
            signal_stats[method]['num_of_highlight_tokens'] += sum([1 for v in this_sample[f"{method}_aggregation"]['label'] if v == 1])
            for k, v in token_type_couter.items():
                signal_stats[method]['token_' + str(k)] += v / num_of_tokens

       
        # visualize the annotation
        if verbose:
            print(f"Sample ID: {sample_id}")
            print(f"Types: {types_counter}")
            for i, s in enumerate(samples):
                print(f"Annotator {i}:")
                print_colored_highlight(s['binary_labels'], tokens)
            print('[voting]:', [round(v, 3) for v in voting_label])
            print_colored_highlight(voting_label, tokens)
            print('[naive]:', naive_label)
            print_colored_highlight(naive_label, tokens)
            print('[loose]:', loose_label)
            print_colored_highlight(loose_label, tokens)
            print('[strict]:', strict_label)
            print_colored_highlight(strict_label, tokens)
            print('[harsh]:', harsh_label)
            print_colored_highlight(harsh_label, tokens)
            print('[complex]:', complex_label)
            print_colored_highlight(complex_label, tokens)
            print('='*50)
            break


    # TODO: figure out what statistics to collect
    # output statistics
    print('Type stats:')
    for k, v in type_stats.items():
        print(f'{k}: {v} ({round(v/len(sample_id_set)*100, 2)}%)')
    span_token_stats_dict = {}
    for method in ["naive", "loose", "strict", "harsh", "complex"]:
        num_of_highlight_spans = signal_stats[method]['num_of_highlight_spans']
        num_of_highlight_tokens = signal_stats[method]['num_of_highlight_tokens']
        average_num_of_highlight_spans = num_of_highlight_spans / len(sample_id_set)
        average_num_of_highlight_tokens = num_of_highlight_tokens / len(sample_id_set)
        average_token_in_a_highlight_span = num_of_highlight_tokens / num_of_highlight_spans
        span_token_stats_dict[method] = {
            "num of highlight spans": round(num_of_highlight_spans, 4),
            "num of highlight tokens": round(num_of_highlight_tokens, 4),
            "average num of highlight spans": round(average_num_of_highlight_spans, 4),
            "average num of highlight tokens": round(average_num_of_highlight_tokens, 4),
            "average token in a highlight span": round(average_token_in_a_highlight_span, 4),
        }

        for k, v in signal_stats[method].items():
            if k not in ['num_of_highlight_spans', 'num_of_highlight_tokens']:
                span_token_stats_dict[method][f'average ratio of {k}'] = round(v/len(sample_id_set), 4) * 100

    # change the statistics to df
    print('Span token stats:')
    pprint(span_token_stats_dict)
    print("average token in a sample:", total_num_of_tokens / len(sample_id_set))
    pd.DataFrame(span_token_stats_dict).to_csv('span_token_stats.csv')
    
    # print('Total number of tokens from vaild annotation:', total_num_of_tokens)

    # output result
    num_of_test = NUM_OF_TEST
    test_filename = output_file.replace('.jsonl', '_test.jsonl')
    test_id_filename = output_file.replace('.jsonl', '_test_ids.txt')
    train_filename = output_file.replace('.jsonl', '_train.jsonl')
    sample_ids = [s['sample_id'] for s in result]
    test_ids = random.sample(sample_ids, num_of_test)
    with open(test_filename, "w") as f:
        for r in result:
            if r['sample_id'] in test_ids:
                f.write(json.dumps(r) + "\n")

    with open(test_id_filename, "w") as f:
        for i in test_ids:
            f.write(i + "\n")

    with open(train_filename, "w") as f:
        for r in result:
            if r['sample_id'] not in test_ids:
                f.write(json.dumps(r) + "\n")

    with open(output_file, "w") as f:
        for r in result:
            f.write(json.dumps(r) + "\n")


'''
    annotation_files: list of annotation files
    - FORMAT (of a line): {
        "id": ID,
        "text": TEXT, 
        "highlight": SPAN1 ||| SPAN2 ||| ...,
        "type": {"0": 0, "1": 1, "2": 0, "3": 0, "4": 0}
        "topic": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0 ...}
    }
    output_file: output file
    - FORMAT (of a line): {
        "id": ID,
        "text": TEXT,
        "tokens": TOKENS, # list of all tokens, by split on space or Spacy
        "highlight_probs": [0, 1, 0.66, ...], # average of different annotations, len = len(tokens)
        "highlight_labels": [0, 1, 1, ...], # probability > threshold, len = len(tokens)
        "highlight_spans: [SPAN1, SPAN2, ...], # list of all highlights spans base on labels
        "type": TYPE, # majority vote
        "topic": TOPIC, # majority vote
'''
# print(f"Duplicate annotation for {sample['id']} by annotator {annotator_id}, keep the first one.")
# normalized_span_tokens = [[t.translate(str.maketrans('', '', string.punctuation)).lower() for t in s] for s in span_tokens] # span tokens without punctuation
# BUG: there might be highlights = "||| |||"
# BUG: duplicate highlights under an annotator, leads to probs > 1


def aggregate_retrieval(annotation_files, output_file):
    annotations = [read_trec(file) for file in annotation_files]
    n_annotators = len(annotations)
    output = OrderedDict()
    for anno in annotations:
        for sample in anno:
            target_id, _, doc_id, score = sample
            score = float(score)
            if (target_id, doc_id) not in output:
                output[(target_id, doc_id)] = []
            output[(target_id, doc_id)].append(score)

    # get average score and output
    with open(output_file, "w") as f:
        for (target_id, doc_id), score in output.items():
            # trec qrel format: qid 0 docno relevance; see: https://github.com/joaopalotti/trectools
            if len(score) != n_annotators:
                print((target_id, doc_id), f"Number of annotators is not consistent: {len(score)} != {n_annotators}")
            mean = sum(score) / len(score)
            f.write(f"{target_id} 0 {doc_id} {round(mean, 4)}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aggregate annotation files")
    parser.add_argument("--annotation_files", "-as", nargs="+", help="Annotation files to aggregate")
    parser.add_argument("--output_file", "-o", help="Output file", default="output.jsonl")
    parser.add_argument("--agreement_threshold", "-at", type=float, help="Threshold for agreement", default=0.5)
    parser.add_argument("--task", "-t", help="Task to aggregate", choices=["highlight", "retrieval"], default="highlight")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print verbose output")
    args = parser.parse_args()

    
    if args.task == "retrieval":
        aggregate_retrieval(args.annotation_files, args.output_file)
    elif args.task == "highlight":
        aggregate_highlights(args.annotation_files, args.output_file, agreement_threshold=args.agreement_threshold, verbose=args.verbose)
