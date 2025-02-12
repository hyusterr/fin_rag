import torch
from transformers import BertTokenizer, BertForTokenClassification, BertConfig

class VIHighlighter(BertForTokenClassification):
    def __init__(self, config):
        super(VIHighlighter, self).__init__(config)
        self.num_labels = config.num_labels

        self.bert = BertForTokenClassification.from_pretrained('bert-base-uncased', num_labels=self.num_labels)

    def forward(self, input_ids, attention_mask=None, token_type_ids=None, position_ids=None, head_mask=None, labels=None):
        outputs = self.bert(input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids, position_ids=position_ids, head_mask=head_mask)
        return outputs
