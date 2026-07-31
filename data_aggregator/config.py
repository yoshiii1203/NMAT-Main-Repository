"""
Shared configuration for data extraction scripts.
All constants mirror dashboard.py definitions.
"""
from pathlib import Path

# Paths — anchored on this file's location, NOT the process cwd (INFRA-01).
# dataset/ lives at the repo root (this file's parent's parent);
# page_results/ lives inside data_aggregator/ (this file's parent).
_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent

ROOT = _REPO_ROOT / "dataset"
EXODUS_PARQUET = ROOT / "NMAT_Exodus.parquet"
EXODUS_CSV = ROOT / "NMAT_Exodus.csv"
REAL_FOREIGNERS = ROOT / "REAL_FOREIGNERS.csv"
RESULTS_DIR = _HERE / "page_results"

# Bin and PLE order
BIN_ORDER = [f"B{i}" for i in range(1, 11)]
PLE_ORDER = ["Confirmed PLE passer", "No confirmed PLE match"]

# Color palettes (used for reference)
PALETTE_UNI = {
    "Public": "#1f77b4",
    "Private": "#ff7f0e",
    "Foreign": "#9467bd",
    "Not Specified": "#7f7f7f",
}
PALETTE_COURSE = {
    "Medical & Allied": "#d62728",
    "Natural Sciences": "#2ca02c",
    "Social & Behavioral Sciences": "#ff9800",
    "Education": "#17becf",
    "Engineering & Technology": "#8c564b",
    "Other": "#7f7f7f",
}
PALETTE_PLE = {
    "Confirmed PLE passer": "#2e7d32",
    "No confirmed PLE match": "#c62828",
}
BIN_COLORS = {
    "B1": "#8B0000", "B2": "#B22222", "B3": "#D9534F",
    "B4": "#F0AD4E", "B5": "#FFD166", "B6": "#A0D468",
    "B7": "#66C2A5", "B8": "#41B6C4", "B9": "#2C7FB8", "B10": "#253494",
}

# Numeric columns from dashboard
NUMERIC_COLS = [
    "Year", "NMS_PER_num", "NMS_GPS", "NMS_APT", "NMS_SA",
    "NMS_VCss","NMS_IRss","NMS_Qss","NMS_PAss",
    "NMS_BIOss","NMS_PHYss","NMS_SSCss","NMS_CHEMss",
    "TotalRawScoreTRUE","PartIRawScoreTRUE","PartIIRawScoreTRUE",
    "Raw_Verbal","Raw_InductiveReasoning","Raw_Quantitative","Raw_PerceptualAcuity",
    "Raw_Biology","Raw_Physics","Raw_SocialScience","Raw_Chemistry",
    "StoredRawTotal","CalculatedRawTotal_Source",
    "APT_CEM","SA_CEM","GPS_CEM","Percentile_CEM",
    "PLE_YEAR_PASSED","PLE_YEAR_GAP","PLE_MATCH_CONFIDENCE",
]

SUBTEST_STD = {
    "Verbal": "NMS_VCss",
    "Inductive": "NMS_IRss",
    "Quantitative": "NMS_Qss",
    "Perceptual": "NMS_PAss",
    "Biology": "NMS_BIOss",
    "Physics": "NMS_PHYss",
    "Social": "NMS_SSCss",
    "Chemistry": "NMS_CHEMss",
}
SUBTEST_RAW = {
    "Verbal": "Raw_Verbal",
    "Inductive": "Raw_InductiveReasoning",
    "Quantitative": "Raw_Quantitative",
    "Perceptual": "Raw_PerceptualAcuity",
    "Biology": "Raw_Biology",
    "Physics": "Raw_Physics",
    "Social": "Raw_SocialScience",
    "Chemistry": "Raw_Chemistry",
}

REQUIRED_PIPELINE_COLS = [
    "APPNO_CLEAN", "PERSON_KEY", "UNDERGRAD_UNI_TYPE", "UNDERGRAD_UNI_LOCATION",
    "UNDERGRAD_COURSE_GROUP", "IS_BEST_NMAT_RECORD", "IS_PLE_PASSER",
    "HasTRUErawScores", "PLE_MATCH_METHOD",
]
