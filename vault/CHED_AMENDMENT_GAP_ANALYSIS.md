# CHED Amendment Gap Analysis

## Dashboard vs. CMO No. __, s. 2026 Requirements

**Date:** 2026-07-26
**Status:** 🔴 CRITICAL GAPS — Dashboard cannot support the new CHED amendment in its current form.

---

## Executive Summary

The dashboard (`dashboard.py` Streamlit + `app.R` R Shiny) was designed for **descriptive trend analysis** of NMAT and PLE data. It was **not built** to support the regulatory requirements of the new CHED amendment. While the **underlying dataset** (`NMAT_Ultima.parquet`) has some of the raw data needed, **the dashboard lacks every single CHED-specific analysis, table, visualization, and model** required by the amendment.

**8 specific gap areas** are documented below. The dashboard currently supports **zero** of the CHED amendment's analytical requirements.

---

## GAP 1: No 5-Year National PLE Average Calculation

### What CHED Requires
> *"The chosen NMAT cut-off shall be applied equally to local and foreign applicants"* and *"Only PHEIs with a PLE performance at a rate above the average national passing percentage for the last five (5) years can avail of this adjusted cut-off."*

The amendment uses the **average national PLE passing percentage for the last 5 years** as the benchmark. Every PHEI must be compared against this benchmark.

### What the Dashboard Has
| Item | Status |
|------|--------|
| Annual national PLE passing rate per year | ✅ Calculated internally (see analysis below) |
| Rolling 5-year national average | ❌ **NOT computed** |
| Comparison of each PHEI vs. national benchmark | ❌ **NOT computed** |

### What Exists
The raw data IS there in `NMAT_Ultima.parquet` — the annual national PLE passing rates from the data:
- 2010: 51.63%
- 2011: 46.89%
- 2012: 45.02%
- 2013: 42.63%
- 2014: 36.52%

But **no 5-year rolling average is calculated anywhere in the dashboard code**. The Policy Tables page only shows aggregate PLE alignment by year/course/uni_type, not the national benchmark.

**Status:** ❌ NOT SUPPORTED

---

## GAP 2: No Per-HEI PLE Performance Table

### What CHED Requires
> *"Only PHEIs with a PLE performance at a rate **above the average national passing percentage** for the last five (5) years can avail of this adjusted cut-off"* and *"If a PHEI's PLE passing rate falls below the average national passing percentage for three (3) consecutive years, CHED shall revoke this autonomy."*

This requires a **per-institution PLE passing rate table** showing:
- Each HEI's name
- Each HEI's PLE passing rate (last 5 years)
- Whether that rate is above or below the national benchmark
- Classification: eligible for 30th percentile cut-off vs. must maintain 40th percentile

### What the Dashboard Has
| Item | Status |
|------|--------|
| Institution-level grouping (`NMA_College`, `UNIVERSITY`, `UNI_TYPE`) | ✅ Available in data |
| Per-HEI PLE passing rate computation | ❌ **NOT implemented** |
| 5-year window filtering per HEI | ❌ **NOT implemented** |
| Eligibility classification (above/below national average) | ❌ **NOT implemented** |
| Visualization or table showing per-HEI eligibility | ❌ **NOT implemented** |

### Why This Gap Matters
The dashboard groups **only** by `UNI_TYPE` (Public/Private/Foreign). This means you can see that **Private HEIs as a group** have a certain PLE rate — but you **cannot** see which specific private schools qualify for the 30th percentile cut-off and which do not. The CHED amendment operates at the INDIVIDUAL HEI level, not the aggregate level.

**Underlying data exists?** ✅ The `NMA_College` column has 3,251 unique institutions, and `IS_PLE_ANALYSIS_SAFE` gives per-examinee PLE status. A per-HEI aggregation is possible but **not built**.

**Status:** ❌ NOT SUPPORTED

---

## GAP 3: No 30th vs 40th Cut-off Scenario Modeling

### What CHED Requires
A PHEI needs to know: *"If I set my cut-off at the 30th percentile (B4+), what does my incoming class look like? How does that compare to a 40th percentile (B5+) cut-off?"*

