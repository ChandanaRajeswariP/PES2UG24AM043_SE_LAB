# Lab 7 - Hypothesis Fuzzing for Password Policy Input

**Student:** Chandana Rajeswari P  
**SRN:** PES2UG24AM043

This submission follows the Lab 7 handout and adapts its three fuzz targets to the assigned `password_policy.py`: `first_character_type`, `split_credentials`, and `digit_ratio`.

## Findings and fixes

The starter functions could crash on empty or non-string values, malformed credential separators, and empty strings passed to `digit_ratio`. The fixed functions return `None` for invalid input and preserve the expected result for valid input. The interactive demo prints a validation message instead of stopping with an exception.

## Files

- `password_policy.py` - hardened application.
- `test_password_policy.py` - Hypothesis properties plus regression examples.
- `Lab7_Fuzzing_Report.pdf` - before/after terminal evidence.
- `screenshots/` and `reports/` - captured command output and text logs.

## Run

Install the dependencies with `python -m pip install pytest hypothesis`, then run:

```powershell
python password_policy.py
python -m pytest -q test_password_policy.py
```

Invalid values return `None`; valid strings retain the original classification, split, and digit-ratio behavior.

## Results

| Stage | Result |
|---|---|
| Original no-crash fuzz tests | 3 failed; Hypothesis found empty-string failures in all three functions and also exposed `None` crashes. |
| Fixed application demo | Valid examples produced the expected values; empty/malformed examples displayed validation messages. |
| Fixed Hypothesis suite | 21 passed, including six properties with 200 generated examples each. |

The PDF report includes the before/after terminal evidence. The same logs and screenshot images are also saved under `reports/` and `screenshots/`.
