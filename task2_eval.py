# input: trec format file
# 20220222_10-K_1090727_part2_item7_para100 Q0 20180221_10-K_1090727_part2_item7_para107 1 84.35596466064453 title-year2018_2022-filtered_out-cik1090727-year2022_2022-item7
# output: evaluation metrics

import argparse
import numpy as np
import pandas as pd
from collections import defaultdict
from pathlib import Path
from evaluation import Task2
from pprint import pprint


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # file arguments
    parser.add_argument('--truth_file', '-tf', type=str, help='the truth file')
    parser.add_argument('--retrieve_result_file', '-rf', type=str, help='the retrieve result file')
    
    args = parser.parse_args()

    task2 = Task2(args.retrieve_result_file, args.truth_file)
    task2.evaluate()
