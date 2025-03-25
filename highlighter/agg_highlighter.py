import torch

from utils.utils import read_jsonl
from data_utils import AGG_MAP
from transformers import BertTokenizer, BertForTokenClassification, BertConfig
from transformers.modeling_outputs import TokenClassifierOutput

# option 1: mix all kinds of aggregation and apply different weights and train at the same time
# option 2: at the beginning, only use one kind of aggregation and then gradually add more, let the model learn from deterministic to soft gradually --> cirriculum learning: strict --> loose
# KEYS_TO_IGNORE_AT_INFERENCE = ['attentions', 'hidden_states']
class AggHighlighter(BertForTokenClassification):
    def __init__(self, config=None, agg_weights_base=0.7, strategy='mix', type_order=None):
        assert strategy in ['mix', 'cirriculum', 'sequential']
        for ty in type_order:
            assert ty in AGG_MAP.keys()

        if config is None:
            config = BertConfig.from_pretrained('bert-base-uncased', num_labels=2) # keys_to_ignore_at_inference=KEYS_TO_IGNORE_AT_INFERENCE)
        super(AggHighlighter, self).__init__(config)
        # self.agg_weights = agg_weights
        self.agg_weights = torch.tensor([
            0.,
            0., # agg_weights_base * 1,
            0., #vagg_weights_base**2 * 1,
            1., # agg_weights_base**3 * 1,
            0., # agg_weights_base**4 * 1,
        ])

    def forward(
            self, 
            input_ids,
            attention_mask=None,
            labels=None,
            token_type_ids=None,
            position_ids=None,
            head_mask=None,
            inputs_embeds=None,
            aggregation=None,
            tokens=None,
        ):

        if self.agg_weights.device != self.device:
            self.agg_weights = self.agg_weights.to(self.device)

        # print(input_dict)
        # input_ids = input_dict['input_ids']
        # attention_mask = input_dict['attention_mask'] if 'attention_mask' in input_dict else None
        # labels = input_dict['labels'] if 'labels' in input_dict else None
        # token_type_ids = input_dict['token_type_ids'] if 'token_type_ids' in input_dict else None
        # return_dict = return_dict if return_dict is not None else self.config.use_return_dict
        return_dict = True
        output_attentions = True
        output_hidden_states = True

        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            # position_ids=position_ids,
            # head_mask=head_mask,
            # inputs_emb:eds=inputs_embeds,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        sequence_output = outputs[0]
        logits = self.classifier(sequence_output)
        loss = None
        if labels is not None:
            loss_fct = torch.nn.CrossEntropyLoss()# reduction='none') # weight=torch.tensor([1., 4.]).to(self.device))
            # Only keep active parts of the loss
            '''
            if attention_mask is not None:
                # not sure if this will be used in the future (consider RAG)
                active_loss = attention_mask.view(-1) == 1
                active_logits = logits.view(-1, self.num_labels)
                active_labels = torch.where(
                    active_loss, labels.view(-1), torch.tensor(loss_fct.ignore_index).type_as(labels)
                )
                loss = loss_fct(active_logits, active_labels)
            '''
            
            # keep the loss with the same shape as the input
            # not so sure if this can turn right back to the original shape
            loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
            # loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1)) # this flatten all losses from all tokens into one scalar
            '''
            agg_type_tensor = aggregation.type_as(self.agg_weights)
            apply_weights = torch.matmul(agg_type_tensor, self.agg_weights)
            weighted_loss = apply_weights * loss.sum(dim=1)
            weighted_loss = weighted_loss.mean() # mean all losses in the batch
            '''
            # I decided to use mean accroding to this link: https://discuss.pytorch.org/t/loss-reduction-sum-vs-mean-when-to-use-each/115641/2
            # "the disadvantage in using the sum reduction would also be that the loss scale (and gradients) depend on the batch size, so you would probably need to change the learning rate based on the batch size."

        # print(logits.shape)

        return TokenClassifierOutput(
                loss=loss, # weighted_loss, 
                logits=logits,
                hidden_states=outputs.hidden_states,
                attentions=outputs.attentions
            )
