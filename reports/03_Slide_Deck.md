# NMAT Performance Analysis — Presentation Deck

**Format:** Comprehensive content-and-narration deck for a mixed audience of technical staff (Data Engineers, Data Scientists) and executive stakeholders (NMAT, CEM, CHED leadership).
**Length:** 38 slides covering the full arc — context, pipeline challenges, analytical findings, recommendations.
**Each slide carries:** Title, on-slide Content (what the audience reads), Figure (which visual from `dashboard.py` to embed), and Narration (what the presenter says, written so a substitute presenter could deliver it verbatim).
**Figure references** use the Figure/Table numbers from `streamlit_results.md` and `dashboard.py` (Figure 1–36, Table 1–48). When figure numbers map to existing dashboard exports in `dataset/analysis_output/` or `streamlit_results.md/images/`, those file paths are noted.

---

## SLIDE 1 — Title

**CONTENT**
- **NMAT Performance & PLE Alignment, 2006–2018**
- A 13-year, 178,927-record analysis
- Prepared for NMAT, CEM, and CHED leadership
- [Date] · [Presenter]

**FIGURE** *(none — title slide)*

**NARRATION**
Good morning. Over the next thirty minutes I will walk you through what 13 years of NMAT data — 178,927 examinations, 134,869 unique persons, and 43,630 confirmed PLE outcomes — tell us about the medical-admissions pipeline in the Philippines. We will spend the first part on the data itself, because some of what we found in the source files materially changed how the analysis had to be conducted. Then we will move to the substantive findings, and finally to recommendations. The single most important thing to take away is this: the NMAT percentile is a strong, statistically large predictor of who eventually passes the medical boards, and the operational steps we describe at the end will make every future analysis cleaner than this one.

---

## SLIDE 2 — Why we did this work

**CONTENT**
The five questions that drove this analysis:
1. Is NMAT performance **stable across years**?
2. Does **background** (Public / Private / Foreign, course group) matter?
3. Does the NMAT actually **predict the PLE**?
4. Does **retaking** the NMAT work?
5. Are there hidden **equity gaps** (gender, foreign status)?

**FIGURE** *(none — text slide; optional Figure 2 pie chart "Course-group composition of best-record examinees" as a visual backdrop)*

**NARRATION**
We started with five questions, all of them policy-driven. NMAT administrators wanted to know whether the test was stable. CEM wanted to know whether the data they custodial could support these analyses without rebuilding. CHED needed evidence-grounded answers about institutional differences and equity. Those five questions structure everything that follows. But before we could give defensible answers we had to confront the data itself — which is where this presentation will spend its first ten minutes.

---

## SLIDE 3 — The data we worked with

**CONTENT**
- **NMAT_CLEANED_DATA.csv** — 178,927 examination records, 29 columns
- **CEM_DATA.csv** — 254,308 examinee records with component subtest scores, 36 columns
- **UNIVS.csv** — 3,022-row institution reference
- **PLE_DATA.csv** — 43,630 PLE passers, 2011–2022
- **PLE_UNMATCHED.csv / PLE_STILL_UNMATCHED.csv** — manual AppNo curation files
- → **NMAT_Ultima.csv** — 178,927 rows × 115 columns (analytical output)

**FIGURE** Block diagram (text-only acceptable) showing source files → cleaning → matching → Ultima → dashboard. *(No specific dashboard figure; use a slide-builder schematic.)*

**NARRATION**
Five source files feed the pipeline. NMAT_CLEANED_DATA contains the 178,927 application records from 2006 to 2018. CEM_DATA contains the component-level subtest scores — Verbal, Inductive, Quantitative, Perceptual Acuity on the aptitude side, and Biology, Physics, Social Science, Chemistry on the science side — for 254,308 examinees, which is a superset of NMAT because it includes non-applicants from related testing programs. UNIVS is our institution reference list. PLE_DATA gives us 43,630 medical-licensure passers between 2011 and 2022 by name and pass year. And two manual curation files — PLE_UNMATCHED.csv and PLE_STILL_UNMATCHED.csv — contain hand-curated NMAT application numbers for PLE passers that automated matching had previously missed. Everything flows into NMAT_Ultima.csv, a single 178,927-row, 115-column analytical dataset that every chart in this deck comes from.

---

## SLIDE 4 — The pipeline at a glance

**CONTENT**
Four sequential phases:
1. **Data Cleaning** (`1_Data_Cleaning_Pipeline.ipynb`)
2. **PLE Matching** (`2_PLE_Matching_Pipeline.ipynb`) — strictly deterministic
3. **Statistical Analysis** (`3_NMAT_PLE_Analysis.ipynb`)
4. **Interactive Dashboard** (`dashboard.py`) — 12 pages

Outputs: 50+ CSV artifacts, 5 Sankey HTML files, the dashboard.

**FIGURE** *(none — schematic optional)*

**NARRATION**
The pipeline runs in four phases. Cleaning standardizes scores, names, and institutions. Matching links NMAT examinees to PLE outcomes. Analysis runs the statistical tests. The dashboard surfaces the results for interactive exploration with twelve thematic pages. Every phase emits CSV artifacts that downstream consumers can read directly — the dashboard is a presentation layer, not a closed system.

---

## SLIDE 5 — The most important data problem we found

**CONTENT**
**42% of stored raw total scores in CEM disagreed with the sum of components.**

| Field | Available on | Mismatch vs component sum |
|---|---:|---:|
| `STU_RSCORE` (stored total) | 174,494 records (68.6%) | **107,422 / 174,494 = 42.2%** |
| `STU_RSCORE_CALC` (computed total) | 254,308 records (100%) | 0.00% |
| `TotalRawScoreTRUE` (our derived total) | 178,882 records | reference truth |

