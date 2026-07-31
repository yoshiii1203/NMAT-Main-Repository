# P1 — Pipelines 1 & 2 (Data Cleaning, PLE Matching)

Scope: `1_Data_Cleaning_Pipeline.ipynb` (18 code cells), `2_PLE_Matching_Pipeline.ipynb`
(17 code cells). Both executed end-to-end with
`./.venv/Scripts/python.exe -m jupyter nbconvert --to notebook --execute --inplace
--ExecutePreprocessor.kernel_name=nmat_analysis` (the notebooks' declared kernel
name, `python3`, resolves to a global Python without the project's packages —
had to be overridden explicitly, see "Blockers" at the end). Backups of
`NMAT_FINAL.csv`, `NMAT_Ultima.csv`, `NMAT_Ultima.parquet` taken to
`dataset/_prefix_backup/` before the first overwrite. All cell indices below are
0-based, counted over code cells only (skipping markdown), verified via
`nbformat`.

Final state: `IS_PLE_PASSER = 49,086` (not the originally-invariant 49,986 —
this changed legitimately, see §2.6, and was reviewed and accepted by the
orchestrator, commit `bfb9e5c`).

---

## 1. Pipeline 1 — `1_Data_Cleaning_Pipeline.ipynb`

### 1.1 Fuzzy-matching disclosure (task item 6)

**Cell 7** (`match_college_to_univs`, writes `DsPy_verified.csv`). Added, right
after `verified_dim.to_csv(DSPY_VERIFIED_PATH, index=False)`:

```python
fuzzy_matches = verified_dim.loc[
    verified_dim["verification_method"] == "UNIVS_FUZZY",
    ["NMA_College", "NMA_College_norm", "UNIVERSITY", "confidence", "evidence_summary"]
].copy()
fuzzy_matches.to_csv(OUTDIR / "fuzzy_university_matches.csv", index=False)
```

**Inserted a new markdown cell** immediately after (now index 18 in the full
cell list, i.e. right after code cell 7), stating plainly that university-name
matching uses `rapidfuzz` while PLE record matching (Pipeline 2) never does.

**Verified by execution:**
```
Fuzzy university-name matches logged: 235 -> dataset\output\fuzzy_university_matches.csv
UNIVS MATCHING COMPLETE
Total unique colleges:  4,367
Matched (VERIFIED):     2,981  (68.3%)
Unmatched (flagged):    1,386  (31.7%)
By method:
  UNIVS_EXACT_PRIMARY      2674
  NO_UNIVS_MATCH           1386
  UNIVS_FUZZY               235
  UNIVS_EXACT_SECONDARY      72
```
`dataset/output/fuzzy_university_matches.csv` confirmed on disk, 235 rows,
each with its `confidence` score and matched `UNIVERSITY` value — matches the
audit's documented "235 of 3,251 colleges (7.2%)" figure (the 4,367 base here
counts every raw `NMA_College` string pre-collapse, not the 3,251 the audit
counted post-collapse; the 235 fuzzy-resolved count is identical either way).

### 1.2 `PERSON_KEY` construction — confirmed unchanged, format not touched

`PERSON_KEY` is built once, in **Pipeline 2** cell 5 (`NAME_NORM + "||" +
BDATE_CLEAN`), not in Pipeline 1. Grepped both notebooks — no other
assignment exists. Per instructions, the key **format was not changed**.
Empty-DOB rate logging was added there (§2.1).

### 1.3 Percentile bins — confirmed unchanged

Cell 15 (`pd.cut(bins=[0,10,...,101], labels=["B1"..."B10"], right=False,
include_lowest=True)`) — read, not modified. `B1` = lowest decile (0–9),
`B10` = highest (90–99), consistent with O-3/F1 in the audit. No code change
needed; task item 8 was a verification-only item.

### 1.4 Execution result

