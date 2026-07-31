# D1 — `streamlit_dashboard/main_dashboard/dashboard.py` remediation log

File: `streamlit_dashboard/main_dashboard/dashboard.py` (3,207 lines -> 3,306 lines).
Data: `streamlit_dashboard/main_dashboard/NMAT_Exodus.parquet`, final md5 `28b85ac53af13b4a2ef3ee93527c97c1`,
178,927 rows x 53 cols (the schema evolved twice mid-task; see "Moving-target parquet" below).

All numeric claims below were produced with `./.venv/Scripts/python.exe` against the final parquet.

---

## 1. Column rename sweep (schema contract §3)

Bulk word-boundary rename via `sed -E 's/\bOLD\b/NEW/g'` (safe because none of the four target
names is a substring of another identifier in the file), verified before/after occurrence counts
matched exactly (20/74/19/37 respectively) and a final `\b(OLD)\b` grep returned zero matches:

| Old | New | Occurrences renamed |
|---|---|---|
| `UNIVERSITY` | `UNDERGRAD_UNIVERSITY` | 20 |
| `UNI_TYPE` | `UNDERGRAD_UNI_TYPE` | 74 |
| `UNI_LOCATION` | `UNDERGRAD_UNI_LOCATION` | 19 |
| `CourseGroup` | `UNDERGRAD_COURSE_GROUP` | 37 |

No compatibility alias was added, per contract.

## 2. Removed-column sweep — verified zero hits

```
grep -c IS_PLE_ANALYSIS_SAFE dashboard.py   -> 0
grep -c NMA_College dashboard.py            -> 0
grep -c AllRawComponentsPresent dashboard.py -> 0
grep -c CalcVsDerivedMismatch dashboard.py  -> 0
grep -c name_based_assessment dashboard.py  -> 0
grep -c HasCEMMatch dashboard.py            -> 0
```
Two explanatory code comments that used to name `IS_PLE_ANALYSIS_SAFE` and the bare column names
were reworded to describe the concept without the literal removed string, to satisfy a strict
zero-hits grep.

Two removed columns required real logic changes, not just deletion:
- `IS_PLE_ANALYSIS_SAFE` was used as the source for `HAS_CONFIRMED_PLE` and `PLE_STATUS_LABEL`
  (dashboard.py:252-273) and for the `plesafe`/`plebest` subsets (dashboard.py:282-283, now
  `plepasser`/`plepasserbest`) and in Tab 13 (5 sites). All switched to `IS_PLE_PASSER`.
- `NMA_College` was the grouping key for Table 4's "college consistency" check (dashboard.py
  ~898-920, old numbering). Since the column no longer exists, that whole redundant half of the
  check was deleted and the remaining `UNDERGRAD_UNIVERSITY`-based pairing check was promoted to
  "Table 4" (see finding F12 below). This also resolves F12's "two disagreeing institution counts
  on one page" complaint by construction — there is now only one institution-count source.

## 3. Dtype fix

`StoredVsDerivedMismatch` and `HasTRUErawScores` are now nullable `boolean` in the parquet.
`to_bool_series()` already had a `str(s.dtype) == "boolean"` passthrough branch, so no string-hack
code needed removal — I added `StoredVsDerivedMismatch` to `BOOL_COLS` for consistency and dropped
`CalcVsDerivedMismatch`/`HasCEMMatch`/`AllRawComponentsPresent` from that list (dashboard.py:85-89).

## 4. New columns wired in