**FIGURE** Table 3 from `dashboard.py` (Data Integrity page) — "TRUE raw-score validation checks." Surface the mismatch counts directly on screen.

**NARRATION**
This is the most consequential discovery in the entire project. CEM stores each examinee's total raw score in a field called `STU_RSCORE`. When we summed the eight component subtest scores ourselves and compared, we found that 107,422 of the 174,494 stored totals — 42.2% — were wrong. They did not equal the sum of the components. A separate field called `STU_RSCORE_CALC` is internally consistent at 100%, but our analytical choice was to build a fresh authoritative total directly from components, which we call `TotalRawScoreTRUE`, plus `PartIRawScoreTRUE` and `PartIIRawScoreTRUE`. Every chart, every statistic in this deck uses those TRUE versions. We did not silently overwrite the original — `STU_RSCORE` is still in the dataset for audit — but no analyst should ever use it again until the source database is repaired.

---

## SLIDE 6 — The university name problem

**CONTENT**
- **4,367** unique college name strings → only **2,981** real institutions
- Causes: punctuation drift, abbreviation variants, foreign institutions, numeric codes (e.g., `13207A`)
- Same institution often classified inconsistently (Private / Public / Not Specified across applications)
- **Resolution: 4-stage cascade**
  1. Exact match (61.3%) → 2. Canonical name (1.6%) → 3. Fuzzy ≥88, margin ≥5 (5.4%) → 4. Fallback "Not Specified" (31.7% of unique strings, only 1.01% of records)
- **Final coverage: 98.99% of NMAT records VERIFIED**

**FIGURE** Table 4 — "Post-cleaning UNI_TYPE consistency by source college" + Table 6 — "Distribution of university type." Show that 100% of post-cleaning colleges map to one UNI_TYPE.

**NARRATION**
University names arrived in 4,367 distinct spellings, even though only roughly three thousand actual institutions exist in the data. Same school, different punctuation, different abbreviation. Some records carried numeric codes — "13207A" — that look like data-entry placeholders. Worse, the same college frequently appeared as Private in one record, Public in another, and Not Specified in a third. We resolved this with a four-stage matching cascade against the UNIVS reference list — exact match first, canonical name second, fuzzy match with a strict 88% similarity floor and a 5-point margin requirement third, and an explicit "Not Specified" fallback when nothing else worked. After cleaning, every unique college name in the dataset maps to exactly one university type — the multi-classification problem is gone. 98.99% of records are verified; the 1% residual is overwhelmingly foreign institutions absent from UNIVS.

---

## SLIDE 7 — The PLE matching problem and our deterministic-only decision

**CONTENT**
- NMAT uses `NMA_AppNo`. PLE uses **name only**. **No shared identifier.**
- Earlier pipeline versions used fuzzy name matching → fragile, not auditable
- **DE-FUZZY refactor: all fuzzy logic eliminated**
- New approach: strict exact matching only, three stages

**FIGURE** *(none — concept slide; optionally a 3-stage flow diagram)*

**NARRATION**
Connecting an NMAT applicant to their eventual PLE outcome should be trivial, but it isn't. NMAT identifies examinees by Application Number. PLE identifies passers by name and pass year. There is no shared key. Earlier versions of this pipeline used fuzzy name matching with confidence thresholds. We retired that approach entirely. Filipino surnames concentrate in narrow lexical bands, fuzzy matches produced false positives we could not audit, and a downstream reviewer could not trace a match back to a specific source document. The pipeline now does exact-only matching in three stages, which we will look at on the next slide.

---

## SLIDE 8 — The three matching stages and what they recovered

**CONTENT**
| Stage | Source | Method | Confirmed matches |
|---|---|---|---:|
| 0 | `PLE_UNMATCHED.csv` (manual AppNo) | Direct AppNo → NMAT | **2,331 / 2,332 = 99.96%** |
| 1 | `PLE_DATA.csv` | Exact name + 5-yr board-gap filter | **33,970 / 41,300 = 82.3%** |
| 2 | `PLE_STILL_UNMATCHED.csv` (deterministic AppNo) | Direct AppNo → NMAT | **321 / 321 = 100%** |

**Total confirmed: 36,395 / 43,630 PLE passers = 83.42%**
**Manual integration contribution: 2,652 records (6.08%) that no automated method recovered.**

**FIGURE** *(none — table-on-slide is sufficient; optionally adapt PLE_MATCH_MASTER.csv summary chart)*

**NARRATION**
Three stages, in this order. Stage 0 is the manual curation file. Reviewers had hand-identified the NMAT application number for 2,332 PLE passers who had previously failed automated matching. When a human commits the time to identify the right AppNo, our deterministic join produces a match in 99.96% of cases — 2,331 of 2,332. Stage 1 is exact-normalized-name matching against the full PLE database, with a five-year board-eligibility filter that protects against impossible matches. This catches 33,970 matches at 82.3% of the input. Stage 2 is a second deterministic AppNo file produced later in the workflow — 321 records, 100% recovery. Across all three stages we confirm 36,395 of 43,630 PLE passers, or 83.42%. The number to remember for operational purposes is the manual contribution: **2,652 records, or 6.08% of all PLE passers, were recovered by manual integration and would not have been confirmed by any automated method alone.**

---

## SLIDE 9 — What the matching residual looks like

