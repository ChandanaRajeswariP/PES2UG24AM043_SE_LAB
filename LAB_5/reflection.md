# Lab 5 Reflection

**Student:** Chandana Rajeswari P  
**SRN:** PES2UG24AM043  
**Project:** Vehicle Service Management System

## 1. Which issues were the easiest and hardest to fix?

The easiest fixes were the mechanical style issues: spacing, line length, function names, and docstrings. Pylint and Flake8 identified these directly. The more important fixes were the mutable default list and broad exception handler because they could produce shared state or hide unrelated failures. The hardest change was removing the shell command from the backup helper while keeping its purpose; shutil.copy2 preserves the copy operation without invoking a shell. I also replaced MD5 while retaining the existing short job-card display format.

## 2. Did the tools report any false positives?

The reviewed findings were actionable. Bandit's hard-coded-password finding referred to a constant that was not used, but leaving a password-like value in source would still be misleading, so I removed it. The MD5 value was only used as a short display identifier rather than an authentication token, so its security impact in this program was limited; SHA-256 removes the weak-hash warning without changing the identifier length. The shell warning was valid because a caller-supplied path was passed through a shell.

## 3. How would you integrate static analysis into your workflow?

I would run Flake8 and Pylint locally before committing and run all three tools in continuous integration. Bandit should block high-severity findings, Flake8 should enforce consistent formatting, and Pylint should maintain a score above 9.5. The reports should be saved with each build so regressions can be compared over time.

## 4. What tangible improvements did I see in the code?

Pylint improved from 4.66/10 to 10.00/10, Bandit went from four findings (two high and two low) to zero, and Flake8 went from four findings to zero. The demonstration still reports totals of 2300 and 2500, three vehicles on file, and KA01AB1234 as the busiest vehicle. The job-card value changed because MD5 was replaced with SHA-256; it remains an eight-character display identifier.
