import json
import string
import argparse
from tqdm.auto import tqdm
from collections import OrderedDict, Counter, defaultdict
import numpy as np
from pprint import pprint

from utils import read_jsonl, read_trec, preprocess_annotations
from utils import TYPE_MAP, TOPIC_MAP, SUBTOPIC_MAP

def aggregate_highlights_complex(annotation_files, output_file):
    # tentative aggregate settings:
    # 1. based on agreement level of types:
    #     a. all agree on type --> use it as label
    #     b. some agree on type --> P(token|type); something like empirical bayes sum of probabilities?
    # 2. based on agreement level of tokens: what if we only use the tokens that have high agreement level?
    #     a. pick the highest agreed tokens (on 0 or 1) as "signal/non-signal center", which are an atomic-level annotation, and then expand the centers
    annotator_annotations, sample_id_set = preprocess_annotations(annotation_files)
    type_stats = Counter()
    result = defaultdict(Counter)
    total_num_of_tokens = 0
    for sample_id in sample_id_set:
        samples = [annotator_annotations[annotator_id][sample_id] for annotator_id in annotator_annotations.keys()]
        try:
            types = [s['signal_type'][0] for s in samples]
        except:
            print('[ERROR] signal_type not found: ', sample_id)
            type_stats['signal_type_not_found'] += 1
            continue
        type_agreement = len(set(types))
        type_stats[f"{type_agreement}_on_types"] += 1

        print(types)
        voting_label = np.mean([s['binary_labels'] for s in samples], axis=0)
        for tok, vot in zip(samples[0]['tokens'], voting_label):
            if vot == 0.0:
                result[f'{type_agreement}_on_types']['token_all_0'] += 1
                print(f'|{tok} {round(vot, 3)}|', end='\t')
            elif vot == 1.0 or vot > 0.6:
                result[f'{type_agreement}_on_types']['token_all_1'] += 1
                print(f'|{tok} {round(vot, 3)}|', end='\t')
            else:
                result[f'{type_agreement}_on_types']['token_mixed'] += 1
                print(f'{tok}', end='\t')
            total_num_of_tokens += 1
        print()

    print('Type stats:')
    for k, v in type_stats.items():
        print(f'{k}: {v} ({round(v/len(sample_id_set)*100, 2)}%)')
    print('Token stats:')
    print()
    print('Total number of tokens from vaild annotation:', total_num_of_tokens)
    for typ, counter in result.items():
        print(typ)
        for k, v in counter.items():
            print(f'{k}: {v} ({round(v/total_num_of_tokens*100, 2)}%)')

   


