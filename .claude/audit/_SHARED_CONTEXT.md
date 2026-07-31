# Shared Audit Context (verified empirically by orchestrator, 2026-07-31)

Repo root: `D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis`
Python: use `./.venv/Scripts/python.exe` (pandas, pyarrow, duckdb available).

## Parquet facts (VERIFIED — do not re-derive, build on these)

All THREE copies of `NMAT_Exodus.parquet` are **byte-identical** (md5 `8034a0e72e1ff4d4e3e0334e91c4bccf`, 11,007,467 bytes):
- `dataset/NMAT_Exodus.parquet`
- `streamlit_dashboard/main_dashboard/NMAT_Exodus.parquet`
- `streamlit_dashboard/CHED_relevant_dashboard/NMAT_Exodus.parquet`

Shape: **178,927 rows x 54 cols**. `PERSON_KEY` nuniq=134,869. `APPNO_CLEAN` nuniq=178,926 (ONE duplicate).

### Columns documented in CLAUDE.md/docs that DO NOT EXIST in the parquet
`PERSON_NAME`, `PLE_MATCH_STATUS`, `IS_BOARD_OBSERVABLE_COHORT`. Treat doc claims skeptically.

### CONFIRMED CRITICAL BUG #1 — `IS_PLE_ANALYSIS_SAFE` is not what docs claim
- Docs/CLAUDE.md say it means "observable cohort: Year <= 2014".
- Empirically: `(df.IS_PLE_ANALYSIS_SAFE == df.IS_PLE_PASSER).all() == True` — it is a **perfect duplicate of IS_PLE_PASSER**.
- `(IS_PLE_ANALYSIS_SAFE == (Year<=2014)).all() == False`. It is True for 4,288 rows in 2015, 3,673 in 2016, 1,136 in 2017, 19 in 2018.
- **Consequence:** any pass-rate denominator filtered on `IS_PLE_ANALYSIS_SAFE` yields 100% by construction. Hunt for this everywhere.

### CONFIRMED ANOMALY #2 — three mutually inconsistent "PLE matched" counts
- `IS_PLE_PASSER == True`: 49,986
- `PLE_YEAR_PASSED.notna()`: 54,528
- `PLE_MATCH_METHOD.notna()`: 57,304
- `PLE_YEAR_GAP.notna()`: 48,842
No two agree. Determine which is authoritative and which the dashboards use.

### PLE match methods
`EXACT` 54,437 | `MANUAL_APPNO_MATCH` 2,776 | `DETERMINISTIC_APPNO` 91 | null 121,623.

### Citizenship / foreigner (all rows)
`FOREIGNER_STATUS`: Filipino 146,413 | Verified Foreigner 32,501 | Likely Foreigner **13**.
`CITIZENSHIP_FINAL` nuniq=91. Top non-Filipino: India 26,491; Nepal 1,158; Thailand 1,062; USA 839; Nigeria 639.
Foreign share (best-record) by year rises 3.9% (2006) -> ~29% (2015-2017). India by year: 44 (2006) -> 6,373 (2017).
`name_based_assessment` is non-null for only **871** rows (Likely Filipino/Filipino-origin 559; Likely true foreigner 312).
`UNI_TYPE`: Private 137,476 | Public 37,304 | Foreign 2,315 | Not Specified 1,832.
Note: only 731 of 2,315 "Foreign" UNI_TYPE rows are Verified Foreigners — UNI_TYPE=Foreign means the *school* is foreign, not the person.

### Other
`Year` 2006-2018. Counts rise 4,376 (2006) -> 27,661 (2018).
`PercentileBin` B1-B10 + 4,141 nulls. `NMS_PER_num` null for 1,275 rows. `Percentile_CEM` null for 4,182.
`StoredRawTotal` non-null for only 99,316 of 178,927 (so "42.2% mismatch" claims apply only to that subset).
`AllRawComponentsPresent` and `CalcVsDerivedMismatch` are **constant (nuniq=1)** — dead columns.
Several boolean-ish columns are stored as **str** not bool: `HasCEMMatch`, `HasTRUErawScores`, `StoredVsDerivedMismatch`, `AllRawComponentsPresent`, `CalcVsDerivedMismatch`. Truthiness bugs are likely — `bool("False") == True`.

## Rules for your audit
1. **Do NOT fix or edit any project file.** Read-only audit. You may only write your own report.
2. **Evidence or it didn't happen.** Every finding needs `path:line` and, where it's a data claim, a runnable snippet + its actual output that you executed.
3. Distinguish CONFIRMED (you ran it) from SUSPECTED (code reading only). Label each finding.
4. Severity: CRITICAL (wrong numbers shown to stakeholder) / HIGH (misleading or unsupported claim) / MEDIUM (fragile, will break) / LOW (cosmetic, docs).
5. Scope discipline: the user only has this dataset. Flag any dashboard claim that the data cannot support.
6. Ignore `RShiny_Dashboard/`, `reports/`, `dashboard.py` at repo root (legacy), and `data_aggregator/page_results/00_MASTER_REPORT.md` (9 MB, do not read).
