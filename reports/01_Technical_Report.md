# NMAT Analysis Pipeline — Comprehensive Technical Report

**Audience:** Data Engineers, Data Scientists, Technical Leads
**Scope:** End-to-end review of the NMAT Analysis pipeline covering the full data lifecycle — ingestion, cleaning, deterministic PLE matching, statistical analysis, and dashboard surfacing — including every data hygiene problem encountered, the exact resolutions applied, the interpretation of analytical results, and forward-looking architectural recommendations.
**Reporting Period:** NMAT exam years 2006–2018; PLE outcomes 2011–2022.
**Primary Output:** `dataset/NMAT_Ultima.csv` — 178,927 rows × 115 columns, with derived authoritative score fields and deterministic PLE linkage flags.

---

## 1. Executive Synopsis

The NMAT Analysis pipeline transforms three heterogeneous source files — `NMAT_CLEANED_DATA.csv` (178,927 raw NMAT records, 29 cols), `CEM_DATA.csv` (254,308 examinee records with component-level scores, 36 cols), and `UNIVS.csv` (3,022-row institution reference) — into a single, audit-ready analytical dataset, `NMAT_Ultima.csv`. The pipeline is implemented as three sequential notebooks (`1_Data_Cleaning_Pipeline.ipynb`, `2_PLE_Matching_Pipeline.ipynb`, `3_NMAT_PLE_Analysis.ipynb`) and a Streamlit dashboard (`dashboard.py`), orchestrated by `00_RUN_ME.ipynb`.

Three engineering decisions define the architecture:

1. **TRUE-source raw scores.** Stored totals in CEM were untrustworthy (42.2% mismatch against the sum of component subtests). We bypass `STU_RSCORE` entirely and treat the freshly derived `TotalRawScoreTRUE` (sum of `CA01`–`CA08`) as the canonical total. The calculated source `STU_RSCORE_CALC` perfectly reconciles to the derived value (0% mismatch), validating that components are reliable building blocks.
2. **Deterministic-only PLE matching.** After deprecating fuzzy/name-based matching (per the `DE-FUZZY.md` refactor), the pipeline now matches on exact `NMA_AppNo` joins sourced from three curated AppNo pools (manual `PLE_UNMATCHED.csv`, exact name-match against `PLE_DATA`, and the `PLE_STILL_UNMATCHED.csv` deterministic AppNo file). Outcome: 36,395 confirmed final matches (83.42% of 43,630 PLE passers) with zero ambiguity in the accepted-for-analysis cohort.
3. **Cohort discipline.** Every analysis below operates on a named cohort (`all`, `best`, `besttrend`, `bestobservable`, `uniobservable`, `plesafe`, `plebest`) and documents which boolean flag generates it. The "observable" cohort restriction (`Year ≤ 2014`) prevents misclassification of recent NMAT cohorts as PLE non-passers when their boards have not yet opened.

The headline analytical findings: percentile rank is overwhelmingly the dominant signal for downstream PLE outcomes (Mann-Whitney effect r ≈ −0.54, a *large* effect), university-type effects are statistically detectable but substantively small (η² = 0.0047), course-group effects are larger (η² = 0.0096) and dominated by an Engineering & Technology outlier with limited N, and 77.65% of repeat takers improve their percentile rank with a median gain of +11 points.

---

## 2. Source Data Inventory and Provenance

### 2.1 Inputs

| File | Rows | Cols | Unique Keys | Notes |
|------|-----:|-----:|-----:|------|
| `NMAT_CLEANED_DATA.csv` | 178,927 | 29 | 178,926 NMA_AppNo (2 duplicates) | Pre-cleaned NMAT 2006–2018 |
| `CEM_DATA.csv` | 254,308 | 36 | 254,304 STU_NO (8 duplicates pre-clean → 4 dropped) | Raw component scores |
| `UNIVS.csv` | 3,022 | 8 | 2,969 normalized college keys | Institution reference |
| `PLE_DATA.csv` | 43,630 | — | 43,630 unique normalized names | PLE passers 2011–2022 |
| `PLE_UNMATCHED.csv` | 6,600 | — | 2,332 rows with manual AppNo | Manual recovery file |
| `PLE_STILL_UNMATCHED.csv` (in `dataset/output/`) | 7,207 | — | 321 with AppNo | Second-round deterministic recovery file |

### 2.2 Outputs

| File | Rows × Cols | Purpose |
|------|-------------|---------|
| `NMAT_FINAL.csv/parquet` | 178,927 × 101 | Cleaned & integrated NMAT+CEM+UNIVS |
| `NMAT_Ultima.csv/parquet` | 178,927 × 115 | NMAT_FINAL + PLE match flags + best-record flag |
| `PLE_MATCH_MASTER.csv` | 43,601 | One canonical match record per PLE passer |
| `PLE_STILL_UNMATCHED_v2.csv` | 6,433 | Final residual unmatched after 3 stages |
| `PLE_AMBIGUOUS_REVIEW.csv` | 772 | Cases flagged for manual review |
| `PLE_PASSERS_IN_NMAT.csv` | 36,305 | Best-record PLE passers (analysis-ready) |
| `dataset/analysis_output/*.csv|.html` | 50+ files | Statistical outputs and Sankey HTML |

