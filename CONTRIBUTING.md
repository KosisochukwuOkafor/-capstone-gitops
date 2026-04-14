# Contributing Guide

this document is the team rulebook. read it fully before making any contributions.

## Full Development Workflow
1. pick up a trello card and move it to In Progress
2. pull the latest main: `git pull origin main`
3. create a feature branch: `git checkout -b feature/TRELLO-###-description`
4. make your changes and commit regularly with trello IDs
5. push your branch and open a PR on github
6. wait for CI to go green
7. get the PR merged
8. move the trello card to Done

## Branching Rules
- never push directly to main, ever
- always branch off the latest main
- branch naming format: `feature/TRELLO-###-short-description`
- use lowercase and hyphens only, no spaces or uppercase
- delete your branch after merging

## Commit Format
every single commit must follow this format:
[TRELLO-###] Short description of what this commit does
good examples:
[TRELLO-003] Add test_reverse_palindrome as 8th test case
[TRELLO-004] Add setup instructions to README
bad examples:
fixed stuff
update
WIP
commits without a trello ID will not count and break the project conventions.

## PR Process
- PR title must include the trello card ID eg. `[TRELLO-004] Add README documentation`
- write a short description explaining what the PR does and why
- CI must be green before merging, do not merge a red PR
- delete the branch after merging
- update your trello card to Done after merging

## CI/CD Explanation
the pipeline runs automatically on every push and PR. it has three stages in this order:
1. **Install dependencies** — runs `pip install -r requirements.txt`
2. **Lint with flake8** — checks code style against PEP 8, any violation fails the build
3. **Run tests with pytest** — runs all tests, any failure fails the build

if any stage fails the next one doesnt run. the PR is blocked from merging until
everything is green. this protects main from broken or badly formatted code.

## Coding Standards
this project follows PEP 8, which is the official python style guide.
flake8 enforces it automatically in the pipeline so you cant ignore it.
main things to watch out for:
- use 4 spaces for indentation, not tabs
- keep lines under 79 characters
- always add a newline at the end of every file
- put spaces around operators eg. `x = 1` not `x=1`

run the linter locally before pushing to catch issues early:
py -3.11 -m flake8 app.py test_app.py

## Failure Handling
if CI goes red dont panic. heres what to do:
1. go to the Actions tab on github and click the failed run
2. click the failed stage to see the error message and line number
3. fix the issue locally
4. run the linter and tests locally to confirm its fixed
5. commit the fix with a proper trello ID message
6. push again — CI will rerun automatically on the new push
never close and reopen a PR just because CI failed, just push the fix to the same branch.