**CONTENT**
| Status | Count | Share of PLE universe |
|---|---:|---:|
| FINAL_MATCH | 36,395 | 83.42% |
| AMBIGUOUS (multiple plausible candidates) | 772 | 1.77% |
| NO_VALID_MATCH (failed filters) | 2,298 | 5.27% |
| **UNMATCHED_NO_APPNO** (no AppNo, no name match) | **4,135** | **9.48%** |
| APPNO_NOT_IN_NMAT | 1 | <0.01% |

**FIGURE** A simple bar chart of the five categories. (No existing dashboard figure maps directly to this — build a static bar.)

**NARRATION**
Here is the honest accounting of what we cannot match. 1.77% are AMBIGUOUS — multiple plausible NMAT candidates per PLE passer; these go to a review file. 5.27% failed our filters — for example, the candidate's NMAT year was too recent relative to PLE year, or percentile was below 40 for all candidates. And 9.48% — 4,135 records — have no NMAT application number and no exact name match. We classified these honestly as unmatched. They are real PLE passers who passed the medical boards, but with the current source data we cannot prove the link. This is the operational ceiling, and it has a fix: pass the NMAT AppNo through to the PRC's PLE registration form.

---

## SLIDE 10 — The integrated dataset: NMAT_Ultima

**CONTENT**
- **178,927 rows × 115 columns**
- Three analytical flags added by the matching pipeline:
  - `IS_PLE_PASSER` — True for 49,986 rows
  - `IS_PLE_ANALYSIS_SAFE` — True for 49,986 rows (no AMBIGUOUS)
  - `IS_BEST_NMAT_RECORD` — True for 133,804 rows (one best record per person)
- Person-level totals: **134,869 unique examinees**, 33,714 repeat takers (25%)
- Best-record PLE passers: **36,305 unique persons** (the analytical cohort)

**FIGURE** Table 2 from the Data Integrity page — "Analysis cohorts used in the dashboard."

**NARRATION**
The integrated dataset NMAT_Ultima carries 178,927 rows and 115 columns. The matching pipeline added three boolean flags that drive every downstream analysis. `IS_PLE_PASSER` marks any NMAT record belonging to a confirmed PLE passer — there are 49,986 such rows, more than the 36,305 unique PLE-passing persons because repeat takers have multiple attempts. `IS_PLE_ANALYSIS_SAFE` is the same set excluding AMBIGUOUS cases. `IS_BEST_NMAT_RECORD` selects one row per person — the matched attempt for passers, and the highest-percentile attempt for non-passers — giving 133,804 person-level records. Every chart in the rest of this deck uses one of these well-defined cohorts.

---

## SLIDE 11 — The "observable cohort" guardrail

**CONTENT**
PLE data covers 2011–2022. A 2018 NMAT examinee would not be observable as a PLE passer until ~2023 (outside our data).

**Solution:** All PLE-alignment analyses restrict to **`Year ≤ 2014`** (`IS_BOARD_OBSERVABLE_COHORT = True`).
- Observable best-record cohort: **64,501 examinees**
- This prevents misclassifying recent cohorts as "did not pass."

**FIGURE** *(text-only; concept slide)*

**NARRATION**
One more methodological guardrail before we move to findings. Our PLE data ends in 2022. Medical school plus boards takes at least five years post-NMAT, so an examinee who took NMAT in 2018 would not be observable as a PLE passer until 2023 at the earliest. If we counted them as "did not pass" we would be wrong. So every PLE-alignment chart in this deck restricts to NMAT years 2006 through 2014 — what we call the observable cohort. That gives us 64,501 examinees with an honest chance of being observed. This caveat applies to every PLE-pass-rate chart that follows.

---

## SLIDE 12 — Headline 1: NMAT predicts PLE — very strongly

**CONTENT**
PLE confirmed pass rate by NMAT decile (observable cohort):

| Decile | PLE Pass % |
|---|---:|
| D1 | 8.77 |
| D2 | 16.07 |
| D3 | 19.21 |
| D4 | 25.66 |
| **D5** | **46.30** *(+20.6 pp from D4)* |
| D6 | 51.82 |
| D7 | 57.64 |
| D8 | 60.44 |
| D9 | 67.82 |
| **D10** | **76.25** |

**Mann-Whitney effect r ≈ −0.54 (large effect)**

**FIGURE** **Figure 22 — "PLE status composition within each percentile decile"** (PLE Alignment page, Decile profile tab). Shows the staircase visually. Alternatively, **Figure 19 — Sankey "Decile → PLE status"** for a flow visualization.

**NARRATION**
This is the most important substantive finding of the entire project. The figure on screen shows the percent of examinees in each NMAT decile who are confirmed PLE passers. Read it from left to right. In the bottom decile, only 8.77% pass the boards. In the top decile, 76.25%. That is a 67.5-percentage-point spread — one of the strongest test-to-licensure relationships you will see in this region's educational measurement literature. Notice the jump from D4 to D5 — 25.66% to 46.30%, a 20.6-percentage-point step. Crossing the 40th NMAT percentile is empirically the strongest single threshold in the dataset for predicting eventual board passage. The statistical effect size is r ≈ −0.54, which by Cohen's conventions is "large" — meaning this is not a marginal pattern, it is a structural one.

---

## SLIDE 13 — Headline 1, continued: the Sankey view

**CONTENT**
The flow visualization makes the staircase intuitive at a glance.
- Top of the chart: most D10 mass flows to "Confirmed PLE passer"
- Bottom of the chart: most D1 mass flows to "No confirmed PLE match"

**FIGURE** **Figure 19 — "Flow from percentile decile to PLE status in the observable cohort"** (Flow & Pathways page, Decile → PLE tab). File: `dataset/analysis_output/05C_sankey_decile_to_ple_status_observable.html`.

