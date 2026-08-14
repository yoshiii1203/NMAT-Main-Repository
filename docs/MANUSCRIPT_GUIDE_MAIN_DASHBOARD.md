# Manuscript Writing Guide — Main Dashboard

This is a **writing guide, not the manuscript**. For each section it says what to discuss, which
dashboard tab/table/figure supplies the evidence, the specific numbers to cite, and the caveat that
must travel with the claim. Evidence source is `streamlit_dashboard/main_dashboard/dashboard.py`
(13 tabs, 42 tabs+subtabs) unless stated otherwise. All numbers were verified against
`dataset/NMAT_Exodus.parquet` (md5 `28b85ac53af13b4a2ef3ee93527c97c1`) on 2026-08-14; see
`docs/HANDOFF_TESTING_GUIDE.md` for the verification commands.

**Global rules that apply to every section below** (do not restate them as caveats each time, but
never violate them):
- **"Linkage," never "pass rate."** The PLE source file contains passers only — no failures, no
  complete roster of takers. Every `IS_PLE_PASSER`-derived percentage is a linkage rate.
- **Observable cohort = `IS_BEST_OBSERVABLE_RECORD` (69,503 people).** Never
  `IS_BEST_NMAT_RECORD & Year<=2014` — that shortcut drops 3,721 people who took their best attempt
  after 2014 but still have an earlier observable-window attempt.
- **B1 is the lowest decile, B10 the highest.** State bin order explicitly in every figure caption;
  never let a reader assume B10 is "top of the alphabet, therefore best" or infer order from a
  string sort.
- **`UNDERGRAD_UNIVERSITY` / `UNDERGRAD_UNI_TYPE` / `UNDERGRAD_UNI_LOCATION` describe the applicant's
  undergraduate degree, not their medical school.** No medical-school identifier exists anywhere in
  this dataset. Evidence: UP Diliman — no College of Medicine — appears as `UNDERGRAD_UNIVERSITY` for
  4,421 rows, 1,914 of them confirmed PLE passers.

---

## 1. Introduction

**What to discuss:** the NMAT as a national gatekeeping instrument (2006–2018), the motivating
question (does score at admission predict eventual licensure?), and — briefly — that this dataset
also underlies a CHED policy brief covered separately (`docs/MANUSCRIPT_GUIDE_CHED_DASHBOARD.md`);
this manuscript is the broader descriptive/analytic account, not the policy submission.

**Evidence:** none yet — this section is framing.

**Numbers to cite:** 178,927 exam sittings, 2006–2018, 134,869 unique examinees.

**Caveat:** state up front that "examinee" means NMAT test-taker, not medical student or physician —
the distinction matters for every later section.

---

## 2. Data and Methods

This section carries the per-pipeline data-quality narrative. Its job is to make the reader trust the
numbers *because* of the corrections described here, not despite them — each subsection is a defect
found, its consequence, and the fix, in that order.

### 2.1 Pipeline 1 — Data Cleaning (`1_Data_Cleaning_Pipeline.ipynb`)

**What to discuss:** application-number standardization; 4-tier university-name matching against
`UNIVS.csv`; raw-score recalculation; percentile-bin construction.

**The headline defect:** the CEM-supplied `StoredRawTotal` disagreed with the sum of the 8 component
subtest raw scores in **56,065 of the 99,316 records that carry a stored total (56.45%)**. Because
44.5% of rows carry no stored total at all, that 56,065 is also 31.33% of all 178,927 rows — always
name the denominator. **`TotalRawScoreTRUE`, recalculated as the sum of the 8 components, is the
canonical value** and is arithmetically perfect: 0 mismatches against
`Raw_Verbal + Raw_InductiveReasoning + Raw_Quantitative + Raw_PerceptualAcuity + Raw_Biology +
Raw_Physics + Raw_SocialScience + Raw_Chemistry` and 0 mismatches for
`PartIRawScoreTRUE + PartIIRawScoreTRUE == TotalRawScoreTRUE`, across all 178,882 non-null rows. Both
identities are enforced as hard-fail invariants in `5_Slim_Exodus.py` and `tests/test_data_invariants.py`.

