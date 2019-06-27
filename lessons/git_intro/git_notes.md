## Intro to Git & Github

#### Making local Git Commits

**git init**: initialize a git directory

**git add {file_name}**: add a file to the staging area

**git status**: shows current status of staging area 

**git commit -m 'comment'**: commit staging area and add it to repository with a comment detailing changes. -m for commenting within terminal, leaving out -m will open text editor

**git log**: shows a record of all commits made to repository

#### Reverting to prior Git Commit

**git log**: copy the commit key you wish to revert to

**git reset {key}**: prepares staging area to revert back to prior version

**git reset --hard {key}**: revert to prior version

### Github
* Github introduces a remote repository system where you can store your local repositories
* Allows for code-sharing

#### Push vs Pull
* **Push**: updates the remote version of the repository with current version of local repository
* **Pull**: brings any changes to the remote repository to local repository
* *** GitHub only modifies files that have CHANGEd since the last time you asked Git to track them. If a file is  not add-committed, it will not go to the remote version if if the code is pushed

### Connecting Local Repo to GitHub

**git remote add origin {github_url}**
 * remote: tells git this will be non-local version
 * add: tells git we are adding a new remote place to interface with 
 * origin: tells git that this remote place will be called 'origin' (this is convention)
 * {github_url}: specific to each repository

**git remote -v**: test to see if it connected. it should look like the following:  
origin	https://github.com/jc98924/test.git (fetch)
origin	https://github.com/jc98924/test.git (push)

**git push origin master**: pushes commit history to remote place 'origin' in the master branch


