import numpy as np
import evaluate
from sklearn.metrics import roc_auc_score, precision_recall_curve, auc, f1_score, precision_score, recall_score, accuracy_score
# from trectools.trectools import TrecQrel, TrecRun, TrecEval
# https://github.com/joaopalotti/trectools
# from deepeval.metrics import ContextualRelevancyMetric
# from deepeval.test_case import LLMTestCase
# from deepeval import evaluate as evaluate_deepeval
import pulp
from ..utils.utils import retrieve_paragraph_from_docid
from itertools import product
from scipy.special import softmax
from tqdm import tqdm
import multiprocessing
import time

rouge = evaluate.load("rouge")

def get_spans_from_binary_labels(labels):
    '''
    labels: list of binary labels, e.g. [0, 1, 1, 0, 0, 1, 1, 0, ...]
    '''
    spans = []
    tmp = []
    for i, l in enumerate(labels):
        if l == 1:
            tmp.append(i)
        else:
            if tmp != []:
                spans.append(tmp)
            tmp = []
    # deal with the last span
    if tmp != []:
        spans.append(tmp)

    if len(spans) == 0:
        return [(-1, -1)], spans
    # keep the span as the start and end index (exclude)
    spans_start_end = [(s[0], s[-1]+1) for s in spans]
    return spans_start_end, spans

def dissimilarity_of_span_pair(span1, span2):
    '''
    dissimilarity = positional_dissimilarity + categorical_dissimilarity
    in our case, categotical dissimilarity is reduced (since we only have 1 highlight category)
    span1: tuple of start and end index, e.g. (0, 3)
    span2: tuple of start and end index, e.g. (0, 3)
    '''
    pesudo_unit = (-1, -1) 
    # print(span1, span2)
    # spirit cost beyond the value of n * pseudo_unit_cost can be discarded
    associate_cost = 1
    if span1 == span2:
        return 0

    if span1 == pesudo_unit or span2 == pesudo_unit:
        return associate_cost

    pd_numerator = abs(span1[0] - span2[0]) + abs(span1[1] - span2[1])
    pd_denominator = span1[1] - span1[0] + span2[1] - span2[0]
    positional_dissimilarity = ((pd_numerator / pd_denominator) ** 2) * associate_cost
    # in our case, we only have 2 categories, so the categorical dissimilarity is 0 or 1

    return positional_dissimilarity

# unitizing: unit locating
# TODO: keep working on this, this is wrong now
def disorder_of_a_unitary_alignment(ua):
    '''
    - unitary alignment: will ultimately become an n-tuple, (in our case, n = 2 for pred and truth) containing at most one unit by each source: It represents the hypothesis that i source agree to some extent on a given phenomenon to be unitized. If one annotator does not agree, then insert a pseudo-unit for it. e.g. [tok1, tok2, tok3]
    A: [0, 1, 1]; B: [1, 1, 0] --> tok1: [-1, 1], tok2: [1, 1], tok3: [1, -1]
    - alignment: is a set of unitary alignments such that each unit of each source belongs to one and only one unitary alignment (so it forms a partition of the sources).
    - discorder of a unitary aligment: the average of the dissimilarity of all pairs of spans in the unitary alignment

    u: list of spans, e.g. [(0, 3), (4, 6), ...]
    v: list of spans, e.g. [(0, 3), (4, 6), ...]
    ua: list of spans with source id, e.g. [((0, 3), 1), ((4, 6), 2), ...]
    '''
    if len(ua) == 1:
        return dissimilarity_of_span_pair(ua[0], (-1, -1))
    spans_from1 = [s[0] for s in ua if s[1] == 1]
    spans_from2 = [s[0] for s in ua if s[1] == 2]
    # add pseudo unit to empty ones
    if len(spans_from1) == 0:
        spans_from1 = [(-1, -1)]
    if len(spans_from2) == 0:
        spans_from2 = [(-1, -1)]
    
    # print(len(spans_from1), len(spans_from2))
    disorder = np.array([dissimilarity_of_span_pair(pair[0], pair[1]) for pair in product(spans_from1, spans_from2)])
    return disorder.mean()


def disorder_of_an_alignment(a, average_num_of_spans):
    '''
    - best alignment: the alignment that minimizes the disorder among all possible alignments
    - disorder of sources: the disorder of its best alignment
    a: list of unitary alignments, e.g. [[(0, 3), (4, 6), ...], [(0, 3), (4, 6), ...], ...]
    '''
    disorder = 0
    for ua in a:
        disorder += disorder_of_a_unitary_alignment(ua)
    return disorder / average_num_of_spans

