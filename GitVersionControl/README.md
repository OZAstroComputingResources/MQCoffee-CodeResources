# GIT VERSION CONTROL 

#### Once Git is installed you can initialise a name and an email address to 'sign' the commits.

`git config --global user.name "your-name"`
`git config --global user.email your-name@mq.edu.au`




### Basic Commands

#### Setup a directory

`mkdir news`
`cd news`

#### To initialise a git repository

`git init`

#### To check if it worked find a .git directory

`ls -a`

#### Use an editor to add some text to a file.
#### If you are unsure of a text editor try nano.

`nano fake-news.txt`

'''

Lochness Monster was sighted in China.

'''

#### We have now created a text file in out git repository but we haven't told git to record the changes.

`git status`

#### If we want to commit this file we first have to add it to the commit

`git add fake-news.txt`

#### Now to commit the changes.

`git commit`

#### Deleting and moving files

`git rm`

`git mv`


### Comparing to previous versions

#### To see the commit log

`git log`

#### To compare differences you need to specify the reference number from the git log

`git diff 9ac1f1648573bf25b521622304a8bc0b0c3be902`

#### You can also have a GUI to look at your commit history.

`gitk`

#### You can use blame to see the date, time, user and which commit each line was modified.

`git blame fake-news.txt`


### Breaching & Merging 

#### To make a new branch

`git branch executive-order`

#### By default we start out on master. Now we need to change to the new branch

`git checkout executive-order`

#### Now we can add some more text

'''

Bunyip tracks found on Hawaiian beach

'''

#### Now compare to the master

`git diff master`

#### To merge our branch with master we need to checkout the master branch

`git checkout master`

`git merge executive-order`

#### To delete a branch
`git merge -d executive-order`


#### Dealing with Conflicts

#### If you have a conflict a message will show:

""" 
Auto-merging fake-news.txt
CONFLICT (content): Merge conflict in fake-news.txt
Automatic merge failed; fix conflicts and then commit the result.
"""

#### In the files you will see arrows like these.
`"""

<<<<<<< HEAD
Yeti tracks found on Hawaiian beach. Shocking!!!
=======
Yeti tracks found on Hawaiian beach. Smashing!!!
>>>>>>> executive-order

"""`

#### Everything between <<<< and ==== is in your HEAD repository and everything between ==== and >>>> is in the repository you are merging from.