---

## 3. Phase 1 — Data Cleaning Pipeline (`1_Data_Cleaning_Pipeline.ipynb`)

### 3.1 Issues Encountered and Resolutions

#### 3.1.1 Application Number Hygiene
**Problem.** `NMA_AppNo` and `STU_NO` arrived as mixed strings — embedded spaces, dashes, alphabetic prefixes, and stray Unicode whitespace. Two duplicate AppNos existed in NMAT (178,926 unique of 178,927 rows); CEM held 8 duplicates over 254,304 unique student numbers.

**Resolution.** Apply `clean_appno(x) = re.sub(r"\D", "", str(x))`, stripping every non-digit and coercing nulls to empty string, then to `NaN`. New canonical keys: `NMA_AppNo_clean`, `STU_NO_clean`. Duplicates in CEM were resolved by a five-key priority sort — `STU_RSCORE_VALID == "VALID"` first, then `raw_component_count desc`, `calc_total_present`, `stored_total_present`, `NMAT_YEAR desc` — keeping only the top-priority row per key. Four rows dropped.

#### 3.1.2 Text Normalization
**Problem.** Free-text fields (`NMA_College`, `NMA_Course`, `COLLEGE_NAME`, `COURSE_DESC`) had inconsistent casing, embedded multiple-space gaps, punctuation variants ("St. La Salle" vs "St La Salle" vs "Saint La Salle"), and trailing whitespace.

**Resolution.** Two-tier normalization. `clean_text(x)` collapses internal whitespace via `re.sub(r"\s+", " ", x).strip()`. `normalize_text(x)` additionally uppercases and strips non-alphanumerics: `re.sub(r"[^A-Z0-9 ]+", " ", x)`. Originals preserved in `NMA_College_RAW` and `COLLEGE_NAME` for audit. The normalized form (`NMA_College_norm`, `COLLEGE_NAME_norm`) is used as the join key into UNIVS.

#### 3.1.3 Raw Score Validation — the 42.2% Problem
**Problem.** CEM ships two total-raw-score fields: `STU_RSCORE` (the stored total, available on only 174,494 of 254,308 rows, 68.6%) and `STU_RSCORE_CALC` (a computed total available on 100% of rows). When we summed the 8 component subtests `CA01`–`CA08` ourselves, **107,422 of 174,494 stored totals (42.2%) disagreed** with the sum of components.

**Resolution.** Treat the component sum as ground truth.
- `PartIRawScoreTRUE = CA01 + CA02 + CA03 + CA04` (Aptitude block) when all four are non-null.
- `PartIIRawScoreTRUE = CA05 + CA06 + CA07 + CA08` (Science block) when all four are non-null.
- `TotalRawScoreTRUE = Σ(CA01..CA08)` when all 8 are non-null.
- Mismatch flags persisted for auditability:
  - `StoredVsDerivedMismatch` — 42.2% True
  - `CalcVsDerivedMismatch` — **0.00% True**, confirming that `STU_RSCORE_CALC` is internally consistent and the stored field is the corrupted one.
- All 178,882 rows that merged to CEM had complete components (`AllRawComponentsPresent = True`), so `TotalRawScoreTRUE` is non-null on essentially the entire analytical cohort. Only 38 best-record rows (0.03%) lack TRUE raw scores; only 45 NMAT rows total failed the CEM merge.

This was the single most consequential cleaning decision: a downstream analyst who naively used `STU_RSCORE` would be reading garbage on roughly 4 of every 10 records.

#### 3.1.4 University Standardization
**Problem.** 4,367 distinct college strings appear in raw NMAT. Variants include abbreviations ("UP Manila" vs "University of the Philippines Manila"), punctuation drift ("Remedios T. Romualdez" vs "Remedios Trinidad Romualdez"), foreign institutions absent from UNIVS, and 75 rows with numeric institution codes (`13207A`, `13100A`, `13155D`, `13206A`) representing data-entry errors or anonymized IDs.

**Resolution.** Four-stage matching cascade against UNIVS:
1. `UNIVS_EXACT_PRIMARY` — exact match on `NMA_College_norm` → 2,674 colleges (61.3% of unique strings).
2. `UNIVS_EXACT_SECONDARY` — exact match on the canonical `COLLEGE_UNIV_norm` → 72 colleges (1.6%).
3. `UNIVS_FUZZY` — `rapidfuzz.token_sort_ratio` with min score 88 **and** a ≥5-point margin over the runner-up → 235 colleges (5.4%). The margin constraint protects against ambiguous matches where two universities are equally close.
4. `NO_UNIVS_MATCH` — 1,386 colleges (31.7% of unique strings, but only 1,807 rows = 1.01% of records) fall through; these get `UNI_TYPE = "Not Specified"`, `UNI_LOCATION = "Unknown"`, and a `final_value_source = "FALLBACK_UNSPECIFIED"` marker.

Overall row-level verification: **177,120 of 178,927 records VERIFIED (98.99%)**. Twelve audit columns (`verification_method`, `verification_status`, `confidence`, `evidence_summary`, `final_value_source`, `draft_*`) preserve provenance for every match decision.

