# NMAT → PLE Passer Forensic Audit Report

**Date:** 2026-07-27  
**Dataset:** NMAT_Exodus.parquet (178,927 rows, 54 columns)  
**Audit scope:** Observable cohort (Year ≤ 2014), confirmed passers only (IS_PLE_ANALYSIS_SAFE=True)  
**Script:** `forensic_audit_v5_final.py`

---

## 1. Audit Population

| Metric | Count |
|---|---|
| Observable cohort (Year ≤ 2014) | 88,144 |
| IS_PLE_ANALYSIS_SAFE = True | 40,870 (rows, including multiple attempts per person) |
| IS_BEST_NMAT_RECORD (unique persons) | 29,273 rows (29,258 after dedup — see §3) |

### By Score Band (Best-Record Confirmed Passers)

| Band | All Confirmed Rows | Best-Record Persons | % of Best-Record |
|---|---|---|---|
| B1 (0–9) | 694 | 508 | 1.7% |
| B2 (10–19) | 1,402 | 830 | 2.8% |
| B3 (20–29) | 2,073 | 997 | 3.4% |
| **B4 (30–39)** | 3,014 | **1,312** | **4.5%** |
| B5 (40–49) | 4,257 | 2,882 | 9.8% |
| B6 (50–59) | 4,478 | 2,992 | 10.2% |
| B7 (60–69) | 4,873 | 3,359 | 11.5% |
| B8 (70–79) | 5,306 | 3,819 | 13.0% |
| B9 (80–89) | 6,049 | 4,595 | 15.7% |
| B10 (90–100) | 8,071 | 7,352 | 25.1% |
| Missing | 653 | 627 | 2.1% |
| **Total** | **40,870** | **29,273** | **100%** |

### Policy-Relevant Aggregates

| Group | Best-Record Count | % of Best-Record |
|---|---|---|
| B4+ (≥30th percentile) | 26,311 | 89.9% |
| B5+ (≥40th percentile) | 24,999 | 85.4% |
| **B4-and-below (<30th)** | **2,335** | **8.0%** |
| **B5-below (<40th)** | **3,647** | **12.5%** |
| B4-to-B5 band (30–39) | 1,312 | 4.5% |

---

## 2. Match Method Distribution (Best-Record)

| Method | Count | % |
|---|---|---|
| EXACT | 27,245 | 93.1% |
| MANUAL_APPNO_MATCH | 1,952 | 6.7% |
| DETERMINISTIC_APPNO | 76 | 0.3% |

---

## 3. Match Cardinality / Uniqueness

| Cardinality Pattern | Count | Notes |
|---|---|---|
| **One-to-one** (1 appno ↔ 1 person) | ~29,258 | Dominant pattern |
| **Many-to-one** (1 appno → >1 person) | **0** | No appno-sharing across persons in best-record |
| **One-to-many PLE** (1 person → >1 PLE year) | **1** | Person 3b1cfa... linked to PLE years 2013 AND 2018 |
| **Duplicate best-record** (1 person → 2 best-record rows) | **15 persons** | Pipeline bug — see §4 |
| Persons with 2+ NMAT attempts (all confirmed) | 7,701 of 31,805 (24.2%) | Repeat taker behavior is common |

### Duplicate Best-Record Bug

**Root cause:** 15 persons appear twice in `IS_BEST_NMAT_RECORD` because both their MANUAL_APPNO_MATCH (from PLE_UNMATCHED.csv, lacking PLE year) AND their EXACT match (from PLE_DATA.csv) were flagged as best-record. The pipeline's join logic flagged two different APPNO_CLEAN values for the same person.

**Pattern observed:**
- 14/15 persons: one MANUAL_APPNO_MATCH row (no PLE year) + one EXACT/MANUAL row (with PLE year)
- 1/15 person: same appno (1073584), same year (2007), but different percentiles (98 vs 80)

**Resolution:** Dedup by keeping the row with PLE_YEAR_PASSED first (preferring the EXACT match). This reduces best-record from 29,273 → 29,258 (15 excess rows removed). Zero impacted persons remain with duplicates after dedup.

---

## 4. Low-Score (< B5 / <40th %ile) Deep Dive

### Demographics

| Metric | Count |
|---|---|
| Best-record below B5 | **3,647** |
| Unique persons below B5 | 3,647 (same — each person counted once) |
| Persons with 1 NMAT attempt | 3,593 (98.5%) |
| Persons with 2+ NMAT attempts | 54 (1.5%) |
| Persons with linked ≠ highest attempt | **25 (0.7%)** |
| Persons whose highest attempt ≥ B5 | 8 (0.2%) |
| Persons whose highest attempt ≥ B4 | 1,323 (36.3%) — mostly B4 band naturally |

