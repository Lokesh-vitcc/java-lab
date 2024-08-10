from git import Repo
from collections import defaultdict

def get_creation_timestamps(repo_path):
    repo = Repo(repo_path)
    creation_times = defaultdict(lambda: None)  # Default to None if not found

    for commit in repo.iter_commits('main'):  # Change 'master' to your branch name if needed
        for entry in commit.tree.traverse():
            if entry.type == 'blob':  # Only interested in files
                if creation_times[entry.path] is None:
                    creation_times[entry.path] = commit.committed_date

    return creation_times

def format_timestamp(epoch_time):
    import datetime
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')

repo_path = '.'  # Change this to your repository path
timestamps = get_creation_timestamps(repo_path)

for file_path, timestamp in timestamps.items():
    print(f"File: {file_path}, Creation Timestamp: {format_timestamp(timestamp)}")