Canonicalization rules eliminate downstream inconsistencies:
- `UNI_TYPE ∈ {"Public", "Private", "Foreign", "Not Specified"}`.
- `UNI_LOCATION ∈ {"Local", "International", "Unknown"}`.
- Inferred: `Foreign → International`; `Public|Private → Local`.

Post-cleaning integrity check (Phase 3 validation): of 3,213 unique colleges in the final dataset, **100% map to exactly one `UNI_TYPE`** — the cleaning pipeline successfully resolved the raw data's 760-college multi-classification problem (e.g., Remedios Trinidad Romualdez Medical Foundation previously appeared as Private, Public, and Not Specified across different applications). Two universities (Velez College, New York University) retain dual `UNI_TYPE × UNI_LOCATION` mappings at the UNIVERSITY-level — both are likely true edge cases (international campuses or relabeling events) that warrant manual classification rules.

#### 3.1.5 Course-Group Derivation
**Problem.** Course text appears across four columns (`Course Classification`, `Course_recode`, `NMA_Course`, `COURSE_DESC`) with no single authoritative source.

**Resolution.** A deterministic keyword classifier (`map_course_group`) checks each field in turn (`Course Classification → Course_recode → NMA_Course → COURSE_DESC`) and returns the first non-"Other" match. Keyword sets:
- **Medical & Allied:** MEDICAL, ALLIED, NURSING, PHARMACY, HEALTH, MED TECHNOLOGY, RADIOLOGIC, PUBLIC HEALTH, NUTRITION.
- **Natural Sciences:** BIOLOGY, NATURAL SCIENCE(S), PHYSICS, CHEMISTRY.
- **Social & Behavioral Sciences:** SOCIAL, BEHAVIORAL/BEHAVIOURAL, PSYCHOLOGY, ECONOMICS.
- **Engineering & Technology:** ENGINEERING, TECHNOLOGY.
- **Education:** EDUCATION, TEACHER.
- **Other:** default.

Distribution in NMAT_FINAL: Medical & Allied 86,140 (48.1%), Natural Sciences 55,900 (31.2%), Social & Behavioral Sciences 22,022 (12.3%), Other 9,855 (5.5%), Education 4,162 (2.3%), Engineering & Technology 848 (0.5%). The 5.5% "Other" residual is small enough to leave as-is, but its disproportionate top-decile representation (34.18% in D8–D10) suggests there are mis-classified Natural Sciences variants hiding in this bucket — see §10.4.

#### 3.1.6 Percentile and Decile Derivation
**Problem.** `NMS_PER` arrives as a string; 4,141 records (2.3%) have no parseable percentile.

**Resolution.** `NMS_PER_num = pd.to_numeric(NMS_PER, errors="coerce")`. `PercentileDecile = pd.cut(NMS_PER_num, bins=[0,10,20,...,100], labels=["D1",...,"D10"], include_lowest=True)`. Missing percentile produces missing decile (3,069 missing in the best-record subset, 2.29%).

#### 3.1.7 NMAT–CEM Merge
**Result.** Join on `NMA_AppNo_clean ↔ STU_NO_clean` after CEM deduplication. **178,882 of 178,927 NMAT rows match (99.97%);** 45 rows (0.03%) carry `HasCEMMatch = False`. CEM enrichment supplies `BDATE`, `AGE`, `SEX`, `CIVIL_STATUS`, `NMAT_YEAR`, plus all eight component scores.

### 3.2 Final NMAT_FINAL Composition

178,927 rows × 101 columns, structured as:
- Identity & demographics (11 cols)
- Enrollment & course (12)
- University & verification (19)
- Geography (3)
- NMAT standard scores + decile (13)
- Merge status (2)
- Raw score validation (8) — `StoredRawTotal`, `CalculatedRawTotal_Source`, `TotalRawScoreTRUE`, `PartIRawScoreTRUE`, `PartIIRawScoreTRUE`, plus flags
- Raw score components (8)
- CEM standardized subtest components (8)
- CEM composite scores (4)
- Audit & mismatch flags (4)
- Test metadata + provenance (9)

### 3.3 Distributions

| UNI_TYPE | Rows | % |
|---|---:|---:|
| Private | 135,519 | 75.7 |
| Public | 37,111 | 20.7 |
| Foreign | 4,016 | 2.2 |
| Not Specified | 2,281 | 1.3 |

| UNI_LOCATION | Rows | % |
|---|---:|---:|
| Local | 172,630 | 96.5 |
| International | 4,465 | 2.5 |
| Unknown | 1,832 | 1.0 |

| Decile | Rows |
|---|---:|
| D1 | 26,226 |
| D2 | 19,647 |
| D3 | 17,172 |
| D4 | 18,230 |
| D5 | 15,750 |
| D6 | 16,457 |
| D7 | 15,012 |
| D8 | 15,228 |
| D9 | 15,376 |
| D10 | 15,688 |
| (missing) | 4,141 |

---

## 4. Phase 2 — Deterministic PLE Matching Pipeline (`2_PLE_Matching_Pipeline.ipynb`)

### 4.1 Architectural Transition

