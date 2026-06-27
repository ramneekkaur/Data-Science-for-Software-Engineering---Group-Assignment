import json

BOT_USERS = {
    "Hive QA",
    "cnsgithub",
    "TrafficServer Bot",
    "Mail Delivery Subsystem",
    "ASF Subversion and Git Services",
    "Hadoop QA",
    "QABot from busbey",
    "Thomas Smets - A3 SYSTEM",
    "ATLAS QA",
    "m",
    "Flink Jira Bot",
    "ASF IRC Bot",
    "Beam JIRA Bot",
    "tester",
    "Mahout QA",
    "Laurent Chabot",
    "TezQA",
    "FAURE SYSTEMS",
    "SentryQA",
    "Bug Reporter",
    "Chris Chabot",
    "Ignite TC Bot",
    "asapsystems",
    "rangerqa",
    "Flume QA",
    "Knox QA",
    "Giraph QA",
    "Jerry Chabot",
    "Sqoop QA Bot",
    "apache@tingo.org",
    "GitHub Import",
    "Tajo QA",
    "Hudson",
    "ASF GitHub Bot",
    "genericqa"
}

with open("data/lucene_issues_raw.json", encoding="utf-8") as f:
    issues = json.load(f)

removed_comments = 0

for issue in issues:

    filtered_comments = []

    for comment in issue["comments"]:

        if comment["author"] in BOT_USERS:
            removed_comments += 1
            continue

        filtered_comments.append(comment)

    issue["comments"] = filtered_comments
    issue["num_comments"] = len(filtered_comments)

with open(
    "data/lucene_issues_clean.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        issues,
        f,
        indent=2,
        ensure_ascii=False
    )

print(f"Removed bot comments: {removed_comments}")
print(f"Issues processed: {len(issues)}")