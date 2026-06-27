import json
import time
import requests
import pandas as pd
from tqdm import tqdm

EXCEL_FILE = "data/Issues.xlsx"
SHEET_NAME = "Lucene"

df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)

issue_ids = (
    df["Issue ID"]
    .dropna()
    .astype(str)
    .str.strip()
    .unique()
)

BASE_URL = "https://issues.apache.org/jira/rest/api/latest/issue/"

all_issues = []

for idx, issue_id in enumerate(tqdm(issue_ids)):

    try:
        response = requests.get(
            BASE_URL + issue_id,
            timeout=20
        )

        if response.status_code != 200:
            print(f"Failed: {issue_id}")
            continue

        issue = response.json()

        fields = issue["fields"]

        parent = None

        if fields.get("parent"):
            parent = fields["parent"]["key"]

        comments = []

        if fields.get("comment"):

            for c in fields["comment"]["comments"]:

                author = "Unknown"

                if c.get("author"):
                    author = c["author"].get(
                        "displayName",
                        "Unknown"
                    )

                comments.append({
                    "author": author,
                    "created": c.get("created"),
                    "body": c.get("body")
                })

        record = {
            "issue_id": issue_id,
            "summary": fields.get("summary"),
            "description": fields.get("description"),
            "status": fields.get("status", {}).get("name"),
            "issue_type": fields.get("issuetype", {}).get("name"),
            "parent": parent,
            "num_comments": len(comments),
            "comments": comments
        }

        all_issues.append(record)

        # Save every 100 issues
        if idx % 100 == 0:

            with open(
                "data/lucene_issues_partial.json",
                "w",
                encoding="utf-8"
            ) as f:
                json.dump(
                    all_issues,
                    f,
                    indent=2,
                    ensure_ascii=False
                )

        time.sleep(0.1)

    except Exception as e:
        print(issue_id, e)

with open(
    "data/lucene_issues_raw.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        all_issues,
        f,
        indent=2,
        ensure_ascii=False
    )

print(f"\nDownloaded {len(all_issues)} issues")