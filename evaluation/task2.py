from ..evaluation.metrics import evaluate_trec_qrels, evaluate_deepeval_context_relevancy
# from evaluation.deepeval import MistralDeepEvalLLM, MISTRAL_7B_INSTRUCT_2

from pprint import pprint

class Task2:
    def __init__(self, run_filename, qrels_filename):
        self.qrels = qrels_filename
        self.run = run_filename

    def evaluate(self, trec=True, llm=True):
        result = {}
        if trec:
            result.update(evaluate_trec_qrels(self.run, self.qrels))
        if llm:
            model = MistralDeepEvalLLM()
            evaluate_deepeval_context_relevancy(self.run, model)

        pprint(result)
        return result