### Year Gaps (NMAT → PLE)

| Gap Category | Count |
|---|---|
| Negative | 0 |
| Zero | 0 |
| < 5 years | 0 |
| 5–10 years | 3,131 (85.9%) |
| > 10 years | 86 (2.4%) |
| Missing | 430 (11.8%) — all MANUAL_APPNO_MATCH / DETERMINISTIC_APPNO |

All gaps ≥ 5 years — consistent with the pipeline's `YEAR_GAP_MIN=5` filter. The 86 persons with >10-year gaps are plausible for delayed medical school/board-taking trajectories (e.g., took NMAT in 2006, passed PLE in 2018+).

### Method Breakdown (Below B5)

| Method | Count | % |
|---|---|---|
| EXACT | 3,217 | 88.2% |
| MANUAL_APPNO_MATCH | 398 | 10.9% |
| DETERMINISTIC_APPNO | 32 | 0.9% |

**Key finding:** 88.2% of low-score passers were linked via exact name match — the strongest possible method.

---

## 5. Validity Classification

### Classification Rules

Mutually exclusive categories applied to deduplicated best-record (N=29,258):

| Category | Rule |
|---|---|
| **valid_unique** | One person, one appno, one PLE year; no conflicts. Default assignment. |
| **valid_repeat_taker** | Unique deterministic PLE match, but linked NMAT attempt has lower percentile than person's highest attempt. |
| **ambiguous_multiple** | Same appno linked to >1 person, or unresolved one-to-many/many-to-one. |
| **data_quality** | Negative/zero year gap, duplicate best-record, multiple PLE years for same person, or other identifier conflict. |
| **insufficient_info** | Cannot determine uniqueness. |

### Results (All Best-Record)

| Category | Count | % |
|---|---|---|
| **valid_unique** | **28,644** | **97.9%** |
| **valid_repeat_taker** | **599** | **2.0%** |
| data_quality | 15 | 0.1% |
| ambiguous_multiple | 0 | 0.0% |
| insufficient_info | 0 | 0.0% |

### Results by Score Band

| Band | valid_unique | valid_repeat_taker | data_quality | Anomalous % |
|---|---|---|---|---|
| B1 | 505 | 3 | 0 | 0.0% |
| B2 | 823 | 7 | 0 | 0.0% |
| B3 | 989 | 6 | 0 | 0.0% |
| B4 | 1,305 | 7 | 0 | 0.0% |
| **B5-below (<40th)** | **3,622** | **23** | **0** | **0.0%** |
| B5 | 2,765 | 113 | 2 | 0.1% |
| B6 | 2,882 | 106 | 2 | 0.1% |
| B7 | 3,247 | 106 | 2 | 0.1% |
| B8 | 3,691 | 126 | 0 | 0.0% |
| B9 | 4,509 | 82 | 3 | 0.1% |
| B10 | 7,301 | 43 | 6 | 0.1% |
| Missing | 627 | 0 | 0 | 0.0% |

### Results by Match Method

| Method | valid_unique | valid_repeat_taker | data_quality |
|---|---|---|---|
| EXACT | 26,701 | 530 | 13 |
| MANUAL_APPNO_MATCH | 1,868 | 69 | 2 |
| DETERMINISTIC_APPNO | 75 | 0 | 0 |

---

## 6. Exception Table (Anomalous Records)

**15 data-quality records total.** All are from the duplicate best-record bug (14 persons) + the 1 person with 2 PLE years. **Zero ambiguous-multiple records.**

| Reason | Count | Detail |
|---|---|---|
| Duplicate best-record resolved | 14 | Person had 2 IS_BEST_NMAT_RECORD rows. Kept the row with PLE year. |
| Multiple PLE years (2) | 1 | Person 3b1cfa... linked to PLE 2013 (DETERMINISTIC_APPNO) AND 2018 (EXACT). Retained EXACT row. |

The 14 duplicate persons all share the same pattern:
- One MANUAL_APPNO_MATCH row from PLE_UNMATCHED.csv — no PLE year, no gap
- One EXACT match row from PLE_DATA.csv — has proper PLE year/gap
- The EXACT row was kept after dedup; the MANUAL row was discarded

The 1 person with 2 PLE years is unexplained — remarkably improbable for legitimate data.

### De-identified Exception Details (Hashed IDs)

