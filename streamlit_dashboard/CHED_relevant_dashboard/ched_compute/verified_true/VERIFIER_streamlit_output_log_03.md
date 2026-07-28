# VERIFIER: Tab 3 — PLE-Passer Linkage (Dashboard Replication)

**Verification Date:** July 28, 2026 14:27
**Data Source:** `NMAT_Exodus.parquet`
**Verifier:** `ched_compute/verified_true/verifier_03_ple_linkage.py`

---

Replicates the exact dashboard logic from `dashboard.py` TAB 3. All values should match those in `ched_compute/page_results/03_ple_linkage.md`.

## Overview

| Metric | Value |
|--------|-------|
| Pre-2015 Cohort Size (Best Record) | 64,501 |
| Matched to PLE Passer Records | 29,273 |
| Overall NMAT-to-PLE Linkage Rate | 45.38% |
| Source | NMAT_Exodus.parquet (best records, Year <= 2014) |

## PLE Linkage by Score Bin

| Score Bin | Range | n (Pre-2015) | PLE Matched | NMAT-to-PLE Linkage Rate |
|:---:|:---:|:---:|:---:|:---:|
| B1 | 0-9 | 6,104 | 505 | 8.27% |
| B2 | 10-19 | 5,254 | 830 | 15.80% |
| B3 | 20-29 | 5,228 | 997 | 19.07% |
| B4 | 30-39 | 5,741 | 1,312 | 22.85% |
| B5 | 40-49 | 6,229 | 2,882 | 46.27% |
| B6 | 50-59 | 5,831 | 2,992 | 51.31% |
| B7 | 60-69 | 5,942 | 3,359 | 56.53% |
| B8 | 70-79 | 6,355 | 3,819 | 60.09% |
| B9 | 80-89 | 6,854 | 4,595 | 67.04% |
| B10 | 90-100 | 9,657 | 7,352 | 76.13% |

*B4 linkage: 22.85%, B5 linkage: 46.27%, B4->B5 jump: +23.42 pp*

## Linkage by Score Bin and UNI_TYPE

| Score Bin | Public | Private | Foreign | Not Specified |
|:---:|:---:|:---:|:---:|:---:|
| B1 | 6.70% (1030) | 8.82% (4843) | 3.47% (144) | 4.60% (87) |
| B2 | 11.44% (822) | 16.94% (4257) | 7.87% (89) | 9.30% (86) |
| B3 | 17.47% (790) | 19.62% (4276) | 9.52% (84) | 15.38% (78) |
| B4 | 17.77% (895) | 24.22% (4703) | 10.00% (80) | 9.52% (63) |
| B5 | 43.37% (1026) | 47.26% (5034) | 18.29% (82) | 49.43% (87) |
| B6 | 49.22% (1022) | 52.05% (4657) | 30.23% (86) | 59.09% (66) |
| B7 | 56.53% (1210) | 57.28% (4567) | 25.96% (104) | 52.46% (61) |
| B8 | 57.02% (1324) | 61.73% (4844) | 28.44% (109) | 55.13% (78) |
| B9 | 65.09% (1630) | 68.76% (5007) | 29.32% (133) | 61.90% (84) |
| B10 | 77.48% (3468) | 76.74% (5876) | 38.97% (195) | 67.80% (118) |

## Score Distribution by PLE Status (Box Plot Data)

| Metric | PLE Passers (Linked) | Non-Linked Examinees | Difference |
|--------|:---:|:---:|:---:|
| n | 29,273 | 35,228 | -5,955 |
| Median Score | 73.0 | 36.0 | +37.0 |
| Q1 Score (25th) | 52.0 | 15.0 | +37.0 |
| Q3 Score (75th) | 90.0 | 63.0 | +27.0 |
| Median TotalRawScore | 143.0 | 112.0 | +31.0 |
| Q1 Raw Score | 125.0 | 94.0 | +31.0 |
| Q3 Raw Score | 164.0 | 134.0 | +30.0 |

## PLE-Passer Linkage by NMAT Year

| Year | n (observable) | Confirmed PLE Passers | Linkage Rate (%) |
|:---:|:---:|:---:|:---:|
| 2006 | 3,665 | 2,038 | 55.61% |
| 2007 | 3,660 | 1,868 | 51.04% |
| 2008 | 4,849 | 2,514 | 51.85% |
| 2009 | 6,881 | 3,226 | 46.88% |
| 2010 | 8,008 | 3,808 | 47.55% |
| 2011 | 8,731 | 3,853 | 44.13% |
| 2012 | 9,145 | 4,066 | 44.46% |
| 2013 | 9,121 | 3,951 | 43.32% |
| 2014 | 10,441 | 3,949 | 37.82% |

## PLE-Passer Linkage by Course Group

