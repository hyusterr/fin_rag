# input: 
#   1. query file: a jsonl contains all mda passages of one company's 10K in one year
#   2. corpus directory
#   3. output file: a trec format file contains (# of query * K passages) lines of result
'''
{"id": "20190823_10-K_1001250_finstats_para12", "order": 12, "paragraph": ["In fiscal 2019, global prestige skin care continued to lead product category growth.", "our skin care business benefited from the enduring strength of hero product lines such as advanced night repair from est e lauder and cr me de la mer from la mer, as well as recent product launches, the growth in asia and targeted expanded consumer reach.", "the launches of advanced night repair eye supercharged complex and micro essence with sakura ferment from est e lauder were particularly successful in asia/pacific.", "during fiscal 2019, we introduced a new level of personalization with clinique id, which allows the consumer to create a custom blend of hydration and treatment."]}
{"id": "20201125_10-K_1744489_part2_item7_para7", "order": 7, "paragraph": ["the impact of these disruptions and the extent of their adverse impact on our financial and operational results will be dictated by the length of time that such disruptions continue, which will, in turn, depend on the currently unknowable duration and severity of the impacts of covid-19, and among other things, the impact and duration of governmental actions imposed in response to covid-19 and individuals' and companies' risk tolerance regarding health matters going forward.", "while we cannot be certain as to the duration of the impacts of covid-19, we currently expect covid-19 to adversely impact our financial results at least through fiscal 2021."]}
'''
# retrieve K=1000 --> filter out invalid passages --> build index once
# filter out invalid passages --> retrieve K=100? --> build index multiple times
# preprocess output than call pyserini sh?

# ref:Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks code
# ref:torch_lightning 

# what are possible retrieval scope limitations?
# 1. time 2. company 3. corpus type (10-K for now)
# files hierarchy: /home/ythsiao/output/EL/10-K/20190823_10-K_1001250.jsonl

import argparse
import jsonlines
import pyserini
from pathlib import Path

class BaseRetriever:
    def __init__(self):
        pass

    def build_index(self, corpus, index_path):
        raise NotImplementedError

    def retrieve(self, query, corpus, K, year_before):
        raise NotImplementedError
        # TREC format?

    def filter(self):
        # post-process
        raise NotImplementedError

    def output(self, result, format='trec'):
        # 20181105_10-K_320193_part2_item7_para1 Q0 20181220_10-K_1090872_fin_stats_para1 1 0.3 fintext
        # qid, Q0, docid, rank, score, tag(identifier for the system)
        raise NotImplementedError


class BM25Retriever(BaseRetriever):
    def __init__(self, corpus, index_path):
        super().__init__()

    def build_index(self, corpus, index_path):
        # corpus: jsonl file
        # index_path: path to save index
        # build index once
        # corpus: jsonl file
        # index_path: path to save index
        # build index once

        # check if index exists
        if Path(index_path).exists():
            print('index exists.')
            return


        print('building index...')
        self.index = pyserini.index.IndexWriter(index_path)
        with jsonlines.open(corpus) as reader:
            for obj in reader:
                self.index.add_document(obj['paragraph'])
        self.index.close()
        print('index built.')

    def retrieve(self, query, corpus, K, year_before):
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, required=True, help='model name', default='bm25')
    parser.add_argument('--corpus', type=str, required=True, help='path to corpus file')
    parser.add_argument('--index_path', type=str, required=True, help='path to save index')
    parser.add_argument('--query', type=str, required=True, help='path to query file')
    parser.add_argument('--output', type=str, required=True, help='path to output file')
    parser.add_argument('--K', type=int, default=1000, help='number of retrieved passages')
    parser.add_argument('--year_before', type=int, default=1, help='number of years before')
    args = parser.parse_args()

    if args.model == 'bm25':
        retriever = BM25Retriever(args.corpus, args.index_path)
    
    retriever.retrieve(args.query, args.corpus, args.K, args.year_before)

