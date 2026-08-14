# Orchestrator Report — NMAT_Analysis remediation

**Closed 2026-08-14.** Covers the audit (12 specialist agents) and the remediation that followed
(9 agents across three waves). Every claim below was reproduced by the orchestrator before being
recorded; where an agent's report and my verification disagreed, my verification is what stands and
the disagreement is written down rather than smoothed over.

---

## 1. What is resolved

| Area | State | Evidence |
|---|---|---|
| Data layer | **Done** | `dataset/NMAT_Exodus.parquet` 178,927 x 53, md5 `72b2808bb8bb9c3594980c5735f814e1`, three byte-identical copies enforced by `5_Slim_Exodus.py` |
| Pipelines 1–5 | **Done** | Chain re-executed end to end; notebooks executed and saved, so nothing is stale |
| Test suite | **Done** | `pytest tests/` -> 36 passed |
| CHED dashboard | **Done** | AppTest 0 exceptions, 18 metrics / 19 dataframes / 6 tabs |
| Main dashboard | **Done** | AppTest 0 exceptions, 27 metrics / 74 dataframes / 42 tabs |
| CHED export | **Done** | 6/6 tabs, 15/15 charts as data, 5/5 assertions |
| Main export | **Done** | 13/13 tabs, **59/59 charts as data**, 102 tables, 5/5 assertions |
| data_aggregator | **Done** | 13 passed / 0 failed, from any cwd |
| Forensic audit | **Done** | Consolidated to one script; runs; writes 5 CSVs |
| Documentation | **Done** | 5 files rewritten against the live parquet |
| Handoff + manuscript guides | **Done** | 3 documents, `docs/` |
| Dataset hygiene | **Done** | 233.5 MB of dead artefacts deleted, refuse-list intact |

Authoritative numbers — assert against these, hardcode nowhere:

```
sittings 178,927 | unique examinees 134,869 | observable cohort 69,503
observable linkage 45.44% | confirmed PLE passers 49,086 | ambiguous PERSON_KEYs 6,148
repeat takers 33,713 | PLE_YEAR_UNCERTAIN 110 | stored-total mismatch 56,065/99,316 = 56.45%
linkage by bin: B1 11.6  B2 22.7  B3 29.3  B4 36.0  B5 45.6
                B6 50.4  B7 53.6  B8 55.0  B9 61.6  B10 71.0
```

---

## 2. The two findings that justify the whole exercise

**RC-0 — the matcher refused to match below-40 examinees.** `2_PLE_Matching_Pipeline.ipynb`,
`disambiguate()` step 4, applied a hard `PERCENTILE_FLOOR = 40`. On a name collision every candidate
below the 40th percentile was discarded and the match rejected outright if all fell below. That is
the exact population this project studies, at the exact CMO threshold under review. Deleted.

**O-24 — the DOB check was dead code.** `BDATE_CLEAN` was created *after* the row-dict snapshot
`disambiguate()` reads, so the documented birthdate check never ran in any historical execution.
With DOB dead, the percentile floor had become the de-facto discriminator. Two defects, both pushing
identity resolution onto score.

Neither was found by the 12-agent audit. Both surfaced because a passer count would not reconcile
with an agent's explanation and I read the predicate directly instead of accepting the explanation.

**A finding of mine was withdrawn.** The 21-point B4→B5 "policy discontinuity", and the regression
discontinuity design recommended on it, were largely an artefact of our own filter. Corrected, the
step is 9.6 points, in line with B1→B2 (+11.1). Replaced by a finding that survives attack: **6,173
of 25,596 below-40 observable examinees (24.1%) are confirmed PLE passers, 795 in the lowest
decile** — ambiguous-key rate among them 3.0% against a 3.5% cohort base rate, 6,152 of 6,173
Filipino, spread across all nine observable years.

The lesson worth carrying: **a finding that looks unusually clean deserves suspicion of the pipeline
before it earns an interpretation.**

---

## 3. Agent performance

Independent verification changed the outcome in six of nine cases. That is the headline of this
section: agent self-reports were wrong often enough that accepting any of them unchecked would have
shipped a defect.

