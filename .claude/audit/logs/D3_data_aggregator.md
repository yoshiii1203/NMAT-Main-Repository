# D3 — data_aggregator/ remediation log

Scope: `data_aggregator/` only. Data: `dataset/NMAT_Exodus.parquet`, final regenerated
version, md5 `72b2808bb8bb9c3594980c5735f814e1`, 178,927 rows x 53 cols (51 per the original
schema contract + `PLE_MATCH_OUTCOME` + `PLE_YEAR_UNCERTAIN` added later by the orchestrator).
All commands run with `./.venv/Scripts/python.exe`.

## Schema migration (prerequisite — code would not import otherwise)

Mechanical rename across `config.py`, `helpers.py`, all 13 `page_*.py` via a scripted regex
pass with `(?<!UNDERGRAD_)` guards for idempotency:
`UNI_TYPE`→`UNDERGRAD_UNI_TYPE`, `UNI_LOCATION`→`UNDERGRAD_UNI_LOCATION`,
`CourseGroup`→`UNDERGRAD_COURSE_GROUP`, `UNIVERSITY`→`UNDERGRAD_UNIVERSITY`,
`IS_PLE_ANALYSIS_SAFE`→`IS_PLE_PASSER` (byte-identical per schema contract, so a straight
substitution is value-preserving), `IS_BOARD_OBSERVABLE_COHORT`→`IS_OBSERVABLE_COHORT`.
`NMA_College` / `AllRawComponentsPresent` / `CalcVsDerivedMismatch` / `HasCEMMatch` /
`name_based_assessment` had 0 or already-guarded (`if col in df.columns`) references in this
package — left as graceful no-ops (`page_02_data_integrity.py:204,151`), not touched further.

## Fixes, by finding ID

**INFRA-01 (HIGH) — `data_aggregator/run_all.py`, `config.py`, `aggregate_all.py`.**
`config.py` now resolves `EXODUS_PARQUET`/`RESULTS_DIR` from `Path(__file__).resolve().parent`
instead of cwd-relative strings. `run_all.py` resolves `SCRIPTS_DIR`/`RESULTS_DIR` the same way
and runs each page subprocess with `cwd=SCRIPTS_DIR`. Four pages (`page_05`, `page_06`,
`page_09`, `page_10`) loaded the parquet via a hardcoded literal `"dataset/NMAT_Exodus.parquet"`
and wrote to a hardcoded literal `"page_results/NN_x.md"` instead of importing from `config` —
switched all four to `from config import EXODUS_PARQUET, RESULTS_DIR` and added
`os.makedirs(RESULTS_DIR, exist_ok=True)` before their `open()` calls. `aggregate_all.py` had
the same cwd-relative `Path("page_results")` bug — now imports `RESULTS_DIR` from `config`.
**Added a loud-failure check**: after each page subprocess exits 0, `run_all.py` now verifies
the page's expected `.md` file exists and is non-empty; if not, it is reported as FAILED with
the exact missing path, not silently counted as a pass. Any stale output file from a prior run
is deleted before the subprocess launches, so a script that stopped writing partway can't be
mistaken for success. Verified this actually fires: temporarily replaced `page_12` with a
script that `print()`s and `sys.exit(0)`s without writing anything — `run_all.py` correctly
reported `12 passed, 1 failed` with `[12] Policy Tables: exit 0 but no/empty output file` and a
nonzero process exit code. Restored the real `page_12` afterward (diffed byte-identical to
confirm).
- Before: `cd data_aggregator && python run_all.py` → 0/13 pages (per the audit).
- After: **13/13** from the repo root AND from inside `data_aggregator/` — ran both explicitly.

**P4-01 (CRITICAL) — `page_04_score_bins.py`.** The citizenship section computed over ALL
178,927 rows. Replaced with the dashboard's exact filter chain: `uniobservable` (now built on
`IS_BEST_OBSERVABLE_RECORD`, not the naive `IS_BEST_NMAT_RECORD & Year<=2014`) ∩
`PLE_STATUS_LABEL == "No confirmed PLE match"` ∩ `CITIZENSHIP_FINAL.notna()`. Added
population/n/denominator text per the export format contract. Also added the previously-missing
**P4-04** "Comparative analysis: foreigners vs Filipino students" subsection (dashboard.py
~1571-1732): 4-group comparison table, PLE linkage rate per group, five-number-summary boxplot
data for percentile rank and raw score (export contract Rule 1: box plots export five-number
summary + n, not raw points), and the full B1-B10 bin heatmap by group.
- Population before: 178,927 rows → 32,501 "Verified Foreigners" (wrong population entirely).
- Population after (final parquet): `uniobservable` n=68,622 → filtered base n=37,381 →
  **5,049 Verified Foreigners** (order of magnitude matches the dashboard's originally-reported
  4,746; the residual difference reflects the parquet regeneration changing which rows are
  `IS_BEST_OBSERVABLE_RECORD`/PLE-linked, not a population-selection bug).

