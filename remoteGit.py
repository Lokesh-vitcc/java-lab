import json
import base64
import os
from git import Repo
from getpass import getpass,getuser
from cryptography.fernet import Fernet
from datetime import datetime
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import argparse

def ParseArgs():
    # vincentHelper tool comming up XD
    parser = argparse.ArgumentParser(prog="remoteGit",description="This program helps students to update their repos\nfrom the comfort of lab computer safely!")
    parser.add_argument('cmd',nargs="?",help=" commands: push")
    parser.add_argument('-a','--pushAll',action='store_true',help="commit and push everything from the repo root")
    parser.add_argument('-r','--resetCreds',action='store_true',help=" create/reset credentials for git user and also this program\'s password")
    parser.add_argument('-v','--viewCreds',action='store_true',help="Show all encrypted configs (caution sensitive data will be printed out)")
    parser.add_argument('-m','--commitMessage',help="adds your message along with default commit message")

    return parser

def keyGen(passwd):
    salt = b'\xc6\xd0B\xbc_\xcf\x14\xdc\xa4\xe0\x036\xd2\xcb\xa8)'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(passwd.encode()))

def decrypt():
    fernet = Fernet(keyGen(getpass(prompt="password (helper):")))
    with open(cred_file,'rb') as f:
        try:
            creds = fernet.decrypt(f.read())
        except:
            print("Invalid password")
            exit()

    return json.loads(creds.decode())

parser = ParseArgs()
args = parser.parse_args()
cred_file = ".creds"

if (args.resetCreds):
    creds={}
    # user inputs
    creds["username"] = input("username (git):")
    creds["token"] = getpass(prompt="password (git):")
    passwd = getpass(prompt="password (helper):")

    # processing
    fernet = Fernet(keyGen(passwd))
    data = json.dumps(creds).encode()
    del creds
    data = fernet.encrypt(data)
    with open(cred_file,"wb") as f:
        f.write(data)
    print("credentials updated!")
    exit()
elif (args.viewCreds):
    creds = decrypt()
    print("\n".join("\t".join(x) for x in creds.items()))
    exit()
elif (args.cmd=="push"):
    creds = decrypt()
    repo = Repo()

    now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    COMMIT_MESSAGE=f"automated commit By script @ {now} from PC: {os.getlogin()}."
    if (msg:=args.commitMessage):
        COMMIT_MESSAGE+=f"\nAdditional message: {msg}"
    untracked_dirs=["JAVA","scripts"]
    with repo.git.custom_environment(GIT_ASKPASS="echo", GIT_USERNAME=creds['username'], GIT_PASSWORD=creds["token"]):
        # add untracked files of specific dirs to staging area
        logs=""
        logs+=repo.git.add(*untracked_dirs,A=True)
        # and also add modifications on all tracked files to staging area
        if args.pushAll:
            logs +=repo.git.add(A=True)
        else:
            logs +=repo.git.add(update=True)
        
        # commit changes and push
        # logs +=
        repo.index.commit(COMMIT_MESSAGE)
        logs += repo.git.push()
    # Clean up
    del creds
    print(logs)
    print("Pushed successfully")
else:
    print("Invalid syntax")
    parser.print_help()
