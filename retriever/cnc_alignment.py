# reproduce the alignment of ACL2023 paper
# input: jsonl file
# {id: "target_id", "text": "target_text", ...}
# output: trec format file
# target_id Q0 doc_id rank score tag

import evaluate
from pathlib import Path
from ..utils.utils import read_jsonl, retrieve_paragraph_from_docid
from ..utils.config import FORMATTED_DIR

class CncAlignment:
    def __init__(self, topK=10, rouge_type='rouge2', tag="cnc_alignment"):
        self.rouge = evaluate.load('rouge')
        self.rouge_type = rouge_type
        self.topK = topK
        self.tag = tag

    def align(self, target):
        target_id = target["id"]
        target_text = target["text"]
        # get all paragraphs from the same item in the previous year
        date, form, cik, part, item, para = target_id.split("_")
        year = int(date[:4])
        search_pattern_file = f"{year-1}*_{form}_{cik}.jsonl"
        search_pattern = Path(FORMATTED_DIR).rglob(search_pattern_file)
        for file in search_pattern:
            references = read_jsonl(file)
            break

        reference_ids = [reference["id"] for reference in references]
        reference_texts = [reference["text"] for reference in references]
        target_texts = [target_text] * len(reference_texts)

        # TODO: check if predictions and referecnces of rouge input matters?
        # calculate synthetic similarity score between the target and each paragraph
        rouge_scores = self.rouge.compute(
            predictions=target_texts, 
            references=reference_texts,
            rouge_types=[self.rouge_type],
            use_agregator=False
        )[self.rouge_type]

        # rank the paragraphs based on the similarity score
        ranked_paragraphs = sorted(zip(reference_ids, rouge_scores), key=lambda x: x[1], reverse=True)

        # get the difference between the ranks and drop the paragraphs after the max difference
        # if the len(result) > topK, drop the paragraphs after the topK
        max_diff, argmax_diff = 0, 0
        for i in range(len(ranked_paragraphs)-1):
            diff = ranked_paragraphs[i][1] - ranked_paragraphs[i+1][1]
            if diff > max_diff:
                max_diff = diff
                argmax_diff = i

        if argmax_diff > self.topK-1:
            result = ranked_paragraphs[:self.topK]
        else:
            result = ranked_paragraphs[:argmax_diff+1]

        return result

    def align_all(self, targets):
        results = {}
        for target in targets:
            results[target["id"]] = self.align(target)
        return results


    def output_trec(self, results, output_file):
        with open(output_file, "w") as f:
            for target_id, paragraphs in results.items():
                for i, (paragraph_id, score) in enumerate(paragraphs):
                    f.write(f"{target_id} Q0 {paragraph_id} {i+1} {score} {self.tag}\n")

    def run(self, input_file, output_file):
        targets = read_jsonl(input_file)
        results = self.align_all(targets)
        self.output_trec(results, output_file)
        return results