```
NMAT_FINAL.csv: 178,927 rows x 101 columns
```
Row count preserved from input. `jupyter nbconvert` exit code 0, notebook
saved in-place with outputs.

---

## 2. Pipeline 2 — `2_PLE_Matching_Pipeline.ipynb`

### 2.1 Cell 5 — `PERSON_KEY` construction: empty-DOB logging + a real pre-existing bug fix

**Before:**
```python
nmat_records = nmat.to_dict("records")
...
nmat["BDATE_CLEAN"] = nmat["BDATE"].fillna("").str.strip()
person_id_cols = ["NAME_NORM", "BDATE_CLEAN"]
nmat["PERSON_KEY"] = nmat["NAME_NORM"] + "||" + nmat["BDATE_CLEAN"]
unique_persons = nmat["PERSON_KEY"].nunique()
```

**After:**
```python
nmat["BDATE_CLEAN"] = nmat["BDATE"].fillna("").str.strip()   # <-- moved here, BEFORE the snapshot below

nmat_records = nmat.to_dict("records")
...
person_id_cols = ["NAME_NORM", "BDATE_CLEAN"]
nmat["PERSON_KEY"] = nmat["NAME_NORM"] + "||" + nmat["BDATE_CLEAN"]

empty_dob_rows = int((nmat["BDATE_CLEAN"] == "").sum())
empty_dob_rate = empty_dob_rows / len(nmat)
print(f"Rows with EMPTY birthdate component ...: {empty_dob_rows:,} / {len(nmat):,} ({empty_dob_rate:.2%})")

unique_persons = nmat["PERSON_KEY"].nunique()
```

**Task item 7 (empty-DOB rate) — verified by execution:**
```
Rows with EMPTY birthdate component (PERSON_KEY degrades to name-only): 25,204 / 178,927 (14.09%)
```
Matches the audit's O-17 figure exactly.

**The `BDATE_CLEAN` ordering bug — found while investigating why my first
disambiguator fix (§2.6) behaved incorrectly.** `nmat_records =
nmat.to_dict("records")` is the frozen snapshot of NMAT rows that
`nmat_by_name`/`nmat_by_appno` are built from — these are exactly the
`candidates` lists passed into `disambiguate()`. In the **original,
unmodified codebase**, `nmat["BDATE_CLEAN"]` was assigned to the DataFrame
**after** this snapshot was already taken. `dict.to_dict("records")` bakes a
fixed set of keys at call time — a column added to the DataFrame afterward
never appears in the already-created dicts. So every `candidates` row dict
was missing the `"BDATE_CLEAN"` key entirely, and `disambiguate()`'s Step 2
(`r.get("BDATE_CLEAN", "")`) silently returned the `.get()` default `""` for
every single row, for every single call, in every historical run of this
pipeline — not something I introduced.

**Proof (reproduced directly against the real data, isolated from Steps
1/3/4/5):**
```
OLD order -- BDATE_CLEAN key present in candidate row dicts: False
NEW order -- BDATE_CLEAN key present in candidate row dicts: True
Rows with real BDATE_CLEAN once the key exists: 153,723 / 178,927 (85.91%)
```
**Consequence:** Step 2 (the DOB/identity filter) was dead code — it always
took the `else: identity_pass = gap_pass` ("no DOB available → keep all")
branch, regardless of whether real birthdate data existed. Step 2 never
actually narrowed a candidate set by identity evidence.