**The widely-repeated "42.2% of stored totals were incorrect" figure is also correct — it is a
different population.** `STU_RSCORE != STU_RSCORE_CALC` on 107,422 of 254,308 rows = 42.24% of the
whole `CEM_DATA.csv`, versus 56.45% of the 99,316 NMAT-matched rows carrying a stored total. Cite
either, but always name the denominator. **Do not claim the project discovered this**: CEM's own
`STU_RSCORE_VALID` column already flags exactly those 107,422 rows as `INVALID`, a perfect predictor
with zero exceptions — the recalculation reproduces a QA judgement the source system published. The
figure appears in `CLAUDE.md`, `README.md`, and older audit
documents; do not carry it into the manuscript. `dashboard.py` Tab 2 (line 978) states this
explicitly and instructs "never state this as 42.2%."

**University-name normalization, with a disclosed exception:** matching against `UNIVS.csv` uses
`rapidfuzz` (`fuzz.token_sort_ratio`, min score 88, min gap 5) for about 7% of the ~3,251 distinct
institution names on the application form; every fuzzy match and its score is logged to
`dataset/output/fuzzy_university_matches.csv` for audit. This is **unrelated to PLE record
matching**, which never uses fuzzy string matching (§2.2) — the "deterministic matching only"
guarantee applies to person identity resolution, not to this free-text cleanup step. State this
distinction explicitly if discussing either.

**Evidence:** `dashboard.py` Tab 2 ("Data Integrity"), Tables 3 and 4.

### 2.2 Pipeline 2 — PLE Matching (`2_PLE_Matching_Pipeline.ipynb`)

**What to discuss:** the 3-stage matching cascade (application-number recovery → exact name → 
deterministic application number), and — this is the section that changed most during remediation —
what `disambiguate()` does when one name matches more than one NMAT record.

**Two defects were found and fixed here; both pushed identity resolution toward score instead of
identity evidence:**

1. **RC-0 — a hard 40th-percentile floor.** `disambiguate()` step 4 discarded every name-collision
   candidate scoring below the 40th percentile, and rejected the match outright if *all* candidates
   scored below it. This is the exact population the CHED brief studies, and 40 is the exact CMO
   threshold under review — so the pipeline used to systematically refuse to match the people the
   project exists to describe. **Deleted.**
2. **O-24 — the documented DOB check never ran.** `BDATE_CLEAN` was created *after* the row-dict
   snapshot `disambiguate()` reads, so the birthdate filter — the strongest identity evidence
   available — silently no-opped in every historical run. Fixed by reordering so `BDATE_CLEAN` exists
   before the snapshot.

**Current cascade (post-fix):** Step 1 (year-gap filter) → Step 2 (DOB/sex identity filter, now
actually live) → Step 3 (take the latest NMAT year among survivors) → if exactly one candidate
remains, match; if more than one survives all three steps, reject as
`rejected_ambiguous_person` rather than deciding on score. No step selects a match by NMAT
percentile.

**Consequence, reported with direction:** confirmed passers moved **49,986 → 49,086** — some
name-collision winners who previously cleared 40 while their name-twin did not are now correctly
ambiguous and dropped; others whose entire candidate group scored below 40 are newly resolvable and
matched. The second group is the one the CHED question is about (see
`docs/MANUSCRIPT_GUIDE_CHED_DASHBOARD.md` §5 for its profile). `disambiguate()` runs only when a name
collides with more than one NMAT record — unique-name matches bypass it entirely, so most of the
dataset was never touched by either bug; the effect is real but confined to name-collision groups.

**Identity-key limitation, disclosed, not silently patched:** `PERSON_KEY` is
`"SURNAME, GIVEN NAMES" || birthdate`. **6,148 keys (4.56%) carry contradictory SEX** across their
rows — one person cannot have two sexes, so this is a lower bound on name-collision merges, not an
exact rate (a same-sex collision is invisible to this test). These are flagged
`PERSON_KEY_AMBIGUOUS = True`, included in every count, and disclosed rather than removed.

**Evidence:** `dashboard.py` Tab 2 Table 9 (PLE match-outcome breakdown, if `PLE_MATCH_OUTCOME` is
present); Tab 8 (Repeat Takers) caption cites the 4.6% collision rate directly.

