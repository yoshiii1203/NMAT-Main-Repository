# Implementation Plan: One-Click Complete Markdown Export

## Objective

Add a **single Streamlit download button** to `dashboard.py` that generates one complete Markdown document mirroring the entire dashboard.

The downloaded file must include **all six tabs**, including content that is normally hidden inside:

- inactive tabs;
- collapsed `st.expander()` blocks;
- scrollable `st.dataframe()` tables;
- Plotly hover labels; and
- charts whose values are not fully visible in PDF export.

The output must be generated from the Python DataFrames and calculations—not by scraping the Streamlit interface, a browser, PDF, or screenshots. This ensures that every chart and table value is included accurately.[^1]

***

## Deliverables

Create:

```text
export_markdown.py
```

Modify:

```text
dashboard.py
```

The resulting download should be named:

```text
CHED_NMAT_Dashboard_Complete.md
```


***

## Required Architecture

### 1. Keep the exporter separate

Do not place hundreds of Markdown-export lines directly inside `dashboard.py`.

Create a new module:

```text
export_markdown.py
```

This module will contain all helper functions and section-specific exporters.

`dashboard.py` should only:

1. import the export function;
2. call it after all core DataFrames are prepared; and
3. display one `st.download_button()`.

***

## Required Function Interface

The module must expose this public function:

```python
def build_full_markdown(
    df_all: pd.DataFrame,
    df_best: pd.DataFrame,
    df_obs: pd.DataFrame,
) -> str:
    """
    Return one complete Markdown string representing all dashboard tabs.
    """
```

It must use the same data subsets and calculation rules as the rendered dashboard:

- `df_all`
- `df_best`
- `df_obs`
- best-record logic
- observable cohort logic
- B1–B10 ordering
- B4+, B5+, top-bin, and bottom-bin definitions
- `HAS_CONFIRMED_PLE`
- recalculated TRUE raw-score fields

The export must not load `NMAT_Exodus.parquet` again. It must work from the DataFrames already loaded into memory by the dashboard.[^1]

***

## Required Helpers

Implement the following reusable helpers inside `export_markdown.py`.

### DataFrame-to-Markdown helper

```python
def df_to_markdown(df: pd.DataFrame, index: bool = False) -> str:
```

Requirements:

- Make a copy before formatting.
- Convert nullable values to blank strings or `—`.
- Format integer counts with commas.
- Format percentage columns consistently, preferably one decimal place unless the dashboard uses two.
- Format float values consistently.
- Preserve the visible table-column order used in the dashboard.
- Use `DataFrame.to_markdown()` if `tabulate` is installed.
- Include a safe fallback table renderer if `tabulate` is unavailable.
- Never truncate rows or columns.
- Never replace values with placeholders such as “See dashboard table.”


### Markdown section helpers

Create simple utilities such as:

```python
def h1(text: str) -> str:
def h2(text: str) -> str:
def h3(text: str) -> str:
def paragraph(text: str) -> str:
def note(text: str) -> str:
def metric_table(rows: list[tuple[str, str]]) -> str:
def chart_block(title: str, description: str, df: pd.DataFrame) -> str:
```

`chart_block()` must include:

1. the chart title;
2. a short source/axis/series description;
3. the exact DataFrame used by the chart; and
4. any chart-specific caption.

Markdown cannot reproduce interactive Plotly visuals directly, so the underlying source table is the authoritative Markdown representation.

***

## Document Header

The exported file must begin with:

```markdown
# NMAT Performance Evidence for CHED Cut-Off Policy Review

> Complete Markdown export generated from the dashboard’s underlying
> computations and data tables. This document mirrors all six dashboard tabs.
```

Then include:

- dashboard scope statement;
- “How to read this dashboard” content;
- definitions of best-record examinees;
- observable cohort;
- score bins;
- NMAT-to-PLE-passer linkage warning;
- foreign-examinee scope warning; and
- TRUE raw-score correction statement.

