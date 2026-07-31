# NMAT Analysis — Comprehensive Audit & Remediation Plan

**Date:** 2026-07-31
**Scope:** full repository, all 47 commits since initialisation, both live Streamlit dashboards, the
citizenship pipeline, the export/compute chains, the forensic audit suite, and all documentation.
**Method:** 12 parallel specialist auditors, every finding independently re-verified by the
orchestrator against `dataset/NMAT_Exodus.parquet` before inclusion here.
**Nothing in this document was fixed.** This is diagnosis plus an implementation plan.

Supporting per-area reports live in `.claude/audit/`. The orchestrator's own directly-verified
findings are in `.claude/audit/_ORCHESTRATOR_FINDINGS.md`.

---

## 0. How to read this document

Read §1 and §2 first — they answer the question you actually asked. §3 is the causal core: five
defects generate roughly forty symptoms, so fixing five things fixes most of the list. §4 is the full
register. §5 is the page-by-page completeness inventory you asked for. §6 is the scope boundary
against the CHED CMO. §7 is a reference card of corrected numbers. §8 is the plan, with commits.

Every claim carries evidence. Where auditors disagreed with each other or with me, I say so and give
the arbitration rather than quietly picking one.

---

## 1. Verdict at a glance

| Component | Verdict | One-line reason |
|---|---|---|
| **Citizenship pipeline** (`4_Citizenship_Integration.py`) | **Sound** | 3-tier joins are clean, zero row inflation, India surge is 99.996% ground-truth backed |
| **Parquet slimming** (118 → 54 cols) | **Safe** | All 54 surviving columns byte-identical to `.bak`; no consumer references a dropped column |
| **Raw-score recalculation** | **Sound** | 0 arithmetic mismatches across 178,882 rows; only its *documentation* is wrong |
| **Statistical tests** (main dash tab 11) | **Sound** | Effect sizes reported, Dunn post-hoc correctly Bonferroni-corrected |
| **PLE linkage** | **Fragile** | 4 non-nested counts (resolved §4.1); identity key collides; disambiguator tie-break is circular |
| **`data_aggregator/`** | **Keep & fix** | Reproduces byte-for-byte; 11/13 pages match; 5 contained bugs |
| **Pipeline 1 (cleaning)** | **Sound, one caveat** | Scores/bins correct, but `rapidfuzz` survives in university matching (H-16) |
| **Pipeline 2 (PLE match)** | **Origin of RC-1** | `analysis_safe` set == `accepted_statuses`; wrong since first run |
| **Main dashboard** (13 tabs) | **Needs fixes** | ~125 elements inventoried; 12 CRITICAL findings |
| **CHED dashboard** (6 tabs) | **Not fit to ship as-is** | Tautological charts; wrong published counts; fixes are contained, not a rebuild |
| **CHED export chain** | **Drifted** | 4 parallel implementations of the same numbers; confirmed disagreement |
| **`verified_true/` QA suite** | **Provides false assurance** | Verifiers compare against hand-typed expectations; cannot fail |
| **Forensic audit** | **Partly invalid** | Core arithmetic reproducible; the "4 mismatches" headline does not hold up |
| **Documentation** | **20 of 44 claims wrong** | Including three phantom columns and a broken documented command |
| **Nested deploy repo (CHED)** | **CRITICAL** | 11+ commits behind parent; may be serving stale code to stakeholders |
| **Tests** | **None exist** | Zero automated tests anywhere at HEAD |

---

## 2. Answering your actual question

You asked whether you performed the analysis correctly. The honest answer has three parts.

### 2.1 What you got right — and it is more than you think

Your instinct to doubt yourself has been productive, but it should not become blanket distrust.
Several things that were genuinely hard, you got genuinely right:

- **The citizenship pipeline works.** You specifically doubted this. It is the most solid component
  in the repository. The 3-tier hierarchy joins on unique keys, preserves 178,927 rows at every step,
  and the tier counts sum exactly. The India surge that looks alarming (26,491 records, rising from
  44 in 2006 to 6,373 in 2017) is **99.996% backed by `REAL_FOREIGNERS.csv` ground truth**, not by
  inference. It is a real phenomenon, correctly measured.
- **The raw-score recalculation is arithmetically perfect.** `TotalRawScoreTRUE` equals the sum of
  its 8 components for all 178,882 non-null rows — zero exceptions — and
  `PartI + PartII == Total` likewise. Your decision to distrust `StoredRawTotal` was correct.
- **The parquet slimming was safe.** All 54 surviving columns are byte-identical to the 118-column
  backup, and no consumer anywhere references a dropped column.
