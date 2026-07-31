# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**NMAT Analysis** is a research/policy analytics pipeline analyzing the Philippine National Medical Admissions Test (2006–2018) with linkage to Philippine Licensure Examination (PLE) outcomes and citizenship data.

**Key deliverables:** `dataset/NMAT_Exodus.parquet` (178,927 rows × 54 columns) consumed by 3 dashboard implementations:
1. `dashboard.py` — Streamlit (2,800+ lines, source of truth)
2. `RShiny_Dashboard/NMAT_Shiny/app.R` — R Shiny (2,200+ lines)
3. `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py` — CHED-specific Streamlit variant

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
streamlit run dashboard.py
```

### Run CHED-Specific Dashboard
```bash
cd streamlit_dashboard/CHED_relevant_dashboard
streamlit run dashboard.py
```

### Run R Dashboards
```bash
# RShiny interactive
cd RShiny_Dashboard/NMAT_Shiny
Rscript -e "shiny::runApp('app.R')"

# Or: R Markdown static HTML
# Knit NMAT_Dashboard_v2.Rmd in RStudio
```

### Re-run Data Pipelines (in order)
```bash
# Full pipeline (1–4, takes 5–10 minutes)
jupyter notebook 1_Data_Cleaning_Pipeline.ipynb
jupyter notebook 2_PLE_Matching_Pipeline.ipynb
jupyter notebook 3_NMAT_PLE_Analysis.ipynb
python 4_Citizenship_Integration.py

# Pipeline 4 only (fastest, 30 seconds)
python 4_Citizenship_Integration.py
```

### Generate Static Reports from Data Aggregator
```bash
cd data_aggregator
python run_all.py
# Outputs: page_results/*.md (13 markdown files)
```

### Run Forensic Audits
```bash
cd forensic_audit
python forensic_audit_v5_final.py      # Final audit suite
python audit_per_bin_report.py         # Per-bin breakdown
python audit_name_check_deep.py        # Name matching verification
```

---

## Architecture & Data Flow

### 4-Pipeline Transformation Chain
```
Raw CSV Input (NMAT_CLEANED_DATA, CEM_DATA, PLE_DATA)
    ↓
Pipeline 1: Data Cleaning (1_Data_Cleaning_Pipeline.ipynb)
    • Standardize application numbers
    • Validate university names via 4-tier matching (UNIVS.csv)
    • Recalculate raw scores (42.2% of CEM totals were incorrect)
    • Create percentile bins (B1–B10)
    → Output: NMAT_FINAL.parquet (101 cols)
    ↓
Pipeline 2: PLE Matching (2_PLE_Matching_Pipeline.ipynb)
    • 3-stage deterministic matching: AppNo recovery → exact name → deterministic AppNo
    • No fuzzy matching (removed rapidfuzz for auditability)
    • 5-step disambiguator for multiple matches (year-gap, DOB, latest year, percentile, tiebreak)
    → Output: NMAT_Ultima.parquet (115 cols), PLE_MATCH_MASTER.csv
    ↓
Pipeline 3: Statistical Analysis (3_NMAT_PLE_Analysis.ipynb)
    • 13 analysis sections (95 output CSVs + PNGs)
    • Kruskal-Wallis, Mann-Whitney, Chi-square tests
    • Sankey flow diagrams, radar profiles, trend charts
    → Output: data/ folder with 95 files (one per analysis)
    ↓
Pipeline 4: Citizenship Integration (4_Citizenship_Integration.py)
    • 3-tier hierarchy: REAL_FOREIGNERS.csv (Tier 1a, 1b) → pseudo-citizenship (Tier 2) → default Filipino (Tier 3)
    • 129 raw nationalities canonicalized to 96 values
    → Output: NMAT_Exodus.parquet (54 cols, 10.5 MB)
    ↓
Dashboards consume NMAT_Exodus.parquet
    • Streamlit dashboard.py (interactive, filters, downloads)
    • RShiny NMAT_Shiny/app.R (interactive, R ecosystem)
    • Data aggregator (static markdown reports)