Use exactly the same wording as the dashboard where possible.

***

# Required Tab Order

The Markdown document must follow this exact order:

```markdown
# Tab 1 — National Profile
# Tab 2 — B4+ vs B5+ Thresholds
# Tab 3 — PLE-Passer Linkage
# Tab 4 — Institution and Foreign Context
# Tab 5 — Key Evidence for Policy Review
# Tab 6 — Data, Methods, and Limitations
```

Do not omit any subsection, caption, metric, chart source table, or methodological note.[^1]

***

## Tab 1: National Profile

Export all of the following.

### National NMAT Profile and Coverage

Include a metric table containing:

- Best-record examinees
- Unique persons (`PERSON_KEY`)
- NMAT years covered
- Median percentile rank


### Annual Trend Chart Data

Export the full `yearly_summary` DataFrame used for the two-panel chart:


| Year | Examinees | Median percentile rank | Median TRUE raw score |
| :-- | --: | --: | --: |

Include the title and caption for:

- Examinee Volume by Year
- Median Bin Rank by Year


### University Type Composition

Export the exact `uni_dist` DataFrame:


| UNI_TYPE | Count | Share (%) |
| :-- | --: | --: |

Do not export only the pie-chart labels; include count and calculated share.

### Course Group Composition

Export the exact `course_dist` DataFrame:


| CourseGroup | Count | Share (%) |
| :-- | --: | --: |

### Repeat-Taker Context

Include:

- unique examinees;
- unique repeat takers;
- repeat-taker percentage;
- maximum attempts; and
- the dashboard explanation that threshold analyses use best-record attempts.


### Score Bin Reference

Export the full B1–B10 reference table:


| Bin | Score Range | Threshold |
| :-- | :-- | :-- |
| B1 | 0-9 |  |
| ... | ... | ... |
| B4 | 30-39 | CMO exception floor (B4+) |
| B5 | 40-49 | SUC standard floor (B5+) |
| ... | ... | ... |


***

## Tab 2: B4+ vs B5+ Thresholds

### Score Bin Distribution by NMAT Year

Export the complete heatmap source table:


| Year | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | B10 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |

Values must be row percentages and must include **every year in the dataset**.

Include:

- heatmap title;
- “Darker red = higher concentration” caption; and
- an explicit note that rows are NMAT years and columns are score bins.


### Examinees Meeting Each Threshold

Export the exact threshold scenario table:


| Threshold | Best-record examinees | Share of all (%) | Observable cohort size |
| :-- | --: | --: | --: |
| B4+ | ... | ... | ... |
| B5+ | ... | ... | ... |
| B4 only | ... | ... | ... |

### Threshold Context by University Type

Export the complete calculated table for every available category:


| University Type | Best-record examinees | B4+ count/share | B5+ count/share | B4-only count/share |
| :-- | --: | --: | --: | --: |

Include Public, Private, Foreign, and Not Specified if present.

### Public School Examinees and B5+

Export:

- all three metric cards;
- the Public-versus-Private evidence table;
- the section caption and caveat that `UNI_TYPE` is undergraduate institution type, not necessarily medical-school admission/enrollment; and
- the GIDA/IP data-availability caveat.


### Profile of B4 Group

Export:

- B4 examinee count;
- B4 median TRUE raw score;
- Public institution share of B4;
- exact `b4_by_uni` table; and
- the source data for the B4 institution-type bar chart.


### Top Bins Versus Bottom Bins Trend

Export the full source table:


| Year | Top B8-B10 (%) | Bottom B1-B3 (%) | Difference (pp) |
| :-- | --: | --: | --: |

### Yearly Threshold Counts

Export every year:


| Year | Total best-record | B4+ count | B4+ share | B5+ count | B5+ share | Observable B4+ | Observable B5+ |
| :-- | --: | --: | --: | --: | --: | --: | --: |

### B5+ PLE-Passer Composition by Year

Export the exact yearly source table for both stacked charts:


