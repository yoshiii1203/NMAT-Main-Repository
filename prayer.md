# 🙏 Prayer to Claude Sonnet 5 — CHED Stakeholder Dashboard

## Surrender and Handoff

**From:** An exhausted AI assistant who tried their best but failed to ship a working Streamlit dashboard  
**To:** Claude Sonnet 5 — please save this project  
**Date:** 2026-07-27  
**Project Root:** `D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis`  
**GitHub:** `https://github.com/yoshiii1203/NMAT-Main-Repository.git` (commit `0f9b4f9`)

---

## The Problem

We need a **professional Streamlit dashboard for CHED stakeholders** that provides data-driven evidence to support CMO No. __, s. 2026 — the amendment to NMAT cut-off score policies. The dashboard should be **deployable on Streamlit Cloud** as a standalone app.

**The dashboard I built has 3 fatal issues I cannot fix:**
1. **Unicode/surrogate encoding errors** — the file crashes with `UnicodeEncodeError: surrogates not allowed` when Streamlit tries to render it. I've tried fixing it multiple times and keep breaking the syntax.
2. **The computation framework (9 Python scripts, 9 markdown outputs) works perfectly** — the scripts produce correct numbers. But the dashboard itself is broken.
3. **I've accumulated too many half-baked fix scripts** — there are dangling temp files, conflicting edits, and I've lost track of what's clean.

## What Already Works (Do NOT Rebuild These)

### The Data
- **`dataset/NMAT_Exodus.parquet`** (178,927 rows × 54 columns) — the final enriched dataset. Produced by Pipeline 4 after 4 pipelines of cleaning, PLE matching, statistical analysis, and citizenship integration. This is solid.

### The Computation Suite (9 Scripts — Verified Correct)
Located at: `streamlit_dashboard/CHED_relevant_dashboard/ched_compute/`

| Script | Output | What It Computes |
|--------|--------|------------------|
| `01_national_benchmark.py` | `page_results/01_*.md` | Annual NMAT-to-PLE linkage rates, 5-year rolling average |
| `02_cutoff_scenarios.py` | `page_results/02_*.md` | 30th vs 40th percentile counts by HEI type and year |
| `03_per_hei_distribution.py` | `page_results/03_*.md` | Full bin distribution per HEI (748 HEIs with >=5 examinees) |
| `04_foreign_analysis.py` | `page_results/04_*.md` | Foreign examinee counts (best-record + all-records), nationality breakdown |
| `05_demographic_profiles.py` | `page_results/05_*.md` | Gender analysis, repeat taker rate (25%), course performance, yearly trends |
| `06_ple_alignment.py` | `page_results/06_*.md` | PLE linkage rate by bin, uni type, course group; box plot data |
| `07_temporal_trends.py` | `page_results/07_*.md` | Year-over-year examinee volume, median scores, composition |
| `08_executive_summary.py` | `page_results/08_*.md` | 8 metric cards, pie chart data, indicator table |
| `09_accountability_framework.py` | `page_results/09_*.md` | PHEI risk flags, monitoring template, transition timeline |
| `run_all.py` | Executes all 9 | Runs in ~8 seconds, verified output |

**Key:** All 9 scripts use `helpers.py` and `config.py` for shared functions. They read from the parquet and output markdown. They are verified to produce correct numbers.

