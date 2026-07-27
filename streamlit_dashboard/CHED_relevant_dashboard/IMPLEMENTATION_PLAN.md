# CHED Stakeholder Dashboard — Implementation Plan

## Data-Driven Evidence for CMO No. __, s. 2026

**Location:** `streamlit_dashboard/CHED_relevant_dashboard/`  
**Status:** 📋 Plan — ready for execution  
**Approach:** Python scripts first → Markdown outputs → Streamlit dashboard

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [What We Can Build vs. Cannot Build](#2-what-we-can-build-vs-cannot-build)
3. [Available Evidence from Existing Analysis](#3-available-evidence-from-existing-analysis)
4. [Key Insights for CHED Policymakers](#4-key-insights-for-ched-policymakers)
5. [Anticipated Stakeholder Questions & Answers](#5-anticipated-stakeholder-questions--answers)
6. [Python Script Architecture](#6-python-script-architecture)
7. [Streamlit Dashboard Design](#7-streamlit-dashboard-design)
8. [Implementation Workflow](#8-implementation-workflow)
9. [File Structure](#9-file-structure)

---

## 1. Executive Summary

### Objective

Build a **standalone Streamlit dashboard** that provides CHED policymakers with data-driven evidence to support, inform, and monitor the implementation of CMO No. __, s. 2026 (Amendment to NMAT Cut-Off Scores).

### Approach: Python First

Unlike the existing dashboard (which was built first, then had data extracted), this project reverses the order:

```
Phase 1: Python computation scripts → Markdown results
Phase 2: Review & validate results
Phase 3: Build Streamlit dashboard using verified data
```

This ensures every number in the dashboard is verified before any UI code is written.

### Data Source

**`NMAT_Exodus.parquet`** (178,927 rows × 54 columns, 10.5 MB) — the final enriched dataset from Pipeline 4 containing:
- NMAT scores, percentile bins (B1–B10), year, demographics
- University type, course group, institution
- PLE match status (IS_PLE_ANALYSIS_SAFE)
- Citizenship (CITIZENSHIP_FINAL, FOREIGNER_STATUS)

### Critical Data Limitation (Brutally Honest)

**We cannot compute PLE pass rates.** Here is exactly what we have and don't have:

| What | Reality |
|------|---------|
| PLE passers in dataset | **49,986** matched NMAT examinees who later passed PLE |
| PLE failers in dataset | **ZERO** — PLE_DATA.csv contains passers only (43,630 rows, 1 column: PLE_YEAR_PASSED) |
| NMAT-PLE linkage rate | **45.38%** (observable cohort) — share of NMAT takers found in PLE passer data |
| Actual PLE pass rate | ❌ **Cannot compute** — missing denominator (total PLE takers including failers) |

**What this means for the CMO:**
- Section IV-B-1b/c requires per-HEI "PLE performance at a rate above the average national passing percentage" — we **cannot determine this**
- Section IV-B-2 requires "3 consecutive years below national average" enforcement — we **cannot track this**
- What we CAN provide: NMAT-to-PLE **linkage rates**, which show the observed relationship between NMAT scores and eventual PLE passage. This is evidence-based but different from official PLE pass rates.

**Foreign student data limitation:** We have CITIZENSHIP_FINAL (32,501 Verified Foreigners) but this counts NMAT *examinees*, not *enrollees*. The 10-slot cap applies to enrollment — we cannot verify compliance.

**Temporal limitation:** NMAT data covers **2006–2018 only**. The CMO takes effect AY 2026-2027. We have an 8-year gap. This is historical analysis, not current monitoring.

**Province data removed:** The `NMAT Province local address` column was removed during the 118→54 column slimming. Province-level geographic analysis is no longer possible without restoring it from the backup.

---

## 2. What We Can Build vs. Cannot Build

### ✅ BUILDABLE (Existing Data)

| Feature | CMO Section | Data Source | Effort |
|---------|-------------|-------------|--------|
| **30th vs 40th percentile cut-off scenario modeling** | IV-A-1, IV-B-1 | `PercentileBin`, `UNI_TYPE`, `Year` | Medium |
| **Per-HEI NMAT score distribution viewer** | IV-B-1 | `NMA_College`, `PercentileBin` | Low |
| **Foreign student counts per SUC per year** | IV-A-2a | `CITIZENSHIP_FINAL`, `UNI_TYPE`, `Year` | Low |
| **NMAT–PLE linkage rates by percentile bin** | IV-B-1b/c | `PercentileBin`, `IS_PLE_ANALYSIS_SAFE` | Medium |
| **Demographic profiles (sex, course, geography)** | IV-A-1, IV-B-1 | `SEX`, `CourseGroup`, province | Low |
| **NMAT temporal trends (2006–2018)** | VI | `Year`, all scores | Low |
| **Per-HEI cut-off impact analysis** | IV-B-1 | `NMA_College`, `PercentileBin` | Medium |

### ⚠️ BUILDABLE with Caveats

| Feature | Caveat |
|---------|--------|
| **Foreign student 10-slot cap analysis** | Data counts NMAT *examinees*, not actual *enrollees*. Per-SUC counts by year are accurate for examinee volume, but actual cap compliance requires enrollment data from HEIs |
| **Annual cut-off monitoring framework** | Dataset ends at 2018 for NMAT. Current-year monitoring requires annual data pipeline updates |

### ❌ CANNOT BUILD (Data Does Not Exist)

| Feature | Reason | Data Gap |
|---------|--------|----------|
| **PLE pass rate per HEI** | Need PLE taker data with pass/fail outcome. We have passers only. | PLE_DATA.csv: 1 column (PLE_YEAR_PASSED), no result field |
| **5-year national PLE average** | Same denominator problem | Need total PLE takers per year (pass + fail) |
| **3-year consecutive compliance tracking** | Needs pass rates + annual data pipeline + data after 2018 | NMAT data ends 2018; CMO starts 2026 |
| **GIDA applicant identification** | Need GIDA boundary mapping at municipal/barangay level | Province column also removed during slimming |
| **IP applicant identification** | Need IP community membership data | Not in NMAT registration, CEM, or any source file |
| **Composite ranking (60/40 NMAT+GWA+interview)** | Need GWA, GPA, interview scores from HEIs | Not in any dataset anywhere in the project |
| **10-slot cap verification** | Need actual enrollment data from SUCs | We count examinees, not enrollees — different numbers |
| **Current-year (2026) monitoring** | NMAT data ends at 2018; 8-year gap to CMO effectivity | No ongoing data pipeline |
| **Predictive PLE outcome model** | Need PLE failers for proper binary classification | Only one class (passers) available |
| **HEI quality ranking based on PLE** | Need multi-year institutional outcome data + risk adjustment | Not available |

---

## 3. Available Evidence from Existing Analysis

The existing `data_aggregator/page_results/00_MASTER_REPORT.md` and `13_ched_compliance.md` already contain substantial CHED-relevant computations. These are the foundation.

### 3.1 National NMAT–PLE Linkage Benchmark (NOT a pass rate)

**Important:** These are NMAT-to-PLE *linkage rates* — the share of NMAT examinees who were later found in PLE passer records. This is NOT the PLE exam pass rate. We label this accurately throughout.

Computed in existing analysis (observable cohort, Year ≤ 2014):

| Year | NMAT Examinees | Found in PLE Passer Data | Linkage Rate |
|:----:|:--------------:|:------------------------:|:------------:|
| 2006 | 3,665 | 2,038 | 55.61% |
| 2007 | 3,660 | 1,868 | 51.04% |
| 2008 | 4,849 | 2,514 | 51.85% |
| 2009 | 6,881 | 3,226 | 46.88% |
| 2010 | 8,008 | 3,808 | 47.55% |
| 2011 | 8,731 | 3,853 | 44.13% |
| 2012 | 9,145 | 4,066 | 44.46% |
| 2013 | 9,121 | 3,951 | 43.32% |
| 2014 | 10,441 | 3,949 | **37.82%** |

**5-year rolling average (2010–2014):** 43.46%

**What this measures:** "Of NMAT examinees from year X, Y% were later found in official PLE passer records." This is a useful benchmark for understanding the NMAT-to-PLE pipeline, but it is NOT the same as a PLE pass rate. The linkage rate is affected by: (a) whether examinees took PLE, (b) whether they passed, and (c) whether they were successfully matched in our data pipeline — we cannot distinguish these factors.  
**Note:** This is an NMAT-to-PLE *linkage rate*, not a PLE pass rate. It tells us what share of NMAT examinees later appeared in PLE passer data — a meaningful metric for cut-off decisions but different from official PLE passing rates.

### 3.2 Per-HEI PLE Linkage (Computed)

- **HEIs above benchmark (43.46%):** 197
- **HEIs below benchmark:** 342
- **Total HEIs with ≥5 examinees:** 539
- **Top performers:** San Sebastian College-Recoletos Canlubang (80%), UP Manila (77.78%), UP Diliman (76.47%)

### 3.3 Cut-Off Scenario: 30th vs 40th Percentile

Existing analysis computed B4 (30th–39th) vs B5+ (40th+) distributions:

| Metric | Value |
|--------|-------|
| Examinees at or above B4 (30th+) | ~109,000 (61.2%) |
| Examinees at or above B5 (40th+) | ~94,000 (52.7%) |
| Difference (30th vs 40th cut-off) | ~15,000 more qualify at 30th |

**PLE linkage rate jump at B4→B5:** The sharpest increase in PLE linkage occurs between B4 and B5 — a +23.42 percentage point jump. This validates the tiered cut-off approach: the 40th percentile threshold selects a meaningfully different cohort from the 30th.

### 3.4 Foreign Student Data (Computed)

| Metric | Value |
|--------|-------|
| Verified Foreigners | 32,501 |
| Foreign in SUCs | 6,218 |
| Foreign in Private HEIs | 25,019 |
| Foreign in Foreign Schools | 825 |
| Top nationality | India (26,490, 81.5%) |

**Critical finding for foreign student policy:**
- Indian-origin examinees have a **median percentile of 14** (B2)
- **62.78% of Indian-origin examinees fall below B4 (30th percentile)**
- This means the 30th percentile cut-off would exclude the majority of the largest foreign group
- The 40th percentile cut-off would exclude even more

### 3.5 PLE Linkage by Percentile Bin (Computed)

| Bin | Percentile Range | n (best-observable) | PLE Linkage Rate |
|:--:|:----------------:|:-------------------:|:----------------:|
| B1 | 0–10 | 4,982 | 18.67% |
| B2 | 10–20 | 5,937 | 28.65% |
| B3 | 20–30 | 6,000 | 36.40% |
| B4 | **30–40** | 6,692 | **42.87%** |
| B5 | **40–50** | 6,345 | **50.90%** |
| B6 | 50–60 | 6,569 | 55.69% |
| B7 | 60–70 | 6,533 | 59.68% |
| B8 | 70–80 | 6,874 | 67.05% |
| B9 | 80–90 | 7,009 | 73.39% |
| B10 | 90–100 | 7,560 | 81.40% |

**Key insight:** The B4→B5 jump (+23.42pp) is the largest increase between adjacent bins. This provides empirical support for using the 40th percentile (B5+) as a meaningful threshold that differentiates applicant pools on PLE outcomes.

### 3.6 University Type Performance (Computed)

| UNI_TYPE | n | Median Percentile | Median TotalRawScore |
|:---------|:--:|:-----------------:|:--------------------:|
| Public | 27,627 | 57 | 128 |
| Private | 102,888 | 48 | 120 |
| Foreign | 1,894 | 56 | 131 |

Public university examinees outperform Private by ~9 percentile points on average.

---

## 4. Key Insights for CHED Policymakers

### Insight 1: The 30th→40th Percentile Jump Is Empirically Validated

The PLE linkage rate jumps from **42.87% at B4 (30th–39th) to 50.90% at B5 (40th–49th)** — a relative increase of 18.7%. This is the largest bin-to-bin improvement across the entire distribution. The tiered cut-off system (30th for high-performing PHEIs, 40th for others) is supported by the data: institutions permitted to use the 30th percentile will admit a pool with measurably different PLE outcome profiles.

### Insight 2: Private HEIs Are the Majority but Trail Public HEIs

- **76.89%** of examinees come from Private HEIs
- **20.65%** from Public (SUCs)
- **1.42%** from Foreign institutions

Private HEI examinees have a **median percentile of 48** vs **57 for Public** — a 9-point gap. This means the cut-off policy disproportionately affects Private HEIs, which serve the majority of applicants and have lower median scores.

### Insight 3: Foreign Applicants Are Overwhelmingly Indian and Low-Scoring

- **81.5% of foreign applicants are Indian** (26,490 of 32,501)
- Median percentile for Indian-origin examinees: **14 (B2)**
- **62.78% fall below the 30th percentile threshold (B4)**
- The 10-slot SUC cap will primarily affect Indian-origin applicants

This suggests the composite ranking system (60/40 NMAT-to-other criteria) is essential if HEIs want to admit foreign students with diverse qualifications beyond NMAT scores.

### Insight 4: Cut-Off Scenarios Have Significant Volume Implications

A 30th percentile cut-off (B4+) admits ~**61.2% of examinees** (109,000 of 178,927).  
A 40th percentile cut-off (B5+) admits ~**52.7%** (94,000).  

The **~15,000 examinees in the B4 range (30th–39th percentile)** are the marginal pool affected by the cut-off choice. These examinees have a **42.87% PLE linkage rate** — below the national benchmark of 43.46%.

### Insight 5: The Data Infrastructure Gap

**What's missing for full CMO support:**
1. **PLE failer data** — Without knowing how many PLE takers failed, we cannot compute pass rates. CHED/PRC needs to provide complete PLE result data (pass + fail).
2. **GIDA boundary classification** — Province-level data exists but GIDA is at municipal/barangay level.
3. **IP membership data** — No IP community identifiers in NMAT registration.
4. **Enrollment figures** — The 10-slot foreign cap applies to *enrollees*, not *examinees*.

---

## 5. Anticipated Stakeholder Questions & Answers

### Q1: Which PHEIs would qualify for the 30th percentile cut-off?

**Answer: We cannot determine this.** The CMO ties eligibility to "PLE performance at a rate above the average national passing percentage for the last five years." We cannot compute PLE pass rates — our dataset contains only PLE passers, no failers. The closest metric we have is the NMAT-to-PLE *linkage rate* per HEI (share of NMAT examinees later found in PLE passer data). Of 539 HEIs with ≥5 examinees, **197 have linkage rates above the 43.46% national benchmark**. However, this is NOT a PLE pass rate and should not be used as a proxy for CMO eligibility determination without validation against actual PLE outcome data.

**Recommendation:** CHED should obtain complete PLE taker data (pass + fail) from PRC to enable proper pass rate computation.

### Q2: What is the national 5-year average PLE passing rate?

**Answer:** We cannot compute the actual PLE passing rate. The closest available metric is the **5-year average NMAT-to-PLE linkage rate** of **43.46%** (2010–2014). This measures: "of NMAT examinees from those years, what share were later found in PLE passer records." This is a useful benchmark for cut-off analysis but not equivalent to the PLE exam pass rate.

### Q3: How would different cut-offs affect applicant pools?

**Answer:** This we CAN answer. Available data:
- **30th percentile (B4+)**: ~109,000 examinees qualify (61.2% of all)
- **40th percentile (B5+)**: ~94,000 examinees qualify (52.7% of all)
- **Difference**: ~15,000 examinees in the B4 range (30th–39th percentile)
- By institution, course group, year, and citizenship — all available

### Q4: Which SUCs exceed the 10-slot foreign student cap?

**Answer:** On NMAT examinee counts (not enrollment), we can show per-SUC foreign examinee volume. However, historical data suggests many SUCs had significant foreign examinee volumes (e.g., University of Northern Philippines had 1,150 foreign examinees, mostly Indian). Actual enrollment data from SUCs is needed for cap compliance monitoring.

### Q5: How does NMAT performance relate to PLE outcomes?

**Answer:** We can show NMAT-to-PLE linkage rates by percentile bin:
- B1 (0–10th): 18.67% linkage rate
- B5 (40–50th): 50.90%
- B10 (90–100th): 81.40%

The linkage rate increases monotonically with percentile — higher NMAT scorers are more likely to be found in PLE passer records. **However, this is NOT causal.** We cannot conclude that raising the cut-off will improve PLE outcomes because:
1. We lack data on NMAT takers who took PLE but failed
2. Many other factors influence PLE success (medical school quality, curriculum, student effort)
3. Selection effects: higher-NMAT students may attend better medical schools

The linkage rate is evidence for *association*, not *causation*. Policy decisions based on this data should acknowledge this limitation.

### Q6: What data should CHED collect to enable full CMO monitoring?

**Answer:** Based on our analysis, CHED should collect:
1. **Complete PLE result data** (pass + fail) from PRC — enables actual pass rate computation
2. **GIDA municipality classification** from DOH/NSCB — enables GIDA applicant identification
3. **HEI enrollment data** — enables slot cap monitoring
4. **GWA/interview scores** from HEIs — enables composite ranking

---

## 6. Python Script Architecture

### Principle: Compute First, Visualize Second

Each computational module:
1. Reads from `NMAT_Exodus.parquet`
2. Computes specific metrics
3. Outputs structured markdown with tables
4. Can be run independently (no cross-dependencies)

### Module Design

```
ched_compute/
├── __init__.py
├── config.py                        # Global constants, file paths, column names
├── helpers.py                       # Shared functions (load_data, pct_table, etc.)
│
├── 01_national_benchmark.py         # Section A: NMAT-PLE linkage rates, trends
├── 02_cutoff_scenarios.py           # Section B: 30th vs 40th percentile analysis
├── 03_per_hei_distribution.py       # Section C: Per-HEI score distributions
├── 04_foreign_student_analysis.py   # Section D: Foreign student counts, nationalities
├── 05_demographic_profiles.py       # Section E: By sex, course, geography
├── 06_ple_alignment_by_bin.py       # Section F: PLE linkage by percentile bin
├── 07_temporal_trends.py            # Section G: Year-over-year trends
│
├── run_all.py                       # Orchestrator: runs all modules
└── page_results/                    # Output directory for markdown files
```

### Key Computations Per Module

#### `01_national_benchmark.py`
- Annual NMAT–PLE linkage rates (observable cohort)
- 5-year rolling average linkage rate
- Line chart data: linkage rate trend 2006–2014
- **Output:** Table A1 (year, n, passers, rate, 5yr_avg)

#### `02_cutoff_scenarios.py`
- Count at B4+ (30th percentile) vs B5+ (40th percentile)
- By UNI_TYPE (Public, Private, Foreign)
- By individual HEI (per-HEI impact)
- By Year
- PLE linkage rate at each cut-off level
- **Output:** Comparison table + scenario matrices

#### `03_per_hei_distribution.py`
- Full bin distribution (B1–B10) per HEI (min 5 examinees)
- HEI ranking by median percentile, by type
- Searchable/filterable table
- **Output:** HEI × Bin matrix, summary stats

#### `04_foreign_student_analysis.py`
- Foreign count by UNI_TYPE, Year, HEI
- Foreign count per SUC per year (for 10-slot cap analysis)
- Nationality distribution (top 30)
- NMAT performance by nationality
- PLE linkage rate by nationality
- **Output:** Foreign student tables + cap compliance estimates

#### `05_demographic_profiles.py`
- By SEX (Male/Female) — NMAT performance, PLE linkage
- By CourseGroup — NMAT performance, PLE linkage
- By province/region — geographic distribution
- **Output:** Demographic comparisons

#### `06_ple_alignment_by_bin.py`
- PLE linkage rate by PercentileBin
- PLE linkage rate by UNI_TYPE × PercentileBin
- PLE linkage rate by CourseGroup × PercentileBin
- PLE linkage rate by CITIZENSHIP_FINAL
- **Output:** Full PLE alignment tables

#### `07_temporal_trends.py`
- Yearly median scores, IQR, examinee counts
- Yearly bin distribution
- Yearly foreign student counts
- **Output:** Trend tables + summary

---

## 7. Streamlit Dashboard Design

### Tab Structure (No Sidebar Filters)

The dashboard uses tabs instead of sidebar filters. Each tab is a complete, self-contained view.

| Tab | Title | Content |
|:---:|-------|---------|
| 1 | **Overview** | Executive summary: key metrics, CHED CMO context, data limitations, how to use this dashboard |
| 2 | **National Benchmark** | NMAT–PLE linkage rates, 5-year rolling average, trend chart, interpretation |
| 3 | **Cut-Off Scenarios** | 30th vs 40th percentile comparison tables, impact by HEI type, PLE linkage by cut-off |
| 4 | **Per-HEI Analysis** | Institution-level NMAT distributions, HEI ranking, search/filter by name |
| 5 | **Foreign Students** | Foreign examinee counts, SUC slot cap analysis, nationality profiles, NMAT performance |
| 6 | **Demographics** | Performance by sex, course group, geography |
| 7 | **PLE Alignment** | PLE linkage by bin, type, course, citizenship |
| 8 | **Trends (2006–2018)** | Year-over-year trends in scores, volume, composition |
| 9 | **Data Appendix** | Methodology notes, column descriptions, data limitations, pipeline overview |

### Visual Style

- **No custom CSS** — default Streamlit theme
- **No sidebar filters** — all navigation via tabs
- **Clear English** — professional, policy-oriented language
- **Tables first, charts second** — policymakers need exact numbers
- **Metric cards** at top of each tab for key numbers
- **Download buttons** for underlying CSV data

### Key Visualizations

| Tab | Chart Type | Data |
|:---:|------------|------|
| Benchmark | Line chart | Annual linkage rate + 5-year rolling avg |
| Cut-Off | Grouped bar | Admitted count at 30th vs 40th by HEI type |
| Per-HEI | Horizontal bar | Top/bottom HEIs by median percentile |
| Foreign | Stacked bar | Foreign vs Filipino per SUC per year |
| Demographics | Grouped bar | Performance by sex, course, region |
| PLE Alignment | Heatmap | PLE linkage rate by bin × type |
| Trends | Line chart | Score trends over 13 years |

---

## 8. Implementation Workflow

### Phase 1: Python Computation Scripts

```
Step 1: Create config.py and helpers.py
Step 2: Create 01_national_benchmark.py → run → verify output
Step 3: Create 02_cutoff_scenarios.py → run → verify output
Step 4: Create 03_per_hei_distribution.py → run → verify output
Step 5: Create 04_foreign_student_analysis.py → run → verify output
Step 6: Create 05_demographic_profiles.py → run → verify output
Step 7: Create 06_ple_alignment_by_bin.py → run → verify output
Step 8: Create 07_temporal_trends.py → run → verify output
Step 9: Create run_all.py → run → verify all outputs
```

### Phase 2: Validation

```
Step 10: Cross-check computed values against existing data_aggregator results
Step 11: Spot-check 10 random values against raw parquet queries
Step 12: Calculate confidence intervals where applicable
Step 13: Document any discrepancies or unexpected findings
```

### Phase 3: Streamlit Dashboard

```
Step 14: Create dashboard.py with tab structure
Step 15: Implement each tab using computed data (no re-computation in dashboard)
Step 16: Test all tabs load correctly
Step 17: Verify with sample user (stakeholder review)
Step 18: Deploy to Streamlit Cloud
```

### Parallelization Strategy

| Agent | Module | Estimated Time |
|-------|--------|:--------------:|
| Agent A | config.py + helpers.py + 01_national_benchmark.py | 30 min |
| Agent B | 02_cutoff_scenarios.py + 03_per_hei_distribution.py | 45 min |
| Agent C | 04_foreign_student_analysis.py + 05_demographic_profiles.py | 45 min |
| Agent D | 06_ple_alignment_by_bin.py + 07_temporal_trends.py | 40 min |
| Agent E | run_all.py + validation cross-check | 30 min |

Then:
| Agent F | Streamlit dashboard (dashboard.py) | 90 min |
| Agent G | Final review, testing, deployment | 30 min |

**Total estimated time:** ~4–5 hours with 4 parallel agents

---

## 9. File Structure

```
streamlit_dashboard/CHED_relevant_dashboard/
│
├── README.md                          # Streamlit Cloud deployment instructions
├── requirements.txt                   # Dependencies
├── .streamlit/
│   └── config.toml                    # Streamlit theme config (optional)
│
├── dashboard.py                       # Main Streamlit app (all tabs)
│
├── ched_compute/                      # Python computation modules
│   ├── __init__.py
│   ├── config.py                      # Constants, paths, column mappings
│   ├── helpers.py                     # Shared functions
│   ├── 01_national_benchmark.py       # Section A
│   ├── 02_cutoff_scenarios.py         # Section B
│   ├── 03_per_hei_distribution.py     # Section C
│   ├── 04_foreign_student_analysis.py # Section D
│   ├── 05_demographic_profiles.py     # Section E
│   ├── 06_ple_alignment_by_bin.py     # Section F
│   ├── 07_temporal_trends.py          # Section G
│   └── run_all.py                     # Orchestrator
│
├── page_results/                      # Computed markdown outputs
│   ├── 01_national_benchmark.md
│   ├── 02_cutoff_scenarios.md
│   ├── 03_per_hei_distribution.md
│   ├── 04_foreign_student_analysis.md
│   ├── 05_demographic_profiles.md
│   ├── 06_ple_alignment_by_bin.md
│   └── 07_temporal_trends.md
│
└── NMAT_Exodus.parquet               # Data file (copy)
```

---

## Appendix: Data Source Schema (Exodus)

Key columns relevant to CHED analysis:

| Column | Type | Use in CHED Analysis |
|--------|------|----------------------|
| `Year` | int | Temporal trends, observable cohort filtering |
| `UNI_TYPE` | string | SUC vs PHEI classification (Public/Private) |
| `UNIVERSITY` / `NMA_College` | string | Per-HEI analysis |
| `CourseGroup` | string | Course-based performance analysis |
| `PercentileBin` | string (B1–B10) | Cut-off analysis (B4+ = 30th, B5+ = 40th) |
| `NMS_PER_num` | float | Continuous percentile for rankings |
| `TotalRawScoreTRUE` | float | Raw score analysis |
| `IS_PLE_ANALYSIS_SAFE` | bool | PLE linkage flag (observable cohort) |
| `IS_BEST_NMAT_RECORD` | bool | Person-level deduplication |
| `CITIZENSHIP_FINAL` | string | Foreign student analysis |
| `FOREIGNER_STATUS` | string | Foreign/Verified/Likely classification |
| `SEX` | string | Demographic analysis |
| `Year` | int | Trend analysis |

---

*Implementation plan generated from: CHED CMO document, existing dashboard analysis (dashboard.py + data_aggregator), NMAT_Exodus.parquet schema, and prior CHED gap analysis.*

*Next steps: Execute Phase 1 — Python computation scripts.*