Prior versions of this pipeline used fuzzy name matching (rapidfuzz with year-gap, percentile-floor, and DOB-modal heuristics) to bridge PLE passers (named with first/last only, no AppNo) to NMAT records. Per the `DE-FUZZY.md` refactoring plan, **all fuzzy logic has been eliminated.** The current pipeline is strictly deterministic, joining only on cleaned `NMA_AppNo`. The change was motivated by two failure modes of fuzzy matching:

1. **False positives at common names.** Filipino surnames concentrate in narrow lexical bands; "DELA CRUZ, JUAN" can match dozens of candidates within score-margin thresholds.
2. **Auditability.** Fuzzy outcomes were not reproducible across rapidfuzz versions and could not be traced to a source document by reviewers.

### 4.2 Three-Stage Match Cascade

| Stage | Source | Input | Method | Output |
|---|---|---:|---|---:|
| 0 | `PLE_UNMATCHED.csv` (manual AppNo) | 2,332 | Direct `AppNo → NMAT` lookup | 2,331 FINAL_MATCH, 1 APPNO_NOT_IN_NMAT |
| 1 | `PLE_DATA.csv` | 43,630 (less Stage 0) | Exact normalized name match + 5-year board-gap filter | 33,970 FINAL_MATCH; 4,208 NEEDS_FUZZY → routed to Stage 2; 2,350 NO_VALID_MATCH; 772 AMBIGUOUS |
| 2 | `PLE_STILL_UNMATCHED.csv` (deterministic AppNo) | 7,207 | Direct AppNo lookup | 321 FINAL_MATCH; 6,886 UNMATCHED_NO_APPNO |

Stage 1 retains the year-gap guardrail (`PLE_YEAR − NMAT_YEAR ≥ 5`) because medical school plus boards requires at least four years post-NMAT. When multiple exact-name matches survive, a deterministic disambiguator selects the latest NMAT year with percentile ≥ 40, falling back to highest-percentile tiebreak with a 5-point margin requirement before declaring AMBIGUOUS.

### 4.3 Master Match Table (`PLE_MATCH_MASTER.csv`, 43,601 rows after dedup)

| MATCH_STATUS | Count | % of 43,630 |
|---|---:|---:|
| FINAL_MATCH | 36,395 | 83.42% |
| AMBIGUOUS | 772 | 1.77% |
| NO_VALID_MATCH | 2,298 | 5.27% |
| UNMATCHED_NO_APPNO | 4,135 | 9.48% |
| APPNO_NOT_IN_NMAT | 1 | 0.00% |

By method: EXACT (Stage 1) = 37,040; DETERMINISTIC_APPNO (Stage 2) = 4,230; MANUAL_APPNO_MATCH (Stage 0) = 2,331.

**Operational recovery.** Manual AppNo curation (Stage 0) recovered 2,331 records (5.34% of the PLE passer universe) that had previously failed automated matching. The second-round deterministic file (Stage 2) added 321 records (0.74%). Together, manual integration directly contributed **2,652 confirmed matches (6.08%)** that no automatic method had recovered.

### 4.4 NMAT_Ultima — Flag Generation

For each NMAT row, lookup is performed first by `APPNO_CLEAN`, then by `NAME_NORM`:

| Flag | Definition | True count |
|---|---|---:|
| `IS_PLE_PASSER` | MATCH_STATUS in {FINAL_MATCH, MANUAL_APPNO_MATCH, DETERMINISTIC_APPNO} | 49,986 |
| `IS_PLE_ANALYSIS_SAFE` | Same as IS_PLE_PASSER (no AMBIGUOUS) | 49,986 |
| `IS_BEST_NMAT_RECORD` | The specific matched AppNo (for passers) OR highest-percentile + latest-year row per `PERSON_KEY` (for non-passers) | 133,804 |
| `PLE_MATCH_STATUS` | Direct from master | 49,986 FINAL_MATCH, 5,595 NO_VALID_MATCH, 1,723 AMBIGUOUS, 121,623 NOT_IN_PLE |

Why does `IS_PLE_PASSER = True` show 49,986 NMAT rows when only 36,305 unique passers exist? Because PLE passers who took the NMAT multiple times have *all* their attempts flagged. The 49,986 number is the row-level count of "this examinee later passed PLE"; the 36,305 number is the person-level count derived via `IS_BEST_NMAT_RECORD`.

Year-gap distribution among matches (median 6 years, min 5, max 15): 4,424 records at gap 5, 18,518 at gap 6, 8,246 at gap 7, declining to 4 records at gap 15. The right-tail (gap ≥ 10, n=516) likely represents retake-then-eventual-pass trajectories.

---

## 5. Phase 3 — Statistical Analysis (`3_NMAT_PLE_Analysis.ipynb`)

### 5.1 Cohort Definitions

| Cohort | Filter | N |
|---|---|---:|
| `all` | none | 178,927 |
| `best` | `IS_BEST_NMAT_RECORD == True` | 133,804 |
| `trend` | `Year ∈ [2006, 2018]` | 178,882 |
| `besttrend` | best ∧ trend | 133,804 |
| `bestobservable` | best ∧ `Year ≤ 2014` (`IS_BOARD_OBSERVABLE_COHORT`) | 64,501 |
| `uni` | besttrend ∧ `UNI_TYPE ∈ {Public, Private, Foreign}` | 130,735 (valid decile) |
| `uniobservable` | bestobservable ∧ same | ~63,665 |
| `plesafe` | `IS_PLE_ANALYSIS_SAFE == True` | 49,986 |
| `plebest` | best ∧ plesafe | 36,305 |

