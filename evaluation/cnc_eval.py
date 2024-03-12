# input: trec format file
# 20220222_10-K_1090727_part2_item7_para100 Q0 20180221_10-K_1090727_part2_item7_para107 1 84.35596466064453 title-year2018_2022-filtered_out-cik1090727-year2022_2022-item7
# output: evaluation metrics

import pandas as pd
from collections import defaultdict
from pathlib import Path
from ..highlighter.cnc_highlighter import CncBertHighlighter
from ..utils.utils import retrieve_paragraph_from_doc_id
from metrics import evaluate_a_pair_highlight


def cnc_evaluate(retrieve_result_file):
    # load the retrieve result to pandas dataframe
    retrieve_result = pd.read_csv(retrieve_result_file, sep=' ', header=None)
    retrieve_result.columns = ['target_id', 'Q0', 'doc_id', 'rank', 'score', 'tag']

    # gruop by target_id, generate {doc_id: [doci_id1, doc_id2, ...]}
    target_id_group = retrieve_result.groupby('target_id')
    target_id_group = target_id_group['doc_id'].apply(list).reset_index()
    target_id_group.columns = ['target_id', 'doc_id_list']
    # transform the doc_id_list to paragraph_list
    target_id_group['paragraph_list'] = target_id_group['doc_id_list'].apply(lambda x: [retrieve_paragraph_from_doc_id(doc_id) for doc_id in x])

    # load the highlighter
    highlighter = CncBertHighlighter()
    
    # evaluate each target_id
    result = defaultdict(list)
    # TODO: use batch or parallel to speed up
    for index, row in target_id_group.iterrows():
        target_id = row['target_id']
        target_text = retrieve_paragraph_from_doc_id(target_id)
        paragraph_list = row['paragraph_list']
        highlight_result = highlighter.highlight_outputs(
                target_text, 
                paragraph_list,
                mean_aggregation=True,
                label_threshold=0.5,
                generate_spans=True
        )
        # TODO: threshold setting duplicated, need to one of them
        # TODO: need to unify naming of keys
        result_tmp = evaluate_a_pair_highlight(paragraph_list, highlight_result)
        for k, v in result_tmp.items():
            if k != 'id':
                result[k].append(v)
    # calculate the average
    for k, v in result.items():
        result[k] = sum(v) / len(v)

    print(result)
    return result



