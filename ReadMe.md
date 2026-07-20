
Hi! adding this absolutely unnecessary line to create conflict with Jyo

Hii! I hate Joanna

# DevOps Lab - Exercise 3

## Repository Overview

This repository is created as part of the **DevOps Laboratory - Exercise 3** to demonstrate Git and GitHub collaboration among team members. The exercise covers repository management, branching, merging, conflict resolution, cherry-picking, and reverting commits.

---

## Team Members

| Student | Role |
|----------|------|
| Student A | Repository Owner |
| Student B | Developer 1 |
| Student C | Developer 2 |

---

## Project Structure

```
DevOps-Lab-Exercise-3/
│
├── README.md
├── Src/
│   ├── login.py
│   ├── register.py
│   ├── calculator.py
│   └── report.py
│
├── Docs/
│
└── Tests/
```

---

## Exercise Tasks

### Task 1 – Repository Setup
**Student A**
- Create GitHub repository
- Add README.md
- Create project folders
- Push repository to GitHub

---

### Task 2 – Clone Repository & Create Modules

**Student B**
- Clone repository
- Create `Src/login.py`
- Add Login module
- Commit and Push

**Student C**
- Clone repository
- Create `Src/register.py`
- Add Registration module
- Commit and Push

---

### Task 3 – Merge Conflict

- Student B edits README.md and commits (without pushing).
- Student C edits the same line, commits, and pushes.
- Student B attempts to push and encounters a merge conflict.
- Resolve conflict using:

```bash
git pull origin master
```

---

### Task 4 – Delete vs Modify Conflict

- Student B deletes `register.py` and commits.
- Student C modifies `register.py` and commits.
- Student B pulls latest changes.
- Resolve the delete/modify merge conflict.

---

### Task 5 – Same Function Conflict

Original Function

```python
def calculate():
    print("Calculation")
```

Student B changes to

```python
def calculate():
    print("SI")
```

Student C changes to

```python
def calculate():
    print("CI")
```

Resolve the merge conflict and finalize the function.

---

### Task 6 – Cherry Pick

- Student B creates `calculator.py`
- Student C creates `report.py`
- Student A cherry-picks only the calculator commit into the master branch.

Example:

```bash
git cherry-pick <commit-id>
```

## Task 6 – Cherry Pick

### Objective
Student A should bring **only** `calculator.py` from Student B's branch into the `master` branch without merging the entire branch.

---

### Student B

Create a new branch.

```bash
git checkout -b calculator-feature
```

Create `Src/calculator.py`.

Stage and commit the file.

```bash
git add Src/calculator.py
git commit -m "Added calculator module"
```

Push the branch to GitHub.

```bash
git push origin calculator-feature
```

---

### Student C

Create a new branch.

```bash
git checkout -b report-feature
```

Create `Src/report.py`.

Stage and commit the file.

```bash
git add Src/report.py
git commit -m "Added report module"
```

Push the branch to GitHub.

```bash
git push origin report-feature
```

---

### Student A

Switch to the `master` branch.

```bash
git checkout master
```

Fetch the latest branches from GitHub.

```bash
git fetch origin
```

View the commit history of Student B's branch.

```bash
git log origin/calculator-feature --oneline
```

Copy the commit hash of **"Added calculator module"** and cherry-pick it into `master`.

```bash
git cherry-pick <commit-hash>
```

Push the updated `master` branch.

```bash
git push origin master
```

---

### Result

Only `calculator.py` is added to the `master` branch.

```
master
│
├── README.md
├── Src
│   ├── login.py
│   ├── register.py
│   └── calculator.py
```

`report.py` remains only in the `report-feature` branch.

---

### Task 7 – Revert

- Student C accidentally deletes `login.py`
- Commit the deletion
- Restore the file by reverting the commit without removing commit history.

Example:

```bash
git revert <commit-id>
```

---

## Git Commands Used

Clone Repository

```bash
git clone <repository-url>
```

Check Status

```bash
git status
```

Add Files

```bash
git add .
```

Commit Changes

```bash
git commit -m "Commit message"
```

Push Changes

```bash
git push origin master
```

Pull Changes

```bash
git pull origin master
```

Cherry Pick

```bash
git cherry-pick <commit-id>
```

Revert Commit

```bash
git revert <commit-id>
```

---

## Learning Outcomes

- GitHub repository management
- Repository cloning
- Commit and push workflow
- Merge conflict creation and resolution
- Delete/modify conflict handling
- Function-level conflict resolution
- Cherry-picking specific commits
- Reverting commits while preserving project history

---

## Conclusion
This exercise demonstrates collaborative software development using Git and GitHub, helping students understand version control, teamwork, conflict resolution, and advanced Git operations commonly used in DevOps workflows.

