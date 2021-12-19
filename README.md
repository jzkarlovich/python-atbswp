# Automate The Boring Stuff With Python

This repository will serve as a place to write notes and store code while reading the book "Automate The Boring Stuff with Python".  I will write my code in Visual Studio and upload it to GitHub while following along with the examples. 

TO DO:
1. ~~Figure out how to write Python in visual studio.~~
2. Create Subsections for each chapter. Notes will be store in .txt files. 
3. Create virtual environments to write code and keep packages seperate from global interpreter. 
4. ~~Is ther a way to auto set .ssh passphrase for git?~~ 
5. Set LaTeX typesetting in Visual Studio and convert .md files (or readme files to LaTeX)
6. Look to add Vim settings to visual studio for writing and editing. 


## Git Commands
Local Git Workflow:

Write Code --> Stage Changes 'git add .' --> Commit Changes 'git commit -m ""' --> Push Change 'git push'

- git clone = copy from host
- git add = track files changes in git
- git commit = save files in git
- git push = upload git files to repo (GitHub)
- git pull = download changes form remote repo to local host

````
git clone git@github.com:jzkarlovich/REPO
cd REPO
git init
git remote add git@github.com:jzkarlovich/REPO main
git remote -v
git status
git remote pull git@github.com:jzkarlovich/REPO main
git add .
git commit -m "MESSAGE"
git status
git push origin main
````

## Testing Section
- [X] Trying to set ssh passphrase.  Started 'start-ssh-agent' after 'ssh-add'.
- [X] Make a change on GitHub and pull. 
