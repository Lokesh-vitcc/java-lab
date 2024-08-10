import os
from git import Repo
from getpass import getpass


# Define your personal access token, username, and repository name
token = getpass()
username = "Lokesh-Spectre"
repo_name = ""

# Local repository path
repo_dir = "/path/to/your/local/repo"

# Initialize the repository object
repo = Repo()

# Define the remote URL with the token
remote_url = "https://github.com/Lokesh-vitcc/java-lab.git"

# Temporarily set the remote URL using custom environment
with repo.git.custom_environment(GIT_ASKPASS="echo", GIT_USERNAME=username, GIT_PASSWORD=token):
    # Perform the push using the temporary remote URL
    repo.git.push(remote_url, 'HEAD:refs/heads/main', '--force')

# Clean up (optional)
del token
