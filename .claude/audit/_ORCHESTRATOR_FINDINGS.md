# Orchestrator's own verified findings (independent of subagents)

All run by the orchestrator against `dataset/NMAT_Exodus.parquet` with `./.venv/Scripts/python.exe`.
These are CONFIRMED — each has a reproducible snippet. Use these to arbitrate subagent claims.

---

## O-1 [CRITICAL] `IS_PLE_ANALYSIS_SAFE` is a byte-for-byte duplicate of `IS_PLE_PASSER`

```python
(df.IS_PLE_ANALYSIS_SAFE == df.IS_PLE_PASSER).all()   # True
(df.IS_PLE_ANALYSIS_SAFE == (df.Year <= 2014)).all()  # False
```
Documented meaning is "observable cohort: Year <= 2014". It is not that. It is True for
4,288 rows in 2015, 3,673 in 2016, 1,136 in 2017, 19 in 2018.

**Consequence:** any rate whose denominator is filtered on `IS_PLE_ANALYSIS_SAFE` and whose
numerator is `IS_PLE_PASSER` returns **100% by construction**. Every "observable cohort pass
rate" in the repo is suspect until proven otherwise.

---

## O-2 [CRITICAL] `IS_BEST_NMAT_RECORD` is broken, and it fails non-randomly toward passers

```
PERSON_KEYs with exactly one True : 133,312
PERSON_KEYs with ZERO True        :   1,311   <-- these people vanish from every "unique people" count
PERSON_KEYs with MORE than one    :     246   <-- these people are double-counted
sum(IS_BEST_NMAT_RECORD) = 133,804   vs   nunique(PERSON_KEY) = 134,869   (deficit 1,065)
```

The 1,311 zero-best people own 1,497 rows, and **1,497 of 1,497 (100%) are `IS_PLE_PASSER == True`**,
concentrated in 2009 (691) and 2010 (478).

**Consequence:** this is not a rounding error. Best-record filtering silently deletes ~1,300
confirmed PLE passers and double-counts 246 more people. Every best-record-filtered PLE pass
rate in both dashboards is **biased downward**, and every "unique examinees" headline is wrong
by 1,065. Docs assert the rule is "latest year -> highest percentile -> earliest attempt";
whatever is implemented does not satisfy it.

---

## O-3 [CONFIRMED] Percentile bin orientation: **B1 is the LOWEST decile**

| Bin | NMS_PER_num range | mean TotalRawScoreTRUE |
|-----|-------------------|------------------------|
| B1  | 0-9   | 75.1  |
| B2  | 10-19 | 90.9  |
| B3  | 20-29 | 101.1 |
| B4  | 30-39 | 109.5 |
| B5  | 40-49 | 117.5 |
| B6  | 50-59 | 125.4 |
| B7  | 60-69 | 133.7 |
| B8  | 70-79 | 143.1 |
| B9  | 80-89 | 155.2 |
| B10 | 90-99 | 175.5 |

Monotonic in raw score, so unambiguous. **B1 = weakest, B10 = strongest.** Any narrative that
reads B1 as "top decile" inverts its own conclusion. Cut-off analyses concern B1-B4.

---

## O-4 [CONFIRMED] The documented "42.2% of stored raw totals are wrong" figure is itself wrong

```
StoredRawTotal non-null           :  99,316 of 178,927 (55.5%)
StoredRawTotal != TotalRawScoreTRUE:  56,065
  = 56.45% of rows that HAVE a stored total
  = 31.33% of all rows
```
Neither figure is 42.2%. The claim needs restating with its denominator named.

Positively: `TotalRawScoreTRUE` arithmetic is **clean** — 0 mismatches against the sum of the 8
`Raw_*` components, and 0 mismatches for `PartIRawScoreTRUE + PartIIRawScoreTRUE == TotalRawScoreTRUE`,
across all 178,882 non-null rows. The recalculation itself is sound; only its documentation is wrong.

---

## O-5 [CONFIRMED] Three (four) mutually inconsistent PLE linkage counts

```
IS_PLE_PASSER == True        : 49,986
PLE_YEAR_PASSED   non-null   : 54,528
PLE_MATCH_METHOD  non-null   : 57,304
PLE_YEAR_GAP      non-null   : 48,842
```
Differences: 57,304 - 54,528 = 2,776 = exactly the `MANUAL_APPNO_MATCH` count.
54,528 - 49,986 = 4,542 unexplained.
Match methods: EXACT 54,437 | MANUAL_APPNO_MATCH 2,776 | DETERMINISTIC_APPNO 91 | null 121,623.

---