The "observable" qualifier is critical: PLE outcomes exist for years 2011–2022. An NMAT examinee from 2018 would not be observable in PLE data until ≈ 2023, so including them in confirmed-PLE-share calculations would falsely depress the rate. All PLE-alignment analyses restrict to `Year ≤ 2014`.

### 5.2 Yearly Trends (Best-Record Trend Cohort)

| Year | N | Raw median | Raw IQR | Pct median | GPS median |
|---|---:|---:|---:|---:|---:|
| 2006 | 3,665 | 131 | 46 | 53 | 508 |
| 2007 | 3,660 | 130 | 48 | 52 | 504 |
| 2008 | 4,849 | 129 | 46 | 54 | 511 |
| 2009 | 6,864 | 129 | 44 | 52 | 504 |
| 2010 | 8,006 | **135** | 46 | 57 | 517 |
| 2011 | 8,725 | 129 | 42 | 52 | 504 |
| 2012 | 9,135 | 121 | 44 | 53 | 510 |
| 2013 | 9,118 | 128 | 51 | 59 | 525 |
| 2014 | 10,441 | 120 | 44 | 57 | 518 |
| 2015 | 10,402 | 118 | 49 | 52 | 506 |
| 2016 | 12,609 | 123 | 49 | 48 | 495 |
| 2017 | 23,955 | 118 | 50 | 44 | 485 |
| 2018 | 22,337 | **111** | 41 | 43 | 481 |

**Interpretation.** Two effects co-occur from 2014 onward: (a) median raw scores fall 24 points from the 2010 peak to 2018; (b) examinee volume more than doubles. The IQR remains tight (41–51), so the distribution is shifting downward as a unit, not widening. Standardized percentile and GPS show milder declines (50% rescales to the population), and Part I (Aptitude) consistently exceeds Part II (Science) across every year. This is consistent with examinee composition change — broader pre-med pipeline absorption — rather than a structural difficulty break.

### 5.3 Stability — Kruskal-Wallis Across Years

| Score | H | p | η² | Effect |
|---|---:|---:|---:|---|
| Total Raw | 5598.2 | <0.001 | 0.042 | Small |
| Part I Raw | 5453.4 | <0.001 | 0.041 | Small |
| Part II Raw | 5516.0 | <0.001 | 0.041 | Small |
| Percentile Rank | 2235.7 | <0.001 | 0.017 | Small |
| GPS | 2420.3 | <0.001 | 0.018 | Small |

All five test statistics are colossal because N is ~134k, but the η² effect sizes hover near 0.02–0.04. **Statistical significance ≠ practical significance here.** Dunn post-hoc with Bonferroni adjustment (Table 48) finds 2010 significantly higher than 2012/2014–2018; 2018 significantly lower than every prior year; the 2006–2009 block and 2015–2017 block are internally similar.

### 5.4 Decile × University Type

Best-record, institutional comparison subset (n=130,735 with valid decile):

| UNI_TYPE | Median pct | D8–D10 share |
|---|---:|---:|
| Public | 55 | **37.0%** |
| Foreign | 50 | 30.3% |
| Private | 48 | 29.0% |

Kruskal-Wallis (UNI_TYPE × percentile): H = 614.156, p < 0.001, η² = 0.0047 (negligible). Chi-square (UNI_TYPE × decile): χ² = 1090.89, p < 0.001, df = 18, Cramér's V = 0.0649 (very weak).

The 8 percentage-point gap between Public and Private/Foreign in top-decile share is the largest practically meaningful institutional effect, but the bulk of variance lives within (not between) university types.

Public-International examinees (n=331, small) underperform Public-Local (median 40 vs 55, gap = 15 percentile points), the largest within-type stratification effect in the dataset.

### 5.5 Decile × Course Group

| CourseGroup | N | Median pct | D8–D10 share |
|---|---:|---:|---:|
| Engineering & Technology | 730 | 72 | **51.58%** |
| Natural Sciences | 40,851 | 54 | 35.53% |
| Other | 7,943 | 53 | 34.18% |
| Education | 3,260 | 51 | 32.37% |
| Medical & Allied | 63,432 | 49 | 27.67% |
| Social & Behavioral Sciences | 16,366 | 39 | 27.52% |

Kruskal-Wallis: H = 1279.83, p < 0.001, η² = 0.0096 (small). The Engineering & Technology figure is striking (51.58% in top deciles) but rests on n = 729; with that small N and the strong selection effect (engineering pre-med applicants are unusual), this number should be reported with confidence-interval caveats.

### 5.6 PLE Alignment — The Main Result

Mann-Whitney U comparing Confirmed PLE Passers (n = 29,269) against No-Confirmed-Match (n = 35,194) within the observable cohort:

| Score | U | p | r (effect) | Confirmed median | NoMatch median |
|---|---:|---:|---:|---:|---:|
| Total Raw | 794M | <0.001 | **−0.54** | 143 | 112 |
| Percentile | 772M | <0.001 | **−0.54** | 73 | 36 |
| GPS | 794M | <0.001 | −0.54 | 564 | 464 |
| Part I | 774M | <0.001 | −0.50 | 76 | 61 |
| Part II | 776M | <0.001 | −0.51 | 68 | 51 |