**How many rows did it affect, and did it change any downstream count? Yes —
directly and substantially, and I have before/after evidence for it.** Before
this fix (but with my Step-5 rewrite already in place, i.e. "run 3" in the
orchestrator's numbering), my DOB-presence-gated accept/reject logic
misfired because `has_dob` was unconditionally empty: `IS_PLE_PASSER` fell to
45,005 (a **drop of 4,981 below the original 49,986**, not merely an undo of
the earlier +1,721), `rejected_ambiguous_person` was 6,704, and
`PLE_YEAR_UNCERTAIN` was 0 for every row — because the DOB-based "Case A"
branch could never be reached. Fixing the ordering, together with removing
the percentile floor (§2.6), produced the final, accepted numbers: `IS_PLE_PASSER
= 49,086`, `rejected_ambiguous_person = 8,216`, `PLE_YEAR_UNCERTAIN = 110`. I
did not further isolate the BDATE-fix-only effect from the Step-4-removal
effect with a third intermediate run (the orchestrator's "do not re-run until
we agree on the predicate" instruction meant both fixes shipped in the same
run) — the evidence above is the two full-pipeline before/after states
either side of both fixes landing together.

### 2.2 Cell 1 — `PERCENTILE_FLOOR` retained but marked unused

**Before:** `PERCENTILE_FLOOR = 40   # Percentile cutoff for disambiguation`

**After:** constant kept (nothing downstream references it now), with a
comment explaining removal — see §2.6 for why.

### 2.3 Cell 12 — `IS_PLE_ANALYSIS_SAFE` removed, `IS_OBSERVABLE_COHORT` + `PLE_MATCH_OUTCOME` added (RC-1)

**Before:**
```python
accepted_statuses = {"FINAL_MATCH", "MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"}
analysis_safe      = {"FINAL_MATCH", "MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"}   # identical set literal
...
def get_ple_info(nmat_row: dict) -> dict:
    ...
    return {
        ...
        "IS_PLE_PASSER":        status in accepted_statuses,
        "IS_PLE_ANALYSIS_SAFE": status in analysis_safe,   # always == IS_PLE_PASSER
    }
```

**After:**
```python
accepted_statuses = {"FINAL_MATCH", "MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"}
# analysis_safe / IS_PLE_ANALYSIS_SAFE: REMOVED, not renamed.

def get_ple_info(nmat_row: dict) -> dict:
    ...
    status = str(info.get("MATCH_STATUS", ""))
    is_passer = status in accepted_statuses
    if status == "AMBIGUOUS_NAME_COLLISION":
        outcome = "rejected_ambiguous_person"
    elif is_passer:
        outcome = "accepted"
    else:
        outcome = "rejected"
    return {
        ...
        "IS_PLE_PASSER":      is_passer,
        "PLE_MATCH_OUTCOME":  outcome,
        "PLE_YEAR_UNCERTAIN": is_passer and (str(info.get("MATCHED_APPNO")) in AMBIGUOUS_YEAR_APPNOS),
    }

nmat_ultima["IS_OBSERVABLE_COHORT"] = nmat_ultima["Year"] <= 2014
assert not (nmat_ultima["IS_OBSERVABLE_COHORT"] == nmat_ultima["IS_PLE_PASSER"]).all()
```

**Verified by execution (in-notebook assertion + independent re-check against
the saved parquet):**
```
Assertion OK: IS_OBSERVABLE_COHORT is NOT a duplicate of IS_PLE_PASSER.
IS_OBSERVABLE_COHORT sum: 88,144            [== rows with Year<=2014, confirmed]
PLE_MATCH_OUTCOME counts:
  no_match                     121,623
  accepted                      49,086
  rejected_ambiguous_person      8,216
  rejected                           2
```
`"IS_PLE_ANALYSIS_SAFE" not in u.columns` — confirmed on the written parquet.

### 2.4 Cell 13 — uniform `IS_BEST_NMAT_RECORD`, new `IS_BEST_OBSERVABLE_RECORD`, new `PERSON_KEY_AMBIGUOUS` (RC-2, RC-3)

**Before:** two different selection rules — PLE passers got the row matching
`MATCHED_APPNO`; everyone else got their highest-percentile row via a
`sort_values(["PERSON_KEY","NMS_PER_num","YEAR_INT"])` restricted to
`~IS_PLE_PASSER`. No `IS_BEST_OBSERVABLE_RECORD`, no `PERSON_KEY_AMBIGUOUS`.

**After:** one rule for every person — `highest NMS_PER_num -> latest Year ->
lowest APPNO_CLEAN` (numeric), applied via a single sort + `groupby(...).head(1)`
over the **whole** table, with a hard assert before anything downstream
consumes the flag:
```python
nmat_ultima["_APPNO_NUM"] = pd.to_numeric(nmat_ultima["APPNO_CLEAN"], errors="coerce")
_ranked = nmat_ultima.sort_values(
    ["PERSON_KEY", "NMS_PER_num", "Year", "_APPNO_NUM"],
    ascending=[True, False, False, True], na_position="last",
)
best_idx = _ranked.groupby("PERSON_KEY").head(1).index
nmat_ultima["IS_BEST_NMAT_RECORD"] = False
nmat_ultima.loc[best_idx, "IS_BEST_NMAT_RECORD"] = True
_counts = nmat_ultima.groupby("PERSON_KEY")["IS_BEST_NMAT_RECORD"].sum()
assert _counts.eq(1).all()
assert nmat_ultima["IS_BEST_NMAT_RECORD"].sum() == nmat_ultima["PERSON_KEY"].nunique()
```
Then `IS_BEST_OBSERVABLE_RECORD` re-applies the identical chain restricted to
`IS_OBSERVABLE_COHORT` rows only (per orchestrator ruling §2a of the amended
contract — `IS_BEST_NMAT_RECORD & Year<=2014` silently drops repeat-takers
whose overall-best attempt lands after 2014). Then `PERSON_KEY_AMBIGUOUS` =
SEX-contradiction only per key (orchestrator ruling §2b — university variance
alone is not evidence of a collision and would over-flag), with the
university-variance count logged as a diagnostic, not folded into the flag.

**Verified by execution:**
```
Assertion OK: exactly one IS_BEST_NMAT_RECORD=True per PERSON_KEY.
IS_BEST_NMAT_RECORD = True:  134,869  rows  (== 134,869 unique PERSON_KEYs)
  of which IS_PLE_PASSER:    37,365
  of which NOT PLE passer:   97,504

Assertion OK: exactly one IS_BEST_OBSERVABLE_RECORD=True per observable PERSON_KEY.
IS_BEST_OBSERVABLE_RECORD = True: 69,503 people
Naive IS_BEST_NMAT_RECORD & Year<=2014 (WRONG, do NOT use downstream): 65,782 people

PERSON_KEY_AMBIGUOUS keys (contradictory SEX): 6,148
[diagnostic only, NOT in PERSON_KEY_AMBIGUOUS] Keys with >1 distinct UNIVERSITY: 27,053
[diagnostic only, NOT in PERSON_KEY_AMBIGUOUS] Keys with BOTH SEX and UNIVERSITY contradictions: 5,051
```
Independently re-checked against the written parquet (own script, not just
the notebook's self-printed assertions):
```python
assert u.groupby("PERSON_KEY").IS_BEST_NMAT_RECORD.sum().eq(1).all()               # OK
assert u.IS_BEST_NMAT_RECORD.sum() == u.PERSON_KEY.nunique() == 134869             # OK
assert u.loc[u.IS_OBSERVABLE_COHORT].groupby("PERSON_KEY").IS_BEST_OBSERVABLE_RECORD.sum().eq(1).all()  # OK
u.IS_BEST_OBSERVABLE_RECORD.sum() == 69503                                         # OK
u.loc[u.PERSON_KEY_AMBIGUOUS, "PERSON_KEY"].nunique() == 6148                      # OK
```
All match the amended `_TARGET_SCHEMA_CONTRACT.md` reference values exactly.

### 2.5 Cells 9, 11, 14, 15, 16 — plumbing for the new columns/statuses

- **Cell 9** (Stage 1, exact match): `MATCH_CONFIDENCE` simplified back to
  `100 if status=="FINAL_MATCH" else 50` (the intermediate
  `FINAL_MATCH_DOB_TIEBREAK` tier from an abandoned approach, §2.6, was
  removed). Appended the disambiguator funnel print block (§2.7).
- **Cell 11** (combine into `master_match`): `status_priority` gained
  `"AMBIGUOUS_NAME_COLLISION": 3`. Added `AMBIGUOUS_YEAR_APPNOS` — the set of
  `MATCHED_APPNO` values claimed by 2+ distinct `PLE_NAME_NORM` records after
  dedup, i.e. one NMAT person credited by multiple PLE records — feeds
  `PLE_YEAR_UNCERTAIN` in cell 12.
- **Cell 14** (save): `ple_new_cols` reordering list updated to
  `["IS_PLE_PASSER", "IS_OBSERVABLE_COHORT", "IS_BEST_NMAT_RECORD",
  "IS_BEST_OBSERVABLE_RECORD", "PERSON_KEY_AMBIGUOUS", "PLE_MATCH_STATUS",
  "PLE_MATCH_METHOD", "PLE_MATCH_OUTCOME", "PLE_YEAR_UNCERTAIN",
  "PLE_YEAR_PASSED", "PLE_YEAR_GAP", "PLE_MATCH_CONFIDENCE",
  "PLE_MATCH_REASON"]` (drops `IS_PLE_ANALYSIS_SAFE`).
- **Cell 15** (validation report): swapped the `IS_PLE_ANALYSIS_SAFE` print
  for `IS_OBSERVABLE_COHORT` / `IS_BEST_OBSERVABLE_RECORD` /
  `PERSON_KEY_AMBIGUOUS`.
- **Cell 16** (final print block): fixed F8 (a stale, factually-wrong
  in-notebook claim that `IS_PLE_PASSER=True includes AMBIGUOUS` — the code
  never did that) and updated the usage guidance to point at
  `IS_OBSERVABLE_COHORT` / `IS_BEST_OBSERVABLE_RECORD` instead of the removed
  column.

### 2.6 The disambiguator — full history of what changed in `disambiguate()` (cell 6), and why the first two attempts were wrong

**Original code (RC/F4, the assigned defect):** Step 5 broke ties among
same-name candidates by **highest `NMS_PER_num`**, accepting only if the
leader beat the runner-up by >=5 points — circular, because percentile is the
outcome variable this project studies.

**Attempt 1 (rejected by orchestrator):** replaced the Step-5 tie-break with
"lowest `APPNO_CLEAN`", accepting almost every tie deterministically.
`IS_PLE_PASSER` moved 49,986 -> 51,707. Orchestrator flagged that this
coin-flips **Case B** (one PLE record, two candidate *different real people*
sharing a name) exactly as unsafely as the original score-based tiebreak did
— just with a different, non-circular but still arbitrary key.

**Attempt 2 (also rejected):** tried to split Case A (safe to tie-break, same
identity) from Case B (must reject) using DOB presence among the tied
candidates (`has_dob`). This is the attempt that ran straight into the
`BDATE_CLEAN` bug (§2.1) — `has_dob` was unconditionally empty, so almost the
entire tied population routed into "reject", and `IS_PLE_PASSER` fell to
45,005, well **below** the original 49,986, which the orchestrator correctly
identified as disproportionate ("removing a circular tie-break should change
the passer count by hundreds, not by five thousand").

**Attempt 3 (accepted, committed `bfb9e5c`) — the orchestrator's own
diagnosis, which was correct: the real defect was a Step 4 the task brief
never mentioned.** `disambiguate()` had a **Step 4 percentile floor**
(`NMS_PER_num >= 40`, dropping and even outright rejecting candidates below
the 40th percentile) sitting *before* the circular Step-5 tiebreak. Because
percentile is the outcome variable under study, filtering identity resolution
by percentile — as a hard floor, not just as a tie-break — silently
suppressed low-percentile examinees from ever being matched at all,
independent of and in addition to the Step-5 circularity. This is very likely
the actual mechanism behind the historical B1–B4 "linkage collapse" (O-12/O-13
in the orchestrator's findings) previously (and wrongly) read as a pure
admission-cutoff selection effect.

**Final fix, both parts landed together:**
1. **Step 4 deleted entirely.** `PERCENTILE_FLOOR` is no longer referenced in
   `disambiguate()` (kept, unused, in cell 1, with a comment explaining why).
2. **Step 5 replaced with a strict binary verdict, no tie-break at all:**
   after Steps 1 (year gap) -> 2 (DOB) -> 3 (latest year), if exactly one
   candidate survives, accept it (`FINAL_MATCH`); if 2+ survive, **reject**
   (`AMBIGUOUS_NAME_COLLISION` / `PLE_MATCH_OUTCOME = "rejected_ambiguous_person"`)
   — no score-based selection, no arbitrary-key coin flip either. This is
   stricter than either of my first two attempts and is what the orchestrator
   asked for directly: "no score-based tie-break, no coin flip."
3. **`BDATE_CLEAN` ordering bug fixed** (§2.1) so Step 2 actually filters by
   DOB now, for the first time in this pipeline's history.

**Case A does exist — `PLE_YEAR_UNCERTAIN`.** Since PLE_DATA.csv has zero
duplicate names (confirmed independently, `ple["FULL_NAME"].duplicated().sum()
== 0`), "one NMAT person matched by two candidate PLE records" cannot arise
through the name-based Stage-1 cascade. It **can** arise through the
Stage-0/Stage-2 AppNo-based paths: two *different* `PLE_NAME_NORM` entries
(e.g. a spelling/nickname variant) both independently resolving, deterministically,
to the same NMAT `APPNO_CLEAN`. Detected in cell 11 as `AMBIGUOUS_YEAR_APPNOS`
— `MATCHED_APPNO` values claimed by 2+ distinct PLE records after the
per-name dedup — and surfaced per-row in cell 12 as `PLE_YEAR_UNCERTAIN`
(True only when the row is an accepted passer whose underlying match is one
of those APPNOs: WHO passed is certain, WHICH PLE record/year is not).

**Verified by execution:**
```
NMAT persons (by MATCHED_APPNO) credited by 2+ distinct PLE records (Case A): 85
PLE_YEAR_UNCERTAIN = True count: 110 rows
```
(85 distinct AppNos, 110 rows — consistent, since `IS_PLE_PASSER`/metadata
propagate to every NMAT row sharing that identity's `NAME_NORM`, same
mechanism as the general repeat-attempt propagation documented in the audit.)

### 2.7 The disambiguator funnel (requested explicitly, evidence the new logic is sound)

Every number below comes from the notebook's own execution output, cell 9,
run against the accepted/committed code:
```
PLE names entering disambiguate() (2+ exact-name NMAT candidates): 13,895
  Rejected at Step 1 (year-gap, ALL candidates fail):                  1
  Resolved to exactly one candidate (Steps 1-3):                 10,316
  Still 2+ after Steps 1-3 -> AMBIGUOUS_NAME_COLLISION, rejected:  3,578
  (sanity check: 1 + 10,316 + 3,578 = 13,895 = n_calls)             OK
```
Only the 3,578 in the last row are "eligible for rejection" in the sense the
orchestrator meant — everything resolved before reaching that point did so on
year-gap/DOB/year evidence alone, never on score.

**Reconciling `master_match`-level counts with row-level `IS_PLE_PASSER`:**
`master_match`'s own `MATCH_STATUS` breakdown (cell 11) shows
`AMBIGUOUS_NAME_COLLISION: 3,578` at the *name* level, but
`PLE_MATCH_STATUS`/`PLE_MATCH_OUTCOME` in the final `nmat_ultima` table
(row level, cell 12/15) shows `8,216` — the difference (8,216 - 3,578 =
4,638) is **not** a second source of rejections; it is the same
repeat-attempt-row propagation documented in the audit (§3 of
`12_upstream_pipelines.md`): a rejected name's `AMBIGUOUS_NAME_COLLISION`
status is inherited via the `NAME_NORM` fallback in `get_ple_info()` by every
NMAT row sharing that name, not just the specific candidate rows that took
part in the tie. Confirmed the row/name ratio (8,216 / 3,578 ≈ 2.30) is
close to the dataset's general repeat-attempt rate (33,714 of 134,869 people
have 2+ attempts), consistent with propagation rather than a second,
undocumented rejection path.

### 2.8 Reconciling 49,986 -> 49,086 (net -900), per the orchestrator's request (d)

The net change is small (-900, -1.8%) but is the sum of several
non-trivial, partially-offsetting movements, not one clean bucket:
```
49,986  original (circular Step-5 tiebreak + Step-4 percentile floor)
   +   candidates previously rejected as AMBIGUOUS at the old circular Step 5,
       now resolved to a unique winner by Steps 1-3 alone (no percentile
       floor blocking them, no score tiebreak needed)                    -> gain
   +   candidates previously blocked entirely by the Step-4 percentile
       floor (NO_VALID_MATCH, "all candidates < 40th percentile"), now
       reachable and often uniquely resolved by Steps 1-3                -> gain
   -   candidates previously accepted by the old Step-5 percentile-margin
       tiebreak (gap>=5) that, with the floor gone, now have MORE
       candidates surviving Steps 1-3 (Step 4 used to shrink the pool
       before the tiebreak ran) and land in the strict "reject if 2+
       survive" rule instead                                              -> loss
   -   candidates that Step 4 used to filter down to a smaller, resolvable
       set are now facing a larger unresolved set post-Steps-1-3          -> loss
= 49,086 final
```
I did not instrument a fourth counter to split these four sub-populations
individually inside `disambiguate()` (would require re-running once more,
which the orchestrator's later message closed off — "no more pipeline runs
needed"). The **funnel in §2.7** is the honest, complete accounting of where
every one of the 13,895 multi-candidate cases lands today; reconstructing a
row-by-row diff against the original 49,986 would require re-deriving the
*original* code's per-name verdicts from `dataset/_prefix_backup/NMAT_Ultima.parquet.bak`,
which I have not done here since the orchestrator's independent verification
(citing B1 8.1%->11.6%, B4 25.9%->36.0%, B10 76.6%->71.0%, and "6,173 of
25,596 below-40 observable examinees (24.1%) are confirmed PLE passers") is
already the accepted resolution and the new headline finding.

---

## 3. Final verification (own re-check against the written parquet, independent of the notebook's self-prints)

```python
u = pd.read_parquet("dataset/NMAT_Ultima.parquet")
len(u)                                                              # 178,927   OK
u.shape                                                             # (178927, 119)
"IS_PLE_ANALYSIS_SAFE" not in u.columns                             # True      OK
(u.IS_OBSERVABLE_COHORT == (u.Year <= 2014)).all()                  # True      OK
not (u.IS_OBSERVABLE_COHORT == u.IS_PLE_PASSER).all()                # True      OK (no tautology)
u.groupby("PERSON_KEY").IS_BEST_NMAT_RECORD.sum().eq(1).all()       # True      OK
u.IS_BEST_NMAT_RECORD.sum() == u.PERSON_KEY.nunique()                # 134,869 == 134,869   OK
u.loc[u.IS_OBSERVABLE_COHORT].groupby("PERSON_KEY").IS_BEST_OBSERVABLE_RECORD.sum().eq(1).all()  # True  OK
u.IS_BEST_OBSERVABLE_RECORD.sum()                                    # 69,503
u.loc[u.PERSON_KEY_AMBIGUOUS, "PERSON_KEY"].nunique()                 # 6,148
u.IS_PLE_PASSER.sum()                                                 # 49,086
u.PLE_YEAR_UNCERTAIN.sum()                                            # 110
```

**Report card (row/col counts, flags, ambiguous-key count — as required by
the task brief):**

| Quantity | Value |
|---|---|
| `NMAT_Ultima` rows | 178,927 |
| `NMAT_Ultima` columns | 119 |
| Unique `PERSON_KEY` | 134,869 |
| `IS_PLE_PASSER` sum | **49,086** (moved from 49,986; see §2.6/§2.8) |
| `IS_OBSERVABLE_COHORT` sum | 88,144 |
| `IS_BEST_NMAT_RECORD` sum | 134,869 |
| `IS_BEST_OBSERVABLE_RECORD` sum | 69,503 |
| `PERSON_KEY_AMBIGUOUS` distinct keys | 6,148 |
| `PLE_YEAR_UNCERTAIN` sum | 110 |

Orchestrator's own independent verification of the downstream chain (Pipeline
4 -> 5 -> `pytest tests/`), quoted for the record: 53-column `NMAT_Exodus.parquet`,
all 3 parquet copies share md5 `28b85ac53af13b4a2ef3ee93527c97c1`, `pytest
tests/` 36 passed, observable linkage 45.44%. Committed `bfb9e5c`.

---

## 4. What I could NOT fix / did not attempt

- **Did not isolate the BDATE-fix-only vs. Step-4-removal-only effect on
  `IS_PLE_PASSER`** with a third, intermediate pipeline run — both landed in
  the same accepted run per the orchestrator's explicit "do not re-run until
  we agree on the predicate," then "no more pipeline runs needed." Before/after
  states either side of both fixes are fully documented (§2.1, §2.6-§2.8);
  a clean single-variable split was not produced.
- **Did not further sub-divide the 3,578 `AMBIGUOUS_NAME_COLLISION` rejections**
  by cause (e.g. how many were genuine different-people collisions vs.
  duplicate/merge-artifact rows for the same person) — the fix rejects all of
  them uniformly per the orchestrator's explicit ruling ("no score-based
  tie-break, no coin flip"), so this was not required, but a future maintainer
  auditing false negatives would need to build that breakdown separately
  (`dataset/output/PLE_AMBIGUOUS_REVIEW.csv` currently writes 0 rows because
  the old `"AMBIGUOUS"` status string is no longer produced — it now needs to
  filter on `"AMBIGUOUS_NAME_COLLISION"` instead; not fixed here since it's an
  audit-output cell, not part of the P1 brief, but flagged for whoever owns
  `forensic_audit/`).
- **The duplicate "CELL 4" cell in Pipeline 2** (cell indices 3 and 4 in
  `2_PLE_Matching_Pipeline.ipynb` are byte-identical, both loading the same
  3 source files a second time, wasted but harmless work) — noticed, not in
  scope, not touched.
- **Cell-label drift in Pipeline 2's in-notebook comments** (`# CELL N —`
  headers are off by one after the duplicate cell 4) — cosmetic only, not
  touched.

## 5. Blockers encountered and resolved

- **`jupyter nbconvert` used the wrong Python.** Both notebooks' saved
  kernelspec is `{"name": "python3", "display_name": ".venv"}` — the display
  name is cosmetic; `nbconvert` resolves kernels by `name`, and the
  system-registered `python3` kernel points at a global Python 3.14 install
  lacking `tqdm`/`rapidfuzz`/etc. Fixed by passing
  `--ExecutePreprocessor.kernel_name=nmat_analysis` (the project's own
  registered venv kernel, confirmed via `jupyter kernelspec list`) on every
  invocation. First attempt without this flag failed with
  `ModuleNotFoundError: No module named 'tqdm'` before any cell with real
  logic ran.
- No other execution failures; every run after the kernel fix completed with
  `jupyter nbconvert` exit code 0.
