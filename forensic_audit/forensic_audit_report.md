# Forensic Audit — NMAT → PLE (consolidated, rewritten)

**Script:** `forensic_audit/forensic_audit.py` (the only audit script in this repo that should be
run or trusted — see `forensic_audit/_superseded/README.md` for what this replaces and why).

**Reproduce:**
```
./.venv/Scripts/python.exe forensic_audit/forensic_audit.py
```
Run from any working directory — every path in the script is relative to the script's own
location, so this always writes into `forensic_audit/`, never the repo root.

**Every number in this document comes from that command**, run against
`dataset/NMAT_Exodus.parquet` (md5 `72b2808bb8bb9c3594980c5735f814e1`, 178,927 rows × 53 cols, the
FINAL post-fix parquet per the orchestrator). No hand-edited values, no manual override step.

---

## STATUS: final — reflects the `disambiguate()` Step-4 fix

**This document supersedes two earlier drafts made while the pipeline was mid-flight.** The parquet
changed materially while this audit was in progress and was re-run twice: draft 1 was against
pre-fix data (`IS_PLE_PASSER` summing to 51,707); draft 2 was against data immediately after P1
removed `disambiguate()` Step 4 but before this script's own band-labeling bug (below) was found and
fixed. **This is draft 3, the first correct one**, confirmed against the orchestrator-supplied md5.

**Bug found and fixed in this script between drafts 2 and 3:** the script originally recomputed
score bands from `NMS_PER_num` with its own cut, instead of using the dataset's canonical
`PercentileBin` column. The two disagree on 573 best-observable rows, all in the B1 range —
`PercentileBin` is null for them (invalid/unbinnable for a reason upstream) while a naive re-cut of
`NMS_PER_num` would include them as B1. This inflated B1's N and slightly diluted its linkage rate.
Switched to `df["PercentileBin"]` directly; the fix brought this report's B1 figure (795 linked /
6,853 people, 11.60%) into exact agreement with the orchestrator's independently-computed number.
Sections 3 (2×2 tables) were never affected — they threshold `NMS_PER_num` directly, not bands.

---

## 0. Framing correction — read this before the tables

**The original question this audit was commissioned to answer — "how can anyone below the cut-off
appear as a confirmed PLE passer at all?" — has the wrong shape.** The corrected data shows
below-cutoff passers are **not rare**: 795 confirmed passers in the lowest decile (B1) alone, 2,330
in B4. Under a strictly and uniformly binding 40th-percentile admission rule this should be close to
impossible. It isn't. **The RDD/sharp-discontinuity framing is withdrawn** (see §0c) — the right
question is not "how do these anomalies exist" but **"why was the existing 40th-percentile rule
evidently not uniformly binding?"** Candidate explanations this dataset can name but not adjudicate
between: pre-2016 cohorts sitting before CMO 18 s.2016 existed, institutional discretion / exception
admits, foreign-applicant pathways with different admission rules, and outright data/identity
artifacts still present despite the fixes below (`PERSON_KEY_AMBIGUOUS`, the 17.1% name-check
coverage gap in §4). This audit cannot distinguish between these without an institution- or
applicant-category-level field this dataset does not have — see §5 for what is explicitly not
claimed here.

### 0a — T1: Admission selection (real-world policy, permanent, still applies)
CMO 18 s.2016 enforces a 40th-percentile floor for admission. People who scored below it were
largely barred from enrolling at all, so anyone observed here scoring below B5 is an **atypical
admitted residual**, not a random sample of everyone who ever scored below the cutoff. This is a
fact about the world and continues to caveat every number below.

### 0b — T2: Matcher suppression (our own code — FIXED in the data this report uses)
`2_PLE_Matching_Pipeline.ipynb`'s `disambiguate()` used to contain a Step 4:
```python
PERCENTILE_FLOOR = 40
pct_pass = [r for r in latest_pass if r["NMS_PER_num"] >= PERCENTILE_FLOOR]
if not pct_pass:
    return {"status": "NO_VALID_MATCH", ...}
```
a **hard filter, not a tie-break**, reached only when a PLE name matched more than one NMAT candidate
(a name-collision group, from the EXACT-match stage only). Within such a group, any candidate below
the 40th percentile was discarded before the final pick, and the match rejected outright if every
survivor was below 40 — the same constant under investigation. **This step is now removed**
(confirmed by reading the current notebook: `PERCENTILE_FLOOR` is retained only as an unused,
explicitly-commented historical constant). `IS_PLE_PASSER` moved from 51,707 (pre-fix) to 49,086
(post-fix) — down overall, because previously-narrowed name-collision groups now more often resolve
honestly to `AMBIGUOUS_NAME_COLLISION` rejections (8,216 rows, new `PLE_MATCH_OUTCOME` column) instead
of being silently narrowed to one survivor by the percentile filter — while **below-40 linkage rose
substantially** (B1: 8.1%→11.6%, B4: 25.9%→36.0%, per the orchestrator's independently-computed
before/after). **The old figures understated exactly the population this audit exists to
investigate**, because our own matcher was suppressing them.

