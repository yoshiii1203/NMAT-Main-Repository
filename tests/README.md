# Data invariant tests

`test_data_invariants.py` is the first test suite in this repo. It checks
`dataset/NMAT_Exodus.parquet` (and its two dashboard-folder copies) against
the binding schema contract at `.claude/audit/_TARGET_SCHEMA_CONTRACT.md`.

## Run

```bash
.venv/Scripts/python.exe -m pytest tests/ -v
```

(`pytest` is in `requirements.txt`; `pip install -r requirements.txt` if it's
not already in your `.venv`.)

## What "red" means here

This suite was written against the **target** schema (post Pipeline
4/5 remediation), not necessarily today's shipped file. Until the full chain
(`1_*.ipynb` → `2_*.ipynb` → `4_Citizenship_Integration.py` →
`5_Slim_Exodus.py`) has been re-run end to end with every agent's fixes
landed, expect real failures — that is the suite doing its job, not a false
alarm. Re-run it after the chain completes; every test should be green.

If a test fails on data you believe is now correct (e.g. an upstream
matching-logic improvement legitimately changed a headline count like
`IS_PLE_PASSER.sum()`), don't delete the assertion — update the expected
constant at the top of the file and say why in the commit message. The
point of a hard-coded reference number failing loudly is that a human looks
at the new number before it ships to a policy dashboard.

## What's covered

- Row/column shape matches the contract (178,927 rows x 52 columns)
- The 4 contract-removed columns + `name_based_assessment` are absent; the
  4 renamed `UNDERGRAD_*` columns are present and the old names are gone
- `HasCEMMatch` / `HasTRUErawScores` / `StoredVsDerivedMismatch` are real
  `bool`-dtype, not the old `str` (`bool("False") is True` bug)
- `IS_BEST_NMAT_RECORD`: exactly one `True` per `PERSON_KEY`
- `IS_OBSERVABLE_COHORT` == `Year <= 2014`, and is not a tautological copy
  of `IS_PLE_PASSER` (the RC-1 bug this whole audit started from)
- `IS_BEST_OBSERVABLE_RECORD`: correct count, one per person within the
  observable window, and provably NOT equivalent to the naive
  `IS_BEST_NMAT_RECORD & Year<=2014` shortcut
- `PERSON_KEY_AMBIGUOUS`: correct count, constant within each key
- No two boolean-dtype columns are byte-identical (guards the RC-1 class of
  bug generally, not just the one instance that was found)
- Raw-score arithmetic identities (`sum(Raw_8) == TotalRawScoreTRUE`,
  `PartI + PartII == Total`)
- `B1` is the lowest percentile decile (mean raw score strictly increases
  `B1` → `B10`)
- `IS_PLE_PASSER` non-nested relationship with `PLE_YEAR_PASSED` metadata
- All three parquet copies (canonical + 2 dashboard folders) share one md5
- `EXODUS_MANIFEST.json`'s recorded md5/row/col counts match the file on disk

No fixtures/frameworks beyond plain `pytest` — one module-scoped fixture
loads the parquet once per run.
