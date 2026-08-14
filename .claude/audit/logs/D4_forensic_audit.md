# D4 — forensic_audit/ consolidation log

**Status: DONE, final.** Ran against `dataset/NMAT_Exodus.parquet`, md5 `72b2808bb8bb9c3594980c5735f814e1`
(178,927 rows × 53 cols) — confirmed against the orchestrator's stated final md5. This is post the
`disambiguate()` Step-4 matcher-suppression fix (verified directly by reading
`2_PLE_Matching_Pipeline.ipynb`: `PERCENTILE_FLOOR` is now an unused, explicitly-commented historical
constant, not a live filter).

## What I consolidated

Moved 10 files to `forensic_audit/_superseded/` with a README explaining why: `forensic_audit_v2.py`
through `v6_dashboard_impact.py`, `forensic_audit_nmat_ple_matches.py`, `audit_name_check.py`,
`audit_name_check_deep.py`, `audit_per_bin_report.py`, `_check_missing.py`, plus their stale outputs
(`forensic_audit_classified.csv`, `forensic_audit_category_counts.csv`,
`forensic_audit_low_score_details.csv`). Wrote one new script, `forensic_audit/forensic_audit.py`
(all paths relative to `os.path.dirname(__file__)`, so `./.venv/Scripts/python.exe
forensic_audit/forensic_audit.py` from repo root reproduces every output into `forensic_audit/`,
fixing F5 from `07_forensic_audit_review.md`).

## Two bugs I found and fixed in my own script (both self-caught, both fixed before finalizing)

1. **`PERSON_KEY.str.split("||")` corrupted every NMAT-side name to empty string.** Pandas treats a
   >1-character `pat` as **regex** by default, and `"||"` as regex means "empty pattern OR empty
   pattern" — matches at every character position and shreds the string. First run of the name-check
   flagged 2,372/2,372 rows as `genuine_mismatch` (100%) with an empty NMAT name on every row — an
   obviously fake "identity crisis" that would have been a bad headline if not sanity-checked. Fixed
   with `str.partition("||")[0]` (literal, not regex).

2. **Recomputing score bands from `NMS_PER_num` instead of using the dataset's canonical
   `PercentileBin` column.** The two disagree on 573 best-observable rows, all in the B1 range —
   `PercentileBin` is null for them (invalid/unbinnable for a reason upstream in the pipeline) while
   a naive `pct<10` re-cut of `NMS_PER_num` counted them as B1, inflating B1's N (7,426 vs the
   correct 6,853) and diluting its linkage rate (10.8% vs the correct 11.6%). Caught because my B1
   figure didn't match the orchestrator's independently-computed number (795 linked / 11.60%) —
   after switching to `df["PercentileBin"].fillna("Missing")`, it matched exactly. Sections 3 (2×2
   tables) were never affected — they threshold `NMS_PER_num` directly, not bands.

Flagging both because catching your own tool's bugs before publishing its output is exactly what
this audit exists to model.

## The central finding, corrected twice during this task

The parquet changed materially **twice** while I was working, both times flagged to me by the
orchestrator with exact before/after numbers I cross-checked against my own run:

1. **Pre-fix → post-`disambiguate()`-Step-4-fix.** `IS_PLE_PASSER` moved 51,707 → 49,086. Below-40
   linkage rose sharply (B1: 8.1%→11.6%, B4: 25.9%→36.0%) because the matcher had been discarding
   below-40th-percentile candidates inside EXACT-match name-collision groups, using the same 40th
   constant this audit investigates (`2_PLE_Matching_Pipeline.ipynb` `disambiguate()` Step 4,
   `PERCENTILE_FLOOR=40`, confined to EXACT matches with >1 same-name candidate — `MANUAL_APPNO_MATCH`
   / `DETERMINISTIC_APPNO` never call it). **The original "how can anyone below cutoff pass at all"
   framing is now known to be measuring an undercount, not a rarity.**
2. **RDD/discontinuity framing withdrawn.** Post-fix, the B4→B5 step is +9.6pp — smaller than B1→B2
   (+11.1pp) and comparable to B9→B10 (+9.4pp). I added the full adjacent-band delta table to
   `forensic_audit_report.md` §0c to make this checkable at a glance. Reframed the report's central
   question from "how do these anomalies exist" to "why was the 40th-percentile rule evidently not
   uniformly binding" — and explicitly listed what this dataset cannot adjudicate between (pre-2016
   cohorts, institutional discretion, foreign pathways, residual identity artifacts) rather than
   guessing.

**Every number in the final `forensic_audit_report.md` and `name_cross_check_evidence.md` comes from
the run against the final md5 above** — I re-ran end to end after each of the two data changes and
after each of my own two bugs, never hand-edited a number forward from a stale run.

## Normaliser's effect on compound-surname false positives

Applied to the 2,371-row checked APPNO-based population (raw vs. normalised):

| | Raw | Normalised | Resolved |
|---|---:|---:|---:|
| `genuine_mismatch`, overall | 55 | 36 | **19** |
| `genuine_mismatch`, low-score (<40th %ile) subset (n=475) | 13 | 10 | **3** |

