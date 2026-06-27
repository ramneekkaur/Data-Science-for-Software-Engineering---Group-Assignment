import json
import requests

TEST_ISSUES = [
    "LUCENE-620",
    "LUCENE-12",
    "LUCENE-17",
    "LUCENE-45",
    "LUCENE-50"
]

BASE_URL = "https://issues.apache.org/jira/rest/api/latest/issue/"

all_issues = []

for issue_id in TEST_ISSUES:

    print(f"Downloading {issue_id}...")

    try:
        response = requests.get(BASE_URL + issue_id)

        if response.status_code != 200:
            print(f"Failed: {issue_id}")
            print(response.status_code)
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
                    author = c["author"].get("displayName", "Unknown")

                comments.append({
                    "author": author,
                    "created": c.get("created"),
                    "body": c.get("body")
                })

        issue_record = {
            "issue_id": issue_id,
            "summary": fields.get("summary"),
            "description": fields.get("description"),
            "status": fields.get("status", {}).get("name"),
            "issue_type": fields.get("issuetype", {}).get("name"),
            "parent": parent,
            "num_comments": len(comments),
            "comments": comments
        }

        all_issues.append(issue_record)

    except Exception as e:
        print(issue_id, e)

with open("../codebase/data/test_issues.json", "w", encoding="utf-8") as f:
    json.dump(all_issues, f, indent=2, ensure_ascii=False)

print("\nSaved test data.")