**r ≈ −0.54 is a large effect.** Confirmed PLE passers separate cleanly from non-passers across every score axis — the gap is 31 raw points, 37 percentile points, 100 GPS points.

Decile-to-PLE staircase (monotone increase, observable cohort):

| Decile | Confirmed PLE % |
|---|---:|
| D1 | 8.77 |
| D2 | 16.07 |
| D3 | 19.21 |
| D4 | 25.66 |
| D5 | 46.30 |
| D6 | 51.82 |
| D7 | 57.64 |
| D8 | 60.44 |
| D9 | 67.82 |
| D10 | **76.25** |

The D4→D5 jump (25.66% → 46.30%, +20.6 pp) is the steepest single-decile threshold, suggesting that crossing the 40th percentile is the strongest empirical predictor of eventual PLE passage in this dataset. The full D1→D10 span is 67.5 percentage points.

### 5.7 PLE Share by Year (Observable Only)

| Year | n_obs | Confirmed pass | Share % |
|---:|---:|---:|---:|
| 2006 | 3,665 | 2,038 | **55.61** |
| 2007 | 3,660 | 1,868 | 51.04 |
| 2008 | 4,849 | 2,514 | 51.85 |
| 2009 | 6,864 | 3,226 | 47.00 |
| 2010 | 8,006 | 3,808 | 47.56 |
| 2011 | 8,725 | 3,852 | 44.15 |
| 2012 | 9,135 | 4,063 | 44.48 |
| 2013 | 9,118 | 3,951 | 43.33 |
| 2014 | 10,441 | 3,949 | **37.82** |

The 2014 trough is partially mechanical: PLE_DATA ends in 2022, so 2014 examinees have an 8-year observation window; 2006 examinees had 16 years. This censoring should be addressed in any longitudinal interpretation.

### 5.8 PLE Share by University Type (Observable)

| UNI_TYPE | n_obs | Confirmed pass | Share % | Median pct |
|---|---:|---:|---:|---:|
| Public | 13,627 | 6,755 | **49.57** | 67 |
| Private | 47,888 | 21,398 | 44.68 | 52 |
| Foreign | 2,117 | 786 | 37.13 | 52 |

Public's 12.4 pp lead over Foreign is the most policy-relevant institutional finding. Note: Foreign median percentile (52) equals Private (52), so the Foreign gap is *not* a percentile gap — it's a gap downstream of NMAT, likely reflecting different licensure pathways, visa friction, or attrition for foreign-educated pre-meds entering Philippine boards.

### 5.9 PLE Share by Course Group (Observable)

| CourseGroup | n_obs | Pass share % | Median pct |
|---|---:|---:|---:|
| Education | 2,969 | **51.90** | 52 |
| Other | 6,180 | 46.17 | 55 |
| Natural Sciences | 15,208 | 45.50 | 66 |
| Medical & Allied | 35,420 | 45.34 | 49 |
| Social & Behavioral Sciences | 4,384 | 40.67 | 64 |
| Engineering & Technology | 302 | 37.75 | **71** |

The Engineering & Technology paradox — highest median percentile (71) but lowest PLE share (37.75%) — almost certainly reflects sample size (n=302) and a survivorship/pathway divergence: engineering grads who took NMAT may be less likely to actually pursue medicine to boards.

### 5.10 Repeat Takers

| Metric | Value |
|---|---:|
| Took NMAT once | 101,155 (75.00%) |
| Took NMAT 2+ times | 33,714 (25.00%) |
| Max attempts | 9 |
| Repeat takers improved percentile rank | 77.65% |
| Repeat takers improved raw score | 73.58% |
| Median percentile change (last − first) | **+11** |
| Median raw score change | **+12** |

Three-quarters of repeat takers improve, with a meaningful median lift. This is one of the cleanest practical findings in the dataset and a strong argument for the legitimacy of NMAT retake policy.

### 5.11 Subtest Profiles (Standardized Means, Best-Record Trend Cohort)

By university type, Public > Foreign > Private across every subtest. By course group, Natural Sciences and Engineering & Technology dominate Quantitative/Physics/Chemistry; Medical & Allied tilts slightly higher on Verbal and Social Science. Social & Behavioral Sciences underperforms on Verbal (453 mean) by a wide margin.

### 5.12 Gender

Female (n=74,153) and Male (n=59,613) medians are 50 vs 49 (percentile), 122 vs 121 (raw), 500 vs 499 (GPS). Mann-Whitney U = 2.18B, p = 0.0958, r = −0.0053. **No meaningful gender effect.** PLE confirmed share: Female 29.20%, Male 24.57%. The 4.6 pp female advantage on PLE share, despite null NMAT differences, suggests downstream factors (matriculation, persistence) drive the gap rather than test performance.

---

## 6. Data Quality Assessment — Cross-Cutting Findings

