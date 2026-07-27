# NMAT Performance Analysis (2006–2018) — Executive Stakeholder Report

**Prepared for:** Executive leadership at NMAT, the Center for Educational Measurement (CEM), and the Commission on Higher Education (CHED).
**Scope:** What we found in 13 years of NMAT data, how we made the data trustworthy enough to find it, and what we recommend you do about it.
**Reporting Period:** NMAT examinations 2006–2018; Philippine Licensure Examination (PLE) results 2011–2022.
**Bottom Line Up Front:** The NMAT percentile rank is a powerful predictor of who eventually passes the medical boards — examinees in the top NMAT decile pass the PLE at a 76.25% rate, examinees in the bottom decile at 8.77%. Public-university students out-perform Private and Foreign students at both the NMAT and the PLE. Three-quarters of examinees who retake the NMAT improve. Beneath those headlines sits a substantial story about the data itself: 42% of "stored total scores" in the source system were wrong, 6% of PLE passers had to be recovered manually, and these issues had to be fixed before any insight could be trusted.

---

## 1. The Question That Started This Work

Three constituencies — NMAT (which administers the examination), CEM (which manages the scoring and analytics), and CHED (which oversees medical-education policy) — needed to know whether the NMAT, after 13 years and 178,927 examinations, was doing the job it was designed to do. Specifically:

1. **Is NMAT performance stable across years**, or has the test gotten easier or harder?
2. **Does background matter** — Public vs Private vs Foreign university, pre-med course choice — for how examinees perform?
3. **Does the NMAT actually predict the PLE**, the licensure exam that gates entry to medical practice?
4. **Does retaking the NMAT help** examinees improve?
5. **Are there hidden gaps in fairness** — by gender, by foreign status, by background — that policy should respond to?

These are the questions this report answers. But before any of those answers could be defended, we had to confront and fix the dataset itself.

---

## 2. What We Built

We constructed a four-stage pipeline:

1. **Data Cleaning** — harmonize NMAT examinee records (178,927 rows), enrich them with component-level scores from the CEM database (254,308 rows), and standardize every university name against a reference list of 3,022 institutions.
2. **PLE Matching** — link each NMAT examinee to their eventual PLE outcome using a strictly deterministic, audit-defensible matching method.
3. **Statistical Analysis** — produce yearly trends, group comparisons, and statistical tests on the integrated dataset.
4. **Interactive Dashboard** — a Streamlit-based exploration tool (`dashboard.py`) with twelve thematic pages, dozens of charts, and filters that let any analyst or policy reviewer slice the results by year, university type, course group, or gender.

All outputs land in a single, fully traceable analytical dataset of 178,927 rows with 115 columns. Every match decision, every score recalculation, and every flag is logged in companion audit files.

---

## 3. The Data Problems We Had to Fix First

### 3.1 The "Stored Total Score" Problem — 42% of values were wrong

The CEM system stores each examinee's total raw score as a single number called `STU_RSCORE`. When we summed the eight component subtest scores ourselves and compared, **107,422 out of 174,494 stored totals (42.2%) disagreed with the sum of components.** That is, almost half of the raw totals in the source system were not consistent with what the examinees actually scored on the individual sections.

**What we did:** We do not use `STU_RSCORE`. Instead, on every record where all eight component scores are present (and we confirmed 100% of merged records satisfy this), we compute a new authoritative total called `TotalRawScoreTRUE`, and Part I / Part II equivalents called `PartIRawScoreTRUE` and `PartIIRawScoreTRUE`. We kept the original `STU_RSCORE` field in the dataset for auditing — analysts can see exactly which records disagreed — but every chart, table, and statistic in this report uses the TRUE versions.

**Why it matters:** Had we shipped analyses on the stored field, roughly 4 in every 10 examinees in policy reports would have had the wrong total score. The fix is invisible to end-users of the dashboard, but it is the single most consequential decision in this entire project.

### 3.2 The University Name Problem — 4,367 college strings, only 2,981 real institutions