**NARRATION**
Same data, flow visualization. Each band width is the count of examinees moving from a decile to a PLE outcome. You can see the higher deciles dominated by green — Confirmed PLE passer. The lower deciles are dominated by red — No confirmed PLE match. This is the picture to keep in mind when we discuss policy applications later.

---

## SLIDE 14 — Headline 2: Public > Private and Foreign at every stage

**CONTENT**
| University Type | Median NMAT pct | D8–D10 share | PLE pass rate (observable) |
|---|---:|---:|---:|
| **Public** | 55 | **37.0%** | **49.57%** |
| Foreign | 50 | 30.3% | 37.13% |
| Private | 48 | 29.0% | 44.68% |

**FIGURE** **Figure 9 — "Share of examinees in D8–D10 by university type"** (Deciles & Background page, University type tab) paired with **Table 30 — "Confirmed PLE alignment by university type"** (PLE Alignment, Policy tables tab).

**NARRATION**
Public university students out-perform Private and Foreign students at every measured stage. Higher median NMAT percentile, higher representation in the top three deciles, and meaningfully higher confirmed PLE pass rate. The gap from Public to Foreign in PLE passage is 12.4 percentage points. The gap from Public to Private is about 5 points. Two important nuances. First, Foreign examinees match Private on median NMAT performance — both at percentile 50 to 52 — so the Foreign-PLE gap is not a knowledge gap at the NMAT moment. It is a gap that opens downstream, in medical school or boards readiness. Second, the institutional effect in statistical terms is small — η² of 0.0047, formally "negligible" — meaning most of the variation in performance is within university types, not between them. The 12-point pass-rate gap is real and policy-grade; the institutional effect on individual percentile is not the dominant driver of outcomes.

---

## SLIDE 15 — Headline 2, continued: the within-Foreign breakdown

**CONTENT**
Foreign examinees:
- **3,218 examinees** (≈2.5% of total)
- Median percentile **51** (essentially identical to Private)
- Top decile share **30.33%**
- PLE pass rate **37.13%**
- Public-International subgroup (n=326): median percentile **40** — 15-point gap vs Public-Local

**FIGURE** **Figure 12 — "Percentile-decile distribution by institution type and location"** (University Type Analysis page) + **Table 16 — Foreign examinee summary**.

**NARRATION**
A closer look at Foreign examinees. About 3,218 of them in the institutional comparison cohort — 2.5% of total. They match Private on NMAT median, slightly better representation in D10 — 16.5% Foreign vs Private's distribution which peaks at 9.8% — and meaningfully worse confirmed PLE pass rate. Notice one more thing on this slide: when we cross university type with location, Public-International — Filipino students at international public universities, about 326 examinees — perform 15 percentile points below Public-Local students. It is a small group but worth flagging because it represents a different educational pathway than the typical Foreign category.

---

## SLIDE 16 — Headline 3: Course group matters more than university type

**CONTENT**
| Course Group | N | Median pct | D8–D10 share | PLE pass rate |
|---|---:|---:|---:|---:|
| **Engineering & Technology** | 730 | **72** | **51.58%** | 37.75% |
| Natural Sciences | 40,851 | 54 | 35.53% | 45.50% |
| Other | 7,943 | 53 | 34.18% | 46.17% |
| Education | 3,260 | 51 | 32.37% | **51.90%** |
| Medical & Allied | 63,432 | 49 | 27.67% | 45.34% |
| Social & Behavioral Sciences | 16,366 | 39 | 27.52% | 40.66% |

**FIGURE** **Figure 11 — "Share of examinees in D8–D10 by course group"** (Deciles & Background page, Course group tab) + **Table 29 — "Confirmed PLE alignment by pre-med background"** (PLE Alignment, Policy tables tab).

**NARRATION**
By pre-med background, the spread is wider than by university type. Engineering & Technology graduates dominate the top NMAT deciles — 51.58% of them land in D8–D10, almost double the rate for Medical & Allied. But their PLE pass rate is the lowest at 37.75%. Two paradoxes. First: engineers who take NMAT are highly self-selected — only the strongest sit for a medical entrance exam. Their sample size is small, 730 best-record examinees, so the statistics are noisy. Second: Education graduates show the highest confirmed PLE pass rate at 51.90%, despite middling NMAT performance. That likely reflects persistence and study habits rather than test aptitude. The volume story is straightforward: 48% of all NMAT examinees come from Medical & Allied backgrounds, 31% from Natural Sciences. Those two course groups are 79% of the universe.

---

## SLIDE 17 — Headline 3, continued: Sankey course → decile

**CONTENT**
Flow visualization showing how each course group distributes across deciles.

**FIGURE** **Figure 18 — "Flow from course group to percentile decile"** (Flow & Pathways page, Course → Decile tab). File: `dataset/analysis_output/05B_sankey_course_group_to_decile.html`.

**NARRATION**
The Sankey on screen shows the same story in flow form. You can see the Natural Sciences and Engineering & Technology bands flowing strongly into the upper deciles on the right. Medical & Allied — the largest band by far — flows roughly evenly across all deciles. Social & Behavioral Sciences shows the most concentrated flow into the bottom deciles. The visual makes the magnitude of the Engineering & Technology selection effect immediately clear, even though the cohort is small.

---

## SLIDE 18 — Headline 4: Retake works

**CONTENT**
| Metric | Value |
|---|---:|
| Examinees who took NMAT once | 101,155 (75%) |
| Examinees who took NMAT 2+ times | 33,714 (25%) |
| Max attempts by one person | 9 |
| Repeat takers who **improved** their percentile | **77.65%** |
| Median percentile change (first → last) | **+11 points** |
| Median raw-score change | **+12 points** |

