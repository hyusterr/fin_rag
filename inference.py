from transformers import AutoTokenizer, AutoModelForTokenClassification
from pathlib import Path
from utils.utils import read_jsonl
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForTokenClassification.from_pretrained("mix_all_bert/checkpoint-3432/")


DATA_DIR = Path('annotation/annotated_result/all/')
TRAIN_DATA = DATA_DIR / 'aggregate_train.jsonl'
TEST_DATA = DATA_DIR / 'aggregate_test.jsonl'
EXPERT_DATA = DATA_DIR / 'expert_annotated_test.jsonl'

train_data = read_jsonl(TRAIN_DATA)
test_data = read_jsonl(TEST_DATA)
expert_data = read_jsonl(EXPERT_DATA)

test_x = [d['tokens'] for d in test_data]
pred_y = []
for x in test_x:
    with torch.no_grad():
        inputs = tokenizer(x, padding=True, truncation=True, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        predictions = torch.argmax(logits, dim=2)
        pred_y.append(predictions[0].cpu().numpy())

for i, d in enumerate(test_data):
    print(d['tokens'])
    print(pred_y[i])
    print(d['naive_aggregation']['label'])


