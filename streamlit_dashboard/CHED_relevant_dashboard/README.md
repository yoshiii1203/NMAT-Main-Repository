# CHED NMAT Cut-Off Evidence Dashboard

Presentation-ready Streamlit dashboard for CHED stakeholders. Built from `NMAT_Exodus.parquet` (Pipeline 4 output, 178,927 records).

## Quick Start

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

## Dashboard Tabs

| Tab | Content |
|-----|---------|
| 1. National Profile | Examinee volume, university/course composition, annual trend |
| 2. 30th vs 40th Thresholds | Percentile distribution, B4+/B5+ counts, yearly threshold table |
| 3. Historical PLE-Passer Linkage | Linkage by percentile bin, year, course, university type |
| 4. Institution and Foreign Context | Score profiles by UNI_TYPE, foreign examinee profile |
| 5. Key Evidence for Policy Review | 5 synthesized findings from the data |
| 6. Data, Methods, and Limitations | Methodology, cohort definitions, documented limitations |

## Data

`NMAT_Exodus.parquet` (10.5 MB, 54 columns, 178,927 rows) — included in this repo.

## Deployment on Streamlit Cloud

1. Push this folder to a GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set main file path to `dashboard.py`
5. Deploy

The parquet file is already in the repo. No additional data setup needed.