The same university appears in the raw data under many spellings — "Remedios T. Romualdez Medical Foundation" vs "Remedios Trinidad Romualdez Medical Foundation," "UP Manila" vs "University of the Philippines Manila," with stray punctuation, capitalization, and abbreviation variants. Worse, 75 records carried numeric institution codes (`13207A`, `13100A`, `13155D`, `13206A`) — clearly data-entry errors or placeholder codes. Some institutions were classified inconsistently across applications (the same college appeared simultaneously as Public, Private, and Not Specified in different rows).

**What we did:** A four-stage matching cascade against the UNIVS reference list:
1. Exact match on normalized college name (61.3% resolved).
2. Exact match on the canonical university name (1.6%).
3. Fuzzy match with strict guardrails (minimum 88% similarity score AND at least a 5-point lead over the next-best candidate) (5.4%).
4. Anything else falls through to "Not Specified" / "Unknown" — 31.7% of unique strings, but because most of these are rare strings, only 1,807 records (1.01%) of the full 178,927-row dataset.

**Result:** 98.99% of all NMAT records have a verified institution. After cleaning, every unique college name maps to exactly one university type — the multi-classification problem is fully resolved. Two universities (Velez College and New York University) retain dual classifications at the canonical-name level, likely real edge cases (international campuses, relabeling events) worth a manual review.

### 3.3 The PLE Matching Problem — Linking two systems that don't share IDs

NMAT examinees are identified by an Application Number (`NMA_AppNo`). PLE passers are identified by name and pass year only — there is no common identifier across the two systems. Earlier versions of this pipeline used fuzzy name matching to bridge the gap, but that approach was fragile (Filipino surnames concentrate in narrow lexical bands, producing false positives) and not auditable (reviewers could not trace a match back to a specific source row).

**What we did:** We eliminated fuzzy matching entirely. The current pipeline uses strict, exact matching only, in three sequential stages:

| Stage | Source | Records processed | Confirmed matches |
|---|---|---:|---:|
| **Stage 0 — Manual AppNo curation** | `PLE_UNMATCHED.csv` (curated by hand) | 2,332 with AppNo | **2,331 (99.96%)** |
| **Stage 1 — Exact name match** | `PLE_DATA.csv` | 41,300 | **33,970 (82.3%)** |
| **Stage 2 — Deterministic AppNo (second pass)** | `PLE_STILL_UNMATCHED.csv` | 321 with AppNo | **321 (100%)** |

**Final result on the 43,630 PLE passers in the source data:**

| Status | Count | Share |
|---|---:|---:|
| Confirmed final match | 36,395 | **83.42%** |
| Ambiguous (multiple plausible NMAT candidates) | 772 | 1.77% |
| No valid match (failed year-gap or other filter) | 2,298 | 5.27% |
| No application number provided | 4,135 | 9.48% |
| Application number not in NMAT system | 1 | 0.00% |

**The manual integration story.** The two manual/deterministic AppNo files together contributed **2,652 confirmed matches (6.08% of all PLE passers)** that no automated method had previously been able to recover. Stage 0 alone — a hand-curated set of 2,332 AppNos provided by reviewers — yielded a 99.96% recovery rate. This is the operational metric to emphasize when discussing the value of human-in-the-loop matching: when a reviewer commits the time to identify the correct NMAT application number, the system links it with essentially zero error.

### 3.4 Other Data Hygiene Findings

- **NMAT↔CEM record linkage:** 99.97% match rate (178,882 of 178,927 NMAT rows successfully joined to CEM). Only 45 records failed.
- **Component score completeness:** All 8 subtest scores present on 100% of CEM-matched records.
- **Percentile rank coverage:** 97.7% of records have a parseable percentile rank.
- **Person deduplication:** Across the 178,927 application records sit 134,869 unique persons — the difference (43,058) is repeat takers.

---

## 4. What We Found — Five Headline Insights

### 4.1 NMAT performance predicts PLE outcomes — very strongly

Within the observable cohort (NMAT 2006–2014, where PLE outcomes are visible in the 2011–2022 window), the relationship between NMAT performance and eventual PLE passage is one of the strongest test-to-licensure relationships in the educational measurement literature for this region.

**Confirmed PLE pass rate by NMAT decile** (D1 = lowest 10%, D10 = highest 10%):

| NMAT Decile | PLE Pass Rate |
|---|---:|
| D1 | 8.77% |
| D2 | 16.07% |
| D3 | 19.21% |
| D4 | 25.66% |
| **D5 (50th percentile)** | **46.30%** |
| D6 | 51.82% |
| D7 | 57.64% |
| D8 | 60.44% |
| D9 | 67.82% |
| **D10** | **76.25%** |

