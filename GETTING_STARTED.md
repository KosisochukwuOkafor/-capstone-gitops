# Getting Started

this guide is for new developers joining the project. follow these steps
and you should be up and running in under an hour.

## Prerequisites
make sure you have these installed before anything else:
- Python 3.11 — https://www.python.org/downloads/release/python-3119/
- Git — https://git-scm.com/downloads
- VSCode — https://code.visualstudio.com

## Environment Setup
1. Clone the repo:
   `git clone https://github.com/YOUR-USERNAME/capstone-gitops.git`
2. Go into the folder:
   `cd capstone-gitops`
3. Install dependencies:
   `py -3.11 -m pip install -r requirements.txt`

## Running the Tests
py -3.11 -m pytest test_app.py -v
you should see 8 passed at the bottom. if not check the troubleshooting section below.

## Running the Linter
py -3.11 -m flake8 app.py test_app.py
if theres no output that means no errors, flake8 is silent when everything is clean.

## Branch Workflow
never push directly to main. always create a feature branch first:
git checkout main
git pull origin main
git checkout -b feature/TRELLO-###-short-description
branch names must be lowercase with hyphens, no spaces. always include the trello card ID.

## Making Commits
every commit message must start with the trello card ID:
git add .
git commit -m "[TRELLO-###] describe what you did"
commits without a trello ID dont count toward the project requirements.

## Opening a PR
1. Push your branch:
   `git push origin feature/TRELLO-###-short-description`
2. Go to GitHub — you'll see a yellow banner, click "Compare and pull request"
3. Title must include the trello ID eg. `[TRELLO-003] Add 8th test case`
4. Add a short description of what the PR does
5. Click "Create pull request" and wait for CI to go green
6. Once its green click "Merge pull request" then "Confirm merge" then "Delete branch"

## Troubleshooting

**Python not found in terminal**
if you get "python is not recognized" try using `py -3.11` instead of `python`.
if that also fails, reinstall python 3.11 and make sure to check "Add Python to PATH" during install.

**git push asks for a password**
github no longer accepts your account password for command line operations.
go to GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic) → Generate new token.
give it "repo" scope and use the token as your password when prompted.

**CI fails on lint**
run `py -3.11 -m flake8 app.py test_app.py` locally first.
fix any errors it reports, then commit and push again.
common issues are lines that are too long, missing spaces around operators, or no newline at end of file.