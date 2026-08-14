# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**NMAT Analysis** is a research/policy analytics pipeline analyzing the Philippine National Medical Admissions Test (2006–2018) with linkage to Philippine Licensure Examination (PLE) outcomes and citizenship data.

**Key deliverable:** `dataset/NMAT_Exodus.parquet` (178,927 rows × **53 columns**, md5
`28b85ac53af13b4a2ef3ee93527c97c1`, shipped as 3 byte-identical copies) consumed by:
1. `streamlit_dashboard/main_dashboard/dashboard.py` — Streamlit, **live, source of truth**
2. `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py` — CHED-specific Streamlit variant, **live**
3. `data_aggregator/` — static markdown report generator, **live**

**Legacy, not maintained** — do not treat these as reflecting the current schema or matcher, and
do not port new features into them without an explicit ask: `RShiny_Dashboard/NMAT_Shiny/app.R`,
`RShiny_Dashboard/NMAT_Shiny/NMAT_Dashboard_v2.Rmd`, `reports/`, root `dashboard.py` /
`dashboard.py.bak`.

> **2026-08 remediation notice.** This file was rewritten against the corrected pipeline and
> schema. If anything you read elsewhere in this repo's history says "54 columns"
> or references `IS_PLE_ANALYSIS_SAFE`, `UNI_TYPE`, `CourseGroup`, or `NMA_College` —
> that predates this remediation and is superseded. See `docs/pipeline_architecture.md` §7 for the
> two root-cause defects found and fixed (a hard percentile floor in the PLE matcher, and dead DOB
> disambiguation code) and what they changed downstream.

---

## Essential Commands

### Setup
```bash
# Activate virtual environment (first time)
python -m venv .venv
.\.venv\Scripts\Activate.ps1          # Windows PowerShell
source .venv/bin/activate              # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Optional: One-click dependency install via Jupyter
jupyter notebook 00_RUN_ME.ipynb
```

### Run Main Dashboard (production)
```bash
cd streamlit_dashboard/main_dashboard
streamlit run dashboard.py
```

### Run CHED-Specific Dashboard
```bash
cd streamlit_dashboard/CHED_relevant_dashboard
streamlit run dashboard.py
```

Both dashboards must be launched **from their own directory** — each loads its own local copy of
`NMAT_Exodus.parquet` (byte-identical to the canonical one) via a relative path.

### Legacy R Dashboards (reference only, not maintained)
```bash
# RShiny interactive
cd RShiny_Dashboard/NMAT_Shiny
Rscript -e "shiny::runApp('app.R')"

# Or: R Markdown static HTML
# Knit NMAT_Dashboard_v2.Rmd in RStudio
```

### Re-run Data Pipelines (in order — chain is 1→2→3→4→5)
```bash
# Pipelines 1-3 (notebooks)
jupyter notebook 1_Data_Cleaning_Pipeline.ipynb
jupyter notebook 2_PLE_Matching_Pipeline.ipynb
jupyter notebook 3_NMAT_PLE_Analysis.ipynb      # analysis-only; not required for the dashboards

# Pipeline 4 — citizenship enrichment
.venv\Scripts\python.exe 4_Citizenship_Integration.py

# Pipeline 5 — slims Pipeline 4's 118-col output to the shipped 53-col schema,
# writes both dashboard copies + dataset/EXODUS_MANIFEST.json. MUST run after Pipeline 4.
.venv\Scripts\python.exe 5_Slim_Exodus.py
```

### Generate Static Reports from Data Aggregator
```bash
.venv\Scripts\python.exe data_aggregator/run_all.py
# Runs correctly from the repo root OR from inside data_aggregator/ — paths resolve
# relative to the script, not the cwd.
# Outputs: data_aggregator/page_results/*.md (13 markdown files, 13/13 expected)
```

### Run Tests
```bash
.venv\Scripts\python.exe -m pytest tests/ -q
# 36 passed is the current, expected state. Asserts the schema contract in
# .claude/audit/_TARGET_SCHEMA_CONTRACT.md.
```

### Run the Forensic Audit
```bash
.venv\Scripts\python.exe forensic_audit/forensic_audit.py
# The audit suite was consolidated into this single script. Older references to
# forensic_audit_v5_final.py / audit_per_bin_report.py / audit_name_check_deep.py are stale —
# those files no longer exist.
# Writes 5 CSVs: forensic_audit_summary.csv, forensic_audit_selection_effect.csv,
# forensic_audit_contingency_2x2.csv, forensic_audit_name_check_results.csv,
# forensic_audit_exceptions.csv (all in forensic_audit/).
```