def aggregate_highlights_naive(annotation_files, output_file, agreement_threshold=0.5):
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
    annotations = [read_jsonl(file) for file in annotation_files]
    n_annotators = len(annotations)
    annotator_id = 0
    output = OrderedDict()
    for anno in annotations:
        annotator_id += 1
        for sample in tqdm(anno):
            # print(sample["id"])
            tokens = sample["text"].split() 
            normalized_tokens = [t.translate(str.maketrans('', '', string.punctuation)).lower() for t in tokens]    

            if sample["id"] not in output:
                # TODO: use Spacy to tokenize
                output[sample["id"]] = {
                    "id": sample["id"],
                    "text": sample["text"],
                    "tokens": tokens,
                    "highlight_probs": [0] * len(tokens),
                    "highlight_labels": [],
                    "highlight_spans": [],
                    "type": [],
                    "topic": [],
                    "subtopic": [],
                    "annotator_id": []
                }

            # record the annotator id
            if annotator_id not in output[sample["id"]]["annotator_id"]:
                output[sample["id"]]["annotator_id"].append(annotator_id)
            else:
                print(f"Duplicate annotation for {sample['id']} by annotator {annotator_id}, keep the first one.")
                continue


            if sample["highlight"] != "":
                span_tokens = [s.split() for s in sample["highlight"].split("|||")] # tokenized spans into tokens
                # filter out empty spans
                span_tokens = [s for s in span_tokens if s != []]
                # because some of the spans will include punctuation, we need to normalize the tokens
                normalized_span_tokens = [[t.translate(str.maketrans('', '', string.punctuation)).lower() for t in s] for s in span_tokens] # span tokens without punctuation


                # get the id of the tokens
                span_already_checked = 0
                i = 0
                while i < len(tokens):
                    if span_already_checked == len(span_tokens):
                        break
                    
                    if normalized_tokens[i] == normalized_span_tokens[span_already_checked][0]:
                        # print(normalized_tokens[i:i+len(span_tokens[span_already_checked])], normalized_span_tokens[span_already_checked])
                        # BUG: there might be highlights = "||| |||"
                        if normalized_tokens[i:i+len(normalized_span_tokens[span_already_checked])] == normalized_span_tokens[span_already_checked]:
                            for j in range(len(span_tokens[span_already_checked])):
                                output[sample["id"]]["highlight_probs"][i+j] += 1
                            i += len(span_tokens[span_already_checked])
                            span_already_checked += 1
                        else:
                            i += 1
                    else:
                        i += 1
            else: # no highlight
                for i in range(len(tokens)):
                    output[sample["id"]]["highlight_probs"][i] += 0

            # collect type and topic
            type_ = max(sample["type"], key=sample["type"].get)
            topic_ = max(sample["topic"], key=sample["topic"].get)
            if sample["topic"][topic_] > 1:
                subtopic_ = topic_ + "-" + str(sample["topic"][topic_])
            else:
                subtopic_ = ""
            output[sample["id"]]["type"].append(type_)
            output[sample["id"]]["topic"].append(topic_)
            output[sample["id"]]["subtopic"].append(subtopic_)
    
    
    # calculate the average of highlight_probs
    validation_stats = {
        "token_agreement": [],
        "type_agreement": [],
    }
    for sample in output.values():
        # BUG: duplicate highlights under an annotator, leads to probs > 1

        # check agreement
        all_0_count = sum([1 for p in sample["highlight_probs"] if p == 0])
        all_1_count = sum([1 for p in sample["highlight_probs"] if p == n_annotators])
        all_agree_count = all_1_count + all_0_count
        token_agreement = all_agree_count / len(sample["highlight_probs"])
        validation_stats["token_agreement"].append(token_agreement)

        type_agreement = len(set(sample["type"])) == 1
        validation_stats["type_agreement"].append(type_agreement)

        sample["highlight_probs"] = [p/n_annotators for p in sample["highlight_probs"]]
        assert all([p <= 1 for p in sample["highlight_probs"]])

        sample["highlight_labels"] = [1 if p > agreement_threshold else 0 for p in sample["highlight_probs"]]
        # get the spans
        i = 0
        while i < len(sample["highlight_labels"]):
            if sample["highlight_labels"][i] == 1:
                start = i
                while i < len(sample["highlight_labels"]) and sample["highlight_labels"][i] == 1:
                    i += 1
                end = i
                sample["highlight_spans"].append((start, end))
            else:
                i += 1
        sample["highlight_spans"] = [" ".join(sample["tokens"][start: end-1]) for start, end in sample["highlight_spans"]]
        assert len(sample["type"]) == n_annotators
        sample["type"] = max(sample["type"], key=sample["type"].count)

        assert len(sample["topic"]) == n_annotators
        sample["topic"] = max(sample["topic"], key=sample["topic"].count)

        assert len(sample["subtopic"]) == n_annotators
        sample["subtopic"] = max(sample["subtopic"], key=sample["subtopic"].count)

    with open(output_file, "w") as f:
        for sample in output.values():
            f.write(json.dumps(sample) + "\n")

    print("Agreement stats:")
    print(f"Token agreement: {sum(validation_stats['token_agreement']) / len(validation_stats['token_agreement'])}")
    print(f"Type agreement: {sum(validation_stats['type_agreement']) / len(validation_stats['type_agreement'])}")


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
    args = parser.parse_args()

    aggregate_highlights_complex(args.annotation_files, args.output_file)
    
    '''
    if args.task == "retrieval":
        aggregate_retrieval(args.annotation_files, args.output_file)
    elif args.task == "highlight":
        aggregate_highlights(args.annotation_files, args.output_file, args.agreement_threshold)
    '''
