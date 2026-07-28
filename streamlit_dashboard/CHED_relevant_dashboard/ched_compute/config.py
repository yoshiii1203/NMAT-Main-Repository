"""
config.py — Constants, file paths, column definitions for CHED computation suite.
"""

import os

# ── Paths ──────────────────────────────────────────────────────────────────
ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
DATASET_DIR = ROOT_DIR
EXODUS_PATH = os.path.join(DATASET_DIR, "NMAT_Exodus.parquet")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "page_results")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── File helpers ───────────────────────────────────────────────────────────
def out_path(script_number: str) -> str:
    """Return full path for a script's markdown output file."""
    return os.path.join(OUTPUT_DIR, f"{script_number}.md")


# ── Column groups ──────────────────────────────────────────────────────────
NUMERIC_COLS = [
    "TotalRawScoreTRUE",
    "PartIRawScoreTRUE",
    "PartIIRawScoreTRUE",
    "Percentile_CEM",
    "NMS_PER_num",
    "NMS_SA",
    "NMS_APT",
    "NMS_GPS",
]

BIN_ORDER = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]
B4_PLUS = ["B4", "B5", "B6", "B7", "B8", "B9", "B10"]
B5_PLUS = ["B5", "B6", "B7", "B8", "B9", "B10"]
TOP_BINS = ["B8", "B9", "B10"]
BOTTOM_BINS = ["B1", "B2", "B3"]

UNI_TYPE_ORDER = ["Public", "Private", "Foreign", "Not Specified"]

# PLE observable cohort cutoff: examinees from Year <= 2014 have had
# enough time to take PLE (typical gap is 5+ years).
PLE_OBSERVABLE_MAX_YEAR = 2014

# ── Labels ─────────────────────────────────────────────────────────────────
LINKAGE_LABEL = "NMAT-to-PLE Linkage Rate"
EXAMINEE_LABEL = "Examinee Count"
FOREIGN_COUNT_LABEL = "Foreign Examinee Count"

# ── Data quality notes ─────────────────────────────────────────────────────
DATA_CAVEAT = """
> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).
"""

OBSERVABLE_CAVEAT = """
> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.
"""

def make_header(title: str, script_number: str) -> str:
    """Return a standard markdown section header."""
    return f"""# {title}

**Date:** {{date}}
**Data Source:** `NMAT_Exodus.parquet` (178,927 records)
**Script:** `ched_compute/{script_number}.py`

---
"""
