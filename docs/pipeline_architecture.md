# NMAT Analysis — Pipeline Architecture

## End-to-End Data Transformation Documentation

**Last updated:** 2026-07-27  
**Final output:** `dataset/NMAT_Exodus.parquet` (54 columns, 10.5 MB)  
**Total examinees:** 178,927 rows covering NMAT 2006–2018

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [Pipeline 1: Data Cleaning & Score Recalibration](#2-pipeline-1-data-cleaning--score-recalibration)
3. [Pipeline 2: PLE Matching](#3-pipeline-2-ple-matching)
4. [Pipeline 3: Statistical Analysis](#4-pipeline-3-statistical-analysis)
5. [Pipeline 4: Citizenship Integration](#5-pipeline-4-citizenship-integration)
6. [Final Dataset: NMAT_Exodus.parquet](#6-final-dataset-nmat_exodusparquet)
7. [Key Decisions & Issues Faced](#7-key-decisions--issues-faced)

---

## 1. System Overview

```mermaid
flowchart TB
    subgraph INPUTS["Raw Data Sources"]
        A1["NMAT_CLEANED_DATA.csv<br/>178,927 rows x 29 cols"]
        A2["CEM_DATA.csv<br/>254,308 rows x 36 cols"]
        A3["UNIVS.csv<br/>3,022 rows x 8 cols"]
        A4["PLE_DATA.csv<br/>43,630 rows"]
        A5["REAL_FOREIGNERS.csv<br/>32,501 rows x 29 cols"]
        A6["pseudo_citizenship_profiling_FINAL.csv<br/>871 rows x 13 cols"]
    end

    subgraph P1["Pipeline 1: Data Cleaning"]
        direction TB
        B1["Clean & Standardize<br/>Application Numbers"]
        B2["University Name<br/>Normalization via UNIVS"]
        B3["TRUE Raw Score<br/>Recalculation<br/>(8 component subtests)"]
        B4["PercentileDecile<br/>Binning (D1-D10)"]
        B5["Course Group<br/>Classification"]
        B1 --> B2 --> B3 --> B4 --> B5
    end

    subgraph P2["Pipeline 2: PLE Matching"]
        direction TB
        C1["Stage 0: Manual AppNo Recovery<br/>from PLE_UNMATCHED.csv"]
        C2["Stage 1: Exact Name Match<br/>via NAME_NORM dictionary"]
        C3["Stage 2: Deterministic AppNo<br/>from PLE_STILL_UNMATCHED.csv"]
        C4["Disambiguator:<br/>Year gap + DOB + Latest Year<br/>+ Percentile Floor + Tiebreak"]
        C1 --> C4
        C2 --> C4
        C3 --> C4
    end

    subgraph P3["Pipeline 3: Statistical Analysis"]
        D1["Yearly Trends &<br/>Stability (Kruskal-Wallis)"]
        D2["Demographic Comparisons<br/>(Uni Type, Course, Gender)"]
        D3["PLE Alignment Analysis<br/>(Mann-Whitney U)"]
        D4["Repeat Taker Patterns"]
        D5["Subtest Profiles"]
        D6["50+ CSV/PNG outputs<br/>in analysis_output/"]
        D1 --> D6
        D2 --> D6
        D3 --> D6
        D4 --> D6
        D5 --> D6
    end

    subgraph P4["Pipeline 4: Citizenship Integration"]
        direction TB
        E1["Tier 1: REAL_FOREIGNERS.csv<br/>32,501 ground-truth records"]
        E2["Tier 2: Pseudo-Citizenship<br/>317 FOREIGN override records"]
        E3["Tier 3: Default Filipino<br/>146,413 remaining records"]
        E1 --> E4["3-Tier Hierarchy<br/>Resolution"]
        E2 --> E4
        E3 --> E4
    end

    subgraph OUTPUT["Final Outputs"]
        F1["NMAT_Exodus.parquet<br/>178,927 rows x 54 cols<br/>10.5 MB"]
        F2["NMAT_Exodus.parquet.bak<br/>Full 118-col backup<br/>27.9 MB"]
        F3["dashboard.py / app.R<br/>Streamlit + R Shiny<br/>Consume Exodus directly"]
    end

    A1 & A2 & A3 --> P1
    P1 --> B6["NMAT_FINAL.parquet<br/>178,927 x 101 cols"]
    B6 & A4 --> P2
    P2 --> C5["NMAT_Ultima.parquet<br/>178,927 x 115 cols"]
    C5 --> P3
    C5 & A5 & A6 --> P4
    P4 --> F1
    F1 --> F3
    F1 -.->|Backup| F2
```

**Total columns over time:**
| Stage | File | Columns | Size |
|-------|------|--------:|-----:|
| Raw NMAT input | NMAT_CLEANED_DATA.csv | 29 | ~50 MB |
| After Pipeline 1 | NMAT_FINAL.parquet | 101 | ~25 MB |
| After Pipeline 2 | NMAT_Ultima.parquet | 115 | ~28 MB |
| After Pipeline 4 | NMAT_Exodus.parquet | **54** | **10.5 MB** |

---

## 2. Pipeline 1: Data Cleaning & Score Recalibration

**File:** `1_Data_Cleaning_Pipeline.ipynb`  
**Status:** ✅ Working

### Inputs

| File | Rows | Description |
|------|-----:|-------------|
| `NMAT_CLEANED_DATA.csv` | 178,927 | Raw NMAT registration & score data |
| `CEM_DATA.csv` | 254,308 | Component-level score records from CEM (testing center) |
| `UNIVS.csv` | 3,022 | University reference table (canonical names, types, locations) |

```mermaid
flowchart LR
    subgraph I1["Inputs"]
        N["NMAT_CLEANED_DATA.csv"]
        C["CEM_DATA.csv"]
        U["UNIVS.csv"]
    end

    subgraph T1["Key Transformations"]
        A["Clean & Standardize<br/>Application Numbers<br/>- Digits-only join keys<br/>- Column name normalization"]
        B["University Name<br/>Normalization<br/>- 4-tier matching cascade<br/>- 2,981 verified (68.3%)<br/>- 1,386 unmatched (31.7%)"]
        C1["TRUE Raw Score<br/>Recalculation<br/>- Sum of 8 component scores<br/>- Stored totals wrong in 42.2%"]
        D["PercentileDecile<br/>Binning<br/>- pd.cut(NMS_PER, 0-100)<br/>- D1=0-10 through D10=90-100"]
        E["Course Group<br/>Classification<br/>- Keyword matching on course name<br/>- 6 groups including Medical & Allied"]
    end

    I1 --> A --> B --> C1 --> D --> E
    E --> O["NMAT_FINAL.parquet<br/>178,927 x 101 cols"]
```

### The Score Corruption Problem (42.2% mismatch)

The CEM data contained two raw score totals:
- **`STU_RSCORE`** (Stored Total): Wrong in **107,422 of 254,308 rows (42.2%)**
- **`STU_RSCORE_CALC`** (Calculated Total): **Always correct** (0 mismatches)

**Root cause:** The stored totals appear to come from a legacy computation or data entry error. The individual component scores (CA01–CA08) are reliable, so the pipeline recomputes `TotalRawScoreTRUE` by summing the 8 components anew. Both the wrong stored total and the TRUE derived total are preserved in the output for downstream auditing.

### University Normalization (4-Tier Matching Cascade)

UNIVS.csv is the **sole source of truth** for university classification — no APIs, no web search.

| Tier | Method | Matched | Cumulative |
|:----:|--------|--------:|:----------:|
| 1 | Exact primary key match (`NMA_College_norm`) | 2,674 | 61.2% |
| 2 | Exact secondary key match (`COLLEGE_UNIV_norm`) | 72 | 62.9% |
| 3 | Fuzzy match (rapidfuzz, score >= 88, gap >= 5) | 235 | 68.3% |
| 4 | Unmatched → retains original, "Not Specified" | 1,386 | 100.0% |

### Output

| File | Rows | Cols | Notes |
|------|-----:|-----:|-------|
| `NMAT_FINAL.csv` | 178,927 | 101 | Full merged dataset (CSV) |
| `output/NMAT_FINAL.parquet` | 178,927 | 101 | Parquet equivalent |
| `DsPy_verified.csv` | 4,367 | 20 | University verification dimension |
| `output/00_source_counts.csv` through `14_qa_*.csv` | ~15 files | — | Audit trail |

**Key new columns created:**
- `TotalRawScoreTRUE`, `PartIRawScoreTRUE`, `PartIIRawScoreTRUE`
- `PercentileDecile` (D1–D10)
- `CourseGroup` (6 categories)
- `UNIVERSITY`, `UNI_TYPE`, `UNI_LOCATION` (from UNIVS)
- `StoredVsDerivedMismatch`, `CalcVsDerivedMismatch`

---

## 3. Pipeline 2: PLE Matching

**File:** `2_PLE_Matching_Pipeline.ipynb`  
**Status:** ✅ Working (after DE-FUZZY refactor)

### Inputs

| File | Rows | Description |
|------|-----:|-------------|
| `NMAT_FINAL.csv` | 178,927 | Cleaned NMAT data from Pipeline 1 |
| `PLE_DATA.csv` | 43,630 | PLE passer records (2011–2022) |
| `PLE_UNMATCHED.csv` | 6,600 | PLE records without NMAT match |
| `PLE_STILL_UNMATCHED.csv` | 7,207 | Second-round residual unmatched |

### The DE-FUZZY Refactor

**Why fuzzy matching was removed:**

1. **False positives at common names.** Filipino surnames concentrate in narrow lexical bands; "DELA CRUZ, JUAN" could match dozens of candidates.
2. **Auditability.** Fuzzy outcomes were not reproducible across `rapidfuzz` versions and could not be traced to a source document.

**What changed:**
- `rapidfuzz` dependency removed entirely
- 3 fuzzy-matching cells deleted, replaced with deterministic AppNo matching
- Binary statuses only: `"Confirmed PLE passer"` / `"No confirmed PLE match"`
- `AMBIGUOUS` category abolished

```mermaid
flowchart TB
    subgraph PLE_MATCH["3-Stage Deterministic Matching"]
        direction TB
        S0["Stage 0: Manual AppNo Recovery<br/>from PLE_UNMATCHED.csv<br/>2,331 FINAL_MATCH"]
        S1["Stage 1: Exact Name Match<br/>via NAME_NORM dictionary<br/>33,970 FINAL_MATCH"]
        S2["Stage 2: Deterministic AppNo<br/>from PLE_STILL_UNMATCHED.csv<br/>321 FINAL_MATCH"]
        
        subgraph DISAMBIG["5-Step Disambiguator<br/>(when multiple candidates)"]
            DS1["1. Year-gap filter:<br/>PLE_YEAR - NMAT_YEAR >= 5"]
            DS2["2. Identity filter:<br/>DOB + Sex match"]
            DS3["3. Latest NMAT year:<br/>keep most recent"]
            DS4["4. Percentile floor:<br/>NMS_PER_num >= 40"]
            DS5["5. Tiebreak:<br/>highest percentile wins<br/>(gap >= 5 pts = FINAL_MATCH)"]
            DS1 --> DS2 --> DS3 --> DS4 --> DS5
        end
        
        S0 --> MASTER["Master Combine<br/>& Deduplication"]
        S1 --> MASTER
        S2 --> MASTER
        S1 -.->|Multiple candidates| DISAMBIG
        DISAMBIG --> MASTER
    end

    MASTER --> O1["PLE_MATCH_MASTER.csv<br/>43,601 match records"]
    MASTER --> O2["NMAT_Ultima.parquet<br/>178,927 x 115 cols"]
    MASTER --> O3["PLE_PASSERS_IN_NMAT.csv<br/>36,305 best-record passers"]
    MASTER --> O4["PLE_STILL_UNMATCHED_v2.csv<br/>6,433 residuals"]
```

### Match Results

| Status | Count | % of PLE records |
|--------|------:|:----------------:|
| **FINAL_MATCH** (accepted) | **36,395** | **83.4%** |
| AMBIGUOUS (manual review) | 772 | 1.8% |
| NO_VALID_MATCH (failed checks) | 2,298 | 5.3% |
| UNMATCHED_NO_APPNO | 4,135 | 9.5% |

### Observable Cohort

The **observable cohort** (`Year <= 2014`) ensures that PLE linkage analyses are fair:
- NMAT 2006 → 16-year window to observe PLE outcome
- NMAT 2014 → 8-year window (most have taken boards)
- NMAT 2015+ → insufficient observation window → right-censoring bias

**Cohort sizes:** 64,501 best-observable rows, 29,269 confirmed PLE passers.

---

## 4. Pipeline 3: Statistical Analysis

**File:** `3_NMAT_PLE_Analysis.ipynb`  
**Status:** ✅ Working

### Input

| File | Description |
|------|-------------|
| `NMAT_Ultima.parquet` | 178,927 rows × 115 columns |

### Key Statistical Tests

```mermaid
flowchart LR
    subgraph ANALYSES["13 Analysis Sections"]
        T1["Yearly Trends<br/>& Stability"]
        T2["Bin Distributions<br/>by Year & Background"]
        T3["University Type<br/>& Location Analysis"]
        T4["CourseGroup<br/>& College Analysis"]
        T5["Sankey Flow<br/>Pathways"]
        T6["PLE Status<br/>Performance Profile"]
        T7["Repeat Taker<br/>Trajectories"]
        T8["Subtest Profiles<br/>& Radar Charts"]
        T9["Gender Analysis"]
    end

    subgraph STATS["Statistical Tests Used"]
        S1["Kruskal-Wallis H-test<br/>+ eta-squared effect size<br/>6 applications"]
        S2["Mann-Whitney U<br/>+ effect size r<br/>2 applications"]
        S3["Chi-square test<br/>+ Cramer's V<br/>2 applications"]
        S4["Dunn post-hoc<br/>Bonferroni-adjusted<br/>3 applications"]
    end

    ANALYSES --> STATS
    STATS --> OUT["95 output files<br/>59 CSV + 36 PNG<br/>in analysis_output/"]
```

### Best-Record Filtering

`IS_BEST_NMAT_RECORD` selects exactly one row per person (identified by `PERSON_KEY`):
- For non-PLE persons: highest percentile, latest year
- For PLE passers: the **specific NMAT attempt that matched** to the PLE record

**Why:** 25.0% of examinees took NMAT 2+ times (max 9 attempts). Without deduplication, repeat takers violate independence assumptions of statistical tests.

### Output

| Metric | Count |
|--------|------:|
| CSV files | 59 |
| PNG charts | 36 |
| Total outputs | 95 |

All saved to `dataset/analysis_output/`.

---

## 5. Pipeline 4: Citizenship Integration

**File:** `4_Citizenship_Integration.py` (rewritten as `.py`, replaced original `.ipynb`)  
**Status:** ✅ Working (after rewrite fixing REAL_FOREIGNERS.csv omission)

### Inputs

| File | Rows | Description |
|------|-----:|-------------|
| `NMAT_Ultima.parquet` | 178,927 | Base dataset from Pipeline 2 |
| `REAL_FOREIGNERS.csv` | 32,501 | Ground-truth citizenship records |
| `pseudo_citizenship_profiling_FINAL.csv` | 871 | Name-based citizenship inference |

### The Problem with the Original Implementation

The original `4_Citizenship_Integration.ipynb` had a critical bug: it **never loaded `REAL_FOREIGNERS.csv`**. Despite the `CITIZENSHIP_REINTEGRATION_PLAN.md` explicitly specifying a 3-tier hierarchy with REAL_FOREIGNERS as Priority 1 ground truth, the code only used:
1. `NAC_NATIONALITY` from the main parquet (already present for all rows)
2. `pseudo_citizenship_profiling_FINAL.csv` (871 rows)

This meant ~32,500 verified foreign records were **completely ignored**.

### The 3-Tier Hierarchy (Fixed Implementation)

```mermaid
flowchart TB
    START["NMAT Examinee<br/>(APPNO_CLEAN)"] --> TIER1
    
    subgraph TIER1["Tier 1: REAL_FOREIGNERS.csv (Ground Truth)"]
        direction TB
        RF["32,501 records<br/>with explicit NAC_NATIONALITY"]
        RF_CHECK{"Found in RF?"}
        RF --> RF_CHECK
        RF_CHECK -->|"YES + known nationality"| RF1a["CITIZENSHIP_FINAL = normalized nationality<br/>FOREIGNER_STATUS = 'Verified Foreigner'"]
        RF_CHECK -->|"YES + ambiguous nationality<br/>(Others/Not Stated)"| RF1b["CITIZENSHIP_FINAL = School Type_rec2_FINAL<br/>FOREIGNER_STATUS = 'Verified Foreigner'"]
    end

    TIER1 -->|"32,501 matched"| VERIFIED["32,501 Verified Foreigners"]
    TIER1 -->|"146,426 unmatched"| TIER2

    subgraph TIER2["Tier 2: Pseudo-Citizenship (Inferred)"]
        PC["871 profiling records<br/>317 FOREIGN overrides"]
        PC_CHECK{"override_applied == FOREIGN<br/>AND not in Tier 1?"}
        PC --> PC_CHECK
        PC_CHECK -->|"YES"| PC2["CITIZENSHIP_FINAL = pseudo_citizenship<br/>FOREIGNER_STATUS = 'Likely Foreigner'"]
    end

    TIER2 -->|"13 matched"| LIKELY["13 Likely Foreigners"]
    TIER2 -->|"146,413 unmatched"| TIER3

    subgraph TIER3["Tier 3: Default"]
        DEF["CITIZENSHIP_FINAL = 'Filipino'<br/>FOREIGNER_STATUS = 'Filipino'"]
    end

    TIER3 --> FILIPINO["146,413 Filipinos"]

    VERIFIED & LIKELY & FILIPINO --> EXODUS["NMAT_Exodus.parquet<br/>178,927 x 118 cols<br/>(later reduced to 54)"]
```

### Nationality Normalization

REAL_FOREIGNERS.csv contained **129 unique nationality values** (e.g., "India" vs "Indian", "Nepal" vs "Nepali"). A normalization map was created to canonicalize these to ~96 country names.

**Example normalizations:**
| Raw | Canonical |
|-----|-----------|
| India, Indian | India |
| Thailand, Thai | Thailand |
| United States, American | United States |
| Korea, Korean, R.O.C. | Korea (South) |
| Vietnemese (typo) | Vietnam |
| Camerdon (typo) | Cameroon |

### Multicultural Verification

Before building Pipeline 4, a **6-dimension cross-validation** was performed to confirm the join is safe:

| Dimension | Match Rate | Verdict |
|-----------|:----------:|:--------|
| AppNo key overlap | **100.0%** | ✅ |
| Name match | **100.0%** | ✅ |
| Year match | **100.0%** | ✅ |
| Percentile score | **100.0%** | ✅ |
| Nationality | **99.94%** | ✅ |
| College (format diff) | 89.4% | ✅ (format, not identity) |

### Output

| Column | Values | Description |
|--------|--------|-------------|
| `CITIZENSHIP_FINAL` | 108 unique | Final nationality label |
| `FOREIGNER_STATUS` | 3 values | "Verified Foreigner" (32,501) / "Likely Foreigner" (13) / "Filipino" (146,413) |
| `name_based_assessment` | String | Only populated for 871 pseudo-citizenship records |

---

## 6. Final Dataset: NMAT_Exodus.parquet

After all 4 pipelines, the original 118-column `NMAT_Ultima.parquet` was slimmed down to 54 columns by removing columns unused by both `dashboard.py` and `data_aggregator/`.

```mermaid
flowchart LR
    subgraph SHRINK["Column Reduction Audit"]
        A["NMAT_Ultima.parquet<br/>118 columns<br/>27.9 MB"]
        A --> B["dashboard.py audit:<br/>56 columns used<br/>62 columns unused"]
        A --> C["data_aggregator audit:<br/>43 columns used<br/>75 columns unused"]
        B & C --> D["Combined keep set:<br/>54 unique columns"]
        D --> E["NMAT_Exodus_Lite.parquet<br/>54 columns<br/>10.5 MB"]
        E --> F["Renamed to<br/>NMAT_Exodus.parquet<br/>(original deleted)"]
        F --> G["NMAT_Exodus.parquet.bak<br/>Full 118-col backup<br/>27.9 MB"]
    end
```

### 64 Columns Removed (Not Used by Any Consumer)

| Category | Columns Removed |
|----------|----------------|
| **CEM standard scores** | `Std_Verbal_CEM` through `Std_Chemistry_CEM` (8 cols) |
| **Verification pipeline** | `draft_university`, `draft_uni_type`, `draft_uni_location`, `draft_hint_method`, `draft_hint_score`, `verification_method`, `verification_status`, `confidence`, `evidence_summary`, `final_value_source`, `merge_verified_university`, `merge_cem` (12 cols) |
| **Medical school choices** | `MED_SCHOOL_CHOICE1`, `MED_SCHOOL_CHOICE2`, `MED_SCHOOL_CHOICE3` (3 cols) |
| **Personal info** | `NMA_Name`, `NMA_Sex`, `NMA_BirthDate`, `BDATE`, `AGE`, `CIVIL_STATUS`, `NAC_NATIONALITY`, `BDATE_CLEAN` (8 cols) |
| **Raw application fields** | `NMA_AppNo`, `NMA_AppNo_clean`, `NMA_TestDate`, `NMA_Graduating`, `NMA_YearGrad`, `NMA_Course`, `Course Classification`, `Course_recode` (8 cols) |
| **College raw fields** | `NMA_College_RAW`, `COLLEGE_NAME`, `COURSE_DESC`, `School Type_rec2_FINAL`, `NMC_Center`, `STU_TESTDATE`, `NMAT_YEAR`, `KEY` (8 cols) |
| **Location raw** | `NMAT Province local address`, `NMAT Region permanent address` (2 cols) |
| **Verification fields** | `UNIVERSITY_VERIFIED`, `UNI_TYPE_VERIFIED`, `UNI_LOCATION_VERIFIED` (3 cols) |
| **Raw score fields** | `NMS_PER`, `STU_RSCORE`, `STU_RSCORE_CALC`, `STU_RSCORE_VALID`, `STU_NO_clean`, `NAME_NORM`, `SOURCE_NMAT`, `raw_component_count` (8 cols) |
| **PLE extended** | `PLE_MATCH_STATUS`, `PLE_MATCH_REASON` (2 cols) |

### Verification After Slimming

- ✅ Row count preserved: 178,927
- ✅ All `REQUIRED_PIPELINE_COLS` present
- ✅ 0 nulls in `CITIZENSHIP_FINAL` and `FOREIGNER_STATUS`
- ✅ All 38 columns needed by `data_aggregator/` present
- ✅ `dashboard.py` syntax: PASSED
- ✅ Size reduction: **27.9 MB → 10.5 MB (62.4% smaller)**

---

## 7. Key Decisions & Issues Faced

### Decision 1: Deterministic Over Fuzzy Matching
**Problem:** Fuzzy name matching produced false positives and was not auditable.  
**Solution:** Eliminated all `rapidfuzz` matching from Pipeline 2. Replaced with 3-stage deterministic AppNo matching using curated AppNo lists.

### Decision 2: TRUE Raw Score Recalculation
**Problem:** 42.2% of stored raw score totals in CEM data were incorrect.  
**Solution:** Recalculated `TotalRawScoreTRUE` by summing 8 component scores from first principles. Preserved both stored and TRUE values for auditing.

### Decision 3: 4-Pipeline Separation
**Problem:** Modifying earlier pipelines could break downstream consumers.  
**Solution:** Added Pipeline 4 as a final enrichment step, keeping Pipelines 1-3 unchanged.

### Decision 4: REAL_FOREIGNERS.csv Integration
**Problem:** Original Pipeline 4 completely omitted the ground-truth citizenship data (32,501 records).  
**Solution:** Rewrote `4_Citizenship_Integration.py` to implement the proper 3-tier hierarchy with REAL_FOREIGNERS as Priority 1.

### Decision 5: Observable Cohort Restriction
**Problem:** Including recent NMAT cohorts in PLE analyses falsely depresses confirmed-PLE rates (right-censoring).  
**Solution:** All PLE-linked analyses use `Year <= 2014` (the "observable cohort"), giving examinees at least 8 years to take the boards.

### Decision 6: Best-Record Deduplication
**Problem:** 25% of examinees took NMAT multiple times, violating independence assumptions for statistical tests.  
**Solution:** `IS_BEST_NMAT_RECORD` flag selects exactly one record per person (for PLE passers: the matched attempt; for others: highest percentile).

### Decision 7: Column Slimming (Exodus Lite)
**Problem:** The dataset had 118 columns, but only 54 were used by any consumer.  
**Solution:** Audited both `dashboard.py` and `data_aggregator/`, removed 64 unused columns. Reduced file size by 62.4% (27.9 MB → 10.5 MB).

### Decision 8: Emoji Handling
**Problem:** A character-sanitization script replaced emojis in Streamlit tab labels with `?`.  
**Solution:** Previous commit (632b5bd) restored emoji icons by selectively recovering non-ASCII characters from git history. All 12 tab icons now display correctly.

---

## Record of Pipeline Output Files

| Stage | Output File | Location | Rows | Cols | Notes |
|-------|-------------|----------|-----:|-----:|-------|
| P1 | `NMAT_FINAL.parquet` | `dataset/output/` | 178,927 | 101 | Intermediate |
| P1 | `NMAT_FINAL.csv` | `dataset/` | 178,927 | 101 | Intermediate (CSV) |
| P2 | `NMAT_Ultima.parquet` | `dataset/` | 178,927 | **115** | Superseded by Exodus |
| P2 | `PLE_MATCH_MASTER.csv` | `dataset/output/` | 43,601 | — | One row per PLE passer |
| P2 | `PLE_PASSERS_IN_NMAT.csv` | `dataset/output/` | 36,305 | — | Best-record passers |
| P3 | Various CSV/PNG | `dataset/analysis_output/` | — | — | 95 files total |
| P4 | **`NMAT_Exodus.parquet`** | `dataset/` | 178,927 | **54** | **Final output (active)** |
| P4 | `NMAT_Exodus.parquet.bak` | `dataset/` | 178,927 | 118 | Full backup |
| P4 | `NMAT_Exodus.csv` | `dataset/` | 178,927 | 54 | CSV for inspection |

---

*Document generated from pipeline code, results documents, and wiki knowledge.*  
*All 4 pipelines verified working. Final dataset: `dataset/NMAT_Exodus.parquet` (54 cols, 10.5 MB).*