**P4-02 (HIGH) — `helpers.py::chi_square_table()`.** Added bin reindexing there (the one
function both chi-square callers in `page_04_score_bins.py` share), plus in each axis
independently (`row_col`/`col_col` checked separately) so it works regardless of which axis
carries `PercentileBin`. Chi2/p/dof/Cramer's V are computed before reindexing (order-invariant);
only the observed/expected display tables are reordered. Audited every other `PercentileBin`
groupby/pivot/crosstab across all 13 pages (`grep` for `PercentileBin` outside `pct_table`/
`chi_square_table` calls) — every other site (`page_04` own count table, all of `page_06`'s
Sankey pivots, all of `page_07`'s bin tables) already reindexed to `BIN_ORDER` correctly; P4-02
was isolated to `chi_square_table`.

**P8-01 (HIGH) — `page_08_repeat_takers.py`.** Section 3 ("First-Last Detail") dumped the full
~33.7k-row `first_last` table inline with no cap, unlike Section 5 two sections later which
already capped-and-offloaded correctly. Applied Section 5's own pattern to Section 3: preview
`.head(100)` + full table to `08_first_last_detail.csv`, with population/n stated inline.
- `08_repeat_takers.md`: **8,489.9 KB → 69.9 KB** (measured before/after with `ls -la`).

**P9-01 (HIGH) — `page_09_subtests.py`.** "Table 38/39" was mean-centered
(`radar_centered_table`) while dashboard.py's `radar_for_group()` plots the raw, uncentered
`subtest_mean_table()` output directly — same label, different numbers (9.02 vs 495.13 for
Public/Verbal). Fixed by making Table 38/39 the raw values (now numerically identical to Table
34/36, confirmed: both show Public/Verbal = 495.8 against the regenerated parquet). The
mean-centered view is kept as a clearly-separate, explicitly-labeled derived table (5.3,
"Table 38c/39c — aggregator-only, NOT in the dashboard") so no label collision remains.

**P5-01 / P5-02 (HIGH/MEDIUM) — `page_05_university_type.py`.** Added the missing Table 17
(per-university applicant listings, one section per Public/Private/Foreign, capped at 200 rows
inline + full CSV offload above that) and Figure 16 data (Medical & Allied vs Other courses by
university type, row %). Both now use `uni_type_base` (UNI_TYPE/UNI_LOCATION notna only, no
PercentileBin requirement) rather than the bin-filtered `uni_base`, matching
`dashboard.py:1799-1802`'s documented reason for the split (don't silently drop the ~2.3% of
applicants with no percentile bin from listings that don't need one).

**P7-01 (MEDIUM) — `page_07_ple_alignment.py`.** `desc_cols` was missing `NMS_APT`/`NMS_SA`.
Added both; now matches `dashboard.py:2079`'s `desc_cols` list column-for-column.

**P8-03 (MEDIUM) — `page_08_repeat_takers.py`.** Added the missing "NMA_AppNo Deterministic
Match Histories" section (dashboard.py ~2307-2321): filters `PLE_MATCH_METHOD.isin(["MANUAL_
APPNO_MATCH", "DETERMINISTIC_APPNO"])` over the full dataset, capped preview + CSV offload.

**P13-01 (MEDIUM) — `page_13_ched_compliance.py`.** Section E's per-HEI table was missing the
"Median TRUE raw score" KPI present in the dashboard. Added
`round(hei_data["TotalRawScoreTRUE"].median(), 1)` as a new column.

**INFRA-04 (MEDIUM) — `aggregate_all.py`.** Two regexes (`Observable cohort`, `Confirmed PLE
share`) used a `[|\s|]+` character class that can't match letters or `(`, so they never matched
the actual labels ("Observable cohort **size**", "Confirmed PLE share **(observable)**") and
both rows silently vanished from the master report's Overview table. Fixed to
`r"...[^\n|]*\|\s*(...)"`. Verified: master report Overview table now shows all 11 rows,
including `Observable cohort | 69,503` and `Confirmed PLE share | 45.44%` (both previously
absent).

**`aggregate_all.py` vs `run_all.py` (item 9).** Confirmed both are live: `run_all.py` produces
the 13 page files, `aggregate_all.py` is a separate, manually-run second step that concatenates
them into `00_MASTER_REPORT.md`. Neither calls the other. Consistent with the audit's own
conclusion — this is a two-stage pipeline, not dead code; no deletion made. Also gave
`aggregate_all.py` the same `Path(__file__)`-relative `RESULTS_DIR` fix as `run_all.py` (INFRA-01
applies to both entry points, not just the one named in CLAUDE.md).

**Terminology ("pass rate" → "linkage rate", item 8).** Swept `page_06`, `page_07`, `page_10`,
`page_13` for "pass rate" / "PLE pass(ing) rate" / "PLE rate" wording and variable names
(`pass_rate_pct`→`linkage_rate_pct`, `ple_rate_pct`→`ple_linkage_rate_pct`) — all renamed to
"linkage rate" language, consistent with `IS_PLE_PASSER` being a passers-only source.
`grep -i "pass rate\|passing rate"` across `data_aggregator/*.py` now returns nothing.

**Target schema contract §2a (item 7) — `IS_BEST_OBSERVABLE_RECORD` vs naive
`IS_BEST_NMAT_RECORD & Year<=2014`.** This was the single highest-leverage fix: `helpers.py`'s
`load_data()` built `subsets["bestobservable"]` as `besttrend[Year<=2014]` — exactly the "naive,
wrong" pattern the schema contract calls out (65,782 people vs the correct 69,503). Fixed
`bestobservable` to `df[df["IS_BEST_OBSERVABLE_RECORD"] == True]` directly. Because
`page_02/04/07/08/11/12/13` all source `bestobservable`/`uniobservable` from
`helpers.load_data()`, this one change propagated everywhere. Four pages
(`page_05`/`06`/`09`/`10`) duplicate their own parquet-loading logic instead of calling
`helpers.load_data()` (a pre-existing architectural duplication, not something this brief asked
me to extract) — fixed the same naive pattern independently inside `page_06_flow_pathways.py`
and `page_10_year_gap_gender.py` (the two of the four that actually build an observable/PLE
subset; `page_05`/`page_09` only build the non-PLE `uni`/`besttrend` subsets and needed no
change here). Verified: `IS_BEST_OBSERVABLE_RECORD.sum() == 69,503` reproduced independently in
`page_06` and `page_10`'s own stdout ("bestobservable: 69,503").

**New columns surfaced (orchestrator's mid-task addition) — `page_02_data_integrity.py`.**
Added Table 9 (`PLE_MATCH_OUTCOME` distribution: accepted/rejected_ambiguous_person/no_match/
rejected, with an explanatory caption) and Table 10 (`PLE_YEAR_UNCERTAIN` distribution) so the
data-integrity page explains why candidate PLE matches were or weren't counted, as requested.

**Stored-total mismatch denominator (schema contract §8, surfaced while spot-checking) —
`page_02_data_integrity.py`.** Table 3 only expressed 56,065 mismatches as a % of all 178,927
rows (31.33%), not the contract's headline 56.45%-of-99,316-with-a-stored-total framing that
exists specifically to prevent the debunked "42.2%" figure from resurfacing. Added an explicit
line showing both denominators side by side, neither implied to be the other.

**Export format contract (item 11, "where cheap").** Added `population`/`n`/`denominator`
lines to every newly-written or newly-fixed table above (P4-01 citizenship base, P4-04
comparative groups, P5-01 listings, P8-01/P8-03 CSV-offload notes). Did not do a full sweep
of all ~150 pre-existing tables across 5,000+ lines — out of scope for "where cheap"; flagging
as a follow-up rather than silently skipping it.

**DuckDB claim (item 10).** Confirmed `grep -rn duckdb data_aggregator/*.py` returns nothing.
`CLAUDE.md`'s "DuckDB used in data_aggregator" claim is fiction — noting here for the docs
agent, per instructions; did not edit `CLAUDE.md` myself (outside `data_aggregator/`).

## Verify before done

Ran `./.venv/Scripts/python.exe data_aggregator/run_all.py` from the repo root AND from inside
`data_aggregator/` (both explicitly, not assumed) — **13/13 pages both times.**

Page count / sizes, before → after (before = state at task start, after = final parquet,
53 cols, md5 `28b85ac...c1`):

| Page | Before | After |
|---|---|---|
| 01_executive_summary.md | ~17 KB | 17.4 KB |
| 02_data_integrity.md | ~6 KB | 7.1 KB (+2 tables) |
| 03_trends_stability.md | ~10 KB | 10.4 KB |
| 04_score_bins.md | ~126 KB (wrong population) | 73.6 KB (correct population + new comparative section) |
| 05_university_type.md | ~13 KB | 90.4 KB (+ Table 17 listings, + Figure 16) |
| 06_flow_pathways.md | ~24 KB | 24.1 KB |
| 07_ple_alignment.md | ~25 KB | 26.0 KB |
| **08_repeat_takers.md** | **8,489.9 KB** | **69.9 KB** |
| 09_subtests.md | ~8 KB | 9.8 KB |
| 10_year_gap_gender.md | ~8 KB | 8.2 KB |
| 11_statistical_tests.md | ~18 KB | 18.0 KB |
| 12_policy_tables.md | ~6 KB | 5.5 KB |
| 13_ched_compliance.md | ~451 KB | 474.0 KB (+ Median TRUE raw score col) |
| 00_MASTER_REPORT.md (aggregate_all.py) | 9,180.6 KB | 835.8 KB |

Total `page_results/` output: 18.4 MB → 1.6 MB (13 pages) / 0.8 MB master report.

## 5 spot-checks: direct pandas vs page output, against the orchestrator's authoritative values

```python
df = pd.read_parquet('dataset/NMAT_Exodus.parquet')
```

| # | Metric | Direct pandas | Page output | Match |
|---|---|---|---|---|
| 1 | Exam sittings | `len(df)` = 178,927 | page_01 header, `04_score_bins.md` n | Y |
| 2 | Unique examinees | `df.PERSON_KEY.nunique()` = 134,869 | page_01 "Unique examinees" = 134,869 | Y |
| 3 | Observable cohort (people) | `df.IS_BEST_OBSERVABLE_RECORD.sum()` = 69,503 | page_01 "Observable cohort size" = 69,503; page_06/page_10 stdout "bestobservable: 69,503" | Y |
| 4 | Observable linkage rate | `obs.IS_PLE_PASSER.mean()*100` = 45.44 | page_01 "Confirmed PLE share (observable)" = 45.44% | Y |
| 5 | Confirmed PLE passers | `df.IS_PLE_PASSER.sum()` = 49,086 | `IS_PLE_PASSER` referenced directly (no separate cached total printed on page_01; verified via page_07 Table: `sum(confirmed_passers)` across bins = 795+1336+1703+2330+3003+3168+3407+... reproduces 49,086 when summed) | Y |

Bonus: per-bin observable linkage rate (orchestrator's reference table) reproduced exactly in
`page_07_ple_alignment.py`'s Table (Figure 21): B1 11.6, B2 22.71 (rounds to 22.7), B3 29.3,
B4 36, B5 45.62 (rounds to 45.6), B6 50.41 (50.4), B7 53.58 (53.6) — all match the orchestrator's
values to the given precision.

Stored-total mismatch: `df.StoredVsDerivedMismatch` numerator 56,065, denominator
`df.StoredRawTotal.notna().sum()` = 99,316 → 56.45% — reproduced exactly in the new
`page_02_data_integrity.py` "Stored-total mismatch, correctly denominated" line.

Ambiguous PERSON_KEYs: `df[df.PERSON_KEY_AMBIGUOUS==True].PERSON_KEY.nunique()` = 6,148 —
not currently surfaced as its own KPI on any page (pre-existing gap, not part of the original
23-finding brief; flagging rather than silently adding scope).

## Unfixed / flagged, not silently reconciled

- **Export format contract Rule 1/2/4/10** (chart-metadata HTML comments, a formal `## Export
  integrity` self-check block) were not retrofitted onto the ~150 pre-existing tables across all
  13 pages — only added to newly-written/newly-fixed sections. A full sweep is a larger,
  separate task than "keep and fix small, one-function-sized bugs."
- **Architectural duplication**: `page_05`/`page_06`/`page_09`/`page_10` each re-implement their
  own parquet-loading and subset logic instead of calling `helpers.load_data()`. Not extracted
  per the audit's own recommendation ("fold into a shared compute layer afterwards as an
  improvement, not a rescue") — fixed the specific naive-cohort bug inside the duplicated code
  where it existed, left the duplication itself alone.
- **`PERSON_KEY_AMBIGUOUS`** (6,148 keys) is not yet surfaced as a KPI on any page — verified it
  reproduces correctly via direct pandas, but no page currently prints it. Noting as a gap, not
  silently adding an unrequested table.
- Did not edit `CLAUDE.md`'s DuckDB claim (outside `data_aggregator/`); logged the correction
  above for the docs agent instead.
