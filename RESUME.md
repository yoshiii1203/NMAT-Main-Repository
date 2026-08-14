# RESUME — where this work stands and what to do next

**Paused:** 2026-07-31, session limit. Branch `master`. Nested repos in
`streamlit_dashboard/*/` were never touched, as instructed.

Read `.claude/audit/_ORCHESTRATOR_FINDINGS.md` first (O-1..O-24), then
`.claude/audit/_TARGET_SCHEMA_CONTRACT.md`. Those two files carry all the state.

---

## Commits so far

| sha | what |
|---|---|
| `016df16` | audit checkpoint — 12 specialist reports + plan |
| `4972ef3` | pipeline chain 1–5 rebuilt (RC-1…RC-4 fixed at source) |
| `bfb9e5c` | **matcher fix (RC-0)** — removed the 40th-percentile hard filter |
| `8e771ad` | forensic audit consolidated, unsupported claims withdrawn |
| `719e04b` | **wip** — CHED dashboard + data_aggregator on the new schema |

## Data layer: DONE and verified

```
dataset/NMAT_Exodus.parquet   178,927 x 53   md5 28b85ac53af13b4a2ef3ee93527c97c1
3 byte-identical copies (dataset/ + both dashboard folders), enforced by 5_Slim_Exodus.py
dataset/EXODUS_MANIFEST.json written
pytest tests/  ->  36 passed
```

Authoritative values — assert against these, hardcode nowhere:
```
sittings 178,927 | unique examinees 134,869 | observable cohort (people) 69,503
observable linkage 45.44% | confirmed PLE passers 49,086 | ambiguous PERSON_KEYs 6,148
repeat takers 33,713   (people with >1 distinct APPNO_CLEAN -- the row-count form gives
                        33,714 because one record is duplicated outright:
                        "VENTANILLA, GLEN TAN||" / appno 1073584 / 2007)
PLE_YEAR_UNCERTAIN 110 | stored-total mismatch 56,065 / 99,316 = 56.45%  (never "42.2%")
linkage by bin: B1 11.6  B2 22.7  B3 29.3  B4 36.0  B5 45.6
                B6 50.4  B7 53.6  B8 55.0  B9 61.6  B10 71.0
```

## The two findings that matter most

**RC-0 — the matcher refused to match below-40 examinees.** `disambiguate()` step 4 had a hard
`PERCENTILE_FLOOR = 40` filter, so name-collision candidates below the 40th percentile were
discarded and the match rejected outright if all fell below. That is the exact population the
project studies, and 40 is the exact CMO threshold under review. Deleted. Identity now resolves on
year-gap, DOB/sex and latest-year only; ties are rejected as ambiguous, never decided on score.

**O-24 — the DOB step was dead code.** `BDATE_CLEAN` was created *after* the row-dict snapshot
`disambiguate()` reads, so the documented birthdate check never ran in any historical execution.
With DOB dead, the percentile floor became the de-facto discriminator. Two defects, both pushing
identity resolution onto score.

**Headline finding (replaces a withdrawn one):** 6,173 of 25,596 below-40 observable examinees
(**24.1%**) are confirmed PLE passers — 795 in the lowest decile. Ambiguous-key rate among them is
3.0%, *below* the 3.5% cohort base rate, so they are not collision artefacts; 6,152 of 6,173 are
Filipino; spread across all nine years.

**Withdrawn:** the 21-point B4→B5 "discontinuity" and the regression-discontinuity recommendation
built on it. Corrected step is 9.6 points, in line with B1→B2 (+11.1). It was mostly our own filter.

---

## Outstanding work