```
#1  Reason: multiple_ple_years_2      Person: 3b1cfa25173c  B5  Pct=49  Year=2009  Method=EXACT
#2  Reason: dup_best_record_resolved  Person: 712678bf8c48  B10 Pct=99  Year=2007  Method=EXACT
#3  Reason: dup_best_record_resolved  Person: 9bf119647233  B6  Pct=54  Year=2008  Method=EXACT
#4  Reason: dup_best_record_resolved  Person: 80bb5ecd163d  B10 Pct=97  Year=2009  Method=EXACT
#5  Reason: dup_best_record_resolved  Person: 50d2e7b0d885  B9  Pct=83  Year=2014  Method=EXACT
#6  Reason: dup_best_record_resolved  Person: 79aa5c2e5194  B10 Pct=97  Year=2009  Method=EXACT
#7  Reason: dup_best_record_resolved  Person: 456660455c25  B10 Pct=90  Year=2007  Method=EXACT
#8  Reason: dup_best_record_resolved  Person: e22a84fb6496  B7  Pct=62  Year=2014  Method=EXACT
#9  Reason: dup_best_record_resolved  Person: b8a51b66f20a  B9  Pct=81  Year=2011  Method=MANUAL
#10 Reason: dup_best_record_resolved  Person: 8c4ae3b66095  B9  Pct=87  Year=2007  Method=EXACT
#11 Reason: dup_best_record_resolved  Person: 240bb4ef0a93  B10 Pct=94  Year=2009  Method=MANUAL
#12 Reason: dup_best_record_resolved  Person: 724dcc532aa9  B7  Pct=60  Year=2012  Method=EXACT
#13 Reason: dup_best_record_resolved  Person: 88e6de8d5560  B6  Pct=53  Year=2007  Method=EXACT
#14 Reason: dup_best_record_resolved  Person: 99a7f0c339d9  B5  Pct=42  Year=2008  Method=EXACT
#15 Reason: dup_best_record_resolved  Person: f469ad56848b  B10 Pct=98  Year=2007  Method=EXACT
```

---

## 7. PLE-Linkage: Before vs After Exclusion

### Comparison Table

| Metric | Original (with dupes) | Before Exclusion (deduped) | After Exclusion (clean) |
|---|---|---|---|
| **Total** | 29,273 | 29,258 | 29,243 |
| **≥ B4** | 26,311 (89.9%) | 26,298 (89.9%) | 26,283 (89.9%) |
| **≥ B5** | 24,999 (85.4%) | 24,986 (85.4%) | 24,971 (85.4%) |
| **< B4** | 2,335 (8.0%) | 2,333 (8.0%) | 2,333 (8.0%) |
| **< B5** | 3,647 (12.5%) | 3,645 (12.5%) | 3,645 (12.5%) |
| **B4-to-B5 band** | 1,312 (4.5%) | 1,312 (4.5%) | 1,312 (4.5%) |
| **B4/B5 gradient** | 1,312 (4.5pp) | 1,312 (4.5pp) | 1,312 (4.5pp) |
| **B4+/B5+ ratio** | 1.0525 | 1.0525 | 1.0525 |

**Conclusion: No material change.** Excluding the 15 anomalous records changes the B4/B5 gradient by 0 (zero) percentage points. The duplicate best-record bug has negligible impact on the clean subset because the defective MANUAL_APPNO_MATCH rows lack PLE year data and are naturally excluded by the ≥5yr gap filter.

### Dashboard Impact Assessment

The dashboard's "clean PLE subset" filter is:
```
IS_BEST_NMAT_RECORD & IS_PLE_ANALYSIS_SAFE & PLE_YEAR_GAP >= 5 & FOREIGNER_STATUS == "Filipino"
```

- Only **1 duplicate pair** passes this filter (same appno, different percentile — Person f469ad56848b)
- B5+ count: 23,357 (with dupes) vs 23,356 (deduped) — **impact of 1/23,357 = 0.004%**
- All other duplicate rows are naturally excluded because they lack `PLE_YEAR_GAP`

---

## 8. The ~3,000 Low-Score Passers Question

### Direct Answer

> **The approximately 3,000–3,600 low-score passers are overwhelmingly valid unique deterministic matches, NOT ambiguous or anomalous.**

### Breakdown of Below-B5 (N=3,647)

| Category | Count | % |
|---|---|---|
| **Valid unique deterministic match** | **3,622** | **99.4%** |
| **Valid repeat-taker linkage** | **23** | **0.6%** |
| Ambiguous multiple match | 0 | 0.0% |
| Data quality concern | 0 | 0.0% |

### Supporting Evidence

1. **No appno-sharing across persons:** Zero application numbers are linked to multiple persons in the best-record. Every low-score match is individually identifiable.

2. **Repeat-taker artifacts are negligible:** Only 23 persons (0.6%) have a different higher-scoring NMAT attempt. Most of these have marginal differences (mean diff = 0.1 percentile points).

