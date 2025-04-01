import math
import torch
import torch.nn.functional as F
from transformers import BertForTokenClassification, BertConfig
from transformers.modeling_outputs import TokenClassifierOutput

# 假設 AGG_MAP 為一個 dict，例如：
# AGG_MAP = {'strict': 0, 'harsh': 1, 'complex': 2, 'naive': 3, 'loose': 4}
from data_utils import AGG_MAP

def get_curriculum_weight(epoch: int, decay_rate: float = 0.1) -> float:
    return math.exp(-decay_rate * epoch)

class AggHighlighter(BertForTokenClassification):
    def __init__(self, config=None, agg_weights_base=0.7, strategy='mix', type_order=None, num_labels=2, id2label=None, label2id=None):
        """
        Args:
            config: 若為 None，則從 'bert-base-uncased' 讀入預設設定
            agg_weights_base: 若為 scalar，則會根據 type_order 長度計算幾何級數權重（第一項固定為 1）
            strategy: 選擇 'mix'、'cirriculum' 或 'sequential'
            type_order: 指定所使用的 aggregation type 序列，例如 ['strict', 'naive', 'loose']
        """
        assert strategy in ['mix', 'curriculum', 'sequential'], "strategy 必須在 ['mix', 'cirriculum', 'sequential'] 中"
        assert type_order is not None and len(type_order) > 0, "請傳入至少一種 aggregation type 到 type_order"
        for ty in type_order:
            assert ty in AGG_MAP.keys(), f"{ty} 不在 AGG_MAP 定義中"
        self.strategy = strategy
        self.type_order = type_order

        if config is None:
            config = BertConfig.from_pretrained('bert-base-uncased', num_labels=2)
        super(AggHighlighter, self).__init__(config)
        
        # 如果是 mix 策略，初始化幾何權重
        if strategy == 'mix':
            agg_weights = [0.] * len(AGG_MAP) # type: int
            if isinstance(agg_weights_base, (int, float)):
                # 第一個權重固定為 1，其餘依序乘上 agg_weights_base 的次方
                init_weight = 1.0
                for typ in type_order:
                    agg_weights[AGG_MAP[typ]] = init_weight
                    init_weight *= agg_weights_base
                self.agg_weights = torch.tensor(agg_weights) 
            elif len(agg_weights_base) == len(type_order):
                for i, typ in enumerate(type_order):
                    agg_weights[AGG_MAP[typ]] = agg_weights_base[i]
                self.agg_weights = torch.tensor(agg_weights)

        else:
            # 其他策略不需要預先固定權重
            self.agg_weights = None

    def forward(
        self, 
        input_ids,
        attention_mask=None,
        labels=None,
        token_type_ids=None,
        position_ids=None,
        head_mask=None,
        inputs_embeds=None,
        aggregation=None,   # 預期為 one-hot tensor，形狀：[batch, seq, num_types]
        tokens=None,
        epoch: float = None,       # curriculum 策略時，傳入進度（例如 0~1 或 epoch 數）
        current_type: int = None,    # sequential 策略時，指定當前 type_order 的索引
        **kwargs
    ):
        # 若有 agg_weights，確保其在正確的裝置上
        if self.agg_weights is not None and self.agg_weights.device != self.device:
            self.agg_weights = self.agg_weights.to(self.device)

        return_dict = True
        output_attentions = True
        output_hidden_states = True

        # 呼叫 bert 模組，不將 aggregation、epoch 等額外參數傳入
        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
            # **kwargs  # 如果 kwargs 中還有其他參數，請視需求決定是否傳入
        )

        sequence_output = outputs[0]
        logits = self.classifier(sequence_output)
        
        loss = None
        if labels is not None:
            loss_fct = torch.nn.CrossEntropyLoss(reduction='none')
            token_loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
            token_loss = token_loss.view(input_ids.size(0), -1)
            '''
            print(token_loss.shape)
            print(aggregation.shape)
            print(aggregation)
            '''
            
            if aggregation is None:
                loss = token_loss.mean()
            else:
                if self.strategy == 'mix':
                    # self.agg_weights fixed on device
                    if self.agg_weights.device != aggregation.device:
                        self.agg_weights = self.agg_weights.to(aggregation.device)
                    agg_type_tensor = aggregation.type_as(self.agg_weights)
                    apply_weights = torch.matmul(agg_type_tensor, self.agg_weights)
                    weighted_loss = apply_weights * token_loss.sum(dim=1)
                    weighted_loss = weighted_loss.mean()
                    loss = weighted_loss

                elif self.strategy == 'sequential':
                    if current_type is None or current_type < 0 or current_type >= len(self.type_order):
                        raise ValueError("sequential 策略需要傳入正確的 current_type 參數")
                    current_type_name = self.type_order[current_type]
                    mask = aggregation[:, :, AGG_MAP[current_type_name]]
                    if mask.sum() > 0:
                        loss = (token_loss * mask).sum() / mask.sum()
                    else:
                        loss = token_loss.mean()

                elif self.strategy == 'curriculum':
                    
                    agg_weights = [0.] * len(AGG_MAP)
                    if epoch is None:
                        raise ValueError("curriculum 策略需要傳入 epoch 參數")
                    # 目前只支援兩種 type 的情形
                    if len(self.type_order) == 1:
                        w = get_curriculum_weight(epoch)
                        agg_weights[AGG_MAP[self.type_order[0]]] = w

                    elif len(self.type_order) == 2:
                        w = get_curriculum_weight(epoch)
                        agg_weights[AGG_MAP[self.type_order[0]]] = w
                        agg_weights[AGG_MAP[self.type_order[1]]] = 1 - w
                        
                    else:
                        raise NotImplementedError("目前只支援 1 或 2 種類型的情形")

                    weights = torch.tensor(agg_weights).to(self.device) 
                    apply_weights = torch.matmul(aggregation.type_as(weights), weights)
                    weighted_loss = apply_weights * token_loss.sum(dim=1)
                    weighted_loss = weighted_loss.mean()
                    
                    loss = weighted_loss
                else:
                    loss = token_loss.mean()

        return TokenClassifierOutput(
            loss=loss,
            logits=logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )
