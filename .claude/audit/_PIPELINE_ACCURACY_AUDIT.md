# Pipeline Accuracy Audit — 1 → 5, from raw CSV to NMAT_Exodus.parquet

**Date:** 2026-08-14. **Question asked:** is the chain from `NMAT_CLEANED_DATA.csv` / `CEM_DATA.csv`
/ `UNIVS.csv` through to `dataset/NMAT_Exodus.parquet` fully accurate?

**Answer: the mechanics are sound; the published headline numbers are not.** No row is lost, no
merge fans out, the score identity holds on every row, the bins are correct. But three separate
issues inflate the project's headline linkage figures, and one of the project's most-repeated
data-quality claims is mischaracterised. The central qualitative finding survives all of it.

Every number below was measured by the orchestrator against the real files. Agent claims that did
not reproduce are marked as such.

---

## 1. The finding that matters most: the PLE source only covers 2011–2022

`dataset/PLE_DATA.csv` contains **zero records before 2011 and none after 2022**:

```
2011 2260 | 2012 2203 | 2013 2254 | 2014 2644 | 2015 3085 | 2016 3382
2017 4153 | 2018 4784 | 2019 5215 | 2020 4402 | 2021 3995 | 2022 5253    total 43,630
```

The median NMAT→PLE gap is **6 years** (mean 6.66, IQR 6–7). So every NMAT cohort is observed
through a *different* window:

- **Early cohorts are left-censored.** A 2006 examinee who passed in 2009 is invisible. Small
  effect — only ~0.3% of observed gaps are ≤4 years.
- **Late cohorts are right-censored.** A 2014 examinee needs to pass by 2022, i.e. within 8 years.
  Roughly 7% of observed gaps exceed that.

This is why linkage appears to fall over time. It largely does not:

| NMAT year | published | equal 8-year window |
|---|---|---|
| 2006 | 54.2% | 45.4% |
| 2010 | 52.6% | 45.0% |
| 2014 | 36.6% | 34.8% |

The published 17.6-point "decline" shrinks to 10.6 once exposure is equalised. **`Year <= 2014` does
not make the cohort comparable** — it was chosen to give examinees time to sit the PLE, but
2014 + 6 = 2020, leaving two years of slack before the data ends.

**Consequence:** `45.44%` is not a rate any cohort experienced. It is a mixture over unequal
windows. The like-for-like figure at a fixed 8-year horizon is **39.4%**.

This limitation was *known*: `reports/01_Technical_Report.md:5` records "PLE outcomes 2011–2022".
It never reached the data dictionary, the pipeline architecture doc, either dashboard, or the
manuscript guides.

---

## 2. Three corrections to the headline, applied in sequence

The project's strongest claim is that below-40 examinees pass the PLE in large numbers, so the
40th-percentile floor was never uniformly binding. Three independent defects inflate it.

**(a) `NMS_PER_num` uses `-1` as a sentinel** for 2,866 rows (573 in the observable cohort). They
are correctly excluded from `PercentileBin` (which is NaN), but `-1 < 40` is true, so any predicate
written as `NMS_PER_num < 40` silently swallows them. Their linkage rate is 1.6% — they are
effectively unmatchable records. This *understates* the headline.

**(b) Unequal exposure**, per §1.

**(c) Contested names — a single PLE record credited to two different people.** `disambiguate()`
correctly refuses to guess on name collisions, but `get_ple_info()` later falls back to a lookup
keyed on **normalised name alone**, with no DOB or PERSON_KEY check. Measured: **1,624 names where
two or more distinct `PERSON_KEY`s are both flagged `IS_PLE_PASSER`**, covering **3,256 people**;
**232** of those names carry two genuinely different, non-empty birthdates. Since `PLE_DATA.csv` has
43,630 *unique* names, one passer record credited twice is a double-count.

These contested-name passers are **enriched in exactly the population the headline rests on**:

```
share of passers sitting on a contested name
  whole observable cohort   9.8%
  below-40 passers         13.6%
  B1 passers               14.0%
```

That enrichment is the signature of collision inflation: a shared name pools several people, and if
any one of them passed, all of them are flagged. Low scorers are less likely to be genuine passers,
so pooling lifts them relatively more.