**Numbers to cite:** 49,086 confirmed passers (`IS_PLE_PASSER`, the only authoritative passer count
— `PLE_YEAR_PASSED`/`PLE_MATCH_METHOD`/`PLE_YEAR_GAP` are diagnostic metadata whose non-null sets do
**not** nest inside `IS_PLE_PASSER`, and must never be used as a passer denominator); 6,148 ambiguous
keys; 110 `PLE_YEAR_UNCERTAIN` confirmed passers whose PLE year could not be pinned down (still
counted as passers, excluded from any year-specific figure).

### 2.3 Pipeline 3 — Statistical Analysis (`3_NMAT_PLE_Analysis.ipynb`)

**What to discuss:** the 13-section analysis this notebook produces (Kruskal-Wallis, Mann-Whitney,
chi-square, with effect sizes reported alongside every p-value and Dunn post-hoc correctly
Bonferroni-corrected). Feeds Tab 3, Tab 7, and Tab 11 of the dashboard directly.

**Evidence:** `dashboard.py` Tab 11 (Statistical Tests) — the tab where every test surfaces with its
effect size.

**Caveat:** this is the one component of the pipeline chain with essentially no open findings against
it — say so plainly rather than manufacturing a caveat that doesn't exist.

### 2.4 Pipeline 4 — Citizenship Integration (`4_Citizenship_Integration.py`)

**What to discuss:** the 3-tier hierarchy — Tier 1 (`REAL_FOREIGNERS.csv`, ground-truth ministry
data, split into 1a "known nationality" and 1b "confirmed foreign, ambiguous nationality" →
"Foreign (unspecified)"), Tier 2 (name-based pseudo-citizenship inference,
`pseudo_citizenship_profiling_FINAL.csv`), Tier 3 (default Filipino).

**What "Verified" vs "Likely" foreigner can and cannot support:** `FOREIGNER_STATUS == "Verified
Foreigner"` traces to ground-truth Tier 1 records and can be cited with confidence. Tier 2's
name-based inference is a plausibility estimate, not a confirmation — never state a Tier-2 count with
the same certainty as Tier 1, and never merge the two into one "foreigner" figure without saying which
tier(s) it includes.

**Numbers to cite:** best-record verified foreigners **24,069** (out of 134,869 — this is the
person-level, deduplicated figure used by `UNDERGRAD_UNI_TYPE`-adjacent analysis); all-rows verified
foreigners **32,501** (18.2% of 178,927 sittings — this is the row-level figure used when discussing
raw application volume, not people). Report which denominator you're using every time; they are both
correct, for different questions.

**Evidence:** `dashboard.py` Tab 4's citizenship-profiling block and Tab 5's foreign-examinee summary.

### 2.5 Pipeline 5 — Slim Exodus (`5_Slim_Exodus.py`)