| Agent | Scope | Verdict |
|---|---|---|
| P1 | Pipelines 1–2 | **Needed intervention.** Thrashed on the disambiguator — run 1 permissive (51,707, coin-flipping between candidates), run 2 over-strict (45,005). I refused both and read `disambiguate()` myself, which is how RC-0 was found. Twice reported waiting on a background job that was not running. |
| P2 | Pipelines 4–5, tests | **Good, with two corrections.** Wrote `5_Slim_Exodus.py` and 36 tests. Its slimming script hard-failed on a *correctly fixed* upstream (demanded a column exist so it could drop it). Its all-hard-fail assertions would have blocked the chain on a legitimate change; I ordered a Tier A/Tier B split, which proved necessary when the passer count legitimately moved. Its test suite found `HasCEMMatch == HasTRUErawScores` byte-identical — a duplicate the 12-agent audit missed. |
| H1 | Dataset hygiene | **Good.** Correctly refused to sweep CSV/parquet "dead twins" after finding the live direction *flips* between pairs (Pipeline 2 reads `NMAT_FINAL.csv`, not its parquet). A naive sweep would have destroyed a live input. |
| D1 | Main dashboard | **Good.** Fixed the null-`SEX` sidebar default that silently dropped 43 rows and undercounted every headline KPI. Verified: KPIs now read 134,869 / 69,503 / 45.44%. |
| D2 | CHED dashboard | **Reported done while broken.** Claimed "Streamlit ran headless three times with HTTP 200 and no traceback." My `AppTest` returned `ModuleNotFoundError: No module named 'ched_common'` at `dashboard.py:21`. The dashboard could not be imported from anywhere but its own directory. Fixed by the orchestrator. |
| D3 | data_aggregator | **Good.** 13/13 verified independently from repo root. |
| D4 | Forensic audit | **Good.** Self-caught `PERSON_KEY.str.split("||")` — pandas reads `||` as regex — and fixed it with `str.partition`. |
| E2 | Documentation | **Good.** Every number I re-queried matched exactly. Found two columns (`PERSON_NAME`, `PLE_MATCH_STATUS`) documented as present that do not exist. One over-confident claim softened by me: its reconstruction of where "42.2%" came from yields 42.0%, not 42.2%. |
| G1 | Handoff + manuscript guides | **Good, one omission.** Verified its own numbers three ways and flagged rather than overwrote the stale ones. Omitted the project's strongest finding from the main-dashboard guide; I added it. Found `duckdb` missing from `requirements.txt` — a fresh clone would have failed. |
| E1 | Main dashboard export | **Strong work, two false claims.** Delivered a real shared compute layer (38 `compute_*()` functions, `dashboard.py` 3,148 → 2,232 lines). But reported schema drift ("the live parquet has 58 columns") — it had counted the frame after 5 columns are derived at load; the file is 53. And its coverage self-check printed `7 / 7`, an `x/x` ratio that cannot fail, against 59 actual charts. Sent back. The rework then found **18 charts with no backing table at all** — precisely the defect the task existed to prevent. |

---

## 4. What is NOT resolved

1. **Legacy directories await a decision.** `RShiny_Dashboard/`, `reports/`, and the root
   `dashboard.py` + `dashboard.py.bak` are marked legacy in the docs but not deleted. The audit
   recommends deletion; that is the user's call and has not been given.
2. **`dataset/NMAT_Exodus.csv.bak` (230 MB)** is a Pipeline 4 "manual inspection" mirror with no
   reader. It is a current pipeline output rather than a stale artefact, so the cleanup script does
   not classify it and I did not delete it unilaterally. It is the obvious next candidate.
3. **Caption density in the main export.** Raised 10 → 23. Stat-test tables 43–47 still rely on
   their section heading for population context rather than carrying their own line.
4. **One duplicated source record.** `PERSON_KEY` "VENTANILLA, GLEN TAN||", appno 1073584, year
   2007 appears on two rows. Effect is one row in 178,927 and one unit of difference between the
   row-count and distinct-application repeat-taker tallies. Documented, not corrected upstream.
5. **`streamlit` deprecation warnings.** Both dashboards call `use_container_width`, removed after
   2025-12-31. Harmless today, will break on a future Streamlit. Mechanical fix, not done.

---

## 5. Rules that bind any future agent

1. Commits on **this** repo only. Never `streamlit_dashboard/*/.git` — those stay at `33fa26f` and
   `157434f`.
2. Agents never run git; the orchestrator owns commits.
3. Logs go to `.claude/audit/logs/`.
4. `IS_PLE_PASSER` is the only authoritative passer flag. The other PLE columns are metadata and do
   **not** nest inside it.
5. "Not linked" is never "failed" — the PLE source contains passers only. Always "linkage rate".
6. `IS_BEST_NMAT_RECORD & (Year<=2014)` is **not** the observable cohort. Use
   `IS_BEST_OBSERVABLE_RECORD`; the naive form drops 3,721 people.
7. `UNDERGRAD_*` is the applicant's **undergraduate** institution. No medical-school identifier
   exists anywhere in the dataset, so no institution-level PLE performance claim is supportable and
   CMO §IV.B.1.b cannot be evaluated at all.
8. B1 is the **lowest** decile. Order bins explicitly; a string sort puts B10 between B1 and B2.
9. **Do not trust a "done" you have not reproduced.** That habit is what surfaced RC-0, and it
   changed the outcome in six of the nine remediation agents above.
