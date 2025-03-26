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
        assert strategy in ['mix', 'cirriculum', 'sequential'], "strategy 必須在 ['mix', 'cirriculum', 'sequential'] 中"
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
            if isinstance(agg_weights_base, (int, float)):
                # 第一個權重固定為 1，其餘依序乘上 agg_weights_base 的次方
                self.agg_weights = torch.tensor([1.0] + [agg_weights_base**i for i in range(1, len(type_order))])
            else:
                self.agg_weights = torch.tensor(agg_weights_base)
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
        epoch: float = None,       # curriculum 策略時，需傳入 0~1 的進度值
        current_type: int = None,     # sequential 策略時，指定當前 type_order 的索引
        **kwargs
    ):
        # 將權重移至同一裝置
        if self.agg_weights is not None and self.agg_weights.device != self.device:
            self.agg_weights = self.agg_weights.to(self.device)

        return_dict = True
        output_attentions = True
        output_hidden_states = True

        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
            # **kwargs
        )

        sequence_output = outputs[0]
        logits = self.classifier(sequence_output)
        
        loss = None
        if labels is not None:
            # 使用不縮減(reduction='none')的 CrossEntropyLoss，以取得每個 token 的 loss
            loss_fct = torch.nn.CrossEntropyLoss(reduction='none')
            # 計算所有 token 的 loss (先展平，再還原成 [batch, seq])
            token_loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
            token_loss = token_loss.view(input_ids.size(0), -1)
            
            # 如果未傳入 aggregation（或格式不符），則直接取平均 loss
            if aggregation is None:
                loss = token_loss.mean()
            else:
                # 根據不同策略計算 loss
                if self.strategy == 'mix':
                    # mix 策略：對 type_order 中各類型 loss 加權累加
                    weighted_loss = 0.0
                    for i, type_name in enumerate(self.type_order):
                        # 取得該 type 在 aggregation tensor 中的通道（假設 AGG_MAP 定義中對應 index）
                        mask = aggregation[:, :, AGG_MAP[type_name]]
                        if mask.sum() > 0:
                            loss_i = (token_loss * mask).sum() / mask.sum()
                        else:
                            loss_i = 0.0
                        weighted_loss += self.agg_weights[i] * loss_i
                    loss = weighted_loss

                elif self.strategy == 'sequential':
                    # sequential 策略：僅使用 current_type 所對應的 loss
                    if current_type is None or current_type < 0 or current_type >= len(self.type_order):
                        raise ValueError("sequential 策略需要傳入正確的 current_type 參數")
                    current_type_name = self.type_order[current_type]
                    mask = aggregation[:, :, AGG_MAP[current_type_name]]
                    if mask.sum() > 0:
                        loss = (token_loss * mask).sum() / mask.sum()
                    else:
                        loss = token_loss.mean()
                elif self.strategy == 'cirriculum':
                    # curriculum 策略：根據進度動態調整各類型的權重
                    if epoch is None:
                        raise ValueError("curriculum 策略需要傳入 epoch 參數")

                    # 示範對三種類型的情形
                    if len(self.type_order) == 1:
                        weights = [1.0]
                    elif len(self.type_order) == 2:
                        weights = get_curriculum_weight(epoch), 1 - get_curriculum_weight(epoch)

                    else:
                        raise NotImplementedError("目前只支援 1 或 2 種類型的情形")
                    
                    '''
                    elif len(self.type_order) == 3:
                        if progress <= 0.5:
                            # progress 介於 0~0.5：從 (1, 0, 0) 線性過渡到 (0.2, 0.8, 0)
                            weights = [1 - 1.6 * progress, 1.6 * progress, 0.0]
                        else:
                            # progress 介於 0.5~1：從 (0.2, 0.8, 0) 線性過渡到 (0, 0, 1)
                            q = (progress - 0.5) / 0.5
                            weights = [0.2 * (1 - q), 0.8 * (1 - q), q]
                    else:
                        # 若 type_order 數量不為 1、2、3，可採用第一個和最後一個做線性插值，中間設定為 0
                        weights = [1 - progress] + [0.0]*(len(self.type_order)-2) + [progress]
                    '''
                    
                    final_loss = 0.0
                    for i, type_name in enumerate(self.type_order):
                        mask = aggregation[:, :, AGG_MAP[type_name]]
                        if mask.sum() > 0:
                            loss_i = (token_loss * mask).sum() / mask.sum()
                        else:
                            loss_i = 0.0
                        final_loss += weights[i] * loss_i
                    loss = final_loss
                else:
                    # 若策略未定義，取平均 loss
                    loss = token_loss.mean()

        return TokenClassifierOutput(
            loss=loss,
            logits=logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )

