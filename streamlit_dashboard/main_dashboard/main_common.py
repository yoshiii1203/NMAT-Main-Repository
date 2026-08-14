"""main_common.py -- single shared compute layer for the main NMAT dashboard.

`dashboard.py` and `export_markdown.py` both import from here so a number
computed once is displayed identically everywhere (export-format contract
Rule 6: exporter and dashboard must call the SAME compute function, never
re-derive an aggregation independently).

Nothing in this file touches Streamlit. Every `compute_*` function takes
plain DataFrames/dicts and returns plain DataFrames/dicts/tuples so it can
be called from the dashboard, the exporter, a script, or a test.

Chart-DRAWING functions (make_heatmap, make_stacked_pct_bar, make_sankey,
make_trends_figure, make_box_by_year, ...) stay in dashboard.py -- they
turn an already-computed table into a plotly Figure and need no shared
compute step of their own.
"""

from pathlib import Path
import concurrent.futures

import numpy as np
import pandas as pd
import duckdb
from scipy import stats

try:
    import scikit_posthocs as sp
    HAS_POSTHOCS = True
except Exception:
    HAS_POSTHOCS = False


# -----------------------------------------------------------------------------
# CONSTANTS (single source of truth -- do not redefine these elsewhere)
# -----------------------------------------------------------------------------
BIN_ORDER = [f"B{i}" for i in range(1, 11)]
PLE_ORDER = ["Confirmed PLE passer", "No confirmed PLE match"]
TOP_BINS = ["B8", "B9", "B10"]
BOTTOM_BINS = ["B1", "B2", "B3"]

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
    "B1": "#8B0000", "B2": "#B22222", "B3": "#D9534F", "B4": "#F0AD4E",
    "B5": "#FFD166", "B6": "#A0D468", "B7": "#66C2A5", "B8": "#41B6C4",
    "B9": "#2C7FB8", "B10": "#253494",
}

NUMERIC_COLS = [
    "Year", "NMS_PER_num", "NMS_GPS", "NMS_APT", "NMS_SA",
    "NMS_VCss", "NMS_IRss", "NMS_Qss", "NMS_PAss",
    "NMS_BIOss", "NMS_PHYss", "NMS_SSCss", "NMS_CHEMss",
    "TotalRawScoreTRUE", "PartIRawScoreTRUE", "PartIIRawScoreTRUE",
    "Raw_Verbal", "Raw_InductiveReasoning", "Raw_Quantitative", "Raw_PerceptualAcuity",
    "Raw_Biology", "Raw_Physics", "Raw_SocialScience", "Raw_Chemistry",
    "StoredRawTotal", "CalculatedRawTotal_Source",
    "APT_CEM", "SA_CEM", "GPS_CEM", "Percentile_CEM",
    "PLE_YEAR_PASSED", "PLE_YEAR_GAP", "PLE_MATCH_CONFIDENCE",
]
BOOL_COLS = [
    "IS_PLE_PASSER", "IS_BEST_NMAT_RECORD",
    "HasTRUErawScores", "StoredVsDerivedMismatch",
    "IS_OBSERVABLE_COHORT", "IS_BEST_OBSERVABLE_RECORD", "PERSON_KEY_AMBIGUOUS",
]

REQUIRED_PIPELINE_COLS = [
    "APPNO_CLEAN",
    "PERSON_KEY",
    "UNDERGRAD_UNI_TYPE",
    "UNDERGRAD_UNI_LOCATION",
    "UNDERGRAD_COURSE_GROUP",
    "IS_BEST_NMAT_RECORD",
    "IS_PLE_PASSER",
    "IS_OBSERVABLE_COHORT",
    "IS_BEST_OBSERVABLE_RECORD",
    "HasTRUErawScores",
    "PLE_MATCH_METHOD",
]


# -----------------------------------------------------------------------------
# PURE HELPERS (moved verbatim from dashboard.py lines ~109-678)
# -----------------------------------------------------------------------------
def find_data_path() -> Path:
    candidates = [
        Path("NMAT_Exodus.parquet"),
        Path(__file__).parent / "NMAT_Exodus.parquet",
        Path("dataset/NMAT_Exodus.parquet"),
        Path("dataset/NMAT_Ultima.parquet"),
        Path("NMAT_Ultima.parquet"),
    ]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError(
        "Could not find NMAT_Exodus.parquet. "
        "Place it in ./dataset/ or in the app root."
    )


def to_bool_series(s: pd.Series) -> pd.Series:
    if str(s.dtype) == "boolean":
        return s
    if pd.api.types.is_bool_dtype(s):
        return s.astype("boolean")

    mapping = {
        "TRUE": True, "1": True, "1.0": True, "YES": True, "Y": True,
        "FALSE": False, "0": False, "0.0": False, "NO": False, "N": False,
    }
    s_norm = s.astype(str).str.strip().str.upper()

    out = s_norm.map(mapping)
    missing_mask = s.isna() | s_norm.isin(["", "NAN", "<NA>", "NONE"])
    out = out.mask(missing_mask, pd.NA)
    return out.astype("boolean")


def classify_course(text: str) -> str:
    text = str(text).upper()
    med = ["MEDICAL", "ALLIED", "NURSING", "PHARMACY", "HEALTH", "MED TECHNOLOGY", "RADIOLOGIC", "PUBLIC HEALTH", "NUTRITION"]
    nat = ["BIOLOGY", "NATURAL SCIENCE", "NATURAL SCIENCES", "PHYSICS", "CHEMISTRY"]
    soc = ["SOCIAL", "BEHAVIORAL", "BEHAVIOURAL", "PSYCHOLOGY", "ECONOMICS"]
    eng = ["ENGINEERING", "TECHNOLOGY"]
    edu = ["EDUCATION", "TEACHER"]
    if any(k in text for k in med):
        return "Medical & Allied"
    if any(k in text for k in nat):
        return "Natural Sciences"
    if any(k in text for k in soc):
        return "Social & Behavioral Sciences"
    if any(k in text for k in eng):
        return "Engineering & Technology"
    if any(k in text for k in edu):
        return "Education"
    return "Other"


def count_true_flags(series: pd.Series) -> int:
    if series is None:
        return 0
    return int((to_bool_series(series) == True).sum())