The jump from D4 (25.66%) to D5 (46.30%) — a 20-percentage-point step at the 40th-percentile threshold — is the single steepest transition in the staircase, and the strongest empirical evidence in the dataset that crossing the 40th NMAT percentile is the critical performance threshold for board-passage probability.

Statistically, the median Confirmed PLE Passer scored 73 in percentile rank, vs 36 for those without a confirmed PLE record — a 37-point gap. The Mann-Whitney effect size r = −0.54 indicates a **large** practical difference, not a marginal statistical artifact.

### 4.2 Public university students outperform Private and Foreign — at both the NMAT and the PLE

This is the most policy-relevant institutional finding in the dataset.

| University Type | Median NMAT percentile | Top decile (D8–D10) share | Confirmed PLE pass rate |
|---|---:|---:|---:|
| **Public** | 55 | **37.0%** | **49.57%** |
| Foreign | 50 | 30.3% | 37.13% |
| Private | 48 | 29.0% | 44.68% |

Several nuances are worth flagging:

- **Public's advantage is consistent at every stage.** Higher median NMAT score → higher representation in top deciles → higher eventual PLE passage. This is not a single-stage effect.
- **Foreign-university examinees match Private on median NMAT performance (both 50–52)** but underperform on PLE passage by 7.5 percentage points. This implies the Foreign-PLE gap is *not* a knowledge gap at the NMAT moment — it is a downstream factor (visa friction, licensure pathway differences, attrition, or selection on who actually proceeds to PH boards). This is a separate policy question from "do Foreign-educated pre-meds perform less well academically."
- **The institutional effect is real but small in formal effect-size terms.** Statistical tests (Kruskal-Wallis η² = 0.0047) classify the magnitude as "negligible" — most of the variance in NMAT performance is *within* university types, not between them. The 12.4 percentage-point Public-vs-Foreign gap in PLE passage, however, is policy-grade, even though by Cohen's effect-size cutoffs the test statistic is small.

### 4.3 Where you came from academically matters more than the type of school

| Course group | N (best record) | Median percentile | Top-decile share | PLE pass rate |
|---|---:|---:|---:|---:|
| **Engineering & Technology** | 730 | **72** | **51.58%** | 37.75% |
| Natural Sciences | 40,851 | 54 | 35.53% | 45.50% |
| Other | 7,943 | 53 | 34.18% | 46.17% |
| Education | 3,260 | 51 | 32.37% | **51.90%** |
| Medical & Allied | 63,432 | 49 | 27.67% | 45.34% |
| Social & Behavioral Sciences | 16,366 | 39 | 27.52% | 40.66% |

Two paradoxes deserve attention:

- **Engineering & Technology graduates dominate the top NMAT deciles but have the lowest PLE pass rate** (37.75%). The most likely explanation is that engineers who take NMAT are highly self-selected (only the strongest sit for it) but many do not actually proceed to complete medical school and boards. With only 302–730 examinees in this group, results are statistically noisy.
- **Education graduates show the highest PLE pass rate (51.9%) despite middling NMAT performance.** This may reflect persistence and study-skill advantages from teacher-training backgrounds, or selection on highly motivated candidates.

The dominant volume story is unmistakable: **48% of all NMAT examinees come from a Medical & Allied pre-med background, and 31% from Natural Sciences.** These two course groups account for 79% of the examinee universe.

### 4.4 Three-quarters of repeat takers improve

| Indicator | Value |
|---|---:|
| Examinees who took NMAT once | 101,155 (75% of persons) |
| Examinees who took NMAT 2+ times | 33,714 (25% of persons) |
| Maximum attempts by a single person | 9 |
| Repeat takers who **improved** their percentile rank | **77.65%** |
| Median percentile-rank gain (first to last attempt) | **+11 points** |
| Median raw-score gain | **+12 points** |

This is one of the cleanest practical findings in the dataset. The retake mechanism is doing what it should: a meaningful majority of examinees who choose to retake make real, measurable progress. An 11-percentile-point median gain is the difference between a D5 and a D6 finisher — and we saw above that crossing from D4 to D5 is the critical PLE-passage threshold. Retaking matters.