| Course Group | N | Confirmed | Median %ile | Linkage Rate (%) |
|:---|:---:|:---:|:---:|:---:|
| Education | 2,973 | 1,541 | 52.0 | 51.83% |
| Engineering & Technology | 302 | 114 | 71.0 | 37.75% |
| Medical & Allied | 35,433 | 16,061 | 49.0 | 45.33% |
| Natural Sciences | 15,219 | 6,921 | 66.0 | 45.48% |
| Other | 6,189 | 2,853 | 55.0 | 46.10% |
| Social & Behavioral Sciences | 4,385 | 1,783 | 64.0 | 40.66% |

## PLE-Passer Linkage by University Type

| University Type | N | Confirmed | Median %ile | Linkage Rate (%) |
|:---|:---:|:---:|:---:|:---:|
| Foreign | 1,124 | 248 | 58.0 | 22.06% |
| Private | 48,991 | 21,909 | 51.0 | 44.72% |
| Public | 13,555 | 6,786 | 68.0 | 50.06% |

## Course Group Survival (B8-B10+)

| Course Group | n (Best Record) | n in B8-B10 | % in B8-B10 | PLE Linkage Rate (Pre-2015) |
|:---|:---:|:---:|:---:|:---:|
| Medical & Allied | 63,900 | 18,138 | 28.38% | 45.33% |
| Natural Sciences | 41,430 | 14,660 | 35.38% | 45.48% |
| Social & Behavioral Sciences | 16,462 | 4,456 | 27.07% | 40.66% |
| Other | 7,983 | 2,778 | 34.80% | 46.10% |
| Education | 3,279 | 1,086 | 33.12% | 51.83% |
| Engineering & Technology | 750 | 382 | 50.93% | 37.75% |

## Clean PLE Subset

Filters: IS_BEST_NMAT_RECORD, IS_PLE_ANALYSIS_SAFE, PLE_YEAR_GAP >= 5, FOREIGNER_STATUS == Filipino

| Metric | Value |
|--------|-------|
| Clean Subset Size | 27,151 |
| PLE Matched in Clean Subset | 27,151 |
| NMAT-to-PLE Linkage Rate (Clean) | 100.00% |
| N_CLEAN_B5 (B5+ in clean subset) | 23,357 |
| Share of observable cohort (B5+ clean) | 36.2% |

### Clean Subset: Linkage by Score Bin

| Score Bin | n (Clean) | PLE Matched | Linkage Rate |
|:---:|:---:|:---:|:---:|
| B1 | 433 | 433 | 100.00% |
| B2 | 729 | 729 | 100.00% |
| B3 | 881 | 881 | 100.00% |
| B4 | 1,163 | 1,163 | 100.00% |
| B5 | 2,678 | 2,678 | 100.00% |
| B6 | 2,775 | 2,775 | 100.00% |
| B7 | 3,139 | 3,139 | 100.00% |
| B8 | 3,554 | 3,554 | 100.00% |
| B9 | 4,325 | 4,325 | 100.00% |
| B10 | 6,886 | 6,886 | 100.00% |

### Clean Subset B5+ PLE Linkage by Year

| Year | Total B5+ (Clean) | Confirmed | Linkage Rate (%) |
|:---:|:---:|:---:|:---:|
| 2006 | 1,435 | 1,435 | 100.0% |
| 2007 | 1,352 | 1,352 | 100.0% |
| 2008 | 1,953 | 1,953 | 100.0% |
| 2009 | 2,432 | 2,432 | 100.0% |
| 2010 | 3,059 | 3,059 | 100.0% |
| 2011 | 3,084 | 3,084 | 100.0% |
| 2012 | 3,283 | 3,283 | 100.0% |
| 2013 | 3,311 | 3,311 | 100.0% |
| 2014 | 3,448 | 3,448 | 100.0% |

### Clean B5+ Subset by University Type

| University Type | N | Share (%) |
|:---|:---:|:---:|
| Foreign | 172 | 0.7% |
| Not Specified | 275 | 1.2% |
| Private | 17,180 | 73.6% |
| Public | 5,730 | 24.5% |

## Verification Summary

| Check | Status |
|-------|--------|
| Observable cohort size (64,501) | PASS |
| PLE matched count (29,273) | PASS |
| Overall linkage rate (45.38%) | PASS |
| Clean subset size (27,151) | PASS |
| Clean B5+ count (23,357) | PASS |
| B1 linkage rate (8.27%) | PASS |
| B2 linkage rate (15.80%) | PASS |
| B3 linkage rate (19.07%) | PASS |
| B4 linkage rate (22.85%) | PASS |
| B5 linkage rate (46.27%) | PASS |
| B6 linkage rate (51.31%) | PASS |
| B7 linkage rate (56.53%) | PASS |
| B8 linkage rate (60.09%) | PASS |
| B9 linkage rate (67.04%) | PASS |
| B10 linkage rate (76.13%) | PASS |

---

*Verifier executed at: 2026-07-28 14:27:05*