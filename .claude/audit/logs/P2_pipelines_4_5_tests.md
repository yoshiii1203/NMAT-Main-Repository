# P2 — Pipelines 4/5 and the data-invariant test suite

Scope: `4_Citizenship_Integration.py`, new `5_Slim_Exodus.py`, new
`tests/test_data_invariants.py`. All commands run with
`./.venv/Scripts/python.exe` from repo root unless noted. Dry-runs against
the live `dataset/` inputs were done in an isolated scratch copy
(`%TEMP%/.../scratchpad/p4_dryrun/`) — `dataset/NMAT_Exodus.parquet` and the
two dashboard-folder copies were **not** touched by any dry-run; only the
final `pytest tests/` run at the end reads (never writes) the real shipped
file.

---

## Task 1 — `4_Citizenship_Integration.py`

### Changes (file:line references are post-edit)

1. **`"Foreign"` placeholder renamed.** Tier-1b assignment (`4_Citizenship_Integration.py`,
   "Tier 1b" section) now writes `"Foreign (unspecified)"` instead of the bare
   `"Foreign"`, so it can never masquerade as a country name in a
   `value_counts()`/chart over `CITIZENSHIP_FINAL`.
2. **`name_based_assessment` dropped from the output**, per the brief's
   recommendation (Audit-01 F1: merged and shown in the dashboard, but never
   consulted by the tier-decision logic, and disagrees with the final label
   in 23 of 871 profiled rows — corroborating evidence that corroborates
   nothing). Added to the `cols_to_drop` list at the end of `main()`, with an
   inline comment documenting the reasoning. I did **not** wire it in as a
   Tier-1c tiebreak (the brief's alternative option) — the 6-row disagreement
   set (Audit-01 F4) is too small and too unaudited to make an automated
   citizenship-status decision on; dropping is the honest option, using it
   silently would just relocate the trap.
3. **Row-count assertion** (`assert len(df) == 178927`) was already present
   pre-existing at Step 9D and is unchanged/still active.
4. **P1's new columns are structurally carried through** — this pipeline
   only merges 2 external CSVs and drops a short, explicit list of
   intermediate/dead columns; it never touches columns it doesn't know
   about, so `IS_OBSERVABLE_COHORT`, `PERSON_KEY_AMBIGUOUS`,
   `IS_BEST_OBSERVABLE_RECORD` (or the earlier-named `PLE_MATCH_OUTCOME`,
   since superseded — see "Contract evolution" below) pass through
   automatically once present in `NMAT_Ultima.parquet`. Added an explicit,
   non-fatal diagnostic print block (Step 9F) that reports per-column
   presence, so a human running the script can see at a glance whether P1
   has landed yet.
5. **Output path renamed to `.bak`.** The old script wrote its ~118-column
   wide output straight to `dataset/NMAT_Exodus.parquet` — the same filename
   as the shipped, narrow, dashboard-facing file. That was Audit-01 Finding
   F2 exactly: "re-run the pipeline" silently overwrote the 54-col shipped
   file with a ~118-col one. Now writes `dataset/NMAT_Exodus.parquet.bak`
   (and `.csv.bak`), matching the naming convention `CLAUDE.md` already
   documents ("`NMAT_Exodus.parquet.bak` — Full 118-column backup"). This is
   the wide intermediate `5_Slim_Exodus.py` reads.

### Dry-run (scratch copy, current `NMAT_Ultima.parquet`, P1 not yet landed)

```
[1/10] Loaded 178,927 rows x 115 cols
[4/10] Unique raw nationalities: 129 -> 89 after normalization; 156 ambiguous
[5/10] RF matched: 32,501 / 178,927 (18.16%)
[6/10] Loaded 871 pseudo-citizenship records; 317 FOREIGN overrides
[8/10] Tier 1a (RF, known nationality): 32,345
       Tier 1b (RF, ambiguous -> 'Foreign (unspecified)'): 156
       Tier 2 (Likely Foreigner): 13
[9/10] CITIZENSHIP_FINAL top values match Audit-01 exactly (Filipino 146,413;
       India 26,491; ...; 'Foreign (unspecified)' 156)
       FOREIGNER_STATUS: Filipino 146,413 / Verified Foreigner 32,501 / Likely Foreigner 13
       Null checks passed (0 nulls); all 32,501 RF appnos correctly marked
       Row count preserved: 178,927
       Total columns: 122 (119 original + 3 new)
       P1 column 'IS_OBSERVABLE_COHORT': not yet landed
       P1 column 'PERSON_KEY_AMBIGUOUS': not yet landed
       P1 column 'PLE_MATCH_OUTCOME': not yet landed
[10/10] Saved dataset\NMAT_Exodus.parquet.bak (178,927 rows x 117 cols)
```

117 = 115 (current Ultima) + `CITIZENSHIP_FINAL` + `FOREIGNER_STATUS`
(`name_based_assessment` dropped, `RF_NATIONALITY`/`IN_REAL_FOREIGNERS`/
`override_applied`/`pseudo_citizenship` were always-intermediate and already
dropped by the pre-existing code). `FOREIGNER_STATUS`/`CITIZENSHIP_FINAL`
distributions match Audit-01's independently-replicated numbers exactly —
confirms this edit didn't disturb the tier logic, only the two things asked
for.

**Blocked on P1:** cannot yet verify that `IS_OBSERVABLE_COHORT`,
`PERSON_KEY_AMBIGUOUS`, `IS_BEST_OBSERVABLE_RECORD` actually survive into the
`.bak` from a *real* P1-fixed `NMAT_Ultima.parquet`, because that file
doesn't exist yet (current `NMAT_Ultima.parquet` is 115 cols, has none of
them). The pass-through mechanism itself only requires "don't drop what you
don't recognize," which I can prove structurally (see the diagnostic print
above correctly reporting their absence today) but not against real P1 data.

