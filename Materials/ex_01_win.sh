#!/bin/bash

#1)
mkdir server
cd server
git init --bare

#2)
cd ..
git clone server/ client1
git clone server/ client2

#3)
cd client1
mkdir src
echo -e "data" > .gitignore
echo -e "This is my readme file" > README.md
echo -e "do_nothing <- function(x) {\n invisible(NULL)\n}" > src/fun-do_nothing.R

#4)
git add .gitignore README.md src/fun-do_nothing.R
git commit -m "Initial Commit"
git push
cd ../client2
git pull
git branch feat/website

#5)
git checkout feat/website
mkdir html
echo -e "<html>\nThis is a stub file\n</html>" > html/index.html

#6)
git add html/index.html
git commit -m "Added website stub"
git push
git push --set-upstream origin feat/website

#7)
cd ../client1
git pull

#8)
echo -e "do_something <- function(x) {\n  x+1 \n}" > src/fun_do-something.R
git add src/fun_do-something.R
git commit -m "Added function do_something"
git push

#9)
cd ../client2
git checkout master
git pull

#10)
git checkout feat/website
git rebase master
git push #ouch
git push --force