### 0c — RDD/sharp-discontinuity framing: withdrawn
The B4→B5 jump is **+9.6 points** post-fix (36.0%→45.6%), down from +21.3 points pre-fix. Comparing
it to every other adjacent-band step in the same table (`best_obs`, post-fix):

| Step | Δ points |
|---|---:|
| B1→B2 | +11.1 |
| B2→B3 | +6.6 |
| B3→B4 | +6.7 |
| **B4→B5** | **+9.6** |
| B5→B6 | +4.8 |
| B6→B7 | +3.2 |
| B7→B8 | +1.5 |
| B8→B9 | +6.6 |
| B9→B10 | +9.4 |

**B4→B5 is not the largest step in the table — B1→B2 is larger, and B9→B10 is comparable.** A prior
draft of this audit's framing (and the orchestrator's own initial characterization of the dataset)
leaned on the B4→B5 jump as a sharp, cutoff-specific discontinuity worth a regression-discontinuity
analysis. **That framing is withdrawn.** The step at the 40th-percentile line is unremarkable next to
the step one band lower, which sits at no policy threshold at all. Any discontinuity narrative built
on the pre-fix +21.3-point jump was itself an artifact of T2, not a real design feature of the data.

**Consequence for `PERSON_KEY_AMBIGUOUS`:** T2's suppression and `PERSON_KEY_AMBIGUOUS` trace to the
same root condition — a name shared by more than one distinct record. Sections 2 and 3 are reported
**twice** throughout: once including `PERSON_KEY_AMBIGUOUS` people, once excluding them.

---

## 1. Audit population

Uses the corrected schema flags (`.claude/audit/_TARGET_SCHEMA_CONTRACT.md`), **not**
`IS_BEST_NMAT_RECORD & Year<=2014` and **not** the removed `IS_PLE_ANALYSIS_SAFE`. Bands come from
the dataset's own `PercentileBin` column (see the bug note above), not a recomputed cut.

| Population | Definition | N |
|---|---|---|
| Row-level observable cohort | `IS_OBSERVABLE_COHORT` (`Year<=2014`) | 88,144 rows |
| Person-level best-in-window | `IS_BEST_OBSERVABLE_RECORD` | 69,503 people |
| `PERSON_KEY_AMBIGUOUS` keys, dataset-wide | contradictory SEX across the key's rows | 6,148 keys |
| `PERSON_KEY_AMBIGUOUS` people within the observable population | | 2,400 (3.45%) |
| **`best_obs_clean`** (ambiguous keys excluded) | the primary population used below | **67,103 people** |

| Band | best_obs | best_obs_clean |
|---|---:|---:|
| B1 | 6,853 | 6,611 |
| B2 | 5,884 | 5,648 |
| B3 | 5,813 | 5,623 |
| B4 | 6,473 | 6,252 |
| B5 | 6,582 | 6,352 |
| B6 | 6,284 | 6,051 |
| B7 | 6,359 | 6,109 |
| B8 | 6,704 | 6,413 |
| B9 | 7,263 | 7,002 |
| B10 | 9,958 | 9,731 |
| Missing (null `PercentileBin`) | 1,330 | 1,311 |

**A positive finding, re-verified rather than assumed:** the old audit
(`_superseded/forensic_audit_v5_final.py` Section 5) manually excluded "data_quality" records —
negative/zero `PLE_YEAR_GAP`, duplicate best-record rows, shared-APPNO-across-persons. Under the
corrected flags, all three are now **zero** by construction. No manual "data_quality" exclusion
category is needed in this rewrite. The only remaining known identity risk is
`PERSON_KEY_AMBIGUOUS`, handled explicitly throughout.

---

## 2. Selection effect — linkage rate by score band (post-T2-fix data)

**"Linked" means `IS_PLE_PASSER` is True. The PLE source file contains passers only. "Not linked" is
never "failed"; it means no confirmed passer record was found (never enrolled, hasn't sat the
boards, genuinely failed, or rejected as an ambiguous name-collision — indistinguishable here).**