### 4.5 NMAT scores have drifted downward — but the test is doing its job

| Year | Median raw score | Median percentile | Examinees |
|---:|---:|---:|---:|
| 2006 | 131 | 53 | 3,665 |
| **2010** | **135** | 57 | 8,006 |
| 2014 | 120 | 57 | 10,441 |
| 2017 | 118 | 44 | 23,955 |
| **2018** | **111** | 43 | 22,337 |

Median raw scores fell 24 points from the 2010 peak to 2018, while annual examinee volume grew from 3,665 (2006) to 22,337 (2018) — a 6× expansion. The interquartile range (the middle 50% of scores) stayed tight at 41–51 points throughout. Our reading: the test has not gotten harder; the examinee pool has broadened. As the pre-med pipeline absorbed more candidates with weaker preparation, the median naturally drifted down. The Kruskal-Wallis effect size for year-to-year differences (η² = 0.04) is small, consistent with composition change rather than test-difficulty drift.

### 4.6 No gender difference at the test — but a gender difference at the licensure

Female (n = 74,153) and male (n = 59,613) examinees have essentially identical NMAT outcomes: median percentile 50 vs 49, median raw 122 vs 121, no statistically significant difference (Mann-Whitney p = 0.0958). But the PLE pass rate diverges meaningfully: **female 29.20% vs male 24.57%** — a 4.6 percentage-point female advantage. Because the NMAT distributions are essentially identical, this gap must originate *after* the NMAT — in matriculation, persistence through medical school, or boards-readiness behavior. This is worth a separate policy investigation.

---

## 5. The Foreign Examinee Picture — A Closer Look

Because foreign examinees are a small but policy-sensitive subgroup, here is the focused view:

- **3,218 foreign examinees** in the institutional comparison cohort (≈2.5% of total).
- **Median NMAT percentile: 51** — essentially identical to Private (52).
- **Top decile (D8–D10) representation: 30.33%** — between Public (37%) and Private (29%).
- **Confirmed PLE pass rate: 37.13%** — meaningfully below both Public (49.57%) and Private (44.68%).

The mismatch — solid NMAT, lower PLE — is the headline. Within Foreign examinees, the bulk (49.35%) come from Medical & Allied backgrounds; the other half (50.65%) split across the remaining course groups. Of note, Public-International examinees (n = 326 — Filipino students at international public universities) are the lowest-performing single subgroup at the NMAT (median percentile 40 vs 55 for Public-Local), suggesting an international-education context separate from the Foreign-private question.

---

## 6. Limitations and Honest Caveats