Two different cut-off levels apply depending on PLE performance:
- **Above national average** → can use 30th percentile (B4+)
- **Below national average** → must use 40th percentile (B5+)

### What the Dashboard Has
| Item | Status |
|------|--------|
| NMAT Percentile Bins (B1-B10) | ✅ Available |
| B4 = 30th-40th, B5 = 40th-50th | ✅ Understandable from bin definition |
| Cut-off scenario comparison tables | ❌ **NOT implemented** |
| Impact analysis: how many students admitted at each cut-off | ❌ **NOT implemented** |
| PLE success rate comparison: 30th-cut-off admits vs 40th-cut-off admits | ❌ **NOT implemented** |
| Visualization of trade-offs between cut-off levels | ❌ **NOT implemented** |

### Why This Gap Matters
The Policy Tables page shows PLE alignment rates, but there is **no "what-if" modeling** for different cut-off scenarios. A policymaker cannot use the dashboard to answer: *"If we raise the cut-off from 30th to 40th percentile, how many students lose admission, and what's the PLE success rate gain?"*

**Status:** ❌ NOT SUPPORTED

---

## GAP 4: No 3-Year Consecutive PLE Performance Tracking

### What CHED Requires
> *"If a PHEI's PLE passing rate falls below the average national passing percentage for three (3) consecutive years, CHED shall revoke this autonomy and reinstate the 40th percentile baseline for that specific institution."*

This requires a **rolling 3-year compliance tracker** per HEI.

### What the Dashboard Has
| Item | Status |
|------|--------|
| PLE data with year of passing (`PLE_YEAR_PASSED`) | ✅ Available |
| Per-HEI annual PLE rate computation | ❌ **NOT implemented** |
| Rolling 3-year consecutive check | ❌ **NOT implemented** |
| Compliance status (green/yellow/red) per HEI | ❌ **NOT implemented** |
| Alert for institutions at risk of sanctions | ❌ **NOT implemented** |

### Why This Gap Matters
This is a **monitoring and compliance** feature. The dashboard was built for descriptive statistics, not ongoing regulatory monitoring. There is no concept of "consecutive years below benchmark" in the codebase. Building this requires:

1. Compute per-HEI annual PLE passing rates
2. Compare each year against the national benchmark
3. Flag HEIs where the rate has been below benchmark for 3+ consecutive years
4. Trigger: automatically revert cut-off to 40th percentile

**Status:** ❌ NOT SUPPORTED

---

## GAP 5: No Foreign Student Slot Analysis

### What CHED Requires
> *"Enrollment is capped at ten (10) slots per incoming freshmen class, effective Academic Year 2026-2027"* for foreign students at SUCs.

AND

> *"The adoption of a composite/weighted ranking system for foreign applicants (e.g., 60/40 or 70/30 NMAT-to-other criteria such as GWA, interview, and/or other validated measures)."*

### What the Dashboard Has
| Item | Status |
|------|--------|
| Foreign/Filipino identification (`NAC_NATIONALITY`) | ✅ Available (32,505 foreigners identified) |
| Foreign student count per institution per year | ❌ **NOT implemented** |
| 10-slot cap compliance monitoring | ❌ **NOT implemented** |
| Composite ranking model (60/40 or 70/30) | ❌ **NOT implemented** |
| GWA or interview score data | ❌ **NOT AVAILABLE IN DATASET** |
| Foreign vs Filipino comparison tables | ✅ Basic pseudo-citizenship section exists |

### Data Constraints
- `NAC_NATIONALITY` exists and correctly identifies foreign examinees
- **Pipeline 4 (Citizenship Integration) is broken** so `CITIZENSHIP_FINAL` and `FOREIGNER_STATUS` do not exist in the parquet
- The dashboard loads pseudo-citizenship on-the-fly (871 records only), missing 32,000+ real foreigner records
- **GWA, interview scores, and other composite-ranking criteria do not exist anywhere in the dataset**
- Therefore, a **60/40 composite ranking system CANNOT be built** with the current data

