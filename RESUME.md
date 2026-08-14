# RESUME — where this work stands and what to do next

**Remediation closed 2026-08-14.** Branch `master`. Nested repos in `streamlit_dashboard/*/` were
never touched and remain at `33fa26f` / `157434f`, as instructed.

Read `.claude/audit/_ORCHESTRATOR_REPORT.md` first — it is the closing report: what is resolved,
what is not, how each agent performed, and the rules that bind future work. Then
`.claude/audit/_ORCHESTRATOR_FINDINGS.md` (O-1..O-24) and
`.claude/audit/_TARGET_SCHEMA_CONTRACT.md` for the detail.

---

## Everything verified green

```
dataset/NMAT_Exodus.parquet   178,927 x 53   md5 72b2808bb8bb9c3594980c5735f814e1
3 byte-identical copies (dataset/ + both dashboard folders), enforced by 5_Slim_Exodus.py

pytest tests/                                          36 passed
CHED dashboard   AppTest                               0 exceptions, 18 metrics / 19 dfs / 6 tabs
main dashboard   AppTest                               0 exceptions, 27 metrics / 74 dfs / 42 tabs
CHED export      6/6 tabs, 15/15 charts as data, 5/5 assertions
main export      13/13 tabs, 59/59 charts as data, 102 tables, 5/5 assertions
data_aggregator/run_all.py                             13 passed, 0 failed (any cwd)
forensic_audit/forensic_audit.py                       completes, writes 5 CSVs
```

Authoritative values — assert against these, hardcode nowhere:
```
sittings 178,927 | unique examinees 134,869 | observable cohort (people) 69,503
observable linkage 43.31% | confirmed PLE passers 47,485 | ambiguous PERSON_KEYs 6,148
PLE_YEAR_UNCERTAIN 79 | stored-total mismatch 56,065 / 99,316 = 56.45%  (never "42.2%")
repeat takers 33,713   (people with >1 distinct APPNO_CLEAN -- the row-count form gives 33,714
                        because appno 1073584 "VENTANILLA, GLEN TAN||" / 2007 carries TWO rows
                        with different score sets, percentiles 98 and 80, same test date:
                        a source collision, not a duplicated row)
confirmed PLE passers  47,485 SITTINGS = 35,746 distinct people. Cite the one you mean.
linkage by bin: B1 10.8  B2 20.7  B3 26.7  B4 33.3  B5 43.3
                B6 47.4  B7 50.5  B8 52.7  B9 59.5  B10 69.8
```

## How to run it

```bash
cd streamlit_dashboard/main_dashboard         && streamlit run dashboard.py
cd streamlit_dashboard/CHED_relevant_dashboard && streamlit run dashboard.py
.venv/Scripts/python.exe data_aggregator/run_all.py
.venv/Scripts/python.exe -m pytest tests/ -q
```
Each dashboard has an **Export Complete Dashboard** expander producing one Markdown document with
every chart's values as a data table. Both can also be regenerated headlessly by running their
`export_markdown.py` directly. `docs/HANDOFF_TESTING_GUIDE.md` is the per-tab acceptance checklist.

## READ THIS BEFORE CITING ANY LINKAGE NUMBER

**`PLE_DATA.csv` covers only 2011–2022.** Zero records before 2011, none after 2022. The median
NMAT→PLE gap is 6 years, so every cohort is observed through a *different* window: 2014 examinees
must pass within 8 years to appear at all, while 2006 examinees lose anyone who passed before 2011.
`Year <= 2014` does **not** make the cohort comparable.

This inflates every published linkage figure. At an equal 8-year horizon the observable linkage is
**38.0%**, not 43.31%, and the apparent 54%→37% decline across years mostly disappears.

Two defects compound on the headline. Applied in sequence (the former `-1`-sentinel step is no
longer separate — it is now fixed at the source, see below):

| below-40 linkage | value | n |
|---|---|---|
| published | 22.6% | 5,665 / 25,023 |
| + equal 8-year exposure | 18.3% | not independently re-verified this pass |
| + drop contested-name people (**conservative floor**) | **17.9%** | 4,325 / 24,185 |

B1, lowest decile: **740 published → 482 at the floor.** The gradient stays clean and monotone
(B1 7.1 → B10 63.3), so **the conclusion survives — the 40th-percentile floor was not uniformly
binding** — but the published precision does not. Cite a range, not "22.6%".

Also: **`NMS_PER_num`'s `-1` sentinel** (2,866 rows) is now **fixed at the source** in Pipeline 1 —
it is `NaN`, not `-1`. Previously it was correctly excluded from `PercentileBin` (NaN) but
`-1 < 40` was `True`, so every naive `< 40` predicate silently swallowed it; that is what the old
"drop `-1` sentinel rows" cascade step above corrected for, and why the "published" row now starts
from the sentinel-safe number directly.

Full detail, including the contested-name double-crediting bug and six other confirmed defects:
`.claude/audit/_PIPELINE_ACCURACY_AUDIT.md`.

## The two findings that matter most

**RC-0 — the matcher refused to match below-40 examinees.** `disambiguate()` step 4 had a hard
`PERCENTILE_FLOOR = 40` filter, so name-collision candidates below the 40th percentile were
discarded and the match rejected outright if all fell below. That is the exact population the
project studies, and 40 is the exact CMO threshold under review. Deleted. Identity now resolves on
year-gap, DOB/sex and latest-year only; ties are rejected as ambiguous, never decided on score.

**O-24 — the DOB step was dead code.** `BDATE_CLEAN` was created *after* the row-dict snapshot
`disambiguate()` reads, so the documented birthdate check never ran in any historical execution.
With DOB dead, the percentile floor became the de-facto discriminator.

**Headline finding (replaces a withdrawn one):** 5,665 of 25,023 below-40 observable examinees
(**22.6%**) are confirmed PLE passers — 740 in the lowest decile. Ambiguous-key rate among them is
3.3%, *below* the 3.5% cohort base rate; 5,645 of 5,665 are Filipino; spread across all nine years.

**Withdrawn:** the 21-point B4→B5 "discontinuity" and the regression-discontinuity recommendation
built on it. Corrected step is 10.0 points, in line with B1→B2 (+9.9). It was mostly our own filter.

---

## Outstanding — all of it needs a decision, none of it blocks use

1. **Legacy directories.** `RShiny_Dashboard/`, `reports/`, root `dashboard.py` + `dashboard.py.bak`
   are marked legacy in the docs but not deleted. The audit recommends deletion; that is your call.
2. **`dataset/NMAT_Exodus.csv.bak` (230 MB)** — a Pipeline 4 "manual inspection" mirror with no
   reader. It is a *current* pipeline output rather than a stale artefact, so the cleanup script
   does not classify it and it was not deleted unilaterally. Obvious next candidate.
   **Never delete** the `_cleanup_stale.py` refuse-list files — the CSV-vs-parquet "dead twin"
   direction *flips* between pairs (Pipeline 2 reads `NMAT_FINAL.csv`, not its parquet), so a naive
   sweep would destroy a live input.
3. **Caption density** in the main export: 23 of 102 tables. Stat-test tables 43–47 lean on their
   section heading for population context rather than carrying their own line.
4. **`use_container_width`** is deprecated in Streamlit (removed after 2025-12-31) and used
   throughout both dashboards. Harmless now, mechanical to fix, will break on a future upgrade.

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
9. **Do not trust a "done" you have not reproduced.** It changed the outcome in six of the nine
   remediation agents — see the report.
