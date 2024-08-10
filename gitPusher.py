import json
import base64
import os
from git import Repo
from getpass import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def keyGen(passwd):
    salt = b'\xc6\xd0B\xbc_\xcf\x14\xdc\xa4\xe0\x036\xd2\xcb\xa8)'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(passwd.encode()))

# Define your personal access token, username, and repository name
# token = getpass()
# key = getpass()
key="MyGitPass"
fernet = Fernet(keyGen(key))
creds = fernet.decrypt(open(".creds").read().encode()).decode()
creds = json.loads(creds)
# print(creds)
# exit()
repo = Repo()
remote_url = repo.remotes.origin.url
# Temporarily set the remote URL using custom environment
COMMIT_MESSAGE="Test message another time"
untracked_dirs=["JAVA","scripts"]

with repo.git.custom_environment(GIT_ASKPASS="echo", GIT_USERNAME=creds['username'], GIT_PASSWORD=creds["token"]):
    # add untracked files of specific dirs to staging area
    # and also add modifications on all tracked files to staging area
    
    repo.git.add("JAVA",".",A=True)
    repo.index.commit(COMMIT_MESSAGE)
    repo.git.push(remote_url)# , 'HEAD:refs/heads/main', '--force')
# Clean up (optional)
del creds
