from github import Github
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

g = Github("")
repo_owner = 'vercel'
repo_name = 'vercel'

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
print(df_commits.duplicated().sum())
df_commits = df_commits.drop_duplicates()
print(df_commits.duplicated().sum())
df_commits.to_csv("commits_data_cleaned.csv", index=False)

df_2023 = pd.DataFrame(df_commits[df_commits['author_date'].dt.year == 2023])
print(df_2023.head())

df_2023['author_date'] = pd.to_datetime(df_2023['author_date'])
df_2023['committer_date'] = pd.to_datetime(df_2023['committer_date'])
print(df_2023.dtypes)
df_2023['year'] = df_2023['author_date'].dt.year
df_2023['month'] = df_2023['author_date'].dt.month
df_2023.to_csv("commits_data_preprocessed.csv", index=False)
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
plt.close()

df_2023['day_of_week'] = df_2023['author_date'].dt.dayofweek
commits_per_day_of_week = df_2023['day_of_week'].value_counts().sort_index()
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
commits_per_day_of_week.index = day_names
plt.figure(figsize=(10, 6))
plt.bar(commits_per_day_of_week.index, commits_per_day_of_week.values, color='skyblue')
plt.title('Number of Commits per Day of the Week in 2023')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Commits')
plt.grid(axis='y')
plt.show()
plt.close()

df_2023['hour_of_day'] = df_2023['author_date'].dt.hour
commits_per_hour = df_2023['hour_of_day'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.bar(commits_per_hour.index, commits_per_hour.values, color='skyblue')
plt.title('Number of Commits per Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Commits')
plt.xticks(range(24))
plt.grid(axis='y')
plt.show()
plt.close()

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
plt.close()

keywords = ["fix", "add", "update", "remove", "rename", "refactor", "test", "merge", "release", "build"]
def count_keywords(message, keywords):
    message = message.lower()
    return {keyword: message.count(keyword) for keyword in keywords}

df_2023['keyword_counts'] = df_2023['message'].apply(lambda x: count_keywords(x, keywords))
keyword_totals = Counter()
for counts in df_2023['keyword_counts']:
    keyword_totals.update(counts)
    plt.figure(figsize=(10, 6))
plt.bar(keyword_totals.keys(), keyword_totals.values(), color='skyblue')
plt.title('Frequency of Keywords in Commit Messages')
plt.xlabel('Keyword')
plt.ylabel('Frequency')
plt.show()
plt.close()

df_2023['message_length'] = df_2023['message'].apply(len)
average_length = df_2023['message_length'].mean()
print(f"Average commit message length: {average_length:.2f} characters")
plt.figure(figsize=(10, 6))
plt.hist(df_2023['message_length'], bins=30, color='skyblue', edgecolor='black')
plt.axvline(average_length, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {average_length:.2f} chars')
plt.title('Distribution of Commit Message Lengths')
plt.xlabel('Message Length (characters)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
plt.close()

df_2023['month_year'] = df_2023['author_date'].dt.strftime('%Y-%m')
keyword_trends = {keyword: [] for keyword in keywords}
dates = sorted(df_2023['month_year'].unique())
for date in dates:
    df_month = df_2023[df_2023['month_year'] == date]
    monthly_counts = Counter()
    for counts in df_month['keyword_counts']:
        monthly_counts.update(counts)
    for keyword in keywords:
        keyword_trends[keyword].append(monthly_counts[keyword])

plt.figure(figsize=(12, 6))
for keyword in keywords:
    plt.plot(dates, keyword_trends[keyword], marker='o', label=keyword)

plt.title('Keyword Trends in Commit Messages Over Time')
plt.xlabel('Time (Month-Year)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()
plt.close()