def ensure_required_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    def process_numeric(col):
        if col in df.columns:
            return col, pd.to_numeric(df[col], errors="coerce")
        return col, None

    def process_bool(col):
        if col in df.columns:
            return col, to_bool_series(df[col])
        return col, None

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for col in NUMERIC_COLS:
            futures.append(executor.submit(process_numeric, col))
        for col in BOOL_COLS:
            futures.append(executor.submit(process_bool, col))

        for future in concurrent.futures.as_completed(futures):
            col, res = future.result()
            if res is not None:
                df[col] = res

    if "YEAR_INT" not in df.columns and "Year" in df.columns:
        df["YEAR_INT"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    elif "YEAR_INT" in df.columns:
        df["YEAR_INT"] = pd.to_numeric(df["YEAR_INT"], errors="coerce").astype("Int64")

    if "Year" in df.columns:
        df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    elif "YEAR_INT" in df.columns:
        df["Year"] = df["YEAR_INT"]

    _BIN_EDGES = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 101]
    # back-compat: rename old column if present
    if "PercentileDecile" in df.columns and "PercentileBin" not in df.columns:
        df = df.rename(columns={"PercentileDecile": "PercentileBin"})
    if "PercentileBin" not in df.columns:
        df["PercentileBin"] = pd.cut(
            pd.to_numeric(df["NMS_PER_num"], errors="coerce"),
            bins=_BIN_EDGES,
            labels=BIN_ORDER,
            right=False,
            include_lowest=True,
        )
    df["PercentileBin"] = pd.Categorical(
        df["PercentileBin"], categories=BIN_ORDER, ordered=True
    )

    missing_required = [c for c in REQUIRED_PIPELINE_COLS if c not in df.columns]
    if missing_required:
        raise ValueError(
            "NMAT_Exodus.parquet is missing required pipeline columns: "
            + ", ".join(missing_required)
        )

    df["UNDERGRAD_UNI_TYPE"] = df["UNDERGRAD_UNI_TYPE"].fillna("Not Specified").astype(str).replace({"nan": "Not Specified"})
    df["UNDERGRAD_UNI_LOCATION"] = df["UNDERGRAD_UNI_LOCATION"].fillna("Unknown")
    df["UNDERGRAD_COURSE_GROUP"] = df["UNDERGRAD_COURSE_GROUP"].fillna("Unknown")

    if "SEX_CLEAN" not in df.columns:
        sex_source = None
        for c in ["SEX", "NMASex"]:
            if c in df.columns:
                sex_source = c
                break
        if sex_source is not None:
            s = df[sex_source].astype(str).str.strip().str.title()
            s = s.replace({"1": "Male", "2": "Female"})
            s = s.where(s.isin(["Male", "Female"]), np.nan)
            df["SEX_CLEAN"] = s
        else:
            df["SEX_CLEAN"] = np.nan
    # A missing/unmapped value must be its own visible category, not a
    # silent NaN -- rows with no SEX would otherwise drop out of every
    # sidebar-filtered subset by construction (isin() never matches NaN).
    df["SEX_CLEAN"] = df["SEX_CLEAN"].fillna("(not specified)")

    # IS_BOARD_OBSERVABLE_COHORT is an internal alias for the pipeline's
    # IS_OBSERVABLE_COHORT (Year <= 2014).
    if "IS_OBSERVABLE_COHORT" in df.columns:
        df["IS_BOARD_OBSERVABLE_COHORT"] = df["IS_OBSERVABLE_COHORT"]
    elif "IS_BOARD_OBSERVABLE_COHORT" not in df.columns:
        df["IS_BOARD_OBSERVABLE_COHORT"] = df["Year"].le(2014).fillna(False)

    # HAS_CONFIRMED_PLE / PLE_STATUS_LABEL describe "found in the PLE passer
    # source list", not "passed vs failed" -- the complement is a LINKAGE
    # gap, never evidence of failure.
    if "IS_PLE_PASSER" in df.columns:
        df["HAS_CONFIRMED_PLE"] = (df["IS_PLE_PASSER"] == True).astype("boolean")
    else:
        df["HAS_CONFIRMED_PLE"] = pd.Series(pd.NA, index=df.index, dtype="boolean")

    if "IS_PLE_PASSER" in df.columns:
        df["PLE_STATUS_LABEL"] = np.where(df["IS_PLE_PASSER"] == True, "Confirmed PLE passer", "No confirmed PLE match")
    else:
        df["PLE_STATUS_LABEL"] = "No confirmed PLE match"
    df["PLE_STATUS_LABEL"] = pd.Categorical(df["PLE_STATUS_LABEL"], categories=PLE_ORDER, ordered=True)

    return df


def load_data_and_subsets():
    """Load + validate the parquet and build the standard analytic subsets.

    No @st.cache_data here -- dashboard.py wraps this with the cache
    decorator so this module stays streamlit-free.
    """
    path = find_data_path()
    df = pd.read_parquet(path, engine="pyarrow", use_threads=True)
    df = ensure_required_columns(df)

    dfall = df
    dfbest = df[df["IS_BEST_NMAT_RECORD"] == True] if "IS_BEST_NMAT_RECORD" in df.columns else df
    dftrend = dfall[dfall["Year"].between(2006, 2018, inclusive="both")]
    dfbesttrend = dfbest[dfbest["Year"].between(2006, 2018, inclusive="both")]
    # IS_BEST_OBSERVABLE_RECORD is the person's best attempt *within*
    # Year<=2014 -- NOT the same as dfbesttrend filtered to Year<=2014,
    # which silently drops people whose overall-best attempt fell later.
    if "IS_BEST_OBSERVABLE_RECORD" in df.columns:
        dfbestobservable = df[df["IS_BEST_OBSERVABLE_RECORD"] == True]
    else:
        dfbestobservable = dfbesttrend[dfbesttrend["IS_BOARD_OBSERVABLE_COHORT"] == True]
    dfuni = dfbesttrend[dfbesttrend["UNDERGRAD_UNI_TYPE"].isin(["Public", "Private", "Foreign"])]
    dfuniobservable = dfbestobservable[dfbestobservable["UNDERGRAD_UNI_TYPE"].isin(["Public", "Private", "Foreign"])]
    dfplepasser = df[df["IS_PLE_PASSER"] == True] if "IS_PLE_PASSER" in df.columns else df.iloc[0:0]
    dfplepasserbest = dfplepasser[dfplepasser["IS_BEST_NMAT_RECORD"] == True] if not dfplepasser.empty else df.iloc[0:0]

    subsets = {
        "all": dfall,
        "best": dfbest,
        "trend": dftrend,
        "besttrend": dfbesttrend,
        "bestobservable": dfbestobservable,
        "uni": dfuni,
        "uniobservable": dfuniobservable,
        "plepasser": dfplepasser,
        "plepasserbest": dfplepasserbest,
    }
    return df, subsets, str(path)


def filter_df(
    df: pd.DataFrame,
    years=None,
    unitypes=None,
    courses=None,
    sexes=None,
    ple_status=None,
):
    mask = np.ones(len(df), dtype=bool)
    if years is not None and len(years) > 0 and "Year" in df.columns:
        mask &= df["Year"].isin(years).to_numpy()
    if unitypes is not None and len(unitypes) > 0 and "UNDERGRAD_UNI_TYPE" in df.columns:
        mask &= df["UNDERGRAD_UNI_TYPE"].isin(unitypes).to_numpy()
    if courses is not None and len(courses) > 0 and "UNDERGRAD_COURSE_GROUP" in df.columns:
        mask &= df["UNDERGRAD_COURSE_GROUP"].isin(courses).to_numpy()
    if sexes is not None and len(sexes) > 0 and "SEX_CLEAN" in df.columns:
        mask &= df["SEX_CLEAN"].isin(sexes).to_numpy()
    if ple_status is not None and len(ple_status) > 0 and "PLE_STATUS_LABEL" in df.columns:
        mask &= df["PLE_STATUS_LABEL"].isin(ple_status).to_numpy()

    return df[mask]


def pct_table(df, group_col, cat_col, cat_order=None):
    tmp = (
        df.dropna(subset=[group_col, cat_col])
        .groupby([group_col, cat_col], observed=True)
        .size()
        .unstack(fill_value=0)
    )
    if cat_order is not None:
        tmp = tmp.reindex(columns=cat_order, fill_value=0)
    pct = tmp.div(tmp.sum(axis=1).replace(0, np.nan), axis=0).mul(100).fillna(0)
    return tmp, pct.round(2)


