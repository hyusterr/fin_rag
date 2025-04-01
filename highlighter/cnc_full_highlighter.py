import evaluate
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from typing import Optional, List
from pathlib import Path
from transformers import (
    AutoTokenizer, BertModel, BertPreTrainedModel
)
from transformers.modeling_outputs import TokenClassifierOutput
from utils.utils import read_jsonl
from utils.config import FORMMATED_DIR


class CncAlignment:
    def __init__(self, topK=10, rouge_type='rouge2', tag="cnc_alignment"):
        self.rouge = evaluate.load('rouge')
        self.rouge_type = rouge_type
        self.topK = topK
        self.tag = tag

    def align(self, target):
        target_id = target["id"]
        target_text = target["text"]
        date, form, cik, part, item, para = target_id.split("_")
        year = int(date[:4])
        search_pattern_file = f"{year-1}*_{form}_{cik}.jsonl"
        search_pattern = Path(FORMMATED_DIR).rglob(search_pattern_file)
        for file in search_pattern:
            references = read_jsonl(file)
            break
        reference_ids = [reference["id"] for reference in references]
        reference_texts = [reference["contents"] for reference in references]
        target_texts = [target_text] * len(reference_texts)

        rouge_scores = self.rouge.compute(
            predictions=target_texts,
            references=reference_texts,
            rouge_types=[self.rouge_type],
            use_aggregator=False
        )[self.rouge_type]

        ranked_paragraphs = sorted(zip(reference_ids, rouge_scores), key=lambda x: x[1], reverse=True)

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

    def run(self, input_file, output_file=None):
        targets = read_jsonl(input_file)
        results = self.align_all(targets)
        if output_file:
            self.output_trec(results, output_file)
        return results


class BertForHighlightPrediction(BertPreTrainedModel):
    _keys_to_ignore_on_load_unexpected = [r"pooler"]

    def __init__(self, config, **model_kwargs):
        super().__init__(config)
        self.num_labels = config.num_labels
        self.bert = BertModel(config, add_pooling_layer=False)
        classifier_dropout = config.classifier_dropout or config.hidden_dropout_prob
        self.dropout = nn.Dropout(classifier_dropout)
        self.tokens_clf = nn.Linear(config.hidden_size, config.num_labels)
        self.softmax = nn.Softmax(dim=-1)

        self.tau = model_kwargs.pop('tau', 1)
        self.gamma = model_kwargs.pop('gamma', 1)
        self.soft_labeling = model_kwargs.pop('soft_labeling', False)
        self.pooling = model_kwargs.pop('pooling', 'max')

        self.tokenizer = AutoTokenizer.from_pretrained(self.config._name_or_path)
        self.init_weights()

    def forward(self, input_ids=None, probs=None, attention_mask=None, token_type_ids=None,
                position_ids=None, head_mask=None, inputs_embeds=None, labels=None,
                output_attentions=None, output_hidden_states=None, return_dict=None):

        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        tokens_output = outputs[0]
        highlight_logits = self.tokens_clf(self.dropout(tokens_output))

        loss = None
        if labels is not None:
            loss_fct = nn.CrossEntropyLoss()
            active_loss = attention_mask.view(-1) == 1
            active_logits = highlight_logits.view(-1, self.num_labels)
            active_labels = torch.where(
                active_loss,
                labels.view(-1),
                torch.tensor(loss_fct.ignore_index).type_as(labels)
            )
            loss_ce = loss_fct(active_logits, active_labels)

            loss_kl = 0
            if self.soft_labeling and probs is not None:
                loss_fct = nn.KLDivLoss(reduction='sum')
                active_mask = (attention_mask * token_type_ids).view(-1, 1)
                n_active = (active_mask == 1).sum()
                active_mask = active_mask.repeat(1, 2)
                input_logp = F.log_softmax(active_logits / self.tau, -1)
                target_p = torch.cat(((1-probs).view(-1, 1), probs.view(-1, 1)), -1)
                loss_kl = loss_fct(input_logp, target_p * active_mask) / n_active

            loss = self.gamma * loss_ce + (1 - self.gamma) * loss_kl

        return TokenClassifierOutput(
            loss=loss,
            logits=highlight_logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )

    def _pool_probs(self, probs, word_ids):
        ret = np.zeros(1 + max(word_ids))
        for w_id, p in zip(word_ids, probs):
            if self.pooling == 'max':
                ret[w_id] = max(ret[w_id], p)
            elif self.pooling == 'mean':
                ret[w_id] = np.mean([ret[w_id], p])
        return ret

    def encode(self, text_tgt: List[str], text_ref: Optional[List[str]] = None,
               device: str = 'cpu', pretokenized: bool = True, return_reference: bool = False):
        if text_ref is None:
            text_ref = [self.tokenizer.pad_token] * len(text_tgt)
        if not pretokenized:
            text_tgt = [t.split() for t in text_tgt]
            text_ref = [t.split() for t in text_ref]

        inputs = self.tokenizer(
            text_ref, text_tgt,
            max_length=512,
            truncation=True,
            padding=True,
            is_split_into_words=True,
            return_tensors='pt'
        ).to(device)

        with torch.no_grad():
            logits = self.forward(**inputs).logits
            probs = self.softmax(logits)[:, :, 1].cpu().numpy()

        results = []
        for i, prob in enumerate(probs):
            mapping = np.array(inputs.word_ids(i))
            sep = np.argwhere(mapping == None).flatten()[1] - 1
            token_probs = prob[mapping != None]
            word_ids = mapping[mapping != None]

            token_probs_ref = token_probs[:sep]
            token_probs_tgt = token_probs[sep:]
            word_ids_ref = word_ids[:sep]
            word_ids_tgt = word_ids[sep:]

            ret = {'words_tgt': text_tgt[i], 
                   'word_probs_tgt': self._pool_probs(token_probs_tgt, word_ids_tgt)}

            if return_reference:
                ret['words_ref'] = text_ref[i]
                ret['word_probs_ref'] = self._pool_probs(token_probs_ref, word_ids_ref)

            results.append(ret)

        return results