### The corrected headline

| | below-40 linkage | n |
|---|---|---|
| published | 24.1% | 6,173 / 25,596 |
| drop `-1` sentinel rows | 24.6% | 6,164 / 25,023 |
| + equal 8-year exposure | 19.5% | 4,879 / 25,023 |
| + drop contested-name people (**conservative floor**) | **17.9%** | 4,325 / 24,185 |

B1, the lowest decile: **795 published → 482 at the conservative floor.**

### The finding survives

Under all three corrections simultaneously, the gradient is still clean and monotone:

```
B1 7.1  B2 15.7  B3 21.6  B4 28.3  B5 37.0
B6 41.8 B7 45.2  B8 46.4  B9 53.8  B10 63.3
```

**482 confirmed passers in the lowest decile, on the most conservative measure available, is still
incompatible with a uniformly enforced 40th-percentile floor.** The B4→B5 step is 8.7 points — in
line with its neighbours, confirming the earlier withdrawal of the "discontinuity" claim. What must
change is the *numbers*, not the conclusion.

---

## 3. "42.2%" was never wrong — my own earlier correction was

Commit `d323409` told readers, across five documents, that the long-standing "42.2% of stored raw
totals were incorrect" figure was wrong and used a bad denominator. **That was my error.** Measured
directly on `CEM_DATA.csv`:

```
STU_RSCORE != STU_RSCORE_CALC   107,422 / 254,308 = 42.24%
```

Both figures are correct and describe different populations:

- **42.2%** — mismatch rate across the **whole CEM file** (254,308 rows)
- **56.45%** — mismatch rate within the **NMAT-matched subset** (99,316 rows carrying a stored total)

Worse for the framing: **CEM already flagged every one of them.** `STU_RSCORE_VALID` labels exactly
those 107,422 rows `INVALID` — a perfect predictor, **zero exceptions in either direction**. The
pipeline's recalculation reproduces a QA judgement the source system had already made and shipped.
The recalculation is still correct and worth doing (median error ±1, 88.6% within ±5 — genuine
arithmetic slips, not a different quantity), but "we discovered that 42.2% were wrong" overstates it.

---

## 4. Other confirmed defects

| # | Severity | Finding |
|---|---|---|
| 1 | **HIGH** | **416 rows carry a university type contradicting their own source hint.** A `drop_duplicates(subset=["NMA_College"], keep="first")` on a key known to be ambiguous discards the per-row hint for placeholder college strings. **233 rows whose own hint says Private are counted as Public**; 181 unspecified → Public. 0.23% of rows, but one-directional, and it touches every by-university-type figure. |
| 2 | **HIGH** | **`MANUAL_APPNO_MATCH` performs no identity check at match time.** 2,330 of 35,886 accepted matches (6.5%) join on a manually supplied AppNo with no name, year or DOB verification, and hardcode `PLE_YEAR_PASSED = NaN` — so the chronology safeguard cannot run on the one stage most likely to need it. Confirmed wrong match: PLE "ABAD, ALBERTO SEÑAL" credited to NMAT "Abad, Albert Caisip". |
| 3 | **HIGH** | **The "no fuzzy matching" guarantee holds for the live code but not the lineage.** Stage 2 unconditionally reads `dataset/output/PLE_STILL_UNMATCHED.csv`, a fossil of a deleted pipeline version; 4,810 of its 7,207 rows carry `MATCH_METHOD="FUZZY"`. Fuzzy output is silently inherited. 29 PLE names also vanish from `PLE_MATCH_MASTER.csv` entirely — neither matched nor marked unmatched. |
| 4 | **HIGH** | **Pipeline 3's outputs are two months stale and it can no longer run.** Real output dir is `dataset/analysis_output/` (98 files, May 26), not the `data/` that `CLAUDE.md` and `README.md` both claim — `data/` never existed. All files predate the 31 July matcher fix. The notebook now references `IS_PLE_ANALYSIS_SAFE` and `PercentileDecile`, both removed upstream, so it `KeyError`s at load. Nothing else reads that directory. |
| 5 | **HIGH** | **A withdrawn claim is still the headline of a stakeholder document.** `reports/02_Stakeholder_Report.md:113` asserts the D4→D5 20-point step is "the strongest empirical evidence in the dataset that crossing the 40th NMAT percentile is the critical performance threshold." That finding was withdrawn; corrected it is ~9 points. Left untouched per standing instruction that `reports/` is out of scope. |
| 6 | **MEDIUM** | **`49,086 confirmed PLE passers` is a sitting count labelled as a person count.** The distinct-person figure is **37,420** (85.8% of the 43,630 source names). The 45.44% linkage rate is correctly person-level; the headline count is not. |
| 7 | **MEDIUM** | **81.83% of rows (146,413) are Filipino by Tier-3 default** — absence of foreign evidence, not positive confirmation. Load-bearing for every foreigner-vs-Filipino comparison. "Likely Foreigner" is only 13 rows, so that category distorts nothing. |
| 8 | **LOW** | **One application number carries two different score sets.** Appno 1073584, "Ventanilla, Glen Tan", 2007, same test date and centre, percentiles **98 and 80**. Earlier documented by me as "a record duplicated outright" — it is not; it is a source collision with conflicting scores. |

