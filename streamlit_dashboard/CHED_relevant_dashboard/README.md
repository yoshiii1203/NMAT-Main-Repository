# CHED NMAT Cut-Off Evidence Dashboard

Presentation-ready Streamlit dashboard for CHED stakeholders. Built from `NMAT_Exodus.parquet` (Pipeline 4 output, 178,927 records).

## Dashboard Tabs

| Tab | Content |
|-----|---------|
| 1. National Profile | Examinee volume, university/course composition, annual trend, bin reference table |
| 2. B4+ vs B5+ Thresholds | Score bin distribution, B4+/B5+ counts, yearly threshold table, B5+ PLE stacked chart, public school attainment evidence |
| 3. PLE-Passer Linkage | Linkage by score bin, year, course group, university type; clean PLE subset stress-test |
| 4. Institution and Foreign Context | Score profiles by UNI_TYPE, bin distribution, top-bin share, foreign examinee profile |
| 5. Key Evidence for Policy Review | 7 synthesized findings from the data |
| 6. Data, Methods, and Limitations | Methodology, cohort definitions, documented limitations |

## Quick Start

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

## Compute Scripts (`ched_compute/`)

The `ched_compute/` directory contains standalone Python scripts that replicate the dashboard's computations and output structured markdown reports. These serve as an offline verification layer and produce the `page_results/` markdown files.

### Structure

```
ched_compute/
├── config.py                 # Shared configuration (paths, bin definitions)
├── helpers.py                # Shared functions (data loading, subset creation, output writing)
├── run_all.py                # Orchestrator: runs all 6 scripts in sequence
│
├── 01_national_profile.py    # Tab 1: National profile + linkage
├── 02_thresholds.py          # Tab 2: B4+/B5+ threshold analysis
├── 03_ple_linkage.py         # Tab 3: PLE-passer linkage analysis
├── 04_institution_context.py # Tab 4: Institution & foreign context
├── 05_evidence_findings.py   # Tab 5: Key evidence findings
├── 06_data_limitations.py    # Tab 6: Data methods & limitations
│
├── page_results/             # Generated markdown reports (one per script)
│   ├── 01_national_profile.md
│   ├── 02_thresholds.md
│   ├── 03_ple_linkage.md
│   ├── 04_institution_context.md
│   ├── 05_evidence_findings.md
│   └── 06_data_limitations.md
│
└── verified_true/            # Verification outputs
    ├── CONSOLIDATED_VERIFICATION_REPORT.md
    ├── VERIFIER_streamlit_output_log_01.md ... 06.md
    └── verifier_01_national_profile.py ... 06.py
```

### Running Compute Scripts

```bash
cd ched_compute
python run_all.py             # Runs all 6 scripts, outputs to page_results/
```

Or run individually:

```bash
cd ched_compute
python 01_national_profile.py
python 02_thresholds.py
# ... etc
```

### What They Do

Each script loads `NMAT_Exodus.parquet`, performs the same computations as the corresponding dashboard tab, and writes a structured markdown report to `page_results/`. This enables:

- **Offline verification**: Compare page_results against live dashboard values
- **CI/CD validation**: Scripts can be run in CI to detect data drift
- **Documentation**: Generated markdown is human-readable and shareable

### Verified True Outputs

The `verified_true/` folder contains Python verifiers that cross-check page_results against direct parquet computations, plus their output logs and a consolidated verification report. Run any verifier to re-validate:

```bash
cd ched_compute/verified_true
python verifier_01_national_profile.py
```

## Data

`NMAT_Exodus.parquet` (10.5 MB, 54 columns, 178,927 rows) — included in this repo.

## Deployment

### Streamlit Cloud

1. Push this folder to a GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set main file path to `dashboard.py`
5. Deploy

### Hugging Face Spaces

1. Create a new Space at [huggingface.co/spaces](https://huggingface.co/spaces)
2. Choose **Streamlit** SDK
3. Push this folder as the Space content
4. The Space will auto-detect `requirements.txt` and `dashboard.py`

```bash
# Example: push to HF Space
cd streamlit_dashboard/CHED_relevant_dashboard
huggingface-cli upload <username>/<space-name> . .
```

## Requirements

```
streamlit>=1.25
pandas>=1.5
numpy>=1.24
pyarrow>=10
plotly>=5.15
```