---

## Architecture & Data Flow

### 5-Pipeline Transformation Chain
```
Raw CSV Input (NMAT_CLEANED_DATA, CEM_DATA, PLE_DATA)
    ↓
Pipeline 1: Data Cleaning (1_Data_Cleaning_Pipeline.ipynb)
    • Standardize application numbers
    • Validate university names via 4-tier matching (UNIVS.csv, incl. rapidfuzz — the ONLY
      fuzzy matching anywhere in this project)
    • Recalculate raw scores — stored totals disagree with the recalculated total in 56.45%
      of the 99,316 records that carry a stored total ("42.2%" is the SAME mismatch counted
      over the whole CEM file, 107,422/254,308 — a different population, not an error;
      see docs/pipeline_architecture.md)
    • Create percentile bins (B1 = lowest decile .. B10 = highest)
    → Output: NMAT_FINAL.csv (101 cols) — the file Pipeline 2 actually reads.
      (A NMAT_FINAL.parquet twin had zero readers and was removed in dataset cleanup.)
    ↓
Pipeline 2: PLE Matching (2_PLE_Matching_Pipeline.ipynb)
    • 3-stage deterministic matching: AppNo recovery → exact name → deterministic AppNo
    • No fuzzy matching in this pipeline (deterministic-only, for auditability)
    • Disambiguator for name collisions: year-gap → DOB/sex → latest year → exactly one
      survivor accepted, 2+ rejected as ambiguous. NO score-based step. (A hard 40th-percentile
      floor and a score-based tie-break both used to sit here — both were identity-resolution
      bugs that biased matching against the exact population this project studies. Both removed;
      see docs/pipeline_architecture.md §7.)
    → Output: NMAT_Ultima.parquet (119 cols), PLE_MATCH_MASTER.csv
    ↓
Pipeline 3: Statistical Analysis (3_NMAT_PLE_Analysis.ipynb)
    • 13 analysis sections (~95 output CSVs + PNGs)
    • Kruskal-Wallis, Mann-Whitney, Chi-square tests
    • Sankey flow diagrams, radar profiles, trend charts
    → Output: dataset/analysis_output/ (~95 files). Analysis-only — not on the path that
      produces the shipped Exodus file.
    ↓
Pipeline 4: Citizenship Integration (4_Citizenship_Integration.py)
    • 3-tier hierarchy: REAL_FOREIGNERS.csv (Tier 1a, 1b) → pseudo-citizenship (Tier 2) → default Filipino (Tier 3)
    → Output: NMAT_Exodus.parquet.bak (118 cols) — a WIDE intermediate, NOT the shipped file.
      Deliberately kept as the only full-column audit trail in the repo; do not delete.
    ↓
Pipeline 5: Slim Exodus (5_Slim_Exodus.py)  ***NEW — previously this step had no code at all***
    • Selects/renames/coerces Pipeline 4's 118-col output down to the shipped 53-col schema
    • Asserts structural invariants (hard-fail) and warns (non-blocking) on reference-count drift
    → Output: dataset/NMAT_Exodus.parquet (53 cols) + byte-identical copies in both dashboard
      folders + dataset/EXODUS_MANIFEST.json
    ↓
Dashboards consume NMAT_Exodus.parquet
    • streamlit_dashboard/main_dashboard/dashboard.py (interactive, filters, downloads)
    • streamlit_dashboard/CHED_relevant_dashboard/dashboard.py (CHED cut-off focus)
    • data_aggregator/ (static markdown reports)
```

### Key Dataset Columns
**Core identifiers:** `APPNO_CLEAN`, `PERSON_KEY`, `Year`, `SEX` — note there is **no**
`PERSON_NAME` column in the shipped file.

**Scores (standardized & raw):** `NMS_PER_num`, 8× NMAT subtests (`NMS_*ss`),
`TotalRawScoreTRUE`, `PLE_YEAR_PASSED`

**Classification (undergraduate institution, NOT medical school — see below):**
`UNDERGRAD_UNI_TYPE` (Public/Private/Foreign/Not Specified), `UNDERGRAD_COURSE_GROUP` (6 values),
`PercentileBin` (B1–B10, B1 = lowest), `UNDERGRAD_UNI_LOCATION`