```

### Key Dataset Columns
**Core identifiers:** APPNO_CLEAN, PERSON_KEY, PERSON_NAME, Year

**Scores (standardized & raw):** NMS_PER_num, 8× NMAT subtests (NMS_*ss), TotalRawScoreTRUE, PLE_YEAR_PASSED

**Classification:** UNI_TYPE (Public/Private/Foreign), CourseGroup (6 values), PercentileBin (B1–B10), UNI_LOCATION

**Flags:** IS_BEST_NMAT_RECORD (deduplicate repeat takers), IS_PLE_ANALYSIS_SAFE (observable cohort: Year ≤ 2014), IS_BOARD_OBSERVABLE_COHORT

**PLE linking:** PLE_MATCH_METHOD, PLE_MATCH_CONFIDENCE, PLE_MATCH_STATUS ("Confirmed PLE passer" / "No confirmed PLE match")

**Citizenship:** CITIZENSHIP_FINAL, FOREIGNER_STATUS (Verified Foreigner / Likely Foreigner / Filipino)

See `data_dictionary.md` for full 54-column reference.

---

## Critical Design Decisions

### Observable Cohort Rule
**Only Year ≤ 2014 is used for PLE-aligned analysis.** Examinees from 2015+ may not have taken PLE yet, so excluding recent years prevents false negatives in pass-rate calculations.

### Best-Record Deduplication
25% of examinees appear 2+ times. `IS_BEST_NMAT_RECORD` flag selects **one best attempt per person** (latest year → highest percentile → earliest attempt). Always filter by this when counting unique individuals.

### Deterministic Matching Only
**All fuzzy/rapidfuzz matching removed.** PLE matches use only deterministic cascades (exact application numbers, confirmed names). This ensures matches are auditable and human-verifiable, not probabilistic.

### Raw Score Recalculation
42.2% of `StoredRawTotal` values in CEM data were mathematically incorrect. `TotalRawScoreTRUE` is recalculated by summing 8 component raw scores and is the canonical value.

---

## Directory Structure

### Root Level
- `dashboard.py` — Main Streamlit app (2,800 lines), single entry point for production
- `4_Citizenship_Integration.py` — Final enrichment pipeline
- `requirements.txt` — All Python dependencies (pandas, numpy, plotly, streamlit, scipy, etc.)
- `NMAT_Analysis.zip` — Archived raw dataset
- `.venv/` — Virtual environment (ignored in git)

### Notebooks (Pipelines 1–3)
- `1_Data_Cleaning_Pipeline.ipynb` — Cleaning, standardization, bin creation
- `2_PLE_Matching_Pipeline.ipynb` — PLE linking logic (deterministic cascade)
- `3_NMAT_PLE_Analysis.ipynb` — 13 statistical analysis sections
- `00_RUN_ME.ipynb` — Convenience one-click dependency installer

### Datasets
- `dataset/NMAT_Exodus.parquet` — Final analytic dataset (54 cols, 178k rows)
- `dataset/NMAT_Exodus.parquet.bak` — Full 118-column backup
- `dataset/NMAT_CLEANED_DATA.csv` — Raw NMAT input
- `dataset/PLE_DATA.csv`, `PLE_UNMATCHED.csv` — Raw PLE records
- `dataset/UNIVS.csv` — University reference list (2,981 verified names)
- `dataset/REAL_FOREIGNERS.csv` — Ground-truth citizenship Tier 1
- `dataset/pseudo_citizenship_profiling_FINAL.csv` — Inferred citizenship Tier 2

### Data Aggregator (Static Report Generation)
```
data_aggregator/
├── config.py                   # Shared constants (bins, palettes, columns)
├── helpers.py                  # DuckDB queries, charting utilities
├── run_all.py                  # Entry point (runs all 13 pages)
├── aggregate_all.py            # Master aggregation script
├── page_01_executive_summary.py through page_13_ched_compliance.py
└── page_results/               # Output markdown files (generated)
```
Each page script mirrors a dashboard tab and outputs a markdown report. DuckDB is used for efficient filtering/grouping instead of pandas.

### R Dashboards
```
RShiny_Dashboard/NMAT_Shiny/
├── app.R                       # Main Shiny app (2,200 lines, 12 pages)
├── NMAT_Dashboard_v2.Rmd       # R Markdown flexdashboard (static HTML)
└── setup.R                     # R package installer
```

### CHED-Specific Streamlit Variant
```
streamlit_dashboard/CHED_relevant_dashboard/
├── dashboard.py               # CHED-focused dashboard
├── export_markdown.py         # Export to markdown
├── ched_compute/              # Computational modules (01–06)
├── ched_compute/verified_true/ # Verification scripts
└── viz/                       # Static images used in dashboard
```

### Forensic Audit Suite
```
forensic_audit/
├── forensic_audit_v5_final.py # Primary audit (validates PLE matches)
├── audit_per_bin_report.py    # Per-bin breakdown
├── audit_name_check_deep.py   # Name cross-check (APPNO matches)
├── forensic_audit_v*.py       # Prior audit iterations (reference)
└── _check_missing.py          # Missing record detection
```

### Documentation
- `README.md` — Full pipeline overview, architecture, key decisions
- `data_dictionary.md` — Complete 54-column reference with interpretation
- `pipeline_architecture.md` — Detailed pipeline diagrams (Mermaid)
- `changelog.md` — Recent changes and feature additions

---

## Working with Dashboards

### Streamlit Dashboard (Main)
- **Entry:** `streamlit run dashboard.py`
- **12 tabs:** Executive Summary, Data Integrity, Trends & Stability, Score Bins, University Type, Flow & Pathways, PLE Alignment, Repeat Takers, Subtests & Profiles, Year Gap & Gender, Statistical Tests, Policy Tables & Export
- **Filters (sidebar):** Year, University Type, Course Group, Sex, PLE Status
- **Features:** Interactive Plotly charts, hover tooltips, CSV download buttons
- **Performance notes:** Uses `@st.cache_data` for parquet load and expensive aggregations. Cache key includes data version to bust stale data.

### Data Aggregator (Static Markdown)
- **Entry:** `cd data_aggregator && python run_all.py`
- **Output:** 13 markdown files in `page_results/` (one per dashboard page)
- **Tech:** DuckDB + pandas for efficient filtering/grouping, no Streamlit overhead
- **Use case:** Generate static reports for archives or email distribution

### R Shiny (Interactive)
- **Entry:** `cd RShiny_Dashboard/NMAT_Shiny && Rscript -e "shiny::runApp('app.R')"`
- **Parity:** Mirrors all 12 Streamlit tabs exactly
- **Key files:** `app.R` (server + UI logic), `setup.R` (installs arrow, dplyr, plotly, shiny)

---

## Important Notes

### Synchronization Across Dashboards
The Python dashboard.py is the **source of truth**. After updates:
1. Verify changes work in dashboard.py
2. Port changes to `RShiny_Dashboard/NMAT_Shiny/app.R` (mirror logic exactly)
3. Port changes to `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py` (CHED variant)
4. Update `data_aggregator/` page scripts if analysis logic changes

All three consume the same `NMAT_Exodus.parquet`, so schema mismatches must be caught before release.

### Debugging Data Issues
1. **Parquet schema mismatch?** Check `NMAT_Exodus.parquet.bak` for full 118-column version
2. **Missing or stale data in dashboard?** Clear Streamlit cache: `streamlit cache clear` or restart the app
3. **PLE matching suspect?** Run `forensic_audit_v5_final.py` to validate matches against ground truth
4. **Bin distribution off?** Check `IS_BEST_NMAT_RECORD` filtering — duplicates can skew counts

### Performance Optimization
- DuckDB queries in `data_aggregator/helpers.py` are ~2–3× faster than pandas for large groupby operations
- Streamlit caching with `@st.cache_data` reduces re-computation; clear manually if data changes
- Plotly rendering is GPU-accelerated when cuDF is available (attempted in dashboard.py startup)

---

## Common Tasks

### Add a New Analysis to Dashboard
1. Create a new function in `dashboard.py` that reads from `NMAT_Exodus.parquet`
2. Add a new tab using `st.tab()` or navigation in the sidebar
3. Replicate the same logic in `RShiny_Dashboard/NMAT_Shiny/app.R` for parity
4. If static reports needed, add a new page script `data_aggregator/page_XX_*.py`
5. Update `data_aggregator/run_all.py` to include the new page

### Modify Data Pipeline
1. Edit the relevant notebook (`1_*.ipynb` through `3_*.ipynb`) or Python script (`4_*.py`)
2. Test locally: re-run the pipeline, check output schema/counts
3. Verify downstream consumers (dashboards) still work: `streamlit run dashboard.py`
4. Document changes in `changelog.md` and commit with clear message

### Fix a Bug in PLE Matching
1. Run forensic audit: `python forensic_audit/forensic_audit_v5_final.py`
2. Examine false positives/negatives in audit output
3. Edit `2_PLE_Matching_Pipeline.ipynb` → adjust cascade logic or disambiguator thresholds
4. Re-run: `jupyter notebook 2_PLE_Matching_Pipeline.ipynb`
5. Re-run Pipeline 3 (analysis) to propagate fixes downstream
6. Verify dashboard shows corrected PLE rates

### Export Data for External Use
- CSV export via dashboard tab "Policy Tables & Export" (recommended for non-technical users)
- Raw parquet: `pd.read_parquet("dataset/NMAT_Exodus.parquet")` in Python
- R: `arrow::read_parquet("dataset/NMAT_Exodus.parquet")` in R
- Data aggregator markdown: `python data_aggregator/run_all.py` → outputs in `page_results/`

---

## Dependencies & Versions
- Python 3.8+ (3.10+ recommended)
- pandas ≥ 1.5, numpy ≥ 1.24, pyarrow ≥ 10
- scipy ≥ 1.10, scikit-posthocs (for Dunn post-hoc)
- plotly ≥ 5.15, kaleido (for static image export)
- streamlit ≥ 1.25
- duckdb (used in data_aggregator for query optimization)
- R (optional): shiny, shinydashboard, arrow, plotly, dplyr, flexdashboard

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
- Recent commits: Data pipeline updates, forensic audits, dashboard parity fixes
- Untracked: `.temp/`, `.agents/`, `.artifacts/` (build artifacts and agent outputs)

---

*Last updated: 2026-07-31 | NMAT Analysis v1.0 | 54-column Exodus schema*
