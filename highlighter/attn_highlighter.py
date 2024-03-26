# reproduce of "Towards Annotating and Creating Sub-Sentence Summary Highlights" from ACL 2019, link:  https://aclanthology.org/D19-5408.pdf
# TODO: check if the backbone model is abstractive or extractive summarization model in original paper
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import transformers
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
from highlighter import BaseHighlighter

# because FPB's label is defined by "the impact of the news on the stock price", we can use the sentiment analysis model to predict the label
MOST_DOWNLOAD_FPB_MODELS_HF = {
    "Sigma/financial-sentiment-analysis": dict(Loss=0.0395, Accuracy=0.9924 F1=0.9924),
    "mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis": dict(Loss=0.1116, Accuracy=0.9823, F1=None),
    "mr8488/distilroberta-finetuned-financial-news-sentiment-analysis-v2": dict(Loss=0.1116, Accuracy=0.9923, F1=None),
    "ahmedrachid/FinancialBERT-Sentiment-Analysis": dict(Loss=None, Accuracy=0.98, F1=0.98)
    }

# because our guidelines for task1 is to find most important signals in financial reports, it somehow mimics the summarization task
MOST_DOWNLOAD_SUM_MODELS_HF = {
    "human-centered-summarization/financial-summarization-pegasus": dict(RougeL=18.14),
    # https://aclanthology.org/2021.hcinlp-1.4.pdf # fin-news sum.
    "facebook/bart-large-cnn": dict(),
    "google/pegasus-xsum": dict(),
    "Falconsai/text_summarization": dict(),
    }
# NOTES: financial related summarization task:
# 1. FINDSum (Financial Report Document Summarization) - HFDataset: Sakshi1307/FindSUM
# 2. https://groups.ischool.berkeley.edu/10k-snap/
# 3. The Financial Narrative Summarisation Shared Task (FNS 2021)
# 4. https://dl.acm.org/doi/pdf/10.1145/3442442.3451373 # MDA as 10K's summary

class AttnHighlighter(BaseHighlighter):
    def __init__(self, model_name, method, device='cuda', load_pipe=False):
        self.device = device
        # TODO: how to automtically get max_length from the model?
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        if method == 'text-classification':
            self.model = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)
        elif method == 'summarization':
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
        self.method = method
        self.model.eval()
        self.pipe = None
        if load_pipe:
            if method == 'text-classification':
                self.pipe = pipeline("text-classification", model=model_name, device=device)
            elif method == 'summarization':
                self.pipe = pipeline("summarization", model=model_name, device=device)

    def predict(self, text: List[str]):
        if self.pipe is not None:
            return self.pipe(text)
        # TODO: window sliding if a text is too long
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512).to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.logits

    def highlight_outputs(
            self,
            target: str,
            text_reference: List[str],
            max_length: int = 512,
            mean_aggregate: bool = True,
            threshold: float = 0.5,
            generate_spans: bool = True,
        ):
        # get the prediction of the target

        # get the attention scores of each token in the target w.r.t. the prediction

        # get the top-
