# input: trec format file
# 20220222_10-K_1090727_part2_item7_para100 Q0 20180221_10-K_1090727_part2_item7_para107 1 84.35596466064453 title-year2018_2022-filtered_out-cik1090727-year2022_2022-item7
# output: evaluation metrics

import json
import argparse
import numpy as np
import pandas as pd
from collections import defaultdict
from pathlib import Path
from ..utils.utils import retrieve_paragraph_from_docid, read_jsonl, read_json
from .metrics import evaluate_a_pair_highlight, evaluate_spans_in_a_pair_highlight
from pprint import pprint
from tqdm.auto import tqdm
from collections import OrderedDict

class Task1:
    def __init__(
            self, 
            highlighter,
            retrieve_result_file, 
            truth_file,
            pred_file=None,
            label_threshold=0.5, 
            get_top_k=0, 
            device='cpu', 
            verbose=False,
            generate_pred=False,
        ):

        if not truth_file:
            raise ValueError("truth_file is required")
        assert bool(get_top_k) != bool(label_threshold), "only one of get_top_k and label_threshold should be set"

        
        self.highlighter = highlighter
        self.retrieve_result_file = retrieve_result_file
        self.truth_file = truth_file
        self.label_threshold = label_threshold
        self.get_top_k = get_top_k
        self.device = device
        self.verbose = verbose
        self.generate_pred = generate_pred
        if type(generate_pred) is str:
            self.generate_pred = Path(generate_pred)
        elif generate_pred:
            self.generate_pred = Path('pred.jsonl')

        # preprocess truth and retrieve result
        self.truths = read_jsonl(truth_file)
        if retrieve_result_file is not None:
            retrieve_result = pd.read_csv(retrieve_result_file, sep=' ', header=None)
            retrieve_result.columns = ['target_id', 'Q0', 'doc_id', 'rank', 'score', 'tag']
            target_id_group = retrieve_result.groupby('target_id')
            target_id_group = target_id_group['doc_id'].apply(list).reset_index()
            target_id_group.columns = ['target_id', 'doc_id_list']
            # transform the doc_id_list to paragraph_list
            target_id_group['paragraph_list'] = target_id_group['doc_id_list'].apply(lambda x: [retrieve_paragraph_from_docid(doc_id) for doc_id in x])
            self.retrieve_result = target_id_group
        else:
            self.retrieve_result = None
        
        if pred_file is not None:
            self.pred_file = read_json(pred_file)
        else:
            self.pred_file = None


    def evaluate(self):
        # TODO: select_topk's spirit is duplicated with r-precision? 
    
        # collect all the predictions
        predictions = OrderedDict()
        # TODO: use batch or parallel to speed up

        if not self.verbose:
            print("[Start highlighting...]")
            iter_data = tqdm(self.truths)
        else:
            iter_data = self.truths

        for row in iter_data:
            # if we assume we know how many words need to be higlight in advance, sounds strange!
            # select_topk = sum(row["highlight_labels"]) if self.get_top_k else None
            select_topk = self.get_top_k
            target_id = row['id']
            target_text = retrieve_paragraph_from_docid(target_id)
            paragraph_list, docid_list = None, None
            if self.retrieve_result_file is not None:
                row = self.retrieve_result[self.retrieve_result['target_id'] == target_id].iloc[0]
                paragraph_list = [r for r in row['paragraph_list'] if r is not None]
                docid_list = row['doc_id_list']

            if self.pred_file is None:
                highlight_result = OrderedDict({"id": target_id})
                _highlight_result = self.highlighter.highlighting_outputs(
                        target=target_text, 
                        text_references=paragraph_list, # can be None
                        select_topk=select_topk, 
                        mean_aggregate=True,
                        label_threshold=self.label_threshold,
                        generate_spans=True
                )

                # add id info
                highlight_result.update(_highlight_result)
                predictions[target_id] = highlight_result
                predictions[target_id]['references'] = paragraph_list
                predictions[target_id]['ref_ids'] = docid_list

            else:
                try:
                    highlight_result = self.pred_file[target_id]
                except KeyError:
                    print(f"no prediction for {target_id}")
                    continue
                predictions[target_id] = highlight_result

        if self.generate_pred:
            prediction_output = OrderedDict()
            # clean the format
            for target_id, highlight_result in predictions.items():
                for k, v in highlight_result.items():
                    if type(v) is np.ndarray:
                        highlight_result[k] = v.tolist()
                prediction_output[target_id] = highlight_result

            with open(self.generate_pred, 'w') as f:
                json.dump(prediction_output, f, indent=4)


        if not self.verbose:
            print("[Start evaluating...]")
            iter_data = tqdm(self.truths)
        else:
            iter_data = self.truths
       
        metrics = defaultdict(list)
        for truth in iter_data:
            target_id = truth['id']
            highlight_result = predictions[target_id]
            paragraph_list = highlight_result.get('references', None)
            ref_ids = highlight_result.get('ref_ids', None)
            # TODO: threshold setting duplicated, need to one of them --> fix threshold = 0.5
            # TODO: need to unify naming of keys
            metric_tmp = evaluate_a_pair_highlight(highlight_result, truth)
            metric_spans_tmp = evaluate_spans_in_a_pair_highlight(highlight_result, truth)
            for k, v in metric_tmp.items():
                if k != 'id':
                    metrics[k].append(v)
            for k, v in metric_spans_tmp.items():
                if k != 'id':
                    metrics[k].append(v)

            if self.verbose:
                print(f"[target]")
                print(f"{target_id}:\t{target_text}")
                print(f"type: {truth['type']}")
                print("-"*50)
                if paragraph_list is not None:
                    print(f"[references]: {len(paragraph_list)}")
                    for id_, p in zip(ref_ids, paragraph_list):
                        print(f"{id_}:\t{p}")
                    print("-"*50)
                print(f"[highlight labels] truth:", truth["highlight_labels"])
                print(f"[highlight labels] prediction:", highlight_result['words_label_tgt_mean'])
                print(f"[highlight labels] prediction (smoothed):", highlight_result['words_label_tgt_smooth'])
                print("-"*50)
                print(f"[highlight spans] truth:")
                for span in truth["highlight_spans"]:
                    print(span)
                print(f"[highlight spans] prediction:")
                print([highlight_result['words_tgt'][i] for i in range(len(highlight_result['words_tgt'])) if highlight_result['words_label_tgt_mean'][i] == 1])
                print(f"[highlight spans] prediction (smoothed):")
                for span in highlight_result['highlight_spans_smooth']:
                    print(span)
                print("-"*50)
                if self.highlighter.method == "text-classification":
                    print("[classification label] prediction:", highlight_result['predictions'])
                elif self.highlighter.method == "summarization":
                    print("[summary] prediction:", highlight_result['predictions'])
                print("[highlight prob. (mean)] truth:", np.array(truth['highlight_probs']).round(3))
                print("[highlight prob. (mean)] prediction:", highlight_result['words_probs_tgt_mean'].round(3))
                print("-"*50)
                print(f"metrics of this sample:")
                print('[sentence-level]')
                pprint(metric_tmp)
                print('[span-level]')
                pprint(metric_spans_tmp)
                print('+='*50)
                print()



        # calculate the average
        for k, v in metrics.items():
            metrics[k] = np.nanmean(np.array(v))

        if self.verbose:
            print(f"metrics of all samples:")

        pprint(metrics)
        return metrics
