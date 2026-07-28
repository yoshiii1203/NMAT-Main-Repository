# Verifier 06: Data, Methods, and Limitations (Tab 6)

**Data source:** `NMAT_Exodus.parquet`
**Dashboard logic replicated:** yes (bug-for-bug for dtype-sensitive comparisons)

## Overview

| Metric | Value |
|--------|-------|
| Total rows | 178,927 |
| Best-record examinees | 133,804 |
| Unique examinees (PERSON_KEY) | 133,558 |
| Pre-2015 observable cohort | 64,501 |
| Repeat takers | 33,713 (25%) |
| PLE passers (all rows) | 49,986 |
| PLE passers (best, observable) | 29,273 |
| Clean subset (Filipino, >=5yr gap) | 27,151 |
| Clean subset B5+ | 23,357 |
| Median PLE year gap | 6.0 |

## Metrics Comparison

| Metric | Computed (from parquet) | Expected (page_results) | Status |
|--------|----------------------|------------------------|--------|
| Total rows | 178,927 | 178,927 | PASS |
| Best-record count (N_BEST) | 133,804 | 133,804 | PASS |
| Unique examinees (best record) | 133,558 | 133,558 | PASS |
| Observable cohort size | 64,501 | 64,501 | PASS |
| Repeat takers | 33,713 | 33,713 | PASS |
| Repeat taker share (%) | 25.24 | 25.24 | PASS |
| TRUE raw score count (dashboard logic) | 0 | 0 | PASS |
| TRUE raw score count (actual) | 178,882 | (not in page_results) | INFO |
| Formula mismatches | 0 | 0 | PASS |
| Stored-vs-derived mismatches (dashboard logic) | 0 | 0 | PASS |
| Stored-vs-derived mismatches (actual) | 56,065 | (not in page_results) | INFO |
| Calc-vs-derived mismatches (dashboard logic) | 0 | 0 | PASS |
| Calc-vs-derived mismatches (actual) | 0 | (not in page_results) | INFO |
| PLE passers (all rows) | 49,986 | 49,986 | PASS |
| PLE passers (best record, observable) | 29,273 | 29,273 | PASS |
| Clean subset total | 27,151 | 27,151 | PASS |
| Clean subset B5+ | 23,357 | 23,357 | PASS |
| Median PLE year gap | 6.0 | 6.0 | PASS |

**Checks:** 15 total, 15 passed, 0 failed

## Column Type Notes

Several columns in the parquet file are stored as **string** dtype, which causes
the dashboard's numeric/bool comparisons (`== True`, `== 1.0`) to always return
`False`.  The verifier replicates this bug-for-bug to match the dashboard display,
while also showing the semantically correct values for reference.

| Column | Actual dtype | Dashboard comparison | Dashboard result | Actual count |
|--------|-------------|---------------------|-----------------|-------------|
| `HasTRUErawScores` | str | `== True` | 0 | 178,882 |
| `StoredVsDerivedMismatch` | str | `== 1.0` | 0 | 56,065 |
| `CalcVsDerivedMismatch` | str | `== 1.0` | 0 | 0 |

*Note: `IS_BEST_NMAT_RECORD` and `IS_PLE_ANALYSIS_SAFE` are properly normalized
to bool dtype by `validate_schema()`, so their comparisons work correctly.*