### best_obs (n=69,503, includes ambiguous keys)

| Band | N | Linked | Linkage rate |
|---|---:|---:|---:|
| B1 | 6,853 | 795 | **11.6%** |
| B2 | 5,884 | 1,336 | 22.7% |
| B3 | 5,813 | 1,703 | 29.3% |
| B4 | 6,473 | 2,330 | 36.0% |
| **B5** | 6,582 | 3,003 | **45.6%** |
| B6 | 6,284 | 3,168 | 50.4% |
| B7 | 6,359 | 3,407 | 53.6% |
| B8 | 6,704 | 3,690 | 55.0% |
| B9 | 7,263 | 4,474 | 61.6% |
| B10 | 9,958 | 7,073 | 71.0% |

**B4→B5 jump: +9.6 points** (36.0% → 45.6%) — see §0c for why this is not a special discontinuity.

### best_obs_clean (n=67,103, ambiguous keys excluded)

| Band | N | Linked | Linkage rate |
|---|---:|---:|---:|
| B1 | 6,611 | 769 | 11.6% |
| B2 | 5,648 | 1,287 | 22.8% |
| B3 | 5,623 | 1,662 | 29.6% |
| B4 | 6,252 | 2,260 | 36.1% |
| **B5** | 6,352 | 2,913 | **45.9%** |
| B6 | 6,051 | 3,084 | 51.0% |
| B7 | 6,109 | 3,314 | 54.3% |
| B8 | 6,413 | 3,613 | 56.3% |
| B9 | 7,002 | 4,380 | 62.6% |
| B10 | 9,731 | 6,957 | 71.5% |

**B4→B5 jump: +9.7 points.** Essentially unchanged by excluding ambiguous keys (+9.6 vs +9.7) — the
currently-visible ambiguous-identity population is not, by itself, driving the size of the jump.
Full per-band table: `forensic_audit_selection_effect.csv`.

**Interpretation:** below-cutoff linkage is now known to be **substantially more common** than the
pre-fix data showed (B1 rose from 8.1% to 11.6%; B4 from 25.9% to 36.0%). This does not mean the
40th-percentile cutoff has no relationship to outcomes — B1-B4 are still well below B5-B10 — but it
means the old "how can this happen at all" framing was measuring our own matcher bug more than the
underlying phenomenon. **No conclusion about lowering the cutoff to the 30th percentile follows from
this table either way** — see T1 (§0a).

---

## 3. Full 2×2 contingency tables (post-T2-fix data)

The first time any script in this repository computes the complement of the passer subset — people
in the observable population who are **not** confirmed PLE passers — at each candidate threshold.
Population: `best_obs` / `best_obs_clean`, restricted to rows with a non-null `NMS_PER_num` (757 /
755 excluded respectively). Unaffected by the band-labeling bug in §STATUS — these threshold on the
continuous score directly.

**CAVEAT:**
- "Sensitivity/specificity/PPV/NPV" are used in the strict statistical 2×2-table sense only — **NOT
  predictive validity**, because we never observe outcomes for people who were **not admitted** at
  all. Every row is **conditional on admission** (T1) — permanent, not fixable by any data
  correction.
- These figures already reflect the T2 fix; they moved substantially from the pre-fix run (see the
  git history of this document / `.claude/audit/logs/D4_forensic_audit.md`).

### best_obs_clean (ambiguous keys excluded), table population = 66,348

| Threshold | Above & Linked | Above & Not Linked | Below & Linked | Below & Not Linked | Base rate linked | Sens. | Spec. | PPV | NPV |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 30th %ile | 26,521 | 21,389 | 3,726 | 14,712 | 45.6% | 87.7% | 40.8% | 55.4% | 79.8% |
| 35th %ile | 25,467 | 19,318 | 4,780 | 16,783 | 45.6% | 84.2% | 46.5% | 56.9% | 77.8% |
| 40th %ile | 24,261 | 17,397 | 5,986 | 18,704 | 45.6% | 80.2% | 51.8% | 58.2% | 75.8% |
| 45th %ile | 22,874 | 15,673 | 7,373 | 20,428 | 45.6% | 75.6% | 56.6% | 59.3% | 73.5% |
| 50th %ile | 21,348 | 13,958 | 8,899 | 22,143 | 45.6% | 70.6% | 61.3% | 60.5% | 71.3% |

### best_obs (includes ambiguous keys), table population = 68,746 — for comparison