### Deeper Problem
Even if we fix Pipeline 4 to use REAL_FOREIGNERS.csv, the dashboard has **no per-institution foreign student enrollment tracking**. We can't show which SUCs have how many foreign students, or whether they'd exceed the 10-slot cap.

**Status:** ❌ NOT SUPPORTED (and cannot be fully supported without new data sources)

---

## GAP 6: No GIDA / IP Data

### What CHED Requires
> *"SUCs may admit applicants with NMAT scores between the 30th and 39th percentile, provided that the applicant belongs to underrepresented and disadvantaged groups (e.g., a resident of a Geographically Isolated and Disadvantaged Area [GIDA] or belongs to an Indigenous Peoples [IP] community)."*

### What the Dashboard Has
| Item | Status |
|------|--------|
| GIDA (Geographically Isolated and Disadvantaged Area) identifier | ❌ **NOT AVAILABLE IN DATASET** |
| IP (Indigenous Peoples) identifier | ❌ **NOT AVAILABLE IN DATASET** |
| NCIP certification tracking | ❌ **NOT AVAILABLE IN DATASET** |
| DOH/LGU certification tracking | ❌ **NOT AVAILABLE IN DATASET** |
| Province/region data for potential GIDA mapping | ✅ `NMAT Province local address`, `NMAT Region permanent address` exist |

### Why This Gap Is Absolute
NO GIDA or IP data exists anywhere in the NMAT dataset. There are province and region address columns that *might* be used as a proxy to identify GIDA areas, but:
1. There is no GIDA classification mapping available
2. There is no IP community membership data
3. The amendment requires **official documentation** (NCIP cert, DOH/LGU cert), not inference
4. Building this from scratch would require external government datasets

**Status:** ❌ NOT SUPPORTED — data does not exist in the dataset

---

## GAP 7: No Composite Ranking Model for Foreign Applicants

### What CHED Requires
> *"The adoption of a composite/weighted ranking system for foreign applicants (e.g., 60/40 or 70/30 NMAT-to-other criteria such as GWA, interview, and/or other validated measures) to ensure a holistic assessment and the protection of state-subsidized slots for Filipino citizens."*

### What the Dashboard Has
| Item | Status |
|------|--------|
| NMAT scores (percentile, raw, subtest) | ✅ Available |
| General Weighted Average (GWA) | ❌ **NOT AVAILABLE IN DATASET** |
| Interview scores | ❌ **NOT AVAILABLE IN DATASET** |
| Other validated measures | ❌ **NOT AVAILABLE IN DATASET** |
| Composite ranking engine | ❌ **NOT implemented** |
| Foreign-applicant-specific ranking dashboard | ❌ **NOT implemented** |

### Why This Gap Matters
Even with perfect NMAT data, a composite ranking system requires **non-NMAT data** (GWA, interview results) that simply does not exist in this dataset. CHED is asking for a holistic assessment, and the NMAT-only dataset cannot support it.

**Status:** ❌ NOT SUPPORTED — requires data sources not in this project

---

## GAP 8: No HEI-Level NMAT Score Distribution

### What CHED Requires
Institutions need to know how their applicant pool distributes across bins to set appropriate cut-offs. The 30th vs 40th percentile decision is institution-specific.

### What the Dashboard Has
| Item | Status |
|------|--------|
| `NMA_College` column with 3,251 institutions | ✅ Available |
| `UNI_TYPE` grouping (Public/Private/Foreign) | ✅ Available |
| Per-HEI NMAT score distribution table | ❌ **NOT implemented** |
| Per-HEI bin composition chart | ❌ **NOT implemented** |
| Per-HEI filtered view (select one school, see its data) | ❌ **NOT implemented** |
| Per-HEI PLE alignment rate | ❌ **NOT implemented** |

### Why This Gap Matters
The dashboard's most granular grouping is `UNI_TYPE` — three categories. The CHED amendment operates at the level of **individual HEIs**. A policymaker from "University of Santo Tomas" needs to see UST-specific data, not "Private" aggregate data. There is no HEI filter, no HEI-specific page, and no per-HEI analysis.

**Status:** ❌ NOT SUPPORTED

