# E2 — Documentation remediation log

Scope (owned, only these touched): `docs/data_dictionary.md`, `docs/pipeline_architecture.md`,
`README.md`, `CLAUDE.md`, `changelog.md`. No `.py`/`.ipynb` files touched, nothing under
`streamlit_dashboard/*/` or `data_aggregator/` touched. No git commands run.

All numbers below were independently verified against the live
`dataset/NMAT_Exodus.parquet` with `.venv/Scripts/python.exe`, not transcribed from
`_TARGET_SCHEMA_CONTRACT.md` or `_ORCHESTRATOR_FINDINGS.md` prose (those were read first for
context, then checked against the actual file).

---

## 1. Schema verification (grounds `docs/data_dictionary.md`)

```python
import pandas as pd
df = pd.read_parquet('dataset/NMAT_Exodus.parquet')
df.shape   # (178927, 53)  -- confirmed, not 54
```
Full column-by-column dtype/null/nunique dump taken for all 53 columns (index 0-52), in order.
Confirmed both `PLE_MATCH_OUTCOME` (index 51) and `PLE_YEAR_UNCERTAIN` (index 52) are present —
the contract described these as optional (52 or 53 width); the live file is the 53-column variant.

Categorical value counts pulled and documented for: `SEX`, `UNDERGRAD_UNI_LOCATION`,
`UNDERGRAD_UNI_TYPE`, `UNDERGRAD_COURSE_GROUP`, `PercentileBin`, `PLE_MATCH_METHOD`,
`PLE_MATCH_CONFIDENCE`, `FOREIGNER_STATUS`, `PLE_MATCH_OUTCOME`, `Year`, `CITIZENSHIP_FINAL` (top
15). Cross-tabs run for `PLE_MATCH_METHOD` x `PLE_MATCH_CONFIDENCE` and `PLE_MATCH_OUTCOME` x
`IS_PLE_PASSER` to confirm the described relationships (e.g. `accepted` == `IS_PLE_PASSER==True`
exactly, 49,086 both sides).

`CalculatedRawTotal_Source` confirmed identical to `TotalRawScoreTRUE` on every non-null row
(`(df['CalculatedRawTotal_Source'].dropna() == df.loc[...,'TotalRawScoreTRUE']).all()` → True) —
documented in the data dictionary as "CEM's own calculated total, always matches TotalRawScoreTRUE."

`APPNO_CLEAN` length distribution re-verified: 10-digit 152,540 (85.3%), 7-digit 23,985 (13.4%),
6-digit 2,402 (1.3%) — matches the shape described in the old (otherwise-superseded) doc, kept.

## 2. Headline numbers re-verified independently (all match RESUME.md / the target contract exactly)

```
rows                                    178,927
unique PERSON_KEY                       134,869
IS_BEST_NMAT_RECORD.sum()               134,869
IS_OBSERVABLE_COHORT.sum()               88,144
IS_BEST_OBSERVABLE_RECORD.sum()          69,503
IS_PLE_PASSER.sum()                      49,086   <- NOT 49,986 (see below)
PERSON_KEY_AMBIGUOUS distinct keys        6,148
PLE_YEAR_UNCERTAIN.sum()                    110
observable linkage rate                  45.44%
repeat takers (>1 distinct APPNO_CLEAN)  33,713
keys with >1 row                         33,714
stored-total mismatch                    56,065 / 99,316 = 56.45%
```
Per-bin observable linkage table reproduced exactly (B1 11.6% ... B10 71.0%), matching O-22.

Below-40th-percentile headline reproduced exactly:
```
below-40 observable people    25,596
of whom confirmed passers      6,173  (24.1%)
by bin: B1 795, B2 1,336, B3 1,703, B4 2,330
citizenship: 6,152 of 6,173 Filipino
```
Duplicate-row check confirmed the single duplicated record: `PERSON_KEY` "VENTANILLA, GLEN TAN||",
`APPNO_CLEAN` 1073584, `Year` 2007, appearing on two distinct rows — this is exactly why the
row-count repeat-taker tally (33,714) differs by one from the distinct-appno tally (33,713). Both
numbers are now stated together with that explanation in `docs/data_dictionary.md`.