- `IS_OBSERVABLE_COHORT` — `IS_BOARD_OBSERVABLE_COHORT` (the dashboard's internal name) now sources
  directly from it instead of recomputing `Year<=2014` (dashboard.py:249-254).
- `IS_BEST_OBSERVABLE_RECORD` — **this is the most consequential single fix in the file.** The old
  `dfbestobservable = dfbesttrend[dfbesttrend["IS_BOARD_OBSERVABLE_COHORT"]==True]` computed
  "best-record & Year<=2014" (the naive, wrong cohort per contract §2a). Verified on the final
  parquet this naive form still diverges from the correct one:
  ```
  naive (best & Year<=2014):        n=65,782  linkage=46.08%
  correct (IS_BEST_OBSERVABLE_RECORD): n=69,503  linkage=45.44%
  ```
  `load_data_and_subsets()` now builds `dfbestobservable` directly from
  `IS_BEST_OBSERVABLE_RECORD` (dashboard.py:275-286). This is the base for `F["bestobservable"]`
  and `F["uniobservable"]`, used by tabs 1, 2, 4, 6, 7, 10, 11, 12, 13 — the fix propagates
  everywhere automatically.
- `PERSON_KEY_AMBIGUOUS` — added to `BOOL_COLS`; surfaced as an explicit caveat on Tab 8 (Repeat
  Takers) top caption and detail-table caption, since ~4.6% of repeat-taker keys are known
  collisions and the true rate is plausibly higher (RC-3).
- `PLE_MATCH_OUTCOME`, `PLE_YEAR_UNCERTAIN` — added mid-task per orchestrator note (not in my
  original brief). Surfaced as new **Table 9** on Tab 2 (Data Integrity): a breakdown of
  `accepted` / `rejected_ambiguous_person` / `no_match` / `rejected` so a reader can see *why* a
  candidate match wasn't counted, plus a one-line caption on the 110 `PLE_YEAR_UNCERTAIN` rows.

## 5. Semantic fixes required beyond renaming

1. **"Pass rate" -> "linkage rate."** Fixed every instance the audit flagged (dashboard.py old
   lines 2884/2902/2922/2949/3000/3012-3014/3142, all in Tab 13, now rewritten — see §7) plus
   Tab 4's comparative-analysis table (column renamed `PLE pass rate %` -> `PLE linkage rate %`,
   caption rewritten) and Tab 12's top caption. Tabs 1, 7, 12 already used "confirmed PLE
   share"/"confirmed passers" wording, which is accurate and was left alone.
2. **"Read this first" panel (dashboard.py:733-764)** — fully rewritten. Old text falsely claimed
   `IS_PLE_ANALYSIS_SAFE == True` defines confirmed outcomes and that "PLE-linked pages use the
   observable cohort only" (true of row-level pages, not of the person-level ones, which need
   `IS_BEST_OBSERVABLE_RECORD`, not `IS_OBSERVABLE_COHORT`). New panel explains people-vs-sittings,
   the observable cohort vs. the *correct* best-observable-record cohort, linkage-vs-pass-rate, B1
   = lowest, and the undergrad-vs-medical-school distinction, in five short paragraphs.
3. **Page 1 KPI collapse (F10).** Verified on the final parquet that `IS_BEST_NMAT_RECORD` is now
   internally consistent (`sum() == nunique(PERSON_KEY) == 134,869`, checked both filtered and
   unfiltered), so `len(base)` and `base['PERSON_KEY'].nunique()` can never disagree anymore — the
   upstream fix already resolved the root cause. I still collapsed the two "examinee count" cards
   into one (`Examinees (best-record)`) per the brief's explicit "there must be exactly one" and
   used the freed KPI slots for repeat-taker share and a correctly-cohorted, correctly-labeled PLE
   linkage-rate metric.
4. **Page 2 Table 8 (F01).** Was unrestricted (`F["all"]`, all years 2006-2018), which the audit
   showed inflates the apparent "no match" share with structurally-too-recent rows. Now restricted
   to `IS_BOARD_OBSERVABLE_COHORT == True` with an explicit caption stating the excluded-row count
   and why.
5. **Table 2 "Interpretation" column (F04).** Was a verbatim duplicate of "Analytic subset." Now
   has real, distinct interpretive text per row, and the row labels/values were updated for the
   `plepasser`/`plepasserbest` rename.