---

## Summary: Full Gap Matrix

| # | CHED Requirement | Dashboard Has It? | Data Available in Parquet? | Effort to Build |
|---|---|---|---|---|
| 1 | 5-year national PLE average benchmark | ❌ No | ✅ Partial | Medium (compute + table) |
| 2 | Per-HEI PLE performance vs benchmark | ❌ No | ✅ Yes (NMA_College + IS_PLE_ANALYSIS_SAFE) | Medium (compute + table) |
| 3 | 30th vs 40th cut-off scenario modeling | ❌ No | ✅ Yes (PercentileBin) | Medium (compute + viz) |
| 4 | 3-year consecutive PHEI compliance tracking | ❌ No | ✅ Yes (PLE_YEAR_PASSED) | High (logic + monitoring UI) |
| 5 | Foreign student slot analysis (10-cap) | ❌ No | ⚠️ Partial (needs Pipeline 4 fix) | Medium (after Pipeline 4 fix) |
| 6 | GIDA / IP applicant provisions | ❌ No | ❌ No (external data needed) | Impossible without new data |
| 7 | Composite ranking (60/40 NMAT+GWA+interview) | ❌ No | ❌ No (GWA/interview missing) | Impossible without new data |
| 8 | Per-HEI NMAT score distribution view | ❌ No | ✅ Yes (NMA_College) | Medium (grouping + viz) |

**Totals:**
- ✅ Supported: **0 / 8**
- ❌ Not supported but buildable with existing data: **4** (Gaps 1, 2, 3, 8)
- ❌ Not supported, needs Pipeline 4 fix first: **1** (Gap 5)
- ❌ Not supported, needs external data: **2** (Gaps 6, 7)
- ❌ Not supported, complex build: **1** (Gap 4)

---

## Conclusion

**The dashboard in its current form does not support a single CHED amendment requirement.** It is a descriptive analytics tool, not a regulatory compliance and scenario-modeling platform.

### Immediate Buildable Work (using existing data)
1. National 5-year rolling PLE average → on the Policy Tables page
2. Per-HEI PLE passing rate table with eligibility classification
3. Cut-off scenario comparison (30th vs 40th percentile impact analysis)
4. Per-HEI filtered view with NMAT score distribution

### Prerequisite Work
5. Fix Pipeline 4 to properly integrate `REAL_FOREIGNERS.csv` → enables foreign student analysis
6. Fix `CITIZENSHIP_FINAL` and `FOREIGNER_STATUS` in parquet → both dashboards reference these columns

### Cannot Build (external data needed)
7. GIDA/IP classification → requires NCIP, DOH, or LGU datasets
8. Composite ranking (60/40) → requires GWA, interview scores from HEIs
9. 3-year consecutive monitoring → requires annual data updates (ongoing process, not one-time build)

---

## Appendix: Data That EXISTS But Is Not Used For CHED

| Available In Dataset | Relevant CMO Use |
|---|---|
| `PercentileBin` (B1-B10) | Identifies 30th percentile (B4+) vs 40th percentile (B5+) — **used nowhere in cut-off analysis** |
| `NMA_College` (3251 unique) | Per-HEI grouping — **used only in Data Integrity page, not in Policy Tables** |
| `IS_PLE_ANALYSIS_SAFE` | Per-examinee PLE status — **aggregated to univ type only, not per-HEI** |
| `NAC_NATIONALITY` (32,505 foreign) | Foreign/Filipino identification — **used only in broken Pipeline 4, not in dashboard citizenship section** |
| `NMAT Province local address` | Potential GIDA proxy — **never analyzed** |
| `PLE_YEAR_PASSED` | Year-specific PLE tracking — **used only for gap calculation, not for benchmark** |

---

*Documented by: NMAT Analysis Codebase Agent*
*Data source: NMAT_Ultima.parquet (178,927 rows × 115 columns, 2006-2018)*
*Dashboard: dashboard.py (Streamlit, ~1,123 lines) + RShiny_Dashboard/NMAT_Shiny/app.R (R Shiny, ~2,190 lines)*
