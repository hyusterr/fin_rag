import torch

from utils.utils import read_jsonl
from transformers import BertTokenizer, BertForTokenClassification, BertConfig
from transformers.modeling_outputs import TokenClassifierOutput

TRAINING_DATA = 'annotation/annotated_result/all/aggregate_train.jsonl'
VALID_DATA = 'annotation/annotated_result/all/aggregate_test.jsonl'
TEST_DATA = 'annotation/annotated_result/all/expert_annotated_test.jsonl'

train_data = read_jsonl(TRAINING_DATA)
valid_data = read_jsonl(VALID_DATA)
test_data = read_jsonl(TEST_DATA)

# option 1: mix all kinds of aggregation and apply different weights and train at the same time
# option 2: at the beginning, only use one kind of aggregation and then gradually add more, let the model learn from deterministic to soft gradually
'''
class AggHighlighterDataset(torch.utils.data.Dataset):
    def __init__(self, data, tokenizer):
        self.data = data
        self.tokenizer = tokenizer

    def __getitem__(self, idx):
        item = self.data[idx]
        text = item['text']
        agg_type = item['agg_type']
        inputs = self.tokenizer(text, return_tensors='pt')
        inputs['agg_type'] = agg_type
        return inputs

    def __len__(self):
        return len(self.data)
'''

class AggHighlighter(BertForTokenClassification):
    def __init__(self): #, config): #agg_weights):
        super(AggHighlighter, self).__init__(BertConfig.from_pretrained('bert-base-uncased', num_labels=2))
        # self.agg_weights = agg_weights



    def forward(self, input_dict):
        # print(input_dict)
        input_ids = input_dict['input_ids']
        attention_mask = input_dict['attention_mask'] if 'attention_mask' in input_dict else None
        labels = input_dict['labels'] if 'labels' in input_dict else None

        '''
        original_outputs = super(AggHighlighter, self).forward(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels
        )
        print(original_outputs.loss) # original_outputs.loss will output a scalar tensor
        '''
        agg_type = input_dict['aggregation'] # one hot encoding
        # weighted_loss = original_outputs.loss * self.agg_weights[agg_type]
        stophere

        return TokenClassifierOutput(
                loss=weighted_loss, 
                logits=original_outputs.logits,
                hidden_states=original_outputs.hidden_states,
                attentions=original_outputs.attentions
            )


    '''
    def train(self):
        pass

    def predict(self, text):
        input_ids = torch.tensor(self.tokenizer.encode(text)).unsqueeze(0)
        with torch.no_grad():
            outputs = self.model(input_ids)
        logits = outputs[0]
        _, predicted = torch.max(logits, 2)
        predicted = predicted.squeeze(0)
        return predicted
    '''