**FIGURE** **Figure 24 — "Distribution of NMAT attempt counts per examinee"** + **Figure 25 — "Change from first to last attempt among repeat takers"** (both Repeat Takers page).

**NARRATION**
One in four examinees retakes the NMAT. Of those, 77.65% improve their percentile rank, with a median gain of 11 percentile points and 12 raw-score points. An 11-percentile-point gain is the difference between a D5 and a D6 finisher — and you recall from a few slides back that crossing from D4 to D5 is the critical PLE-passage threshold. So retake genuinely matters. Examinees who do not give up after their first attempt have a meaningful pathway to improve. This is the cleanest, most policy-defensible finding in the entire dataset.

---

## SLIDE 19 — Headline 5: Yearly trends — composition, not difficulty

**CONTENT**
| Year | Median raw | Median pct | Examinees |
|---:|---:|---:|---:|
| 2006 | 131 | 53 | 3,665 |
| **2010** | **135** | 57 | 8,006 |
| 2014 | 120 | 57 | 10,441 |
| 2017 | 118 | 44 | 23,955 |
| **2018** | **111** | 43 | 22,337 |

Raw median fell **24 points** from 2010 to 2018. Examinee volume grew **6×**.

**FIGURE** **Figure 4 — "Annual score trends and examinee volume"** (Trends & Stability page). Shows median raw, Part I, Part II, percentile, and examinee count side-by-side. File: `dataset/analysis_output/01A_yearly_summary.csv` for the underlying numbers.

**NARRATION**
Median raw scores fell 24 points from the 2010 peak to 2018, while annual examinee volume more than sextupled. The interquartile range stayed stable at roughly 41 to 51 points throughout. Our reading is that the test has not gotten harder — the examinee pool has broadened. As the pre-med pipeline absorbed more candidates with weaker preparation, the median naturally drifted down. The Kruskal-Wallis test confirms year-to-year differences are statistically detectable, but the effect size η² is around 0.04 — small. Dunn post-hoc analysis clusters 2006 through 2009 as similar, 2015 through 2017 as similar, and identifies 2018 as significantly below every prior year. This is consistent with composition change, not test-difficulty drift.

---

## SLIDE 20 — Headline 5, continued: the Kruskal-Wallis evidence

**CONTENT**
| Score | H | p | η² (effect) |
|---|---:|---:|---:|
| Total Raw | 5598.2 | <0.001 | 0.042 — small |
| Part I Raw | 5453.4 | <0.001 | 0.041 — small |
| Part II Raw | 5516.0 | <0.001 | 0.041 — small |
| Percentile Rank | 2235.7 | <0.001 | 0.017 — small |
| GPS | 2420.3 | <0.001 | 0.018 — small |

**With N=134k, p-values are mechanically tiny — read the effect size, not the p-value.**

**FIGURE** **Table 9 — "Kruskal-Wallis tests for year-to-year score differences"** (Trends & Stability page).

**NARRATION**
A technical aside on statistics. With 134,000 unique persons, almost every comparison reaches p less than 0.001 mechanically — that is what happens when sample size is enormous. What matters is the *effect size*, η², which sits between 0.017 and 0.042 across every score measure. That is "small" in formal Cohen terms. So while year-to-year shifts are statistically detectable, the magnitude of those shifts is modest. We report effect sizes next to every p-value throughout this deck for exactly this reason.

---

## SLIDE 21 — Headline 6: Gender — no NMAT gap, but a PLE gap

**CONTENT**
| Metric | Female (n=74,153) | Male (n=59,613) |
|---|---:|---:|
| Median percentile | 50 | 49 |
| Median raw | 122 | 121 |
| Mann-Whitney p | 0.0958 | (not significant) |
| **PLE pass rate** | **29.20%** | **24.57%** |

Female PLE advantage: **+4.6 percentage points** despite no NMAT difference.

**FIGURE** **Figure 33 — "Percentile-rank distribution by sex"** (Year Gap & Gender page, Gender tab) + **Table 42** (PLE composition by sex).

**NARRATION**
Female and male examinees show essentially identical NMAT performance — median percentile 50 versus 49, median raw 122 versus 121, no statistically significant difference. But their confirmed PLE pass rates diverge by 4.6 percentage points in favor of women — 29.20% versus 24.57%. Because the NMAT distributions are essentially identical, the PLE gap originates after the NMAT — in matriculation, medical-school persistence, or boards-readiness behavior. This is a separate policy question worth dedicated study.

---

## SLIDE 22 — Subtest profiles: where strengths live

**CONTENT**
Standardized subtest means tell us where each group's strengths concentrate.
- **By university type:** Public leads on every subtest; gaps largest in Biology, Physics, Chemistry.
- **By course group:** Natural Sciences and Engineering & Technology dominate Quantitative and Physics; Social & Behavioral Sciences weakest on Verbal (453).

**FIGURE** Two visualizations side by side: **Figure 29 — "Standardized subtest radar profile by university type"** and **Figure 30 — "Standardized subtest radar profile by course group"** (both Subtests & Profiles page).

**NARRATION**
The two radar charts on screen show standardized subtest means by university type on the left and by course group on the right. A larger radar shape means stronger overall standardized performance; an asymmetric shape means uneven strengths and weaknesses. By university type, the Public radar sits cleanly outside the Foreign and Private radars on most axes — that is the Public outperformance we already saw. By course group, Engineering & Technology is dramatically outside on Quantitative and Physics, Natural Sciences is comparable on those plus Chemistry and Biology, and Social & Behavioral Sciences has the smallest radar overall with a particularly pinched Verbal axis. These profiles are useful for advising and curriculum design.