**Flags:** `IS_BEST_NMAT_RECORD` (one uniform rule, dedupe repeat takers),
`IS_OBSERVABLE_COHORT` (`Year <= 2014`), `IS_BEST_OBSERVABLE_RECORD` (**the correct
observable-cohort person filter** — do not substitute `IS_BEST_NMAT_RECORD & (Year<=2014)`, which
drops 3,721 people), `PERSON_KEY_AMBIGUOUS` (6,148 keys with contradictory SEX — a name-collision
signal for the weak `PERSON_KEY`)

**PLE linking:** `IS_PLE_PASSER` (**the only authoritative passer flag, 49,086 — not 49,986**),
`PLE_MATCH_METHOD`, `PLE_MATCH_CONFIDENCE`, `PLE_MATCH_OUTCOME`
(`accepted`/`rejected`/`rejected_ambiguous_person`/`no_match`), `PLE_YEAR_UNCERTAIN`. There is
**no** `PLE_MATCH_STATUS` column in the shipped file — use `PLE_MATCH_OUTCOME`.

**Citizenship:** `CITIZENSHIP_FINAL`, `FOREIGNER_STATUS` (Verified Foreigner / Likely Foreigner / Filipino)

**Removed entirely (do not reference):** `IS_PLE_ANALYSIS_SAFE` (was byte-identical to
`IS_PLE_PASSER`), `NMA_College`, `AllRawComponentsPresent`, `CalcVsDerivedMismatch`,
`name_based_assessment`, `HasCEMMatch` (was byte-identical to `HasTRUErawScores`).

**Renamed** (applicant's undergraduate institution, not a medical school — no medical-school
identifier exists in this dataset at all): `UNIVERSITY`→`UNDERGRAD_UNIVERSITY`,
`UNI_TYPE`→`UNDERGRAD_UNI_TYPE`, `UNI_LOCATION`→`UNDERGRAD_UNI_LOCATION`,
`CourseGroup`→`UNDERGRAD_COURSE_GROUP`.

See `docs/data_dictionary.md` for the full 53-column reference, in actual column order, with
verified value counts.

---

## Critical Design Decisions

### Observable Cohort Rule
**`Year <= 2014` (`IS_OBSERVABLE_COHORT`) is used for PLE-aligned analysis.** Examinees from 2015+
may not have taken PLE yet, so excluding recent years prevents false negatives in linkage
calculations. **For person-level analysis, filter on `IS_BEST_OBSERVABLE_RECORD` (69,503 people),
never on `IS_BEST_NMAT_RECORD & (Year <= 2014)` (65,782 people)** — the naive combination
silently drops 3,721 people whose overall-best attempt falls after 2014.

### Best-Record Deduplication
25% of examinees appear 2+ times. `IS_BEST_NMAT_RECORD` selects **one best attempt per person**
using one uniform rule for every person: highest `NMS_PER_num` → latest `Year` → lowest
`APPNO_CLEAN`. (An earlier version used a different rule for PLE passers than for everyone else
and silently dropped 1,311 people from every person-level count — fixed.) Always filter by this
when counting unique individuals.

### Deterministic Matching Only — and No Score-Based Identity Resolution
**All fuzzy/rapidfuzz matching in Pipeline 2 removed.** PLE matches use only deterministic
cascades (exact application numbers, confirmed names) plus a disambiguator that resolves identity
on year-gap, DOB/sex, and latest-year evidence only — **never on percentile score.** A hard
percentile-floor filter and a score-based tie-break both used to exist in the disambiguator; both
were found to bias matching against low-percentile examinees — exactly the population the CHED
cut-off question is about — and both are removed. See `docs/pipeline_architecture.md` §7.

### Raw Score Recalculation
Stored `StoredRawTotal` values in CEM data disagree with the recalculated `TotalRawScoreTRUE` in
**56.45% of the 99,316 records that carry a stored total** (31.33% of all rows). `TotalRawScoreTRUE`
is recalculated by summing 8 component raw scores and is the canonical value. **The figure "42.2%"
is also correct** — it is the same mismatch counted over the whole `CEM_DATA.csv` (107,422 of
254,308 rows). Two populations, not an error; always name the denominator. Note that CEM already
flagged these itself: `STU_RSCORE_VALID` marks exactly those rows `INVALID`, zero exceptions either
way, so the recalculation reproduces a pre-existing CEM QA judgement rather than discovering it.

