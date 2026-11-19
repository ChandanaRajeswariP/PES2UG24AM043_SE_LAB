# Lab 6 - Password Policy Checker

**Student:** Chandana Rajeswari P  
**SRN:** PES2UG24AM043

This folder contains separate pytest suites for statement (code) coverage and branch coverage of the assigned `password_policy.py` module.

## Files

- `password_policy.py` - assigned application module.
- `CodeCoverageTest_password_policy.py` - executes each application statement.
- `BranchCoverageTest_password_policy.py` - exercises both outcomes of each decision.
- `screenshots/` - terminal-output captures for the two final coverage runs.
- `reports/` - text reports from the final runs.

## Run the coverage suites

Install the tools with `python -m pip install pytest coverage`, then run these commands from this folder:

```powershell
python -m coverage erase
python -m coverage run --source=password_policy -m pytest -q CodeCoverageTest_password_policy.py
python -m coverage report -m

python -m coverage erase
python -m coverage run --branch --source=password_policy -m pytest -q BranchCoverageTest_password_policy.py
python -m coverage report -m
```

Both suites are designed for at least 90% coverage. The line suite aims to execute every statement. The branch suite also tests both sides of each length, common-password, character-class, strength, and suggestion decision.

## Results

| Suite | Tests passed | Statement coverage | Branch coverage |
|---|---:|---:|---:|
| Code coverage | 6 | 100% (47/47 statements) | Not measured in this run |
| Branch coverage | 5 | 100% (47/47 statements) | 100% (36/36 branches) |

The report files and screenshots are captured from these successful runs.