| Threshold | Above & Linked | Above & Not Linked | Below & Linked | Below & Not Linked | Sens. | Spec. | PPV | NPV |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 30th %ile | 27,145 | 22,478 | 3,843 | 15,280 | 87.6% | 40.5% | 54.7% | 79.9% |
| 40th %ile | 24,815 | 18,335 | 6,173 | 19,423 | 80.1% | 51.4% | 57.5% | 75.9% |
| 50th %ile | 21,812 | 14,756 | 9,176 | 23,002 | 70.4% | 60.9% | 59.6% | 71.5% |

Full 10-row table (both populations × 5 thresholds): `forensic_audit_contingency_2x2.csv`.

**Reading these responsibly:** at the 40th-percentile threshold (`best_obs_clean`), 5,986 people
scored below cutoff and were still linked to a confirmed PLE pass, out of 24,690 people below cutoff
overall (24.2% base linkage below the line vs. 58.2% above it). That gap is real and, per §0, larger
than pre-fix data suggested at the low end — but the below-cutoff group observed here is still not a
random sample of "everyone who could have scored below cutoff" (T1), and it cannot distinguish
pre-2016 cohorts, exception admits, foreign-applicant pathways, or residual identity artifacts from
each other (§0).

---

## 4. Name cross-check — see `name_cross_check_evidence.md` for full detail

T2's fix changes *which* PLE record links to which NMAT record for name-collision groups; it does
not touch `MANUAL_APPNO_MATCH` / `DETERMINISTIC_APPNO` records (those never call `disambiguate()`),
so this section's population and results are unaffected in substance by the fix.

Of 2,867 APPNO-based matches, **82.7% (2,371) could be checked** against
`dataset/output/PLE_MATCH_MASTER.csv`, the only file in this repo carrying PLE-side names. A
deterministic compound-surname normaliser (implemented in code, applied uniformly, no manual step)
resolves 19 of 55 raw `genuine_mismatch` flags, leaving **36 unresolved** (10 of them in the
low-score, <40th-percentile subset).

---

## 5. What is explicitly withdrawn, and what is NOT claimed

| Prior claim | Status | Why |
|---|---|---|
| "4 genuine mismatches" (`name_cross_check_evidence.md`, old version) | **Withdrawn** | Required an undocumented manual override of 13 of the 17 records the cited script actually flagged. Not reproducible by the command the old document told readers to run. |
| "97.2% same-surname / 0.2% genuine mismatch" system-wide | **Withdrawn** | Computed against a name source covering only ~62% of the parquet's EXACT-matched population, ~7 weeks stale. Not restated here — see §4 coverage caveat. |
| Any claim about how *rare* below-cutoff PLE passers are | **Withdrawn** | The opposite is now shown: they are common (11.6% linkage in B1, 36.0% in B4). The denominator was suppressed by our own matcher (T2), not merely reduced by admission selection (T1). |
| B4→B5 as a sharp, cutoff-specific discontinuity / RDD candidate | **Withdrawn** (§0c) | Post-fix, the step (+9.6pp) is smaller than the B1→B2 step (+11.1pp) and comparable to B9→B10 (+9.4pp) — not a special feature of the 40th-percentile line. |
| "The 3,647 confirmed PLE passers below B5 are valid observations" (old `forensic_audit_report.md`) | **Withdrawn as stated** | Two different N's (pre-/post-dedup) were silently used under one heading. Superseded by §2/§3 above. |
| **Any explanation for *why* the 40th-percentile rule was not uniformly binding** | **Not claimed — data cannot support it** | This dataset has no institution identifier, no admission-year-vs-CMO-effective-date field, no applicant-category (foreign/exception-admit) field beyond `FOREIGNER_STATUS`, and no enrolment record. §0 names candidate explanations (pre-2016 cohorts, institutional discretion, foreign pathways, residual identity artifacts) as *hypotheses to investigate elsewhere*, not findings. |
| Any cut-off-validity or predictive-validity conclusion | **Never established** | §3's 2×2 tables are explicitly conditional-on-admission, not predictive validity, by construction (T1). |

---

## 6. Outputs

| File | Contents |
|---|---|
| `forensic_audit_summary.csv` | Section 1/2/4 headline numbers, one row per metric |
| `forensic_audit_selection_effect.csv` | Section 2 full per-band table, both populations |
| `forensic_audit_contingency_2x2.csv` | Section 3 full 2×2 tables, both populations × 5 thresholds |
| `forensic_audit_name_check_results.csv` | Every checked APPNO-based row, both verdicts (raw / normalised) |
| `forensic_audit_exceptions.csv` | Unresolved mismatches + ambiguous-source conflicts + uncoverable rows — for human review, never silently reclassified |