def make_flow(df: pd.DataFrame, source_col: str, target_col: str, source_order=None, target_order=None):
    flow = (
        df.dropna(subset=[source_col, target_col])
        .groupby([source_col, target_col], observed=True)
        .size()
        .reset_index(name="count")
    )

    if source_order is not None:
        flow[source_col] = pd.Categorical(flow[source_col], categories=source_order, ordered=True)
    if target_order is not None:
        flow[target_col] = pd.Categorical(flow[target_col], categories=target_order, ordered=True)

    flow = flow.sort_values([source_col, target_col]).reset_index(drop=True)
    return flow


def kruskal_table(df: pd.DataFrame, group_col: str, score_map: dict):
    rows = []
    for col, label in score_map.items():
        if col not in df.columns or group_col not in df.columns:
            continue
        groups = [g[col].dropna().values for _, g in df.groupby(group_col) if g[col].dropna().shape[0] > 4]
        if len(groups) < 2:
            continue
        stat, p = stats.kruskal(*groups)
        ntotal = sum(len(g) for g in groups)
        k = len(groups)
        eta2 = max(0.0, (stat - k + 1) / (ntotal - k)) if ntotal > k else np.nan
        rows.append({
            "Score": label,
            "H": round(stat, 3),
            "p_value": "<0.001" if p < 0.001 else round(float(p), 4),
            "eta_squared": round(float(eta2), 4) if pd.notna(eta2) else np.nan,
        })
    return pd.DataFrame(rows)


def mann_whitney_ple(df: pd.DataFrame, cols: dict):
    g1 = df[df["PLE_STATUS_LABEL"] == "Confirmed PLE passer"]
    g2 = df[df["PLE_STATUS_LABEL"] == "No confirmed PLE match"]
    rows = []
    for col, label in cols.items():
        if col not in df.columns:
            continue
        a = g1[col].dropna()
        b = g2[col].dropna()
        if len(a) < 5 or len(b) < 5:
            continue
        stat, p = stats.mannwhitneyu(a, b, alternative="two-sided")
        r = 1 - (2 * stat / (len(a) * len(b)))
        rows.append({
            "Score": label,
            "U_stat": round(float(stat), 1),
            "p_value": "<0.001" if p < 0.001 else round(float(p), 4),
            "effect_r": round(float(r), 4),
            "Confirmed_median": round(float(a.median()), 2),
            "NoMatch_median": round(float(b.median()), 2),
        })
    return pd.DataFrame(rows)


def chi_square_unitype_bin(df: pd.DataFrame):
    tmp = pd.crosstab(df["UNDERGRAD_UNI_TYPE"], df["PercentileBin"]).reindex(columns=BIN_ORDER, fill_value=0)
    chi2, p, dof, expected = stats.chi2_contingency(tmp.values)
    n = tmp.values.sum()
    r, c = tmp.shape
    cramers_v = np.sqrt(chi2 / (n * min(r - 1, c - 1))) if min(r - 1, c - 1) > 0 else np.nan
    summary = pd.DataFrame([{
        "chi2": round(float(chi2), 4),
        "p_value": "<0.001" if p < 0.001 else round(float(p), 4),
        "degrees_of_freedom": int(dof),
        "n_observations": int(n),
        "cramers_v": round(float(cramers_v), 4) if pd.notna(cramers_v) else np.nan,
    }])
    expected_df = pd.DataFrame(expected, index=tmp.index, columns=tmp.columns)
    return tmp, expected_df, summary


def get_yearly_summary(df: pd.DataFrame):
    out = (
        df.groupby("Year", observed=True)
        .agg(
            n=("APPNO_CLEAN", "count"),
            raw_median=("TotalRawScoreTRUE", "median"),
            raw_q25=("TotalRawScoreTRUE", lambda x: x.quantile(0.25)),
            raw_q75=("TotalRawScoreTRUE", lambda x: x.quantile(0.75)),
            part1_median=("PartIRawScoreTRUE", "median"),
            part2_median=("PartIIRawScoreTRUE", "median"),
            per_median=("NMS_PER_num", "median"),
            per_q25=("NMS_PER_num", lambda x: x.quantile(0.25)),
            per_q75=("NMS_PER_num", lambda x: x.quantile(0.75)),
            gps_median=("NMS_GPS", "median"),
        )
        .reset_index()
    )
    if not out.empty:
        out["iqr_raw"] = out["raw_q75"] - out["raw_q25"]
        out["part1_share_pct"] = np.where(out["raw_median"] > 0, out["part1_median"] / out["raw_median"] * 100, np.nan)
        out["part2_share_pct"] = np.where(out["raw_median"] > 0, out["part2_median"] / out["raw_median"] * 100, np.nan)
    return out.round(2)


def subtest_mean_table(df: pd.DataFrame, group_col: str, std=True):
    if std:
        cols = {
            "Verbal": "NMS_VCss", "Inductive": "NMS_IRss", "Quantitative": "NMS_Qss",
            "Perceptual": "NMS_PAss", "Biology": "NMS_BIOss", "Physics": "NMS_PHYss",
            "Social": "NMS_SSCss", "Chemistry": "NMS_CHEMss",
        }
    else:
        cols = {
            "Verbal": "Raw_Verbal", "Inductive": "Raw_InductiveReasoning", "Quantitative": "Raw_Quantitative",
            "Perceptual": "Raw_PerceptualAcuity", "Biology": "Raw_Biology", "Physics": "Raw_Physics",
            "Social": "Raw_SocialScience", "Chemistry": "Raw_Chemistry",
        }

    available = {k: v for k, v in cols.items() if v in df.columns}
    if not available:
        return pd.DataFrame()
    out = df.groupby(group_col, observed=True)[list(available.values())].mean().round(2)
    out.columns = list(available.keys())
    return out


def radar_for_group(df: pd.DataFrame, group_col: str):
    """Returns (plotly Figure, table). Kept per the task's explicit move
    list -- uses only plotly.graph_objects (no streamlit dependency)."""
    import plotly.graph_objects as go

    table = subtest_mean_table(df, group_col, std=True)
    if table.empty:
        return go.Figure(), table
    fig = go.Figure()
    categories = list(table.columns)
    if not categories:
        return fig, table
    for grp in table.index:
        values = table.loc[grp, categories].fillna(0).tolist()
        if not values:
            continue
        fig.add_trace(go.Scatterpolar(
            r=values + [values[0]],
            theta=categories + [categories[0]],
            fill="toself",
            name=str(grp)
        ))
    fig.update_layout(title=f"Subtest Profile by {group_col}", height=520)
    return fig, table


# =============================================================================
# TAB 1 -- Executive Summary
# =============================================================================
def compute_tab1_kpis(base: pd.DataFrame, observable: pd.DataFrame, trend: pd.DataFrame) -> dict:
    n_person = base["PERSON_KEY"].nunique()
    repeat_n = int((trend.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique() > 1).sum())
    return {
        "n_best": len(base),
        "n_years": int(base["Year"].nunique()),
        "median_raw": float(base["TotalRawScoreTRUE"].median()) if len(base) else float("nan"),
        "median_pct": float(base["NMS_PER_num"].median()) if len(base) else float("nan"),
        "n_repeat": repeat_n,
        "repeat_share_pct": (repeat_n / n_person * 100) if n_person else None,
        "n_observable": len(observable),
        "ple_linkage_pct": float(observable["HAS_CONFIRMED_PLE"].mean() * 100) if len(observable) else None,
    }


