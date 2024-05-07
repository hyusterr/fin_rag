from evaluation.metrics import evaluate_trec_qrels
from pprint import pprint

class Task2:
    def __init__(self, run_filename, qrels_filename):
        self.qrels = qrels_filename
        self.run = run_filename

    def evaluate(self, trec=True, llm=True):
        if trec:
            result = evaluate_trec_qrels(self.run, self.qrels)
        if llm:
            pass
        pprint(result)
        return result