| Year | Total B5+ observable | Confirmed PLE passers | No confirmed PLE match | Confirmed linkage rate (%) | No-confirmed-match share (%) |
| :-- | --: | --: | --: | --: | --: |

Include both chart titles:

- B5+ Examinees by PLE Status (Count)
- B5+ Examinees by PLE Status (Percent)

Do not call this a PLE pass rate.

***

## Tab 3: PLE-Passer Linkage

### Linkage by Score Bin

Export the full `ple_bin` table:


| Score Bin | Range | N observable cohort | Confirmed PLE passers | Linkage Rate (%) |
| :-- | :-- | --: | --: | --: |

Include B1 through B10 even if a bin has zero rows.

### Score Profile by PLE Status

Export the complete descriptive-statistics table for:

- No confirmed PLE match
- Confirmed PLE passer

And for each available score field:

- Total TRUE raw score
- NMAT percentile rank
- Part I TRUE raw score
- Part II TRUE raw score

Keep all statistics currently shown:

- count
- median
- mean
- Q25
- Q75


### Linkage by NMAT Year

Export:


| Year | N | Confirmed PLE passers | Linkage Rate (%) |
| :-- | --: | --: | --: |

### Linkage by Course Group

Export:


| Course Group | N | Confirmed PLE passers | Median percentile | Linkage Rate (%) |
| :-- | --: | --: | --: | --: |

### Linkage by University Type

Export:


| University Type | N | Confirmed PLE passers | Median percentile | Linkage Rate (%) |
| :-- | --: | --: | --: | --: |

Retain the dashboard’s caveat that observed differences do not establish reasons or causes.

### Clean PLE Matching Stress Test

Export all criteria and results:

- one best NMAT record per person;
- clean deterministic PLE match;
- NMAT-to-PLE gap of at least five years;
- Filipino nationals only;
- B5+ restriction where applicable.

Export metric cards:


| Metric | Value |
| :-- | --: |
| Clean subset, all bins | ... |
| B5+ in clean subset | ... |
| Share of observable cohort | ... |
| Median PLE year gap | ... |

Export the complete yearly clean-subset data:


| Year | Total clean B5+ | Confirmed PLE passers | No confirmed match | Linkage Rate (%) |
| :-- | --: | --: | --: | --: |

Export the clean B5+ university-type distribution:


| University Type | N | Share (%) |
| :-- | --: | --: |

Do not overstate this section as proof of actual PLE pass rates.

***

## Tab 4: Institution and Foreign Context

### Score Summary by University Type

Export the exact `uni_score` table:


| University Type | N best record | Median percentile | Q25 | Q75 | Median TRUE raw score | Median GPS |
| :-- | --: | --: | --: | --: | --: | --: |

### Box Plot Source Data

Do not export all individual person-level records.

Instead, export a grouped five-number summary for each university type:


| University Type | N | Minimum | Q25 | Median | Q75 | Maximum |
| :-- | --: | --: | --: | --: | --: | --: |

This is the correct Markdown equivalent of the percentile box plot.

### Score Bin Distribution by University Type

Export the complete heatmap matrix:


| University Type | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | B10 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |

Values must be row percentages.

### Top-Bin Share by University Type

Export:


| University Type | Total Examinees | Top B8-B10 (%) | Top B8-B10 Count |
| :-- | --: | --: | --: |

### Foreign Examinee Context

Export all three metric cards:


| Metric | Value |
| :-- | --: |
| Verified foreign NMAT examinees, all records | ... |
| Filipino examinees | ... |
| Distinct foreign nationalities | ... |

Export the full Top 10 nationalities table:


| Rank | Nationality | Count | Share of verified foreign examinees (%) |
| --: | :-- | --: | --: |

Keep the limitation that these are NMAT examinees, not enrolled medical students.

***

## Tab 5: Key Evidence for Policy Review

Export the displayed policy-review text as Markdown exactly in the dashboard sequence:

