# reproduce of "Towards Annotating and Creating Sub-Sentence Summary Highlights" from ACL 2019, link:  https://aclanthology.org/D19-5408.pdf
# TODO: check if the backbone model is abstractive or extractive summarization model in original paper
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import transformers
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline, AutoModelForSeq2SeqLM
from highlighter.base import BaseHighlighter
from typing import List

# because FPB's label is defined by "the impact of the news on the stock price", we can use the sentiment analysis model to predict the label
MOST_DOWNLOAD_FPB_MODELS_HF = {
    "Sigma/financial-sentiment-analysis": dict(Loss=0.0395, Accuracy=0.9924, F1=0.9924),
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
    def __init__(
            self, 
            model_name='human-centered-summarization/financial-summarization-pegasus', 
            method='summarization', 
            device='cuda:2', 
            load_pipe=False
        ):
        # TODO: hf now supports device_map='auto', which will automatically select the device, see: https://huggingface.co/docs/accelerate/v0.22.0/en/concept_guides/big_model_inference
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.max_length = self.tokenizer.model_max_length
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

    # TODO: window sliding if a text is too long
    def predict(self, text: List[str], output_attentions=False):
        '''
        text example: ["The stock price of Apple Inc. has increased by 10% after the announcement of the new iPhone 13.", "The stock price of Apple Inc. has increased by 10% after the announcement of the new iPhone 13."]
        '''
        if self.pipe is not None and not output_attentions:
            out = self.pipe(text, output_attentions=output_attentions)
            return None, out
        
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True).to(self.device) # use intrinsic padding and truncation wrt. max_length
        with torch.no_grad():
            if self.method == 'text-classification':
                outputs = self.model(**inputs, output_attentions=output_attentions, return_dict=True)

            # TODO: what is the difference between generate and forward?
            # TODO: check the usage of decoder_input_ids
            # "Pegasus uses the pad_token_id as the starting token for decoder_input_ids generation. If past_key_values is used, optionally only the last decoder_input_ids have to be input (see past_key_values)."
            # decide to use generate() instead of forward() because we can skip the decoder_input_ids process
            elif self.method == 'summarization':
                outputs = self.model.generate(
                        **inputs, 
                        return_dict_in_generate=True, 
                        output_scores=True,
                        # decoder_input_ids=self.tokenizer.pad_token_id, 
                        output_attentions=output_attentions, 
                        num_beams=1, # default num_beams=8 in Pegasus # no beam search for simplicity
                        length_penalty=None, # default length_penalty=0.6 in Pegasus, if num_beams=1, length_penalty should be unset
                        # return_dict=True
                        )
                # default return a GenerateBeamEncoderDecoderOutput object, see https://huggingface.co/docs/transformers/internal/generation_utils#transformers.generation.GenerateBeamEncoderDecoderOutput
                # TODO: decide whether to use beam_search or not
        return inputs, outputs

    def highlighting_outputs(
            self,
            target: str,
            text_reference: List[str], # attn_highlighter do not need text_reference, just for compatibility
            max_length: int = 512,
            mean_aggregate: bool = True,
            label_threshold: float = 0.5,
            generate_spans: bool = True,
            verbose: bool = True
        ):
        
        return_dict = {}

        # get the prediction of the target
        tokenized_inputs, outputs = self.predict(target, output_attentions=True)
        # print(type(outputs)) # GenerateBeamEncoderDecoderOutput or GenerateEncoderDecoderOutput
    

        # get the attention scores of each token in the target w.r.t. the prediction
        if self.method == 'text-classification':
            attentions = outputs.attentions
        elif self.method == 'summarization':
            # TODO: decide to use encoder_attentions or cross_attentions or decoder_attentions
            attentions = outputs.cross_attentions 

        # attentions shape: (num_generated_tokens, num_layers, num_beams, num_heads, 1(one generated token), num_target_tokens), with the first and second dimensions are store in tuples
        # pegasus has 16 layers and 16 heads for encoder and decoder respectively
        # get the average attention scores of each token in the target w.r.t. the prediction
        attention_target = torch.stack([torch.stack(a) for a in attentions]) # shape: (num_generated_tokens, num_layers, num_beams, num_heads, 1, num_target_tokens) # first 2 dimensions are stored in tuples, so .stack() twice
        # get the average attention scores of each target token, shape (num_target_tokens, 1)
        attention_target = attention_target.mean(dim=(0, 1, 2, 3, 4)).squeeze() # shape: (num_target_tokens, 1)
        # dim: the dimension to reduce; .squeeze() remove the dimension with size 1
        # here, sum(attention_target) = 1, because the attention scores are normalized, this shall be transformed to a sequece of probabilities, i.e. each element's max value is 1 after combine subwords

        decoded = self.tokenizer.convert_ids_to_tokens(self.tokenizer(target)['input_ids'])
        assert len(decoded) == len(attention_target)

        # if 2+ subwords are combined, the attention scores should be combined as well
        for i, token in enumerate(decoded):
            if self.tokenizer.is_token_part(token):
                print(token)
                break


                  

        # get the top-K tokens with the highest attention scores, return label=1

        if verbose:
            print("target: ", target)
            print("target length (str): ", len(target.split()))
            print("target length (tokenizer): ", len(self.tokenizer(target)['input_ids']))
            decoded = self.tokenizer.convert_ids_to_tokens(self.tokenizer(target)['input_ids'])
            print("target decoded: ", decoded)
            print("output type:", type(outputs))
            print(outputs.keys())
            print("outputs.sequences: ", outputs.sequences)
            print("summary:", self.tokenizer.decode(outputs.sequences[0]))
            print("summary length: ", len(outputs.sequences[0]))    
            # print("model: ", self.model)
            print("len(attentions): ", len(attentions))
            print("len(attentions[0]): ", len(attentions[0]))
            print("len(attentions[0][0]): ", attentions[0][0].shape)
            print("attentions_target: ", attention_target)
            # print("softmax(attention_target): ", F.softmax(attention_target, dim=0)) # not useful because the attention scores are already normalized, sum to 1
            print("normalized attention_target: ", attention_target / attention_target.max())
            print(sum(attention_target)) # =1
            print(len(decoded) == len(attention_target))
            print(list(zip(decoded, attention_target)))




        # get smoothed label for each token

        # get the smoothed span