## O-6 [CONFIRMED] All three parquet copies are byte-identical

md5 `8034a0e72e1ff4d4e3e0334e91c4bccf`, 11,007,467 bytes, at `dataset/`,
`streamlit_dashboard/main_dashboard/`, `streamlit_dashboard/CHED_relevant_dashboard/`.
No drift *today* — but three uncontrolled copies is a latent divergence hazard.

---

## O-7 [CONFIRMED] Phantom columns in the documentation

`PERSON_NAME`, `PLE_MATCH_STATUS`, `IS_BOARD_OBSERVABLE_COHORT` are documented in `CLAUDE.md`
and `docs/data_dictionary.md` but **do not exist** in the 54-column parquet. Note the absence of
`PERSON_NAME` specifically undermines any name-based forensic cross-check run against this parquet.

---

## O-8 [CONFIRMED] Dead and mistyped columns

- Constant (nuniq=1, carry zero information): `AllRawComponentsPresent`, `CalcVsDerivedMismatch`
- Stored as `str` but semantically boolean: `HasCEMMatch`, `HasTRUErawScores`,
  `StoredVsDerivedMismatch`, `AllRawComponentsPresent`, `CalcVsDerivedMismatch`
  -> `bool("False") is True`, so any truthiness test on these is silently inverted.
- `APPNO_CLEAN`: 178,926 unique over 178,927 rows — one duplicate.
- `name_based_assessment`: non-null for only 871 of 178,927 rows (0.5%).

---

## O-10 [CRITICAL — highest-impact finding of the audit] `UNIVERSITY` is the applicant's UNDERGRADUATE school, not their medical school

