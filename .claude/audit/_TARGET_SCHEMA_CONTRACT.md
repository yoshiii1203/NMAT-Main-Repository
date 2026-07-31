# TARGET SCHEMA CONTRACT v2 — binding on every agent

This is the **authoritative specification** of `NMAT_Exodus.parquet` after remediation.
Every agent codes against THIS, not against the current parquet. Do not deviate; if you believe a
change is needed, report it to the orchestrator rather than diverging silently.

Baseline (pre-fix): 178,927 rows x 54 cols.
**Target: 178,927 rows x 51 cols.** (54 − 6 removed + 3 added)

> **ORCHESTRATOR RULING — `HasCEMMatch` is dropped (6th removal).** Found by
> `tests/test_data_invariants.py::test_no_duplicate_bool_columns`, **not by the original audit**:
> `HasCEMMatch` is byte-identical to `HasTRUErawScores` (both 178,882 True). They encode one
> condition — TRUE raw scores exist precisely when a CEM record matched. Keeping
> `HasTRUErawScores` (32 references vs 13; clearer name for the data-integrity narrative).
> Two identical columns is the RC-1 trap; collapse to one. **Consumers referencing `HasCEMMatch`
> must switch to `HasTRUErawScores`.** Final width: **51**.

> **ORCHESTRATOR RULING — `name_based_assessment` is dropped (5th removal).** P2 correctly flagged
> this as a deviation rather than diverging silently. Approved: the column is non-null for only
> 871 of 178,927 rows (0.5%), is never consulted by the tier-decision logic, and **contradicts the
> final citizenship label in 23 of those 871 rows**. A column that looks like corroborating evidence
> but influences nothing is precisely the trap that produced this audit. Final width: **52**.

---

## 1. Columns REMOVED (4)

| Column | Why |
|---|---|
| `IS_PLE_ANALYSIS_SAFE` | Byte-identical duplicate of `IS_PLE_PASSER`; documented as Year<=2014 but is not. Root cause RC-1. Replaced by `IS_OBSERVABLE_COHORT`. |
| `NMA_College` | Redundant duplicate of `UNIVERSITY` (identical once case/punctuation normalised) with different cardinality (3,251 vs 2,907) — a grouping hazard. |
| `AllRawComponentsPresent` | Constant (nunique = 1). Zero information. |
| `CalcVsDerivedMismatch` | Constant (nunique = 1). Zero information. |
| `name_based_assessment` | Non-null for 871/178,927 rows (0.5%); never used in the tier decision; contradicts the final label in 23 of 871. Looks like evidence, influences nothing. |

## 2b. Provenance columns carried through when present (optional, +1 or +2)

| Column | Type | Meaning |
|---|---|---|
| `PLE_MATCH_OUTCOME` | `str` | `accepted` / `rejected` / `rejected_ambiguous_person` / `no_match`. Lets the dashboards state **why** a candidate match was not counted, instead of silently showing a smaller passer count. |
| `PLE_YEAR_UNCERTAIN` | `bool` | Accepted passer whose PLE *year* could not be disambiguated (one person, two candidate passer records). Passer status is certain; the year is not. |