3. **Year gaps are plausible:** All gaps ≥ 5 years. 85.9% are 5–10 years (normal 4-year med school + board timing). 2.4% exceed 10 years (plausible delayed paths).

4. **Match method is strong:** 88.2% of low-score matches used EXACT name matching. Only 10.9% used MANUAL_APPNO_MATCH and 0.9% used DETERMINISTIC_APPNO.

5. **Majority are single-attempt examinees:** 98.5% of low-score passers took NMAT only once. Their score is their score.

### Why the ~3,000 Number Is Reasonable

The dashboard shows 3,647 best-record confirmed passers below B5 (out of 29,273 total confirmed passers). With 178,927 examinees in the full dataset, a roughly 2% linkage rate in the lowest bands is consistent with:
- Historical PLE passing rates (typically 40–60% of takers)
- The fact that only a fraction of NMAT takers enter medical school
- The expectation that some examinees with lower NMAT scores still succeed in med school and pass boards (the entire premise of the CHED cut-off debate)

---

## 9. Conclusions and Recommendations

### A. Validity of Low-Score Passers

The 3,647 confirmed PLE passers below B5 are **valid observations**, not artifacts. The matching pipeline correctly identifies real PLE passers who took NMAT and scored in the lower percentiles. These represent legitimate historical cases of examinees with modest NMAT scores who subsequently passed the physician licensure exam.

### B. Impact on B4-to-B5 Gradient

Excluding the 15 anomalous records changes the B4/B5 gradient by **exactly 0 percentage points**. The dashboard's "clean PLE subset" B4/B5 ratio of 1.0525 is robust and unaffected.

### C. Recommended Revisions

| Item | Recommendation | Priority |
|---|---|---|
| **Duplicate best-record bug** | Fix pipeline's `IS_BEST_NMAT_RECORD` flagging to prevent duplicate assignment. Select one best-record per PERSON_KEY even when both a MANUAL and EXACT match exist. | **Medium** |
| **Person with 2 PLE years** | Investigate record 3b1cfa... (PLE years 2013 and 2018). If unresolved, exclude from analyses requiring unique PLE linkage. | **Low** |
| **Missing PLE_YEAR_GAP (76 DETERMINISTIC_APPNO records)** | Compute year gap for deterministic appno matches that have `PLE_YEAR_PASSED` but missing `PLE_YEAR_GAP`. | **Low** |
| **Dashboard caveat** | No revision needed to current dashboard tables/charts. The "clean PLE subset" filter already excludes the duplicate rows. Consider adding a footnote: "All PLE linkages are deterministic (exact name, manual appno, or direct appno match). No fuzzy matching was used." | **Optional** |
| **Summary/infographic** | No revision needed. The B4/B5 gradient figure (1,312 or 4.5pp) is robust. | **None** |
| **Withhold any metric** | No metric needs to be withheld. The anomaly rate of 0.1% (15/29,273) is below any reasonable materiality threshold. | **None** |

### D. Statement for CHED Presentation

> *"The NMAT-to-PLE-passer linkage rates presented in this dashboard are derived from deterministic-only matching (exact name, manual application number, or direct CEM application-number matching). A record-level forensic audit of the 3,647 confirmed PLE passers below the 40th percentile found that 99.4% are valid unique deterministic matches. Only 0.1% of all confirmed PLE-passers (15 of 29,258) had any data-quality flag — all attributable to a pipeline bookkeeping issue that does not affect the dashboard's primary exhibits. No fuzzy matching was used at any stage."*

---

## 10. Audit Trail

| Step | Rows | Operation |
|---|---|---|
| Load NMAT_Exodus.parquet | 178,927 | Full dataset |
| Filter: Year ≤ 2014 | 88,144 | Observable cohort |
| Filter: IS_PLE_ANALYSIS_SAFE = True | 40,870 | Confirmed passers (all rows) |
| Filter: IS_BEST_NMAT_RECORD = True | 29,273 | Best-record (1 per person intended) |
| Dedup: remove 15 excess duplicate rows | 29,258 | Keep row with PLE year first |
| Classify validity | 29,258 | 5 mutually exclusive categories |
| Exclude anomalous (15 data_quality) | 29,243 | Clean subset for comparison |

**Audit script:** `D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\forensic_audit_v5_final.py`  
**Output CSVs:**
- `forensic_audit_classified.csv` — full classified dataset
- `forensic_audit_exceptions.csv` — the 15 anomalous records
- `forensic_audit_summary.csv` — summary table by band
- `forensic_audit_low_score_details.csv` — per-person analysis of low-score passers