def compute_sittings_by_year(trend_df: pd.DataFrame) -> pd.Series:
    return trend_df.groupby("Year", observed=True)["APPNO_CLEAN"].count()


def compute_composition(df: pd.DataFrame, col: str, dropna: bool = True) -> pd.DataFrame:
    dist = df[col].value_counts(dropna=not dropna).rename_axis(col).reset_index(name="Count")
    dist["Share (%)"] = (dist["Count"] / dist["Count"].sum() * 100).round(2)
    return dist


def compute_tab1_summary_table(base: pd.DataFrame) -> pd.DataFrame:
    top_bin = base["PercentileBin"].isin(TOP_BINS).mean() * 100
    bottom_bin = base["PercentileBin"].isin(BOTTOM_BINS).mean() * 100
    return pd.DataFrame({
        "Indicator": [
            "Median Total Raw Score", "Median Part I Raw Score", "Median Part II Raw Score",
            "Median Percentile Rank", "Top-bin share (B8-B10)", "Bottom-bin share (B1-B3)",
        ],
        "Value": [
            round(base["TotalRawScoreTRUE"].median(), 2),
            round(base["PartIRawScoreTRUE"].median(), 2),
            round(base["PartIIRawScoreTRUE"].median(), 2),
            round(base["NMS_PER_num"].median(), 2),
            round(top_bin, 2),
            round(bottom_bin, 2),
        ],
    })


# =============================================================================
# TAB 2 -- Data Integrity
# =============================================================================
def compute_tab2_kpis(df: pd.DataFrame, best_filtered: pd.DataFrame, best_observable_filtered: pd.DataFrame) -> dict:
    return {
        "n_all": len(df),
        "n_best": len(best_filtered),
        "n_true_raw": int((df["HasTRUErawScores"] == True).sum()),
        "n_best_observable": len(best_observable_filtered),
    }


def compute_cohort_table(F: dict) -> pd.DataFrame:
    return pd.DataFrame({
        "Analytic subset": [
            "All cleaned NMAT rows",
            "One best NMAT record per person",
            "Best-record rows within 2006-2018",
            "Best-record rows in the observable PLE window",
            "Confirmed PLE-passer NMAT rows",
            "Confirmed PLE-passer best-record persons",
        ],
        "Row count": [
            len(F["all"]), len(F["best"]), len(F["besttrend"]),
            len(F["bestobservable"]), len(F["plepasser"]), len(F["plepasserbest"]),
        ],
        "Interpretation": [
            "Every cleaned NMAT sitting, any year, all applicants.",
            "One row per unique PERSON_KEY -- their single best NMAT attempt (highest percentile, latest year, lowest APPNO_CLEAN tiebreak).",
            "Best-record rows restricted to NMAT years 2006-2018 (the trend window).",
            "One row per person: their best attempt among sittings with Year <= 2014 (IS_BEST_OBSERVABLE_RECORD) -- the correct PLE-linked person-level cohort.",
            "All rows (any year) flagged IS_PLE_PASSER == True -- found in the PLE passer source list. This is a linkage flag, not evidence of failure for the rest.",
            "Rows above further restricted to IS_BEST_NMAT_RECORD == True (one row per passer).",
        ],
    })


def compute_raw_validation_checks(df: pd.DataFrame) -> dict:
    eq_mask = df[["TotalRawScoreTRUE", "PartIRawScoreTRUE", "PartIIRawScoreTRUE"]].notna().all(axis=1)
    mismatch = (df.loc[eq_mask, "TotalRawScoreTRUE"] - df.loc[eq_mask, "PartIRawScoreTRUE"] - df.loc[eq_mask, "PartIIRawScoreTRUE"]).round(6) != 0
    stored_nonnull = df["StoredRawTotal"].notna() if "StoredRawTotal" in df.columns else pd.Series(dtype=bool)
    mismatch_flag_n = count_true_flags(df["StoredVsDerivedMismatch"]) if "StoredVsDerivedMismatch" in df.columns else 0
    mismatch_rate_pct = (mismatch_flag_n / stored_nonnull.sum() * 100) if stored_nonnull.sum() > 0 else float("nan")
    return {
        "eq_mask_n": int(eq_mask.sum()),
        "mismatch_n": int(mismatch.sum()),
        "stored_nonnull_n": int(stored_nonnull.sum()),
        "mismatch_flag_n": int(mismatch_flag_n),
        "mismatch_rate_pct": mismatch_rate_pct,
    }


def compute_university_pairing_audit(df: pd.DataFrame):
    if "UNDERGRAD_UNIVERSITY" not in df.columns:
        return None, None
    university_pairing = (
        df[["UNDERGRAD_UNIVERSITY", "UNDERGRAD_UNI_TYPE", "UNDERGRAD_UNI_LOCATION"]]
        .dropna(subset=["UNDERGRAD_UNIVERSITY"])
        .groupby("UNDERGRAD_UNIVERSITY", observed=True)
        .agg(
            records=("UNDERGRAD_UNI_TYPE", "size"),
            n_uni_types=("UNDERGRAD_UNI_TYPE", "nunique"),
            n_locations=("UNDERGRAD_UNI_LOCATION", "nunique"),
            uni_types=("UNDERGRAD_UNI_TYPE", lambda s: " | ".join(sorted(set(str(x) for x in s if pd.notna(x))))),
            locations=("UNDERGRAD_UNI_LOCATION", lambda s: " | ".join(sorted(set(str(x) for x in s if pd.notna(x))))),
        )
        .reset_index()
        .sort_values(["n_uni_types", "n_locations", "records"], ascending=[False, False, False])
    )
    pairing_conflicts = university_pairing[
        (university_pairing["n_uni_types"] > 1) | (university_pairing["n_locations"] > 1)
    ]
    return university_pairing, pairing_conflicts


def compute_ple_status_observable(df: pd.DataFrame):
    obs_status = df[df["IS_BOARD_OBSERVABLE_COHORT"] == True]
    status_counts = obs_status["PLE_STATUS_LABEL"].value_counts(dropna=False).rename_axis("PLE_STATUS_LABEL").reset_index(name="Count")
    non_obs_n = int((df["IS_BOARD_OBSERVABLE_COHORT"] == False).sum())
    non_obs_pct = (non_obs_n / len(df) * 100) if len(df) else 0.0
    return status_counts, non_obs_n, non_obs_pct


def compute_ple_match_outcome(df: pd.DataFrame):
    if "PLE_MATCH_OUTCOME" not in df.columns:
        return None, None
    outcome_tbl = df["PLE_MATCH_OUTCOME"].value_counts(dropna=False).rename_axis("PLE_MATCH_OUTCOME").reset_index(name="Count")
    outcome_tbl["Percent"] = (outcome_tbl["Count"] / outcome_tbl["Count"].sum() * 100).round(2)
    yr_uncertain_n = count_true_flags(df["PLE_YEAR_UNCERTAIN"]) if "PLE_YEAR_UNCERTAIN" in df.columns else None
    return outcome_tbl, yr_uncertain_n


