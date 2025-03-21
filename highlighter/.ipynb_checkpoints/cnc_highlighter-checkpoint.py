import torch
import numpy as np
from transformers import AutoTokenizer
from .cnc_highlighting.encode import BertForHighlightPrediction
# from ..utils.utils import retrieve_paragraph_from_docid


class CncBertHighlighter:
    def __init__(self, model_name: str = 'DylanJHJ/bert-base-final-v0-ep2', device: str = 'cpu'):
        self.device = torch.device(device)
        self.model = BertForHighlightPrediction.from_pretrained(model_name)
        self.method = 'CnC'
        self.model.to(self.device)
    
    def highlighting_outputs(
            self, 
            target, 
            text_references, 
            max_length: int = 512,
            mean_aggregate: bool = False,
            label_threshold: float = 0.5,
            select_topk: int = 5,
            generate_spans: bool = False,
        ):

        # TODO: this can be improved; the window can be obtained by a rationale model? (RQ)
        # at least 3 special tokens: [CLS], [SEP], [SEP]
        # tokenized_target = self.model.tokenizer.tokenize(target)
        tokenized_target = target.split()
        target_length = len(tokenized_target)


        tokenized_target_length = len(self.model.tokenizer.tokenize(target))
        if tokenized_target_length > (max_length - 3) // 2:
            # raise ValueError(f"Target length {target_length} is longer than max_length {max_length - 3}")
            truncate_len = target_length // 2
            while tokenized_target_length > (max_length - 3) // 2:
                truncate_len = truncate_len // 2
                tokenized_target_length = len(self.model.tokenizer.tokenize(" ".join(tokenized_target[:truncate_len]))) 
            targets = []
            len_already_truncated = 0
            while len_already_truncated < target_length:
                targets.append(" ".join(tokenized_target[len_already_truncated:len_already_truncated+truncate_len]))
                len_already_truncated += truncate_len

        else:
            targets = [target]
            truncate_len = target_length

        text_windows = []
        for text_raw in text_references:
            text = text_raw.split()
            if len(text) > max_length - truncate_len - 30:
                while len(text) > max_length - truncate_len - 30:
                    window = text[:max_length - target_length - 30]
                    text_windows.append(" ".join(window)) # not efficient here
                    text = text[len(window):]
                text_windows.append(" ".join(text))
            else:
                text_windows.append(text_raw)
        num_windows = len(text_windows)
        # tokenized_text_windows = [self.model.tokenizer.tokenize(text) for text in text_windows] # the output looks weird since subword tokenization
        # tokenized_text_windows = [text.split() for text in text_windows]


        outputs = {}
        for sub_target in targets:
            highlight_targets = [sub_target] * num_windows

            sub_outputs = self.model.encode(
                device=self.device,
                text_tgt=highlight_targets,
                text_ref=text_windows,
                pretokenized=False, 
                return_reference=False
            )

            # if mean_aggragte = False, then no label_threshold and generate_spans will be used
            # if no label_threshold, then no generate_spans will be used
            # TODO: threshold labeling can perform on each reference separately
            assert mean_aggregate or (not mean_aggregate and not label_threshold and not generate_spans)
    
            if mean_aggregate:
                words_tgt = sub_outputs[0]['words_tgt']
                word_probs_tgt = self.mean_aggregate_highlights(sub_outputs)
                sub_outputs = {'words_tgt': words_tgt, 'words_probs_tgt_mean': word_probs_tgt}

            if label_threshold:
                assert 'words_probs_tgt_mean' in sub_outputs
                sub_outputs['words_label_tgt_mean'] = (sub_outputs['words_probs_tgt_mean'] > label_threshold).astype(int)

            if select_topk:
                assert 'words_probs_tgt_mean' in sub_outputs
                sub_outputs['words_label_tgt_mean'] = (word_probs_tgt > np.sort(word_probs_tgt)[-select_topk]).astype(int)

            if generate_spans:
                assert 'words_label_tgt_mean' in sub_outputs
                sub_outputs['words_label_tgt_smooth'] = self.generate_highlight_spans(sub_outputs['words_label_tgt_mean'])
                # get the spans of the words
                i, spans = 0, []
                tmp = []
                for label in sub_outputs['words_label_tgt_smooth']:
                    if label:
                        tmp.append(i)
                    else:
                        if tmp:
                            spans.append(tmp)
                            tmp = []
                    i += 1
                sub_outputs['highlight_spans_smooth'] = [' '.join(sub_outputs['words_tgt'][span[0]:span[-1]+1]) for span in spans]

            for key, value in sub_outputs.items():
                if key not in outputs:
                    outputs[key] = np.array([])
                outputs[key] = np.concatenate([outputs[key], value])
        
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
