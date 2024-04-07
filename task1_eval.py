# input: trec format file
# 20220222_10-K_1090727_part2_item7_para100 Q0 20180221_10-K_1090727_part2_item7_para107 1 84.35596466064453 title-year2018_2022-filtered_out-cik1090727-year2022_2022-item7
# output: evaluation metrics

import argparse
import numpy as np
import pandas as pd
from collections import defaultdict
from pathlib import Path
from utils.utils import retrieve_paragraph_from_docid, read_jsonl
from highlighter import AttnHighlighter, CncBertHighlighter
from evaluation import Task1
from pprint import pprint


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # file arguments
    parser.add_argument('--truth_file', '-tf', type=str, help='the truth file')
    parser.add_argument('--retrieve_result_file', '-rf', type=str, help='the retrieve result file')
    
    # highlighter arguments
    parser.add_argument('--highlighter', '-hl', type=str, default='attn', help='the highlighter to use')
    parser.add_argument('--model_id', '-m', type=str, help='the model id')
    parser.add_argument('--method', '-mt', type=str, default='summarization', help='the method to use in attn highlighter')

    # evaluation arguments
    parser.add_argument('--label_threshold', '-lt', type=float, default=0, help='use thresholding determine label')
    parser.add_argument('--get_top_k', '-tk', type=int, default=0, help='use ranking method to determine label')
    parser.add_argument('--device', '-d', type=str, default='cpu', help='the device to use')
    parser.add_argument('--verbose', '-v', action='store_true', help='print the details')
    args = parser.parse_args()

    highlighter = None
    if args.highlighter == 'attn':
        assert args.method in ['summarization', 'text-classification'], f'{args.method} method not supported'
        highlighter = AttnHighlighter(args.model_id, args.method, device=args.device)
    elif args.highlighter == 'cnc':
        highlighter = CncBertHighlighter(device=args.device)
    else:
        raise ValueError('highlighter not supported')

    task1 = Task1(
        highlighter=highlighter,
        retrieve_result_file=args.retrieve_result_file,
        truth_file=args.truth_file,
        label_threshold=args.label_threshold,
        get_top_k=args.get_top_k,
        device=args.device,
        verbose=args.verbose
    )
    task1.evaluate()