# =============================================================================
# TAB 4 -- Score Bins & Background
# =============================================================================
def compute_percentile_summary_by(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """n / median / Q25 / Q75 of NMS_PER_num by an arbitrary group column
    (e.g. Tab 4 Table 12: percentile summary by course group)."""
    return (
        df.groupby(group_col, observed=True)["NMS_PER_num"]
        .agg(n="count", median="median", q25=lambda x: x.quantile(0.25), q75=lambda x: x.quantile(0.75))
        .round(2)
        .reset_index()
    )


def compute_box_summary_by(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """Five-number summary + n + outlier count per group -- the mandatory
    stand-in for a box-plot chart's raw points (export contract Rule 1).
    Outlier = outside [Q1-1.5*IQR, Q3+1.5*IQR] (standard Tukey rule, matches
    the default box-plot whisker convention)."""
    rows = []
    for grp, s in df.dropna(subset=[group_col, value_col]).groupby(group_col, observed=True)[value_col]:
        s = s.dropna()
        if s.empty:
            continue
        q1, med, q3 = s.quantile(0.25), s.median(), s.quantile(0.75)
        iqr = q3 - q1
        lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        rows.append({
            group_col: grp, "n": int(s.shape[0]), "min": round(float(s.min()), 2),
            "q1": round(float(q1), 2), "median": round(float(med), 2), "q3": round(float(q3), 2),
            "max": round(float(s.max()), 2), "outliers": int(((s < lo) | (s > hi)).sum()),
        })
    return pd.DataFrame(rows)


def compute_year_gap_histogram(gap_df: pd.DataFrame) -> pd.DataFrame:
    """Distribution table backing the PLE-year-gap histogram."""
    out = gap_df["PLE_YEAR_GAP"].value_counts().sort_index().rename_axis("PLE_YEAR_GAP").reset_index(name="Count")
    return out


def compute_repeat_change_summary(first_last: pd.DataFrame) -> pd.DataFrame:
    """Five-number summary of percentile/raw-score change from first to last
    attempt -- backs the repeat-taker change box plot."""
    long_change = first_last.melt(
        id_vars=["PERSON_KEY"], value_vars=["pct_improvement", "raw_improvement"],
        var_name="Measure", value_name="Change",
    )
    long_change["Measure"] = long_change["Measure"].replace({
        "pct_improvement": "Percentile change", "raw_improvement": "Raw score change",
    })
    return compute_box_summary_by(long_change, "Measure", "Change")


def compute_top_bottom_by(pct_df: pd.DataFrame) -> pd.DataFrame:
    """Top (B8-B10) vs bottom (B1-B3) share per row of an already-computed
    pct_table() output (e.g. indexed by Year)."""
    top = pct_df[TOP_BINS].sum(axis=1)
    bottom = pct_df[BOTTOM_BINS].sum(axis=1)
    out = pd.DataFrame({
        pct_df.index.name or "Group": pct_df.index.astype(str),
        "Top B8-B10 (%)": top.to_numpy(dtype=float),
        "Bottom B1-B3 (%)": bottom.to_numpy(dtype=float),
    })
    out["Difference (pp)"] = (out["Top B8-B10 (%)"] - out["Bottom B1-B3 (%)"]).round(1)
    return out


def compute_bin_by_year_and_unitype(df: pd.DataFrame) -> pd.DataFrame:
    con = duckdb.connect()
    con.register("_yr_uni_src", df)
    out = con.execute("""
        SELECT
            CAST(Year AS INTEGER) AS Year,
            UNDERGRAD_UNI_TYPE,
            PercentileBin,
            COUNT(*) AS n
        FROM _yr_uni_src
        WHERE UNDERGRAD_UNI_TYPE IN ('Public', 'Private', 'Foreign')
          AND PercentileBin IS NOT NULL
          AND Year IS NOT NULL
        GROUP BY Year, UNDERGRAD_UNI_TYPE, PercentileBin
        ORDER BY Year, UNDERGRAD_UNI_TYPE, PercentileBin
    """).df()
    con.close()
    if not out.empty:
        out["PercentileBin"] = pd.Categorical(out["PercentileBin"], categories=BIN_ORDER, ordered=True)
        out = out.sort_values(["Year", "UNDERGRAD_UNI_TYPE", "PercentileBin"])
    return out


def compute_citizenship_profile(df_uniobservable: pd.DataFrame) -> dict:
    """Bundle of every aggregation behind the Tab-4 'Citizenship profile for
    no-PLE-match examinees' section. One function, one shared population
    definition (_pc_base), so every chart/table in that section reads from
    the same base."""
    if "CITIZENSHIP_FINAL" not in df_uniobservable.columns:
        return {"available": False}

    pc_base = df_uniobservable[
        (df_uniobservable["PLE_STATUS_LABEL"] == "No confirmed PLE match")
        & (df_uniobservable["CITIZENSHIP_FINAL"].notna())
    ].copy()
    if pc_base.empty:
        return {"available": True, "empty": True}

    kpis = {
        "n_profiled": len(pc_base),
        "n_foreigners": int((pc_base["FOREIGNER_STATUS"] == "Verified Foreigner").sum()),
        "n_filipinos": int((pc_base["CITIZENSHIP_FINAL"] == "Filipino").sum()),
        "n_distinct": int(pc_base["CITIZENSHIP_FINAL"].nunique()),
    }

    pc_counts = pc_base["CITIZENSHIP_FINAL"].value_counts().reset_index()
    pc_counts.columns = ["CITIZENSHIP_FINAL", "n"]

    top15 = pc_counts.head(15)["CITIZENSHIP_FINAL"].tolist()
    pc_dec_base = pc_base[pc_base["CITIZENSHIP_FINAL"].isin(top15)].copy()
    bin_dist_top15 = None
    if not pc_dec_base.empty and "PercentileBin" in pc_dec_base.columns:
        _, bin_dist_top15 = pct_table(pc_dec_base, "CITIZENSHIP_FINAL", "PercentileBin", BIN_ORDER)
        bin_dist_top15.index.name = "CITIZENSHIP_FINAL"

    topbin_share = None
    if "PercentileBin" in pc_base.columns:
        t = (
            pc_base.assign(_is_top=pc_base["PercentileBin"].isin(TOP_BINS))
            .groupby("CITIZENSHIP_FINAL", observed=True)
            .agg(n=("_is_top", "size"), top_n=("_is_top", "sum"))
            .reset_index()
        )
        t["top_dec_pct"] = (t["top_n"] / t["n"].replace(0, np.nan) * 100).fillna(0).round(1)
        topbin_share = t[t["n"] >= 3].sort_values("top_dec_pct")

    pc_base["_is_top_d"] = pc_base["PercentileBin"].isin(TOP_BINS) if "PercentileBin" in pc_base.columns else False
    pc_base["_is_bot_d"] = pc_base["PercentileBin"].isin(BOTTOM_BINS) if "PercentileBin" in pc_base.columns else False
    summary = (
        pc_base.groupby("CITIZENSHIP_FINAL", observed=True)
        .agg(
            n_examinees=("APPNO_CLEAN", "count"),
            median_percentile_rank=("NMS_PER_num", "median"),
            median_true_raw_score=("TotalRawScoreTRUE", "median"),
            top_decile_n=("_is_top_d", "sum"),
            bottom_decile_n=("_is_bot_d", "sum"),
        )
        .round(2)
        .reset_index()
    )
    summary["top_decile_pct"] = (summary["top_decile_n"] / summary["n_examinees"].replace(0, np.nan) * 100).fillna(0).round(2)
    summary["bottom_decile_pct"] = (summary["bottom_decile_n"] / summary["n_examinees"].replace(0, np.nan) * 100).fillna(0).round(2)
    summary["top_decile_n"] = summary["top_decile_n"].astype(int)
    summary["bottom_decile_n"] = summary["bottom_decile_n"].astype(int)
    summary = summary[
        ["CITIZENSHIP_FINAL", "n_examinees", "median_percentile_rank", "median_true_raw_score",
         "top_decile_n", "top_decile_pct", "bottom_decile_n", "bottom_decile_pct"]
    ].sort_values(["n_examinees", "median_percentile_rank"], ascending=[False, False])

    by_unitype = None
    if "UNDERGRAD_UNI_TYPE" in pc_base.columns:
        by_unitype = (
            pc_base.groupby(["CITIZENSHIP_FINAL", "UNDERGRAD_UNI_TYPE"], observed=True)
            .agg(n=("APPNO_CLEAN", "count"), median_percentile_rank=("NMS_PER_num", "median"), median_true_raw_score=("TotalRawScoreTRUE", "median"))
            .round(2).reset_index()
        )

    by_course = None
    if "UNDERGRAD_COURSE_GROUP" in pc_base.columns:
        by_course = (
            pc_base.groupby(["CITIZENSHIP_FINAL", "UNDERGRAD_COURSE_GROUP"], observed=True)
            .agg(n=("APPNO_CLEAN", "count"), median_percentile_rank=("NMS_PER_num", "median"), median_true_raw_score=("TotalRawScoreTRUE", "median"))
            .round(2).reset_index()
        )

    by_year = None
    if "Year" in pc_base.columns:
        by_year = pc_base.groupby(["CITIZENSHIP_FINAL", "Year"], observed=True).size().unstack(fill_value=0)
        by_year.index.name = "CITIZENSHIP_FINAL"
        by_year = by_year.reset_index()

    return {
        "available": True, "empty": False,
        "kpis": kpis, "counts": pc_counts, "top15": top15,
        "bin_dist_top15": bin_dist_top15, "topbin_share": topbin_share,
        "summary": summary, "by_unitype": by_unitype, "by_course": by_course,
        "by_year": by_year, "records": pc_base,
    }


def compute_comparative_groups(df_uniobservable: pd.DataFrame, df_bestobservable: pd.DataFrame):
    """Foreigners vs Filipino (public/private/foreign-undergrad) comparison
    used in Tab 4's 'Comparative analysis' section."""
    cmp_parts = []

    g_for = df_uniobservable[df_uniobservable["FOREIGNER_STATUS"] == "Verified Foreigner"].copy() if "FOREIGNER_STATUS" in df_uniobservable.columns else pd.DataFrame()
    if not g_for.empty:
        g_for["_cmp_group"] = "Foreigners (non-Filipino)"
        cmp_parts.append(g_for)

    if "CITIZENSHIP_FINAL" in df_uniobservable.columns:
        g_fil_for = df_uniobservable[
            (df_uniobservable["CITIZENSHIP_FINAL"] == "Filipino") & (df_uniobservable["UNDERGRAD_UNI_TYPE"] == "Foreign")
        ].copy()
        if not g_fil_for.empty:
            g_fil_for["_cmp_group"] = "Filipinos (foreign undergrad)"
            cmp_parts.append(g_fil_for)

    g_pub = df_bestobservable[df_bestobservable["UNDERGRAD_UNI_TYPE"] == "Public"].copy()
    if not g_pub.empty:
        g_pub["_cmp_group"] = "Filipinos (public undergrad)"
        cmp_parts.append(g_pub)

    g_prv = df_bestobservable[df_bestobservable["UNDERGRAD_UNI_TYPE"] == "Private"].copy()
    if not g_prv.empty:
        g_prv["_cmp_group"] = "Filipinos (private undergrad)"
        cmp_parts.append(g_prv)

    if not cmp_parts:
        return None

    cmp_score_cols = ["_cmp_group", "NMS_PER_num", "TotalRawScoreTRUE", "PartIRawScoreTRUE", "PartIIRawScoreTRUE", "PercentileBin", "HAS_CONFIRMED_PLE"]
    cmp_df = pd.concat([p[[c for c in cmp_score_cols if c in p.columns]] for p in cmp_parts], ignore_index=True)

    cmp_agg = (
        cmp_df.groupby("_cmp_group", observed=True)
        .agg(
            n=("NMS_PER_num", "count"),
            median_percentile_rank=("NMS_PER_num", "median"),
            q25_pct=("NMS_PER_num", lambda x: x.quantile(0.25)),
            q75_pct=("NMS_PER_num", lambda x: x.quantile(0.75)),
            median_raw_score=("TotalRawScoreTRUE", "median"),
        )
        .round(2).reset_index().rename(columns={"_cmp_group": "Group"})
    )
    if "HAS_CONFIRMED_PLE" in cmp_df.columns:
        cmp_df["_ple_num"] = (cmp_df["HAS_CONFIRMED_PLE"] == True).astype(float)
        ple_rates = (
            cmp_df.groupby("_cmp_group", observed=True)["_ple_num"].mean().mul(100).round(2)
            .reset_index().rename(columns={"_cmp_group": "Group", "_ple_num": "PLE linkage rate %"})
        )
        cmp_agg = cmp_agg.merge(ple_rates, on="Group", how="left")

    bin_pct = None
    if "PercentileBin" in cmp_df.columns:
        _, bin_pct = pct_table(cmp_df.dropna(subset=["_cmp_group", "PercentileBin"]), "_cmp_group", "PercentileBin", BIN_ORDER)
        bin_pct.index.name = "_cmp_group"

    topbot = None
    if bin_pct is not None and len(bin_pct):
        topbot = pd.DataFrame({
            "Group": bin_pct.index.tolist(),
            "Top B8-B10 (%)": bin_pct[TOP_BINS].sum(axis=1).values,
            "Bottom B1-B3 (%)": bin_pct[BOTTOM_BINS].sum(axis=1).values,
        })

    return {"cmp_df": cmp_df, "agg": cmp_agg, "bin_pct": bin_pct, "topbot": topbot}


# =============================================================================
# TAB 5 -- University Type Analysis
# =============================================================================
def compute_unitype_location_mix(df: pd.DataFrame) -> pd.DataFrame:
    type_loc = df.groupby(["UNDERGRAD_UNI_TYPE", "UNDERGRAD_UNI_LOCATION"], observed=True).size().reset_index(name="Count")
    type_loc["Percent of total"] = (type_loc["Count"] / type_loc["Count"].sum() * 100).round(2)
    return type_loc.sort_values(["UNDERGRAD_UNI_TYPE", "UNDERGRAD_UNI_LOCATION"])


def compute_unitype_location_crosstab(df: pd.DataFrame):
    inst_count = pd.crosstab(df["UNDERGRAD_UNI_TYPE"], df["UNDERGRAD_UNI_LOCATION"], margins=True)
    inst_pct_row = (pd.crosstab(df["UNDERGRAD_UNI_TYPE"], df["UNDERGRAD_UNI_LOCATION"], normalize="index") * 100).round(2)
    inst_pct_col = (pd.crosstab(df["UNDERGRAD_UNI_TYPE"], df["UNDERGRAD_UNI_LOCATION"], normalize="columns") * 100).round(2)
    return inst_count, inst_pct_row, inst_pct_col


def compute_unitype_location_bin_dist(df: pd.DataFrame) -> pd.DataFrame:
    inst_decile = (
        df.dropna(subset=["UNDERGRAD_UNI_TYPE", "UNDERGRAD_UNI_LOCATION", "PercentileBin"])
        .groupby(["UNDERGRAD_UNI_TYPE", "UNDERGRAD_UNI_LOCATION", "PercentileBin"], observed=True)
        .size().unstack(fill_value=0).reindex(columns=BIN_ORDER, fill_value=0)
    )
    if inst_decile.empty:
        return inst_decile
    inst_decile_pct = inst_decile.div(inst_decile.sum(axis=1).replace(0, np.nan), axis=0).mul(100).fillna(0).round(2)
    inst_decile_pct.index = [f"{u} ({l})" for u, l in inst_decile_pct.index]
    return inst_decile_pct


def compute_uni_bin_summary(df: pd.DataFrame):
    count, pct = pct_table(df, "UNDERGRAD_UNI_TYPE", "PercentileBin", BIN_ORDER)
    pct.index.name = "UNDERGRAD_UNI_TYPE"
    summary = count.copy()
    summary["Total students"] = summary.sum(axis=1)
    summary.index.name = "UNDERGRAD_UNI_TYPE"
    summary = summary.reset_index()
    return pct, summary


def compute_foreign_summary(df: pd.DataFrame) -> dict:
    foreign = df[df["UNDERGRAD_UNI_TYPE"].eq("Foreign")].copy()
    return {
        "n_foreign": len(foreign),
        "pct_of_total": (len(foreign) / max(len(df), 1) * 100),
        "median_pct": float(foreign["NMS_PER_num"].median()) if not foreign.empty else None,
        "topbin_pct": float(foreign["PercentileBin"].isin(TOP_BINS).mean() * 100) if not foreign.empty else None,
        "foreign_df": foreign,
    }


def compute_course_bucket_by_unitype(df: pd.DataFrame) -> pd.DataFrame:
    med_other = df.copy()
    med_other["Course bucket"] = np.where(med_other["UNDERGRAD_COURSE_GROUP"].eq("Medical & Allied"), "Medical & Allied", "Other Courses")
    med_tbl = (
        med_other.groupby(["UNDERGRAD_UNI_TYPE", "Course bucket"], observed=True)
        .size().unstack(fill_value=0).reindex(columns=["Medical & Allied", "Other Courses"], fill_value=0)
    )
    med_pct = med_tbl.div(med_tbl.sum(axis=1).replace(0, np.nan), axis=0).mul(100).round(2)
    med_pct.index.name = "UNDERGRAD_UNI_TYPE"
    return med_pct


def compute_university_listing(df: pd.DataFrame, unitype: str) -> pd.DataFrame:
    return (
        df[df["UNDERGRAD_UNI_TYPE"] == unitype]
        .groupby(["UNDERGRAD_UNIVERSITY", "UNDERGRAD_UNI_LOCATION"], observed=True)
        .agg(total_applicants=("APPNO_CLEAN", "count"))
        .reset_index()
        .sort_values("total_applicants", ascending=False)
    )


# =============================================================================
# TAB 6 -- Flow & Pathways
# =============================================================================
def compute_flow_pct(flow: pd.DataFrame, source_col: str, target_col: str, source_order, target_order) -> pd.DataFrame:
    row_pct = (
        flow.pivot(index=source_col, columns=target_col, values="count")
        .reindex(index=source_order, columns=target_order)
        .fillna(0)
    )
    row_pct = row_pct.div(row_pct.sum(axis=1).replace(0, np.nan), axis=0).mul(100).fillna(0).round(2)
    return row_pct


def compute_top_pathways(df: pd.DataFrame, group_col: str, n: int = 10) -> pd.DataFrame:
    return (
        df[df["PercentileBin"].isin(TOP_BINS)]
        .groupby([group_col, "PercentileBin"], observed=True)
        .size().reset_index(name="Count")
        .sort_values("Count", ascending=False).head(n)
    )


# =============================================================================
# TAB 7 / TAB 12 -- PLE Alignment & Policy Tables (shared pattern)
# =============================================================================
def compute_score_desc_by(df: pd.DataFrame, group_col: str, cols) -> pd.DataFrame:
    desc_cols = [c for c in cols if c in df.columns]
    q25 = lambda x: x.quantile(0.25)
    q25.__name__ = "q25"
    q75 = lambda x: x.quantile(0.75)
    q75.__name__ = "q75"
    return df.groupby(group_col, observed=True)[desc_cols].agg(["count", "median", "mean", q25, q75]).round(2)


def compute_ple_status_by_bin(df: pd.DataFrame) -> pd.DataFrame:
    decile_status = (
        df.dropna(subset=["PercentileBin", "PLE_STATUS_LABEL"])
        .groupby(["PercentileBin", "PLE_STATUS_LABEL"], observed=True)
        .size().unstack(fill_value=0).reindex(index=BIN_ORDER, columns=PLE_ORDER, fill_value=0)
    )
    decile_status_pct = decile_status.div(decile_status.sum(axis=1).replace(0, np.nan), axis=0).mul(100).fillna(0).round(2)
    decile_status_pct.index.name = "PercentileBin"
    return decile_status_pct


def compute_top_bin_share_by(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """'Survival to top bins' -- used by Tab 7 Table 26 and Tab 12 Table 4
    (previously two copies of the identical block)."""
    survival_base = df.dropna(subset=[group_col, "PercentileBin"]).copy()
    survival_base["IS_TOP_BIN"] = survival_base["PercentileBin"].isin(TOP_BINS)
    survival = (
        survival_base.groupby(group_col, observed=True)
        .agg(total_examinees=("IS_TOP_BIN", "size"), top_decile_n=("IS_TOP_BIN", "sum"))
        .reset_index()
    )
    survival["top_decile_n"] = survival["top_decile_n"].astype(int)
    survival["survival_rate_pct"] = (survival["top_decile_n"] / survival["total_examinees"] * 100).round(2)
    return survival.sort_values(["survival_rate_pct", "top_decile_n"], ascending=[False, False]).reset_index(drop=True)


def compute_ple_alignment_by(df: pd.DataFrame, group_col: str, include_median: bool = False) -> pd.DataFrame:
    """Confirmed-PLE-passer alignment table by any grouping column -- used
    by Tab 7 Table 28/29/30 and Tab 12 Tables 1-3 (previously six copies of
    the same block)."""
    sub = df
    if group_col == "UNDERGRAD_UNI_TYPE":
        sub = sub[sub["UNDERGRAD_UNI_TYPE"].isin(["Public", "Private", "Foreign"])]

    def _agg(x):
        d = {
            "n_observable_best_records": len(x),
            "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
            "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
            "confirmed_ple_share_pct": round((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2),
        }
        if include_median:
            d["median_percentile_rank"] = round(x["NMS_PER_num"].median(), 2)
        return pd.Series(d)

    out = sub.groupby(group_col, observed=True).apply(_agg).reset_index()
    if group_col == "Year":
        out = out.sort_values("Year")
    elif include_median and group_col != "UNDERGRAD_UNI_TYPE":
        out = out.sort_values("confirmed_ple_share_pct", ascending=False)
    return out


# =============================================================================
# TAB 8 -- Repeat Takers
# =============================================================================
def compute_attempt_distribution(df: pd.DataFrame):
    attempt_ct = df.groupby("PERSON_KEY", observed=True)["APPNO_CLEAN"].nunique().reset_index(name="attempt_count")
    attempt_summary = (
        attempt_ct["attempt_count"].value_counts().sort_index()
        .rename_axis("Attempts").reset_index(name="Count")
    )
    attempt_summary["Percent"] = (attempt_summary["Count"] / attempt_summary["Count"].sum() * 100).round(2)
    return attempt_ct, attempt_summary


def compute_repeat_trajectories(df: pd.DataFrame):
    attempt_ct, _ = compute_attempt_distribution(df)
    repeat_persons = attempt_ct.loc[attempt_ct["attempt_count"] > 1, "PERSON_KEY"]
    repeat_df = df[df["PERSON_KEY"].isin(repeat_persons)].copy()
    if repeat_df.empty:
        return None, None
    repeat_df = repeat_df.sort_values(["PERSON_KEY", "YEAR_INT", "APPNO_CLEAN"])
    first_last = (
        repeat_df.groupby("PERSON_KEY", observed=True)
        .agg(
            first_year=("YEAR_INT", "first"), last_year=("YEAR_INT", "last"),
            first_pct=("NMS_PER_num", "first"), last_pct=("NMS_PER_num", "last"),
            first_raw=("TotalRawScoreTRUE", "first"), last_raw=("TotalRawScoreTRUE", "last"),
            n_attempts=("APPNO_CLEAN", "count"),
        )
        .dropna().reset_index()
    )
    first_last["pct_improvement"] = first_last["last_pct"] - first_last["first_pct"]
    first_last["raw_improvement"] = first_last["last_raw"] - first_last["first_raw"]
    summary = {
        "n_repeat_persons": int(repeat_persons.nunique()),
        "n_analytic_repeat_takers": int(len(first_last)),
        "pct_improved_percentile": round((first_last["pct_improvement"] > 0).mean() * 100, 2),
        "pct_improved_raw": round((first_last["raw_improvement"] > 0).mean() * 100, 2),
        "median_pct_change": round(first_last["pct_improvement"].median(), 2),
        "median_raw_change": round(first_last["raw_improvement"].median(), 2),
    }
    return first_last, summary


def compute_appno_deterministic_matches(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["PLE_MATCH_METHOD"].isin(["MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"])]


# =============================================================================
# TAB 10 -- Year Gap & Gender
# =============================================================================
def compute_year_gap_kpis(df: pd.DataFrame):
    gap_df = df[(df["PLE_STATUS_LABEL"] == "Confirmed PLE passer") & df["PLE_YEAR_GAP"].notna()].copy()
    if gap_df.empty:
        return gap_df, {}
    kpis = {
        "n": len(gap_df),
        "median": float(gap_df["PLE_YEAR_GAP"].median()),
        "q25": float(gap_df["PLE_YEAR_GAP"].quantile(0.25)),
        "q75": float(gap_df["PLE_YEAR_GAP"].quantile(0.75)),
    }
    return gap_df, kpis


def compute_year_gap_by_course(gap_df: pd.DataFrame) -> pd.DataFrame:
    return (
        gap_df.groupby("UNDERGRAD_COURSE_GROUP", observed=True)
        .agg(
            confirmed_passers=("PERSON_KEY", "nunique"),
            median_year_gap=("PLE_YEAR_GAP", "median"),
            q25_year_gap=("PLE_YEAR_GAP", lambda x: x.quantile(0.25)),
            q75_year_gap=("PLE_YEAR_GAP", lambda x: x.quantile(0.75)),
            median_percentile=("NMS_PER_num", "median"),
        )
        .reset_index().sort_values("median_year_gap").round(2)
    )


def compute_score_by_sex(df: pd.DataFrame):
    sex_base = df.dropna(subset=["SEX_CLEAN"]).copy()
    if sex_base.empty:
        return None
    return (
        sex_base.groupby("SEX_CLEAN", observed=True)
        .agg(n=("PERSON_KEY", "nunique"), median_raw=("TotalRawScoreTRUE", "median"), median_pct=("NMS_PER_num", "median"), median_gps=("NMS_GPS", "median"))
        .reset_index().round(2)
    )


# =============================================================================
# TAB 11 -- Statistical Tests
# =============================================================================
def compute_dunn_posthoc(df: pd.DataFrame):
    if not HAS_POSTHOCS:
        return None
    ph_df = df.dropna(subset=["Year", "NMS_PER_num"]).copy()
    if ph_df["Year"].nunique() < 3:
        return None
    dunn = sp.posthoc_dunn(ph_df, val_col="NMS_PER_num", group_col="Year", p_adjust="bonferroni")
    dunn.index = dunn.index.astype(str)
    dunn.columns = dunn.columns.astype(str)
    return dunn


# =============================================================================
# TAB 13 -- CHED Compliance
# =============================================================================
def _bin_at_or_above(b, threshold_b):
    if pd.isna(b):
        return False
    try:
        return BIN_ORDER.index(b) >= BIN_ORDER.index(threshold_b)
    except (ValueError, IndexError):
        return False


def compute_cutoff_scenarios(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for uni_type in ["All", "Public", "Private", "Foreign"]:
        sub_obs = df if uni_type == "All" else df[df["UNDERGRAD_UNI_TYPE"] == uni_type]
        for label, b in [("30th percentile (B4+)", "B4"), ("40th percentile (B5+)", "B5")]:
            ple_cohort = sub_obs[sub_obs["PercentileBin"].apply(lambda x: _bin_at_or_above(x, b))]
            rows.append({
                "University Type": uni_type,
                "Cut-off": label,
                "Observable-cohort applicants at/above cut-off": len(ple_cohort),
                "PLE passers (observable)": int(ple_cohort["IS_PLE_PASSER"].sum()),
                "PLE linkage rate (%)": round(ple_cohort["IS_PLE_PASSER"].mean() * 100, 2) if len(ple_cohort) > 0 else 0,
                "Median percentile": round(ple_cohort["NMS_PER_num"].median(), 1) if len(ple_cohort) > 0 else 0,
            })
    return pd.DataFrame(rows)


def compute_citizenship_group_bin_dist(df: pd.DataFrame):
    if "FOREIGNER_STATUS" not in df.columns:
        return None, None
    d = df.copy()
    d["_citz_group"] = np.where(d["FOREIGNER_STATUS"] != "Filipino", "Foreigner", "Filipino")
    _, citz_pct = pct_table(d, "_citz_group", "PercentileBin", BIN_ORDER)
    citz_pct.index.name = "Group"
    citz_n = d["_citz_group"].value_counts().rename_axis("Group").reset_index(name="n")
    return citz_n, citz_pct


def compute_linkage_gradient(df: pd.DataFrame) -> pd.DataFrame:
    grad = df.groupby("PercentileBin", observed=True)["IS_PLE_PASSER"].agg(["size", "sum", "mean"]).reindex(BIN_ORDER)
    grad.columns = ["n", "linked_n", "linkage_rate"]
    grad["linkage_rate_pct"] = (grad["linkage_rate"] * 100).round(2)
    grad = grad.drop(columns=["linkage_rate"]).reset_index()
    return grad
