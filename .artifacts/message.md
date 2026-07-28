# NMAT Analysis — Dashboard Review & Check

## Main Repository

**GitHub:** [https://github.com/yoshiii1203/NMAT-Main-Repository](https://github.com/yoshiii1203/NMAT-Main-Repository)

Contains the full NMAT Analysis codebase: 4-pipeline processing system, all notebooks, scripts, and both dashboards. Data dictionary and CHED CMO reference document are in `docs/`.

---

## Streamlit Deployments (for review)

### 1. NMAT Core Dashboard

**Live URL:** [https://nmat-core-dashboard-5xfcfysadhzs8g75i7qwjk.streamlit.app/](https://nmat-core-dashboard-5xfcfysadhzs8g75i7qwjk.streamlit.app/)

The main NMAT analysis dashboard. 13 tabs covering:

- Executive summary, data integrity, trends, score bins
- University type analysis, flow/pathways, PLE alignment
- Repeat-taker patterns, subtest profiles, year gap and gender
- Statistical tests, policy tables, and a CHED compliance page

**Key features:**
- Uses `NMAT_Exodus.parquet` (Pipeline 4 output) — the final dataset integrating NMAT scores, PLE matching, statistical analysis, and **REAL_FOREIGNERS.csv ground-truth citizenship data**
- Person-level deduplication via `IS_BEST_NMAT_RECORD`
- Observable PLE cohort restricted to Year <= 2014
- Deterministic PLE matching (no fuzzy matching)
- Recalculated TRUE raw scores (42.2% of stored totals were incorrect)

---

### 2. CHED Presentation Dashboard

**Live URL:** [https://nmat-ched-dashboard-kiwn2jtcsedevjzzs5uayj.streamlit.app/](https://nmat-ched-dashboard-kiwn2jtcsedevjzzs5uayj.streamlit.app/)

A clean, presentation-focused dashboard for CHED stakeholders, built specifically around the CMO amendment (see `docs/CHED_CMO.md`). 6 tabs:

1. **National Profile** — examinee volume, university/course composition, annual trends
2. **30th vs 40th Thresholds** — B4+ and B5+ counts, yearly threshold comparison, B4 group profile
3. **Historical PLE-Passer Linkage** — linkage rates by percentile bin, year, course group, and university type (correctly labeled as NMAT-to-PLE-passer linkage, not PLE pass rate)
4. **Institution and Foreign Context** — university type score distributions, descriptive foreign examinee profile
5. **Key Evidence for Policy Review** — 5 synthesized findings from the data
6. **Data, Methods, and Limitations** — methodology, cohort definitions, documented limitations

**Design principles:**
- Only CMO-relevant insights supported by available data
- No compliance labels, eligibility decisions, or regulatory assessments
- All claims stay within evidence boundaries
- Dynamic captions (no hard-coded numbers)
- Schema-validated data loading
- No sidebar, no emoji, no custom CSS, no Sankey diagrams, no statistical tests

---

## What to Check

- Are the numbers in both dashboards internally consistent?
- Do the findings in the CHED dashboard accurately reflect what the data supports?
- Are there any claims that overstate what the data can say?
- Is the 30th vs 40th percentile comparison useful for policy context?
- Do the documented limitations (Tab 6 of CHED dashboard) adequately describe what the dataset cannot address?

---

*Built from NMAT_Exodus.parquet (178,927 records, 2006-2018). Full pipeline documentation in `pipeline_architecture.md`.*