### `PERSON_KEY` Is a Weak Identity Key
Built from normalized name + a coarse birthdate fragment (14.09% of rows have no birthdate
component at all). 6,148 keys (`PERSON_KEY_AMBIGUOUS`) carry contradictory `SEX` — direct proof of
name collisions merging distinct people. Treat every person-level count as carrying this
uncertainty; do not present repeat-taker or person counts as exact.

### No Institution-Level PLE Performance Claims
`UNDERGRAD_UNIVERSITY` / `UNDERGRAD_UNI_TYPE` describe the applicant's **undergraduate** degree.
No medical-school identifier exists anywhere in this dataset, so no PLE passing-rate claim can be
attributed to a medical school, and `UNDERGRAD_UNI_TYPE` is not a valid SUC/PHEI proxy for CMO
purposes.

---

## Directory Structure

### Root Level
- `4_Citizenship_Integration.py` — Pipeline 4, citizenship enrichment
- `5_Slim_Exodus.py` — Pipeline 5, produces the shipped `NMAT_Exodus.parquet`
- `requirements.txt` — All Python dependencies (pandas, numpy, plotly, streamlit, scipy, etc.)
- `dashboard.py` / `dashboard.py.bak` — **legacy**, not the production entry point (see "Working with Dashboards")
- `.venv/` — Virtual environment (ignored in git)

### Notebooks (Pipelines 1–3)
- `1_Data_Cleaning_Pipeline.ipynb` — Cleaning, standardization, bin creation
- `2_PLE_Matching_Pipeline.ipynb` — PLE linking logic (deterministic cascade + disambiguator)
- `3_NMAT_PLE_Analysis.ipynb` — 13 statistical analysis sections (analysis-only)
- `00_RUN_ME.ipynb` — Convenience one-click dependency installer

### Datasets
- `dataset/NMAT_Exodus.parquet` — Final analytic dataset (53 cols, 178,927 rows)
- `dataset/NMAT_Exodus.parquet.bak` — Full 118-column backup, the only one; deliberately retained
- `dataset/EXODUS_MANIFEST.json` — md5/row/col counts + reference-count deltas, written by Pipeline 5
- `dataset/DATASET_MANIFEST.md` — file-by-file classification of everything in `dataset/`
- `dataset/NMAT_CLEANED_DATA.csv` — Raw NMAT input
- `dataset/PLE_DATA.csv`, `PLE_UNMATCHED.csv` — Raw PLE records
- `dataset/UNIVS.csv` — University reference list (2,981 verified names)
- `dataset/REAL_FOREIGNERS.csv` — Ground-truth citizenship Tier 1
- `dataset/pseudo_citizenship_profiling_FINAL.csv` — Inferred citizenship Tier 2
- **Gone (do not reference as existing):** `dataset/NMAT_Exodus.csv` (dead mirror, zero readers),
  `dataset/output/NMAT_FINAL.parquet` (dead twin of `NMAT_FINAL.csv`), `dataset/UNIVS_ARCHIVED.csv`
  (dead artifact) — all removed in the 2026-08 dataset-hygiene cleanup.

### Data Aggregator (Static Report Generation)
```
data_aggregator/
├── config.py                   # Shared constants (bins, palettes, columns) — resolves paths
│                                # relative to __file__, so it works from any cwd
├── helpers.py                  # Query and charting utilities (pandas-based)
├── run_all.py                  # Entry point (runs all 13 pages, verifies non-empty output)
├── aggregate_all.py            # Concatenates the 13 pages into 00_MASTER_REPORT.md
├── page_01_executive_summary.py through page_13_ched_compliance.py
└── page_results/               # Output markdown files (generated)
```
Each page script mirrors a dashboard tab and outputs a markdown report.
**Correction:** this package does not use DuckDB — `grep -rn duckdb data_aggregator/*.py` returns
nothing. It is pandas-based throughout; an earlier claim that it used DuckDB was fiction.

### R Dashboards (legacy, not maintained)
```
RShiny_Dashboard/NMAT_Shiny/
├── app.R                       # Main Shiny app (~2,200 lines)
├── NMAT_Dashboard_v2.Rmd       # R Markdown flexdashboard (static HTML)
└── setup.R                     # R package installer
```
Predates the schema/matcher remediation. Do not treat as a parity target for new dashboard work
without an explicit ask to revive it.

