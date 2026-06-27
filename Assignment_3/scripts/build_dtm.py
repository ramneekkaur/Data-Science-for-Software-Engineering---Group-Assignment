import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

with open("data/lucene_issues_processed.json", encoding="utf-8") as f:
    issues = json.load(f)

documents = [
    " ".join(issue["tokens"])
    for issue in issues
]

vectorizer = CountVectorizer()

dtm = vectorizer.fit_transform(documents)

dtm_df = pd.DataFrame(
    dtm.toarray(),
    columns=vectorizer.get_feature_names_out()
)

dtm_df.to_csv(
    "data/document_term_matrix.csv",
    index=False
)

print("DTM shape:", dtm_df.shape)