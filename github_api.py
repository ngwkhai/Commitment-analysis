from github import Github
import pandas as pd
import matplotlib.pyplot as plt

g = Github("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")
repo_owner = 'electron'
repo_name = 'electron'

repo = g.get_repo(f"{repo_owner}/{repo_name}")
prs = repo.get_commits()

commit_data = []
for pr in prs:
    print(pr.last_modified_datetime)
    commit_info = {
        "sha": pr.sha,
        "author": pr.commit.author.name,
        "author_date": pr.commit.author.date,
        "committer": pr.commit.committer.name,
        "committer_date": pr.commit.committer.date,
        "message": pr.commit.message,
    }
    commit_data.append(commit_info)

df_commits = pd.DataFrame(commit_data)
df_commits.to_csv("commits_data.csv", index=False)
print(df_commits.head())

print(df_commits.isnull().sum())
df_commits = df_commits.dropna()
print(df_commits.isnull().sum())
df_commits.to_csv("commits_data_cleaned.csv", index=False)

df_commits['author_date'] = pd.to_datetime(df_commits['author_date'])
df_commits['committer_date'] = pd.to_datetime(df_commits['committer_date'])
print(df_commits.dtypes)

df_commits['year'] = df_commits['author_date'].dt.year
df_commits['month'] = df_commits['author_date'].dt.month
df_commits.to_csv("commits_data_preprocessed.csv", index=False)
print(df_commits.head())

df_2023 = df_commits[df_commits['author_date'].dt.year == 2023]
print(df_2023.head())

commits_per_month_2023 = df_2023.groupby(df_2023['author_date'].dt.month).size()
print(commits_per_month_2023)
plt.figure(figsize=(10, 6))
plt.plot(commits_per_month_2023.index, commits_per_month_2023.values, marker='o')
plt.title('Number of Commits per Month in 2023')
plt.xlabel('Month')
plt.ylabel('Number of Commits')
plt.xticks(commits_per_month_2023.index)
plt.grid(True)
plt.show()

commits_per_author_2023 = df_2023['author'].value_counts()
print(commits_per_author_2023.head(10))
plt.figure(figsize=(10, 6))
plt.bar(commits_per_author_2023.index[:10], commits_per_author_2023.values[:10], color='skyblue')
plt.title('Top 10 Authors by Number of Commits in 2023')
plt.xlabel('Author')
plt.ylabel('Number of Commits')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

fix_commits_2023 = df_2023[df_2023['message'].str.contains("fix", case=False)]
print(len(fix_commits_2023))