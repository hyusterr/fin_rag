import json
import argparse
from statistics import mean

def compute_expert_stats(input_path):
    spans_per_para = []
    span_lengths = []
    highlighted_tokens = []

    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            spans = [span.strip() for span in data.get('highlight', '').split('|||') if span.strip()]
            spans_per_para.append(len(spans))
            lengths = [len(span.split()) for span in spans]
            span_lengths.extend(lengths)
            highlighted_tokens.append(sum(lengths))

    stats = {
        'Avg spans per paragraph': mean(spans_per_para),
        'Avg span length (tokens)': mean(span_lengths) if span_lengths else 0,
        'Avg highlighted tokens per paragraph': mean(highlighted_tokens)
    }
    return stats

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compute expert annotation statistics.")
    parser.add_argument('--input', help='Path to the expert annotation JSONL file')
    args = parser.parse_args()

    stats = compute_expert_stats(args.input)
    for k, v in stats.items():
        print(f"{k}: {v:.3f}")

