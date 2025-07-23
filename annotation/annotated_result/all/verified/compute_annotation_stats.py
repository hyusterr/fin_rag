#!/usr/bin/env python3
"""
Script to compute annotation statistics:
1. Average tokens per paragraph
2. Average number of highlighted spans per paragraph
3. Average tokens in highlighted spans
4. Average highlighted tokens per paragraph
5. Average pairwise Cohen's kappa
6. Krippendorff's alpha (nominal)
Usage:
    python compute_annotation_stats.py CE_qlabels.jsonl YC_qlabels.jsonl YX_qlabels.jsonl
"""

import sys
import json
import numpy as np
from sklearn.metrics import cohen_kappa_score
import pandas as pd

def load_jsonl(path):
    """Load JSONL file, return list of dicts."""
    with open(path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]

def krippendorff_alpha_binary(label_matrix):
    """
    Compute Krippendorff's alpha for nominal binary data.
    label_matrix: 2D numpy array of shape (n_annotators, n_items), entries 0 or 1.
    """
    n_annotators, n_items = label_matrix.shape
    counts = np.array([np.bincount(label_matrix[:,j], minlength=2) for j in range(n_items)])
    n0 = counts[:,0]
    n1 = counts[:,1]
    total_disagree_pairs = np.sum(n0 * n1)
    pairs_per_item = n_annotators * (n_annotators - 1) / 2
    Do = (total_disagree_pairs / pairs_per_item) / n_items

    total_labels = label_matrix.size
    p0 = np.sum(label_matrix == 0) / total_labels
    p1 = np.sum(label_matrix == 1) / total_labels
    De = 2 * p0 * p1

    return 1.0 - Do/De

def compute_stats(file_paths):
    ann_data = [load_jsonl(fp) for fp in file_paths]
    n_annotators = len(ann_data)

    para_token_counts = []
    span_counts = []
    span_token_counts = []
    highlight_token_counts = []
    label_vectors = [[] for _ in range(n_annotators)]

    # assume all files align on paragraphs
    n_paras = len(ann_data[0])
    for idx in range(n_paras):
        tokens = ann_data[0][idx]['text'].split()
        para_token_counts.append(len(tokens))

        for ai in range(n_annotators):
            hl = ann_data[ai][idx].get('highlight', '')
            spans = [s.strip() for s in hl.split('|||')] if hl else []

            # spans
            span_counts.append(len(spans))
            if spans:
                for s in spans:
                    span_token_counts.append(len(s.split()))
            else:
                span_token_counts.append(0)

            # token-level labels
            labels = [int(any(tok in span for span in spans)) for tok in tokens]
            label_vectors[ai].extend(labels)

            # highlighted tokens in this paragraph
            highlight_token_counts.append(sum(labels))

    # compute averages
    avg_para_tokens = np.mean(para_token_counts)
    avg_spans = np.mean(span_counts)
    avg_span_tokens = np.mean(span_token_counts)
    avg_highlight_tokens = np.mean(highlight_token_counts)

    # pairwise Cohen's kappa
    kappas = []
    for i in range(n_annotators):
        for j in range(i+1, n_annotators):
            kappas.append(cohen_kappa_score(label_vectors[i], label_vectors[j]))
    avg_cohen = np.mean(kappas)

    # Krippendorff's alpha
    label_matrix = np.array(label_vectors)
    alpha = krippendorff_alpha_binary(label_matrix)

    # assemble DataFrame
    df = pd.DataFrame({
        'Metric': [
            'Avg tokens per paragraph',
            'Avg spans per paragraph',
            'Avg tokens per span',
            'Avg highlighted tokens per paragraph',
            "Avg Cohen's kappa",
            "Krippendorff's alpha"
        ],
        'Value': [
            round(avg_para_tokens, 2),
            round(avg_spans, 2),
            round(avg_span_tokens, 2),
            round(avg_highlight_tokens, 2),
            round(avg_cohen, 3),
            round(alpha, 3)
        ]
    })
    return df

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python compute_annotation_stats.py CE_qlabels.jsonl YC_qlabels.jsonl YX_qlabels.jsonl")
        sys.exit(1)
    df_stats = compute_stats(sys.argv[1:])
    print(df_stats.to_string(index=False))