**What to discuss:** the previously-undocumented, hand-maintained 118→53-column slim step is now a
reproducible script with structural (hard-fail) and reference (warn-only) invariant checks, and a
byte-identical three-copy guarantee across `dataset/`, `main_dashboard/`, and
`CHED_relevant_dashboard/` (all three share md5 `28b85ac53af13b4a2ef3ee93527c97c1`, recorded in
`dataset/EXODUS_MANIFEST.json`). This is infrastructure, not a finding — mention it briefly as the
reason the two dashboards can never silently diverge on their source data (they can still diverge on
*computation*, which is a separate concern; see the CHED guide's Pipeline 4/RC-5 discussion).

---

## 3. Results — section by section, mapped to dashboard tabs

For each subsection: what to discuss / evidence source / numbers to cite / caveat.

### 3.1 Descriptive overview (Tab 1 — Executive Summary)

**What to discuss:** overall volume and composition across 2006–2018, median score levels, the
repeat-taker share, and the observable-cohort linkage headline as a single-sentence orientation for
the reader before the detailed tabs.

**Evidence:** Tab 1 Overview/Composition/Quick Tables sub-tabs; Table 1.

**Numbers:** 134,869 unique examinees across 13 years; median TRUE raw score 122.0; median percentile
rank 50.0; 33,713 repeat takers (25.0%); observable cohort 69,503; observable-cohort linkage 45.44%.

**Caveat:** the repeat-taker figure inherits the `PERSON_KEY` collision risk (§2.2) — footnote it here
even though the detailed treatment belongs in §3.8.

### 3.2 Data-quality summary (Tab 2 — Data Integrity)

**What to discuss:** this tab is itself a methods appendix rendered in-app — cohort-definition table,
raw-score validation, and the PLE match-outcome breakdown. Use it as the manuscript's "data quality"
table rather than re-deriving these checks narratively.

**Evidence:** Tab 2 Tables 2, 3, 9.

**Numbers:** 178,927 all rows; 134,869 best-record; 178,882 rows with TRUE raw scores; 69,503
observable best-record; 56,065/99,316 (56.45%) stored-vs-derived mismatch.

**Caveat:** none beyond §2.1's — this section exists to demonstrate the corrections, not add new
claims.

### 3.3 Trends and year-to-year stability (Tab 3)

**What to discuss:** score trends by year, and — importantly — that best-record-filtered *volume*
figures should not be read as a trend in application counts, because the best-record filter removes a
non-uniform share of sittings per year (60–92.6%, non-uniform across 2006–2018). Use `F["trend"]`
(all sittings) rather than `F["besttrend"]` for any statement about *how many people applied* in a
given year; use the best-record cohort only for *score-level* trends.

**Evidence:** Tab 3 Figure 4 caption; Kruskal-Wallis table (H, p, η²) for year-to-year differences in
5 score measures.

**Caveat:** distinguish "fewer distinct examinees are represented by year X's best record" from "fewer
people took the NMAT in year X" — they are not the same statement.

### 3.4 Score-bin distribution and background (Tab 4)

**What to discuss:** the B1–B10 distribution over time and by undergraduate background; the
chi-square association between university type and bin; the citizenship-profiling comparison of
matched-vs-unmatched-PLE examinees (this sub-block is the closest thing to a descriptive equity
profile the dataset supports, and it is explicitly scoped to *examinees who did not link to a PLE
passer record* — not "examinees who failed," see the global linkage-not-pass-rate rule).

**Evidence:** Tab 4's heatmaps, chi-square Table 11, citizenship metrics.

**Numbers:** citizenship-profiling block — 37,381 profiled no-PLE-match records, 5,049 flagged
foreigners, 32,320 Filipinos, 43 distinct citizenship labels among that subset. (These are a different
population than §2.4's headline citizenship figures — this table is restricted to the *no-PLE-match*
subset specifically.)

**Caveat:** the foreigner-vs-Filipino "comparison groups" built later in this tab explicitly mix two
different sampling frames (profiling-matched foreigners vs. all-observable-best-record Filipinos by
undergrad type) — the dashboard's own caption says these are not apples-to-apples samples; repeat that
warning if citing this comparison.

### 3.5 University-type analysis (Tab 5)

**What to discuss:** score distributions by undergraduate institution type (Public/Private/Foreign),
framed explicitly as **applicant-origin** analysis, never institutional performance.

**Evidence:** Tab 5 tables/heatmaps; Table 16 (foreign-examinee summary).

**Numbers:** foreign examinees 1,860 (1.43% of the `uni_base` population in this tab — note this is
yet a third denominator from §2.4/§3.4's figures, restricted here to rows with both type and location
present); median percentile among them 52.0; top-bin (B8–B10) share 34.30%.

**Caveat — this is RC-4, the scope ceiling, and it must appear here explicitly:** `UNDERGRAD_UNI_TYPE`
is the undergraduate institution's public/private status, and it is **not** a SUC/PHEI proxy for
medical-school regulatory purposes — that classification applies to the medical school, which this
dataset does not identify. Do not title any subsection here "institutional performance"; call it
"applicant-origin composition" or similar.

### 3.6 Flow and pathways (Tab 6)

**What to discuss:** Sankey-style flow from background (university type, course group) into score bin,
and from score bin into PLE status within the observable cohort — a compact visual complement to
§3.4/§3.7's tables, useful for a figure but the underlying numbers are the same tables already cited
elsewhere. Cite the table, not just the diagram, per the export-format contract's "every visual is
data" rule.

**Evidence:** Tab 6's four flow tables (18–21).

**Caveat:** the Bin→PLE flow is restricted to the observable cohort (69,503) — state that scope in the
figure caption, not just in prose.

### 3.7 PLE alignment (Tab 7) and 3.12 Policy tables (Tab 12)

**Discuss these two together** — they compute the same three aggregations (alignment by year, by
pre-med background, by university type) independently in two places in the code. Cite whichever is
more convenient for the manuscript's flow, but if both are shown side by side in a draft, they must
agree; if they don't, that is a code regression, not a legitimate second estimate (see
`docs/HANDOFF_TESTING_GUIDE.md` §3).

