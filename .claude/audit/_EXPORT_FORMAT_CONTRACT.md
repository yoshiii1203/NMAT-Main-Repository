# EXPORT FORMAT CONTRACT — binding on all exporter agents

The user's stated purpose: *"upload all of them and analysis is easy as fuck."* The exported markdown
is **an analysis input for an LLM**, not a human-facing report. Optimise for that.

Applies to `main_dashboard/export_markdown.py` (new) and
`CHED_relevant_dashboard/export_markdown.py` (existing, to be brought into compliance).

---

## Rule 1 — Every visual becomes DATA, never an image

For **every** chart on **every** page, emit the **underlying dataframe as a markdown table**.
Images are optional and supplementary; the data table is mandatory and must be complete.

A bar chart, line chart, pie chart, box plot, heatmap, radar, Sankey or scatter is a *rendering* of a
table. Export the table. If a chart has 3 series x 13 years, the table has 39 rows (or 13 rows x 3
columns) — never a prose summary, never a picture, never a truncation.

**Box plots** must export the five-number summary plus n (min, Q1, median, Q3, max, n, outlier count)
per group — not raw points.
**Heatmaps** must export the full 2-D matrix with row and column labels.
**Sankey / flow** must export every source→target→value triple.
**Radar** must export each axis value per series.

## Rule 2 — Chart blocks carry machine-readable metadata

Precede each table with an HTML comment block so a downstream model knows exactly what it is:

```markdown
### Figure 7 — PLE Linkage Rate by Score Bin

<!-- chart_type: bar | x: PercentileBin | y: linkage_rate_pct | series: none
     population: observable cohort (Year<=2014), best-record only
     n: 68,746 | denominator: unique examinees with a percentile
     source_tab: 3 | element_id: ched_t3_fig1 -->

| PercentileBin | linked | n | linkage_rate_pct |
|---|---|---|---|
| B1 | 556 | 6,853 | 8.1 |
...
```

`population`, `n` and `denominator` are **mandatory on every table**. Most misreadings in this
project came from an unstated denominator — make it impossible.

## Rule 3 — No truncation without an explicit marker

Never silently `.head()`. If a table is capped, say so in the metadata
(`truncated: true | shown: 100 | total: 2,907 | full_csv: exports/data/t4_universities.csv`)
and write the complete data to an accompanying CSV. Prefer emitting the full table where it is under
~2,000 rows.

**Do not** dump ~33,700 person-rows inline (this produced an 8.7 MB file). Person-level detail goes
to CSV; the markdown carries the aggregate.

## Rule 4 — Every KPI is a row in a KPI table

```markdown
## KPIs

| metric | value | population | note |
|---|---|---|---|
| Unique examinees | 134,869 | all years, one row per person | — |
| Observable cohort | 69,503 | Year<=2014, unique people | >=5yr PLE window |
```

## Rule 5 — Narrative captions are exported verbatim

Every `st.caption`, `st.markdown` interpretation and finding text appears in the export **exactly as
the dashboard renders it**, including dynamically computed numbers. The export must be a faithful
transcript, not a paraphrase.

## Rule 6 — Numbers come from ONE shared compute layer

The exporter and the dashboard must call the **same** `compute_*()` function. Never reimplement an
aggregation in the exporter — that is root cause RC-5, which already produced a published 57/49 vs
56/48 discrepancy. If you find yourself writing a groupby in an exporter, stop and extract it.

**Verification requirement:** after generating, assert that a sample of exported values equals the
dashboard's computed values by calling the same functions. Record the assertion in your log.

## Rule 7 — Structure and file layout

```
<dashboard>/complete_markdown/
    <NAME>_Complete.md          # everything, one file, uploadable
    exports/data/*.csv          # full tables that were capped inline
    viz/*.png                   # optional supplementary images
```

Document structure:
1. Title + generation timestamp + source parquet md5 + row/col counts
2. **How to read this document** — the population definitions, the linkage-vs-pass-rate warning,
   the B1=lowest convention, people-vs-sittings
3. Global KPI table
4. One `# Tab N — <name>` section per tab, in dashboard order, containing every element in
   dashboard order
5. **Data limitations** section (carried from the dashboard verbatim)
6. Appendix: column dictionary for every column referenced

## Rule 8 — Terminology, enforced

- **"linkage rate"**, never "pass rate" — the PLE source contains passers only.
- **"NMAT-to-PLE-passer linkage"** on first use in each tab.
- `UNDERGRAD_UNIVERSITY` / `UNDERGRAD_UNI_TYPE` — always describe as the **undergraduate**
  institution. Never imply a medical school.
- Percentile bins ordered `B1..B10`, B1 lowest. Never string-sorted.
- Nationality shares against the full verified-foreigner denominator (32,501).

## Rule 9 — One click, no arguments

A single Streamlit button generates everything and offers a download. It must also be runnable
headlessly (`python export_markdown.py`) for CI. Both paths share one code path.

## Rule 10 — Self-check block at the end of every export

```markdown
## Export integrity
| check | result |
|---|---|
| Source parquet md5 | 8034a0... |
| Rows / cols | 178,927 / 52 |
| Tabs exported | 6 / 6 |
| Charts exported as data | 27 / 27 |
| Tables exported | 41 / 41 |
| Captions exported | 63 / 63 |
| Dashboard-vs-export value assertions passed | 27 / 27 |
```

If any count is short of its total, the export is incomplete — say so loudly in the document itself
rather than shipping a silent gap.
