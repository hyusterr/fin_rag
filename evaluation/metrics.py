import numpy as np
import evaluate
from trectools import TrecQrel, TrecRun, TrecEval
# https://github.com/joaopalotti/trectools
from deepeval.metrics import ContextualRelevancyMetric
from deepeval.test_case import LLMTestCase
from deepeval import evaluate as evaluate_deepeval
from utils.utils import retrieve_paragraph_from_docid

rouge = evaluate.load("rouge")
def evaluate_a_pair_highlight(pred, truth): #, pred_threshold=0.5) -> dict:
    """
    Evaluate a pair of predictions and truth.
    - pred: prediction after average of different ref-tgt pair dict, e.g. {
        "id": str, 
        "words_tgt": [str, ...],
        "words_probs_tgt_mean": [0, 0.66, ...],
        "words_label_tgt_mean": [0, 1, ...],
        "words_label_tgt_smooth": [0, 1, ...],
        "highlight_spans_smooth": [str, str, ..., ...],
    }
    - truth: dict, e.g. {
        "id": str, 
        "text": str, 
        "tokens": [str, ...],
        "highlight_probs": [0, 0.66, ...],
        "highlight_labels": [0, 1, ...],
        "highlight_spans": [[str, str, ...], ...],
        "type": str,
        "topic": str,
        "subtopic": str,
    }
    """
    # Check if the id matches
    assert pred["id"] == truth["id"], f"ID mismatch: {pred['id']} vs {truth['id']}"
    # Check if the length matches
    assert len(pred["words_probs_tgt_mean"]) == len(truth["highlight_probs"]), f"Length mismatch: {len(pred['pred_prob'])} vs {len(truth['highlight_probs'])}"

    # Convert the prediction to binary 
    # TODO: not sure if threshold is a parameter of evaluation or a parameter of prediction
    # pred_bin = [1 if p > pred_threshold else 0 for p in pred["pred_prob"]]
    pred_bin = pred["words_label_tgt_smooth"]
    # Calculate the R-Precision

    r_truth = sum(truth["highlight_labels"])
    truth_index = [i for i, t in enumerate(truth["highlight_labels"]) if t == 1]
    topr_pred_index = sorted(range(len(pred["words_probs_tgt_mean"])), key=lambda i: pred["words_probs_tgt_mean"][i], reverse=True)[:r_truth]
    r_precision = len(set(truth_index) & set(topr_pred_index)) / r_truth if r_truth > 0 else 0

    # calculate the correlation 
    if np.std(truth["highlight_probs"]) != 0:
        correlation = np.corrcoef(truth["highlight_probs"], pred["words_probs_tgt_mean"])[0, 1] if r_truth > 0 else 0

    # Calculate the metrics
    tp = sum([1 for p, t in zip(pred_bin, truth["highlight_labels"]) if p == 1 and t == 1])
    fp = sum([1 for p, t in zip(pred_bin, truth["highlight_labels"]) if p == 1 and t == 0])
    fn = sum([1 for p, t in zip(pred_bin, truth["highlight_labels"]) if p == 0 and t == 1])
    tn = sum([1 for p, t in zip(pred_bin, truth["highlight_labels"]) if p == 0 and t == 0])
    # Calculate the precision, recall, and F1
    precision = tp / (tp + fp) if tp + fp > 0 else 0
    recall = tp / (tp + fn) if tp + fn > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0

    # calculate ROUGEs
    # pred_tokens = [truth["tokens"][i] for i, p in enumerate(pred_bin) if p == 1] 
    pred_tokens = pred["highlight_spans_smooth"]
    # TODO: do we need to consider splitting into spans considering the consecutive tokens? now is the simpliest version
    # TODO: the evaluate shall support some parallel processing, maybe not count at every single pair will be faster
    ref_tokens = " ".join(truth["highlight_spans"])
    pred_tokens = " ".join(pred_tokens)
    # TODO: rouge implement batch inside, the efficiency has not yet been leveraged
    rouges = rouge.compute(predictions=[pred_tokens], references=[ref_tokens])
    
    
    # Return the metrics
    output = {
        "id": pred["id"],
        # "type": truth["type"],
        # "topic": truth["topic"],
        # "subtopic": truth["subtopic"],
        "r_precision": r_precision,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "correlation": correlation,
    }
    output.update(rouges)

    return output
# TODO: the granularity of the evaluation is not clear, e.g. the evaluation of the whole dataset or the evaluation of each pair

def evaluate_trec_qrels(preds, truths, K=10):
    """
    preds: filename of trec run format: target_id' 'Q0' 'doc_id' 'rank' 'score' 'run_id
    truths: filename trec qrels format: target_id' '0' 'doc_id' 'relevance'
    """
    run = TrecRun(preds)
    qrels = TrecQrel(truths)
    evaluator = TrecEval(run, qrels)
    # results = run.evaluate_run(qrels, per_query=True)
    ndcg = evaluator.get_ndcg(depth=K)
    recall = evaluator.get_recall(depth=K)
    precision = evaluator.get_precision(depth=K)
    results = {
        f"ndcg@{K}": ndcg,
        f"recall@{K}": recall,
        f"precision@{K}": precision,
    }
    return results


def evaluate_deepeval_context_relevancy(preds, llm, topK=10) -> dict:
    """
    preds: filename of trec run format: target_id' 'Q0' 'doc_id' 'rank' 'score' 'run_id
    llm: a class inherit deepeval.models.base_model.DeepEvalBaseLLM
    """
    # usage ref: https://github.com/joaopalotti/trectools/blob/418c970c3c37bc8f3b3a99d8178e8f9893bce1d5/trectools/trec_eval.py#L668
    run = TrecRun(preds).run_data
    topX_result = run.groupby("query")["docid"].apply(lambda x: x.head(topK).tolist()).to_dict()
    # already sort descending by score
    deepeval_testcases = [
            LLMTestCase(
                input=retrieve_paragraph_from_docid(target_id),
                actual_output=retrieve_paragraph_from_docid(target_id),
                retrieval_context=[retrieve_paragraph_from_docid(doc_id) for doc_id in context_ids]
                )
            for target_id, context_ids in topX_result.items()
            ]
    cr_metric = ContextualRelevancyMetric(model=llm)
    evaluate_deepeval(deepeval_testcases, [cr_metric])