**What to discuss:** the individual-level linkage gradient by score bin — the single relationship this
dataset can speak to most directly — and the score-profile difference between confirmed passers and
no-confirmed-match examinees (Mann-Whitney, with effect size).

**Evidence:** Tab 7 Tables 23–30; Tab 12's four tables + Table 30-equivalent.

**Numbers:** the corrected B1–B10 linkage gradient (§below) and its year-over-year, background-level
breakdowns from Tables 28–30.

**Caveat — the selection-effect confound, mandatory wherever the gradient is cited:** linkage rises
across the bin scale, but the historical non-uniform school-level admission cutoffs mean low-bin
examinees were **partly never admitted** to medical school at all — their low linkage rate partly
measures non-admission, not later failure to be linked. **The gradient cannot be used to estimate how
many additional passers a new uniform cutoff would produce or exclude.** State this every time the
gradient supports a claim about cutoff policy, not just once in a methods footnote.

### 3.8 Repeat takers (Tab 8)

**What to discuss:** attempt-count distribution and score change on repeat attempts — but lead with
the identity-key caveat before any headline percentage, not after.

**Evidence:** Tab 8's attempt-count table, trajectory summary, and its own caption.

**Numbers:** 33,713 repeat takers (25.0% of unique examinees) — this arithmetic is correct at the
stated precision. **What is not defensible is treating that 25% as a clean count of genuine repeat
attempts.** 4.56% of all `PERSON_KEY`s show contradictory SEX (a detectable-only lower bound on
name-collision merges); among repeat-taker keys specifically the detectable collision rate is higher,
and scaling for undetectable same-sex collisions (Filipino given names are strongly gendered, which
biases the scaling *downward*, i.e. the true rate is higher still) implies the genuine-repeat share of
the 25% could be overstated by a third or more.

**Caveat:** do not publish a repeat-taker headline number without this caveat attached in the same
sentence or the immediately following one — this is the single largest identity-integrity risk in the
dataset and belongs next to the number, not in a distant limitations section.

### 3.9 Subtests and profiles (Tab 9)

**What to discuss:** standardized subtest profiles (radar charts) by university type and course
group — descriptive, methodologically clean, inherits only the best-record deduplication.

**Evidence:** Tab 9's heatmaps and radar figures.

**Caveat:** same RC-4 framing as §3.5 — "by university type" means by undergraduate origin.

### 3.10 Year gap and gender (Tab 10)

**What to discuss:** the NMAT-to-PLE year gap distribution among confirmed passers, and score
patterns by sex — including the explicit "(not specified)" SEX category, which now surfaces as its
own group rather than silently vanishing from filtered counts (a historical bug, fixed; see
`docs/HANDOFF_TESTING_GUIDE.md` §7).

**Evidence:** Tab 10's year-gap metrics and Table 40/41/42.

**Numbers:** 29,519 confirmed passers with a determinable year gap; median gap 6 years (Q1 6, Q3 7).

**Caveat:** the year-gap analysis is confined to confirmed passers by construction — it cannot speak
to time-to-outcome for non-linked examinees, because "non-linked" includes both people who have not
yet passed and people who never will, indistinguishably.

### 3.11 Statistical tests (Tab 11)

**What to discuss:** formal significance tests behind the descriptive claims in §3.3, §3.7, §3.9 —
Kruskal-Wallis by year, Mann-Whitney by PLE status, chi-square for university-type/bin association,
Dunn post-hoc (Bonferroni-corrected) where applicable.

**Evidence:** Tab 11's four sub-tabs.