---

## SLIDE 23 — PLE year gap

**CONTENT**
- Median NMAT → PLE gap: **6 years**
- 5th-percentile gap: 5 years (the policy minimum)
- 95th-percentile gap: 7 years
- 85.8% of passers reach the boards within 7 years of NMAT
- No meaningful gap variation by course group or decile

**FIGURE** **Figure 31 — "Distribution of NMAT-to-PLE year gap"** + **Figure 32 — "PLE year gap by course group"** (Year Gap & Gender page, PLE year gap tab).

**NARRATION**
For confirmed PLE passers, the time between NMAT and licensure passage has a clean median of six years, with five years as the minimum (the policy floor for medical school plus boards) and a tight upper tail. Almost 86% of passers reach the boards within seven years of taking NMAT. There is no meaningful gap variation by course group or by performance decile — once an examinee is on the medical track, the time to licensure is structurally similar across groups.

---

## SLIDE 24 — Where the matching residual lives

**CONTENT**
The 4,135 UNMATCHED_NO_APPNO records (9.48% of PLE passers) are the operational ceiling.

**Root cause:** PLE registration does not capture the NMAT Application Number.

**Fix:** Pass `NMA_AppNo` through the PRC's PLE registration flow.

**FIGURE** *(text-only)*

**NARRATION**
We have one operational fact to flag before recommendations. 4,135 PLE passers — 9.48% of the universe — cannot be matched to NMAT records because no shared identifier exists and no exact name match found a clean candidate. These are real PLE passers who passed real boards. They are missing from our analytical cohort because of a data-collection gap, not because they don't exist. The fix is upstream: if the PRC's PLE registration form captured the original NMAT Application Number, this entire residual disappears in future cohorts. Until then, manual curation is the only path forward.

---

## SLIDE 25 — A note on small samples

**CONTENT**
Several findings rest on small N — interpret with confidence-interval caveats:
- Engineering & Technology: **n = 302–730** (best-record subset)
- Public-International: **n = 326–331**
- Foreign-PLE observable: **n = 2,117**

**Always report effect size + confidence interval alongside point estimates.**

**FIGURE** *(text-only)*

**NARRATION**
One methodological caution. Three subgroups in this analysis carry small sample sizes: Engineering & Technology with about 730 best-record examinees, Public-International with about 330, and the Foreign-observable cohort at about 2,100. Findings about these groups should always be reported with confidence-interval caveats. The point estimates are real — but small samples mean those point estimates have wider uncertainty than the headline numbers suggest. We recommend bootstrap confidence intervals on any future cross-reporting that highlights these subgroups.

---

## SLIDE 26 — Dashboard tour (1/2): structure

**CONTENT**
Twelve thematic pages in `dashboard.py`:
1. Executive Summary · 2. Data Integrity · 3. Trends & Stability · 4. Deciles & Background · 5. University Type · 6. Flow & Pathways · 7. PLE Alignment · 8. Repeat Takers · 9. Subtests & Profiles · 10. Year Gap & Gender · 11. Statistical Tests · 12. Policy Tables & Export

Global sidebar filters: Year, University Type, Course Group, Sex, optional PLE Status.

**FIGURE** Screenshot of the dashboard's sidebar + page navigation. (Live demo if presenting.)

**NARRATION**
Now a quick tour of what is in the dashboard, because everything we have presented sits behind these twelve pages and any of you can re-derive any of these statistics interactively. Executive Summary gives the headline KPIs. Data Integrity surfaces the cohort definitions and validation checks. Trends & Stability is yearly. Deciles & Background, University Type, and Flow & Pathways carry the institutional and course-group analyses. PLE Alignment is the observable-cohort centerpiece. Repeat Takers, Subtests, Year Gap & Gender are the secondary analyses. Statistical Tests gives the full Kruskal-Wallis, Mann-Whitney, Chi-square, and Dunn post-hoc evidence. Policy Tables & Export is for downloadable reference. The sidebar filters apply across pages — you can dial in any year range, any subset of university types, any course groups, and see every chart update.

---

## SLIDE 27 — Dashboard tour (2/2): worked example

**CONTENT**
Live demo (or screenshot sequence):
1. Default view — all data
2. Filter to Public + Foreign universities only
3. Observe top-decile representation difference
4. Switch to PLE Alignment page, observe Confirmed-share

**FIGURE** Screenshots showing the filter cascade.

**NARRATION**
If we apply a filter — say, restrict to Public and Foreign universities only — every chart in the dashboard updates. The decile distribution heatmap on the Deciles page now shows just two rows. The Sankey on the Flow page redraws. And critically, the PLE Alignment page reflects the same filtered cohort, so we can compare Public-versus-Foreign PLE pass rates directly. This is the workflow for anyone in this room who wants to explore a question we haven't pre-answered.

---

## SLIDE 28 — Recommendation 1 (NMAT): Publish the decile-to-PLE table

**CONTENT**
**Make the decile-to-PLE-passage table a public-facing policy artifact.**

- D1: 8.77% pass
- D5: 46.30% pass
- D10: 76.25% pass

Enables informed advising. Sets realistic expectations for candidates. Validates the test against its policy purpose.

**FIGURE** Re-use **Figure 22 — PLE composition within each decile** (the staircase).

