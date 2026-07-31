# D4 — forensic_audit/ consolidation log

**Status: DONE, but PROVISIONAL.** Ran against `dataset/NMAT_Exodus.parquet` as of 2026-07-31
(52 cols, includes the new `PLE_MATCH_OUTCOME` diagnostic column; still pre-`disambiguate()`-Step-4-fix
in substance — `PLE_MATCH_METHOD`/`IS_PLE_PASSER` counts unchanged from the earlier 51-col run).
Per the orchestrator, P1 is re-running Pipeline 2 with `disambiguate()` Step 4 removed. **When that
lands, re-run `forensic_audit/forensic_audit.py` and regenerate both markdown reports — the script
hardcodes nothing, so this is a one-command re-run, not a rewrite.**

## What I consolidated

Moved 10 files to `forensic_audit/_superseded/` with a README explaining why: `forensic_audit_v2.py`
through `v6_dashboard_impact.py`, `forensic_audit_nmat_ple_matches.py`, `audit_name_check.py`,
`audit_name_check_deep.py`, `audit_per_bin_report.py`, `_check_missing.py`, plus their stale outputs
(`forensic_audit_classified.csv`, `forensic_audit_category_counts.csv`,
`forensic_audit_low_score_details.csv`). Wrote one new script, `forensic_audit/forensic_audit.py`
(all paths relative to `os.path.dirname(__file__)`, so `./.venv/Scripts/python.exe
forensic_audit/forensic_audit.py` from repo root reproduces every output into `forensic_audit/`,
fixing F5 from `07_forensic_audit_review.md`).

## Bug I found and fixed in my own first draft

First run of the name-check section flagged **2,372 of 2,372** checked rows as `genuine_mismatch`
— every single one, with an empty NMAT-side name. Root cause: `PERSON_KEY.str.split("||")` — pandas
treats a >1-character `pat` as **regex** by default, and `"||"` as regex means "empty pattern OR
empty pattern", which matches at every character position and shreds the string. Fixed with
`str.partition("||")[0]` (literal, not regex). Re-ran; verdict distribution became sane (see below).
Flagging this because it's exactly the kind of silent-corruption bug this whole audit exists to
catch, and it would have produced a fake "system-wide identity crisis" headline if I hadn't sanity-
checked the raw output before writing it up.

## Normaliser's effect on compound-surname false positives

Implemented `normalize_surname()` in code (merges Filipino prefix tokens De/Dela/Del/La/Las/Los/San/
Santa/Santo/Sto/Sta with the following token — see `name_cross_check_evidence.md` §2 for the exact
function). Applied to the same 2,372-row checked population, raw vs. normalised:

| | Raw | Normalised | Resolved |
|---|---:|---:|---:|
| `genuine_mismatch`, overall | 55 | 36 | **19** |
| `genuine_mismatch`, low-score (<40th %ile) subset (n=476) | 13 | 10 | **3** |

No manual override anywhere. The 36 (and 10) that remain are written verbatim to
`forensic_audit_exceptions.csv` (`exception_type=unresolved_genuine_mismatch`) — not reclassified.
3 of the old "4 genuine mismatches" (AHUJA/PYDI, ROXAS/ROYALES, LIAO/LIM) reproduce identically in
this list. The 4th (CASAO) is now correctly separated into `ambiguous_source_conflict` — the source
file has two competing PLE-name candidates for that one APPNO, which a name-parser cannot and should
not resolve by itself.

**Note this is not the "17" the old script's headline referenced** — that 17 came from a smaller,
stale-file-only population. This run's 55/13 raw counts are on the full current-parquet APPNO-based
population, so they aren't directly comparable to 17; the like-for-like comparison is raw-vs-normalised
within this run, which is the 19/3 resolved above.

## Coverage

Population checked: 2,868 APPNO-based matched rows (`MANUAL_APPNO_MATCH` + `DETERMINISTIC_APPNO`),
dataset-wide, joined to `dataset/output/PLE_MATCH_MASTER.csv` (the only file in the repo carrying a
PLE-side name — unavoidable, since `NMAT_Exodus.parquet` has no PLE name column at all).

- **Matched (checkable): 2,372 (82.7%)**
- Ambiguous source conflict (>1 PLE-name candidate for one APPNO in the master file): 5 (0.2%)
- **Uncoverable (no master record at all): 491 (17.1%)** — reported as unverified, not assumed clean.

