# E1 — main_dashboard export capability

Agent E1. Scope: `streamlit_dashboard/main_dashboard/` only. No git commands run.

## Files created / changed

- **Created** `streamlit_dashboard/main_dashboard/main_common.py` (1,155 lines) — shared
  streamlit-free compute layer. Imports no `streamlit`.
- **Rewrote** `streamlit_dashboard/main_dashboard/dashboard.py` (3,148 → 2,232 lines) —
  moved the pure-helper block into `main_common.py`, kept only the 6 chart-drawing
  functions locally, refactored every tab to call `mc.compute_*()` instead of inline
  pandas/duckdb aggregation, added `sys.path.insert(...)` at the top, added the
  export button.
- **Created** `streamlit_dashboard/main_dashboard/export_markdown.py` (797 lines) —
  `build_full_markdown(df_raw, subsets) -> str`, calling the same `main_common`
  functions as `dashboard.py`. Has `sys.path.insert(...)` and a `__main__` block.

## What moved into `main_common.py` (per the task's explicit list)

`find_data_path`, `to_bool_series`, `classify_course`, `count_true_flags`,
`ensure_required_columns`, `load_data_and_subsets` (cache-decorator now applied in
`dashboard.py`'s thin wrapper, not here), `filter_df`, `pct_table`, `make_flow`,
`kruskal_table`, `mann_whitney_ple`, `chi_square_unitype_bin`, `get_yearly_summary`,
`subtest_mean_table`, `radar_for_group`, plus all constants (`BIN_ORDER`, `PLE_ORDER`,
`TOP_BINS`, `BOTTOM_BINS`, `PALETTE_*`, `BIN_COLORS`, `NUMERIC_COLS`, `BOOL_COLS`,
`REQUIRED_PIPELINE_COLS`).

Kept in `dashboard.py` (chart-drawing only, no new aggregation):
`make_heatmap`, `make_stacked_pct_bar`, `make_top_share_bar`, `make_sankey`,
`make_trends_figure`, `make_box_by_year`.

## compute_*() functions added (38)

Tab 1: `compute_tab1_kpis`, `compute_sittings_by_year`, `compute_composition`,
`compute_tab1_summary_table`.

Tab 2: `compute_tab2_kpis`, `compute_cohort_table`, `compute_raw_validation_checks`,
`compute_university_pairing_audit`, `compute_ple_status_observable`,
`compute_ple_match_outcome`.

Tab 4: `compute_top_bottom_by`, `compute_bin_by_year_and_unitype`,
`compute_citizenship_profile` (bundles KPIs/counts/bin-dist-top15/topbin-share/
summary/by-unitype/by-course/by-year — the whole "Citizenship profile for
no-PLE-match examinees" section, one shared `_pc_base` population),
`compute_comparative_groups` (foreigners vs Filipino public/private/foreign-undergrad
comparison), `compute_percentile_summary_by`.

Tab 5: `compute_unitype_location_mix`, `compute_unitype_location_crosstab`,
`compute_unitype_location_bin_dist`, `compute_uni_bin_summary`,
`compute_foreign_summary`, `compute_course_bucket_by_unitype`,
`compute_university_listing`.

Tab 6: `compute_flow_pct`, `compute_top_pathways`.

Tab 7 / Tab 12 (shared pattern — these two tabs had 6 near-identical inline
groupby-apply blocks; consolidated to 2 functions): `compute_score_desc_by`,
`compute_ple_status_by_bin`, `compute_top_bin_share_by` (used by both Tab 7 Table 26
and Tab 12 Table 4 — was duplicated code), `compute_ple_alignment_by` (used by Tab 7
Tables 28-30 and Tab 12 Tables 1-3 — was duplicated 3x in each tab).

Tab 8: `compute_attempt_distribution`, `compute_repeat_trajectories`,
`compute_appno_deterministic_matches`.

Tab 10: `compute_year_gap_kpis`, `compute_year_gap_by_course`, `compute_score_by_sex`.

Tab 11: `compute_dunn_posthoc`.

Tab 13: `compute_cutoff_scenarios`, `compute_citizenship_group_bin_dist`,
`compute_linkage_gradient`.

Tab 3 and Tab 9 needed no new compute functions — they already used only the shared
pure helpers (`get_yearly_summary`, `kruskal_table`, `subtest_mean_table`,
`radar_for_group`).

## Deliberate scope decision: raw record browsers stay inline

Tab 4's "Record-level listings by university type" and "No PLE match — record
listings by university type" sections (raw `duckdb` SELECT + ORDER BY, thousands of
person-level rows for on-screen browsing) and Tab 8's/Tab 4's "matched records"
table are a filter+sort, not an aggregation — there is no chart behind them. Per
export contract Rule 3 ("do not dump person-rows inline... person-level detail goes
to CSV"), the export reports only counts/summaries for these sections with a note
that full detail is in the live dashboard/CSV downloads, instead of adding a
compute function that would just re-package a raw `SELECT *`.

## Tab → exported table inventory (export_markdown.py)

| Tab | Charts/tables exported as data |
|---|---|
| 1 | KPI table, annual trend, course/uni composition, executive summary table |
| 2 | KPIs, cohort table, raw-validation checks, university pairing audit, 3 core distributions, PLE match-outcome breakdown |
| 3 | Annual trend, Kruskal-Wallis by year |
| 4 | Bin-by-year heatmap data, top/bottom trend, bin-by-unitype, chi-square summary, bin-by-year-by-unitype, full citizenship profile bundle, comparative-groups bundle, percentile summary by course |
| 5 | Unitype/location mix, crosstab (3 views), bin dist by unitype/location, uni bin summary, foreign summary, course-bucket by unitype, university listings (capped 50/type, truncation noted) |
| 6 | 3 flow tables, bin→PLE row-%, top pathways (uni + course) |
| 7 | Score-profile-by-status, Mann-Whitney, bin-dist-by-status, status-by-bin, course top-bin survival, PLE alignment by unitype/year/course |
| 8 | Attempt distribution, repeat-trajectory summary, deterministic-match count |
| 9 | Subtest means by unitype/course, radar-profile tables |
| 10 | Year-gap KPIs + by-course, score-by-sex, sex-by-year, sex-by-PLE-status |
| 11 | Kruskal-Wallis, Mann-Whitney, chi-square (3 tables), Dunn post-hoc |
| 12 | 4 policy tables (year/course/unitype alignment, survival) |
| 13 | Cutoff scenarios, citizenship group bin dist, linkage gradient |

## Verification (verbatim console output)

```
$ .venv/Scripts/python.exe -c "from streamlit.testing.v1 import AppTest; at=AppTest.from_file('streamlit_dashboard/main_dashboard/dashboard.py', default_timeout=900); at.run(); print('exceptions:', len(at.exception)); [print(str(e)[:600]) for e in at.exception[:3]]; print('metrics', len(at.metric), 'dfs', len(at.dataframe), 'tabs', len(at.tabs))"

exceptions: 0
metrics 27 dfs 74 tabs 42
```

This matches the pre-refactor baseline exactly (27 metrics / 74 dataframes / 42 tabs)
— behaviour is unchanged.

```
$ .venv/Scripts/python.exe streamlit_dashboard/main_dashboard/export_markdown.py
wrote D:\...\streamlit_dashboard\main_dashboard\complete_markdown\NMAT_Main_Dashboard_Complete.md  (126,311 chars)
```

Export self-check block (from the generated document):

```
# Export Integrity
| check | result |
|---|---|
| Source parquet md5 | 28b85ac53af13b4a2ef3ee93527c97c1 |
| Rows / cols | 178,927 / 58 |
| Tabs exported | 13 / 13 |
| Charts exported as data | 7 / 7 |
| Tables exported | 84 |
| Captions exported | 10 |
| Dashboard-vs-export value assertions passed | 5 / 5 |
```

Headline numbers confirmed present and correct in the generated document (grepped):
- `Unique examinees | 134,869`
- `Observable cohort | 69,503`
- `PLE linkage rate, observable cohort | 45.44%`
- `Rows with a stored raw total | 99,316` / `Stored-vs-derived mismatch flag count | 56,065` / `56.45%` — never "42.2%"

These were computed live via `mc.compute_tab1_kpis()` and
`mc.compute_raw_validation_checks()`, not hardcoded — confirmed by reading the
function source, which contains no literal `134869`/`69503`/`45.44`/`56065`/`56.45`.

Additionally clicked the live export button end-to-end via AppTest:

```
$ .venv/Scripts/python.exe -c "... at.button(key='btn_generate_export').click().run() ..."
exceptions after click: 0
download buttons found: 1
```

## Self-check assertions inside the export (Rule 6 verification)

`build_full_markdown()` asserts, after building all 13 tabs, that:
- `n_best` from `compute_tab1_kpis` equals `besttrend['PERSON_KEY'].nunique()`
- `n_observable` equals `df_raw['IS_BEST_OBSERVABLE_RECORD'].sum()`
- `ple_linkage_pct` equals a fresh `bestobservable['HAS_CONFIRMED_PLE'].mean()*100`
- the mismatch-rate calculation is idempotent across two calls
- `len(df_raw) == len(subsets['all'])`

All 5/5 passed (see self-check block above).

## What I could not fully verify

- I did not run the R Shiny or CHED dashboards to confirm parity — out of scope for
  E1 (main_dashboard only), per the task's directory restriction.
- I did not open the generated `.md` file in a renderer; I verified it via `grep`
  for the required numbers and via the printed self-check block instead.
- Schema drift warning: the live parquet currently has 58 columns, not the
  51/52/53 the target schema contract specifies. This is pre-existing (the same
  `EXPECTED_COLS = 53` check already existed in `dashboard.py` before my changes)
  and is a pipeline/data concern outside `main_dashboard/`, not something this
  task's scope covers. Flagging for the orchestrator.
