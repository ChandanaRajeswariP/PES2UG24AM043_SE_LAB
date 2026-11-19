# Lab 5 Static Code Analysis - Vehicle Service Management System

**Student:** Chandana Rajeswari P  
**SRN:** PES2UG24AM043  
**Assigned file:** vehicle_service.py

This submission applies Pylint, Bandit, and Flake8 to the vehicle service script. It fixes the security, correctness, and style findings while preserving the demonstration's service totals and busiest-vehicle result.

## Deliverables

- vehicle_service.py: cleaned program.
- issues.md: original line references, findings, and fixes.
- reflection.md: four reflection responses.
- pylint_report.txt, bandit_report.txt, flake8_report.txt: final analysis reports.
- reports/before and reports/after: snapshots from each tool before and after fixes.

## Reproduce the analysis

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install pylint bandit flake8
python vehicle_service.py
python -m pylint vehicle_service.py
python -m bandit -r vehicle_service.py
python -m flake8 vehicle_service.py
```

Analysis was run with Python 3.12.14, Pylint 4.1.4, Bandit 1.9.4, and Flake8 7.5.0. The final results are Pylint 10.00/10, no Bandit findings, and no Flake8 findings.

The handout requires three commits for the three tool-driven fix groups. A local commit bundle is provided with the deliverables; it has not been pushed to GitHub.
