# Handoff Testing Guide

For a person sitting down at this repo for the first time who has to confirm it works. Every number
in this guide was read directly off the running apps and the shipped parquet on **2026-08-14** — the
exact commands are given so you can reproduce each one yourself. If a command below produces a
different number than what's printed here, trust what you get and treat this guide as stale for that
line — do not assume you did something wrong.

Authoritative reference numbers (source: `RESUME.md`, cross-checked against
`dataset/NMAT_Exodus.parquet` and both dashboards' own `AppTest` metric output while writing this
guide):

```
sittings 178,927 | unique examinees 134,869 | observable cohort (people) 69,503
observable linkage 45.44% | confirmed PLE passers (IS_PLE_PASSER) 49,086
ambiguous PERSON_KEYs 6,148 | PLE_YEAR_UNCERTAIN 110
stored-total mismatch 56,065 / 99,316 = 56.45%  ("42.2%" = same mismatch over the whole
                       CEM file, 107,422/254,308 -- a different population, also correct)
repeat takers 33,713 (25.0%) -- NOT 33,714; see the Known Issues note below
linkage by bin: B1 11.6  B2 22.7  B3 29.3  B4 36.0  B5 45.6
                B6 50.4  B7 53.6  B8 55.0  B9 61.6  B10 71.0
parquet md5 28b85ac53af13b4a2ef3ee93527c97c1 (all 3 copies + EXODUS_MANIFEST.json)
```

**Repeat-taker count note:** `RESUME.md` says 33,714; the currently-running code in both dashboards
says 33,713. Both dashboards define a repeat taker as a `PERSON_KEY` with more than one distinct
`APPNO_CLEAN` (application-based). The row-count form is one higher because one application number
carries two rows with different score sets in the source data (VENTANILLA, GLEN TAN, application
1073584, 2007, percentiles 98 and 80 on the same test date) and gets counted as two applications
only if you count rows, not distinct application numbers. The
application-based definition (33,713) is what both dashboards display and is the one to check
against — treat 33,714 as superseded.

---

## 1. Environment setup

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1          # Windows PowerShell
# or: source .venv/bin/activate       # macOS/Linux

pip install -r requirements.txt
```

**Gap to know about:** root `requirements.txt` does not list `duckdb`, but
`streamlit_dashboard/main_dashboard/dashboard.py` does `import duckdb` unconditionally (used by Tab 4's
"Bin composition per year" facet query). If you set up a fresh venv from the root requirements file
only, install it separately:

```bash
pip install duckdb
```

(`streamlit_dashboard/main_dashboard/requirements.txt` already includes it if you'd rather install
from that file for main-dashboard-only work.)

All commands below assume `.venv/Scripts/python.exe` (Windows) is your interpreter; substitute
`.venv/bin/python` on macOS/Linux.

---

## 2. Launch commands

Each dashboard is launched **from its own directory** — this is the documented and tested path.

```bash
# Main dashboard (13 tabs)
cd streamlit_dashboard/main_dashboard
streamlit run dashboard.py

# CHED dashboard (6 tabs)
cd streamlit_dashboard/CHED_relevant_dashboard
streamlit run dashboard.py

# Static markdown reports (13 pages), runnable from ANY cwd since the D3/INFRA-01 fix
python data_aggregator/run_all.py
# or: cd data_aggregator && python run_all.py   -- both work identically now

