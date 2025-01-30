# Command line instructions

You can also upload existing files from your computer using the instructions below.

### Git global setup
```git
git config -- global user.name "Xxxxxx Xxxxxxx"
git config -- global user.email "xx@gmail.com"
```
### Create a new repository
```git
git clone https://gitlab.com/xxxxxxxx/cicd-exemplo1.git
cd cicd-exemplo1
git switch -c main
touch README.md
git add README.md
git commit -m "add README"
git push -u origin main
```

### Push an existing folder
```git
cd existing_folder
git init -- initial-branch=main
git remote add origin https://gitlab.com/xxxxxxxx/cicd-exemplo1.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

### Push an existing Git repository
```git
cd existing_repo
git remote rename origin old-origin
git remote add origin https://gitlab.com/xxxxxxxx/cicd-exemplo1.git
git push -u origin -- all
git push -u origin -- tags
```