### 1. Verify the wip commit (`719e04b`) — do this first
Neither was orchestrator-verified before the pause.
```bash
.venv/Scripts/python.exe -m pytest tests/ -q
.venv/Scripts/python.exe -c "from streamlit.testing.v1 import AppTest; \
  at=AppTest.from_file('streamlit_dashboard/CHED_relevant_dashboard/dashboard.py', default_timeout=540); \
  at.run(); print('exceptions:', len(at.exception)); [print(str(e)[:300]) for e in at.exception[:3]]"
.venv/Scripts/python.exe data_aggregator/run_all.py     # must produce 13/13 from ANY cwd
```
Check `.claude/audit/logs/D2_ched_dashboard.md` and `D3_data_aggregator.md` for what they claim,
then confirm it independently. **Do not trust a "done" you have not reproduced** — that habit is
what surfaced RC-0.

### 2. Agents that were still running at the pause
Their work may be partially on disk. Re-verify or re-dispatch:
- **D1** (`main_dashboard/dashboard.py`) — was fixing a bug I found: the default sidebar **Sex**
  filter silently drops the 43 rows with null `SEX`, so headline KPIs read 134,826 / 69,460 instead
  of 134,869 / 69,503. Fix = add an explicit **"(not specified)"** option, selected by default, and
  check Year / Course Group / University Type / PLE status for the same defect.
- **E1** — building `main_dashboard/export_markdown.py` (the export button the user asked for),
  plus `main_common.py` shared compute. Spec: `.claude/audit/_EXPORT_FORMAT_CONTRACT.md`.
- **E2** — rewriting `docs/data_dictionary.md`, `docs/pipeline_architecture.md`, `CLAUDE.md`,
  `README.md`, `changelog.md`.

### 3. Not yet started
- **Handoff/testing guide** — how to run each dashboard, what to check on each tab, how to verify
  an export matches what the screen shows.
- **Two manuscript guides** — section outlines + what to discuss, one for main-dashboard insights,
  one for CHED-dashboard insights. Must include the per-pipeline data-quality narrative (the
  CHED/CEM problems Pipelines 1–2 handle): the 56.45% stored-total mismatch, the fuzzy
  university-name matching, the dead DOB filter, the percentile floor, PERSON_KEY collisions.
- **Stale-artifact cleanup** — `dataset/_cleanup_stale.py` exists and is **dry-run only**; its
  `TIER_NOW` holds just `UNIVS_ARCHIVED.csv`. `TIER_FUTURE` (~472 MB: `NMAT_Exodus.csv`,
  `output/NMAT_FINAL.parquet`) is now safe to promote since the pipelines have re-run and
  `5_Slim_Exodus.py` exists. Review `dataset/DATASET_MANIFEST.md` first.
  **Never delete** the refuse-list files — H1 found the CSV-vs-parquet "dead twin" direction *flips*
  between pairs (Pipeline 2 reads `NMAT_FINAL.csv`, not its parquet), so a naive sweep would destroy
  a live input.
- **Decide on** `RShiny_Dashboard/`, `reports/`, root `dashboard.py` + `dashboard.py.bak` — the plan
  recommends deleting all as legacy. Not done; needs the user's nod.
- **`forensic_audit/`**: `PLE_AMBIGUOUS_REVIEW.csv` still filters on the retired `"AMBIGUOUS"`
  status string instead of `"AMBIGUOUS_NAME_COLLISION"` (flagged by P1, unowned).

---

## Rules that still bind any agent

1. Commits on **this** repo only. Never `streamlit_dashboard/*/.git`.
2. Agents never run git; the orchestrator owns commits.
3. Logs go to `.claude/audit/logs/`.
4. `IS_PLE_PASSER` is the only authoritative passer count; the other PLE columns are metadata and
   do **not** nest inside it.
5. "Not linked" is never "failed" — the PLE source contains passers only. Always "linkage rate".
6. `IS_BEST_NMAT_RECORD & (Year<=2014)` is **not** the observable cohort — use
   `IS_BEST_OBSERVABLE_RECORD` (the naive form drops 3,721 people).
7. `UNDERGRAD_*` is the applicant's **undergraduate** institution. No medical-school identifier
   exists, so no institution-level PLE performance claim is supportable.
8. B1 is the **lowest** decile. Order bins explicitly; string sort puts B10 between B1 and B2.