---

## 5. What is confirmed sound

- **Row conservation is exact.** 178,927 in `NMAT_CLEANED_DATA.csv`, 178,927 out of Pipeline 5. No
  merge fan-out at any stage; Pipeline 4 conserves the count exactly.
- **The score identity holds on every row.** `TotalRawScoreTRUE` equals the sum of the 8 components,
  and `PartI + PartII == Total`, with zero exceptions across all 178,882 non-null rows.
- **Percentile bins are correct.** B1 = 0–9 (lowest) through B10 = 90–99, contiguous,
  non-overlapping, no value outside a bin, sentinel rows excluded.
- **End-to-end value integrity.** Joining raw to final on cleaned appno: zero `Year` mismatches and
  zero `NMS_PER` discrepancies across 178,927 rows, apart from the single collided appno above.
- **Both prior `disambiguate()` fixes are real.** The `PERCENTILE_FLOOR = 40` filter is genuinely
  gone and the DOB-ordering bug is genuinely fixed (verified by line order in the current code). No
  outcome-correlated variable — score, percentile, bin — is used anywhere in identity resolution.
- **Disambiguator behaviour is honest.** 74.2% of 13,895 name-collision groups resolve on
  non-outcome criteria; 25.7% are rejected as ambiguous rather than guessed.
- **Chronology check passes.** Zero PLE-before-NMAT matches wherever the check can run (it cannot
  run on Stage 0 — see defect 2).
- **Pipeline 4 tier precedence** is enforced by construction; a later tier cannot overwrite an
  earlier one. Nationality canonicalisation (129 → 89) has no material merge errors.
- **Pipeline 3's statistics** mostly apply the right cohort: KW and chi-square deduplicate to
  best-record, PLE-outcome tests restrict to the observable cohort, Dunn applies Bonferroni. One
  gender section uses all years instead of the observable cohort — confirmed **not** propagated to
  the live `data_aggregator` page.

---

## 6. What should change

1. **State the 2011–2022 PLE window** in the data dictionary, both dashboards, and both manuscript
   guides. Nothing downstream is interpretable without it.
2. **Republish the headline numbers** with equal exposure, and present the conservative floor
   alongside: below-40 **17.9–24.6%** depending on treatment, B1 **482–795** passers. The
   conclusion is unchanged; the precision implied by a bare "24.1%" is not supportable.
3. **Fix `get_ple_info()`** to key on `PERSON_KEY`, not normalised name — defect the single largest
   contributor to false linkage.
4. **Revert the "42.2% is wrong" claim** in the five documents that now carry it, and reframe it as
   two populations plus a pre-existing CEM validity flag.
5. **Relabel `49,086`** as sittings, and publish 37,420 as the passer count.
6. **Guard the `-1` sentinel** — convert to NaN at load, or every `< 40` predicate stays wrong.
7. Decide on `reports/` (defect 5) and on Pipeline 3 (defect 4): repair or retire.
