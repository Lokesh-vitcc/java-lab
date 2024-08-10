from git import Repo

# PATH_OF_GIT_REPO = r'path\to\your\project\folder\.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo()
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except Exception as e:
        print(e)
        print('Some error occured while pushing the code')    

print(git_push())