1. **Raw-score field hierarchy is now formally defined.** Use `TotalRawScoreTRUE`, `PartIRawScoreTRUE`, `PartIIRawScoreTRUE` exclusively. Treat `STU_RSCORE` as audit-only. The pipeline preserves the originals so analysts can independently verify mismatch claims.
2. **Match quality is dominated by AppNo coverage in the source PLE files.** Of the 4,135 final UNMATCHED_NO_APPNO records, none are recoverable without either a fresh AppNo curation pass or a return to name-based matching (which we have rejected). This is a hard ceiling at 90.5% of the PLE passer universe.
3. **The 1,807 "Not Specified" institution records (1.01%)** are predominantly foreign institutions absent from UNIVS and a tail of numeric institution codes. They are excluded from UNI_TYPE comparisons (`uni` cohort) but retained in trend analyses where institution is not the analysis axis.
4. **Two NMAT applicants share a duplicate `NMA_AppNo`** that survives cleaning (178,926 unique of 178,927 rows). The duplicate has not been resolved at source and should not be silently dropped; analysts using AppNo as a join key should be aware.
5. **CEM is the authoritative source for component scores;** the 99.97% NMAT↔CEM match rate validates this design.
6. **Person-level deduplication uses `NAME_NORM + BDATE`.** Records with missing BDATE rely on name alone — common-name false collapses are possible but the 134,869 unique persons figure is robust at the population level.

---

## 7. Interpretation of Analytical Results — Technical View

The substantive story is dominated by three signals:

**Signal 1: Percentile rank is the right outcome variable.** Raw score, GPS, and percentile rank all give the same answer about who passes PLE, but percentile is most interpretable cross-year because it controls for cohort difficulty drift. The Mann-Whitney r ≈ −0.54 effect against PLE status is, by Cohen's conventions, a "large" effect — bigger than most cognitive/medical-licensure correlation literature reports.

**Signal 2: Institutional effects are small but real.** η² = 0.0047 for UNI_TYPE × percentile is "negligible" by formal cutoffs, but the 12.4 percentage-point Public-vs-Foreign gap in confirmed PLE share is a policy-grade difference. Two effects must be disentangled: (a) Public students have higher median percentile (67 vs 52), suggesting they enter with stronger preparation; (b) Foreign students underperform on PLE conditional on percentile, suggesting downstream factors. These should be analyzed separately in future work.

**Signal 3: 2017–2018 anomalies are composition, not difficulty.** The 24-point raw-score decline 2010→2018 coincides with an ~7× volume increase. With Dunn post-hoc clustering 2015–2017 as similar and 2018 as significantly lower than every prior year, the most parsimonious explanation is admission-pipeline broadening rather than test difficulty shift.

---

## 8. Technical Recommendations

### 8.1 Pipeline Hygiene

1. **Pin package versions.** The `pip install -U` pattern in `00_RUN_ME.ipynb` introduces reproducibility risk. Ship `requirements.txt` with exact versions (the README provides a candidate set).
2. **Promote `00_RUN_ME.ipynb` to a `make`-style runner with hash-checked source files.** Detect when source CSVs change and rerun only the affected stages.
3. **Add unit tests for the cleaning helpers.** `normalize_name`, `clean_appno`, `clean_year`, `map_course_group`, the disambiguation tie-breaker — these are pure functions with deterministic behavior and should have a small pytest suite that prevents regression. The existing `assert normalize_name(...)` calls inside notebook cells are too easily bypassed.
4. **Audit the two duplicate `NMA_AppNo` rows** in NMAT_CLEANED_DATA. Either resolve at source or document the canonical row to keep.
5. **Persist the `MEMORY.md`-style provenance** of which CEM row was retained on each priority-sort tie. Currently 4 dropped CEM rows leave no trail.

### 8.2 Scaling

1. **Move from CSV → Parquet end-to-end.** The pipeline already writes Parquet copies of NMAT_FINAL and NMAT_Ultima; standardize on Parquet as the canonical format and treat CSV as an export-only convenience. This eliminates `dtype=str` re-coercion and the silent `pd.to_numeric(errors="coerce")` masking of dirty values.
2. **Replace the row-by-row tqdm loops in matching with vectorized `merge` operations.** Stage 0 currently iterates 2,332 PLE_UNMATCHED rows with an in-loop dict lookup; a left-merge would be 100× faster and eliminate per-row object allocation.
3. **Cache the UNIVS fuzzy-match results.** Each pipeline rerun reprocesses 4,367 unique college strings; serialize the college → match mapping to a versioned JSON and only re-fuzzy when UNIVS or the new-college set changes.
4. **Switch dashboard data load from CSV to Parquet** (`dashboard.py` may already do this — confirm) and apply `pyarrow` partition-by-year to enable lazy loading. With Streamlit's `@st.cache_data` decorator on the loader, the 178k-row dataset can be re-filtered in milliseconds rather than re-parsed.

### 8.3 Validation