**Caveat:** report effect sizes (η², rank-biserial r, Cramér's V) alongside every p-value — the
dashboard already does this; the manuscript should not drop them even under space pressure, since a
large-N dataset like this one makes p<0.001 nearly automatic and uninformative on its own.

### 3.13 CHED Compliance tab (Tab 13) — treat as a bridge section, not a duplicate manuscript

**What to discuss:** this tab exists specifically to state what the dataset can and cannot tell CHED,
plus three self-contained analyses (cut-off scenario table, foreign/Filipino composition, individual
linkage gradient). If the main-dashboard manuscript touches CMO policy at all, source it from here and
cross-reference `docs/MANUSCRIPT_GUIDE_CHED_DASHBOARD.md` for the full policy treatment rather than
duplicating it.

**Evidence:** Tab 13 Sections A–C.

**Numbers:** the corrected linkage-by-bin gradient — B1 11.6% (795/6,853), B2 22.7%, B3 29.3%, B4
36.0%, B5 45.6%, B6 50.4%, B7 53.6%, B8 55.0%, B9 61.6%, B10 71.0%.

**Caveat:** carry both the selection-effect caveat (§3.7) and the RC-4 scope ceiling (§3.5) here
explicitly — this is the tab most likely to be screenshotted into a policy conversation, so it cannot
rely on caveats stated only in earlier tabs.

### 3.13a The one finding strong enough to lead with

**What to discuss:** the single most defensible result in the project, and the one that should carry
the manuscript's headline. Of the **25,596** observable-cohort examinees who scored below the 40th
percentile, **6,173 (24.1%)** are confirmed PLE passers — **795** of them in B1, the lowest decile.
Under a uniformly enforced 40th-percentile floor those people should barely exist. They do exist, in
volume, which says the historical floor was **not uniformly binding** across the schools examinees
actually attended between 2006 and 2014. That is a direct, data-supported observation about the
premise of CMO §IV.B.1, and unlike the linkage gradient it does not require any counterfactual.

**Evidence:** Tab 7 (PLE Alignment) and Tab 13; reproduce with
`IS_BEST_OBSERVABLE_RECORD & (NMS_PER_num < 40)` and `IS_PLE_PASSER`.

**Why it survives attack — state all three, they are what makes it publishable:**
- Identity collisions do not explain it: the `PERSON_KEY_AMBIGUOUS` rate among these 6,173 is
  **3.0%**, *below* the observable cohort's own **3.5%** base rate. If they were collision artefacts
  the rate would be higher, not lower.
- Citizenship does not explain it: **6,152 of 6,173** are Filipino.
- A single anomalous year does not explain it: they are spread across **all nine** observable years,
  2006–2014.

**Caveat:** this establishes that the floor was not uniformly applied. It does **not** estimate how
many additional passers a new uniform cutoff would produce or exclude — that requires the
counterfactual the selection-effect confound (§3.7) rules out. Keep the two claims separate.

---

## 4. Discussion and limitations

**What to discuss:** synthesize the caveats already stated per-section rather than introducing new
ones here — a limitations section that repeats known caveats in one place is more useful than one that
invents new hedges. Minimum required list: linkage-vs-pass-rate; the `PERSON_KEY` identity-collision
risk and its effect on repeat-taker and best-record counts; the undergraduate-vs-medical-school scope
ceiling; the selection-effect confound on the linkage gradient; the two disclosed-and-fixed PLE
matcher defects (RC-0, O-24) and what moved as a result.

**Caveat on caveats:** do not let this section imply the whole dataset is unreliable — the raw-score
recalculation, the citizenship pipeline, and the statistical-test methodology are all sound (§2.1,
§2.3, §2.4). Distinguish "fixed and now trustworthy" from "structurally unfixable and must be
disclosed every time" (the identity-key and scope-ceiling issues fall in the second category; the
stored-total and matcher issues fall in the first).

---

## 5. Claims that were withdrawn and must not be repeated

An earlier version of this analysis reported a **21-point "policy discontinuity"** in PLE linkage
between bin B4 and bin B5 — exactly at the 40th percentile — and proposed a regression-discontinuity
design around it. **This finding was withdrawn.** After fixing RC-0 (the matcher's hard 40th-percentile
floor, §2.2), the corrected B4→B5 step is **9.6 points**, in line with B1→B2 (+11.1) and B9→B10
(+9.4) — not an outlier among the nine consecutive bin-to-bin steps:

```
B1->B2 +11.1   B2->B3 +6.6   B3->B4 +6.7   B4->B5 +9.6   B5->B6 +4.8
B6->B7 +3.2    B7->B8 +1.4   B8->B9 +6.6   B9->B10 +9.4
```

The original 21-point jump was **largely an artefact of the project's own matching code**, not a
signal of a real admission discontinuity. Do not resurrect the discontinuity framing or the
regression-discontinuity recommendation built on it in any new draft. If a reader asks why an earlier
version of this work made that claim, the honest answer is that it was found to rest on a bug in the
identity-matching pipeline, discovered and corrected during remediation — say so rather than quietly
dropping the topic.
