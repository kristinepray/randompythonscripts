1a. Write a Ruby or Bash script that will print the usernames of all users on a Linux system
   together with their home directories.

#!/usr/bin/env
awk -F ':' '{print $1":"$6}' /etc/passwd

1b.

#!/usr/bin/env
touch /var/log/current_users
touch /var/log/user_changes
awk -F ':' '{print $1":"$6}' /etc/passwd | md5sum > /var/log/current_users
variable=$(diff /var/log/current_users /var/log/user_changes)
variable2=$(echo $variable | awk '{print $3}')
variable3=$(date)
variable4=$(grep $variable2 /var/log/user_changes)
if [ "$variable4" == "$variable2" ]; then
        echo "No changes"
else
echo "$variable2" "$variable3" "Changes occured" >> /var/log/user_changes
fi

1c.

0 * * * * /path/to/script.sh

2. 
A user is complaining that it's taking a long time to load a page on our
web application. In your own words, write down and discuss the possible
cause(s) of the slowness. Also describe how you would begin to troubleshoot
this issue.

a. Try and duplicate the issue
b. Is it images that run slow or all pages? Find a text page and see if its slow. Also check a page with images.
If its slow on images only you might want to disable the session state:
[SessionState(System.Web.SessionState.SessionStateBehavior.Disabled)]
c. check the logs to see if there are any errors
d. Check monitoring to see if there are any glaring problems like cpu or ram spikes.
e. Check the web.config file and see if debug is set to true. If it is set it to false.
f. Explore the possibility of replacing entity framework with dapper
g. Check for duplicate database queries and remove them
h. Look for unnecessary queries and joins
i. Look for loops in the coding and see if you can eliminate them
j. Disable ipv6
k. restart services

3. 
The Git commit graph below shows the output of `git log --all --decorate --oneline --graph`. What sequence of Git commands would result in this commit graph when starting from an empty directory?

```console
git init
git add .
git commit -am  "first commit"
git commit -am "second commit"
git checkout -b awesome_feature
git status <-- I just like to do this to make sure I am where I should be
git add .
git commit -am "third commit"
git checkout master
git merge awesome_feature
```

4. 
GitLab has hired you to write a Git tutorial for beginners on this topic:
Using Git to implement a new feature/change without affecting the main branch

Using Git to implement a new feature/change without affecting the main branch

You can use Git to introduce a new change without affecting the main branch. Its easy and this tutorial will show you how.

Step 1: Initialize a Git Repository

git init

It should look like this:

```console
[ec2-user]$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:   git config --global init.defaultBranch <name>
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:   git branch -m <name>
Initialized empty Git repository in /home/ec2-user/.git/
```
Step 2: Create a New Branch for Your Feature

Next, create a new branch to work on your feature or change. This keeps your work separate from the main branch (usually called master or main). Use the following command:

```console
[ec2-user]$ git checkout -b "awesome_feature"
```
Feel free to replace "awesome_feature" with any branch name you prefer.

The result should look like this:
```console
[ec2-user]$ git checkout -b "awesome_feature"
Switched to a new branch 'awesome_feature'
```
Step 3: Check Your Current Branch
To confirm that you're working in the correct branch, use the git status command:
```console
[ec2-user]$ git status
On branch awesome_feature
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .viminfo
        test1.sh~
nothing added to commit but untracked files present (use "git add" to track)
```
Step 4: Make Changes and Commit to Your Feature Branch
You can now make your changes or add your feature. Once you're ready to save your work, stage and commit the changes:
```console
[ec2-user]$ git add .
[ec2-user]$ git commit -m "third commit"
[awesome_feature 7573b9a] third commit
Committer: EC2 Default User
 3 files changed, 70 insertions(+)
```
Step 5: Merge the Feature Branch (When Ready)
When your feature is complete and you’re ready to integrate it into the main branch, you can switch back to the main branch and merge your feature:
```console
git checkout master
git merge awesome_feature
```

For additional help you can read these articles:

[Branches](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
[Branches and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)


5. What is a technical book/blog/course/etc. you experienced recently or in the past that you enjoyed?
I took the security plus certification recently. These flashcards were really helpful:
[Udemy](https://www.udemy.com/course/new-comptia-security-sy0-701-practice-tests/?srsltid=AfmBOorS66uCjcR8Dayw-gyGU1R_ufzUmLnqWd7ACXfyiCqopUeJjn5t&fbclid=IwY2xjawIYQrtleHRuA2FlbQIxMAABHYjDnOmKIg4r7h_kBXH-sQyAub7Ax0qb6nkBdoyC2J4eVuXISXVN3UyvkQ_aem_J2Lk3qsI2Kyzb46V5jJVzg&couponCode=PLOYALTY0923)
I feel that these flashcards were a key to helping me pass the course.

Currently I am studying for my AWS Certified Cloud Practitioner. So far this course has been super helpful. It has hands on lessons, cram sessions at the end of the chapters, pop quizes and practice exams:

[AWS Certified Cloud Practitioner](https://www.udemy.com/course/aws-certified-cloud-practitioner-training-course)