# Superseded — historical only, do not run or cite

Everything in this folder is retired. `forensic_audit/forensic_audit.py` is the
only audit script that should be run or trusted going forward; its report is
`forensic_audit/forensic_audit_report.md` and
`forensic_audit/name_cross_check_evidence.md`.

## Why these were retired

An independent review (`.claude/audit/07_forensic_audit_review.md`) found two
defects that invalidate the headline claims produced by these scripts:

1. **"4 genuine mismatches" is not reproducible.** `name_cross_check_evidence.md`
   told readers to verify it by running `audit_name_check_deep.py`. Doing so
   today, exactly as committed, yields **17** low-score mismatches and **77**
   overall — not 4 and 6. The "4" was reached by a human manually re-reading
   and overriding 13 of the 17 flagged records. That override step exists in
   no committed file and is not reproducible by the documented command.
   Root cause: `parse_names()` in `audit_name_check_deep.py` and
   `audit_per_bin_report.py` splits surnames on whitespace and compares tokens
   literally, so it cannot recognise that "DE GUZMAN" (two tokens) and
   "DEGUZMAN" (one token) are the same Filipino compound surname written two
   ways — a systematic false-positive pattern, not a one-off bug.

2. **The name source is a stale, partially-reconciled intermediate.**
   `audit_name_check.py`, `audit_name_check_deep.py`, and
   `audit_per_bin_report.py` all read `dataset/output/PLE_MATCH_MASTER.csv`,
   which was ~7 weeks older than the analysed parquet at review time and whose
   accepted EXACT-match rows covered only ~62% of the parquet's EXACT-matched
   population. The "97.2% same-surname / 0.2% genuine mismatch" system-wide
   claim in `name_cross_check_evidence.md` describes that partial, stale
   sample, not the full matched population.

3. **No script computed the full 2x2 contingency table** (above/below
   threshold x linked/not-linked). Every version starts already restricted to
   the confirmed-passer subset, so none of them can support any claim about
   the cutoff's predictive validity — only about the passer subset's
   internal composition.

4. Four of the six scripts (`forensic_audit_v2.py`, `v3`, `v5_final.py`,
   `forensic_audit_nmat_ple_matches.py`) hardcoded their output directory to
   the repo root, not `forensic_audit/`, so re-running them as documented in
   CLAUDE.md did not reproduce the files that were actually committed.

## What was still true in these scripts

The core NMAT-score-gradient arithmetic (population counts, B4/B5 linkage
percentages, bin orientation B1=lowest/B10=highest) in `forensic_audit_v5_final.py`
was internally consistent and reproduced exactly on rerun. That part of the
old logic is folded into the new `forensic_audit.py`, now computed against the
corrected `IS_BEST_OBSERVABLE_RECORD` / `IS_OBSERVABLE_COHORT` /
`PERSON_KEY_AMBIGUOUS` flags instead of the deprecated
`IS_BEST_NMAT_RECORD & Year<=2014` combination and the removed
`IS_PLE_ANALYSIS_SAFE` column.

## Inventory

| File | What it was |
|---|---|
| `forensic_audit_nmat_ple_matches.py` | Earliest full audit script |
| `forensic_audit_v2.py` .. `v6_dashboard_impact.py` | Five successive iterations; v5 was the version cited by the committed report |
| `audit_name_check.py`, `audit_name_check_deep.py` | Name cross-check against the stale `PLE_MATCH_MASTER.csv`; source of the "4 genuine mismatches" claim |
| `audit_per_bin_report.py` | Per-bin (B1-B4) breakdown of the same name check |
| `_check_missing.py` | Ad-hoc debug script tracing two specific named records |
| `forensic_audit_classified.csv`, `forensic_audit_category_counts.csv`, `forensic_audit_low_score_details.csv` | Outputs of `forensic_audit_v5_final.py`, superseded by the new script's own outputs |

Do not resurrect the manual-override step. If a name pair needs human
judgement, it belongs in `forensic_audit/forensic_audit_exceptions.csv` as a
reviewable row, not as a silent reclassification inside a script.