# Test suite, from repo root
.venv/Scripts/python.exe -m pytest tests/ -v
```

Both dashboard folders ship their own `NMAT_Exodus.parquet` copy plus a `requirements.txt`; you do
not need to run pipelines to view them, only to change the underlying data (§7 of `CLAUDE.md`).

---

## 3. Per-tab acceptance checklist — Main Dashboard (13 tabs, 42 tabs+subtabs)

All values below are what the dashboard shows **under default sidebar filters** (all Years, all
University types, all Course groups, all Sex values selected, "Filter PLE pages by status" unchecked)
— verified live via `AppTest` on 2026-08-14. If your screen disagrees under the same default filters,
something regressed.

| # | Tab | Sub-tab | What should appear | Numbers to read off screen |
|---|---|---|---|---|
| 1 | Executive Summary | Overview | Figure 1: 2×2 subplot (median raw score, Part I vs II, median percentile, volume bar) by year | Top metrics: **Examinees (best-record) 134,869**; Years covered 13; Median TRUE raw score **122.0**; Median percentile rank **50.0**; Repeat takers **33,713 (25.0%)**; Observable cohort **69,503**; PLE linkage rate, observable cohort **45.44%** |
| 1 | Executive Summary | Composition | Two pie charts: course-group and university-type composition | Pie slice counts must sum to 134,869 |
| 1 | Executive Summary | Quick Tables | Table 1: 6-row summary (median scores, top/bottom-bin share) | Top-bin share (B8–B10) and bottom-bin share (B1–B3) — cross-check against Tab 4's heatmap |
| 2 | Data Integrity | — | Cohort-definition tables, raw-score validation, uni-type/course-group counts, PLE match-outcome breakdown | Metrics: **All NMAT rows 178,927**; Best-record rows **134,869**; Rows with TRUE raw scores **178,882**; Observable best-record rows **69,503**; Stored-vs-derived mismatch rate **56.45%**; Universities checked **2,907**; University pairing conflicts **0**. Caption states 56,065/99,316 mismatch explicitly; "42.2%" is the same mismatch over the whole CEM file (107,422/254,308), a different denominator rather than an error |
| 3 | Trends & Stability | — | Figure 4 (same 2×2 subplot restricted to besttrend); 4 boxplots by year; Kruskal-Wallis table | No `st.metric`s. Caption states best-record volume is 60–92.6% of true sittings across years (non-uniform). Kruskal-Wallis table has 5 rows (Score, H, p_value, eta_squared) |
| 4 | Score Bins & Background | By year | Heatmap (bins × years), stacked composition bar, top/bottom trend line | Heatmap rows must read B10 (top) → B1 (bottom); values should NOT look string-sorted (B1, B10, B2…) |
| 4 | Score Bins & Background | University type | Heatmap, chi-square test, DuckDB facet bar, record listings, citizenship profiling block, foreigner-vs-Filipino comparison | Citizenship metrics: **Profiled no-PLE-match records 37,381**; **Foreigners 5,049**; **Filipinos 32,320**; **Distinct citizenship labels 43**. This DuckDB-backed sub-tab is where `import duckdb` (§1 gap) matters most — if it errors, that's the missing dependency |
| 4 | Score Bins & Background | Course group | Heatmap, top-bin share bar, percentile summary table | No metrics; table is `UNDERGRAD_COURSE_GROUP` × n/median/q25/q75 |
| 5 | University Type Analysis | — | Type×location tables, heatmap, bin composition, foreign-examinee summary | Metrics: **Foreign examinees 1,860**; **% of total 1.43%**; **Median percentile 52.0**; **Top bin % 34.30%** |
| 6 | Flow & Pathways | University → Bin | Sankey + flow-count table | Sankey total should equal `F["uni"]` row count; no metric widget |
| 6 | Flow & Pathways | Course → Bin | Sankey + flow-count table | same pattern |
| 6 | Flow & Pathways | Bin → PLE | Sankey (observable cohort only) + row-% pivot | Sankey population = 69,503 |
| 6 | Flow & Pathways | Top pathways | Two "largest pathway" tables (uni-type, course-group), top 10 each | — |
| 7 | PLE Alignment | Status profile | Score-profile-by-status table, boxplot, Mann-Whitney table | No metrics; check that "Confirmed" vs "No confirmed match" labels never say "failed" |
| 7 | PLE Alignment | Bin profile | Bin-distribution-by-status figure, composition bar, % table | Caption reports the count/pct of rows lacking a percentile bin, excluded from this figure |
| 7 | PLE Alignment | Background links | Course-group "survival" table, university-type PLE-alignment table (Table 27) | Table 27 must equal Tab 12's Table 3 (independent re-implementation of the same aggregation — a divergence here is a regression, see §6) |
| 7 | PLE Alignment | Policy tables | Alignment by year (28), by pre-med background (29), by university type (30) | Table 30 must equal Tab 12's Table 3 |
| 8 | Repeat Takers | — | Attempt-count histogram, trajectory summary, first-vs-last scatter, detail table with CSV download | Table 32's "Repeat-taker persons" should trace back to the 33,713 figure from Tab 1. Caption states the ~4.6% detectable name-collision rate and that the true rate is plausibly higher |
| 9 | Subtests & Profiles | University type | Standardized-subtest heatmap, raw-score table | No metrics |
| 9 | Subtests & Profiles | Course group | Same, by course group | No metrics |
| 9 | Subtests & Profiles | Radar profiles | Two radar charts (uni type, course group) + underlying tables | No metrics |
| 10 | Year Gap & Gender | PLE year gap | Histogram, boxplot by course group, summary table | Metrics: **Confirmed passers 29,519**; **Median year gap 6.0**; **Q1 year gap 6.0**; **Q3 year gap 7.0** |
| 10 | Year Gap & Gender | Gender patterns | Score-by-sex table, boxplot, composition-by-year bar, PLE-status-by-sex table | No metrics. "(not specified)" should appear as its own SEX category (see §7 troubleshooting) in the score table, but is excluded from the hardcoded Male/Female composition-by-year chart |
| 11 | Statistical Tests | Kruskal-Wallis by year | Table 43 | No metrics |
| 11 | Statistical Tests | PLE status tests | Table 44 (Mann-Whitney) | No metrics |
| 11 | Statistical Tests | Chi-square tests | Observed-counts table, chi-square summary (chi2/p/df/n/Cramér's V), heatmap, expected-counts table | No metrics |
| 11 | Statistical Tests | Post hoc | Dunn post-hoc matrix (Bonferroni-adjusted), heatmap | Only renders if `scikit-posthocs` is installed and ≥3 years are in the current filter |
| 12 | Policy Tables & Export | — | 4 tables (year/course/university/survival) identical in construction to Tab 7's 28/29/30 + survival, 4 CSV download buttons | Table values must equal Tab 7's — cross-check |
| 13 | CHED Compliance | — | Section A: cut-off scenario table + grouped bar; Section B: Foreign/Filipino composition; Section C: linkage gradient by bin | Section C table/chart must read **B1 11.6% (795/6,853), B2 22.7%, B3 29.3%, B4 36.0%, B5 45.6%, B6 50.4%, B7 53.6%, B8 55.0%, B9 61.6%, B10 71.0%** — these are the corrected, post-fix numbers (see the manuscript guides for what "corrected" means here) |

**Known quirks worth knowing, not bugs to chase:**
- "Table 9" is used twice (Tab 2's PLE match-outcome table and Tab 3's Kruskal-Wallis table) — a
  numbering collision in the UI labels, not a data problem.
- Table numbering skips from 35 to 37 in Tab 9 (no "Table 36").
- Download buttons exist only on Tabs 8, 12, 13. Large tables on Tabs 2, 4, 5 have no CSV export —
  copy manually from the on-screen `st.dataframe` if you need the data outside the app.

---

## 4. Per-tab acceptance checklist — CHED Dashboard (6 tabs)

Same method: default filters (none — this dashboard has no sidebar filters, it always shows the full
dataset split into best-record/observable subsets internally), values from live `AppTest` on
2026-08-14.

| # | Tab | What should appear | Numbers to read off screen |
|---|---|---|---|
| 1 | National Profile | Two-panel volume+percentile trend, uni-type/course pies, bin-reference table, repeat-taker note | Metrics: **Best-record examinees 134,869**; **Unique persons (PERSON_KEY) 134,869** (equal by construction, do not read as two different counts); NMAT years covered **13**; Median NMAT percentile **50.0** |
| 2 | B4+ vs B5+ Thresholds | Bin heatmap by year, threshold-scenario table, threshold-by-uni-type table, B4-group profile, top/bottom trend, yearly-threshold table, B5+ PLE-status stacked bars (count + %) | Metrics: **Public examinees meeting B5+ 17,752 (65.2%)**; **Public examinees in B4-only 2,247 (8.3%)**; **Private examinees meeting B5+ 60,184 (59.4%)**; **B4 examinees (best record) 12,589**; Median total raw score **109.0**; Public-institution share **17.8%**. The B5+ stacked bars must show a visible red "No confirmed PLE match" slice in most years — if it is flat zero in every year, the C-01 tautology bug (§6 below) has regressed |
| 3 | PLE-Passer Linkage | Linkage-by-bin bar (with 50% reference line), score-profile-by-status table, linkage-by-year/course/university-type charts, stress-test section | Metrics: **B5+ Filipino population 41,289**; **Confirmed under strict criteria 23,128**; **Strict-criteria linkage rate 56.0%**; Median PLE year gap **6 yrs**. The strict-criteria line chart must show values **below** 100% in at least some years — a flat 100% line is the C-01 regression (this is the "stress test," it exists specifically to NOT be tautological) |
| 4 | Institution and Foreign Context | Score-summary-by-uni-type table, box plot, bin heatmap, top-bin-share bar, foreign-examinee metrics, top-10-nationality bar | Metrics: **Verified Foreign NMAT examinees (best record) 24,069**; **Filipino examinees 110,787**; **Distinct foreign nationalities 89**. Score summary table: Public median %ile **57**, Private **49**, Foreign **52**. Top nationality **India, 19,090, 79.3%** of the 24,069 verified-foreign denominator (never against the top-10 subtotal — see caption) |
| 5 | Key Evidence for Policy Review | 8 narrative findings, no tables/charts | Read the "40th-Percentile Floor Was Not Uniformly Binding" finding — it must cite the live B1/B4 linkage numbers (11.6%/36.0%) and the 795-passer B1 figure, not the withdrawn 21-point-discontinuity framing |
| 6 | Data, Methods, and Limitations | Dataset overview, 5 methodology expanders, 9 limitation cards | 1 metric: **Stored-vs-derived mismatches — "56,065 of 99,316 rows with a stored total (56.5%)"**. Card 6 ("PHEI Accountability and Sanctions") must state plainly that no medical-school identifier exists at all. Card 9 must describe the corrected PLE-matcher disclosure (the 40th-percentile hard-filter bug, now fixed) |

**Both dashboards must agree where they overlap.** Both show 134,869 examinees, 69,503/observable
figures consistent with 45.44% linkage, and the same B1–B10 linkage gradient. A discrepancy between
the two on any of these is a regression, not a legitimate difference in scope.

---

## 5. Producing and verifying an export

### CHED dashboard — full export with a self-check block

**In-app:** expand "Export Complete Dashboard" at the top of the page → click "Generate & Download
(with Charts)" → then "Download Complete Dashboard (Markdown)".

**Headless (CI-friendly):**
```bash
cd streamlit_dashboard/CHED_relevant_dashboard
../../.venv/Scripts/python.exe export_markdown.py
```
Writes `complete_markdown/CHED_NMAT_Dashboard_Complete.md` and (if a `viz/` dir is reachable)
`viz/*.png` chart images. Both paths call the same `build_full_markdown()` function, so they cannot
drift from each other.

**Verify it matches the screen** — scroll to the `# Export Integrity` section at the very end of the
generated file:

```markdown
| check | result |
|---|---|
| Source parquet md5 | 28b85ac53af13b4a2ef3ee93527c97c1 |
| Rows / cols | 178,927 / 53 |
| Tabs exported | 6 / 6 |
| Charts exported as data | 15 / 15 |
| Tables exported | 34 |
| Captions exported | 41 |
| Dashboard-vs-export value assertions passed | 5 / 5 |
```

Check each row:
1. **md5** must equal `dataset/EXODUS_MANIFEST.json`'s `md5` field and the md5 of the parquet copy
   inside `CHED_relevant_dashboard/`. If not, the export ran against a stale/different file — re-copy
   or re-run `5_Slim_Exodus.py`.
2. **Tabs / Charts / assertions** are written as `N / total`. **If N < total for any row, the export
   is incomplete** — the file itself will also print a bolded warning
   (`**INCOMPLETE EXPORT — not all tabs were rendered. Do not treat this document as authoritative.**`).
   Do not distribute a short export; re-run and check stderr for the `compute_*()` call that raised.
3. Spot-check one number by hand: pick "Public median %ile" from the export's "Score Summary by
   University Type" table (should read 57) and compare it to the live dashboard's Tab 4 table. Both
   call `ched_common.compute_uni_score_summary()` — if they ever disagree, that is the historical
   57/49-vs-56/48 drift bug (RC-5) recurring, and is a release blocker.

### Main dashboard — full export with a self-check block

The main dashboard now has the same export the CHED dashboard has. Use the **"Export Complete
Dashboard"** expander at the top of the page, or regenerate it headlessly:

```bash
.venv/Scripts/python.exe streamlit_dashboard/main_dashboard/export_markdown.py
# writes streamlit_dashboard/main_dashboard/complete_markdown/NMAT_Main_Dashboard_Complete.md
```

Both paths call the same `main_common.compute_*()` functions the dashboard renders from, so the
document and the screen cannot silently disagree. The export covers the **unfiltered** cohort, not
whatever the sidebar happens to be set to — it says so in its own header.

**What to check in the self-check block at the end of the document:**

| line | expected |
|---|---|
| Source parquet md5 | `28b85ac53af13b4a2ef3ee93527c97c1` |
| Rows / cols (source parquet on disk) | `178,927 / 53` — the file, not the 58-column in-memory frame |
| Derived columns added at load time | 5 (`YEAR_INT`, `SEX_CLEAN`, `IS_BOARD_OBSERVABLE_COHORT`, `HAS_CONFIRMED_PLE`, `PLE_STATUS_LABEL`) |
| Tabs exported | 13 / 13 |
| **Charts exported as data** | **59 / 59** |
| Tables exported | 102 |
| Dashboard-vs-export value assertions passed | 5 / 5 |

The chart figure is a genuine check, not a self-satisfying ratio: `CHART_TABLE_MAP` in
`export_markdown.py` holds one entry per `st.plotly_chart()` call in `dashboard.py` (asserted equal
to 59 at import), and coverage is measured by looking for each chart's backing-table heading in the
assembled body. **If it ever reads below 59/59, a chart on screen has no table carrying its
numbers** — the document then lists the offending charts by name under "Charts NOT covered by a data
table". Treat that as a release blocker. To confirm the check still works, rename one backing-table
heading and re-run: it must drop to 58/59 and name that chart.

Use the **Chart-to-Table Index** near the top of the document to go from any chart on screen to the
table holding its values.

Per-tab CSV downloads still exist alongside the full export, on 3 of the 13 tabs:

| Tab | Files | Content |
|---|---|---|
| 8 Repeat Takers | `repeat_taker_detail_full.csv`, `appno_match_history_full.csv` | Full unsliced tables (the on-screen slider only limits the *displayed* rows, not the download) |
| 12 Policy Tables & Export | `policy_table_year.csv`, `policy_table_course.csv`, `policy_table_university.csv`, `policy_table_top_decile_survival.csv` | Reflect the sidebar filters active at download time (per the tab's own caption) |
| 13 CHED Compliance | `ched_cutoff_scenarios.csv`, `ched_linkage_gradient_by_bin.csv` | Section A / Section C tables |

**How to verify a main-dashboard CSV matches the screen** (the full export self-checks itself; these
per-tab CSVs do not, so check them by hand):
1. Download the CSV and open it (pandas, Excel, or a text viewer).
2. Compare its row count and column headers to the `st.dataframe` immediately above the download
   button on screen.
3. Spot-check 2–3 cell values. For `ched_linkage_gradient_by_bin.csv` under default filters, the B1
   row must read `n=6853, linked_n=795, linkage_rate_pct=11.6` — the same number in §3's Tab 13 row.
4. If a count is short (fewer rows than the on-screen table, or a filtered subset when you expected
   the full one), re-check the sidebar filter state before downloading — the policy tables in Tab 12
   are filter-sensitive by design; the Tab 8 and Tab 13 CSVs are not.

If you add a chart or a tab, `.claude/audit/_EXPORT_FORMAT_CONTRACT.md` is the spec both exporters
follow. In practice: add the chart, add its backing table, add an entry to `CHART_TABLE_MAP`, and
bump the `assert len(CHART_TABLE_MAP) == 59` to match the new `st.plotly_chart()` count. The assert
is deliberate — it makes a new chart fail loudly at import rather than quietly ship unexported.
The "Tab 7 vs Tab 12" duplicate-table quirk noted in §3 is resolved: both now call the single
`main_common.compute_ple_alignment_by()`.

---

## 6. Known-good reference output

Run these from the repo root and expect exactly these results (confirmed 2026-08-14):

```bash
.venv/Scripts/python.exe -m pytest tests/ -q
# -> 36 passed

.venv/Scripts/python.exe -c "
from streamlit.testing.v1 import AppTest
at = AppTest.from_file('streamlit_dashboard/CHED_relevant_dashboard/dashboard.py', default_timeout=540)
at.run()
print(len(at.exception), len(at.metric), len(at.dataframe), len(at.tabs))
"
# -> 0 18 19 6   (exceptions, metrics, dataframes, tabs)

.venv/Scripts/python.exe -c "
from streamlit.testing.v1 import AppTest
at = AppTest.from_file('streamlit_dashboard/main_dashboard/dashboard.py', default_timeout=540)
at.run()
print(len(at.exception), len(at.metric), len(at.dataframe), len(at.tabs))
"
# -> 0 27 74 42   (exceptions, metrics, dataframes, tabs)

.venv/Scripts/python.exe data_aggregator/run_all.py
# -> Complete: 13 passed, 0 failed

.venv/Scripts/python.exe streamlit_dashboard/main_dashboard/export_markdown.py
# -> wrote .../NMAT_Main_Dashboard_Complete.md
#    self-check: 178,927 / 53 | 13/13 tabs | 59/59 charts as data | 102 tables | 5/5 assertions

.venv/Scripts/python.exe streamlit_dashboard/CHED_relevant_dashboard/export_markdown.py
# -> wrote .../CHED_NMAT_Dashboard_Complete.md
#    self-check: 178,927 / 53 | 6/6 tabs | 15/15 charts as data | 5/5 assertions

.venv/Scripts/python.exe forensic_audit/forensic_audit.py
# -> AUDIT COMPLETE, 5 CSVs written into forensic_audit/
```

If any of these numbers differ on your machine, something in the data layer or dashboard code has
changed since this guide was written — re-read `RESUME.md` and
`.claude/audit/_ORCHESTRATOR_FINDINGS.md` before assuming your environment is broken.

---

## 7. Troubleshooting

**`ModuleNotFoundError: No module named 'ched_common'` (or similar sibling-import failure) in the
CHED dashboard.** Cause: `import ched_common` resolves under `streamlit run` (which puts the script's
own directory on `sys.path`) but fails if the module is imported another way — e.g. under `AppTest`,
or if `dashboard.py` is invoked via a full path from a different cwd. Fixed in commit `edc31ab`: both
`CHED_relevant_dashboard/dashboard.py` and `export_markdown.py` now insert their own directory onto
`sys.path` at the top of the file (before any sibling import), so the app is launchable and testable
from anywhere. Verify the fix is present: `grep -n "sys.path" streamlit_dashboard/CHED_relevant_dashboard/dashboard.py`
should show an `sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))` line near the top.
(The main dashboard has no sibling-module imports, so this particular failure mode does not apply to
it — if the main dashboard fails to launch, look at the parquet-path resolution below instead.)

**`FileNotFoundError: Could not locate NMAT_Exodus.parquet`.** Both dashboards look for the parquet
in a short list of candidate paths relative to their own directory (`find_data_path()` in
`ched_common.py`; an equivalent list in `main_dashboard/dashboard.py`). If you moved or deleted a
dashboard's local parquet copy, either restore it from `dataset/NMAT_Exodus.parquet` or re-run
`5_Slim_Exodus.py`, which copies the canonical file into both dashboard folders and writes
`dataset/EXODUS_MANIFEST.json`.

**Stale Streamlit cache / dashboard shows old numbers after a data change.** Both dashboards use
`@st.cache_data` on the parquet load. In-app: use the "⋮" menu → "Clear cache", or press `C` then
`Enter` in the running terminal. From a clean start, just restart the `streamlit run` process — cache
is per-process and does not persist across restarts.

**Parquet md5 mismatch between the three copies** (`dataset/`, `main_dashboard/`,
`CHED_relevant_dashboard/`). This should never happen if `5_Slim_Exodus.py` was the last thing to
touch any of the three files — it writes all three from one in-memory dataframe and hard-fails
(`raise SystemExit`) if the resulting files aren't byte-identical. If you see a mismatch, one copy was
edited or replaced by hand outside the pipeline. Fix: re-run `python 5_Slim_Exodus.py` from the repo
root (requires `dataset/NMAT_Exodus.parquet.bak` — the Pipeline 4 output — to exist), then re-run
`pytest tests/ -v`; `test_dashboard_copies_are_byte_identical` and
`test_manifest_md5_matches_canonical_file` will catch any remaining divergence.

**`duckdb` import error in the main dashboard's Tab 4 "University type" sub-tab.** See §1 — root
`requirements.txt` omits `duckdb`; install it separately or use
`streamlit_dashboard/main_dashboard/requirements.txt`.

**Dunn post-hoc panel (Tab 11) doesn't render.** Requires `scikit-posthocs` (in both requirements
files) and at least 3 distinct years in the current sidebar filter — it silently skips otherwise by
design, not a bug.

**A number in the app doesn't match this guide.** First re-run the exact `AppTest`/`pytest` command
from §6 to see if the *code* still produces the reference numbers. If it does, your app-under-test is
running against different data (check the parquet md5, §above). If it doesn't, the code changed since
this guide was written — check `git log` for anything touching `dashboard.py`, `ched_common.py`, or
the pipeline scripts after 2026-08-14, and treat this guide's specific number (not the general
procedure) as superseded.

**Do not trust `forensic_audit/` conclusions as a validation source.** Per
`AUDIT_AND_REMEDIATION_PLAN.md` §9, that suite's headline "4 genuine mismatches" claim required an
undocumented manual override and does not reproduce from the committed scripts alone. Use the
`pytest tests/` invariant suite and the `AppTest` reference counts in this guide instead.