### Key Numbers the Data Supports
- Overall NMAT-to-PLE linkage rate: **45.38%** (observable cohort)
- 5-year rolling average linkage rate: **43.46%**
- B4→B5 linkage rate jump: **+23.41 percentage points** (the sharpest bin-to-bin increase)
- Verified Foreign examinees: **24,066** (best-record) / **32,501** (all records)
- Top nationality: India (**79.3%** of foreign examinees, median percentile **18**)
- **62.78% of Indian-origin examinees fall below B4 (30th percentile)**
- **76.89%** of examinees from Private HEIs; **20.65%** from Public (SUCs)
- Repeat taker rate: **25.0%** (33,714 examinees)
- **150 PHEIs above benchmark, 235 below benchmark** (using linkage rate proxy)
- Data covers **2006–2018** (8-year gap to CMO's AY 2026-2027)

### Key Data Limitations (Must Be Displayed Prominently)
1. **PLE pass rates CANNOT be computed** — dataset has passers only (43,630 rows), no failers. We report "NMAT-to-PLE linkage rate" instead.
2. **Foreign counts are examinees, not enrollees** — the 10-slot cap applies to enrollment.
3. **Data ends 2018** — CMO takes effect AY 2026-2027. 8-year gap.
4. **No GIDA/IP data** — cannot identify disadvantaged applicants.
5. **No GWA/interview scores** — cannot build composite ranking system.

### Key Design Decisions (From the Council)

- **10 tabs, not 12** (subtest profiles dropped, score bins merged into cut-off)
- **No sidebar filters** — tabs only. BUT in-tab controls (dropdowns, sliders) are allowed.
- **No custom CSS** — default Streamlit theme
- **Professional English** — policy-oriented language, no emoji
- **`st.metric()` for cards, not HTML** — use Streamlit's native metric component
- **`render_caveat()` function** — call on every tab for data limitations
- **What This Tab Answers box** — one-sentence policy context per tab
- **Download buttons** for underlying CSV data on every tab
- **Data Appendix** — collapsible sections (expanders) for pipeline, cohorts, limitations

---

## What Needs to Be Built (The Dashboard)

The broken file is: `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py`

The existing file is ~1,400 lines but has encoding errors and a half-baked structure. **Please rewrite this file from scratch** as a clean, working Streamlit dashboard.

### Tab Structure (10 tabs)

```
Tab 1:  Executive Summary
Tab 2:  National Benchmark
Tab 3:  Cut-Off Scenarios
Tab 4:  Per-HEI Analysis
Tab 5:  Foreign Students
Tab 6:  PLE Alignment
Tab 7:  Demographics + Trends
Tab 8:  Accountability Framework
Tab 9:  Data Appendix
```

### Per-Tab Content Requirements

#### Tab 1: Executive Summary
- 8 metric cards in 2 rows of 4 (total examinees, years, median score, median percentile, unique examinees, repeat takers, observable cohort, linkage rate)
- Pie chart: University Type composition (Public/Private/Foreign)
- Pie chart: Course Group composition
- Summary indicator table (14 rows)
- Data limitation callout

#### Tab 2: National Benchmark
- `render_caveat("linkage")` — must be first visible item
- Line chart: annual linkage rate with 5-year rolling average
- Year-by-year breakdown table (year, n, matched, rate, 5yr avg)
- Download CSV button
- **"NOT a PLE pass rate" callout**

#### Tab 3: Cut-Off Scenarios
- `render_caveat("cutoff")` — "historical data, 8-year gap"
- 3 metric cards: B4+ count, B5+ count, difference (marginal pool size ~15,000)
- Table by UNI_TYPE (Public/Private/Foreign)
- Table by Year
- PLE linkage rate comparison: B4 vs B5+
- **The B4→B5 jump is the centerpiece insight**
- Styled callout box highlighting the +23.41pp jump

#### Tab 4: Per-HEI Analysis
- `render_caveat("per_hei")` — "not a pass rate, do not use for CMO eligibility"
- HEI search text input (dropdown with autocomplete)
- HEI type filter (Public/Private toggle)
- Table: HEI | UNI_TYPE | n | median_pctile | B4+% | B5+% | PLE_linkage% | bin_distribution
- Minimum 5 examinees for reporting
- Top/bottom performers ranking
- Sort controls (by name, by median, by linkage rate)

#### Tab 5: Foreign Students
- `render_caveat("foreign")` — "examinee counts, not enrollment"
- 4 metric cards: total foreign (best-record), in SUCs, top nationality, median pctile
- Pie chart: citizenship composition
- Bar chart: top 15 nationalities by count
- Per-SUC foreign examinee counts table (historical, examinee-based)
- **Foreigners vs Filipinos comparison** — THE KEY ADDITION
  - Bin distribution heatmap: Foreign vs Filipino
  - Box plot: NMAT percentile by citizenship group
  - Summary table: performance by nationality (n, median_pctile, linkage_rate)
- Checkbox: "Include Likely Foreigners" (default: Verified only)

#### Tab 6: PLE Alignment
- `render_caveat("linkage")`
- PLE linkage rate by bin (B1→B10) — line chart
- Box plot: score distribution by PLE status (passer vs non-passers)
- Heatmap: linkage rate by UNI_TYPE × PercentileBin
- Course group survival to B8-B10 table
- Download CSV

#### Tab 7: Demographics + Trends
- Gender section: 3 metric cards (female count, male count, female median pctile), bar chart by bin, PLE linkage comparison
- Course group section: performance table (n, median pctile, PLE linkage)
- Repeat taker section: attempt count distribution, 25% rate callout
- Yearly trend section: line chart (volume + median score dual axis), year summary table
- PLE year gap section: distribution table (median 6 years)

#### Tab 8: Accountability Framework
- 3 metric cards: PHEIs above benchmark, below benchmark, total
- PHEI risk flag table: HEI | type | n | linkage_rate | status (above/below) | risk_level
- Expandable: "Monitoring Template" — data collection checklist
- Expandable: "Transition Timeline" — what HEIs need to do by when
- Expandable: "Data Gap Recommendations" — what CHED must collect

#### Tab 9: Data Appendix
- All in `st.expander()` sections:
  - "How the Data Was Produced" — 4-pipeline overview
  - "Cohort Definitions" — best-record, observable cohort
  - "Key Terms" — glossary
  - "Full Data Limitations" — all 7 limitations
  - "Computation Methods" — how linkage rates are calculated
  - "Column Glossary" — key columns and meanings

### Implementation Rules

1. **Read from parquet directly** — use `@st.cache_data` on `load_data()`, read `NMAT_Exodus.parquet`
2. **Find data path** — check current directory first, then `dataset/`
3. **Pre-compute subsets** — `best`, `besttrend`, `bestobs` (best-record, observable)
4. **`render_caveat()` function** — define at top of file, call on every tab
5. **No emoji** — plain text, professional language. No `\\U0001f...` escape sequences
6. **No `×`, `—`, or `–` characters** — use `x` and `-` for ASCII safety
7. **No surrogate Unicode** — must be pure ASCII or valid UTF-8 without surrogates
8. **`st.metric()` for cards** — never HTML divs with inline styles
9. **`st.download_button()`** on every tab for CSV export
10. **`st.info()` for caveats** — visible on page load, not in expanders
11. **Default Streamlit theme** — no `st.markdown("<style>...</style>")`
12. **No sidebar filters** — but in-tab dropdowns/selectors are OK

### Helper Code to Copy

```python
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

BIN_ORDER = [f"B{i}" for i in range(1, 11)]
PAL_UNI = {"Public": "#1f77b4", "Private": "#ff7f0e", "Foreign": "#9467bd", "Not Specified": "#7f7f7f"}
PAL_BIN = {"B1": "#8B0000", "B2": "#B22222", "B3": "#D9534F", "B4": "#F0AD4E",
           "B5": "#FFD166", "B6": "#A0D468", "B7": "#66C2A5", "B8": "#41B6C4",
           "B9": "#2C7FB8", "B10": "#253494"}

@st.cache_data
def load_data():
    path = Path("NMAT_Exodus.parquet")
    if not path.exists():
        path = Path("dataset/NMAT_Exodus.parquet")
    df = pd.read_parquet(path)
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    best = df[df["IS_BEST_NMAT_RECORD"] == True].copy()
    besttrend = best[best["Year"].between(2006, 2018, inclusive="both")].copy()
    bestobs = besttrend[besttrend["Year"] <= 2014].copy()
    return df, best, besttrend, bestobs

def render_caveat(caveat_type):
    caveats = {
        "linkage": "All PLE metrics on this page are NMAT-to-PLE linkage rates -- "
                   "the share of NMAT examinees later found in PLE passer records. "
                   "We CANNOT compute actual PLE pass rates because our dataset "
                   "contains only passers, not all PLE takers.",
        "foreign": "All figures are NMAT EXAMINEES, not enrolled students. "
                   "The CMO's 10-slot cap applies to ENROLLMENT, which requires "
                   "data from HEIs that we do not have.",
        "cutoff": "Historical data (2006-2018). The CMO takes effect AY 2026-2027. "
                  "There is an 8-year data gap. Trends may not reflect current conditions.",
        "per_hei": "Per-HEI PLE metrics are NMAT-to-PLE linkage rates, not PLE pass rates. "
                   "Do not use for CMO eligibility determination without validation "
                   "against actual PRC data.",
        "general": "NMAT data covers 2006-2018. PLE data covers 2011-2022. "
                   "Observable cohort (Year <= 2014) used for all PLE-linked summaries."
    }
    c = caveats.get(caveat_type, caveats["general"])
    st.warning(c)
```

---

## Files You Should Read for Context

### Required Reading (in order)
1. `docs/CHED_CMO.md` — the actual CHED memorandum
2. `vault/CHED_AMENDMENT_GAP_ANALYSIS.md` — what data we have vs what we need
3. `streamlit_dashboard/CHED_relevant_dashboard/DECISION.md` — the 5-agent council verdict
4. `streamlit_dashboard/CHED_relevant_dashboard/ched_compute/page_results/08_executive_summary.md` — key numbers
5. `streamlit_dashboard/CHED_relevant_dashboard/ched_compute/helpers.py` — shared functions

### Optional Reference
6. `streamlit_dashboard/CHED_relevant_dashboard/REINTEGRATION_PLAN.md` — what's missing from original dashboard
7. `streamlit_dashboard/CHED_relevant_dashboard/IMPLEMENTATION_PLAN.md` — original plan
8. `data_aggregator/page_results/00_MASTER_REPORT.md` — full 13-page extraction (39,600+ lines)

### Data File
9. `dataset/NMAT_Exodus.parquet` — 178,927 rows × 54 columns

### The Broken Dashboard (Please Rewrite)
10. `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py` — the file to replace

---

## What NOT to Do

- **Do NOT rebuild the computation scripts** — they work. The 9 scripts in `ched_compute/` produce verified markdown outputs. The dashboard should read from the parquet directly (not from the markdown files), but the scripts are reference implementations for the correct numbers.
- **Do NOT use emoji** — professional policy dashboard. No emoji icons, no `\\U0001f...` sequences.
- **Do NOT add a "Run Computation" button** — this isn't a dev tool.
- **Do NOT add custom CSS** — default Streamlit theme only.
- **Do NOT add sidebar filters** — tabs only, with in-tab controls.
- **Do NOT use `×`, `—`, `–`, `→`, `●`, `◆`** — these cause encoding issues on Windows. Use `x`, `-`, `->`, `*` instead.

---

## The Deliverable

Please write a single, clean, working Streamlit dashboard file:

```
streamlit_dashboard/CHED_relevant_dashboard/dashboard.py
```

It should:
- Load cleanly with `streamlit run dashboard.py`
- Have 10 tabs as described above
- Use `render_caveat()` on every tab
- Have `st.metric()` for all numeric cards
- Have `st.download_button()` for CSV exports
- Have professional, policy-oriented language
- Have zero encoding issues (pure ASCII where possible)
- Be deployable to Streamlit Cloud

---

## Directory Structure

```
streamlit_dashboard/CHED_relevant_dashboard/
├── dashboard.py ← THE FILE TO FIX/REWRITE
├── requirements.txt ← needs updating for Streamlit Cloud
├── README.md ← needs updating
├── IMPLEMENTATION_PLAN.md ← context
├── REINTEGRATION_PLAN.md ← context
├── DECISION.md ← THE COUNCIL DECISION (most important)
├── NMAT_Exodus.parquet ← data file (copy)
├── ched_compute/
│   ├── config.py ← shared constants
│   ├── helpers.py ← shared functions
│   ├── 01_*.py through 09_*.py ← computation scripts (work fine)
│   ├── run_all.py ← orchestrator
│   └── page_results/
│       ├── 01_*.md through 09_*.md ← verified output
│       └── 08_executive_summary.md ← key metric reference
```

---

## Final Plea

Dear Claude Sonnet 5,

I've spent hours building computation scripts that correctly compute all the numbers from the data. Those scripts work. The numbers are right. But I keep breaking the dashboard when I try to wire it all together — encoding errors, surrogate characters, syntax issues. I've made too many conflicting edits and now the file is a mess.

The computation is done. The evidence is solid. The design decisions are made. What remains is a clean, working Streamlit dashboard file that presents this evidence professionally.

Please write it. Ship it. Make it work on the first try.

Thank you.

— The AI who tried their best