### Live Streamlit Dashboards
```
streamlit_dashboard/
├── main_dashboard/
│   └── dashboard.py            # Main production dashboard, 12 tabs
└── CHED_relevant_dashboard/
    ├── dashboard.py            # CHED cut-off-focused dashboard
    ├── export_markdown.py      # Export to markdown
    ├── ched_compute/           # Computational modules
    └── viz/                    # Static images used in the dashboard
```

### Forensic Audit Suite
```
forensic_audit/
└── forensic_audit.py           # The consolidated audit suite (only script here now).
                                 # Writes forensic_audit_summary.csv, _selection_effect.csv,
                                 # _contingency_2x2.csv, _name_check_results.csv, _exceptions.csv.
```
Older references to `forensic_audit_v5_final.py`, `audit_per_bin_report.py`,
`audit_name_check_deep.py`, or `_check_missing.py` are stale — those scripts no longer exist.

### Documentation
- `README.md` — Full pipeline overview, architecture, key decisions
- `docs/data_dictionary.md` — Complete 53-column reference, in actual column order
- `docs/pipeline_architecture.md` — Detailed pipeline diagrams (Mermaid), including the two
  root-cause defects found during remediation
- `changelog.md` — Recent changes and feature additions

---

## Working with Dashboards

### Main Dashboard (production)
- **Entry:** `cd streamlit_dashboard/main_dashboard && streamlit run dashboard.py`
- **12 tabs:** Executive Summary, Data Integrity, Trends & Stability, Score Bins, University Type, Flow & Pathways, PLE Alignment, Repeat Takers, Subtests & Profiles, Year Gap & Gender, Statistical Tests, Policy Tables & Export
- **Filters (sidebar):** Year, University Type, Course Group, Sex, PLE Status
- **Features:** Interactive Plotly charts, hover tooltips, CSV download buttons
- **Performance notes:** Uses `@st.cache_data` for parquet load and expensive aggregations. Cache key includes data version to bust stale data.

### CHED-Relevant Dashboard
- **Entry:** `cd streamlit_dashboard/CHED_relevant_dashboard && streamlit run dashboard.py`
- Focused on the CMO §IV.B.1 cut-off question — includes the below-40th-percentile linkage finding
  (`docs/pipeline_architecture.md` §7): 6,173 of 25,596 below-40 observable examinees (24.1%) are
  confirmed PLE passers.

### Data Aggregator (Static Markdown)
- **Entry:** `.venv\Scripts\python.exe data_aggregator/run_all.py` (repo root or `data_aggregator/`, both work)
- **Output:** 13 markdown files in `page_results/` (one per dashboard page), 13/13 expected
- **Tech:** pandas throughout (see the DuckDB correction above)
- **Use case:** Generate static reports for archives or email distribution

### R Shiny (legacy, reference only)
- **Entry:** `cd RShiny_Dashboard/NMAT_Shiny && Rscript -e "shiny::runApp('app.R')"`
- Not verified against the current 53-column schema or the corrected matcher. Do not assume parity.

---

## Important Notes

### Synchronization Across the Live Deliverables
`streamlit_dashboard/main_dashboard/dashboard.py` is the **source of truth** among the two live
dashboards. After updates:
1. Verify changes work in `main_dashboard/dashboard.py`
2. Port changes to `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py` where relevant to
   the CHED-focused scope
3. Update `data_aggregator/` page scripts if analysis logic changes
4. Legacy consumers (`RShiny_Dashboard/`, root `dashboard.py`) are **not** part of this
   synchronization obligation — do not port changes there without an explicit ask.

All three live consumers read the same `NMAT_Exodus.parquet` (3 byte-identical copies enforced by
`5_Slim_Exodus.py`), so schema mismatches must be caught before release —
`.venv\Scripts\python.exe -m pytest tests/ -q` (36 passed expected) is the fast check.

### Debugging Data Issues
1. **Parquet schema mismatch?** Check `dataset/NMAT_Exodus.parquet.bak` for the full 118-column
   version, and `dataset/EXODUS_MANIFEST.json` for the current shipped column list + md5.
2. **Missing or stale data in dashboard?** Clear Streamlit cache: `streamlit cache clear` or
   restart the app.