NUM_OF_SOURCE = 2
def chance_disorder(n=NUM_OF_SOURCE):
    '''
    n: number of sources
    - chance discorder means if we assume the distribution of 
        1. number of spans in each source
        2. highlight labels of each span
        3. span length per highlighted span (length of label 1)
        4. gap's length between two highlighted spans (length of label 0)
    '''
    pass

def get_observed_disorder(truth, pred, max_size_of_ua=2000):
    '''
    spans_from1: list of spans, e.g. [(0, 3), (4, 6), ...]
    spans_from2: list of spans, e.g. [(0, 3), (4, 6), ...]
    '''
    import time
    start = time.time()
    
    spans_from1, _ = get_spans_from_binary_labels(truth)
    spans_from2, _  = get_spans_from_binary_labels(pred)
    length_of_truth = len(truth)
    if len(spans_from2) > 20:
        return np.nan # or 1? 
    # print('spans from pred:', len(spans_from2))
    spans_pool = [(s, 1) for s in spans_from1] + [(s, 2) for s in spans_from2] 
    # get partitions of the spans pool
    # TODO: need DP or transform it as a linear programming problem --> use LP for now
    # ref: https://coin-or.github.io/pulp/CaseStudies/a_set_partitioning_problem.html 
    n = len(spans_pool)
    max_size = n
    max_size_per_ua = n
    avarage_num_of_span = n / NUM_OF_SOURCE

    # print('time for getting spans:', time.time() - start)

    # get all possible UA
    # TODO: apply filter to decrease the number of UA --> maybe don't need it since n is small in our task
    # 1. if an disorder(ua) > disorder(span, null), it will not take into consideration
    # 2. if (1, 2) is not taken into consideration, (1, 2, 3) will not also
    if len(spans_pool) > 20:
        return np.nan

    all_unitary_alignments = [tuple(c) for c in pulp.allcombinations(spans_pool, max_size_per_ua) if len(c) < 20]
    # print('all ua:', len(all_unitary_alignments))
    if len(all_unitary_alignments) > 500000: 
        # extreme case --> ignore, not so much, like [0, 1] * n/2; ignore it since with the training progress, case like this will be lesser and lesser
        return np.nan
    possible_unitary_alignments, disorder_of_possible_ua = [], []
    for ua in all_unitary_alignments:
        if len(ua) > 20:
            continue
        disorder = disorder_of_a_unitary_alignment(ua)
        if disorder <= 1:
            possible_unitary_alignments.append(ua)
            disorder_of_possible_ua.append(disorder)
    # print('possible ua:', len(possible_unitary_alignments))

    if len(possible_unitary_alignments) > max_size_of_ua:
        possible_unitary_alignments = possible_unitary_alignments[:max_size_of_ua]
        disorder_of_possible_ua = disorder_of_possible_ua[:max_size_of_ua]
        # return np.nan
    # print(len(possible_unitary_alignments)) # [0, 1] * n/2 case will have 10K+ possible unitary alignments, will cause memory error
    # print('time for getting possible_unitary_alignments and filter by disorder:', time.time() - start)
    ua2i_map = {c: i for i, c in enumerate(possible_unitary_alignments)}
    i2ua_map = {v: k for k, v in ua2i_map.items()}
    i2ua_list = list(i2ua_map.keys()) # unitary_alignment # name too long error
    # describe the inputs
    x = pulp.LpVariable.dicts(
        "ua", i2ua_map.keys(), lowBound=0, upBound=1, cat=pulp.LpInteger
    ) # unitary_alignment # name too long error

    # describe the objectives
    alignment_disorder_model = pulp.LpProblem("alignment_disorder", pulp.LpMinimize)
    alignment_disorder_model += pulp.lpSum([disorder_of_possible_ua[i] * x[i] for i in i2ua_list])
    alignment_disorder_model += (
        pulp.lpSum([x[i] for i in i2ua_list]) <= max_size,
        "Max_ua", # maxium_number_of_ua
    )
    for span in spans_pool:
        alignment_disorder_model += (
            pulp.lpSum([x[i] for i in i2ua_list if span in i2ua_map[i]]) == 1,
            f"Must_seat_{span}",
        )
    # define solvers
    # [PROBLEM] multi-threading cause deadlock with Trainer
    solver = pulp.PULP_CBC_CMD(msg=False, threads=32, logPath='/dev/null', timeLimit=30)
    # SCIP, GUROBI, CPLEX are faster
    # solver = pulp.SCIP_PY(msg=False, threads=32)
    # solver = pulp.FSCIP_CMD('/tmp2/yshuang/fin.rag/scip/bin/fscip', msg=False, threads=32)
    # solver = pulp.SCIP_CMD('/tmp2/yshuang/fin.rag/scip/bin/scip', msg=False)
    # print('time for setting up the model:', time.time() - start)
    alignment_disorder_model.solve(solver)
    # print('time for solving the model:', time.time() - start)
    
    # get the result
    best_alignment = []
    for i in i2ua_list:
        if x[i].value() == 1.:
            best_alignment.append(i2ua_map[i])
    
    best_disorder = disorder_of_an_alignment(best_alignment,  avarage_num_of_span)

    return best_disorder #, best_alignment