---

## Task 2 — `5_Slim_Exodus.py` (new)

Reads `dataset/NMAT_Exodus.parquet.bak`, selects/renames/coerces to the
contract's target schema, writes `dataset/NMAT_Exodus.parquet` + 2
dashboard-folder copies + `dataset/EXODUS_MANIFEST.json`.

### Contract evolution during this task (both ruled by the orchestrator, both actioned)

1. **Amendment 1** (mid-task): contract gained `IS_BEST_OBSERVABLE_RECORD`
   (3rd new column) and narrowed `PERSON_KEY_AMBIGUOUS` to SEX-contradiction
   only (6,148 keys, not SEX-or-university's 27,053). Target moved from
   52 to 53 in the amended contract text (54 − 4 + 3). Actioned directly —
   `P1_NEW_COLUMNS` list, `EXPECTED_BEST_OBSERVABLE`/`EXPECTED_AMBIGUOUS_KEYS`
   constants, and the corresponding hard/soft checks below all reflect this.
   Note `PLE_MATCH_OUTCOME` (named in the original P2 brief's coordination
   note) does not appear in either the original or amended contract's
   "Columns ADDED" list — treated as superseded by the contract, not carried
   into the target schema. Pipeline 4 still passes it through if P1 emits it
   (harmless), but Pipeline 5 does not select it (see `BASELINE_54` / target
   column selection — it's simply not in either list, so a select-based slim
   naturally excludes it, the same way it excludes the 60+ other Ultima
   working columns that were never part of the 54-col baseline).
2. **My own finding, escalated and resolved**: dropping
   `name_based_assessment` (Task 1) makes the true final width 52, not the
   amended contract's literal 54−4+3=53 arithmetic, because the contract's
   "Columns REMOVED" list (4 items) never named it. I documented this as an
   explicit, non-silent deviation in the first version of the script and
   flagged it here. **Orchestrator ruling: approved as contract-compliant.**
   `_TARGET_SCHEMA_CONTRACT.md` was updated to "54 − 5 removed + 3 added =
   52" — the docstring/manifest language was updated accordingly to describe
   52 as the target, not a deviation from it.
3. **Orchestrator ruling on assertion strictness** (after Task 2 was
   functionally complete): split all checks into two tiers instead of one
   uniform hard-fail list, because P1 is authorized to legitimately change
   headline counts (its disambiguator tie-break is moving off the circular
   `NMS_PER_num`) and a hard-`SystemExit` pipeline must not block a correct
   upstream fix over a stale reference number. Actioned — see "Two-tier
   assertions" below.

### Two-tier assertions (final structure)

**Tier A — structural, `check_hard`, raises `SystemExit`:** row count
178,927; post-rename column count preserved; one `IS_BEST_NMAT_RECORD` per
person; `IS_BEST_NMAT_RECORD.sum() == PERSON_KEY.nunique()`; one
`IS_BEST_OBSERVABLE_RECORD` per person within `Year<=2014`; naive
`IS_BEST_NMAT_RECORD & Year<=2014` filter is provably NOT equal to
`IS_BEST_OBSERVABLE_RECORD.sum()` (regression guard); `PERSON_KEY_AMBIGUOUS`
constant within each key; `IS_OBSERVABLE_COHORT == (Year<=2014)`;
`IS_OBSERVABLE_COHORT` not tautological with `IS_PLE_PASSER`;
`sum(RAW_8) == TotalRawScoreTRUE` (max abs diff < 1e-6); `IS_PLE_ANALYSIS_SAFE`
/ `NMA_College` / `name_based_assessment` absent; all 3 coerced columns are
real bool dtype; all 3 parquet copies share one md5.

**Tier B — reference counts, `check_soft`, prints `WARNING:` and records
into `EXODUS_MANIFEST.json["reference_count_deltas"]`, never raises:**
`PERSON_KEY.nunique()` (134,869), `IS_BEST_OBSERVABLE_RECORD.sum()` (69,503),
`PERSON_KEY_AMBIGUOUS` distinct-key count (6,148), `IS_PLE_PASSER.sum()`
(49,986), observable linkage rate (45.4-45.8%).

### Dry-run methodology (P1's 3 columns don't exist yet — proved in 3 steps)

**Step 1 — proves the fail-loud contract is honored.** Ran `5_Slim_Exodus.py`
against the real `.bak` from Task 1's dry-run (no P1 columns):

```
BLOCKED: P1 has not yet landed ['IS_OBSERVABLE_COHORT', 'PERSON_KEY_AMBIGUOUS',
'IS_BEST_OBSERVABLE_RECORD'] in NMAT_Ultima.parquet. 5_Slim_Exodus.py refuses
to fabricate a fallback for these columns -- per the P2 brief, fail loudly
rather than silently degrade. Re-run this script after P1's pipeline lands.
```
Exits cleanly, writes nothing. This is the expected/correct behavior today.

**Step 2 — proves the logic is right, using definitions transcribed
verbatim from the contract (not invented).** In a scratch script, computed
synthetic stand-ins for P1's 3 columns directly from the contract's own
formulas (`Year<=2014` for `IS_OBSERVABLE_COHORT`; SEX-contradiction-per-key
for `PERSON_KEY_AMBIGUOUS`; highest-`NMS_PER_num`→latest-`Year`→lowest-
`APPNO_CLEAN` computed *within* the `Year<=2014` subset for
`IS_BEST_OBSERVABLE_RECORD`) and confirmed they independently reproduce the
contract's stated reference numbers exactly:

```
ambiguous keys: 6148  (contract says 6,148)
best observable sum: 69503  (contract says 69,503)
```

This is strong evidence my reading of the contract's definitions is
correct, since I derived these numbers from the raw data + formula, not by
copying the contract's stated answer.

Ran `5_Slim_Exodus.py` against this synthetic `.bak` (real, still-broken
`IS_BEST_NMAT_RECORD` from the current unfixed `NMAT_Ultima.parquet` left
untouched):

```
[STRUCTURAL OK] len(df) == 178,927
[STRUCTURAL OK] len(df.columns) == 52 (post-rename width preserved)
[STRUCTURAL FAIL] groupby(PERSON_KEY).IS_BEST_NMAT_RECORD.sum() is 1 for every person
SystemExit: CONTRACT VIOLATION (structural): groupby(PERSON_KEY).IS_BEST_NMAT_RECORD.sum() is 1 for every person
```
Correctly and immediately catches the real, still-live O-2 bug (1,311
zero-flag people / 246 double-flagged) and refuses to ship — exactly the
"fail loudly" behavior required, and proof the check fires on real broken
data, not just in theory.

**Step 3 — full clean end-to-end run.** Additionally synthesized a
contract-rule-correct `IS_BEST_NMAT_RECORD` (same three-key sort, applied
to the whole dataset instead of just the observable window) purely to
exercise the rest of the pipeline once the one bug P1 owns is out of the
way:

```
[STRUCTURAL OK] len(df) == 178,927
[STRUCTURAL OK] len(df.columns) == 52 (post-rename width preserved)
[STRUCTURAL OK] groupby(PERSON_KEY).IS_BEST_NMAT_RECORD.sum() is 1 for every person
[STRUCTURAL OK] IS_BEST_NMAT_RECORD.sum() == PERSON_KEY.nunique() (flag count matches distinct persons)
[STRUCTURAL OK] groupby(PERSON_KEY).IS_BEST_OBSERVABLE_RECORD.sum() is 1 for every person in Year<=2014
[STRUCTURAL OK] naive filter (65,782) != IS_BEST_OBSERVABLE_RECORD.sum() (69,503) -- guards the RC bug returning
[STRUCTURAL OK] PERSON_KEY_AMBIGUOUS is constant within each PERSON_KEY
[STRUCTURAL OK] IS_OBSERVABLE_COHORT == (Year <= 2014) for all rows
[STRUCTURAL OK] IS_OBSERVABLE_COHORT is not a tautological copy of IS_PLE_PASSER
[STRUCTURAL OK] max |sum(RAW_8) - TotalRawScoreTRUE| < 1e-6 (actual 0.00e+00)
[STRUCTURAL OK] 'IS_PLE_ANALYSIS_SAFE' not in columns
[STRUCTURAL OK] 'NMA_College' not in columns
[STRUCTURAL OK] 'name_based_assessment' not in columns
[STRUCTURAL OK] HasCEMMatch/HasTRUErawScores/StoredVsDerivedMismatch dtype is bool-like
[REFERENCE OK] PERSON_KEY.nunique() (expected 134869, actual 134869)
[REFERENCE OK] IS_BEST_OBSERVABLE_RECORD.sum() (expected 69503, actual 69503)
[REFERENCE OK] PERSON_KEY_AMBIGUOUS distinct-key count (expected 6148, actual 6148)
[REFERENCE OK] observable linkage rate (expected [45.4%, 45.8%], actual 45.71%)
[STRUCTURAL OK] All 3 copies share one md5
```
Note the naive-filter number the pipeline computed independently on this
run, **65,782**, matches the contract's documented "wrong" reference value
exactly — further cross-confirmation the synthetic reconstruction is faithful.

Also deliberately forced a Tier-B mismatch (`EXPECTED_PLE_PASSERS = 12345`)
to prove the warn-only path doesn't block:
```
[REFERENCE WARNING] IS_PLE_PASSER.sum() (expected 12345, actual 49986)
WARNING: 'ple_passers' moved from the documented reference value. ...NOT blocking the chain.
```
Run still completed, wrote all 3 files, and `EXODUS_MANIFEST.json` recorded
`"reference_count_deltas": {"ple_passers": {"expected": 12345, "actual": 49986, "match": false}, ...}`
alongside the 4 other (matching) reference checks — confirmed by reading the
written JSON directly.

Final 52-column list (post-rename), read from the manifest of the clean run:
```
APPNO_CLEAN, PERSON_KEY, Year, SEX, UNDERGRAD_UNIVERSITY, UNDERGRAD_UNI_LOCATION,
UNDERGRAD_UNI_TYPE, UNDERGRAD_COURSE_GROUP, PercentileBin, NMS_PER_num, NMS_GPS,
NMS_APT, NMS_SA, NMS_VCss, NMS_IRss, NMS_Qss, NMS_PAss, NMS_BIOss, NMS_PHYss,
NMS_SSCss, NMS_CHEMss, TotalRawScoreTRUE, PartIRawScoreTRUE, PartIIRawScoreTRUE,
Raw_Verbal, Raw_InductiveReasoning, Raw_Quantitative, Raw_PerceptualAcuity,
Raw_Biology, Raw_Physics, Raw_SocialScience, Raw_Chemistry, StoredRawTotal,
StoredVsDerivedMismatch, CalculatedRawTotal_Source, HasTRUErawScores, HasCEMMatch,
APT_CEM, SA_CEM, GPS_CEM, Percentile_CEM, IS_BEST_NMAT_RECORD, IS_PLE_PASSER,
PLE_MATCH_METHOD, PLE_MATCH_CONFIDENCE, PLE_YEAR_PASSED, PLE_YEAR_GAP,
CITIZENSHIP_FINAL, FOREIGNER_STATUS, IS_OBSERVABLE_COHORT, PERSON_KEY_AMBIGUOUS,
IS_BEST_OBSERVABLE_RECORD
```

All scratch/synthetic files (`p4_dryrun/`, `*_synthetic*`, `*_TEST*`) were
deleted after verification; nothing under `dataset/` or `streamlit_dashboard/`
was modified by any dry-run.

**Still blocked on P1:** the real `IS_BEST_NMAT_RECORD` fix and the real
values of P1's 3 new columns. Everything above proves the *logic* is
correct against contract-derived synthetic data; the orchestrator's planned
final chain run will be the first time this script executes against real
P1 output.

---

## Task 3 — `tests/test_data_invariants.py` (new) + `tests/README.md` (new)

37 tests, plain `pytest` (v9.0.3, already present in `.venv`; added
`pytest>=7.0` to `requirements.txt` since it wasn't listed there before).
One module-scoped fixture loads `dataset/NMAT_Exodus.parquet` once. No other
fixtures/frameworks.

Covers: row/col/unique-person counts; removed columns absent / renamed
columns present / old names gone; 3 bool coercions; one best-record per
person (+ sum-matches-nunique); `IS_OBSERVABLE_COHORT` correctness and
non-tautology; `IS_BEST_OBSERVABLE_RECORD` correctness, one-per-person-in-
window, and non-equivalence to the naive filter; observable linkage rate
band; `PERSON_KEY_AMBIGUOUS` count and per-key constancy; **no two
bool-dtype columns are byte-identical** (general RC-1 guard, not just the
one known instance); raw-score arithmetic identities; B1-is-lowest-decile
monotonicity; `IS_PLE_PASSER` non-nested-metadata relationship; all-3-copies
share one md5; manifest md5/row/col match the file on disk.

### Run against the CURRENT (pre-fix) shipped file

```
.venv/Scripts/python.exe -m pytest tests/ -v
...
28 failed, 8 passed, 1 skipped in 3.55s
```

This is the correct and expected state today — the suite is written against
the *target* schema, and the current shipped `dataset/NMAT_Exodus.parquet`
is the old 54-col, pre-fix file. Notably:

- `test_no_duplicate_bool_columns` **failed with exactly the RC-1 evidence**:
  `AssertionError: byte-identical bool column pairs found (RC-1 class):
  [('IS_PLE_ANALYSIS_SAFE', 'IS_PLE_PASSER')]` — independent confirmation,
  from a test written without hard-coding that specific pair, that the test
  suite actually detects the root-cause bug class it exists to prevent, not
  just the one column name.
- `test_column_count` failed reporting the real current 54 columns (listed
  in full in the pytest output), confirming the fixture correctly loads the
  live file.
- The 8 passing tests (`test_row_count`, `test_unique_person_count`,
  `test_total_raw_score_equals_sum_of_components`,
  `test_part_i_plus_part_ii_equals_total`,
  `test_b1_is_lowest_decile_monotonic_raw_score`,
  `test_is_ple_passer_authoritative_count`,
  `test_ple_linkage_metadata_is_not_nested_with_passer_flag`,
  `test_dashboard_copies_are_byte_identical`) are exactly the invariants
  that were already true pre-fix per the orchestrator's own findings (row
  count, raw-score arithmetic, B1 ordering, the 49,986 passer count, the
  7,318/2,776 non-nesting, and the fact the 3 current parquet copies are
  already byte-identical per O-6) — so passing here is a correct positive
  control, not a bug in the tests.
- `test_manifest_md5_matches_canonical_file` was skipped: `EXODUS_MANIFEST.json`
  doesn't exist yet (it's written by `5_Slim_Exodus.py`, which hasn't run
  against real data).