**One number I deliberately did NOT use from the schema contract:** `_TARGET_SCHEMA_CONTRACT.md`
§8 lists "Confirmed PLE passers: 49,986" as the reference value. The live parquet's actual
`IS_PLE_PASSER.sum()` is **49,086**. I read `.claude/audit/logs/P1_pipelines_1_2.md` and
`RESUME.md` to understand why: P1's disambiguator fix (RC-0 + O-24, landed together) legitimately
moved the count from 49,986 to 49,086, and this was reviewed and accepted by the orchestrator
(commit `bfb9e5c`). `5_Slim_Exodus.py`'s own `check_soft` tier is explicitly designed to warn
rather than block on exactly this kind of legitimate upstream movement. I used **49,086**
throughout (the number that matches the live file) and flagged in every doc that 49,986 is the
pre-fix figure, not a typo — this is the single point where I trusted the data over the contract
text, per the task's own instruction ("If a number here disagrees with the data, trust the data").

## 3. Pipeline-chain facts re-verified against the code, not just prose

- Read `5_Slim_Exodus.py` in full: confirmed the two-tier (`check_hard`/`check_soft`) assertion
  design, the `EXPLICIT_DROP` / `EXPLICIT_DROP_TASK1` lists (6 total removals, including
  `HasCEMMatch`), `RENAME_MAP` (4 renames), `BOOL_COERCE` (2 dtype fixes), and the manifest
  contents. Used this, not the contract prose, as the source of truth for "what does Pipeline 5
  actually do."
- Read `.claude/audit/logs/P1_pipelines_1_2.md` in full for the exact `disambiguate()` before/after
  code (RC-0's Step 4 percentile floor, O-24's `BDATE_CLEAN` ordering bug) and the funnel numbers
  (13,895 groups → 1 rejected at year-gap → 10,316 resolved → 3,578 ambiguous) — reproduced
  verbatim in `docs/pipeline_architecture.md` §3 and §7 rather than re-deriving from scratch, since
  P1's log already contains the in-notebook execution evidence.