def get_observed_disorder_in_process(truth, pred, return_dict, idx):
    disorder = get_observed_disorder(truth, pred)
    return_dict[idx] = disorder


def get_holistic_gamma(truth, pred):
    '''
    pred: list of predicions, e.g. [0, 1, 0, ...]
    truth: list of truth, e.g. [0, 1, 0, ...]
    ref: https://aclanthology.org/J15-3003/
    Spirits:
    - any unitary alignment with a cost above ∆∅ can be replaced by creating a separate unitary alignment for each unit (of cost ∆∅ per unitary alignment, so of total cost n · ∆∅).
    - actually a backpack problem? 
    '''
    # get the spans from each prediction
    pred_spans_start_end, _ = get_spans_from_binary_labels(pred)
    truth_spans_start_end, _ = get_spans_from_binary_labels(truth)
    
    expected_disorder = get_expected_disorder(2)
    observed_disorder = get_observed_disorder(pred_spans_start_end, truth_spans_start_end)
    holistic_gamma = 1 - observed_disorder / expected_disorder
    return holistic_gamma



def get_r_precision(truth, pred):
    """
    Evaluate the R-Precision.
    - pred: list of predicted probability, e.g. [0.1, 0.9, 0.2, ...]
    - truth: list of truth, e.g. [0, 1, 0, ...]
    """
    r_truth = sum(truth)
    truth_index = [i for i, t in enumerate(truth) if t == 1]
    topr_pred_index = sorted(range(len(pred)), key=lambda i: pred[i], reverse=True)[:r_truth]
    r_precision = len(set(truth_index) & set(topr_pred_index)) / r_truth if r_truth > 0 else 0
    return r_precision


# it seems like the serial correlation is not suitable for this task, since we only have 1/0 from one expert
def get_correlation(truth, pred):
    """
    Evaluate the correlation.
    - pred: list of predictions of probability, e.g. [0.1, 0.9, 0.2, ...]
    - truth: list of voting probability, e.g. [0.1, 0.9, 0.2, ...]
    """
    correlation = np.corrcoef(truth, pred)[0, 1]
    return correlation


def evaluate_a_pair_highlight(pred, truth, agg_type='naive_aggregation'): #, pred_threshold=0.5) -> dict:
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
    # TODO: not sure if threshold is a parameter of evaluation or a parameter of prediction --> fixed to 0.5
    # pred_bin = [1 if p > pred_threshold else 0 for p in pred["pred_prob"]]
    pred_bin = pred["words_label_tgt_smooth"]
    pred_prob = pred["words_probs_tgt_mean"]

    try:
        truth_bin = truth["binary_labels"] # for expert set
        truth_prob = truth["binary_labels"] # we only have one expert, so the truth_prob is the same as truth_bin
    except:
        truth_bin = truth[agg_type]["highlight_labels"]
        truth_prob = truth["highlight_probs"]
    # Calculate the R-Precision
    r_precision = get_r_precision(pred_prob, truth_bin)


    # calculate the correlation 
    if np.std(truth_prob) != 0:
        correlation = get_correlation(pred_prob, truth_prob)
    else:
        correlation = np.nan

    # Calculate the metrics
    precision, recall, f1 = get_precision_recall_f1(pred_bin, truth_bin)

    if sum(truth_bin) == 0 or sum(truth_bin) == len(truth_bin):
        auc = np.nan # auc needs 2 classes
    else:
        auc = get_auc(pred_prob, truth_bin)

    # rouge seems non-sense for this task, skip it for now
    '''
    # calculate ROUGEs
    # pred_tokens = [truth["tokens"][i] for i, p in enumerate(pred_bin) if p == 1] 
    pred_tokens = pred["highlight_spans_smooth"]
    # TODO: do we need to consider splitting into spans considering the consecutive tokens? now is the simpliest version
    # TODO: the evaluate shall support some parallel processing, maybe not count at every single pair will be faster
    try:
        ref_tokens = " ".join(truth["highlight_spans"]) # it seems like this will be wrong when there are multiple spans
        # I have not yet prepare spans for the expert set

    except:
        ref_tokens = " ".join(truth[agg_type]["spans"]) # it seems like this will be wrong when there are multiple spans
    pred_tokens = " ".join(pred_tokens)
    # TODO: rouge implement batch inside, the efficiency has not yet been leveraged
    rouges = rouge.compute(predictions=[pred_tokens], references=[ref_tokens])
    '''
    
    
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
        "auc": auc,
    }
    # output.update(rouges)

    # print(output)

    return output