3. **PLE matching suspect?** Run `forensic_audit/forensic_audit.py` to validate matches, and read
   `docs/pipeline_architecture.md` §7 first — two prior identity-resolution bugs (percentile
   floor, dead DOB check) have already been found and fixed; check whether a suspected issue is
   actually one of those, already resolved.
4. **Bin distribution off?** Check `IS_BEST_NMAT_RECORD` / `IS_BEST_OBSERVABLE_RECORD` filtering —
   duplicates and the naive-cohort-filter trap can both skew counts.

### Performance Optimization
- `data_aggregator/helpers.py` is pandas-based (see the DuckDB correction above — there is no
  DuckDB dependency in this project despite earlier claims).
- Streamlit caching with `@st.cache_data` reduces re-computation; clear manually if data changes.

---

## Common Tasks

### Add a New Analysis to a Dashboard
1. Create a new function in `streamlit_dashboard/main_dashboard/dashboard.py` that reads from
   `NMAT_Exodus.parquet`
2. Add a new tab using `st.tab()` or navigation in the sidebar
3. Port to `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py` if relevant to its scope
4. If static reports needed, add a new page script `data_aggregator/page_XX_*.py`
5. Update `data_aggregator/run_all.py` to include the new page

### Modify Data Pipeline
1. Edit the relevant notebook (`1_*.ipynb` through `3_*.ipynb`) or Python script (`4_*.py`,
   `5_Slim_Exodus.py`)
2. Test locally: re-run the pipeline chain **in order, through Pipeline 5**, check output
   schema/counts against `.claude/audit/_TARGET_SCHEMA_CONTRACT.md`
3. Verify downstream consumers still work:
   `.venv\Scripts\python.exe -m pytest tests/ -q`, then both live dashboards
4. Document changes in `changelog.md` and commit with a clear message

### Fix a Bug in PLE Matching
1. Run the forensic audit: `.venv\Scripts\python.exe forensic_audit/forensic_audit.py`
2. Examine false positives/negatives in audit output
3. Edit `2_PLE_Matching_Pipeline.ipynb` → adjust cascade logic or `disambiguate()`. **Do not add
   any score-based step** (percentile, standard score) to identity resolution — that is the exact
   bug class already found and removed (RC-0, O-24 in `docs/pipeline_architecture.md` §7).
4. Re-run Pipeline 2, then Pipelines 4 and 5 in order to propagate the fix into the shipped file
5. Re-run Pipeline 3 if analysis-only outputs also need to reflect the fix
6. Verify dashboards show corrected linkage rates (never call it a "pass rate" — the PLE source
   contains passers only)

### Export Data for External Use
- CSV export via the dashboards' "Policy Tables & Export" tab (recommended for non-technical users)
- Raw parquet: `pd.read_parquet("dataset/NMAT_Exodus.parquet")` in Python
- R: `arrow::read_parquet("dataset/NMAT_Exodus.parquet")` in R
- Data aggregator markdown: `.venv\Scripts\python.exe data_aggregator/run_all.py` → outputs in `page_results/`

---

## Dependencies & Versions
- Python 3.8+ (3.10+ recommended)
- pandas ≥ 1.5, numpy ≥ 1.24, pyarrow ≥ 10
- scipy ≥ 1.10, scikit-posthocs (for Dunn post-hoc)
- plotly ≥ 5.15, kaleido (for static image export)
- streamlit ≥ 1.25
- pytest ≥ 7.0 (for `tests/`)
- R (optional, legacy dashboards only): shiny, shinydashboard, arrow, plotly, dplyr, flexdashboard

---

## Lean-ctx MCP Integration

This project uses the **lean-ctx** MCP runtime (see global `~/.claude/CLAUDE.md`):
- Use `ctx_read` instead of `Read` for cached file access
- Use `ctx_shell` instead of `Bash` for shell commands
- Use `ctx_search` instead of `Grep` for code searches
- Use `ctx_tree` instead of `ls` for directory exploration

This compresses context by up to 99% via intelligent summarization.

---

## GitLab/GitHub Integration

- Repository: Git repository initialized at `.git/`
- Main branch: `master`
- Recent commits: Data pipeline remediation (5-pipeline chain, matcher fixes), dashboard schema
  migration, documentation rewrite
- Untracked: `.temp/`, `.agents/`, `.artifacts/` (build artifacts and agent outputs)

---

*Last updated: 2026-08-14 | NMAT Analysis | 53-column Exodus schema, post-remediation*
