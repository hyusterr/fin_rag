
import torch
import numpy as np
from typing import List
from transformers import (
    AutoModelForSequenceClassification,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    pipeline
)

class AttnFullHighlighter:
    def __init__(
        self,
        model_name: str = "facebook/bart-large-cnn",
        method: str = "summarization",
        device: str = "cpu",
        load_pipe: bool = False,
    ):
        self.device = device
        self.method = method

        if "roberta" in model_name.lower():
            self.tokenizer = AutoTokenizer.from_pretrained(model_name, add_prefix_space=True)
        else:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.max_length = self.tokenizer.model_max_length

        if method == "text-classification":
            self.model = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)
        elif method == "summarization":
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
        else:
            raise ValueError(f"Unsupported method: {method}")

        self.model.eval()
        self.pipe = None
        if load_pipe:
            self.pipe = pipeline(method, model=self.model, tokenizer=self.tokenizer, device=device)

    def predict(self, text: List[str], output_attentions: bool = False):
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            is_split_into_words=True,
            truncation=True,
        ).to(self.device)

        if self.method == "text-classification":
            outputs = self.model(**inputs, output_attentions=output_attentions, return_dict=True)
        elif self.method == "summarization":
            outputs = self.model.generate(
                **inputs,
                return_dict_in_generate=True,
                output_scores=True,
                output_attentions=output_attentions,
                num_beams=1,
            )
        return inputs, outputs

    def generate_highlight_spans(self, words, labels):
        spans = []
        current_span = []
        for word, label in zip(words, labels):
            if label == 1:
                current_span.append(word)
            elif current_span:
                spans.append(current_span)
                current_span = []
        if current_span:
            spans.append(current_span)
        return labels, spans

    def highlighting_outputs(
        self,
        target: str,
        text_references: List[str] = None,
        max_length: int = 512,
        mean_aggregate: bool = True,
        label_threshold: float = 0.5,
        select_topk: int = 0,
        generate_spans: bool = True,
        verbose: bool = False,
    ):
        assert bool(select_topk) != bool(label_threshold)

        outputs = {}
        tokenized_inputs, predictions = self.predict(target, output_attentions=True)

        if self.method == "text-classification":
            attentions = predictions.attentions
        elif self.method == "summarization":
            attentions = predictions.cross_attentions

        attention_target = torch.stack([torch.stack(a) for a in attentions])
        attention_target = attention_target.mean(dim=(0, 1, 2, 3, 4)).squeeze()

        words_tgt = target.split()
        word_attentions_tgt = [0] * len(words_tgt)
        for i in range(len(tokenized_inputs["input_ids"][0])):
            word_id = tokenized_inputs.token_to_word(0, i)
            if word_id is not None:
                word_attentions_tgt[word_id] += attention_target[i].item()
        word_attentions_tgt = np.array(word_attentions_tgt)
        word_probs_tgt = word_attentions_tgt / word_attentions_tgt.max()

        outputs["words_tgt"] = words_tgt
        outputs["words_probs_tgt"] = word_probs_tgt
        if mean_aggregate:
            outputs["words_probs_tgt_mean"] = word_probs_tgt

        if label_threshold:
            outputs["words_label_tgt_mean"] = (word_probs_tgt > label_threshold).astype(int)
        elif select_topk:
            outputs["words_label_tgt_mean"] = (word_probs_tgt > np.sort(word_probs_tgt)[-select_topk]).astype(int)

        if generate_spans:
            outputs["words_label_tgt_smooth"], outputs["highlight_spans_smooth"] = self.generate_highlight_spans(
                outputs["words_tgt"], outputs["words_label_tgt_mean"]
            )

        if self.method == "text-classification":
            outputs["predictions"] = self.model.config.id2label[predictions.logits.argmax().item()]
        elif self.method == "summarization":
            outputs["predictions"] = self.tokenizer.decode(predictions.sequences[0], skip_special_tokens=True)

        return outputs