No manual override anywhere. The 36 (and 10) that remain are written verbatim to
`forensic_audit_exceptions.csv` (`exception_type=unresolved_genuine_mismatch`) — not reclassified.
3 of the old "4 genuine mismatches" (AHUJA/PYDI, ROXAS/ROYALES, LIAO/LIM) reproduce identically in
this list. The 4th (CASAO) is now correctly separated into `ambiguous_source_conflict` — the source
file has two competing PLE-name candidates for that one APPNO, which a name-parser cannot and should
not resolve by itself.

## Coverage

2,867 APPNO-based matched rows (`MANUAL_APPNO_MATCH` + `DETERMINISTIC_APPNO`), dataset-wide, joined
to `dataset/output/PLE_MATCH_MASTER.csv` (the only file in the repo carrying a PLE-side name).
- **Matched (checkable): 2,371 (82.7%)**
- Ambiguous source conflict: 5 (0.2%)
- **Uncoverable (no master record at all): 491 (17.1%)** — reported as unverified, not assumed clean.

This section of the audit is unaffected in substance by the Step-4 fix: `MANUAL_APPNO_MATCH` /
`DETERMINISTIC_APPNO` never call `disambiguate()`. The 1-row drift (2,868→2,867 across pipeline
re-runs) is ordinary non-determinism at the margins, not a T2 effect.

## 2×2 contingency tables (first time computed in this repo)

Full tables at 30/35/40/45/50th percentile, for `best_obs` (69,503, `IS_BEST_OBSERVABLE_RECORD`) and
`best_obs_clean` (67,103, `PERSON_KEY_AMBIGUOUS` excluded). At the 40th-percentile threshold,
`best_obs_clean`: Above&Linked=24,261, Above&NotLinked=17,397, Below&Linked=5,986,
Below&NotLinked=18,704 (sensitivity 80.2%, specificity 51.8%, PPV 58.2%, NPV 75.8%). Every cell
explicitly caveated as conditional-on-admission, never predictive validity. Full 10-row table:
`forensic_audit/forensic_audit_contingency_2x2.csv`.

B4→B5 linkage jump: 36.0%→45.6% (+9.6pp) including ambiguous keys; 36.1%→45.9% (+9.7pp) excluding
them — essentially unchanged by the ambiguous-key exclusion, stated explicitly in the report. Both
figures are roughly half the pre-fix jump (+21.3pp / +20.4pp), which is itself evidence the old jump
was substantially a T2 artifact.

## Claims withdrawn (full list in `forensic_audit_report.md` §5 and `name_cross_check_evidence.md` §7)

1. "4 genuine mismatches" — not reproducible, required an undocumented manual override.
2. "97.2% same-surname / 0.2% genuine mismatch" system-wide — computed on a ~62%-coverage, ~7-week-stale
   name source; not restated in the rewrite at all.
3. Any claim about how *rare* below-cutoff passers are — the opposite is now shown (11.6%/36.0%
   linkage in B1/B4). Denominator was suppressed by our own matcher (T2), not just admission
   selection (T1).
4. B4→B5 as a sharp, cutoff-specific discontinuity worth an RDD analysis — post-fix it's smaller than
   the B1→B2 step and unremarkable next to the rest of the adjacent-band gradient.
5. "3,647 confirmed PLE passers below B5" — silently mixed pre-dedup/post-dedup N's under one
   heading in the old report; superseded by §2/§3, which use one stated N throughout.
6. Any cut-off-validity conclusion — never established by any version of this audit; the 2×2 tables
   (new in this rewrite) are explicitly labeled conditional-on-admission, not predictive validity.

## What I could NOT do

- Could not identify *why* the 40th-percentile rule wasn't uniformly binding — no institution
  identifier, no admission-year-vs-CMO-effective-date field, no applicant-category field beyond
  `FOREIGNER_STATUS`, no enrolment record. Named the candidate hypotheses (pre-2016 cohorts,
  institutional discretion, foreign pathways, residual identity artifacts) explicitly as unresolved
  in `forensic_audit_report.md` §0 and §5, not guessed at.
- Could not close the 17.1% name-check coverage gap — no file in this repo carries PLE-side names
  for those 491 rows. Reported as unverified, not fabricated or assumed clean.
- Did not attempt a system-wide (EXACT-match-inclusive) name-quality figure — out of scope per
  Section 0 of `name_cross_check_evidence.md` (EXACT matches are matched by name equality already).

## Verify

```
./.venv/Scripts/python.exe forensic_audit/forensic_audit.py
```
Ran end-to-end 4 times total during this task (2 to catch/fix my own bugs, 2 to track the pipeline's
own data changes), exit code 0 each time, ~30-60s. Final md5 of the input parquet matches the
orchestrator's stated `72b2808bb8bb9c3594980c5735f814e1`. Output files:
`forensic_audit_summary.csv`, `forensic_audit_selection_effect.csv`,
`forensic_audit_contingency_2x2.csv`, `forensic_audit_name_check_results.csv` (2,371 rows),
`forensic_audit_exceptions.csv` (532 rows — 36 unresolved mismatches + 5 ambiguous-source conflicts +
491 uncoverable). All under `forensic_audit/`, confirmed by `ls` after the run.
