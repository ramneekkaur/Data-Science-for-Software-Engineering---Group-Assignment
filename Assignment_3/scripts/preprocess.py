import json
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

STOP_WORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()

with open("data/lucene_issues_clean.json", encoding="utf-8") as f:
    issues = json.load(f)

processed_issues = []

for issue in issues:

    summary = issue.get("summary") or ""
    description = issue.get("description") or ""

    text = summary + " " + description

    text = text.lower()

    # remove urls
    text = re.sub(r"http\S+", " ", text)

    # keep only letters/numbers
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    tokens = word_tokenize(text)

    tokens = [
        token
        for token in tokens
        if token not in STOP_WORDS
        and len(token) > 2
    ]

    tokens = [
        LEMMATIZER.lemmatize(token)
        for token in tokens
    ]

    issue["tokens"] = tokens

    processed_issues.append(issue)

with open(
    "data/lucene_issues_processed.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        processed_issues,
        f,
        indent=2,
        ensure_ascii=False
    )

print("Processed issues:", len(processed_issues))

print("\nSample tokens:\n")
print(processed_issues[0]["tokens"][:30])