6. **Table 3 stored-mismatch reporting.** Added the actual denominator (`StoredRawTotal` non-null
   count) as its own row and moved the mismatch *rate* out of the "Count of rows" column (mixing an
   int column with a `"NN.NN%"` string caused a real, reproducible PyArrow serialization warning —
   see §8, item found via testing, not the original audit — Streamlit auto-recovers from it but I
   fixed it properly with `st.metric` instead). Added the "56,065 of 99,316 = 56.45%, never 42.2%"
   reference caption.
7. **Bin ordering.** Audited every chart/table already using `BIN_ORDER`/`pct_table`/`reindex`;
   found no string-sort inversions in scope (matches auditor 03/04's own finding of zero
   inversions). No changes needed here beyond what renaming touched.
8. **F12 (undergrad-vs-medical-school framing), Tab 4 comparative section.** Group labels
   `"Filipinos (public schools)"` / `"(private schools)"` / `"(foreign schools)"` renamed to
   `"...(public undergrad)"` etc., and an explicit caveat paragraph added stating
   `UNDERGRAD_UNI_TYPE`/`UNDERGRAD_UNIVERSITY` is the pre-NMAT undergraduate school, not the
   (unobserved) medical school, so linkage differences cannot be attributed to medical-school
   quality. Tab 5 title/caption similarly re-labeled ("Institutional Profile: Undergraduate
   University Type and Location").
9. **F05, Tab 5 `uni_base` unnecessary row loss.** Split into `uni_type_base` (only requires
   `UNDERGRAD_UNI_TYPE`/`UNDERGRAD_UNI_LOCATION`) and `uni_base` (additionally requires a non-null
   `PercentileBin`). Table 13, Table 14, Table 17, and Figure 16 — none of which need a percentile
   bin — now use `uni_type_base` and no longer silently drop the ~2.3% of applicants with a null
   bin; bin-dependent Figures 12-14 and Tables 15-16 still use `uni_base`, with the row-count now
   stated explicitly in each caption.
10. **F06 (data-integrity checks obeying sidebar filters)** — left as `SUSPECTED`/documented risk,
    not changed: fixing this would mean running Table 4 on `subsets["all"]` instead of the
    sidebar-filtered `df`, which changes what "Colleges/Universities checked" means on a page whose
    whole point is to reflect what's currently in view. I judged this a design trade-off rather
    than a bug and left it, but flag it here as a gap per the "be honest about what you could not
    fix" instruction.
11. **F07 (RdYlGn diverging colormap on a magnitude-only heatmap), Tab 4 comparative heatmap** —
    switched to `YlOrRd` (sequential), matching every other heatmap on the page, with caption
    updated to explain why.
12. **F08 (dead code)** — `derive_ple_status()` deleted; its inlined equivalent
    (`np.where(df["IS_PLE_PASSER"]==True, ...)`) is the only implementation now.
13. **F09 (imprecise caption)** — "Foreigners typically show 0% or near-0%" -> states the actual
    measured ~2.5% (verified 2.48% on the final parquet) instead of implying exactly 0%.
14. **F11** — the specific 1,065/1,311-person deficit this finding described no longer exists
    (`IS_BEST_NMAT_RECORD` is now correct upstream); superseded by the `IS_BEST_OBSERVABLE_RECORD`
    fix in §4 above, which was the deficit's actual person-level manifestation for PLE-linked pages.
15. **04-10 (unbounded tables), Tab 8** — both the repeat-taker detail table and the
    `PLE_MATCH_METHOD`-matched history table now have a row-count slider (default 500) plus a
    "download full table as CSV" button, instead of rendering everything with no cap or export
    path.
16. **04-11 (unlabeled lambda columns), Tab 7 Table 23** — named the two quantile aggregation
    functions (`q25`/`q75`) via `__name__` instead of letting pandas emit `<lambda_0>`/`<lambda_1>`.
17. **04-12 (undisclosed PercentileBin dropna), Tab 7 Figures 21/22** — added an explicit
    "N of M rows lack a percentile bin and are excluded" caption.

## 6. Tab 13 — full rebuild (per brief item 4)

Deleted wholesale (not weakened, not kept behind a flag):
- **Section A** (National PLE Benchmark, positional `.rolling(5)` over NMAT-admission years used as
  a proxy for the PRC's actual PLE-administration-year benchmark — 04-03/04-04).
- **Section B** (Per-HEI PLE Performance, ✅/🔴 verdicts keyed on `UNDERGRAD_UNIVERSITY` — 04-05,
  04-08, the RC-4 flagship misattribution).
- **Section D** (Foreign Student 10-Slot Cap applied retroactively to 2006-2018 test-taker counts
  against a rule effective AY2026-2027, counting test-takers as if they were enrolled freshmen —
  04-06).
- **Section E**'s per-institution "PLE pass rate (observable)" KPI (same RC-4 issue as Section B).

Replaced with:
- An expander, open by default, titled "What this dataset CAN and CANNOT tell CHED" — explicit
  bullet lists of what's supportable (applicant-pool distributions vs. thresholds, foreign/Filipino
  composition, individual-level linkage gradient) and not supportable (per-institution PLE
  performance, the CMO's 5-year national benchmark, GIDA/IP, enrolment/the foreign cap, composite
  admission ranking), each with the specific reason drawn from the audit (RC-4, no PRC pass-rate
  series, no equity fields, test-takers != enrollees, no GWA/interview data).
- **Section A (new): Applicant-Pool Cut-off Scenarios** — the old Section C's 30th-vs-40th
  cut-off table, fixed for 04-07's cohort mismatch (both the "admitted" count and the "PLE linkage"
  count now come from the same observable-cohort window, instead of mixing all-years-admitted
  against observable-only-linked in one row) and relabeled "PLE linkage rate," not "pass rate." The
  old `_benchmark_val` hline (which depended on the deleted Section A) was removed.