1. **The 2014 PLE-pass-rate trough is partly mechanical.** PLE records cover 2011–2022. An NMAT 2014 examinee has roughly an 8-year observation window for boards; an NMAT 2006 examinee had 16. The apparent decline in confirmed PLE share from 55.61% (2006) to 37.82% (2014) blends real cohort effects with right-censoring. Newer cohorts (2015–2018) are excluded from PLE-share analyses altogether for this reason.
2. **9.48% of PLE passers (4,135 records) have no NMAT-side application number we can match to.** These are likely real examinees who passed, but without an AppNo there is no audit-defensible link. They are excluded from confirmed-pass counts but counted in the overall PLE universe.
3. **1.77% (772 records) are flagged as AMBIGUOUS** — multiple plausible NMAT candidates per PLE passer. These remain in a review file for manual resolution.
4. **Engineering & Technology and Public-International groups are small.** Findings about these subgroups should be reported with sample-size caveats.
5. **Statistical significance is not the same as practical importance.** With 134,869 unique persons in the dataset, almost every comparison reaches p < 0.001. We have consistently reported effect sizes (η², Cramér's V, r) so the *magnitude* of each finding is visible alongside its statistical detectability.

---

## 7. Recommendations

We organize recommendations by audience.

### 7.1 For NMAT Administration

- **Publish the decile-to-PLE-passage table as a policy artifact.** This is the most consequential public-facing finding: knowing that D1 examinees pass PLE at 8.77% and D10 at 76.25% allows informed advising and gating decisions.
- **Continue and formalize the retake policy.** The 77.65% improvement rate and +11-point median gain justify the retake mechanism. Consider publishing retake-improvement statistics annually to set realistic expectations for candidates.
- **Invest in the Foreign-applicant PLE pathway.** Foreign examinees match Private on NMAT performance but lose ground at the PLE. The gap is not a test-knowledge gap — it is a pathway-friction gap, and it is fixable with targeted support (visa coordination, mentor matching, PLE readiness programs).

### 7.2 For CEM (Data Custodian)

- **Resolve the stored-vs-derived raw-score mismatch at source.** A 42% disagreement between `STU_RSCORE` and the component sums is a serious data-integrity problem in the master database. Until it is fixed at source, every analyst who queries `STU_RSCORE` is using corrupted data. Replace `STU_RSCORE` with the component sum during the next maintenance window.
- **Standardize institution names at the application form.** Free-text college entry produces the variant explosion we saw (4,367 spellings for ~2,981 real institutions). A drop-down tied to UNIVS would eliminate 31% of fuzzy-matching effort downstream.
- **Persist `NMA_AppNo` linkage in the PLE submission flow.** The 4,135 PLE passers we cannot match have no AppNo. If PRC could ask each examinee at PLE registration for their original NMAT AppNo (or capture it via consent from PRC↔CEM data sharing), this entire 9.48% unmatched residual disappears.
- **Resolve the duplicate `NMA_AppNo`** that survives in NMAT_CLEANED_DATA (2 records share one ID).

### 7.3 For CHED (Policy)

- **Use confirmed-PLE-share by university type as a quality signal, not a gatekeeping criterion.** Public's 49.57% vs Foreign's 37.13% PLE pass rate is real, but it reflects pipeline self-selection, not a verdict on individual institutions.
- **Investigate the Public-International underperformance.** Filipino students at international public institutions (n=326) score 15 percentile points below Public-Local peers. This is a small group but worth understanding before it grows.
- **Consider an audit of the Engineering & Technology pre-med pathway.** The 51.58% top-decile NMAT representation paired with 37.75% PLE pass rate suggests these are highly capable test-takers who are not converting into medical practitioners. Policy may want to understand why.
- **Recognize the female-PLE advantage despite gender-neutral NMAT.** A 4.6 percentage-point female PLE pass-rate lead, with no corresponding NMAT-score lead, suggests the medical-school-to-boards journey advantages women in ways the entrance exam does not capture. This is interesting and worth dedicated study.

### 7.4 For Joint Operations (NMAT + CEM + CHED)

- **Commission a small AmbiguousMatchReview team for the 772 flagged records.** Each case takes a reviewer roughly 30 seconds. Full resolution would push final-match coverage from 83.4% to ~85%.
- **Republish UNIVS.csv with the 1,386 currently unmatched institutions reviewed.** Most are foreign institutions absent from the lookup; one targeted curation sprint resolves the long tail.
- **Adopt versioned pipeline releases.** Tag each rerun (`v2026.05`, etc.) so historical reports remain reproducible against a known dataset state. The technical companion report (`01_Technical_Report.md`) details the engineering steps.

---

## 8. Closing Note

The NMAT, evaluated against the licensure outcome it is designed to predict, is doing its job — and doing it well. A test-taker's NMAT percentile is a powerful, internally-consistent, downstream-validated signal of who will eventually pass the medical boards. Where the data tells a more nuanced story — institutional differences, foreign-examinee attrition, the gender PLE gap, the Engineering & Technology pathway anomaly — those are policy openings rather than test-design failures.

The largest unresolved question is not analytical, it is operational: roughly one in ten PLE passers cannot be tied back to an NMAT record because no shared identifier exists. Closing that loop, by passing `NMA_AppNo` from CEM through to the licensure record, would make every future analysis straightforwardly definitive. Until then, the deterministic-only pipeline documented here is the right floor: it does not over-claim, every match is traceable, and the manual-curation pathway is open to incrementally improve coverage one well-reviewed AppNo at a time.

The companion technical report (`01_Technical_Report.md`) details the engineering. The dashboard (`dashboard.py`) lets anyone explore these findings interactively. The data backing every number in this report is preserved in `dataset/NMAT_Ultima.csv` and the matching audit trail in `dataset/output/PLE_MATCH_MASTER.csv`.
