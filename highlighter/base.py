import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import transformers
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModelForMaskedLM, AutoModel, AutoConfig, Trainer, TrainingArguments, DataCollatorWithPadding
import evaluate
from datasets import load_dataset
from typing import List

FPB_label2id = {0: "negative", 1: "neutral", 2: "positive"}
FPB_id2label = {v: k for k, v in FPB_label2id.items()}

class BaseHiglighter:
    def __init__(self, model_name='bert-base-uncased', device='cuda'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForMaskedLM.from_pretrained(model_name)
        self.model.eval()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        

    def highlight_outputs(
            self, 
            target, 
            text_reference,
            max_length=512,
            mean_aggregate=True,
            label_threshold=0.5,
            generate_spans=True
        ):
        raise NotImplementedError('highlight method not implemented')

    
    @staticmethod
    def mean_aggregate_highlights(highlight_results):
        # TODO: Add more aggregation methods, mean is the simplest
        word_probs_tgt = [highlight['word_probs_tgt'] for highlight in highlight_results]
        mean_word_probs_tgt = sum(word_probs_tgt) / len(word_probs_tgt)
        return mean_word_probs_tgt

    @staticmethod
    def generate_highlight_spans(
            words_tgt: List[str], 
            word_label_tgt: List[int], 
            smoothen=True,
            max_gap=5,
        ):
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

        
        for label in smooth_tokenids:
            if label:
                tmp.append(i)
            else:
                if tmp:
                    spans.append(tmp)
                    tmp = []
            i += 1
        highlight_spans_smooth = [' '.join(words_tgt[span[0]:span[-1]+1]) for span in spans]
 
        return smooth_tokenids, highlight_spans_smooth


class AutoSequenceClassifier:
    def __init__(self, model_name='bert-base-uncased', device='cuda', label2id=FPB_label2id, id2label=FPB_id2label):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(
                model_name, num_labels=len(label2id), id2label=id2label, label2id=label2id
        )
        self.model.eval()
        self.device = torch.device(device)
        self.model.to(self.device)    
        self.data_collator = DataCollatorWithPadding(tokenizer=self.tokenizer)
        self.metric = evaluate.load("accuracy")

    def classify(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        inputs.to(self.device)
        outputs = self.model(**inputs)
        probs = F.softmax(outputs.logits, dim=-1)
        return probs


    def calculate_attention(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        inputs.to(self.device)
        outputs = self.model(**inputs, output_attentions=True)
        return outputs.attentions


    def get_argmax_attention(self, text):
        attentions = self.calculate_attention(text)
        attentions = attentions[-1]
        attentions = attentions[0].mean(dim=0)
        attentions = attentions.cpu().detach().numpy()
        attentions = np.mean(attentions, axis=0)
        attentions = attentions / attentions.sum()
        return attentions

    def create_highlight_text(self, text, attentions):
        tokens = self.tokenizer.tokenize(text)
        tokens = ['[CLS]'] + tokens + ['[SEP]']
        attentions = attentions[1:-1]
        attentions = attentions[:len(tokens)-2]
        attentions = attentions / attentions.sum()
        attentions = attentions * 100
        attentions = attentions.round(2)
        attentions = attentions.astype(int)
        tokens = [f'<span style="background-color: rgba(255, 255, 0, {att}%);">{token}</span>' for token, att in zip(tokens, attentions)]
        return ' '.join(tokens)

    def compute_metrics(self, eval_pred):
        predictions, labels = eval_pred
        predictions = np.argmax(predictions, axis=1)
        return self.metric.compute(predictions=predictions, references=labels)


if __name__ == '__main__':
    fpb_data = load_dataset("financial_phrasebank", "sentences_50agree")
    a_sample = fpb_data['train'][0]
    classifier = AutoSequenceClassifier("ahmedrachid/FinancialBERT-Sentiment-Analysis")
    print(a_sample['sentence'], a_sample['label'])
    print(classifier.classify(a_sample['sentence']))
    print(classifier.calculate_attention(a_sample['sentence']))
