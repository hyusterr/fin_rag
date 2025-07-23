import json
from collections import Counter, defaultdict
import pandas as pd

# Path to your JSONL where each line has keys 'naive_aggregation', 'loose_aggregation', etc.
INPUT_FILE = "aggregate.jsonl"

# The aggregation schemes present in each record
AGG_KEYS = ["naive_aggregation", "loose_aggregation", "strict_aggregation",
            "harsh_aggregation", "complex_aggregation"]

# Counters for each scheme
counts = {agg: Counter() for agg in AGG_KEYS}
total_tokens = Counter()

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        rec = json.loads(line)
        for agg in AGG_KEYS:
            labels = rec[agg]["label"]
            # count each token's label
            for lab in labels:
                counts[agg][lab] += 1
            total_tokens[agg] += len(labels)

# Build a DataFrame for easy viewing
rows = []
for agg in AGG_KEYS:
    c = counts[agg]
    tot = total_tokens[agg]
    rows.append({
        "Aggregation": agg.replace("_aggregation","").capitalize(),
        "Total tokens": tot,
        "Count=1": c[1],
        "Count=0": c[0],
        "Count=None": c.get(None, 0),
        "Pct=1": c[1] / tot if tot else 0,
        "Pct=0": c[0] / tot if tot else 0,
        "Pct=None": c.get(None, 0) / tot if tot else 0,
    })

df = pd.DataFrame(rows)
print(df.to_markdown(index=False))