- Read `.claude/audit/logs/P2_pipelines_4_5_tests.md` for Pipeline 4/5 mechanics (the `.bak` output
  path fix, `name_based_assessment` drop, the two-tier assertion design's rationale) and confirmed
  `pytest tests/ -q` still reports **36 passed** on the current repo state (re-ran it myself,
  not just cited the log).
- Read `.claude/audit/logs/D3_data_aggregator.md` for two facts I would not otherwise have caught:
  (a) `data_aggregator` does **not** use DuckDB — `CLAUDE.md`'s prior "DuckDB used in
  data_aggregator" claim was fiction, confirmed by D3's own `grep -rn duckdb data_aggregator/*.py`
  returning nothing; corrected in the new `CLAUDE.md`. (b) the live dashboard folder names
  (`main_dashboard/`, `CHED_relevant_dashboard/`) and their both-live status.

## 4. Live vs. legacy deliverables — verified by directory listing, not assumption

```
streamlit_dashboard/main_dashboard/dashboard.py            exists
streamlit_dashboard/CHED_relevant_dashboard/dashboard.py   exists
data_aggregator/*.py (13 page scripts + run_all.py)        exist
tests/test_data_invariants.py                               exists, 36 passed
```
Marked `RShiny_Dashboard/`, `reports/`, and root `dashboard.py`/`dashboard.py.bak` as legacy in
all four docs, per the task brief — did not delete or modify any of them.

## 5. Mid-task correction from the orchestrator — addressed

The orchestrator sent two corrections while I was mid-rewrite (both independently re-verified,
not taken on faith):

1. **Forensic audit consolidation.** `ls forensic_audit/` confirmed only `forensic_audit.py`
   remains (plus its own output CSVs/`.md` files and a `_superseded/` folder) — the three commands
   `CLAUDE.md` used to document (`forensic_audit_v5_final.py`, `audit_per_bin_report.py`,
   `audit_name_check_deep.py`) no longer exist. Fixed the "Run the Forensic Audit" section of
   `CLAUDE.md` to the single current command and cross-referenced the change in the "Forensic
   Audit Suite" directory-structure block.
2. **Dataset cleanup.** `ls dataset/` and `ls dataset/output/` confirmed `NMAT_Exodus.csv`,
   `output/NMAT_FINAL.parquet`, and `UNIVS_ARCHIVED.csv` are all genuinely gone. Grepped all 5 owned
   files for references to these three filenames and fixed every hit:
   - `docs/pipeline_architecture.md`: Pipeline 1's Mermaid node and "Column counts over the chain"
     table changed from `NMAT_FINAL.parquet` to `NMAT_FINAL.csv` (the file that actually persists
     and that Pipeline 2 actually reads), with an explicit note that the parquet twin was removed.
     Pipeline 1's "Output" prose section updated the same way.
   - `docs/data_dictionary.md`: "Pipeline Outputs Referenced" table corrected the same way, plus an
     explicit note that `NMAT_Exodus.csv` no longer exists and should not be treated as a
     documentation target.
   - `README.md`: Pipeline 1's "Output" bullet corrected to `NMAT_FINAL.csv` with the same note.
   - `CLAUDE.md`: Pipeline 1's chain description and the "Datasets" directory-structure block both
     updated — added an explicit "Gone (do not reference as existing)" line listing all three
     removed files.
   - Confirmed `NMAT_Exodus.parquet.bak`'s description in all four docs already framed it as
     deliberately-kept ("the only full-column audit trail... do not delete"), matching the
     orchestrator's guidance; strengthened the wording slightly in `docs/data_dictionary.md` and
     `README.md`'s Output Structure block to say "the only one" explicitly.
   - Re-grepped all 5 files afterward for `NMAT_Exodus.csv`, `NMAT_FINAL.parquet`, and
     `output/NMAT_FINAL` — zero remaining false-positive hits (every surviving occurrence is an
     explicit "this no longer exists" note, verified with a final grep pass, output pasted below).

```
$ grep -rn "NMAT_Exodus.csv\|NMAT_FINAL.parquet\|output/NMAT_FINAL" docs/ README.md CLAUDE.md
docs/pipeline_architecture.md: 2 hits, both "...twin...was removed..." / "...had zero readers..."
docs/data_dictionary.md: 1 hit, "...used to exist...was removed..."
README.md: 1 hit, "...twin was removed..."
CLAUDE.md: 1 hit, "Gone (do not reference as existing): ... dataset/output/NMAT_FINAL.parquet ..."
```

## 6. Claims from the old docs found wrong, beyond the list already supplied in the task brief

- **Old `docs/data_dictionary.md` claimed `PercentileBin` was "created by `pd.cut()` in the
  dashboard at load time (or renamed from `PercentileDecile` in older pipeline versions)."** This
  is stale — `PercentileBin` is created once, upstream, in Pipeline 1 (confirmed by reading
  `1_Data_Cleaning_Pipeline.ipynb` cell 15 per P1's log), not recomputed per-dashboard-load.
  Corrected.
- **Old `docs/pipeline_architecture.md` Pipeline 4 diagram labeled the citizenship tiers "32,402"
  and "99"** for Tier 1a/1b; the live, current tier split (per P2's own dry-run against the
  regenerated `.bak`) is 32,345 / 156. Used the current split throughout, not the older figures —
  both were internally consistent with their own eras, but only the current one matches the
  shipped file.
- **Old `README.md`'s "Key Decisions" table implied a flat 4-pipeline separation was the final
  design** ("4-pipeline separation... Added Pipeline 4 as a final enrichment step"). This
  undersold the actual current state — there is now a 5th pipeline, and it exists specifically
  because the 4-pipeline design left the final column-selection step with no code at all
  (documented explicitly in the new pipeline_architecture.md §6, quoting `5_Slim_Exodus.py`'s own
  docstring on this point).
- **Old `CLAUDE.md`'s "Key Dataset Columns" listed `PERSON_NAME` and `PLE_MATCH_STATUS`** as
  columns in the shipped file. Neither exists in the live 53-column parquet (confirmed by the
  full column dump in §1) — this matches O-7 in the orchestrator's findings ("phantom columns in
  the documentation"), which I independently reconfirmed rather than trusting the finding at face
  value.

## 7. What I did not touch / could not fully verify

- Did not independently re-run Pipelines 1-5 end-to-end (out of scope — I own docs only, and the
  data layer is already marked DONE/verified in `RESUME.md`; I re-verified its *output*, not its
  *process*, by querying the live parquet directly).
- Did not verify `forensic_audit_report.md` / `name_cross_check_evidence.md` content (present in
  `forensic_audit/` but not named in the orchestrator's correction or the task brief) — only
  confirmed the 5 CSV outputs the orchestrator specified.
- The `changelog.md` footer ("Total commits: 36 / Latest: `7fa0f18`") is now stale (many more
  commits have landed since), but I did not update it — computing the correct current count/sha
  requires `git log`, and the task rules explicitly forbid any agent from running git. Left as
  historical record; flagging for the orchestrator, who owns commits, to update if desired.
- Did not touch `.py`/`.ipynb` files, `streamlit_dashboard/*/`, or `data_aggregator/` per the
  task's explicit restriction, even where I noticed a documentation-adjacent detail there (e.g.
  D3's own log already covers the DuckDB-in-`CLAUDE.md` correction I applied).
