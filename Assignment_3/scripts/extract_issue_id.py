import pandas as pd

EXCEL_FILE = "../data/Issues.xlsx"

# Show all sheet names
xls = pd.ExcelFile(EXCEL_FILE)

print("\nAvailable Sheets:")
for sheet in xls.sheet_names:
    print(f" - {sheet}")

# Change this after checking the sheet names
SHEET_NAME = "Lucene"

df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)

print("\nColumns:")
print(df.columns.tolist())

# Adjust column name if needed
issue_col = "Issue ID"

issue_ids = (
    df[issue_col]
    .dropna()
    .astype(str)
    .str.strip()
)

total_issues = len(issue_ids)
unique_issues = issue_ids.nunique()

print(f"\nTotal issues   : {total_issues}")
print(f"Unique issues  : {unique_issues}")
print(f"Duplicates     : {total_issues - unique_issues}")

# Save issue IDs
output_file = "../data/lucene_issue_ids.txt"

issue_ids.drop_duplicates().to_csv(
    output_file,
    index=False,
    header=False
)

print(f"\nSaved issue IDs to: {output_file}")

print("\nFirst 10 issue IDs:")
print(issue_ids.head(10).tolist())