- **Section B (new): Foreign vs. Filipino Applicant-Pool Composition** — a bin-composition
  stacked-bar + table, one of the three explicitly-named supportable analyses, not previously
  present on this tab (it existed only nested inside Tab 4's citizenship deep-dive).
- **Section C (new): Individual-Level PLE Linkage Gradient by Percentile Bin** — the linkage-rate-
  by-bin table/chart, the second explicitly-named supportable analysis.

## 7. Mid-task correction from the orchestrator (matcher fix) — addressed

While I was working, the orchestrator found and fixed a real bug in the upstream PLE matcher (a
hard filter that discarded below-40th-percentile name-collision candidates) and re-ran the pipeline.
This changed the linkage-by-bin gradient from a sharp step at B4->B5 to a smooth rise, and changed
`IS_PLE_PASSER` from 49,986 to 49,086. Consequences I addressed:
- Removed all "selection-effect" / "40th-percentile admission floor causes a sharp jump" narrative I
  had written into Tab 13 (three locations: the CAN/CANNOT panel bullet, a `st.warning` box in
  Section A, and a caption under Section C's chart) — that finding no longer holds and would have
  been actively misleading if left in.
- Replaced it with the corrected framing (steady gradient, no sharp step) and surfaced the
  orchestrator-supplied replacement finding instead: Section C's caption now states, **computed live
  from the dataframe, not hardcoded**, how many B1 (lowest-decile) examinees in the observable
  cohort are confirmed PLE passers (795 on the parquet at hand).
- Confirmed no other caption in the file hardcodes a PLE-passer-derived count; the one hardcoded
  numeric caption I wrote (the stored-mismatch "56,065 of 99,316 = 56.45%" reference) is
  independent of the matcher fix and was re-verified to still hold exactly on the final parquet.
- Added the `PLE_MATCH_OUTCOME`/`PLE_YEAR_UNCERTAIN` panel (§4 above) per the orchestrator's request.

## 8. Bug found via testing that the original audit did not flag

Running the file through `streamlit.testing.v1.AppTest` (see §9) surfaced a real, reproducible
PyArrow serialization failure in Table 3 (Tab 2): the "Count of rows" column mixed three plain
`int`s with a formatted `"NN.NN%"` string, which `pa.Table.from_pandas` cannot type-infer
(`ArrowInvalid: Could not convert '56.45%' with type str: tried to convert to int64`). Streamlit
silently auto-recovers from this (coerces the whole column to strings) so it was not visibly
breaking the page, but it was a real latent bug. Fixed by keeping "Count of rows" purely integer and
moving the mismatch rate to its own `st.metric()`.

## 9. Verification performed

```
./.venv/Scripts/python.exe -m py_compile streamlit_dashboard/main_dashboard/dashboard.py   -> OK (final pass, after all edits)
```

Headless functional test, run twice (before and after the orchestrator's mid-task parquet update),
using `streamlit.testing.v1.AppTest` (executes the full script including all 13 `with tabN:` bodies
in one headless pass — more rigorous than curling the HTML shell, which only fetches the static
page without ever running the script):
```
at = AppTest.from_file("streamlit_dashboard/main_dashboard/dashboard.py", default_timeout=180)
at.run()
at.exception   -> empty on both runs ("NO EXCEPTIONS - app ran clean")
```

Also ran the literal instruction from the brief: `streamlit run ... --server.headless true
--server.port 860{1,2}` in the background, waited for the "You can now view your Streamlit app"
banner, `curl`'d the root URL (HTTP 200 both times), grepped the server log for
Traceback/Error/Exception (none found either time), then killed the process. Note: a plain `curl`
only fetches Streamlit's static HTML shell and does not itself execute the Python script (execution
happens per browser/websocket session), so the `AppTest` run is the test that actually exercises
tab logic; the `streamlit run` pass is included because the brief asked for it explicitly and it
does confirm the server itself boots without an import-time exception.

Headline KPI cross-check against the orchestrator's final authoritative table, computed fresh from
`streamlit_dashboard/main_dashboard/NMAT_Exodus.parquet` (md5 `28b85ac53af13b4a2ef3ee93527c97c1`):

| Quantity | Expected | Actual | Match |
|---|---|---|---|
| Exam sittings | 178,927 | 178,927 | Yes |
| Unique examinees | 134,869 | 134,869 | Yes |
| Observable cohort (people) | 69,503 | 69,503 | Yes |
| Observable linkage rate | 45.44% | 45.44% | Yes |
| Confirmed PLE passers | 49,086 | 49,086 | Yes |
| Ambiguous PERSON_KEYs | 6,148 | 6,148 | Yes |
| Stored-total mismatch | 56,065/99,316 = 56.45% | 56,065/99,316 = 56.45% | Yes |
| Linkage by bin (B1..B10) | 11.6/22.7/29.3/36.0/45.6/50.4/53.6/55.0/61.6/71.0 | (verified identical) | Yes |

Removed-column sweep: zero hits for all six removed names (§2). Bare (unprefixed) occurrences of
the four renamed columns: zero.

## 10. Known gaps / things I did not fix

- **F06** (data-integrity checks obeying sidebar filters) — documented as a design trade-off, not
  fixed; see §5 item 10.
- I did not port any of these changes to `RShiny_Dashboard/NMAT_Shiny/app.R` or
  `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py` — those are explicitly out of my
  ownership per the brief ("you own `main_dashboard/dashboard.py` exclusively").
- The parquet changed twice during this task (schema grew 51 -> 52 -> 53 columns, and
  `IS_PLE_PASSER` changed value three times: 49,986 (original contract) -> 51,707 -> 49,086
  (final)). Every numeric claim in this log and in the dashboard's own captions is either computed
  live from the dataframe or was re-verified against the final md5 `28b85ac53af13b4a2ef3ee93527c97c1`
  file; nothing is pinned to an intermediate value.
- Did not address the pre-existing, file-wide `use_container_width` deprecation warning (Streamlit
  1.56 wants `width=` instead) — out of scope for this remediation and present in effectively every
  `st.dataframe`/`st.plotly_chart` call in the file; a mechanical follow-up, not a correctness bug.
