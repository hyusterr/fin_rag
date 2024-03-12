import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import transformers
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModelForMaskedLM, AutoModel, AutoConfig, Trainer, TrainingArguments, DataCollatorWithPadding
import evaluate
import numpy as np
from datasets import load_dataset

FPB_label2id = {0: "negative", 1: "neutral", 2: "positive"}
FPB_id2label = {v: k for k, v in FPB_label2id.items()}

class BaseHiglighter:
    def __init__(self, model_name='bert-base-uncased', device='cuda'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForMaskedLM.from_pretrained(model_name)
        self.model.eval()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        

    def highlight(self, target, reference):
        raise NotImplementedError('highlight method not implemented')


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