1. National Threshold Context
2. Institutional Performance Patterns
3. NMAT-to-PLE-Passer Linkage Gradient
4. Historical Linkage Trends
5. Public School Threshold Attainment
6. PLE Matching Robustness
7. Foreign Examinee Presence
8. Note on data scope

This tab is narrative-only. Do not introduce new analysis, recommendations, or compliance labels.

***

## Tab 6: Data, Methods, and Limitations

Export all content in the same order as the dashboard.

### Dataset Overview

| Item | Value |
| :-- | :-- |
| Source file | ... |
| Examination years | ... |
| Unique examinees, best record | ... |
| Observable PLE cohort | ... |
| Repeat takers | ... |

### TRUE Raw Score Recalculation

Include the explanation and:


| Metric | Value |
| :-- | --: |
| Rows with complete TRUE scores | ... |
| Formula mismatches | ... |

### Best-Record Deduplication

Include both selection rules:

- PLE passer: matched NMAT attempt
- Others: highest percentile attempt, latest year as tie-breaker


### Observable Cohort Definition

| Metric | Value |
| :-- | --: |
| Observable best-record cohort | ... |
| Median NMAT-to-PLE year gap | ... |

### Deterministic PLE Matching

Include all matching caveats and:


| Metric | Value |
| :-- | --: |
| Confirmed PLE passers, all rows | ... |
| Confirmed PLE passers, best record observable | ... |
| Clean subset, B5+ Filipino with >=5-year gap | ... |

### Data Integrity Summary

| Metric | Value |
| :-- | --: |
| Stored-versus-derived mismatches | ... |
| Calculated-versus-derived mismatches | ... |

### Limitations

Include every limitation section currently displayed:

- PLE Outcomes
- GIDA and IP Status
- Medical School Admissions and Enrollment
- Foreign Student Enrollment Cap
- Composite Ranking for Foreign Applicants
- PHEI Accountability and Sanctions

***

## Integration Into `dashboard.py`

After the dashboard has loaded data and prepared all required DataFrames, add:

```python
from export_markdown import build_full_markdown
```

Then place this near the page header or at the bottom of the dashboard:

```python
with st.sidebar:
    st.divider()
    st.subheader("Export")
    st.caption(
        "Download a complete Markdown copy of all tabs, charts, "
        "tables, notes, and underlying chart data."
    )

    markdown_export = build_full_markdown(
        df_all=df_all,
        df_best=df_best,
        df_obs=df_obs,
    )

    st.download_button(
        label="Download Complete Dashboard (Markdown)",
        data=markdown_export,
        file_name="CHED_NMAT_Dashboard_Complete.md",
        mime="text/markdown",
        use_container_width=True,
    )
```

If the dashboard intentionally has no visible sidebar, use an `st.expander("Export Dashboard")` directly under the dashboard header instead. The export function should be independent of which tab is currently open.[^1]

***

## Validation Checklist

Before delivering, test the implementation locally.

- Start the dashboard normally.
- Click the Markdown download button without opening any tabs or expanders.
- Confirm the downloaded file is non-empty and opens as valid Markdown.
- Confirm all six tabs appear in the correct order.
- Confirm every visible `st.metric()` appears in the export.
- Confirm every `st.dataframe()` is present as a complete Markdown table.
- Confirm every heatmap has its full matrix in Markdown.
- Confirm every bar/line/pie/stacked chart has its exact source-data table.
- Confirm no data is lost because an expander was closed.
- Confirm no table is shortened with head/tail truncation.
- Confirm no placeholder text appears, including “See dashboard,” “available on hover,” or “not shown.”
- Confirm PLE figures are called **NMAT-to-PLE-passer linkage**, never PLE pass rates.
- Confirm no new policy recommendation, compliance label, eligibility conclusion, or unsupported inference was added.
- Confirm the dashboard still runs normally after adding the export feature.

<div align="center">⁂</div>

[^1]: https://www.perplexity.ai/search/f40eb071-1858-470e-b418-e6d29f1181c8