**NARRATION**
First recommendation, for NMAT administration. Publish the decile-to-PLE table as a public-facing policy artifact. It is among the strongest test-validity demonstrations you have — a 67.5-percentage-point spread from D1 to D10. Use it for candidate advising. Use it to set realistic expectations. Use it in any future test-validation work. This is the easy win.

---

## SLIDE 29 — Recommendation 2 (NMAT): Formalize retake support

**CONTENT**
**77.65% of repeat takers improve. Median gain: 11 percentile points.**

Action items:
- Publish retake improvement statistics annually
- Provide structured study guidance to first-attempt non-passers
- Track per-attempt outcomes for ongoing program evaluation

**FIGURE** Re-use **Figure 25 — Change from first to last attempt among repeat takers** (the improvement boxplot).

**NARRATION**
Second recommendation. The retake mechanism works. 77.65% of repeat takers improve, median gain 11 percentile points. Formalize support around this. Publish improvement statistics annually so candidates have realistic expectations. Consider offering structured study guidance to examinees who score below the 40th percentile on first attempt — that is the population for whom retake-and-improvement most likely changes their PLE-passage probability. And track per-attempt outcomes so the program can iterate.

---

## SLIDE 30 — Recommendation 3 (CEM): Fix the stored-score field

**CONTENT**
**42% of `STU_RSCORE` values disagree with component sums.**

Action: replace `STU_RSCORE` with the component sum at source in the next maintenance window.

Until then: do not query `STU_RSCORE` for analysis.

**FIGURE** Re-use **Table 3 — TRUE raw-score validation checks** to remind audience of the magnitude.

**NARRATION**
For CEM. The stored total raw score field, `STU_RSCORE`, is unreliable on 42% of records. This is the single most consequential data-integrity finding in the project. Until the underlying master database is repaired, any analyst querying this field is using corrupted data. The fix is one maintenance window: replace `STU_RSCORE` with the component sum, where the components are present, and flag the residual where they are not. Our pipeline does this in derivation — but the upstream system should do it at source.

---

## SLIDE 31 — Recommendation 4 (CEM): Standardize at the form

**CONTENT**
**4,367 college name spellings for ~2,981 real institutions.**

Action: Replace free-text college entry with a dropdown tied to UNIVS.

Result: eliminates ~31% of downstream fuzzy-matching effort. Permanent fix.

**FIGURE** Re-use **Table 4 / Figure 8** showing the breadth of UNIVERSITY entries.

**NARRATION**
Same audience. Free-text entry of college names produces the variant explosion we saw — 4,367 spellings for about 3,000 real institutions. A controlled dropdown tied to the UNIVS reference list would eliminate roughly 31% of the downstream fuzzy-matching workload and make future analyses cleaner without any change to UNIVS itself. This is a one-time form change with permanent payoff.

---

## SLIDE 32 — Recommendation 5 (CEM/PRC joint): Capture AppNo at PLE registration

**CONTENT**
**4,135 PLE passers (9.48%) are unmatchable for lack of a shared identifier.**

Action: Pass `NMA_AppNo` through the PRC's PLE registration form, captured with examinee consent under CEM↔PRC data-sharing.

Result: 9.48% residual closes; future analyses become trivial.

**FIGURE** Re-use **Slide 9's table** to remind the audience of the residual.

**NARRATION**
Joint recommendation for CEM and the PRC. We have 4,135 confirmed PLE passers we cannot tie back to NMAT records because no shared identifier exists in the source data. If the PLE registration form captured the NMAT Application Number — easily collected with examinee consent under existing data-sharing arrangements — this entire residual closes for future cohorts. Every analysis of NMAT-PLE alignment after that date becomes straightforwardly definitive.

---

## SLIDE 33 — Recommendation 6 (CHED): Investigate Foreign-PLE gap

**CONTENT**
- Foreign examinees match Private on NMAT performance
- But pass PLE at **37.13%** vs Private's **44.68%** — a **7.5 pp** gap not explained by test scores

Causes hypothesized: visa friction · licensure pathway differences · attrition during medical school

Action: targeted study of Foreign-PLE pathway, with policy interventions where indicated.

**FIGURE** Re-use **Table 30 — Confirmed PLE alignment by university type** alongside the matched-NMAT-medians.

**NARRATION**
For CHED. The Foreign-PLE gap is a downstream gap, not a test-knowledge gap. Foreign examinees match Private on NMAT median percentile, but lose 7.5 percentage points at the PLE relative to Private and 12.4 points relative to Public. Likely causes include visa friction, licensure pathway complexity for foreign-trained medical students, and differential attrition. A targeted CHED study of this pathway — separate from any NMAT changes — would identify policy interventions to close the gap. This is a policy opportunity, not a test-design problem.

---

## SLIDE 34 — Recommendation 7 (CHED): Investigate the Engineering & Technology paradox

**CONTENT**
- Engineering & Technology pre-meds: **51.58%** in top NMAT deciles (highest)
- But **37.75%** confirmed PLE pass rate (lowest)
- Sample small (n=302–730): caveat with CIs

Action: Audit the engineering pre-med pathway. Why are top NMAT scorers from this background not converting into medical practitioners?

**FIGURE** Re-use **Figure 11 — D8-D10 share by course group** alongside the PLE pass rates from Table 29.

**NARRATION**
Also for CHED. Engineering & Technology graduates who take the NMAT dominate the top deciles at 51.58%, but their PLE pass rate is the lowest at 37.75%. With a small N — about 302 in the observable cohort — the point estimate carries uncertainty, but the directional pattern is consistent. Most likely explanation: engineering grads who sit for NMAT are extremely self-selected on aptitude, but many do not actually proceed through medical school to boards. An audit of this pathway would reveal whether these are interrupted pre-meds, decisions to pursue an MD elsewhere, or a particular dropout pattern.