NMAT-side names now come from `PERSON_KEY` in the current parquet (not the stale intermediate); the
PLE-side name is still necessarily the stale/partial `PLE_MATCH_MASTER.csv`, and that gap (the
17.1%) is disclosed rather than silently absorbed, per F2 in `07_forensic_audit_review.md`.

## 2×2 contingency tables (first time computed in this repo)

Full tables at 30/35/40/45/50th percentile, for `best_obs` (69,503 people,
`IS_BEST_OBSERVABLE_RECORD`) and `best_obs_clean` (67,103, `PERSON_KEY_AMBIGUOUS` excluded). At the
40th-percentile threshold, `best_obs_clean`: Above&Linked=26,483, Above&NotLinked=15,175,
Below&Linked=4,391, Below&NotLinked=20,299 (sensitivity 85.8%, specificity 57.2%, PPV 63.6%, NPV
82.2%). Every cell explicitly caveated as conditional-on-admission (never predictive validity) and,
for the Below&Linked cell specifically, as a pre-fix floor pending the Pipeline-2 rerun (see below).
Full 10-row table: `forensic_audit/forensic_audit_contingency_2x2.csv`.

B4→B5 linkage jump: 25.9%→47.2% (+21.3pp) including ambiguous keys; 26.8%→47.2% (+20.4pp) excluding
them — essentially unchanged by the ambiguous-key exclusion, stated explicitly in the report.

## New finding folded in mid-task: matcher suppression (T2)

The orchestrator flagged, after I'd started, that `2_PLE_Matching_Pipeline.ipynb` `disambiguate()`
Step 4 hard-drops any name-collision candidate scoring below the 40th percentile (`PERCENTILE_FLOOR
= 40`) and rejects the match outright if every surviving candidate is below 40 — the same constant
this audit investigates. This is distinct from the admission-selection effect (T1) and is scoped to
EXACT matches with >1 same-name candidate (APPNO-based matches are unaffected — they don't call
`disambiguate()`). I added both as named, distinct threats to validity (`forensic_audit_report.md`
§0), report Sections 2 and 3 twice (with/without `PERSON_KEY_AMBIGUOUS`) per the orchestrator's
request, and withdrew any rarity claim about below-cutoff passers (existence is not withdrawn —
Section 3 shows ~4,400 of them at the 40th-percentile line). I did not modify the notebook — that's
P1's file, outside `forensic_audit/`.

## Claims withdrawn (full list in `forensic_audit_report.md` §5 and `name_cross_check_evidence.md` §7)

1. "4 genuine mismatches" — not reproducible, required an undocumented manual override.
2. "97.2% same-surname / 0.2% genuine mismatch" system-wide — computed on a ~62%-coverage, ~7-week-stale
   name source; not restated in the rewrite at all.
3. Any claim about how *rare* below-cutoff passers are — confounded by T2 (matcher suppression), not
   just T1 (admission selection). Existence, not rarity, is what the data supports.
4. "3,647 confirmed PLE passers below B5" — silently mixed pre-dedup/post-dedup N's under one
   heading in the old report; superseded by Section 2/3, which use one stated N throughout.
5. Any cut-off-validity conclusion — never established by any version of this audit; the 2×2 tables
   (new in this rewrite) are explicitly labeled conditional-on-admission, not predictive validity.

## What I could NOT do

- Could not verify the T2 fix's effect on any number — Pipeline 2 hadn't been rerun as of this audit.
  The report is explicitly marked PROVISIONAL and states the exact re-run command.
- Could not close the 17.1% name-check coverage gap — no file in this repo carries PLE-side names
  for those 491 rows. Reported as unverified, not fabricated or assumed clean.
- Did not attempt a system-wide (EXACT-match-inclusive) name-quality figure — out of scope per
  Section 0 of `name_cross_check_evidence.md` (EXACT matches are matched by name equality already,
  so re-checking them is close to tautological); flagged as a legitimate gap, not filled with a
  low-confidence number.

## Verify

```
./.venv/Scripts/python.exe forensic_audit/forensic_audit.py
```
Ran end-to-end, exit code 0, ~65s. Output files: `forensic_audit_summary.csv`,
`forensic_audit_selection_effect.csv`, `forensic_audit_contingency_2x2.csv`,
`forensic_audit_name_check_results.csv` (2,372 rows), `forensic_audit_exceptions.csv` (532 rows —
36 unresolved mismatches + 5 ambiguous-source conflicts + 491 uncoverable). All under
`forensic_audit/`, confirmed by `ls` after the run.
