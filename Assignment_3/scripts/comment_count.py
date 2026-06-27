import json

with open("data/lucene_issues_raw.json", encoding="utf-8") as f:
    issues = json.load(f)

print("Issues:", len(issues))

missing_desc = sum(
    1 for i in issues
    if not i.get("description")
)

print("Missing descriptions:", missing_desc)

total_comments = sum(
    i["num_comments"]
    for i in issues
)

print("Total comments:", total_comments)