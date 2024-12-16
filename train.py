# from highlighter.base import BERTHighlighter
from utils.utils import read_jsonl

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import DataCollatorForTokenClassification, TrainingArguments, Trainer, EarlyStoppingCallback
from datasets import Dataset, load_dataset, DatasetDict
import evaluate
from pathlib import Path
import numpy as np

DATA_DIR = Path('annotation/annotated_result/all/')
TRAIN_DATA = DATA_DIR / 'aggregate_train.jsonl'
TEST_DATA = DATA_DIR / 'aggregate_test.jsonl'
EXPERT_DATA = DATA_DIR / 'expert_annotated_test.jsonl'

train_data = read_jsonl(TRAIN_DATA)
test_data = read_jsonl(TEST_DATA)
expert_data = read_jsonl(EXPERT_DATA)

def data_generator_mix_all(data_list):
    '''
    this means that one input data can have multiple aggregation labels
    x --> y1, y2, y3...
    if use in the validation set, it will be weird since a model can never predict right on multiple labels simultaneously
    '''
    
    for data in data_list:
        tokens = data['tokens']
        for key in data:
            if 'aggregation' in key:
                labels = data[key]['label']
                yield {'tokens': tokens, 'labels': labels}

def data_generator_expert(data_list):
    for data in data_list:
        id_ = list(data.keys())[0]
        tokens = data[id_]['tokens']
        texts = data[id_]['text']
        labels = data[id_]['binary_labels']
        yield {'id': id_, 'tokens': tokens, 'texts': texts, 'labels': labels}


tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
def tokenize_and_align_labels(examples):
    tokenized_inputs = tokenizer(examples["tokens"], truncation=True, is_split_into_words=True)

    labels = []
    for i, label in enumerate(examples[f"labels"]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)  # Map tokens to their respective word.
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:  # Set the special tokens to -100.
            if word_idx is None:
                label_ids.append(-100)
            elif label[word_idx] is None: # for null in strict_aggregation
                label_ids.append(-100) 
            elif word_idx != previous_word_idx:  # Only label the first token of a given word.
                label_ids.append(label[word_idx])
            else:
                label_ids.append(-100)
            previous_word_idx = word_idx
        labels.append(label_ids)

    tokenized_inputs["labels"] = labels
    return tokenized_inputs



seqeval = evaluate.load("seqeval")
label_list = ['0', '1']
def compute_metrics(p):
    predictions, labels = p
    predictions = np.argmax(predictions, axis=2)

    true_predictions = [
        [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_labels = [
        [label_list[l] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]

    results = seqeval.compute(predictions=true_predictions, references=true_labels)
    return {
        "precision": results["overall_precision"],
        "recall": results["overall_recall"],
        "f1": results["overall_f1"],
        "accuracy": results["overall_accuracy"],
    }

# print(train_data[0])
'''
print(len(train_data[0]['tokens']))
for key in train_data[0]:
    if 'aggregation' in key:
        print(key)
        print(len(train_data[0][key]['label']))
'''

# wnut = load_dataset("wnut_17")
# print(type(wnut))
train_dataset = Dataset.from_generator(data_generator_mix_all, gen_kwargs={'data_list': train_data})
test_dataset = Dataset.from_generator(data_generator_mix_all, gen_kwargs={'data_list': test_data})
expert_dataset = Dataset.from_generator(data_generator_expert, gen_kwargs={'data_list': expert_data})
highlight_dataset = DatasetDict({'train': train_dataset, 'test': expert_dataset})
tokenized_datasets = highlight_dataset.map(tokenize_and_align_labels, batched=True)
data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)
model = AutoModelForTokenClassification.from_pretrained("bert-base-uncased", num_labels=2)

print(train_dataset[0])

training_args = TrainingArguments(
    output_dir="mix_all_bert",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=20,
    weight_decay=0.01,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)

# about specify devices: https://github.com/huggingface/transformers/issues/12570#issuecomment-876009872
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
    # processing_class=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
    callbacks = [EarlyStoppingCallback(early_stopping_patience=5)]
)

trainer.train()