Proof: **UP Diliman has no College of Medicine** (UP's MD program is at UP Manila). Yet:
```
UNIVERSITY == 'UNIVERSITY OF THE PHILIPPINES - DILIMAN' : 4,421 rows
   of which IS_PLE_PASSER == True                       : 1,914
```
1,914 physicians cannot have graduated from a medical school that does not exist. Corroborating:
`CourseGroup` for these rows is a *bachelor's* degree field — Education (316),
Engineering & Technology (37), Social & Behavioral Sciences (819). NMAT is taken *after* the
bachelor's degree, so `UNIVERSITY` + `CourseGroup` describe the **pre-med undergraduate origin**.
Ateneo de Manila (939) and DLSU Manila (2,979) — neither had an MD program in this period — appear
for the same reason.

**Consequence for the CHED deliverable:** CMO Section IV.B.1.b ties a PHEI's right to a 30th-percentile
cut-off to *that PHEI's own PLE performance*. Any institution-level PLE rate computed from
`UNIVERSITY` in this dataset attributes each doctor's licensure outcome to the university where
they did their **undergraduate degree**, not the medical school that trained them. Such a metric
does not measure what the CMO regulates. **The dataset cannot produce a CMO-compliant institutional
PLE passing rate at all** — the med-school identifier simply is not present.

## O-11 [MEDIUM] `NMA_College` is a redundant duplicate of `UNIVERSITY`

Identical for 92.9% of rows exactly, and 100% once punctuation is normalised — the only
differences are casing and stripped commas (`"University Of San Carlos, Cebu City"` vs
`"UNIVERSITY OF SAN CARLOS CEBU CITY"`). 12,681 rows differ on punctuation alone.
Two near-identical free-text columns with different cardinality (2,907 vs 3,251 distinct) is a
grouping hazard: grouping by one gives different institution counts than the other.
(Checked for encoding corruption — none; earlier apparent mojibake was console rendering only.)

## O-18 [ARBITRATION] The observable-cohort definitional ladder — a correction to auditor 04

Auditor 04 reported the dashboard's 45.38% should be **47.28%**, a "+1.90 pp undercount". My own
reconstruction does not support a swing that large. The full ladder for Year <= 2014:

| # | Definition | Count | Linkage rate |
|---|---|---|---|
| a | all rows (sittings) | 88,144 | — |
| b | unique PERSON_KEY | **69,503** | **45.76%** |
| c | unique PERSON_KEY with non-null percentile | 68,746 | 45.40% |
| d | best-record **rows** | 64,501 | ~45.38% (dashboard / CHED doc path) |
| e | best-record **unique** PERSON_KEY | 64,312 | 45.49% |

Two conclusions, and the distinction governs how alarmed to be:

1. **The linkage *rate* is robust.** Every defensible denominator lands in 45.4-45.8%. The
   best-record bug does not materially distort the headline rate, because it removes numerator and
   denominator roughly proportionally. Auditor 04's 47.28% rests on a dedup yielding n=64,531, which
   matches none of the definitions above; I could not reproduce it and am not adopting it.
2. **The published *population count* is genuinely wrong.** "Observable cohort (Year<=2014) = 64,501"
   is a count of best-record **rows** presented as a count of **people**. The true number of people
   is **69,503** — understated by 5,002 (7.2%). Same error class as O-14's 133,558 vs 134,869.

Correct framing for the report: **rates survive, counts do not.** Sentences of the form "N examinees"
are wrong; sentences of the form "X% of the cohort" are approximately right. State this explicitly so
the user does not over-correct and rewrite conclusions that are actually sound.

## O-12 [REFERENCE] Corrected headline figures — use these to check every dashboard number

```
exam sittings (rows)                      178,927
unique examinees (nunique PERSON_KEY)     134,869
rows flagged IS_BEST_NMAT_RECORD          133,804   <- wrong, should equal 134,869

TRUE observable cohort (Year <= 2014):
  sittings                                 88,144
  unique people                            69,503
  PLE-linked rows                          40,870
  linkage rate among unique people          45.76%

If IS_PLE_ANALYSIS_SAFE is (incorrectly) used as the cohort filter:
  rows 49,986, of which IS_PLE_PASSER 49,986  ->  100.0% by construction
```

### Person-level PLE linkage by candidate cut-off (Year<=2014, one row per person, highest percentile)
n = 68,746 unique people with a percentile.

| Cut-off | At/above: n | linked | Below: n | linked |
|---|---|---|---|---|
| 30th | 49,623 | 57.3% | 19,123 | 14.2% |
| 40th | 43,150 | 62.0% | 25,596 | 17.2% |
| 50th | 36,568 | 64.8% | 32,178 | 23.2% |

### Linkage rate by percentile bin (same cohort)
| Bin | linked | n | rate |
|---|---|---|---|
| B1 | 556 | 6,853 | 8.1% |
| B2 | 939 | 5,884 | 16.0% |
| B3 | 1,224 | 5,813 | 21.1% |
| B4 | 1,677 | 6,473 | 25.9% |
| B5 | 3,080 | 6,582 | **46.8%** |
| B6 | 3,327 | 6,284 | 52.9% |
| B7 | 3,691 | 6,359 | 58.0% |
| B8 | 4,107 | 6,704 | 61.3% |
| B9 | 4,942 | 7,263 | 68.0% |
| B10 | 7,623 | 9,958 | 76.6% |

## O-13 [CRITICAL INTERPRETATION] The B4->B5 jump is the existing policy, not ability

Linkage rises smoothly across B1-B4 (8.1 -> 25.9) and B5-B10 (46.8 -> 76.6), but **jumps 21 points
between B4 and B5** — precisely at the 40th percentile, which is the mandatory cut-off already
imposed by CMO No. 18 (s. 2016) Section 17.5.

The mechanism is admission, not aptitude: people below the 40th percentile were largely *barred
from enrolling in medical school at all*, so they could never appear as PLE passers. Their low
linkage rate measures **non-admission**, not failure.

Two consequences, both central to the deliverable:

1. **Any "students below the cut-off still pass the PLE" argument is computed on a
   heavily-selected residual** — the atypical few who were admitted below 40 despite the rule
   (exemptions, foreign applicants, pre-2016 practice, data error). They are not representative of
   the below-cut-off population, so no conclusion about lowering the cut-off to the 30th percentile
   follows from them. This is the bias that most threatens the published brief.

2. **It also creates a genuine opportunity.** A sharp, policy-induced discontinuity at a known
   threshold is the textbook setting for a **regression discontinuity design**. Comparing outcomes
   just above vs just below the 40th percentile is the one defensible way this dataset can speak to
   the causal effect of the cut-off. This should be the headline recommendation for new analysis —
   it is within scope, uses only existing columns, and answers the actual policy question.

## O-14 [CONFIRMED] Three published CHED numbers are wrong, traced to O-2

From `complete_markdown/CHED_NMAT_Dashboard_Complete.md`:

| Line | Published | Actual | Cause |
|---|---|---|---|
| 534 | Unique examinees (best record) **133,558** | **134,869** | the 1,311 zero-best people (O-2) |
| 535/571 | Observable cohort Year<=2014 **64,501** | **69,503** | same, plus best-record filter |
| 543 | "**42.2%** of stored totals were incorrect" | **56.45%** of the 99,316 rows that have a stored total | wrong denominator |

The 42.2% is internally inconsistent *within the same document*: line 594 reports 56,065 mismatches,
and 56,065/133,558 = 41.98% ~ the quoted 42.2% — i.e. the count of mismatched rows was divided by
the count of *unique best-record examinees*, two different populations. The defensible statement is
"56,065 of the 99,316 records that carry a stored total (56.5%) disagree with the recalculated total."

Note 64,312 (best-record & Year<=2014 unique) is also not 64,501, so the published cohort figure
does not reproduce under either definition — a third, undocumented filter is in play.

## O-15 [MEDIUM] The best-record rule differs by PLE status, and the docs describe neither version

`CHED_NMAT_Dashboard_Complete.md:557` states the real rule: *"For PLE passers: the specific NMAT
attempt that matched to the PLE record. For others: the highest percentile attempt."* This
contradicts `CLAUDE.md`/`docs/`, which claim "latest year -> highest percentile -> earliest attempt".
Neither document describes what is actually implemented for both groups.

Measured on repeat takers (n=33,733):

| Group | best == highest-percentile attempt | mean shortfall when not |
|---|---|---|
| Not PLE-linked | 99.3% | 19.3 pctile pts |
| PLE-linked | 90.7% | 8.1 pctile pts |

So the two groups being compared are selected by **different rules**. Effect on the selected record's
mean percentile: passers 72.60 (vs 73.36 if max-selected), non-passers 42.94 (vs 43.08).

**Direction: conservative.** Passers are understated by ~0.76 points and non-passers by ~0.14, so
the differential slightly *shrinks* the observed score-outcome gradient. It does not manufacture the
gradient — good news for the headline conclusion. But an inconsistent selection rule across compared
groups is indefensible on principle and must be disclosed or made uniform. It is also almost
certainly the mechanism behind the 1,311 zero-best passers in O-2: where the matched attempt could
not be identified, no record got flagged.

## O-16 [CONFIRMED — I independently reproduced auditor 06's drift finding, and found a second bug in the same metric]

Auditor 06 reported the live dashboard shows Public/Private **56/48** while the exported document
publishes **57/49**, caused by `export_markdown.py` filtering out null `PercentileBin` where
`dashboard.py` does not. Independently reproduced:

```
best-record, no PercentileBin null-filter  ->  Public 56, Private 48   (dashboard)
best-record, PercentileBin null-filter     ->  Public 57, Private 49   (export)
null PercentileBin among best-record rows  ->  3,069
```
`CHED_NMAT_Dashboard_Complete.md:491` publishes 57/49. **Drift confirmed.**

**Second, separate bug in the same sentence:** the metric is labelled *"median bin rank"*, but 57 and
49 are on the 0-99 percentile scale — they are the median of `NMS_PER_num`. An actual median *bin
rank* is 6 and 5 (bins run B1-B10). So the published sentence attaches a percentile value to a
bin-rank label. A policy reader seeing "median bin rank 57" against a 10-bin scheme has no way to
interpret it. Both the number and its name need fixing.

Compounding this with O-10: `UNI_TYPE` here describes the **undergraduate** institution, so the true
statement is "applicants who did their bachelor's at public universities have a higher median NMAT
percentile (57) than those from private universities (49)" — a statement about applicant origin, not
about any medical school's performance. The current heading, *"Institutional Performance Patterns"*,
invites exactly the wrong reading.

## O-17 [CRITICAL] `PERSON_KEY` is a weak identity key — it merges distinct people

`PERSON_KEY` is `"SURNAME, GIVEN NAMES" + "||" + birthdate`. Two structural problems:

```
rows whose birthdate component is EMPTY : 25,204 of 178,927 (14.09%)
distinct non-empty birthdate values     : 10,725        <- implausibly few; not a full date
distinct names                          : 123,736
distinct PERSON_KEY                     : 134,869       <- DOB adds only 11,133 of discrimination
```
For 14% of rows the key degenerates to **name only**. Even where present, the birthdate field takes
only 10,725 distinct values across ~154k rows, so it is coarse (likely year or a partial date) and
adds little separating power.

Direct evidence that distinct people are being merged:
```
PERSON_KEYs with contradictory SEX      :  6,148 of 134,869 (4.56%), spanning 16,020 rows
  of which also span >1 UNIVERSITY      :  5,051
names carrying both sexes               : 10,172
```
One person does not have two sexes and two undergraduate universities. These are collisions —
common Filipino names colliding, which is exactly the failure mode a name-based key invites.

**Impact, and it is broad:**
- **Repeat takers**: 33,714 keys have >1 row and are reported as "25% repeat takers". 6,148 of those
  (**18.2%**) have contradictory SEX, so a substantial share of the headline repeat-taker figure is
  name collisions, not genuine repeat attempts. Every number on the repeat-taker page inherits this.
- **Best-record dedup**: collapsing two people into one key deletes one of them from every
  person-level count. This compounds O-2.
- **PLE linkage**: a collision can attach one person's PLE record to another's NMAT score.

This is the deepest defect found. It is not fixable by editing a dashboard — it requires either a
stronger key from upstream identifiers, or an explicit, disclosed uncertainty band on every
person-level figure.

### Estimating the true collision rate

4.56% is only the *detectable* rate — a collision is visible to this test only when the two merged
people differ in sex. With the observed split (Female 56.6% / Male 43.4%), two independently drawn
people differ in sex with probability 2(0.566)(0.434) = **0.491**. Scaling up:

```
observed detectable collisions       :  4.56%  of keys  (6,148)
implied true collision rate          : ~9.3%   of keys  (~12,514)
among claimed repeat takers: observed: 18.2%  ->  implied ~37%
```

**This is still a lower bound, and materially so.** The scaling assumes sex is independent of name,
but Filipino given names are strongly gendered — two people colliding on a name are far *more* likely
than chance to share a sex, which pushes the detection probability below 0.491 and the true collision
rate above 9.3%. It also assumes collisions merge only two people; three-way merges are undercounted.

**Bottom line: the "25% of examinees are repeat takers" headline is not defensible.** A substantial
minority — plausibly a third or more — of those "repeats" are two different people sharing a name.
The repeat-taker page should not ship until the key is fixed or the figure is presented as a bounded
range with the collision caveat stated inline.

## O-19 [CRITICAL — the flagship example] A chart series mathematically incapable of being non-zero

Independently reproduced from auditor 05's F01, on the shipped CHED parquet:

```python
clean = df[df.IS_PLE_ANALYSIS_SAFE == True]      # 49,986 rows
(clean.IS_PLE_PASSER == True).sum()              # 49,986
(clean.IS_PLE_PASSER == False).sum()             # 0   <- the "No confirmed PLE match" series
per-year no-match counts 2006..2014              # 0,0,0,0,0,0,0,0,0
```

Because `IS_PLE_ANALYSIS_SAFE` **is** `IS_PLE_PASSER` (O-1), filtering on the first and then
splitting by the second is a tautology. Consequences in the shipped deliverable:

- **Tab 2, "B5+ PLE-Passer Composition by Year"** — a stacked bar chart whose legend advertises a red
  *"No confirmed PLE match"* category that can never render a single pixel, in any year, ever.
- **Tab 3, "Clean PLE Subset Stress Test"** — a line chart pinned at a flat 100% across all nine years.
- **Tab 5, Finding 6** — narrates that flat line as evidence *"confirming robustness"* of the PLE
  matching. It confirms nothing. A tautology cannot serve as a robustness check; it passes
  identically whether the matching is perfect or entirely broken.

Lead the report with this. It is unambiguous, trivially reproducible, visible to any reader who
looks at the chart legend, and it currently sits in a document informing national medical-admissions
policy. It is duplicated verbatim in `export_markdown.py`, so it propagates into the exported
markdown and the PDF brief.

## O-20 [HIGH] The self-verification suite provides false assurance

Auditors 05 and 06 independently established that `verified_true/` verifies nothing: the verifiers
never import `ched_compute/0X.py`, never diff against `page_results/*.md`, and instead reimplement
the logic a fourth time and compare it against a **hand-typed `expected = {...}` dict**. A verifier
whose expectations are transcribed from the output it checks cannot fail.

Concretely: `CONSOLIDATED_VERIFICATION_REPORT.md` certifies the string-boolean dtype bug as
"FIXED in commit 619a150", but `git show --stat 619a150` touched only `dashboard.py` — no
`ched_compute/*` file. The bug is still live in `ched_compute/06_data_limitations.py`, and its
committed output reads *"Rows with complete TRUE scores: 0 (99.97%)"* — a self-contradicting line a
genuine verifier would have caught instantly.

This matters beyond the individual bugs. A directory named `verified_true/` and a file named
`CONSOLIDATED_VERIFICATION_REPORT.md` are exactly what would persuade a reviewer that the numbers had
been checked. That assurance is unearned, which makes it worse than no assurance at all.

## O-9 [CONFIRMED] Everything compiles

`main_dashboard/dashboard.py` (3,207 lines), `CHED_relevant_dashboard/dashboard.py` (1,262 lines),
`export_markdown.py` (834 lines), `4_Citizenship_Integration.py` all pass `py_compile`.
No tests exist anywhere in the repo. Failures here are semantic, not syntactic.