**Expectation for the orchestrator's final chain run:** after
`4_Citizenship_Integration.py` → `5_Slim_Exodus.py` run against P1's
corrected `NMAT_Ultima.parquet`, `pytest tests/ -v` should go fully green
(37 passed, 0 skipped) except possibly the Tier-B-style reference-count
tests (`test_unique_person_count`, `IS_PLE_PASSER` count via
`test_is_ple_passer_authoritative_count`) if P1's disambiguator fix
legitimately moves those numbers — per the orchestrator's ruling on
`5_Slim_Exodus.py`, that would be expected and the constants at the top of
the test file should be updated to match, not the assertions removed.

---

## Summary of files touched

- `4_Citizenship_Integration.py` — edited (Tier-1b label, drop
  `name_based_assessment`, P1-column diagnostic prints, `.bak` output path)
- `5_Slim_Exodus.py` — new
- `tests/test_data_invariants.py` — new
- `tests/README.md` — new
- `requirements.txt` — added `pytest>=7.0`

## What remains blocked on P1

1. `NMAT_Ultima.parquet` still lacks `IS_OBSERVABLE_COHORT`,
   `PERSON_KEY_AMBIGUOUS`, `IS_BEST_OBSERVABLE_RECORD` — `5_Slim_Exodus.py`
   correctly refuses to run past column-selection without them (verified,
   Step 1 above).
2. `IS_BEST_NMAT_RECORD` is still the broken O-2/O-3 version in the current
   `NMAT_Ultima.parquet` — `5_Slim_Exodus.py` correctly hard-fails on it
   (verified, Step 2 above) rather than shipping a file that would fail its
   own invariant.
3. The orchestrator's planned final chain re-run
   (`4_Citizenship_Integration.py` → `5_Slim_Exodus.py` → `pytest tests/`)
   against P1's real corrected `NMAT_Ultima.parquet` has not happened yet —
   everything in this log up to that point is dry-run/synthetic
   verification of logic correctness, not a production run.
