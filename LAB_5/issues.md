# Lab 5 Static Analysis Findings and Fixes

**Student:** Chandana Rajeswari P  
**SRN:** PES2UG24AM043  
**Project:** Vehicle Service Management System  
**Baseline:** vehicle_service.py from the assigned repository; line numbers below refer to the original file.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Weak MD5 job-card hash (B324) | Security - High | 39 | MD5 is a weak hash and should not be used for security-sensitive hashing. | Replaced MD5 with SHA-256 while keeping the displayed eight-character identifier format. The identifier is not used for authentication. |
| Shell-enabled backup command (B602, B404) | Security - High / Low | 3, 61 | A folder value is concatenated into a shell command with shell=True, allowing shell interpretation and command injection. Importing subprocess is also flagged. | Removed subprocess and copied the backup with shutil.copy2, which does not invoke a shell. |
| Hard-coded admin password (B105) | Security - Low | 8 | The source contains a fixed password string, even though the program does not use it. | Removed the unused password constant instead of keeping a secret in source code. |
| Mutable default argument (W0102) | Bug / Pylint | 12 | The default history list is shared between calls, so separate service operations can share state unintentionally. | Changed the default to None and create a new list inside add_service when no history is supplied. |
| Overly broad exception (W0718, E722) | Error handling / Pylint and Flake8 | 23 | A bare except catches errors unrelated to a missing vehicle record and can hide defects. | Catch only KeyError, which is raised when the vehicle is not in the service record map. |
| Missing file encoding (W1514) | Portability / Pylint | 50 | saveRecords opens a text file without an explicit encoding. | Open the JSON file with encoding="utf-8". |
| Non-snake-case names and missing docstrings (C0103, C0114, C0116) | Maintainability / Pylint | 1, 12-64 | Several functions and variables use camelCase, and the module/functions lack documentation. | Renamed functions and variables to snake_case and added a module docstring and function docstrings. |
| Whitespace after comma (E231) | Style / Flake8 | 7 | The service-rate dictionary is missing whitespace after a comma. | Put dictionary entries on separate, consistently formatted lines. |
| Whitespace around assignment (E225) | Style / Flake8 | 43 | The busiest-vehicle initialization is missing spaces around the assignment operator. | Used a formatted expression to select the vehicle with the most jobs. |
| Function spacing and line length (E302, E501) | Style / Flake8 | 49, 77 | A function definition has insufficient blank-line separation and one line exceeds 79 characters. | Applied PEP 8 spacing and wrapped the output statement. |
| Import-time demo execution (manual review) | Maintainability | 80 | Calling main at module scope makes importing the module run the demonstration and write services.json. | Added the standard __main__ guard so the demo runs only when the file is executed directly. |

## Tool results

| Tool | Before | After |
|---|---:|---:|
| Pylint | 4.66 / 10 | 10.00 / 10 |
| Bandit | 4 findings (2 High, 2 Low) | 0 findings |
| Flake8 | 4 findings | 0 findings |

The before/after reports are included under reports/before and reports/after. The root-level report files contain the final after results.