Final shipped width is therefore **52** (with `PLE_MATCH_OUTCOME`) or **53** (once
`PLE_YEAR_UNCERTAIN` lands from P1's disambiguator rework). Both are contract-valid;
`5_Slim_Exodus.py` carries them through when present and logs a NOTE when absent.

## 2. Columns ADDED (3)

| Column | Type | Definition |
|---|---|---|
| `IS_OBSERVABLE_COHORT` | `bool` | `Year <= 2014`. The genuine observable cohort — allows >=5 years for PLE passage. **This is the only legitimate cohort filter for PLE-linked analysis.** |
| `PERSON_KEY_AMBIGUOUS` | `bool` | `True` where the `PERSON_KEY` has **contradictory `SEX`** across its rows. **6,148 keys.** Exposes RC-3 rather than hiding it. |
| `IS_BEST_OBSERVABLE_RECORD` | `bool` | The person's best attempt **among rows with `Year <= 2014`** — see §2a. **69,503 True.** |

### §2a — Why `IS_BEST_OBSERVABLE_RECORD` is a separate flag (ORCHESTRATOR RULING)

`IS_BEST_NMAT_RECORD & (Year <= 2014)` is **not** the observable cohort. A person who sat in 2013 and
again in 2016 has their 2016 attempt selected as overall-best, so the naive filter silently drops
them — losing **3,721 people** and inflating the linkage rate.

| Definition | People | Linkage rate |
|---|---|---|
| `IS_BEST_NMAT_RECORD & Year<=2014` (naive, **wrong**) | 65,782 | 46.69% |
| `IS_BEST_OBSERVABLE_RECORD` (best attempt *within* the window, **correct**) | **69,503** | **45.71%** |

The correct flag also uses only information available by 2014, which is what an "observable cohort"
means. **All PLE-linked analysis must filter on `IS_BEST_OBSERVABLE_RECORD`, never on
`IS_BEST_NMAT_RECORD & Year<=2014`.**

### §2b — Why `PERSON_KEY_AMBIGUOUS` uses SEX only (ORCHESTRATOR RULING)

Measured over the 33,714 multi-row keys:

```
contradictory SEX only : 1,097     >1 UNIVERSITY only : 22,002     both : 5,051
SEX contradiction total: 6,148     UNIVERSITY differs total: 27,053
```

A differing university is **not** evidence of a collision — repeat takers legitimately record their
institution differently across sittings (branch naming, abbreviation). Using it would flag 22,002
extra keys and make the column useless. **Use the SEX contradiction only (6,148).**
Emit the university-variance count to the log as a weaker diagnostic; do not put it in the flag.

## 3. Columns RENAMED (4) — the permanent fix for RC-4

`UNIVERSITY` is the applicant's **undergraduate** institution, not their medical school. Renaming
makes the misreading structurally impossible.

| Old | New |
|---|---|
| `UNIVERSITY` | `UNDERGRAD_UNIVERSITY` |
| `UNI_TYPE` | `UNDERGRAD_UNI_TYPE` |
| `UNI_LOCATION` | `UNDERGRAD_UNI_LOCATION` |
| `CourseGroup` | `UNDERGRAD_COURSE_GROUP` |

Every consumer must be updated. No compatibility alias — a silent alias would defeat the purpose.

## 4. Dtypes CORRECTED (3)

Currently stored as `str`, so `bool("False") is True` silently inverts truthiness tests:

| Column | From | To |
|---|---|---|
| `HasTRUErawScores` | `str` | `boolean` (nullable) |
| `StoredVsDerivedMismatch` | `str` | `boolean` (nullable) |

`HasCEMMatch` is no longer coerced — it is dropped entirely (see the ruling above).
Nullable `boolean` is used rather than numpy `bool` because `StoredVsDerivedMismatch` carries
79,611 NaN; plain `bool` cannot hold missingness and would silently coerce NaN to a value.

## 5. Semantics CORRECTED (1)

`IS_BEST_NMAT_RECORD` — **one uniform rule for every person, passers and non-passers alike**:

```
highest NMS_PER_num  ->  latest Year  ->  lowest APPNO_CLEAN     (deterministic, total order)
```

Rows with null `NMS_PER_num` still participate (they sort last) so that **every** `PERSON_KEY`
receives exactly one `True`.

**Hard invariant:** `df.groupby("PERSON_KEY").IS_BEST_NMAT_RECORD.sum().eq(1).all() == True`
and `df.IS_BEST_NMAT_RECORD.sum() == df.PERSON_KEY.nunique() == 134,869`.

Do NOT reintroduce the old split rule (passers got their matched attempt, others their best) — it
selected the two compared groups by different criteria.

---

## 6. Invariants every consumer may rely on

```python
len(df) == 178_927
df.PERSON_KEY.nunique() == 134_869
df.IS_BEST_NMAT_RECORD.sum() == 134_869
df.IS_BEST_OBSERVABLE_RECORD.sum() == 69_503
df.PERSON_KEY_AMBIGUOUS.groupby(df.PERSON_KEY).first().sum() == 6_148
(df.IS_OBSERVABLE_COHORT == (df.Year <= 2014)).all()
not (df.IS_OBSERVABLE_COHORT == df.IS_PLE_PASSER).all()      # no tautology
df.IS_PLE_PASSER.sum() == 49_986                              # authoritative passer count
(df[RAW_8].sum(axis=1) - df.TotalRawScoreTRUE).abs().max() < 1e-6
"IS_PLE_ANALYSIS_SAFE" not in df.columns
"NMA_College" not in df.columns
```

`RAW_8 = [Raw_Biology, Raw_Chemistry, Raw_InductiveReasoning, Raw_PerceptualAcuity,
Raw_Physics, Raw_Quantitative, Raw_SocialScience, Raw_Verbal]`

## 7. Semantics that must be respected in ALL analysis code

- **`IS_PLE_PASSER` (49,986) is the ONLY authoritative passer count.** `PLE_YEAR_PASSED`,
  `PLE_MATCH_METHOD`, `PLE_YEAR_GAP` are diagnostic metadata; the sets are **not nested**
  (7,318 rows have a year but are not passers — rejected matches that kept metadata; 2,776 are
  passers with no year — all `MANUAL_APPNO_MATCH`, whose source file has no year column).
  Never use them as a passer denominator.
- **"Not linked" is NOT "failed".** The PLE source contains passers only. Every rate built from
  `IS_PLE_PASSER` is a **linkage rate**, never a pass rate. Label it as such everywhere.
- **Percentile bins: `B1` is the LOWEST decile (0-9); `B10` the highest (90-99).** Always order
  charts/tables by `BIN_ORDER = [B1..B10]` — string sorting puts B10 between B1 and B2.
- **People vs sittings:** filter `IS_BEST_NMAT_RECORD` when counting people; do not when counting
  exam sittings. State which in every caption.
- **`CITIZENSHIP_FINAL` contains a literal `"Foreign"` placeholder (156 rows)** — an unresolved
  bucket, not a country. Exclude or explicitly label it in nationality charts.
- **Nationality shares must use the full `Verified Foreigner` denominator (32,501)**, never a
  top-N subtotal. India is **81.5%**, not 85.1%.
- **The B4->B5 linkage jump (25.9% -> 46.8%) is the existing 40th-percentile admission rule, not
  ability.** Any cut-off narrative must state this selection effect.
- **No institution-level PLE performance claims.** No medical-school identifier exists.
  `UNDERGRAD_UNI_TYPE` is not an SUC/PHEI proxy.

## 8. Reference values after remediation (for tests and captions)

| Quantity | Value |
|---|---|
| Exam sittings | 178,927 |
| Unique examinees | **134,869** |
| Observable cohort (people, Year<=2014) | **69,503** |
| Observable linkage rate (`IS_BEST_OBSERVABLE_RECORD`) | **45.71%** |
| Naive `IS_BEST_NMAT_RECORD & Year<=2014` (**do not use**) | 65,782 people / 46.69% |
| `PERSON_KEY_AMBIGUOUS` keys | 6,148 |
| Confirmed PLE passers | 49,986 |
| Stored-total mismatch | **56,065 of 99,316 rows with a stored total = 56.45%** (31.33% of all rows). NEVER "42.2%". |
| India share of verified foreigners | **81.5%** (26,490 / 32,501) |
| Verified foreigners | 32,501 (18.2% of records) |
| Best-record rows with valid bin | 130,735 |
| Row-level match rate, observable window | 46.4% |

## 9. File layout after remediation

```
dataset/NMAT_Exodus.parquet                              <- canonical, produced by 5_Slim_Exodus.py
streamlit_dashboard/main_dashboard/NMAT_Exodus.parquet   <- copy, must be byte-identical
streamlit_dashboard/CHED_relevant_dashboard/NMAT_Exodus.parquet  <- copy, must be byte-identical
```

`5_Slim_Exodus.py` copies to both dashboard folders and writes a checksum manifest, so the three
can never silently diverge.

## 10. Rules for all agents

1. Log your work to `.claude/audit/logs/<your-id>_<area>.md` — what you changed, file:line, what you
   verified, what you could NOT do and why. Be honest about failures; a false "done" is worse than a
   reported blocker.
2. **Never commit.** The orchestrator owns all commits. Never run git commit/push/checkout/reset.
3. **Never touch the nested repos** at `streamlit_dashboard/*/. git` — parent repo only.
4. Use `./.venv/Scripts/python.exe`.
5. Verify by running, not by reading. Every numeric claim in your log needs a command + its output.
6. If you finish early, deepen your verification rather than expanding scope.
