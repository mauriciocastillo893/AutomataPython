# AutomataPython
This is my project about an automaton in python. I hope you enjoy and understand these concepts with this program.

## Creating the virtual environment in python

**To create a virtual environment in python, we use the ** venv ** command**
`python3 -m venv .venv`

**Once the virtual environment is created, you can activate it with the next command line (Windows)**
`.venv/bin/activate`

**To desactivate the virtual environment, follow the next command line**
`deactivate`

*Suggestion: Use the name ".venv" to follow the Python convention.*

**To see what libraries we have in our project**
`pip list`

**To install our required libraries for this project (Not required, no data).**
`pip install <no_data>`



# Basic git-hub command lines to initialize a remote repository pointing to the local one.
Link your local repository to your GitHub repository:
`git remote add origin <URL_FROM_REPOSITORY>`

**Change 'main' to the name of your main branch if different**
`git branch -M main`
`git add <DOCUMENTS_TO_LAUNCH>`
`git commit -m "message"`
`git push -u origin <MAIN_BRANCH>`

**To initialize a local repository**
`git init`

**To verify what branch you are**
`git branch`

**To create a new branch**
`git branch <NEW_BRANCH_NAME>`

**To switch to another branch**
`git checkout <BRANCH_TO_GO>`

**To delete a branch**
`git branch -d <BRANCH_TO_DELETE>`

**To align a local main branch with the remote main branch on GitHub:**
`git pull origin main --allow-unrelated-histories`



# Using PyInstaller
**If you want to make an executable about your python code, do this**

Install **pyinstaller**
`pip install pyinstaller`

Create your executable in the script location of your code, and type the next command line _".pyw"_
### With this one, anyone can try to run your code without having installed python 
`pyinstaller --onefile -w <nombre_del_archivo.py>`

