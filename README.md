# NMAT Analysis Pipeline

A comprehensive data analysis and reporting pipeline for National Medical Admission Test (NMAT) performance across years, examinee backgrounds, and alignment with Philippine Licensure Examination (PLE) outcomes.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [System Requirements](#system-requirements)
3. [Installation & Setup](#installation--setup)
4. [Data Requirements](#data-requirements)
5. [Pipeline Workflow](#pipeline-workflow)
6. [Running the Analysis](#running-the-analysis)
7. [Dashboard](#dashboard)
8. [Output Structure](#output-structure)
9. [Key Outputs & Interpretations](#key-outputs--interpretations)
10. [Troubleshooting](#troubleshooting)
11. [Data Dictionary](#data-dictionary)

---

## Project Overview

### Objective

This project produces **descriptive and trend-based analysis reports** on NMAT performance, focusing on:

- **NMAT Raw Scores & Standardized Metrics**: Analysis of raw scores, standardized scores, and percentile ranks across exam years (2006–2018+)
- **Distributional Analysis**: Performance using percentile deciles (D1–D10)
- **Performance Stability**: Trends across years and repeat test-takers
- **Background-Based Comparisons**: Analysis by university type (Public/Private/Foreign), course group, and pre-med background
- **PLE Alignment**: Descriptive alignment with Philippine Licensure Examination outcomes using existing match data (no new matching)

### What This Pipeline **Does NOT** Include

- Extension or redesign of NMAT–PLE matching logic (uses existing match classifications only)
- Real-time data collection or scoring
- Advanced causal inference or predictive modeling

---

## System Requirements

### Minimum Hardware

- **CPU**: 4+ cores (8+ recommended)
- **RAM**: 8 GB minimum (16 GB recommended for smooth performance)
- **Disk Space**: 2 GB free space (for datasets + outputs)

### Software

- **Operating System**: Windows, macOS, or Linux
- **Python**: 3.8 or higher (3.10+ recommended)
- **Git**: For version control (optional but recommended)

### Browser (For Dashboard)

- Modern browser supporting Streamlit (Chrome, Firefox, Edge, Safari)

---

## Installation & Setup

### Step 1: Clone or Download the Repository

```bash
# If using git:
git clone <repository-url>
cd NMAT_Analysis

# Or, extract the zip file and navigate to the directory
```

### Step 2: Create a Python Virtual Environment

It is **strongly recommended** to use a virtual environment to isolate dependencies.

#### On Windows (PowerShell):

```powershell
# Create virtual environment
python -m venv .venv

# Activate it
.\.venv\Scripts\Activate.ps1

# If you get execution policy error, run:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
# Then activate again
.\.venv\Scripts\Activate.ps1
```

#### On macOS/Linux (Bash):

```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate
```

### Step 3: Upgrade pip and Install Core Dependencies

```bash
# Upgrade pip
pip install --upgrade pip setuptools wheel

# Install all required packages
pip install -U pandas numpy pyarrow matplotlib seaborn scipy scikit-posthocs plotly kaleido rapidfuzz unidecode tqdm streamlit dspy-ai google-genai python-dateutil
```

#### Package Descriptions

| Package | Purpose |
|---------|---------|
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computing |
| `pyarrow` | Efficient data serialization (Parquet support) |
| `matplotlib` | Static plotting |
| `seaborn` | Statistical visualization |
| `scipy` | Statistical tests (Kruskal-Wallis, Mann-Whitney, Chi-square) |
| `scikit-posthocs` | Post-hoc statistical tests |
| `plotly` | Interactive visualizations & dashboards |
| `kaleido` | Export Plotly figures as static images |
| `rapidfuzz` | Fuzzy string matching (for data cleaning) |
| `unidecode` | Unicode text normalization |
| `tqdm` | Progress bars for long operations |
| `streamlit` | Interactive dashboard framework |
| `dspy-ai` | AI-assisted data cleaning (optional) |
| `google-genai` | Google Generative AI integration (optional) |
| `python-dateutil` | Flexible date parsing |

### Step 4: Verify Installation

```bash
python -c "import pandas, numpy, plotly, streamlit; print('All packages installed successfully!')"
```

---

## Data Requirements

### Required Data Files

Place all data files in the `dataset/` directory. The pipeline expects:

#### Core NMAT Data

- **`NMAT_Ultima.csv`** (Primary analytical dataset)
  - 178,927+ records
  - 115+ columns including raw scores, demographics, institutional background, and PLE match status
  - Covers examination years 2006–2018+

#### Supporting Reference Files

- **`UNIVS.csv`**: University reference table (used in data cleaning/verification)
- **`PLE_DATA.csv`**: Philippine Licensure Examination pass records
- **`CEM_DATA.csv`**: Common Entrance Mechanism data (supplementary)
- **`DsPy_verified.csv`**: AI-verified data points (from DSPy cleaning pipeline)

#### Optional Historical Files (For Reference)

- `NMAT_CLEANED_DATA.csv`: Alternative cleaned version
- `NMAT_FINAL.csv`: Legacy final version
- `PLE_UNMATCHED.csv`: PLE records without NMAT matches

### Data File Locations

```
dataset/
├── NMAT_Ultima.csv              # Primary dataset
├── UNIVS.csv                    # University reference
├── PLE_DATA.csv                 # PLE outcomes
├── CEM_DATA.csv                 # CEM data
├── DsPy_verified.csv            # Verified records
├── analysis_output/             # Generated outputs (created by pipeline)
│   ├── 00_data_validation_*.csv
│   ├── 01A_yearly_summary.csv
│   ├── 02_kruskal_wallis_by_year.csv
│   ├── 03A_decile_by_year_*.csv
│   ├── 04A_uni_type_*.csv
│   ├── 05A_sankey_*.html
│   └── ... (50+ output files)
└── output/                      # Dashboard & supplementary outputs
```

### Data Quality Notes

**Important**: The raw data has known quality issues that the pipeline addresses:

- **Missing Total Raw Scores**: Some records have missing `TotalRawScore` values → pipeline recalculates from component scores
- **Score Mismatches**: In some cases, stored total ≠ sum of components → pipeline flags and documents these
- **Institution Name Variations**: Raw institution names are standardized using fuzzy matching and reference tables
- **Missing Demographics**: Age, birthdate, and gender fields have ~14% missingness → pipeline handles gracefully
- **PLE Matching Status**: Not all NMAT examinees have confirmed PLE outcomes → pipeline categorizes as "Confirmed Passer," "Ambiguous Match," or "No Confirmed Match"

**Instruction**: Do not silently overwrite raw values. All recalculated fields are stored separately and compared against originals in validation reports.

---

## Pipeline Workflow

The analysis consists of **3 sequential notebooks + 1 interactive dashboard**:

### Phase 1: Data Cleaning & Validation (`1_Data_Cleaning_Pipeline.ipynb`)

**Purpose**: Standardize, validate, and prepare raw data for analysis.

**Key Operations**:
- Load NMAT raw data and reference tables
- Standardize institution names (fuzzy matching against `UNIVS.csv`)
- Classify universities as Public/Private/Foreign
- Recalculate total raw scores from component scores
- Validate data integrity (missing values, outliers, inconsistencies)
- Generate validation reports

**Outputs**:
- `00_data_validation_summary.csv`: Overall data quality snapshot
- `00_data_validation_missing.csv`: Column-wise missingness analysis
- `00E_university_type_*.csv`: Institution classification results
- `00E_university_type_location_conflicts.csv`: Conflicts in university classification

**Runtime**: ~5–15 minutes

---

### Phase 2: PLE Matching (`2_PLE_Matching_Pipeline.ipynb`)

**Purpose**: Align NMAT records with PLE outcomes using existing match classifications.

**Key Operations**:
- Load PLE datasets and match records
- Join NMAT and PLE using applicant number / student ID
- Classify match status:
  - **"Confirmed PLE Passer"**: Single matched PLE record with pass status
  - **"Ambiguous Match"**: Multiple PLE matches or unclear status
  - **"No Confirmed PLE Match"**: No match found or unconfirmed
- Generate match summary statistics

**Outputs**:
- `05A_sankey_uni_type_to_decile.html`: Flow diagram (university → NMAT decile)
- `05B_sankey_course_group_to_decile.html`: Flow diagram (course → NMAT decile)
- `05C_sankey_decile_to_ple_status_observable.html`: Flow diagram (NMAT decile → PLE outcome)
- `06A_ple_status_descriptive_observable.csv`: PLE outcome statistics

**Runtime**: ~5–10 minutes

**Note**: This phase does NOT perform new matching; it uses pre-existing classifications.

---

### Phase 3: Statistical Analysis & Reporting (`3_NMAT_PLE_Analysis.ipynb`)

**Purpose**: Generate comprehensive descriptive statistics, trend analyses, and comparisons.

**Key Analyses**:

#### 3.1 Yearly Trends
- Median scores, IQR by year
- Kruskal-Wallis tests for year-to-year differences
- Decile distribution changes over time

#### 3.2 Background Comparisons
- **By University Type** (Public/Private/Foreign):
  - Descriptive statistics
  - Kruskal-Wallis rank tests
  - Decile distribution (count & percentage)
  - Chi-square tests for independence
- **By Course Group** (e.g., Medical & Allied, Natural Sciences, Education):
  - Distribution by decile
  - Median performance
  - Post-hoc tests (if significant)

#### 3.3 PLE Alignment
- NMAT decile vs. PLE pass status
- Mann-Whitney U tests (Confirmed PLE Passers vs. others)
- Flow diagrams (Sankey charts)
- Decile-to-outcome mapping

#### 3.4 Repeat Test-Takers
- Improvement patterns
- Distribution of attempts
- Persistence in top/bottom deciles

**Outputs**: 50+ CSV/HTML files including:
- `01A_yearly_summary.csv`: Year-wise descriptive stats
- `02_kruskal_wallis_by_year.csv`: Statistical test results
- `03A_decile_by_year_count.csv` & `03A_decile_by_year_pct.csv`: Decile trends
- `04A_uni_type_decile_*.csv`: University type comparisons
- `04B_course_decile_*.csv`: Course group comparisons
- `06D_ple_status_decile_pct_observable.csv`: PLE–NMAT alignment
- And more (see [Output Structure](#output-structure))

**Runtime**: ~10–20 minutes

---

### Phase 4: Interactive Dashboard (`dashboard.py`)

**Purpose**: Explore data interactively with dynamic visualizations and filters.

**Features**:
- Filter by year, university type, course group, decile range
- Interactive plots (bar charts, box plots, histograms)
- Sankey diagrams for flow analysis
- Summary statistics and test results
- Export-ready HTML visualizations

**Runtime**: Runs indefinitely until stopped; responds to user interactions in real-time

---

## Running the Analysis

### Quick Start (All Pipelines in One Go)

**Run the master notebook** which orchestrates all phases:

```bash
# In your terminal with virtual environment activated
jupyter notebook 00_RUN_ME.ipynb
```

This master notebook:
1. Installs/updates all dependencies
2. Runs Phase 1 (Data Cleaning)
3. Runs Phase 2 (PLE Matching)
4. Runs Phase 3 (Statistical Analysis)
5. Summarizes all outputs

**Expected total runtime**: 30–50 minutes (first run) | 20–30 minutes (subsequent runs)

---

### Running Individual Pipelines

If you prefer to run phases separately:

#### Phase 1: Data Cleaning

```bash
jupyter notebook 1_Data_Cleaning_Pipeline.ipynb
```

#### Phase 2: PLE Matching

```bash
jupyter notebook 2_PLE_Matching_Pipeline.ipynb
```

#### Phase 3: Statistical Analysis

```bash
jupyter notebook 3_NMAT_PLE_Analysis.ipynb
```

---

### Notebook Execution Tips

1. **Clear Kernel State**: Before re-running, clear all outputs:
   - In Jupyter: `Kernel → Restart & Clear Output`
   - Then run all cells sequentially

2. **Monitor Progress**: Look for:
   - ✅ `Path exists` messages → Data files found
   - ⚠️ `WARNING` messages → Non-critical issues (review before dismissing)
   - ❌ `ERROR` or `AssertionError` → Execution stopped (see [Troubleshooting](#troubleshooting))

3. **Save Outputs**: Each notebook auto-saves CSV/HTML to `dataset/analysis_output/`; ensure this directory has write permissions.

---

## Dashboard

### Launching the Dashboard

Once analysis completes, launch the interactive Streamlit dashboard:

```bash
# Make sure virtual environment is activated
streamlit run dashboard.py
```

**Output**:
```
  You can now view your Streamlit app in your browser.

  URL: http://localhost:8501

  Press Q to quit
```

### Dashboard Features

- **Sidebar Filters**:
  - Year range slider
  - University type multi-select (Public, Private, Foreign, Not Specified)
  - Course group multi-select
  - Decile range slider

- **Visualizations**:
  - Yearly summary (violin plots, KDE)
  - Decile distribution (stacked bar charts)
  - PLE outcome breakdown (bar charts + statistics)
  - Interactive Sankey diagrams
  - Comparisons by background

- **Export**: Right-click on any Plotly chart → `Download plot as PNG`

### Dashboard Troubleshooting

| Issue | Solution |
|-------|----------|
| "ModuleNotFoundError: No module named 'streamlit'" | Reinstall: `pip install streamlit` |
| Port 8501 already in use | Use: `streamlit run dashboard.py --server.port 8502` |
| Dashboard loads but no data | Ensure `NMAT_Ultima.csv` is in `dataset/` and analysis has been run |
| Interactive widgets unresponsive | Refresh browser (F5) and wait 2–3 seconds |

---

## Output Structure

### Directory Layout

```
dataset/analysis_output/
├── Data Validation (Phase 1)
│   ├── 00_data_validation_summary.csv
│   ├── 00_data_validation_missing.csv
│   ├── 00E_university_type_post_cleaning.csv
│   ├── 00E_university_type_location_*.csv
│
├── Yearly Trends (Phase 3)
│   ├── 01A_yearly_summary.csv
│   ├── 01B_subtest_median_by_year.csv
│   ├── 01C_parti_partii_trend.csv
│   ├── 02_iqr_by_year.csv
│   ├── 02_kruskal_wallis_by_year.csv
│
├── Decile Analysis (Phase 3)
│   ├── 03A_decile_by_year_count.csv
│   ├── 03A_decile_by_year_pct.csv
│
├── Background Comparisons (Phase 3)
│   ├── University Type
│   │   ├── 04A_uni_type_decile_count.csv
│   │   ├── 04A_uni_type_decile_pct.csv
│   │   ├── 04A_kw_uni_type_descriptive.csv
│   │   ├── 04D_chi_square_uni_type_vs_decile.csv
│   │
│   ├── Course Group
│   │   ├── 04B_course_decile_count.csv
│   │   ├── 04B_course_decile_pct.csv
│   │   ├── 04B_kw_course_descriptive.csv
│   │
│   └── Institution Type + Location
│       ├── 04A_ext_inst_*.csv
│       ├── 04C_college_*.csv
│
├── Flow & Sankey Diagrams (Phase 2 & 3)
│   ├── 05A_sankey_uni_type_to_decile.html
│   ├── 05B_sankey_course_group_to_decile.html
│   ├── 05C_sankey_decile_to_ple_status_observable.html
│   ├── 05D_*.csv (pathway data)
│   └── 05E_*.csv (composition data)
│
├── PLE Alignment (Phase 2 & 3)
│   ├── 06A_ple_status_descriptive_observable.csv
│   ├── 06C_mannwhitney_ple_status_observable.csv
│   ├── 06D_ple_status_decile_pct_observable.csv
│   ├── 06E_survival_top_decile_by_course.csv
│   ├── 06F_ple_status_by_decile_*.csv
│
├── Repeat Test-Takers (Phase 3)
│   ├── 07_attempt_count_dist.csv
│   ├── 07B_repeat_taker_improvement.csv
│   ├── 07B_repeat_taker_summary.csv
│
└── Subtest Analysis (Phase 3)
    ├── 08_subtest_by_course.csv
    ├── 08_subtest_by_uni_type.csv
    └── ... (additional subtest breakdowns)
```

### File Naming Convention

| Prefix | Meaning |
|--------|---------|
| `00_` | Data validation outputs |
| `01_` | Yearly/temporal trends |
| `02_` | Statistical tests (Kruskal-Wallis, IQR) |
| `03_` | Decile distributions |
| `04_` | Background comparisons (A=Uni Type, B=Course, C=College, D=Chi-square) |
| `05_` | Flow diagrams and pathway analysis |
| `06_` | PLE alignment and outcomes |
| `07_` | Repeat test-taker analysis |
| `08_` | Subtest-level breakdowns |

---

## Key Outputs & Interpretations

### 1. Decile Scores

**Definition**: NMAT performance is categorized into **10 deciles** (D1–D10):
- **D1 (Lowest)**: Lowest 10% of performers
- **D2–D9**: Middle 80%
- **D10 (Highest)**: Top 10% of performers

**Interpretation**: A score in D8 means the examinee outperformed 80% of all test-takers.

### 2. Statistical Tests

**Kruskal-Wallis Test**:
- Tests if NMAT scores differ significantly across groups (e.g., by year or university type)
- **p-value < 0.05** → Statistically significant difference
- Output: `02_kruskal_wallis_by_year.csv`, `04A_kw_*.csv`, `04B_kw_*.csv`

**Mann-Whitney U Test**:
- Compares NMAT scores between PLE passers and non-passers
- Output: `06C_mannwhitney_ple_status_observable.csv`

**Chi-Square Test**:
- Tests association between university type and NMAT decile
- Output: `04D_chi_square_uni_type_vs_decile.csv`

### 3. Sankey Diagrams

**What They Show**: Multi-stage flow (e.g., University Type → NMAT Decile → PLE Status)

**How to Read**:
- **Width of bands** = proportion of examinees in that category
- **Colors** = differentiate groups
- **Hover** = see exact counts and percentages

### 4. Key Metrics

- **Median Score by Year**: Central tendency; robust to outliers
- **IQR (Interquartile Range)**: 50th percentile spread (Q3–Q1); measures variability
- **Repeat Taker Improvement**: Score gain from first to second attempt
- **PLE Pass Rate by Decile**: Percentage of NMAT examinees (by decile) confirmed as PLE passers

---

## Troubleshooting

### Common Issues & Solutions

#### 1. **"FileNotFoundError: dataset/NMAT_Ultima.csv"**

**Cause**: Required data file is missing or in wrong location.

**Solution**:
- Verify `NMAT_Ultima.csv` is in `dataset/` directory
- Check file name exactly (case-sensitive on some systems)
- Ensure file is not corrupted: try opening in Excel/LibreOffice

#### 2. **"No module named 'pandas'" or other ImportError**

**Cause**: Package not installed or wrong virtual environment.

**Solution**:
```bash
# Verify virtual environment is activated (should show (.venv) in prompt)
# If not:
.\.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate     # macOS/Linux

# Reinstall packages:
pip install -U pandas numpy matplotlib seaborn scipy plotly streamlit
```

#### 3. **"MemoryError" during data processing**

**Cause**: Dataset too large for available RAM.

**Solution**:
- Close other applications
- Ensure 8+ GB RAM available
- Check if `NMAT_Ultima.csv` is corrupted (try re-downloading)
- Process in chunks (modify notebooks to filter by year)

#### 4. **Notebooks slow / frozen**

**Cause**: Long-running computations (statistical tests, Sankey generation).

**Solution**:
- Wait 30–60 seconds (especially for Kruskal-Wallis across 1000s of groups)
- Reduce dataset size (filter to specific years)
- Disable unused visualizations (comment out in code)
- Check system resources (CPU, disk usage)

#### 5. **"AssertionError" in data cleaning**

**Cause**: Data structure or values not as expected.

**Solution**:
- Check data validation reports: `00_data_validation_summary.csv`
- Review the error message; it usually specifies what failed
- Ensure `UNIVS.csv` is present (for institution standardization)

#### 6. **Dashboard won't load ("Connection refused")**

**Cause**: Port already in use or Streamlit crashed.

**Solution**:
```bash
# Use different port
streamlit run dashboard.py --server.port 8502

# Or restart from scratch:
# 1. Kill any running Streamlit process
# 2. Reactivate virtual environment
# 3. Re-run streamlit command
```

#### 7. **Deprecation warnings (e.g., about pandas functions)**

**Cause**: Minor library version differences.

**Solution**:
- Warnings are non-critical; analysis continues
- To suppress: run with `export PYTHONWARNINGS=ignore` (Linux/macOS) or `-W ignore` (Windows)
- For production, consider pinning package versions in `requirements.txt`

---

### Debugging Tips

1. **Run one notebook at a time**: Easier to pinpoint which phase fails
2. **Check cell outputs**: Look for warnings in yellow or errors in red
3. **Print intermediate data**: Add `print(df.head())` to inspect shapes/columns
4. **Enable verbose logging**: In notebooks, add `logging.basicConfig(level=logging.DEBUG)`
5. **Validate raw data**: Open `NMAT_Ultima.csv` in Excel → inspect columns and data types
6. **Check disk space**: Ensure 2+ GB free on drive holding `dataset/`

---

## Environment File (Optional)

To make setup reproducible across machines, create a **`requirements.txt`**:

```bash
# Save current environment:
pip freeze > requirements.txt

# Reinstall on another machine:
pip install -r requirements.txt
```

**Pre-made `requirements.txt`** (recommended versions):

```text
pandas==2.0.3
numpy==1.24.3
pyarrow==12.0.1
matplotlib==3.7.2
seaborn==0.12.2
scipy==1.11.2
scikit-posthocs==0.3.8
plotly==5.16.1
kaleido==0.2.1
rapidfuzz==3.1.1
unidecode==1.3.0
tqdm==4.66.1
streamlit==1.28.1
dspy-ai==2.0.0
google-genai==0.3.0
python-dateutil==2.8.2
```

Install with:
```bash
pip install -r requirements.txt
```

---

## Data Dictionary

Refer to [data_dictionary.md](data_dictionary.md) for complete column descriptions, including:

- **Identity & Demographics**: Name, sex, age, birth date, nationality, civil status
- **Education & Institution**: College/university, course group, university type (Public/Private/Foreign), location
- **Scores**: Raw scores (Part I, Part II, Total), standardized scores, percentile, decile
- **Test Metadata**: Test date, year, attempt number
- **PLE Status**: Match classification, outcome, pass status

### Key Scoring Notes

- **Part I**: Aptitude & cognitive skills (Verbal, Reasoning, Quantitative, Perceptual Acuity)
- **Part II**: Science knowledge (Biology, Physics, Chemistry, Social Science)
- **Total Raw Score**: Sum of Part I + Part II raw scores
- **Percentile Decile (PercentileDecile)**: D1–D10 categorization of percentile rank

---

## Quick Reference

### Start-to-Finish Workflow

```
1. Clone/download repository
   ↓
2. Create & activate virtual environment (.venv)
   ↓
3. Install dependencies (pip install -r requirements.txt)
   ↓
4. Verify data files in dataset/ (NMAT_Ultima.csv, UNIVS.csv, etc.)
   ↓
5. Run analysis:
   ├─ jupyter notebook 00_RUN_ME.ipynb  (all-in-one)
   └─ OR run individual notebooks (1_..., 2_..., 3_...)
   ↓
6. Monitor progress (3 notebooks, ~30–50 min total)
   ↓
7. Review outputs in dataset/analysis_output/
   ↓
8. Launch dashboard: streamlit run dashboard.py
   ↓
9. Explore in browser (http://localhost:8501)
```

### File Locations

| Item | Location |
|------|----------|
| Main notebooks | Root directory (`*.ipynb`) |
| Data files | `dataset/` |
| Analysis outputs | `dataset/analysis_output/` |
| Dashboard script | `dashboard.py` |
| Virtual environment | `.venv/` |
| This README | `README.md` |
| Data dictionary | `data_dictionary.md` |
| Instructions | `instructions.md` |

---

## Support & Documentation

- **Detailed Analysis Guide**: See [instructions.md](instructions.md)
- **Column Reference**: See [data_dictionary.md](data_dictionary.md)
- **Analysis Results Summary**: See `*_Results.md` files (e.g., `3_NMAT_PLE_Results.md`)
- **Hypothesis Testing Details**: Review CSV outputs (e.g., `02_kruskal_wallis_by_year.csv`)

---

## Notes for Reproducibility

1. **Seed Random Numbers** (if added): Use `np.random.seed(42)` and `random.seed(42)` for exact reproducibility
2. **Package Versions**: Use `requirements.txt` to pin versions
3. **Data Snapshots**: Datasets are expected to be static; re-runs should produce identical outputs
4. **Documentation**: Keep this README updated if pipeline structure changes

---

## Recent Updates: Deterministic Matching Transition

As outlined in the `DE-FUZZY.md` refactoring plan, the NMAT-PLE matching pipeline has been completely overhauled to transition from fuzzy matching to a strictly deterministic architecture.

- **Fuzzy Logic Eliminated:** All fuzzy matching code, parameters, and outputs have been entirely removed.
- **Exact Matching Implementation:** The matching process now relies exclusively on exact matching utilizing the `NMA_AppNo` identifier sourced from `PLE_STILL_UNMATCHED.csv`.
- **Documentation & Notebook Updates:** `2_PLE_Matching_Results.md` and `3_NMAT_PLE_Analysis.ipynb` have been comprehensively overhauled to reflect this shift.
- **Downstream Integration:** All downstream data lineage and dashboard components (`dashboard.py`) have been fully updated to support this deterministic matching workflow.

---

## License & Attribution

[Add your license information here if applicable]

---

**Last Updated**: April 2026

For questions or issues, refer to the in-notebook comments and error messages. Most issues are resolved by re-checking data files and virtual environment activation.
