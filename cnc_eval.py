# input: trec format file
# 20220222_10-K_1090727_part2_item7_para100 Q0 20180221_10-K_1090727_part2_item7_para107 1 84.35596466064453 title-year2018_2022-filtered_out-cik1090727-year2022_2022-item7
# output: evaluation metrics

import pandas as pd
import argparse
from collections import defaultdict
from pathlib import Path
from utils.utils import retrieve_paragraph_from_docid, read_jsonl
from highlighter.cnc_highlighter import CncBertHighlighter
from evaluation.metrics import evaluate_a_pair_highlight
from pprint import pprint


def cnc_evaluate(retrieve_result_file, truth_file) -> dict:
    # load the retrieve result to pandas dataframe
    truths = read_jsonl(truth_file)

    retrieve_result = pd.read_csv(retrieve_result_file, sep=' ', header=None)
    retrieve_result.columns = ['target_id', 'Q0', 'doc_id', 'rank', 'score', 'tag']

    # gruop by target_id, generate {doc_id: [doci_id1, doc_id2, ...]}
    target_id_group = retrieve_result.groupby('target_id')
    target_id_group = target_id_group['doc_id'].apply(list).reset_index()
    target_id_group.columns = ['target_id', 'doc_id_list']
    # transform the doc_id_list to paragraph_list
    target_id_group['paragraph_list'] = target_id_group['doc_id_list'].apply(lambda x: [retrieve_paragraph_from_docid(doc_id) for doc_id in x])

    # load the highlighter
    highlighter = CncBertHighlighter()
    
    # collect all the predictions
    predictions = dict()
    # TODO: use batch or parallel to speed up
    for index, row in target_id_group.iterrows():
        target_id = row['target_id']
        target_text = retrieve_paragraph_from_docid(target_id)
        paragraph_list = [r for r in row['paragraph_list'] if r is not None]
        highlight_result = highlighter.highlighting_outputs(
                target_text, 
                paragraph_list,
                mean_aggregate=True,
                label_threshold=0.5,
                generate_spans=True
        )
        # add id info
        highlight_result['id'] = target_id
        predictions[target_id] = highlight_result


    metrics = defaultdict(list)
    for truth in truths:
        highlight_result = predictions[truth['id']]
        # TODO: threshold setting duplicated, need to one of them
        # TODO: need to unify naming of keys
        metric_tmp = evaluate_a_pair_highlight(highlight_result, truth) #, threshold=0.5)
        for k, v in metric_tmp.items():
            if k != 'id':
                metrics[k].append(v)
    # calculate the average
    for k, v in metrics.items():
        metrics[k] = sum(v) / len(v)

    pprint(metrics)
    return metrics


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--retrieve_result_file', '-rf', type=str, help='the retrieve result file')
    parser.add_argument('--truth_file', '-tf', type=str, help='the truth file')
    args = parser.parse_args()
    cnc_evaluate(args.retrieve_result_file, args.truth_file)