- **Your statistical tests are methodologically sound.** Effect sizes (η², rank-biserial r,
  Cramér's V) accompany every p-value, and the Dunn post-hoc correctly applies Bonferroni. This is
  better practice than most published work in this space.
- **Your scope discipline in the CHED deliverable is genuinely good.** The dashboard says "this is
  NOT a PLE pass rate" in four separate places, refuses to assign compliance labels to institutions,
  and has an honest limitations tab that correctly names GIDA/IP, enrolment, and composite-ranking
  as out of scope. That is the hardest thing to get right in policy analytics and you got it right.
- **The linkage *rate* is robust.** Across every defensible cohort definition it lands in 45.4–45.8%.
  Your headline gradient (low bins link at ~8%, high bins at ~76%) is real and survives audit.

### 2.2 What is genuinely broken

Five root causes (§3), producing errors that are real and, in the CHED deliverable, published.
The most vivid: **a chart in the shipped CHED analysis has a legend entry that is mathematically
incapable of ever rendering**, and a narrative paragraph cites that chart as proof of robustness.

### 2.3 The thing that changes what is possible

`UNIVERSITY` is the applicant's **undergraduate** institution, not the medical school they attended.
This is not a bug to fix — it is a ceiling on what the dataset can answer. The CMO's central
mechanism (a PHEI's cut-off privilege conditioned on that PHEI's own PLE performance) **cannot be
evaluated with this data at all.** Better to know now than after a stakeholder asks. §6 maps the
boundary precisely, and §10 shows what you can do instead — including one genuinely strong design
you are currently not using.

---

## 2.4 ADDENDUM (found during remediation, 2026-07-31) — RC-0, which outranks all five

**The PLE matcher refuses to match examinees below the 40th percentile.**

`2_PLE_Matching_Pipeline.ipynb` cell 6, `disambiguate()`, **Step 4**:

```python
PERCENTILE_FLOOR = 40                       # cell 1
pct_pass = [r for r in latest_pass
            if pd.notna(r.get("NMS_PER_num")) and r["NMS_PER_num"] >= PERCENTILE_FLOOR]
if not pct_pass:
    return {"status": "NO_VALID_MATCH", ...}
```

A **hard filter, not a tie-break**: among name-collision groups it discards every candidate below the
40th percentile, and rejects the match outright when all candidates fall below it.

**Why this outranks RC-1 through RC-5.** The question this project exists to answer is whether
examinees below the 40th percentile pass the PLE. The pipeline systematically refuses to match them.
So the collapse in linkage below B5 is **partly manufactured by the matcher**, not solely the
admission-selection effect described in §6. The constant is `40` — precisely the CMO threshold under
review. Everything downstream inherits it: the bin gradient, the cut-off brief and its PDF, the
forensic audit's entire premise, and every bin-level table in both dashboards.

**Scope limiter, stated honestly:** `disambiguate()` runs only when a name matches >1 NMAT record.
Unique-name matches bypass it, which is why B1–B4 passers exist at all. The bias is confined to
name-collision groups — but it is directional and lands exactly on the population under study, so it
must be measured rather than waved away.

**How it was missed:** the original audit examined the *step-5 tie-break* and correctly judged its
circularity negligible (~0.006%). That verdict was right about step 5 and irrelevant to step 4. It
surfaced only because a remediation agent's passer counts would not reconcile and the predicate was
read directly instead of its explanation being accepted.

**Fix:** delete Step 4. Percentile says nothing about *which person* a PLE record belongs to. Keep
year-gap, DOB/sex and latest-year; if more than one candidate survives, reject as ambiguous rather
than selecting on score. Expect movement both ways — and report the newly-matched below-40 group
with its bin distribution, because that is the group the CHED question is about.

---

## 3. The five root causes

Fix these five and roughly 40 downstream symptoms resolve.

### RC-1 — `IS_PLE_ANALYSIS_SAFE` is a duplicate of `IS_PLE_PASSER` [CRITICAL]

```python
(df.IS_PLE_ANALYSIS_SAFE == df.IS_PLE_PASSER).all()    # True
(df.IS_PLE_ANALYSIS_SAFE == (df.Year <= 2014)).all()   # False
```

Documented everywhere as "observable cohort: Year ≤ 2014". It is not. It is True for 4,288 rows in
2015, 3,673 in 2016, 1,136 in 2017, 19 in 2018.

**Worst consequence — the flagship finding of this audit.** The CHED dashboard builds
`_df_clean_ple` by filtering on `IS_PLE_ANALYSIS_SAFE == True`, then splits that subset by
`IS_PLE_PASSER` to show a confirmed/no-match breakdown:

```
clean = df[df.IS_PLE_ANALYSIS_SAFE == True]   # 49,986 rows
(clean.IS_PLE_PASSER == False).sum()          # 0
per-year no-match counts, 2006-2014           # 0,0,0,0,0,0,0,0,0
```

So:
- **Tab 2 "B5+ PLE-Passer Composition by Year"** — a stacked bar chart whose legend advertises a red
  *"No confirmed PLE match"* category that can never render a single pixel, in any year.
- **Tab 3 "Clean PLE Subset Stress Test"** — a line pinned at a flat 100% for all nine years.
- **Tab 5 Finding 6** — narrates that flat line as *"confirming robustness"* of the PLE matching.
  A tautology cannot be a robustness check; it passes identically whether the matching is flawless
  or entirely broken.

This is duplicated verbatim in `export_markdown.py`, so it propagates into the exported markdown and
the PDF brief.

**Also:** the main dashboard's own "Read this first" panel
(`main_dashboard/dashboard.py:722`) tells users *"Confirmed PLE outcomes refer to
IS_PLE_ANALYSIS_SAFE == True"*, and line 714 claims *"PLE-linked pages use the observable cohort
only."* Both statements mis-instruct the reader.

**Fix:** create a genuine `IS_OBSERVABLE_COHORT = (Year <= 2014)`, repoint every consumer, and retire
`IS_PLE_ANALYSIS_SAFE`. Do not merely rename it — the two concepts must be separate columns.

---

### RC-2 — `IS_BEST_NMAT_RECORD` is broken, and fails non-randomly toward passers [CRITICAL]

```
PERSON_KEYs with exactly one True : 133,312
PERSON_KEYs with ZERO True        :   1,311    <- dropped from every person-level count
PERSON_KEYs with MORE than one    :     246    <- double-counted
sum(IS_BEST_NMAT_RECORD) = 133,804   vs   nunique(PERSON_KEY) = 134,869
```

The 1,311 zero-flagged people own 1,497 rows, and **1,497 of 1,497 (100%) are PLE passers**,
concentrated in 2009 (691) and 2010 (478). This is not noise; it is directional.

**Why it happens.** The real selection rule (documented only inside the exported markdown, line 557,
and contradicting `CLAUDE.md`) is: *for PLE passers, take the attempt that matched the PLE record;
for everyone else, take the highest-percentile attempt.* Where the matched attempt could not be
identified, no record got flagged at all. Measured on repeat takers:

| Group | best == highest-percentile attempt |
|---|---|
| Not PLE-linked | 99.3% |
| PLE-linked | 90.7% |

Two different selection rules for the two groups being compared. The bias direction is
**conservative** — it slightly shrinks the observed score-outcome gradient rather than manufacturing
it — but an inconsistent rule across compared groups is indefensible on principle.

**Published consequences:** "Unique examinees (best record) 133,558" should be **134,869**.
"Observable cohort 64,501" (a count of *rows* presented as a count of *people*) should be **69,503**.

**Fix:** one uniform rule for all persons, applied by a single tested function; assert
`sum(flag) == nunique(PERSON_KEY)` in CI.

---

### RC-3 — `PERSON_KEY` is a weak identity key that merges distinct people [CRITICAL]

`PERSON_KEY` = `"SURNAME, GIVEN NAMES" + "||" + birthdate`.

```
rows whose birthdate component is EMPTY : 25,204 of 178,927 (14.09%)
distinct non-empty birthdate values     : 10,725     <- coarse; not a full date
distinct names 123,736  vs  distinct PERSON_KEY 134,869   (DOB adds only 11,133)
```

For 14% of rows the key degenerates to name alone. Direct evidence of merged people:

```
PERSON_KEYs with contradictory SEX : 6,148 (4.56%), spanning 16,020 rows
   of which also span >1 UNIVERSITY: 5,051
names carrying both sexes          : 10,172
```

One person does not have two sexes and two undergraduate universities.

**Estimating the true rate.** 4.56% is only what is *detectable* — a collision is visible only when
the merged people differ in sex. With the observed split (F 56.6% / M 43.4%), two random people
differ in sex with probability 0.491, implying a true rate of **~9.3% of keys**. That remains a
**lower bound**: Filipino given names are strongly gendered, so name-colliding people are *more*
likely than chance to share a sex, which suppresses detection further.

**Impact on the repeat-taker headline:** 33,714 keys have >1 row, reported as "25% repeat takers".
18.2% of those show a sex contradiction; scaling implies **~37% may be name collisions rather than
genuine repeat attempts.** The "25% of examinees are repeat takers" claim is not currently defensible.

This also compounds RC-2 (a collision deletes a person from person-level counts) and can attach one
person's PLE record to another's NMAT score.

**Fix:** this is the one defect not fixable in a dashboard. Either strengthen the key from upstream
identifiers, or publish person-level figures with a disclosed uncertainty band. Recommendation in §8.

---

### RC-4 — `UNIVERSITY` is the undergraduate school, not the medical school [CRITICAL — scope ceiling]

**Proof.** UP Diliman has no College of Medicine (UP's MD programme is at UP Manila). Yet:

```
UNIVERSITY == 'UNIVERSITY OF THE PHILIPPINES - DILIMAN'  : 4,421 rows
   of which IS_PLE_PASSER == True                        : 1,914
```

1,914 physicians cannot have trained at a medical school that does not exist. Corroborating: their
`CourseGroup` values are bachelor's fields — Education (316), Engineering & Technology (37), Social
& Behavioral Sciences (819). NMAT is sat *after* the bachelor's degree. Ateneo de Manila (939) and
DLSU Manila (2,979), neither of which ran an MD programme in this period, appear for the same reason.

**Therefore:** any institution-level PLE rate computed from `UNIVERSITY` attributes each doctor's
licensure outcome to the university where they did their **undergraduate degree**. `UNI_TYPE`
(Public/Private) describes the undergraduate institution and is **not** a valid SUC-vs-PHEI proxy.

The main dashboard's Tab 13 does exactly this — per-HEI benchmarking, a 10-slot cap analysis, and an
institution viewer, some on samples as small as n=5 (163 of 539 "HEIs" have 5–10 examinees).

**Note in fairness to the CHED dashboard:** it never groups by `UNIVERSITY` at all (grep confirms
zero groupbys). Its exposure is limited to `UNI_TYPE` framing — real, but far less severe than the
main dashboard's Tab 13.

**Fix:** not fixable. Remove institution-level PLE claims and state the limitation explicitly. §6.

---

### RC-5 — Four parallel implementations of the same numbers, with confirmed drift [HIGH]

The same quantities are computed independently in four places: `dashboard.py`, `export_markdown.py`,
`ched_compute/0X.py`, and `verified_true/verifier_0X.py`. They disagree.

**Confirmed drift, independently reproduced:**

```
best-record, no PercentileBin null-filter  ->  Public 56, Private 48   (live dashboard)
best-record, WITH PercentileBin null-filter->  Public 57, Private 49   (exported document)
null PercentileBin among best-record rows  ->  3,069
```

`CHED_NMAT_Dashboard_Complete.md:491` publishes **57/49**; the live dashboard shows **56/48**. This
is precisely the "exported artefact ≠ dashboard" failure — sitting in text that would be quoted
directly into a policy brief.

**A second bug in the same sentence:** the metric is labelled *"median bin rank"*, but 57 and 49 are
on the 0–99 percentile scale. The actual median *bin rank* is 6 and 5 (bins run B1–B10). The
published sentence attaches a percentile value to a bin-rank label.

**The QA suite cannot catch any of this.** `verified_true/` verifiers never import
`ched_compute/0X.py`, never diff against `page_results/*.md`, and instead reimplement the logic a
fourth time and compare against a **hand-typed `expected = {...}` dict**. A verifier whose
expectations are transcribed from the output it checks cannot fail.
`CONSOLIDATED_VERIFICATION_REPORT.md` certifies the string-boolean dtype bug as "FIXED in commit
619a150" — but that commit touched only `dashboard.py`. The bug is still live in
`ched_compute/06_data_limitations.py`, whose committed output reads *"Rows with complete TRUE
scores: 0 (99.97%)"* — a self-contradiction a genuine verifier would have caught instantly.

A directory named `verified_true/` is exactly what would persuade a reviewer the numbers had been
checked. That assurance is unearned, which is worse than none.

**Fix:** one shared `ched_common.py` with pure `compute_*()` functions that all three consumers call.
Drift becomes structurally impossible. Delete the verifiers or rewrite them as real property tests.

---

## 4. Complete findings register

Severity: **C**ritical (wrong numbers reach a stakeholder) / **H**igh (misleading or unsupported) /
**M**edium (fragile) / **L**ow (cosmetic/docs). RC = root cause from §3.

### Critical

| # | Finding | Where | RC |
|---|---|---|---|
| C-01 | "No confirmed PLE match" chart series is identically zero for all 9 years; legend advertises a category that can never render | CHED tab 2, tab 3; `export_markdown.py` | RC-1 |
| C-02 | Tab 5 Finding 6 cites the tautological flat-100% line as proof of matching robustness | CHED tab 5 | RC-1 |
| C-03 | Dashboard onboarding text defines "Confirmed PLE outcomes" as `IS_PLE_ANALYSIS_SAFE == True` | `main_dashboard/dashboard.py:722` | RC-1 |
| C-04 | Published "unique examinees 133,558" — true value 134,869 | `CHED_..._Complete.md:534` | RC-2 |
| C-05 | Published "observable cohort 64,501" is a row count presented as a people count — true 69,503 | `CHED_..._Complete.md:535,571` | RC-2 |
| C-06 | 1,311 people (100% PLE passers) silently dropped from every person-level count | parquet flag | RC-2 |
| C-07 | 246 people double-counted as best-record | parquet flag | RC-2 |
| C-08 | `PERSON_KEY` merges distinct people; ≥6,148 keys with contradictory SEX, true rate ~9.3%+ | parquet | RC-3 |
| C-09 | "25% repeat takers" — up to ~37% may be name collisions | repeat-taker tab | RC-3 |
| C-10 | Tab 13 per-HEI PLE benchmarking attributes outcomes to undergraduate schools | main tab 13 §B,D,E | RC-4 |
| C-11 | Tab 13 HEI status computed on samples as small as n=5 (163/539 HEIs have 5–10) | main tab 13 | RC-4 |
| C-12 | Tab 13 rolling 5-year benchmark is positional (`.rolling(5)`), silently averaging non-contiguous years when the Year filter has gaps; frozen at reference year 2014 vs the CMO's 2026 effectivity | main tab 13 | — |
| C-13 | Exported doc publishes 57/49 where the live dashboard shows 56/48 | `export_markdown.py:647` vs `dashboard.py:1004` | RC-5 |
| C-14 | India published as 85.1% of verified foreigners; true 81.5% (share taken against top-10 subtotal 31,116 instead of all 32,501) | `export_markdown.py:631`, PDF brief | — |
| C-15 | "42.2% of stored totals incorrect" — true 56.45% of the 99,316 rows with a stored total | 3× in CHED `dashboard.py`, docs | — |
| C-16 | Page 2 shows 72.87% "no confirmed PLE match" while 51.79% of rows are structurally too recent to have a board outcome | main tab 2 | RC-1 |
| C-17 | Nested CHED deploy repo is 11+ commits behind parent with 23 files / 6,738 uncommitted deleted lines | `CHED_relevant_dashboard/.git` | — |
| C-18 | Forensic "4 genuine mismatches" required an undocumented manual override of 13 of the script's 17 flagged records | `name_cross_check_evidence.md` | — |
| C-19 | Forensic name source is a stale intermediate (`PLE_MATCH_MASTER.csv`, ~7 weeks older) covering only ~62% of EXACT matches | `forensic_audit/` | — |

### High

| # | Finding | Where |
|---|---|---|
| H-01 | `verified_true/` verifiers compare against hand-typed expectations; cannot fail |
| H-02 | `CONSOLIDATED_VERIFICATION_REPORT.md` certifies a fix that was never applied to the audited files |
| H-03 | String-as-boolean bug still live: `"True" == True` → 0 rows instead of 178,882 | `ched_compute/06_data_limitations.py:39,48,49` |
| H-04 | Committed output literally reads "Rows with complete TRUE scores: 0 (99.97%)" | `page_results/06_data_limitations.md` |
| H-05 | Forensic suite never computes the full 2×2 contingency table, so no cut-off validity claim is supported |
| H-06 | 2,618 observable examinees (4.06%) who *did* match a PLE record are shown as "No confirmed PLE match" |
| H-07 | Four PLE columns disagree; dashboards silently pick one (resolved in §4.1 — the sets are *not* nested) |
| H-16 | **`rapidfuzz` fuzzy matching survives in Pipeline 1's university-name matching** (cells 3 and 17: `fuzz.`, `process.extract`), affecting 235 of 3,251 colleges with one demonstrated false positive — directly contradicting the repo-wide "all fuzzy matching removed for auditability" guarantee |
| H-17 | `MANUAL_APPNO_MATCH` (2,776 rows / 2,331 people) has **zero documented provenance** — "manual" in a pipeline claiming full determinism, with no audit trail |
| H-18 | `data_aggregator` page 4 citizenship section computes over all 178,927 rows instead of the dashboard's filtered 34,727-row cohort — reports **32,501 "Verified Foreigners" vs the dashboard's 4,746**. A different population, not a rounding gap |
| H-19 | Aggregator "Table 38/39" (subtest radar) is mean-centred while the dashboard's same-labelled table is raw — Public/Verbal reads **495.13** in the dashboard vs **9.02** in the aggregator |
| H-20 | `CLAUDE.md` claims `data_aggregator` uses DuckDB for performance. It contains **zero DuckDB** — pure pandas throughout (`grep -ril duckdb data_aggregator/` returns nothing) |
| H-08 | `name_based_assessment` shipped and displayed but never used in tier logic; disagrees with the final label in 23 of 871 rows |
| H-09 | Retroactive application of a 2026-effective foreign-slot cap to 2006–2018 data |
| H-10 | Mismatched cohorts in one Tab 13 table row (91,409 "admitted" vs 46,609 "PLE cohort") |
| H-11 | `ched_compute` counts "Verified"+"Likely" foreigners where dashboard/export count "Verified" only |
| H-12 | `viz/` paths hardcoded wrong in `export_markdown.py`; only the committed output was hand-patched, so re-running regresses the fix |
| H-13 | `ec8ec8c`/`e69dd6c` labelled "Pylance lint fixes" actually change semantics (`na_value=0` turns missing into a real 0.0%; `text_auto=True` drops pinned `.1f` precision) |
| H-14 | Documented `cd data_aggregator && python run_all.py` is broken — hardcoded CWD-relative paths, every page silently skips |
| H-15 | Root `requirements.txt` missing `duckdb`; Pipeline 1 still needs `rapidfuzz` though it was removed |

### Medium / Low (abridged — full list in `.claude/audit/`)

- M: Shipped 54-col parquet has **no generating script** — the slimming step is manual and
  unreproducible (`4_Citizenship_Integration.py` only emits the 118-col `.bak`).
- M: `CITIZENSHIP_FINAL` contains a literal `"Foreign"` placeholder (156 rows) that appears in the
  published top-10 nationality chart as if it were a country.
- M: Best-record selection rule differs by PLE status and matches neither documented description.
- M: `NMA_College` is a redundant duplicate of `UNIVERSITY`; the two give different institution
  counts (3,251 vs 2,907 distinct), and page 2 reports both on the same page.
- M: Unbounded repeat-taker tables (8.7 MB `08_repeat_takers.md`).
- M: 4 of 6 forensic scripts write outputs to the repo root, not `forensic_audit/`.
- M: PDF §3.1 "130,818 best-record records with a valid percentile bin" — current parquet gives
  **130,735** (83-record gap ⇒ stale snapshot).
- L: `AllRawComponentsPresent` and `CalcVsDerivedMismatch` are constant (zero information) yet one is
  displayed as a live integrity KPI.
- L: Phantom columns in docs: `PERSON_NAME`, `PLE_MATCH_STATUS`, `IS_BOARD_OBSERVABLE_COHORT`.
- L: "12 tabs" documented; 13 exist. `CITIZENSHIP_FINAL` cardinality documented as 96/108/91 in three
  places; actual is 91. Both `tree_dir.txt` omit `streamlit_dashboard/` and `forensic_audit/`.
- L: Diverging colormap used on a magnitude metric; duplicate placeholder table column; dead code.
- L: **Six tracked PDFs are deleted in the working tree but still present in HEAD** —
  `CHED_relevant_dashboard/pdf_exports/tab_1..tab_6*.pdf`, committed in `113d00d`, directory now
  absent from disk. Predates this audit (`.git/index` last written 2026-07-28 20:50, and no auditor
  wrote to any project file). Either restore them or commit the deletion; leaving HEAD disagreeing
  with the working tree is how a stale artefact gets redeployed. Related to C-17.
- L: `.gitignore` gaps (`*.msi`, `ngrok_log.txt`, `*_out.txt`). `ngrok_log.txt` was read in full —
  **no secret present**; every session shows an auth failure before a tunnel URL was issued. The gap
  is a latent risk, not a current leak.

### 4.1 The four PLE counts, resolved — and a correction to my own earlier framing

I initially characterised the four counts as nested, with an unexplained "4,542 gap". **That was
wrong**, and auditor 12 corrected it. The sets are not nested. Verified directly:

```
PLE_YEAR_PASSED present AND IS_PLE_PASSER : 47,210
PLE_YEAR_PASSED present AND NOT passer    :  7,318   <- rejected AMBIGUOUS/NO_VALID_MATCH rows
                                                        that still inherited method + year metadata
IS_PLE_PASSER but NO year                 :  2,776   <- exactly the MANUAL_APPNO_MATCH count
```

**Mechanism** (`2_PLE_Matching_Pipeline.ipynb`, cell 11): `get_ple_info()` populates
`PLE_MATCH_METHOD` and `PLE_YEAR_PASSED` for *any* candidate match regardless of adjudication
outcome, but gates `IS_PLE_PASSER` on accepted status only. The 2,776 manual matches structurally
lack a year because their source (`PLE_UNMATCHED.csv`) has no year column.

**Authoritative count of confirmed PLE passers: `IS_PLE_PASSER` = 49,986.** The other three columns
are diagnostic metadata and must never be used as a passer denominator.

**Exact origin of RC-1**, same cell:
```python
analysis_safe = {"FINAL_MATCH", "MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"}   # == accepted_statuses
```
There is no `Year <= 2014` term anywhere. `NMAT_Ultima.parquet` already carries the bug, so it was
**never correct and never later clobbered** — it has been wrong since Pipeline 2 first ran.

**Also corrected: the "~32% match rate" is misleading.** That figure mixes in 2015–2018 cohorts too
recent to appear in PLE data. Restricted to the observable window the row-level match rate is
**46.4%** (vs 27.9% across all years).

**Disambiguator circularity — CONFIRMED as a mechanism.** Step 5 of the 5-step disambiguator breaks
ties among name-collision candidates by **highest `NMS_PER_num`**, accepting when the leader beats
the runner-up by ≥5 points. Selecting the match partly on the very variable whose relationship to PLE
outcome is later analysed is circular. Magnitude is structurally small (person-level name-collision
rate ≈0.006% after DOB filtering), so it does not threaten the headline gradient — but it must be
disclosed, and it should be re-specified to break ties on something outcome-independent.

### 4.2 Arbitrations (where I overruled an auditor)

1. **Observable-cohort rate.** Auditor 04 reported the 45.38% should be 47.28% (+1.90 pp). I could
   not reproduce it; their n=64,531 matches no definition in the ladder below. **The rate is robust
   at 45.4–45.8% under every defensible denominator.** What is genuinely wrong is the *population
   count*, not the rate.

   | Definition | Count | Rate |
   |---|---|---|
   | all rows (sittings) | 88,144 | — |
   | unique PERSON_KEY | **69,503** | **45.76%** |
   | unique with non-null percentile | 68,746 | 45.40% |
   | best-record rows *(published as "people")* | 64,501 | 45.38% |
   | best-record unique PERSON_KEY | 64,312 | 45.49% |

   **Rates survive; counts do not.** Sentences of the form "N examinees…" are wrong; sentences of
   the form "X% of the cohort…" are approximately right. Do not over-correct conclusions that hold.

2. **Repeat-taker percentage.** Auditor 11 flagged "33,713 (25.0%)" as wrong, giving 25.24%. Direct
   computation: 33,714 / 134,869 = **25.0%**. The published figure is correct at the stated
   precision. (The *composition* of that 25% is the real problem — RC-3 — not the arithmetic.)

3. **Auditor 02's "audit trail destruction"** framing of the column slimming is overstated. All 64
   dropped columns are unused or safely recomputed via guarded fallbacks in every consumer. The
   slimming is safe; the real issue is only that it has no reproducible script (M-1).

---

## 5. Dashboard completeness inventory

You asked whether every visualisation, metric, and insight is complete. Both dashboards were walked
element by element (~125 main + ~60 CHED).

### 5.1 Main dashboard — 13 tabs (`streamlit_dashboard/main_dashboard/dashboard.py`, 3,207 lines)

| # | Tab | Sub-tabs | Status |
|---|---|---|---|
| 1 | 🏠 Executive Summary | Overview / Composition / Quick Tables | Two "examinee count" KPIs (133,804 and 133,558) disagree **with each other**; both wrong (C-04/06) |
| 2 | 🧪 Data Integrity | — | 72.87% "no match" mixes in structurally-unobservable years (C-16); two disagreeing institution counts on one page; constant column shown as live KPI |
| 3 | 📈 Trends & Stability | — | Volume trend driven by broken best-record flag; shows 60.1–92.6% of true sittings per year, non-uniformly ⇒ distorts trend *shape* |
| 4 | 📊 Score Bins & Background | By year / Uni type / Course group | Bin orientation correct (B1 lowest). No inversion found |
| 5 | 🏫 University Type Analysis | foreign / public / private splits | RC-4 throughout: framed as institutional performance, actually undergraduate origin |
| 6 | 🔄 Flow & Pathways | Uni→Bin / Course→Bin / Bin→PLE / Top pathways | Bin→PLE inherits RC-1 |
| 7 | 🎯 PLE Alignment | Status / Bin / Background / Policy tables | Highest-risk tab. "Pass rate" language on a *match* rate (lines 2884–3142); RC-1 + RC-2 |
| 8 | 🔁 Repeat Takers | — | RC-3: up to ~37% of "repeats" may be collisions. Unbounded table |
| 9 | 🧠 Subtests & Profiles | Uni type / Course / Radar | Sound; inherits best-record deficit only |
| 10 | ⏰ Year Gap & Gender | Year gap / Gender | Sound |
| 11 | 📐 Statistical Tests | 4 sub-tabs | **Sound.** Effect sizes present; Dunn correctly Bonferroni-corrected |
| 12 | 📋 Policy Tables & Export | — | Inherits upstream defects into downloads |
| 13 | ⚖️ CHED Compliance | per-HEI viewer | **Should be removed or rebuilt.** C-10/11/12; you were right to distrust it |

### 5.2 CHED dashboard — 6 tabs (`CHED_relevant_dashboard/dashboard.py`, 1,262 lines)

| # | Tab | Status |
|---|---|---|
| 1 | National Profile | Sound. Volume, uni-type and course composition, repeat-taker context, bin reference |
| 2 | B4+ vs B5+ Thresholds | **C-01** — tautological stacked bars. Public-school framing inherits RC-4 |
| 3 | PLE-Passer Linkage | **C-01** — flat-100% stress test. Linkage-by-bin gradient itself is sound and well-labelled |
| 4 | Institution and Foreign Context | **C-14** (India 85.1% vs 81.5%); `"Foreign"` placeholder shown as a country; RC-4 in UNI_TYPE framing |
| 5 | Key Evidence for Policy Review | **C-02** (Finding 6 circular); **C-13** (57/49 drift); "median bin rank" mislabel |
| 6 | Data, Methods, and Limitations | **Best content in the repository.** Honest, covers GIDA/IP, enrolment, cap, composite ranking. Needs C-15 corrected and RC-4 added |

**Coverage verdict:** the export chain omits *nothing* — all 14 charts are present and all `../viz/`
paths resolve. The problem is never omission; it is silent recomputation drift (RC-5).

---

## 6. Scope boundary — what this dataset can and cannot answer

Traceability against `docs/CHED_CMO.md`:

| CMO provision | Data support | Verdict |
|---|---|---|
| §IV.A.1 — SUC 40th-percentile floor for Filipinos | Percentile ✓, citizenship ✓, **SUC identity ✗** | **Partial** — describable for *applicants*, not by institution |
| §IV.A.1 — 30–39th band for GIDA/IP applicants | **No GIDA, IP, residence or SES field exists** | **Not answerable** |
| §IV.A.2.a — cap foreign enrolment at 10/class | Examinee citizenship ✓, **enrolment ✗** | **Not answerable** — we see test-takers, not enrollees |
| §IV.A.2.b — composite 60/40 or 70/30 ranking | **No GWA, interview, or other criteria** | **Not answerable** |
| §IV.B.1 — PHEI cut-off floor ≥30th percentile | Percentile distribution ✓ | **Answerable at applicant level** |
| §IV.B.1.b/c — privilege conditioned on the PHEI's own 5-yr PLE rate | **No med-school identifier; no institutional PLE denominator** | **Not answerable — the central mechanism of the CMO** |
| §IV.B.2 — revocation after 3 sub-average years | Same as above, plus no national benchmark | **Not answerable** |
| §VI — monitoring | — | Out of scope |

**The one-sentence version for a stakeholder:** *This dataset describes NMAT examinees and their
subsequent appearance in PLE passer records. It contains no medical-school identifier, no enrolment
data, no PLE failures, and no equity indicators — so it can characterise the applicant pool against
candidate thresholds, but it cannot measure any institution's performance or evaluate the
institution-conditioned provisions of the CMO.*

### The selection effect you must state explicitly

Linkage rises smoothly across B1–B4 (8.1 → 25.9%) and B5–B10 (46.8 → 76.6%), but **jumps 21 points
between B4 and B5** — exactly at the 40th percentile, the cut-off already mandated by CMO 18 (s.2016).

The mechanism is **admission, not aptitude**. People below the 40th percentile were largely barred
from enrolling at all, so they could never appear as PLE passers. Their low linkage measures
non-admission, not failure.

Therefore any "students below the cut-off still pass the PLE" argument is computed on a heavily
selected residual — the atypical few admitted below 40 despite the rule. **No conclusion about
lowering the cut-off to the 30th percentile follows from them.** This is the single biggest threat to
the published brief's defensibility, and the brief does not currently name it.

---

## 7. Corrected numbers reference card

| Quantity | Published / displayed | **Correct** |
|---|---|---|
| Exam sittings | 178,927 | 178,927 ✓ |
| Unique examinees | 133,558 / 133,804 | **134,869** |
| Observable cohort (Year ≤ 2014), people | 64,501 | **69,503** |
| Observable linkage rate | 45.38% | 45.4–45.8% ✓ (robust) |
| Stored-total mismatch | "42.2%" | **56.45%** of the 99,316 rows with a stored total (= 31.33% of all rows) |
| India share of verified foreigners | 85.1% | **81.5%** (26,490 / 32,501) |
| Public/Private median percentile | 57/49 (export) vs 56/48 (dashboard) | **56/48** unfiltered; 57/49 if null bins dropped — pick one and label it *percentile*, not "bin rank" |
| Best-record rows w/ valid bin | 130,818 | **130,735** |
| Repeat takers | 33,713 (25.0%) | 33,714 (25.0%) ✓ *but see RC-3 on composition* |
| Verified foreigners | 32,501 (18.2%) | ✓ |
| Bin orientation | — | **B1 = lowest (0–9); B10 = highest (90–99)** |
| Confirmed PLE passers | varies by column | **49,986** (`IS_PLE_PASSER`) — the other three columns are diagnostic metadata |
| Rows w/ year but not passer | — | 7,318 (rejected matches that kept metadata) |
| Rows passer but no year | — | 2,776 (all `MANUAL_APPNO_MATCH`; source file has no year column) |
| Row-level match rate | "~32%" | **46.4%** within the observable window (27.9% across all years, which mixes in cohorts too recent to have sat the PLE) |

---

## 8. Remediation plan

Four tracks. **A and D can start immediately and run in parallel** (disjoint files). B depends on A.
C depends on B. Each step lists its commit.

### Track A — Data-layer truth (blocking; do first)

**A1. Add a real observable-cohort flag.** *(fixes RC-1)*
In the slimming step, add `IS_OBSERVABLE_COHORT = (Year <= 2014)`. Keep `IS_PLE_PASSER`. Mark
`IS_PLE_ANALYSIS_SAFE` deprecated — do not delete yet, so nothing breaks silently.
```
fix(data): add IS_OBSERVABLE_COHORT, deprecate IS_PLE_ANALYSIS_SAFE

IS_PLE_ANALYSIS_SAFE was a byte-identical duplicate of IS_PLE_PASSER, not
the documented Year<=2014 cohort. Any rate using it as a denominator filter
returned 100% by construction.
```

**A2. Rebuild the best-record flag.** *(fixes RC-2)*
One uniform rule for every person — recommend highest percentile → latest year → lowest APPNO.
Apply to passers and non-passers alike.
```
fix(data): rebuild IS_BEST_NMAT_RECORD with one uniform selection rule

1,311 PERSON_KEYs had zero flagged rows (all 1,497 of them PLE passers) and
246 had more than one. Passers and non-passers were selected by different
rules. Unique-examinee count corrects 133,558 -> 134,869.
```

**A3. Quantify and expose identity uncertainty.** *(mitigates RC-3)*
Add `PERSON_KEY_AMBIGUOUS` (True where a key shows contradictory SEX or >1 undergraduate
university). Do not silently "fix" the key — surface it.
```
feat(data): flag ambiguous PERSON_KEYs to expose name-collision risk

>=6,148 keys (4.56%) merge distinct people; scaling for undetectable
same-sex collisions implies ~9.3%+. Affects repeat-taker counts most.
```

**A4. Make the 54-column slim reproducible.** *(fixes M-1)*
Write `5_Slim_Exodus.py` reproducing the 118→54 step that is currently manual.
```
feat(pipeline): add 5_Slim_Exodus.py so the shipped parquet is reproducible

The 54-column parquet consumed by both dashboards had no generating script.
```

**A5. Single source of data.** Replace the three parquet copies with one path (or a build step that
copies and records a checksum).
```
refactor(data): single parquet source of truth with checksum manifest
```

### Track B — Shared compute layer (depends on A; fixes RC-5)

**B1.** Create `ched_common.py`: `load_and_validate()` plus pure `compute_*()` per tab. Move every
aggregation out of `dashboard.py`, `export_markdown.py`, and `ched_compute/0X.py` into it.
```
refactor(ched): extract shared compute module to eliminate drift

dashboard.py, export_markdown.py and ched_compute/ each reimplemented the
same aggregations and disagreed (Public/Private median 56/48 vs 57/49).
```

**B2.** Delete `verified_true/`; replace with real tests (Track D).
```
refactor(ched): remove verified_true/, superseded by real tests

Verifiers compared against hand-typed expectations and could not fail;
CONSOLIDATED_VERIFICATION_REPORT certified a fix never applied to ched_compute.
```

**B3.** Fix the string-as-boolean bug in `ched_compute/06_data_limitations.py`.
```
fix(ched): coerce string-typed boolean columns in ched_compute

HasTRUErawScores is str; "True" == True is False, so the committed output
read "Rows with complete TRUE scores: 0 (99.97%)".
```

### Track C — Correct the deliverables (depends on B)

**C1.** Remove the tautological charts; replace with an honest observable-cohort split.
```
fix(ched): remove tautological PLE-status charts

Filtering on IS_PLE_ANALYSIS_SAFE then splitting by IS_PLE_PASSER produced a
"No confirmed PLE match" series identically zero in all 9 years, and Finding 6
cited that flat 100% line as evidence of matching robustness.
```

**C2.** Fix the India denominator and drop `"Foreign"` from nationality charts.
```
fix(ched): compute nationality shares against all verified foreigners

Shares used the top-10 subtotal (31,116) not the full 32,501, publishing
India as 85.1% instead of 81.5%.
```

**C3.** Correct the 42.2% claim everywhere; state its denominator.
```
fix: correct stored-total mismatch rate to 56.45% of 99,316 rows with a stored total
```

**C4.** Remove or rebuild main-dashboard Tab 13; remove per-HEI PLE benchmarking.
```
fix(dashboard): remove per-HEI PLE benchmarking from CHED Compliance tab

UNIVERSITY is the applicant's undergraduate institution, not their medical
school (UP Diliman: no MD programme, 4,421 rows, 1,914 "PLE passers"). No
medical-school identifier exists, so institutional PLE performance — the
CMO's central mechanism — cannot be computed from this dataset.
```

**C5.** Add the selection-effect caveat and the RC-4 limitation to the limitations tab; fix the
"median bin rank" label; correct the onboarding panel at `dashboard.py:714,722`.
```
docs(ched): state the admission-selection confound and institution-identifier limit
```

**C6.** Regenerate the export and the PDF brief from the corrected pipeline.
```
chore(ched): regenerate complete markdown and brief from corrected compute layer
```

### Track D — Infrastructure (parallel with A from day one)

**D1.** Add tests. There are currently none. Minimum viable set:
```python
def test_best_record_is_one_per_person():
    assert df.groupby("PERSON_KEY").IS_BEST_NMAT_RECORD.sum().eq(1).all()

def test_observable_cohort_is_year_based():
    assert (df.IS_OBSERVABLE_COHORT == (df.Year <= 2014)).all()

def test_no_tautological_filters():
    # no column may be a perfect duplicate of another
    assert not (df.IS_OBSERVABLE_COHORT == df.IS_PLE_PASSER).all()

def test_raw_total_equals_component_sum():
    assert (df[RAW_COLS].sum(axis=1) - df.TotalRawScoreTRUE).abs().max() < 1e-6

def test_export_matches_dashboard():
    # every compute_*() called once, results compared to the exported markdown
```
```
test: add data-invariant suite covering the five root causes
```

**D2.** Resolve the nested deploy repos (C-17) — convert to submodules or delete and deploy from the
parent. **Verify what the live Streamlit Cloud instance is actually serving before anything else.**
```
fix(deploy): reconcile nested CHED repo, 11 commits behind parent
```

**D3.** Repo hygiene: `.gitignore` gaps, remove `dashboard.py.bak`, track `CLAUDE.md`/`changelog.md`,
regenerate `tree_dir.txt`.
```
chore: repo hygiene — gitignore gaps, remove stale .bak, regenerate tree
```

**D4.** Rewrite documentation from the corrected facts (§7 is the source).
```
docs: rewrite data dictionary and pipeline architecture from verified schema

20 of 44 documented claims were wrong, including three phantom columns
(PERSON_NAME, PLE_MATCH_STATUS, IS_BOARD_OBSERVABLE_COHORT).
```

**D5.** Fix `data_aggregator` (keep it — see §11).
```
fix(aggregator): resolve paths relative to __file__ so documented invocation works

cd data_aggregator && python run_all.py produced 0/13 pages; hardcoded
CWD-relative paths resolved to nonexistent directories and every page
silently skipped.
```
```
fix(aggregator): page 4 citizenship must use the filtered cohort

Computed over all 178,927 rows instead of the dashboard's 34,727, reporting
32,501 verified foreigners against the dashboard's 4,746.
```
```
fix(aggregator): reindex percentile bins by BIN_ORDER and cap repeat-taker dump

Bins rendered B1, B10, B2, B3... from string sorting. Section 3 dumped all
~33,702 person-rows inline (8.7 MB); the next section already caps at 100.
```

**D6.** Disclose or remove the surviving fuzzy matching. *(fixes H-16)*
```
fix(pipeline): document surviving rapidfuzz use in university-name matching

Pipeline 1 cells 3 and 17 still use fuzz./process.extract for 235 of 3,251
college names, contradicting the documented "no fuzzy matching" guarantee.
Either replace with a deterministic alias table or state the exception.
```

**D7.** Disclose the disambiguator tie-break. *(fixes §4.1 circularity)*
```
fix(pipeline): break PLE disambiguation ties on an outcome-independent key

Step 5 broke ties on highest NMS_PER_num — the same variable whose
association with PLE outcome is later analysed.
```

### Suggested order

```
Day 1   A1 A2 A3      ‖  D1 D2 D3      (D2 FIRST — find out what is actually deployed)
Day 2   A4 A5         ‖  D4 D6 D7
Day 3   B1 B2 B3      ‖  D5
Day 4   C1 C2 C3 C4 C5
Day 5   C6            + full regression against §7
```

Track A blocks B blocks C. Track D is independent of all of them and can run start to finish in
parallel — it touches no file that A/B/C touch.

---

## 9. What to do about the forensic audit

Do not patch it. The reproducible core (score-gradient arithmetic, bin orientation) is fine, but two
defects invalidate its headline:

1. The "4 genuine mismatches" required a **manual override of 13 of the 17 records the script
   flagged** — a step that exists in no committed file. Re-running the documented command yields 17,
   not 4. The heuristic auto-flags Filipino compound-surname spacing variants ("De Guzman" /
   "Deguzman") that the evidence document itself calls clean.
2. The name source is a **stale intermediate covering ~62% of EXACT matches**. The specific
   low-score population did reconcile 100% (430/430), so the low-score deep-dive stands — but the
   system-wide "97.2% / 0.2%" claims do not.

**A defensible version** computes the full 2×2 — above/below each candidate threshold × PLE-linked /
not-linked — reports base rates, states that "not linked" ≠ "failed", and runs the name check over
100% of the current parquet with the compound-surname normalisation applied *in code*, not by hand.

---

## 10. Analyses worth adding (all within the existing 54 columns)

1. ~~**Regression discontinuity at the 40th percentile.**~~ **WITHDRAWN — see §2.4 (RC-0).**
   This recommendation rested on a sharp jump between B4 (25.9%) and B5 (46.8%). After removing the
   `PERCENTILE_FLOOR = 40` filter from the matcher, that jump is **9.6 points, not 21**, and no
   longer an outlier among the other bin-to-bin steps (B1→B2 is +11.1, B9→B10 is +9.4). The
   discontinuity was mostly our own code. RDD may still be worth testing formally, but the visual
   evidence that motivated it does not survive the fix — do not lead with it.

1b. **The replacement, and it is stronger: characterise the below-threshold passers directly.**
   On corrected data, **795 examinees in B1 — the lowest decile — are confirmed PLE passers (11.6%
   linkage), and B4 reaches 36.0%.** Under a strictly enforced 40th-percentile rule these people
   should barely exist. Their number implies the existing rule was not uniformly binding. Profile
   this group (year, undergraduate origin, citizenship, subtest pattern, repeat-taker status) and
   report it with the linkage caveat. It speaks directly to what a 30th-percentile floor would
   admit, which is the actual question in CMO §IV.B.1 — and unlike the discontinuity story, it is
   robust.
2. **Full threshold contingency tables** at 30/35/40/45/50 with base rates — replaces the
   one-directional gradient that invites over-reading.
3. **Subtest profile of the B4-only band** — who exactly is in the 30–39 window the CMO exception
   targets. Uses the 8 `NMS_*ss` columns.
4. **Repeat-taker threshold mobility** — how many people cross 30th/40th on a later attempt.
   Directly relevant to whether a floor excludes people permanently or temporarily. *(Gate on RC-3.)*
5. **Foreign vs Filipino percentile distributions** — descriptive, well-supported, relevant to
   §IV.A.2, and honest about being applicants rather than enrollees.
6. **Linkage-rate time trend with a stated observability window** — the 55.6% (2006) → 37.8% (2014)
   decline is real and interesting, but must be shown against the shrinking observation window.

Deliberately excluded as unsupported: any per-institution PLE rate, any enrolment estimate, any
GIDA/IP analysis, any sensitivity/specificity or ROC framing (no observed failures or non-admits).

---

## 11. Component recommendations

- **`data_aggregator/` — keep and fix. I withdraw my earlier instinct to retire it.**
  Auditor 08's evidence changed the answer: a from-scratch rerun reproduces the committed
  `page_results/*.md` **byte-for-byte** (zero diff outside the timestamp), and 11 of 13 pages match
  `dashboard.py`'s formulas exactly. This is a working, current component, not an abandoned one. Its
  defects are small and mostly one-function-sized: fix the page-4 filter chain (H-18), add the
  `BIN_ORDER` reindex so bins stop rendering B1, B10, B2, B3…, cap the repeat-taker dump with
  `.head()` (it already does this correctly in the *next* section), un-centre Table 38/39 (H-19), and
  resolve paths relative to `__file__` (H-14). Fold it into the Track B shared compute layer
  afterwards as an improvement, not as a rescue.
  Note also H-20: it uses **no DuckDB at all**, so the documented performance rationale is fiction —
  correct the docs rather than the code.
- **`reports/`** — stale, as you said. Delete or move to `.artifacts/`.
- **Root `dashboard.py` + `dashboard.py.bak`** — legacy duplicates of the live main dashboard. Delete.
- **`RShiny_Dashboard/`** — abandoned. Delete, and remove the parity guidance from `CLAUDE.md`.
- **`verified_true/`** — delete (B2). It is worse than nothing.
- **`forensic_audit/`** — keep the scripts, withdraw the conclusions pending §9.

---

## 12. The one thing to do first

Before any code: **determine what the live Streamlit Cloud deployment is actually serving.** The
nested CHED repo is 11+ commits behind the parent with thousands of uncommitted deleted lines. If
that remote drives the stakeholder-facing deployment, then the dashboard CHED can see today is not
the one this audit reviewed — and every fix below lands somewhere nobody is looking.

---

*Audit conducted 2026-07-31. 12 parallel specialist auditors; all findings independently re-verified
by the orchestrator against the shipped parquet before inclusion. Supporting reports in
`.claude/audit/`.*
