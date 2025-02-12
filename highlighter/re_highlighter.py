import torch
from transformers import BertTokenizer, BertForTokenClassification

class REHighlighter():
    def __init__(self, model_path):
        self.highlighter = BertForTokenClassification.from_pretrained(model_path)
        self.highlighter_tokenizer = BertTokenizer.from_pretrained(model_path)
        self.retriever = BertForTokenClassification.from_pretrained(model_path)
        self.retriever_tokenizer = BertTokenizer.from_pretrained(model_path)
        
        
    def highlight(self, sentence):
        inputs = self.tokenizer(sentence, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=2)
        tokens = self.tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
        highlights = []
        for token, prediction in zip(tokens, predictions[0]):
            if token.startswith("##"):
                highlights[-1] += token[2:]
            else:
                highlights.append(token)
        return highlights
