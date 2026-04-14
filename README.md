# Capstone GitOps Project

## Project Overview
This project is about setting up a GitOps workflow using a Python Flask web API,
GitHub Actions for CI/CD automation, and Trello for task tracking.
basically we wrapped a simple Flask app with a full DevOps pipeline that does
linting, automated testing, and branch-based collaboration.

## Architecture
The Flask app has three endpoints:
- `/health` (GET) — returns `{"status": "UP"}` to confirm the app is running.
- `/sum` (POST) — takes `{"a": x, "b": y}` and returns the sum of both numbers.
- `/reverse-string` (POST) — takes `{"text": "..."}` and returns it reversed.

## Workflow Description
1. Pick a Trello card and move it to In Progress.
2. Create a feature branch: `feature/TRELLO-###-description`
3. Make commits that reference the card ID.
4. Push and open a Pull Request targeting main.
5. CI runs automatically: install dependencies, lint, then test.
6. Once all checks pass you can merge the PR.
7. Move the Trello card to Done.

## Commit Conventions
Every commit has to start with the Trello card ID in square brackets like this:
[TRELLO-001] Initial project setup
[TRELLO-003] Add 8th test case
[TRELLO-004] Add README documentation
this way every code change is linked to an actual task on the board.

## Setup Instructions
1. Clone the repository:
   `git clone https://github.com/YOUR-USERNAME/capstone-gitops.git`
2. Enter the folder:
   `cd capstone-gitops`
3. Install dependencies:
   `py -3.11 -m pip install -r requirements.txt`
4. Run the tests:
   `py -3.11 -m pytest test_app.py -v`
5. Run the linter:
   `py -3.11 -m flake8 app.py test_app.py`

## Reflection Answers

### Question 1: What is GitOps and why does it matter for engineering teams?
GitOps is basically a way of working where Git is the single source of truth for everything, like the code, configs, all of it. every change has to go through the repository, so theres always a full history of what changed and who did it. nothing just gets pushed randomly.

it matters alot for engineering teams because without structure things get messy fast. like developers can overwrite each others work or push untested code and then suddenly somethings broken in production and nobody knows why. GitOps fixes that by making the repo the only way changes get in. you cant just push to main directly, everything goes through a pull request which triggers the automated checks first.

for teams this is really useful because new people can join and just read the git history to understand what happened and why. debugging is easier too because every deployment is tied to a specific commit so you can trace back exactly what changed. and when you release something you already know the tests passed and the linting is clean because the pipeline already ran. in this project you could see GitOps in every phase, trello tracked the tasks, feature branches kept changes isolated, PRs gave a review point, and github actions ran the checks before anything got merged. it all connects together in a way that makes the whole process more reliable and less stressful honestly.

### Question 2: How does a CI/CD pipeline improve code quality and team productivity?
a CI/CD pipeline is basically an automated system that runs checks everytime someone pushes code. CI is continuous integration which means you merge changes frequently and verify each one automatically. CD is continuous delivery which means every verified change is ready to be shipped.

in this project the pipeline runs three stages in order, first it installs dependencies, then it lints with flake8, then runs the tests with pytest. if any stage fails it stops right there and the PR cant be merged. so broken or badly formatted code literally cannot get into main.

the effect on code quality is big. without automation you might forget to run tests before pushing, or miss a style error that makes the code harder to read. the pipeline catches all that instantly and tells you exactly what went wrong and on which line. so instead of finding a bug days later in production you see the failure within minutes of pushing.

for productivity it also helps alot. when everyone on the team knows that main is always in a working state they can build on each other's work without worrying. you dont have to manually check every teammates code because the pipeline already did it. code reviews can focus on the actual logic instead of style stuff because flake8 already handled that. overall the team moves faster because the boring repetitive checking is automated.

### Question 3: What challenges did you face implementing this workflow, and how did you resolve them?
there were a few challenges during this project that took some time to figure out.

the first one was a python version problem. i was running python 3.14 which turned out to be too new for flask and werkzeug. the tests wouldnt even collect and it threw an AttributeError in the ast module. i had to install python 3.11 instead because thats what the ci.yml file specifies, and then use py -3.11 for all local commands so that the local environment matched what github actions was using.

the second issue was with pytest and flake8 not being recognized in powershell on windows. after installing everything the terminal just said command not found when i typed pytest. the fix was to use python -m pytest and python -m flake8 instead which runs them as python modules and doesnt rely on PATH at all. that worked fine.

the third thing was a small flake8 error, a missing newline at the end of test_app.py (W292). it seems like a tiny thing but flake8 is strict about it and it wouldve failed the whole pipeline. just had to add a blank line at the end of the file and it was fixed. it was a good reminder to always run the linter locally before pushing instead of waiting for CI to catch everything.

### Question 4: How would this workflow scale if the team grew from 3 to 20 developers?
scaling from 3 to 20 developers makes things more complicated but the core workflow stays the same, it actually becomes more important at that size.

with 20 people all working at the same time theres way more branches and PRs happening in parallel. to manage that you would need proper branch protection rules on github that require at least one or two people to review a PR before it can merge, not just a green CI check. you cant have people merging their own code without anyone looking at it when theres 20 developers touching the same codebase.

the pipeline would also need to be faster. with a small team a 2 minute pipeline is fine but with 20 people pushing multiple times a day a slow pipeline becomes a bottleneck where everyone is just waiting. you could fix this by running test stages in parallel, caching dependencies between runs, or only running tests related to the files that actually changed.

trello would probably need to be replaced with something more powerful like Jira or Linear which have better filtering and github integration. commit and branch naming conventions also become way more critical at scale because with 20 people inconsistent naming makes it really hard to trace what branch belongs to what task. you could enforce this automatically using git hooks or github policies so people cant push without following the format.

### Question 5: What additional tools or practices would you add if this were a real production service?
if this was a real production service there would be quite a few things to add on top of what we have.

first thing would be an actual CD stage in the pipeline. right now the pipeline just tests the code, it doesnt deploy it anywhere. in a real service a passing build on main should automatically deploy to a staging environment and then after some approval step deploy to production. you would probably use Docker to package the flask app into a container and something like Kubernetes to manage the deployments.

second would be secrets management. this project has no sensitive data but a real service would have API keys, database passwords, stuff like that. those cant be hardcoded anywhere. you would use something like AWS Secrets Manager or HashiCorp Vault to store them and inject them at runtime.

third would be monitoring and alerting. once the app is live you need to know immediately if something breaks or goes down. tools like Prometheus for collecting metrics and Grafana for dashboards would give visibility into whats happening. the /health endpoint already in the flask app is actually a good starting point for a health check monitor.

and lastly id add pre-commit hooks which are checks that run on your local machine before a commit is even created. this catches lint errors before they ever reach github which makes the feedback loop even faster and reduces pipeline failures from simple silly mistakes.