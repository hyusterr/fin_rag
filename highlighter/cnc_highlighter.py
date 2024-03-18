print(__name__)
from transformers import AutoTokenizer
from cnc_highlighting.encode import BertForHighlightPrediction
from fin_rag.utils.utils import retrieve_paragraph_from_docid


class CncBertHighlighter:
    def __init__(self, model_name: str = 'DylanJHJ/bert-base-final-v0-ep2', device: str = 'cpu'):
        self.device = device
        self.model = BertForHighlightPrediction.from_pretrained(model_name)
        self.model.to(self.device)
    
    def highlighting_outputs(
            self, 
            target, 
            text_references, 
            mean_aggregate: bool = False,
            label_threshold: float = 0.5,
            generate_spans: bool = False,
        ):
        num_references = len(text_references)
        targets = [target] * num_references

        outputs = self.model.encode(
            text_tgt=targets,
            text_ref=text_references,
            pretokenized=False, 
            return_reference=False
        )

        # if mean_aggragte = False, then no label_threshold and generate_spans will be used
        # if no label_threshold, then no generate_spans will be used
        # TODO: threshold labeling can perform on each reference separately
        assert mean_aggregate or (not mean_aggregate and not label_threshold and not generate_spans)
    
        if mean_aggregate:
            words_tgt = outputs[0]['words_tgt']
            word_probs_tgt = self.mean_aggregate_highlights(outputs)
            outputs = {'words_tgt': words_tgt, 'word_probs_tgt_mean': word_probs_tgt}

        if label_threshold:
            assert 'word_probs_tgt_mean' in outputs
            outputs['word_label_tgt_mean'] = (outputs['word_probs_tgt_mean'] > label_threshold).astype(int)

        if generate_spans:
            assert 'word_label_tgt_mean' in outputs
            outputs['word_label_tgt_smooth'] = self.generate_highlight_spans(outputs['word_label_tgt_mean'])
            # get the spans of the words
            i, spans = 0, []
            tmp = []
            for label in outputs['word_label_tgt_smooth']:
                if label:
                    tmp.append(i)
                else:
                    if tmp:
                        spans.append(tmp)
                        tmp = []
                i += 1
            outputs['highlight_spans_smooth'] = [' '.join(outputs['words_tgt'][span[0]:span[-1]+1]) for span in spans]

        return outputs
    
    def find_highest_prob_word(self, words_tgt, word_probs_tgt, n):
        sorted_indices = word_probs_tgt.argsort()[::-1]  # Sort indices in descending order
        top_n_indices = sorted_indices[:n]  # Get the top-n indices
        top_n_words = [words_tgt[i] for i in top_n_indices]
        return top_n_words

    
    def visualize_top_k_highlight(self, highlight_results, highlight_words_cnt=5):
        for i in range(len(highlight_results)):
            words_tgt = highlight_results[i]['words_tgt']
            word_probs_tgt = highlight_results[i]['word_probs_tgt']
            top_k_words = self.find_highest_prob_word(words_tgt, word_probs_tgt, highlight_words_cnt)
            print(f"reference {i+1}:", top_k_words)

    @staticmethod
    def mean_aggregate_highlights(highlight_results):
        # TODO: Add more aggregation methods, mean is the simplest
        word_probs_tgt = [highlight['word_probs_tgt'] for highlight in highlight_results]
        mean_word_probs_tgt = sum(word_probs_tgt) / len(word_probs_tgt)
        return mean_word_probs_tgt

    @staticmethod
    def generate_highlight_spans(word_label_tgt, max_gap=5):
        # ref: https://aclanthology.org/D19-5408.pdf
        # we actually will not know how many token need to be highlighted if we don't peek the true label
        # first version: use threshold labeling --> perform smoothing to generate spans
        # connecting two selected words if there is a small gap (<5 words) between them.
        # [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1] --> [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1]
        # span = ["token1 token2 token3 token4 token5", "token12"]
        # TODO: need to check edge cases
        smooth_tokenids = []
        start = None
        for i, label in enumerate(word_label_tgt):
            if label:
                smooth_tokenids.append(label)
                if start is None:
                    start = i
                if start is not None and i - start < max_gap:
                    smooth_tokenids[start:i+1] = [1] * (i - start + 1)
                start = i

            else:
                smooth_tokenids.append(label)
            
        return smooth_tokenids
            

if __name__ == "__main__":

    reference_docids = [
        "20221028_10-K_320193_part2_item7_para7",
        "20221028_10-K_320193_part2_item7_para8",
        "20220318_10-K_1045810_part2_item7_para5"
    ]
    text_references = [retrieve_paragraph_from_docid(docid) for docid in reference_docids]
    target = retrieve_paragraph_from_docid("20221028_10-K_320193_part2_item7_para7")
    highlighter = CncBertHighlighter()
    highlight_results = highlighter.highlighting_outputs(target, text_references, mean_aggregate=True, label_threshold=0.3, generate_spans=True)
    # highlighter.visualize_top_k_highlight(highlight_results, highlight_words_cnt=5)
    print(highlight_results)