# TODO: the granularity of the evaluation is not clear, e.g. the evaluation of the whole dataset or the evaluation of each pair

def evaluate_spans_in_a_pair_highlight(pred, truth):
    # check if the id matches
    assert pred["id"] == truth["id"], f"ID mismatch: {pred['id']} vs {truth['id']}"

    # get the spans in truth
    tmp, spans_group_ids = [], []
    for i, t in enumerate(truth["highlight_labels"]):
        if t == 1:
            tmp.append(i)
        else:
            if tmp != []:
                spans_group_ids.append(tmp)
            tmp = []
    if tmp != []:
        spans_group_ids.append(tmp)

    # print("spans_group_ids", spans_group_ids)
    
    # TODO: if there is no span in the truth, the evaluation shall be 0
    if spans_group_ids == []:
        return {
            "id": pred["id"],
            "span_accuracy": np.nan,
            "span_exact_match": np.nan,
            # "span_auc": None,
        }

    spans_group_pred_probs, spans_group_truth_probs = [], []
    spans_group_pred_labels, spans_group_truth_labels = [], []
    for group in spans_group_ids:
        spans_group_pred_probs.append([pred["words_probs_tgt_mean"][i] for i in group])
        spans_group_pred_labels.append([pred["words_label_tgt_smooth"][i] for i in group])

        spans_group_truth_probs.append([truth["highlight_probs"][i] for i in group])
        spans_group_truth_labels.append([truth["highlight_labels"][i] for i in group])

    assert len(spans_group_pred_probs) == len(spans_group_truth_probs), "The number of spans in prediction and truth does not match"
    

    # evaluate the metrics by spans
    # accuracy
    accuracy = [sum(p) / sum(t) if sum(t) > 0 else 0 for p, t in zip(spans_group_pred_labels, spans_group_truth_labels)]
    accuracy = sum(accuracy) / len(accuracy)

    # exact match
    # e.g. id = [1, 2, 4, 5]
    # pred = [0.1, 0.9, 0.8, 0.8]
    # exact_match = 0.5
    each_exact_match = [1 if sum(p) == sum(t) else 0 for p, t in zip(spans_group_pred_labels, spans_group_truth_labels)]
    exact_match = sum(each_exact_match) / len(each_exact_match)
    
    # AUC
    # auc = [roc_auc_score(t, p) for p, t in zip(spans_group_pred_probs, spans_group_truth_labels)]
    # auc = sum(auc) / len(auc)

    # TODO: ROUGE (to extend the task to generation)

    # average the result of each span as the span-level evaluation
    # return the metrics

    
    output = {
        "id": pred["id"],
        "span_accuracy": accuracy,
        "span_exact_match": exact_match,
        # "span_auc": auc,
    }

    # print(output)
    
    return output


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

def get_auprc(truth, pred_prob):
    """
    Evaluate the AUPRC.
    - pred: list of predictions of probability, e.g. [0.1, 0.9, 0.2, ...]
    - truth: list of truth, e.g. [0, 1, 0, ...]
    """
    if len(truth) == 0 or len(set(truth)) == 1:
        return np.nan
    precision, recall, _ = precision_recall_curve(truth, pred_prob, pos_label=1)
    auprc = auc(recall, precision)
    return auprc

def get_r_precision(pred_prob, truth):
    '''
    Evaluate the R-Precision.
    - pred: list of predicted probability, e.g. [0.1, 0.9, 0.2, ...]
    - truth: list of truth, e.g. [0, 1, 0, ...]
    '''
    R = sum(truth)
    topR_pred_prob = sorted(pred_prob, reverse=True)[:R]
    r_precision = sum([1 for p in topR_pred_prob if p > 0.5]) / R if R > 0 else 0
    return r_precision
