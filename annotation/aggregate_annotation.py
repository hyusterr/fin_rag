import json
import string
import argparse
from collections import OrderedDict

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

def aggregate_highlights(annotation_files, output_file, agreement_threshold=0):
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
    output = OrderedDict()
    for anno in annotations:
        for sample in anno:
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
                }
            span_tokens = [s.split() for s in sample["highlight"].split("|||")] # tokenized spans into tokens
            # because some of the spans will include punctuation, we need to normalize the tokens
            normalized_span_tokens = [[t.translate(str.maketrans('', '', string.punctuation)).lower() for t in s] for s in span_tokens]

            # get the id of the tokens
            span_already_checked = 0
            i = 0
            while i < len(tokens):
                if span_already_checked == len(span_tokens):
                    break

                if normalized_tokens[i] == normalized_span_tokens[span_already_checked][0]:
                    print(normalized_tokens[i:i+len(span_tokens[span_already_checked])], normalized_span_tokens[span_already_checked])
                    if normalized_tokens[i:i+len(normalized_span_tokens[span_already_checked])] == normalized_span_tokens[span_already_checked]:
                        for j in range(len(span_tokens[span_already_checked])):
                            output[sample["id"]]["highlight_probs"][i+j] += 1
                        i += len(span_tokens[span_already_checked])
                        span_already_checked += 1
                    else:
                        i += 1
                else:
                    i += 1

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
    for sample in output.values():
        sample["highlight_probs"] = [p/n_annotators for p in sample["highlight_probs"]]
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
        sample["highlight_spans"] = [sample["tokens"][start: end-1] for start, end in sample["highlight_spans"]]
        sample["type"] = max(sample["type"], key=sample["type"].count)
        sample["topic"] = max(sample["topic"], key=sample["topic"].count)
        sample["subtopic"] = max(sample["subtopic"], key=sample["subtopic"].count)

    with open(output_file, "w") as f:
        for sample in output.values():
            f.write(json.dumps(sample) + "\n")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aggregate annotation files")
    parser.add_argument("--annotation_files", "-as", nargs="+", help="Annotation files to aggregate")
    parser.add_argument("--output_file", "-o", help="Output file", default="output.jsonl")
    args = parser.parse_args()

    aggregate_highlights(args.annotation_files, args.output_file)
