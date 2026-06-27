import json
from collections import Counter
import pandas as pd

with open("data/lucene_issues_processed.json", encoding="utf-8") as f:
    issues = json.load(f)

counter = Counter()

for issue in issues:
    counter.update(issue["tokens"])

vocab_df = pd.DataFrame(
    counter.items(),
    columns=["token", "frequency"]
)

vocab_df = vocab_df.sort_values(
    by="frequency",
    ascending=False
)

vocab_df.to_csv(
    "data/vocabulary.csv",
    index=False
)

print("Vocabulary size:", len(counter))
print("\nTop 30 tokens:\n")
print(vocab_df.head(30))