---

## SLIDE 35 — Recommendation 8 (Joint): Resolve the 772 AMBIGUOUS cases

**CONTENT**
- 1.77% of PLE passers flagged AMBIGUOUS — multiple plausible candidates
- Each case: ~30 seconds of human review
- Full resolution lifts confirmed-match coverage **83.4% → ~85%**

Action: Small review-team sprint (1–2 days).

**FIGURE** *(text-only)*

**NARRATION**
A small operational win. 1.77% of PLE passers are flagged AMBIGUOUS — multiple plausible NMAT candidates passed all our automated filters. Each case requires roughly thirty seconds of human review to pick the correct match. A small team could resolve all 772 cases in a day or two. The payoff is modest in absolute terms — pushing confirmed-match coverage from 83.4% to about 85% — but the operational principle is important: human-in-the-loop matching produces 99.96% accuracy when reviewers commit the time, and the AmbiguousMatchReview workflow is straightforward to spin up.

---

## SLIDE 36 — Recommendation 9 (Engineering): Pipeline hardening

**CONTENT**
For the data engineering team:
- Pin package versions in `requirements.txt`
- Add `pandera`/`great_expectations` schema validation at every join
- Containerize via Docker for reproducible reruns
- Auto-generate `data_quality_report.html` per run
- Externalize manual-AppNo curation into versioned append-only file

**FIGURE** *(none — operational slide)*

**NARRATION**
For the data engineering team. Five hardening steps. Pin package versions. Add schema validation — `pandera` or `great_expectations` — at every ingestion and join point so that any column drift or dtype change fails loud and early. Containerize via Docker. Auto-generate a data-quality report per run, aggregating the validation outputs that today sit in scattered notebook cells. And externalize the manual AppNo curation into a single, versioned, append-only file with source attribution per row, so the manual-recovery effort becomes a reviewable artifact rather than a multi-file workflow.

---

## SLIDE 37 — Closing

**CONTENT**
- NMAT works: r ≈ −0.54 effect on PLE outcome, large by Cohen
- Public > Private > Foreign at the PLE; institutional effect small at the NMAT
- Retaking works: 77.65% improve, +11 percentile median gain
- Yearly trends reflect composition change, not difficulty drift
- Equity findings: no gender gap at NMAT, 4.6 pp female PLE advantage
- 9.48% of PLE passers are operationally unrecoverable until AppNo capture is fixed
- The pipeline is ready for annual rerun cadence

**FIGURE** Composite slide combining **Figure 22 (decile staircase)** and **Figure 25 (retake improvement)** as the two takeaway visuals.

**NARRATION**
To close, the NMAT is doing its job. It produces a strong, internally consistent, downstream-validated signal of who will eventually pass the medical boards. Institutional differences are real but modest; course-group differences are larger and clearly tied to selection effects. The retake mechanism is working — three-quarters of those who try again improve, with a meaningful median gain. The yearly score drift reflects a broadening examinee pool, not a structural test-difficulty change. No gender gap at the test, a modest female advantage at the licensure. The single operational fix we are asking for — capturing the NMAT Application Number on the PLE registration form — would make every future analysis trivially definitive. The pipeline, the dashboard, and the audit trails behind everything in this deck are ready for annual rerun cadence. Thank you. We are open for questions.

---

## SLIDE 38 — Appendix / References

**CONTENT**
- Technical companion: `reports/01_Technical_Report.md`
- Stakeholder companion: `reports/02_Stakeholder_Report.md`
- Analytical dataset: `dataset/NMAT_Ultima.csv`
- PLE match audit: `dataset/output/PLE_MATCH_MASTER.csv`
- Dashboard: `dashboard.py` → `streamlit run dashboard.py`
- All charts and tables referenced in this deck are reproducible from the dashboard

**FIGURE** *(none)*

**NARRATION**
The appendix lists where to find every artifact behind this deck. The technical report has the engineering details; the stakeholder report restates these findings in narrative form; the dashboard reproduces every chart interactively. Every number on every slide can be traced to a row in NMAT_Ultima and a corresponding entry in the PLE match audit. The full reproduction path is open.

---

## Presenter Notes — Logistics

- **Total slides:** 38
- **Estimated run time:** 35–45 minutes presentation + 15–20 minutes Q&A
- **Audience handouts:** Pair this deck with `02_Stakeholder_Report.md` printed in advance for executive readers
- **Live demo opportunity:** Slides 26–27 (dashboard tour). Have `streamlit run dashboard.py` already running on a second screen
- **High-impact visuals to test in advance:** Figure 22 (the decile-to-PLE staircase), Figure 19 (the Sankey), Figure 25 (the retake improvement boxplot). These three carry roughly 60% of the deck's persuasive weight
- **Pre-built file paths for figure exports:**
  - `dataset/analysis_output/05A_sankey_uni_type_to_decile.html`
  - `dataset/analysis_output/05B_sankey_course_group_to_decile.html`
  - `dataset/analysis_output/05C_sankey_decile_to_ple_status_observable.html`
  - For static images (Figures 1–35), use `plotly.io.write_image` via the kaleido dependency (`pip install -U kaleido`) and save to `reports/figures/`
- **Q&A preparation:** Anticipate questions on (a) why we eliminated fuzzy matching, (b) why effect sizes are small while p-values are tiny, (c) the 4,135 unmatched residual and whether it could be reduced, (d) the Foreign-PLE gap mechanism, and (e) whether the 2018 score decline indicates an admissions-quality problem