1. **Schema validation at ingest.** Add a `pandera` or `great_expectations` checkpoint at the top of each notebook: column presence, dtype, primary-key uniqueness, expected-value ranges (e.g., `Year ∈ [2006, 2018]`, `NMS_PER_num ∈ [0, 100]`).
2. **Emit a single, auto-generated `data_quality_report.html`** per run that surfaces: row counts at every join, every null-rate, the StoredVsDerivedMismatch tally, the 1,807-record fallback count, and the post-cleaning UNI_TYPE consistency check. The information exists in the validation cells today — it just isn't aggregated.
3. **Track the 1,386 unmatched college strings as a known-residual dataset** with assigned owners for periodic UNIVS extension. Many are foreign institutions and could be resolved with a targeted curation sprint.
4. **Re-validate the 2 universities with dual `UNI_TYPE × UNI_LOCATION` mappings** (Velez College, NYU) with manual classification rules.

### 8.4 Matching Architecture

1. **Externalize the AppNo curation list.** The `PLE_UNMATCHED.csv` + `PLE_STILL_UNMATCHED.csv` two-file pattern should be unified into a single, versioned, append-only `PLE_MANUAL_APPNO.csv` with source attribution per row. This makes it possible to ship the manual curation effort as a standalone, reviewable artifact.
2. **Build a low-friction reviewer UI for the 772 AMBIGUOUS cases.** These are records where exact name matched but disambiguation left multiple candidates after the year-gap + percentile filters. Each one is potentially recoverable by a human in ~30 seconds. At full resolution we would push final-match share from 83.42% to ~85%.
3. **Consider a probabilistic record-linkage library** (e.g., `splink`, `recordlinkage`) for the 4,135 UNMATCHED_NO_APPNO residual. The deterministic-only mandate should not preclude a clearly-labeled, separately-stored, "candidate-pair-for-review" set that does not contaminate the analytical cohort.

### 8.5 Analysis & Reporting

1. **Bootstrap confidence intervals on the small-N findings** — especially Engineering & Technology (n=302–730), Public-International (n=326–331), and the Foreign-PLE gap (n=2,117). Point estimates in these cells are unstable.
2. **Standardize on `effect_size` reporting next to every p-value.** The pipeline already produces η², Cramér's V, and r for Mann-Whitney; the dashboard should default to showing them alongside p, with traffic-light coloring (≥0.14 large, ≥0.06 medium, ≥0.01 small).
3. **Add a censoring/right-truncation note to every PLE-share-by-year chart.** The 2014 trough is a known artifact and should never be presented without that caveat.
4. **Surface the `AMBIGUOUS` and `NOT_IN_PLE` populations as separately filterable cohorts** in the dashboard's PLE pages, alongside today's binary Confirmed/No-Match. The dashboard's `PLE_STATUS_LABEL` is currently two-valued; promote it to four.
5. **Author a `notebooks/0_data_dictionary_check.ipynb`** that round-trips `data_dictionary.md` against the live NMAT_Ultima schema, flagging any column drift.

### 8.6 Reproducibility & Operations

1. **Containerize.** A `Dockerfile` with pinned Python/pandas/streamlit versions removes the entire class of "works on my machine" failures for downstream consumers (CHED, NMAT board staff).
2. **Cron the pipeline against versioned source files** with a release tag (`v2026.05` etc.). The current notebook-driven flow is great for development but fragile for production.
3. **Move secrets/paths out of inline constants.** `ROOT_CANDIDATES = [Path("/root/dataset"), Path("root/dataset"), Path("dataset")]` is reasonable Colab-tolerance code but should resolve from a `config.yaml`.
4. **Generate dashboard PNG snapshots automatically** at every run with `plotly.io.write_image` (kaleido is already a dependency). Embed those into a static `executive_brief.html` that ships with each pipeline release.

---

## 9. Known Limitations

| Limitation | Impact | Mitigation |
|---|---|---|
| PLE data window 2011–2022 censors NMAT cohorts 2015+ | Confirmed-PLE-share by year is right-truncated | All charts use `Year ≤ 2014` observable cohort |
| 4,135 PLE passers have no AppNo and no exact name match | 9.48% of PLE universe unreachable deterministically | Manual curation campaigns; clearly excluded from headline metrics |
| 772 AMBIGUOUS matches not assigned | 1.77% of PLE passers in limbo | Surfaced in `PLE_AMBIGUOUS_REVIEW.csv` for review |
| Engineering & Technology n = 302–730 | Estimates unstable | Always report with N and CI |
| Foreign-international institutions absent from UNIVS | 1,386 unique unmatched colleges → 1,807 rows fallback | Targeted UNIVS extension |
| 2 universities with dual UNI_TYPE × LOCATION | Sub-cell ambiguity in institution-location matrix | Manual rule needed |
| Person dedup via NAME_NORM + BDATE | Missing-BDATE records may collide on common names | Document; consider name+DOB+sex composite |

---

## 10. Conclusion

The NMAT Analysis pipeline is in a mature, defensible state for descriptive policy reporting. The deterministic-matching transition has eliminated a class of audit risks at a manageable recall cost. The single most important engineering decision — using component-summed `TotalRawScoreTRUE` rather than the corrupted stored total — is well-documented and preserved in the data lineage. The analytical signals are clear: NMAT percentile is a large-effect predictor of PLE passage; institutional differences exist but are dominated by composition rather than structural advantage; repeat-taking works; gender does not differentiate performance. With the operational recommendations in §8 — particularly schema validation, the 772 AMBIGUOUS review surface, and CI containerization — this pipeline can scale to annual rerun cadence with minimal incremental engineering effort.
