#!/bin/sh
# Shell script to create git repo

dir="repo2"
if [ ! -d ${dir} ]
then
	mkdir ./${dir}
	echo "Folder '${dir}' created"
	cd ${dir}
fi

# Create git repo if not exists
if [ ! -d .git ]
then
	git init
fi

for i in {1..5}
do
	touch ${i}
	git add ${i}
	git commit -m "${i}"
done

# Creating 3 commits on branch feature
COMMIT_ID=$(git log --oneline | tail -1 | cut -c1-7)
git branch feature ${COMMIT_ID}

# Switch to feature branch
git checkout feature
for i in {6..8}
do
	touch ${i}
	git add ${i}
	git commit -m "${i}"
done

# Select commits 4 and 5 to be moved to branch feature
git checkout master

COMMITS=$(git log --oneline | tail -r | tail -2 | cut -c1-7)
git checkout feature
while read line;
do
	git cherry-pick $line
done <<< "${COMMITS}"
# Remove 4 and 5 from master
git checkout master
git reset --hard HEAD~2

git branch debug
git checkout debug
git checkout feature -- 7
git commit -m "9"
git reset HEAD 4 5

# Move master to commit 5 on feature
COMMIT=$(git log feature --oneline | head -n 1 | cut -c1-7)
git branch -f master ${COMMIT}

# Move feature back to commit 8
git checkout feature
git reset HEAD~2

cd ~


