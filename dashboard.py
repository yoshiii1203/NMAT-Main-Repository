from pathlib import Path
import warnings
import concurrent.futures

try:
    import cudf.pandas
    cudf.pandas.install()
    print("cuDF Pandas acceleration activated.")
except Exception:
    pass

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import duckdb
import streamlit as st
from scipy import stats

warnings.filterwarnings("ignore")

try:
    import scikit_posthocs as sp
    HAS_POSTHOCS = True
except Exception:
    HAS_POSTHOCS = False


# -----------------------------------------------------------------------------
# CONFIG
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="NMAT Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

BIN_ORDER = [f"B{i}" for i in range(1, 11)]
PLE_ORDER = ["Confirmed PLE passer", "No confirmed PLE match"]

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
    "B1": "#8B0000",
    "B2": "#B22222",
    "B3": "#D9534F",
    "B4": "#F0AD4E",
    "B5": "#FFD166",
    "B6": "#A0D468",
    "B7": "#66C2A5",
    "B8": "#41B6C4",
    "B9": "#2C7FB8",
    "B10": "#253494",
}

NUMERIC_COLS = [
    "Year", "NMS_PER_num", "NMS_GPS", "NMS_APT", "NMS_SA",
    "NMS_VCss","NMS_IRss","NMS_Qss","NMS_PAss",
    "NMS_BIOss","NMS_PHYss","NMS_SSCss","NMS_CHEMss",
    "TotalRawScoreTRUE","PartIRawScoreTRUE","PartIIRawScoreTRUE",
    "Raw_Verbal","Raw_InductiveReasoning","Raw_Quantitative","Raw_PerceptualAcuity",
    "Raw_Biology","Raw_Physics","Raw_SocialScience","Raw_Chemistry",
    "StoredRawTotal","CalculatedRawTotal_Source",
    "APT_CEM","SA_CEM","GPS_CEM","Percentile_CEM",
    "PLE_YEAR_PASSED","PLE_YEAR_GAP","PLE_MATCH_CONFIDENCE"
]
BOOL_COLS = [
    "IS_PLE_PASSER","IS_PLE_ANALYSIS_SAFE","IS_BEST_NMAT_RECORD",
    "HasCEMMatch","HasTRUErawScores","AllRawComponentsPresent",
]

REQUIRED_PIPELINE_COLS = [
    "APPNO_CLEAN",
    "PERSON_KEY",
    "UNI_TYPE",
    "UNI_LOCATION",
    "CourseGroup",
    "IS_BEST_NMAT_RECORD",
    "IS_PLE_ANALYSIS_SAFE",
    "HasTRUErawScores",
    "PLE_MATCH_METHOD",
]


# -----------------------------------------------------------------------------
# HELPERS
# -----------------------------------------------------------------------------
def find_data_path() -> Path:
    candidates = [
        Path("dataset/NMAT_Ultima.parquet"),
        Path("NMAT_Ultima.parquet"),
    ]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError(
        "Could not find NMAT_Ultima.parquet. "
        "Place it in ./dataset/ or in the app root."
    )


def to_bool_series(s: pd.Series) -> pd.Series:
    if str(s.dtype) == "boolean":
        return s
    if pd.api.types.is_bool_dtype(s):
        return s.astype("boolean")

    mapping = {
        "TRUE": True, "1": True, "YES": True, "Y": True,
        "FALSE": False, "0": False, "NO": False, "N": False,
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


def derive_ple_status(row: pd.Series) -> str:
    if row.get("IS_PLE_ANALYSIS_SAFE") == True:
        return "Confirmed PLE passer"
    return "No confirmed PLE match"


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

    BIN_ORDER = [f"B{i}" for i in range(1, 11)]
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
            "NMAT_Ultima.parquet is missing required pipeline columns: "
            + ", ".join(missing_required)
        )

    df["UNI_TYPE"] = df["UNI_TYPE"].fillna("Not Specified").astype(str).replace({"nan": "Not Specified"})
    df["UNI_LOCATION"] = df["UNI_LOCATION"].fillna("Unknown")
    df["CourseGroup"] = df["CourseGroup"].fillna("Unknown")

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

    if "IS_BOARD_OBSERVABLE_COHORT" not in df.columns:
        df["IS_BOARD_OBSERVABLE_COHORT"] = df["Year"].le(2014).fillna(False)

    if "HAS_CONFIRMED_PLE" not in df.columns:
        if "IS_PLE_ANALYSIS_SAFE" in df.columns:
            df["HAS_CONFIRMED_PLE"] = (df["IS_PLE_ANALYSIS_SAFE"] == True).astype("boolean")
        else:
            df["HAS_CONFIRMED_PLE"] = pd.Series(pd.NA, index=df.index, dtype="boolean")

    if "PLE_STATUS_LABEL" not in df.columns:
        if "IS_PLE_ANALYSIS_SAFE" in df.columns:
            df["PLE_STATUS_LABEL"] = np.where(df["IS_PLE_ANALYSIS_SAFE"] == True, "Confirmed PLE passer", "No confirmed PLE match")
        else:
            df["PLE_STATUS_LABEL"] = "No confirmed PLE match"
    df["PLE_STATUS_LABEL"] = pd.Categorical(df["PLE_STATUS_LABEL"], categories=PLE_ORDER, ordered=True)

    return df


@st.cache_data(show_spinner=False)
def load_data_and_subsets():
    _v = "bin_v1"  # cache bust: parquet regenerated with PercentileBin
    path = find_data_path()
    df = pd.read_parquet(path, engine="pyarrow", use_threads=True)
    df = ensure_required_columns(df)
    
    dfall = df
    dfbest = df[df["IS_BEST_NMAT_RECORD"] == True] if "IS_BEST_NMAT_RECORD" in df.columns else df
    dftrend = dfall[dfall["Year"].between(2006, 2018, inclusive="both")]
    dfbesttrend = dfbest[dfbest["Year"].between(2006, 2018, inclusive="both")]
    dfbestobservable = dfbesttrend[dfbesttrend["IS_BOARD_OBSERVABLE_COHORT"] == True]
    dfuni = dfbesttrend[dfbesttrend["UNI_TYPE"].isin(["Public", "Private", "Foreign"])]
    dfuniobservable = dfbestobservable[dfbestobservable["UNI_TYPE"].isin(["Public", "Private", "Foreign"])]
    dfplesafe = df[df["IS_PLE_ANALYSIS_SAFE"] == True] if "IS_PLE_ANALYSIS_SAFE" in df.columns else df.iloc[0:0]
    dfplebest = dfplesafe[dfplesafe["IS_BEST_NMAT_RECORD"] == True] if not dfplesafe.empty else df.iloc[0:0]

    subsets = {
        "all": dfall,
        "best": dfbest,
        "trend": dftrend,
        "besttrend": dfbesttrend,
        "bestobservable": dfbestobservable,
        "uni": dfuni,
        "uniobservable": dfuniobservable,
        "plesafe": dfplesafe,
        "plebest": dfplebest,
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
    if unitypes is not None and len(unitypes) > 0 and "UNI_TYPE" in df.columns:
        mask &= df["UNI_TYPE"].isin(unitypes).to_numpy()
    if courses is not None and len(courses) > 0 and "CourseGroup" in df.columns:
        mask &= df["CourseGroup"].isin(courses).to_numpy()
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


def make_heatmap(table: pd.DataFrame, title: str, xlab: str, ylab: str, color_scale="Blues"):
    fig = px.imshow(
        table,
        text_auto=".1f",
        aspect="auto",
        color_continuous_scale=color_scale,
        labels={"x": xlab, "y": ylab, "color": "Percent"},
        title=title,
    )
    fig.update_traces(
        hovertemplate=f"{ylab}: %{{y}}<br>{xlab}: %{{x}}<br>Percent: %{{z:.2f}}<extra></extra>"
    )
    fig.update_layout(height=450)
    return fig


def make_stacked_pct_bar(pct_df: pd.DataFrame, title: str, xlab: str, ylab: str, color_map=None):
    plot_df = pct_df.reset_index().melt(id_vars=pct_df.index.name or "index", var_name="Category", value_name="Percent")
    idx_name = pct_df.index.name or "index"
    fig = px.bar(
        plot_df,
        x=idx_name,
        y="Percent",
        color="Category",
        title=title,
        labels={idx_name: xlab, "Percent": ylab},
        color_discrete_map=color_map,
    )
    fig.update_traces(
        hovertemplate=f"{xlab}: %{{x}}<br>Category: %{{fullData.name}}<br>{ylab}: %{{y:.2f}}%<extra></extra>"
    )
    fig.update_layout(barmode="stack", height=450, legend_title_text="")
    return fig


def make_top_share_bar(series: pd.Series, title: str, xlab: str, ylab: str, color_map=None):
    s = series.sort_values()
    colors = [color_map.get(i, "#7f7f7f") if color_map else "#1f77b4" for i in s.index]
    fig = go.Figure(
        go.Bar(
            x=s.values,
            y=s.index.astype(str),
            orientation="h",
            marker_color=colors,
            text=[f"{v:.1f}%" for v in s.values],
            textposition="outside",
            hovertemplate=f"{ylab}: %{{y}}<br>{xlab}: %{{x:.2f}}%<extra></extra>",
        )
    )
    fig.update_layout(title=title, xaxis_title=xlab, yaxis_title=ylab, height=450)
    return fig


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


def make_sankey(flow: pd.DataFrame, source_col: str, target_col: str, title: str, source_colors=None, target_colors=None):
    source_nodes = flow[source_col].astype(str).drop_duplicates().tolist()
    target_nodes = flow[target_col].astype(str).drop_duplicates().tolist()
    labels = source_nodes + target_nodes
    node_map = {label: i for i, label in enumerate(labels)}

    sources = flow[source_col].astype(str).map(node_map).tolist()
    targets = flow[target_col].astype(str).map(node_map).tolist()
    values = flow["count"].tolist()

    use_custom_colors = bool(source_colors or target_colors)

    node_dict = dict(
        pad=18,
        thickness=18,
        line=dict(color="black", width=0.4),
        label=labels,
    )
    link_dict = dict(
        source=sources,
        target=targets,
        value=values,
    )

    if use_custom_colors:
        node_colors = []
        for lab in labels:
            if source_colors and lab in source_colors:
                node_colors.append(source_colors[lab])
            elif target_colors and lab in target_colors:
                node_colors.append(target_colors[lab])
            else:
                node_colors.append("#bdbdbd")

        link_colors = []
        for _, r in flow.iterrows():
            tgt = str(r[target_col])
            src = str(r[source_col])
            if target_colors and tgt in target_colors:
                link_colors.append(target_colors[tgt])
            elif source_colors and src in source_colors:
                link_colors.append(source_colors[src])
            else:
                link_colors.append("rgba(160,160,160,0.45)")

        node_dict["color"] = node_colors
        link_dict["color"] = link_colors

    fig = go.Figure(
        data=[
            go.Sankey(
                arrangement="snap",
                node=node_dict,
                link=link_dict,
            )
        ]
    )
    fig.update_traces(
        node_hovertemplate="%{label}<extra></extra>",
        link_hovertemplate=f"{source_col}: %{{source.label}}<br>{target_col}: %{{target.label}}<br>Count: %{{value}}<extra></extra>",
    )
    fig.update_layout(title=title, height=560)
    return fig


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
    tmp = pd.crosstab(df["UNI_TYPE"], df["PercentileBin"]).reindex(columns=BIN_ORDER, fill_value=0)
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


def make_trends_figure(summary: pd.DataFrame):
    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Median TRUE Raw Score (with IQR)",
            "Median Part I vs Part II Raw Score",
            "Median Percentile Rank (with IQR)",
            "Examinee Count by Year",
        ),
    )

    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["raw_q75"], mode="lines", line=dict(color="lightblue"), showlegend=False), 1, 1)
    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["raw_q25"], mode="lines", fill="tonexty", fillcolor="rgba(31,119,180,0.25)", line=dict(color="lightblue"), name="Raw IQR"), 1, 1)
    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["raw_median"], mode="lines+markers", name="Median raw", line=dict(color="#1f77b4", width=3)), 1, 1)

    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["part1_median"], mode="lines+markers", name="Part I", line=dict(color="#2ca02c", width=3)), 1, 2)
    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["part2_median"], mode="lines+markers", name="Part II", line=dict(color="#ff7f0e", width=3)), 1, 2)

    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["per_q75"], mode="lines", line=dict(color="lightsalmon"), showlegend=False), 2, 1)
    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["per_q25"], mode="lines", fill="tonexty", fillcolor="rgba(255,127,14,0.22)", line=dict(color="lightsalmon"), name="Percentile IQR"), 2, 1)
    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["per_median"], mode="lines+markers", name="Median percentile", line=dict(color="#d62728", width=3)), 2, 1)

    fig.add_trace(go.Bar(x=summary["Year"], y=summary["n"], name="Examinees"), 2, 2)

    fig.update_layout(height=760, hovermode="x unified")
    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="Score", row=1, col=1)
    fig.update_yaxes(title_text="Score", row=1, col=2)
    fig.update_yaxes(title_text="Percentile", row=2, col=1)
    fig.update_yaxes(title_text="Count", row=2, col=2)
    return fig


def make_box_by_year(df: pd.DataFrame, value_col: str, title: str):
    tmp = df.dropna(subset=["Year", value_col]).copy()
    fig = px.box(tmp, x="Year", y=value_col, points=False, title=title)
    fig.update_traces(hovertemplate="Year: %{x}<br>Value: %{y:.2f}<extra></extra>")
    fig.update_layout(height=420)
    return fig


def subtest_mean_table(df: pd.DataFrame, group_col: str, std=True):
    if std:
        cols = {
            "Verbal": "NMS_VCss",
            "Inductive": "NMS_IRss",
            "Quantitative": "NMS_Qss",
            "Perceptual": "NMS_PAss",
            "Biology": "NMS_BIOss",
            "Physics": "NMS_PHYss",
            "Social": "NMS_SSCss",
            "Chemistry": "NMS_CHEMss",
        }
    else:
        cols = {
            "Verbal": "Raw_Verbal",
            "Inductive": "Raw_InductiveReasoning",
            "Quantitative": "Raw_Quantitative",
            "Perceptual": "Raw_PerceptualAcuity",
            "Biology": "Raw_Biology",
            "Physics": "Raw_Physics",
            "Social": "Raw_SocialScience",
            "Chemistry": "Raw_Chemistry",
        }

    available = {k: v for k, v in cols.items() if v in df.columns}
    if not available:
        return pd.DataFrame()
    out = df.groupby(group_col, observed=True)[list(available.values())].mean().round(2)
    out.columns = list(available.keys())
    return out


def radar_for_group(df: pd.DataFrame, group_col: str):
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


# -----------------------------------------------------------------------------
# LOAD
# -----------------------------------------------------------------------------
df_raw, subsets, data_path = load_data_and_subsets()

dfbesttrend = subsets["besttrend"]
dfbestobservable = subsets["bestobservable"]

# --- Pseudo-citizenship profile lookup ---
_PC_PROFILE_PATH = Path("dataset/pseudo_citizenship_profiling_FINAL.csv")
try:
    _pc_lookup = pd.read_csv(
        _PC_PROFILE_PATH,
        usecols=["APPNO_CLEAN", "override_applied", "name_based_assessment", "pseudo_citizenship"],
        dtype=str,
    )
    _pc_lookup["APPNOCLEAN"] = _pc_lookup["APPNO_CLEAN"].str.strip()
    _pc_lookup = (
        _pc_lookup
        .drop(columns=["APPNO_CLEAN"])
        .drop_duplicates(subset=["APPNOCLEAN"])
        .reset_index(drop=True)
    )
    _PC_LOOKUP_AVAILABLE = True
except Exception:
    _pc_lookup = pd.DataFrame(
        columns=["APPNOCLEAN", "override_applied", "name_based_assessment", "pseudo_citizenship"]
    )
    _PC_LOOKUP_AVAILABLE = False

# -----------------------------------------------------------------------------
# SIDEBAR  (filters only — navigation is now handled by st.tabs)
# -----------------------------------------------------------------------------
st.sidebar.subheader("Global filters")

year_options = sorted([int(x) for x in dfbesttrend["Year"].dropna().unique()])
unitype_options = sorted(dfbesttrend["UNI_TYPE"].dropna().astype(str).unique().tolist())
course_options = sorted(dfbesttrend["CourseGroup"].dropna().astype(str).unique().tolist())
sex_options = sorted([x for x in dfbesttrend["SEX_CLEAN"].dropna().astype(str).unique().tolist() if x])

selected_years = st.sidebar.multiselect("Year", year_options, default=year_options)
selected_unitypes = st.sidebar.multiselect("University type", unitype_options, default=unitype_options)
selected_courses = st.sidebar.multiselect("Course group", course_options, default=course_options)
selected_sexes = st.sidebar.multiselect("Sex", sex_options, default=sex_options)

apply_ple_status_filter = st.sidebar.checkbox("Filter PLE pages by status", value=False)
selected_ple_status = PLE_ORDER if apply_ple_status_filter else None
if apply_ple_status_filter:
    selected_ple_status = st.sidebar.multiselect("PLE status", PLE_ORDER, default=PLE_ORDER)

st.sidebar.divider()
st.sidebar.caption(f"Source file: {data_path}")

# common filtered subsets
with concurrent.futures.ThreadPoolExecutor() as executor:
    future_to_name = {
        executor.submit(
            filter_df,
            df,
            years=selected_years,
            unitypes=selected_unitypes,
            courses=selected_courses,
            sexes=selected_sexes,
            ple_status=selected_ple_status if name in ["bestobservable", "uniobservable"] else None,
        ): name
        for name, df in subsets.items()
    }
    F = {}
    for future in concurrent.futures.as_completed(future_to_name):
        name = future_to_name[future]
        F[name] = future.result()

# Merge pseudo-citizenship lookup into the observable university subset
_uniobs_pc = F["uniobservable"].copy()
_uniobs_pc["APPNOCLEAN"] = _uniobs_pc["APPNO_CLEAN"].astype(str).str.strip()
_uniobs_pc = _uniobs_pc.merge(_pc_lookup, on="APPNOCLEAN", how="left").drop(columns=["APPNOCLEAN"])

# -----------------------------------------------------------------------------
# HEADER
# -----------------------------------------------------------------------------
st.title("NMAT Performance Dashboard, 2006–2018")
st.caption("Descriptive, trend-based, and policy-oriented summaries based on the cleaned NMAT_Ultima pipeline. Person-level views use the best NMAT record per examinee where appropriate, while PLE-linked pages use the observable cohort only.")

with st.expander("Read this first: how to interpret the dashboard", expanded=False):
    st.markdown(
        """
- Best-record pages show one NMAT record per examinee.
- Trend pages cover NMAT years 2006–2018.
- PLE-linked pages use the observable cohort only.
- Confirmed PLE outcomes refer to IS_PLE_ANALYSIS_SAFE == True.
        """
    )

(
    tab1, tab2, tab3, tab4, tab5, tab6,
    tab7, tab8, tab9, tab10, tab11, tab12,
) = st.tabs([
    "🏠 Executive Summary",
    "🧪 Data Integrity",
    "📈 Trends & Stability",
    "📊 Score Bins & Background",
    "🏫 University Type Analysis",
    "🔄 Flow & Pathways",
    "🎯 PLE Alignment",
    "🔁 Repeat Takers",
    "🧠 Subtests & Profiles",
    "⏰ Year Gap & Gender",
    "📐 Statistical Tests",
    "📋 Policy Tables & Export",
])

# -----------------------------------------------------------------------------
# TAB 1
# -----------------------------------------------------------------------------
with tab1:
    base = F["besttrend"]
    observable = F["bestobservable"]

    st.subheader("Executive Summary")
    st.caption("High-level summary of examinee volume, score levels, composition, and observable PLE alignment using the filtered best-record cohort.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Best-record examinees", f"{len(base):,}", help="Number of best-record rows in the current filtered trend cohort.")
    col2.metric("Years covered", f"{base['Year'].nunique():,}", help="Distinct NMAT years represented after filters are applied.")
    col3.metric("Median TRUE raw score", f"{base['TotalRawScoreTRUE'].median():.1f}", help="Median of TotalRawScoreTRUE in the filtered best-record trend cohort.")
    col4.metric("Median percentile rank", f"{base['NMS_PER_num'].median():.1f}", help="Median of NMS_PER_num in the filtered best-record trend cohort.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Unique examinees", f"{base['PERSON_KEY'].nunique():,}", help="Unique PERSON_KEY count in the current filtered trend cohort.")
    col2.metric("Repeat takers", f"{(F['trend'].groupby('PERSON_KEY')['APPNO_CLEAN'].nunique() > 1).sum():,}", help="Repeat takers come from multiple NMAT applications linked to the same PERSON_KEY.")
    col3.metric("Observable cohort size", f"{len(observable):,}", help="Best-record rows with Year <= 2014, used for fair PLE-linked descriptive summaries.")
    col4.metric("Confirmed PLE share in observable cohort", f"{observable['HAS_CONFIRMED_PLE'].mean() * 100:.2f}%", help="Confirmed PLE outcomes are based on the pipeline field IS_PLE_ANALYSIS_SAFE == True.")

    st.markdown("""
    📚 **Course Group Distribution**

    Course groups are sourced directly from the cleaned pipeline output (`CourseGroup`):

    - **Medical & Allied**: Medical, Nursing, Pharmacy, Health-related
    - **Natural Sciences**: Biology, Physics, Chemistry, Natural Sciences
    - **Social & Behavioral Sciences**: Psychology, Economics, Social Sciences
    - **Engineering & Technology**: Engineering, Technology fields
    - **Education**: Teacher training, Education programs
    - **Other**: All remaining courses
    """)

    exec_tab1, exec_tab2, exec_tab3 = st.tabs(["📊 Overview", "📈 Composition", "📋 Quick Tables"])

    with exec_tab1:
        st.markdown("**Figure 1. Annual NMAT score and volume profile**")
        st.caption("This figure combines median TRUE raw score, Part I and Part II medians, median percentile rank, and examinee count by year. Use it to see whether performance and testing volume moved together or in opposite directions over time.")
        summary = get_yearly_summary(base)
        st.plotly_chart(make_trends_figure(summary), use_container_width=True, key="fig_t1_trends")

    with exec_tab2:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Figure 2. Course-group composition of best-record examinees**")
            st.caption("Values are counts of filtered best-record examinees by category.")
            course_dist = base["CourseGroup"].value_counts().rename_axis("CourseGroup").reset_index(name="Count")
            fig = px.pie(course_dist, names="CourseGroup", values="Count")
            st.plotly_chart(fig, use_container_width=True, key="fig_t1_course_pie")
        with c2:
            st.markdown("**Figure 3. University-type composition of best-record examinees**")
            st.caption("Percent shares refer to the current filtered cohort only.")
            uni_dist = base["UNI_TYPE"].value_counts().rename_axis("UNI_TYPE").reset_index(name="Count")
            fig = px.pie(uni_dist, names="UNI_TYPE", values="Count")
            st.plotly_chart(fig, use_container_width=True, key="fig_t1_uni_pie")

    with exec_tab3:
        top_bin = base["PercentileBin"].isin(["B8", "B9", "B10"]).mean() * 100
        bottom_bin = base["PercentileBin"].isin(["B1", "B2", "B3"]).mean() * 100
        st.markdown("**Table 1. Executive summary indicators**")
        st.caption("This table reports central score levels and the shares of examinees in the upper and lower bins. Top-bin share refers to B8–B10, while bottom-bin share refers to B1–B3.")
        summary_tbl = pd.DataFrame({
            "Indicator": [
                "Median Total Raw Score",
                "Median Part I Raw Score",
                "Median Part II Raw Score",
                "Median Percentile Rank",
                "Top-bin share (B8-B10)",
                "Bottom-bin share (B1-B3)",
            ],
            "Value": [
                round(base["TotalRawScoreTRUE"].median(), 2),
                round(base["PartIRawScoreTRUE"].median(), 2),
                round(base["PartIIRawScoreTRUE"].median(), 2),
                round(base["NMS_PER_num"].median(), 2),
                round(top_bin, 2),
                round(bottom_bin, 2),
            ]
        })
        st.dataframe(summary_tbl, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 2
# -----------------------------------------------------------------------------
with tab2:
    st.subheader("Data Integrity and Cohort Definition Checks")
    st.caption("This page verifies whether the dashboard inputs remain aligned with the cleaned NMAT_Ultima pipeline, including cohort construction, raw-score consistency, and institutional classification fields.")
    df = F["all"]
    best_filtered = F["best"]
    best_observable_filtered = F["bestobservable"]
    plesafe_filtered = F["plesafe"]
    plebest_filtered = F["plebest"]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("All NMAT rows", f"{len(df):,}", help="All cleaned NMAT_Ultima rows that are loaded into the app.")
    col2.metric("Best-record rows", f"{len(best_filtered):,}", help="Number of best-record rows in the pipeline (one per examinee after best-record flag applied).")
    col3.metric("Rows with TRUE raw scores", f"{int((df['HasTRUErawScores'] == True).sum()):,}", help="Rows where HasTRUErawScores == True.")
    col4.metric("Observable best-record rows", f"{len(best_observable_filtered):,}", help="Best-record rows with Year <= 2014, used for fair PLE-linked descriptive summaries.")

    st.subheader("Table 2. Analysis cohorts used in the dashboard")
    st.caption("Each row defines one analytic subset used in later pages. Counts should be interpreted as rows, not necessarily unique persons, unless explicitly stated otherwise.")
    cohort_tbl = pd.DataFrame({
        "Analytic subset": [
            "All cleaned NMAT rows",
            "One best NMAT record per person",
            "Best-record rows within 2006–2018",
            "Best-record rows in the observable PLE window",
            "Confirmed PLE-matched NMAT rows",
            "Confirmed PLE-matched best-record persons",
        ],
        "Row count": [
            len(F["all"]),
            len(F["best"]),
            len(F["besttrend"]),
            len(F["bestobservable"]),
            len(plesafe_filtered),
            len(plebest_filtered),
        ],
        "Interpretation": [
            "All cleaned NMAT rows",
            "One best NMAT record per person",
            "Best-record rows within 2006–2018",
            "Best-record rows in the observable PLE window",
            "Confirmed PLE-matched NMAT rows",
            "Confirmed PLE-matched best-record persons",
        ],
    })
    st.dataframe(cohort_tbl, use_container_width=True)

    st.subheader("Table 3. TRUE raw-score validation checks")
    st.caption("These checks confirm whether TRUE total raw score is internally consistent with its Part I and Part II components, and whether stored or calculated mismatch flags remain zero.")
    eq_mask = df[["TotalRawScoreTRUE", "PartIRawScoreTRUE", "PartIIRawScoreTRUE"]].notna().all(axis=1)
    mismatch = (df.loc[eq_mask, "TotalRawScoreTRUE"] - df.loc[eq_mask, "PartIRawScoreTRUE"] - df.loc[eq_mask, "PartIIRawScoreTRUE"]).round(6) != 0
    raw_tbl = pd.DataFrame({
        "Validation check": [
            "Rows with complete Total + Part I + Part II",
            "Formula mismatches: Total != Part I + Part II",
            "Stored-vs-derived mismatch flag count",
            "Calc-vs-derived mismatch flag count",
        ],
        "Count of rows": [
            int(eq_mask.sum()),
            int(mismatch.sum()),
            count_true_flags(df["StoredVsDerivedMismatch"]) if "StoredVsDerivedMismatch" in df.columns else 0,
            count_true_flags(df["CalcVsDerivedMismatch"]) if "CalcVsDerivedMismatch" in df.columns else 0,
        ],
    })
    st.dataframe(raw_tbl, use_container_width=True)

    st.subheader("Table 4. Post-cleaning UNI_TYPE consistency by source college")
    st.caption("Each row summarizes how one normalized source college name maps to the cleaned UNI_TYPE field. Any college with more than one mapped type should be reviewed.")
    if "NMA_College" in df.columns:
        integrity_base = df[["NMA_College", "UNI_TYPE"]].copy()
        integrity_base["NMA_College_norm"] = (
            integrity_base["NMA_College"]
            .astype("string")
            .str.strip()
            .str.upper()
        )

        college_check = (
            integrity_base.dropna(subset=["NMA_College_norm"])
            .groupby("NMA_College_norm", observed=True)
            .agg(
                records=("UNI_TYPE", "size"),
                n_types=("UNI_TYPE", "nunique"),
                mapped_types=("UNI_TYPE", lambda s: " | ".join(sorted(set(str(x) for x in s if pd.notna(x)))))
            )
            .reset_index()
            .sort_values(["n_types", "records"], ascending=[False, False])
        )
        inconsistent = college_check[college_check["n_types"] > 1]

        if "UNIVERSITY" in df.columns:
            university_pairing = (
                df[["UNIVERSITY", "UNI_TYPE", "UNI_LOCATION"]]
                .dropna(subset=["UNIVERSITY"])
                .groupby("UNIVERSITY", observed=True)
                .agg(
                    records=("UNI_TYPE", "size"),
                    n_uni_types=("UNI_TYPE", "nunique"),
                    n_locations=("UNI_LOCATION", "nunique"),
                    uni_types=("UNI_TYPE", lambda s: " | ".join(sorted(set(str(x) for x in s if pd.notna(x))))),
                    locations=("UNI_LOCATION", lambda s: " | ".join(sorted(set(str(x) for x in s if pd.notna(x)))))
                )
                .reset_index()
                .sort_values(["n_uni_types", "n_locations", "records"], ascending=[False, False, False])
            )
            pairing_conflicts = university_pairing[
                (university_pairing["n_uni_types"] > 1) | (university_pairing["n_locations"] > 1)
            ]
        else:
            university_pairing = pd.DataFrame()
            pairing_conflicts = pd.DataFrame()

        c1, c2 = st.columns(2)
        c1.metric("Colleges checked", f"{college_check.shape[0]:,}")
        c2.metric("Colleges with >1 type", f"{inconsistent.shape[0]:,}")
        st.dataframe(inconsistent.head(100), use_container_width=True)

        if "UNIVERSITY" in df.columns:
            c3, c4 = st.columns(2)
            c3.metric("Universities checked", f"{university_pairing.shape[0]:,}")
            c4.metric("University pairing conflicts", f"{pairing_conflicts.shape[0]:,}")
            with st.expander("Table 5. UNIVERSITY to UNI_TYPE and UNI_LOCATION pairing audit", expanded=False):
                st.caption("This table checks whether each standardized university name maps consistently to one university type and one location in the cleaned pipeline.")
                st.dataframe(pairing_conflicts.head(200), use_container_width=True)
    else:
        st.info("NMACollege is not available in the dataset.")

    st.subheader("Core distributions")
    st.caption("Values are row counts under the current filters.")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Table 6. Distribution of university type in the filtered rows**")
        st.dataframe(df["UNI_TYPE"].value_counts(dropna=False).rename_axis("UNI_TYPE").reset_index(name="Count"), use_container_width=True)
    with c2:
        st.markdown("**Table 7. Distribution of course group in the filtered rows**")
        st.dataframe(df["CourseGroup"].value_counts(dropna=False).rename_axis("CourseGroup").reset_index(name="Count"), use_container_width=True)
    with c3:
        st.markdown("**Table 8. Distribution of PLE status label in the filtered rows**")
        st.dataframe(df["PLE_STATUS_LABEL"].value_counts(dropna=False).rename_axis("PLE_STATUS_LABEL").reset_index(name="Count"), use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 3
# -----------------------------------------------------------------------------
with tab3:
    st.subheader("Performance Trends and Year-to-Year Stability")
    st.caption("This page summarizes how NMAT score levels and score distributions changed across test years using the filtered best-record trend cohort.")
    df = F["besttrend"]
    summary = get_yearly_summary(df)

    st.markdown("**Figure 4. Annual score trends and examinee volume**")
    st.caption("Panels show the median TRUE raw score with interquartile range, median Part I and Part II raw scores, median percentile rank with interquartile range, and examinee count by year.")
    st.plotly_chart(make_trends_figure(summary), use_container_width=True, key="fig_t3_trends")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**This boxplot shows the yearly spread, median, and upper/lower quartiles for TRUE raw scores**")
        st.plotly_chart(make_box_by_year(df, "TotalRawScoreTRUE", "Total Raw Score by Year"), use_container_width=True, key="fig_t3_box_raw")
    with c2:
        st.markdown("**This boxplot shows the yearly spread of percentile rank**")
        st.plotly_chart(make_box_by_year(df, "NMS_PER_num", "Percentile Rank by Year"), use_container_width=True, key="fig_t3_box_pct")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**This boxplot shows the yearly spread of Part I raw score**")
        st.plotly_chart(make_box_by_year(df, "PartIRawScoreTRUE", "Part I Raw Score by Year"), use_container_width=True, key="fig_t3_box_p1")
    with c2:
        st.markdown("**This boxplot shows the yearly spread of Part II raw score**")
        st.plotly_chart(make_box_by_year(df, "PartIIRawScoreTRUE", "Part II Raw Score by Year"), use_container_width=True, key="fig_t3_box_p2")

    st.markdown("**Table 9. Kruskal-Wallis tests for year-to-year score differences**")
    st.caption("This table tests whether score distributions differ significantly across NMAT years. Eta-squared is included as an effect-size indicator, so statistical significance is not mistaken for practical importance.")
    ktable = kruskal_table(
        df,
        "Year",
        {
            "TotalRawScoreTRUE": "Total Raw Score",
            "PartIRawScoreTRUE": "Part I Raw Score",
            "PartIIRawScoreTRUE": "Part II Raw Score",
            "NMS_PER_num": "Percentile Rank",
            "NMS_GPS": "GPS Standard Score",
        },
    )
    st.dataframe(ktable, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 4
# -----------------------------------------------------------------------------
with tab4:
    st.subheader("Bin Distribution by Year and Examinee Background")
    st.caption("This page shows how score bins are distributed across NMAT years, university type, and pre-med course background in the best-record trend cohort.")
    df = F["besttrend"]
    dfuni = F["uni"]

    dec_tab1, dec_tab2, dec_tab3 = st.tabs(["By year", "University type", "Course group"])

    with dec_tab1:
        st.caption("Use this tab to see whether later cohorts became more concentrated in higher bins, lower bins, or the middle of the distribution.")
        count, pct = pct_table(df, "Year", "PercentileBin", BIN_ORDER)
        pct.index.name = "Year"
        # Transpose for deciles on y-axis, years on x-axis
        pct_transposed = pct.T
        pct_transposed.index.name = "Bin"
        # Reverse decile order for D10-D1 descending
        decile_order_desc = BIN_ORDER[::-1]
        pct_transposed = pct_transposed.reindex(decile_order_desc)
        st.markdown("**Figure 5. Percentile-bin heatmap by NMAT year**")
        st.caption("Heatmap values are within-year percentages; B8–B10 represents the upper segment and B1–B3 represents the lower segment.")
        st.plotly_chart(make_heatmap(pct_transposed, "Bin Distribution by Year", "Bin", "Year", "YlOrRd"), use_container_width=True, key="fig_t4_heatmap_year")

        # Add deciles distribution table by counts with D10 to D1 rows and Year columns
        st.markdown("**Table 10. Count of examinees in each bin by NMAT year**")
        st.caption("Counts are rows in the filtered best-record trend cohort. Rows show bins (B10→B1) and columns show years.")
        count_transposed = count.T.reindex(BIN_ORDER[::-1])
        count_transposed.index.name = "PercentileBin"
        st.dataframe(count_transposed.reset_index(), use_container_width=True)

        st.markdown("**Figure 6. Bin composition within each NMAT year**")
        st.caption("This figure shows within-year percentile-bin composition (percent). B8–B10 is the upper segment and B1–B3 the lower segment.")
        st.plotly_chart(make_stacked_pct_bar(pct, "Bin Composition by Year", "Year", "Percent", BIN_COLORS), use_container_width=True, key="fig_t4_stacked_year")

        top = pct[["B8", "B9", "B10"]].sum(axis=1)
        bottom = pct[["B1", "B2", "B3"]].sum(axis=1)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=top.index.astype(str), y=top.values, mode="lines+markers", name="Top B8-B10", line=dict(color="#2e7d32", width=3)))
        fig.add_trace(go.Scatter(x=bottom.index.astype(str), y=bottom.values, mode="lines+markers", name="Bottom B1-B3", line=dict(color="#c62828", width=3)))
        fig.update_layout(title="Top vs Bottom Bin Share by Year", xaxis_title="Year", yaxis_title="Percent", height=420)
        st.markdown("**Figure 7. Top-bin versus bottom-bin share by NMAT year**")
        st.caption("This chart compares combined B8–B10 (top) versus B1–B3 (bottom) shares by year.")
        st.plotly_chart(fig, use_container_width=True, key="fig_t4_topbot")

    with dec_tab2:
        st.caption("Insight: Compare which university types are overrepresented in higher bins.")
        _, uni_pct = pct_table(dfuni, "UNI_TYPE", "PercentileBin", BIN_ORDER)
        uni_pct.index.name = "UNI_TYPE"
        st.markdown("**Figure 8. Percentile-bin distribution by university type**")
        st.caption("Heatmap values are within-type percentages.")
        st.plotly_chart(make_heatmap(uni_pct, "Bin Distribution by University Type", "Bin", "University type"), use_container_width=True, key="fig_t4_heatmap_uni")

        top_uni = uni_pct[["B8", "B9", "B10"]].sum(axis=1)
        st.markdown("**Figure 9. Share of examinees in B8–B10 by university type**")
        st.caption("The bar chart highlights representation in the top three bins (B8–B10) by university type.")
        st.plotly_chart(make_top_share_bar(top_uni, "Top Bin Share by University Type", "Percent in B8-B10", "University type", PALETTE_UNI), use_container_width=True, key="fig_t4_top_uni")

        contingency, expected, chi_summary = chi_square_unitype_bin(dfuni.dropna(subset=["UNI_TYPE", "PercentileBin"]))
        st.markdown("**Table 11. Chi-square test for association between university type and percentile bin**")
        st.caption("The chi-square table tests whether bin composition differs by university type beyond random variation.")
        st.dataframe(chi_summary, use_container_width=True)

        st.divider()
        st.subheader("Bin distribution per year by university type")
        st.caption("Each facet shows one university type. Bars are stacked by percentile bin so you can see how Foreign, Public, and Private examinees are distributed each year.")

        _dq_con = duckdb.connect()
        _dq_con.register("_yr_uni_src", dfuni)
        _yr_uni_dec = _dq_con.execute("""
            SELECT
                CAST(Year AS INTEGER) AS Year,
                UNI_TYPE,
                PercentileBin,
                COUNT(*) AS n
            FROM _yr_uni_src
            WHERE UNI_TYPE IN ('Public', 'Private', 'Foreign')
              AND PercentileBin IS NOT NULL
              AND Year IS NOT NULL
            GROUP BY Year, UNI_TYPE, PercentileBin
            ORDER BY Year, UNI_TYPE, PercentileBin
        """).df()
        _dq_con.close()

        if _yr_uni_dec.empty:
            st.info("No data available for this chart under the current filters.")
        else:
            _yr_uni_dec["PercentileBin"] = pd.Categorical(
                _yr_uni_dec["PercentileBin"], categories=BIN_ORDER, ordered=True
            )
            _yr_uni_dec = _yr_uni_dec.sort_values(["Year", "UNI_TYPE", "PercentileBin"])
            _yr_uni_dec["Year"] = _yr_uni_dec["Year"].astype(str)

            _fig_yr_uni = px.bar(
                _yr_uni_dec,
                x="Year",
                y="n",
                color="PercentileBin",
                facet_col="UNI_TYPE",
                barmode="stack",
                title="Examinees per bin by year and university type",
                labels={"n": "Examinees", "Year": "Year", "PercentileBin": "Bin"},
                color_discrete_map=BIN_COLORS,
                category_orders={"PercentileBin": BIN_ORDER},
            )
            _fig_yr_uni.update_layout(height=520)
            _fig_yr_uni.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
            st.markdown("**Figure: Bin composition per year — Foreign vs Public vs Private**")
            st.caption("Counts are filtered best-record trend examinees. Use this chart to compare year-to-year shifts within each university type.")
            st.plotly_chart(_fig_yr_uni, use_container_width=True, key="fig_t4_yr_uni_bin_facet")

        st.divider()
        st.subheader("Record-level listings by university type")
        st.caption("Browse all examinees under each university type. Sorted by year (newest first) then percentile rank (highest first).")

        _rec_tab_foreign, _rec_tab_public, _rec_tab_private = st.tabs(
            ["🌐 Foreign", "🏛️ Public", "🏫 Private"]
        )
        _rec_display_cols = [
            c for c in [
                "PERSON_KEY", "APPNO_CLEAN", "UNIVERSITY", "UNI_LOCATION",
                "Year", "CourseGroup", "PercentileBin", "NMS_PER_num", "TotalRawScoreTRUE",
            ]
            if c in dfuni.columns
        ]
        _rec_col_sql = ", ".join([f'"{c}"' for c in _rec_display_cols])
        _rec_con = duckdb.connect()
        _rec_con.register("_rec_src", dfuni)

        for _rtab, _utype in [
            (_rec_tab_foreign, "Foreign"),
            (_rec_tab_public, "Public"),
            (_rec_tab_private, "Private"),
        ]:
            with _rtab:
                _recs = _rec_con.execute(f"""
                    SELECT {_rec_col_sql}
                    FROM _rec_src
                    WHERE UNI_TYPE = '{_utype}'
                    ORDER BY CAST(Year AS INTEGER) DESC NULLS LAST,
                             NMS_PER_num DESC NULLS LAST
                """).df()
                if _recs.empty:
                    st.info(f"No {_utype} university examinees found under the current filters.")
                else:
                    st.caption(
                        f"{len(_recs):,} {_utype} examinee records. "
                        "Sorted by year (newest first) and percentile rank (highest first)."
                    )
                    st.dataframe(_recs, use_container_width=True, hide_index=True)

        _rec_con.close()

        st.divider()
        st.subheader("No PLE match — record listings by university type")
        st.caption(
            "Records shown here belong to the observable best-record cohort (Year ≤ 2014) "
            "and have **no confirmed PLE match** (IS_PLE_ANALYSIS_SAFE ≠ True). "
            "The observable cohort is used because examinees from later years cannot yet be "
            "classified as non-passers."
        )

        _nople_df = F["uniobservable"]

        _nople_tab_foreign, _nople_tab_public, _nople_tab_private = st.tabs(
            ["🌐 Foreign", "🏛️ Public", "🏫 Private"]
        )
        _nople_display_cols = [
            c for c in [
                "PERSON_KEY", "APPNO_CLEAN", "UNIVERSITY", "UNI_LOCATION",
                "Year", "CourseGroup", "PercentileBin", "NMS_PER_num",
                "TotalRawScoreTRUE", "PLE_STATUS_LABEL",
            ]
            if c in _nople_df.columns
        ]
        _nople_col_sql = ", ".join([f'"{c}"' for c in _nople_display_cols])
        _nople_con = duckdb.connect()
        _nople_con.register("_nople_src", _nople_df)

        for _ntab, _utype in [
            (_nople_tab_foreign, "Foreign"),
            (_nople_tab_public, "Public"),
            (_nople_tab_private, "Private"),
        ]:
            with _ntab:
                _nople_recs = _nople_con.execute(f"""
                    SELECT {_nople_col_sql}
                    FROM _nople_src
                    WHERE UNI_TYPE = '{_utype}'
                      AND PLE_STATUS_LABEL = 'No confirmed PLE match'
                    ORDER BY CAST(Year AS INTEGER) DESC NULLS LAST,
                             NMS_PER_num DESC NULLS LAST
                """).df()
                if _nople_recs.empty:
                    st.info(
                        f"No {_utype} university examinees without a PLE match found "
                        "under the current filters and observable cohort window."
                    )
                else:
                    st.caption(
                        f"{len(_nople_recs):,} {_utype} examinee records with no confirmed PLE match. "
                        "Sorted by year (newest first) and percentile rank (highest first)."
                    )
                    st.dataframe(_nople_recs, use_container_width=True, hide_index=True)

        _nople_con.close()

        # ── Pseudo-citizenship profile ─────────────────────────────────────
        st.divider()
        st.subheader("Pseudo-citizenship profile for no-PLE-match examinees")
        st.caption(
            "This subsection uses APPNOCLEAN to link the no-PLE-match profiling file to the "
            "NMAT_Ultima analytic records. Pseudo-citizenship comes only from the profiling CSV, "
            "while all scores, bins, year, university type, and background fields come from "
            "the parquet-based dashboard dataset."
        )

        if not _PC_LOOKUP_AVAILABLE:
            st.info(
                "Pseudo-citizenship profiling file not found. "
                "Place pseudo_citizenship_profiling_FINAL.csv in the dataset/ folder."
            )
        else:
            _pc_base = _uniobs_pc[
                (_uniobs_pc["PLE_STATUS_LABEL"] == "No confirmed PLE match")
                & (_uniobs_pc["pseudo_citizenship"].notna())
            ].copy()

            if _pc_base.empty:
                st.info("No profiled no-PLE-match records match the current filters.")
            else:
                _pc_foreigners = int((_pc_base["override_applied"] == "FOREIGN").sum())
                _pc_filipinos = int((_pc_base["pseudo_citizenship"] == "Filipino").sum())
                _pc_distinct = int(_pc_base["pseudo_citizenship"].nunique())

                _pm1, _pm2, _pm3, _pm4 = st.columns(4)
                _pm1.metric("Profiled no-PLE-match records", f"{len(_pc_base):,}")
                _pm2.metric("Foreigners", f"{_pc_foreigners:,}")
                _pm3.metric("Filipinos", f"{_pc_filipinos:,}")
                _pm4.metric("Distinct pseudo-citizenship labels", f"{_pc_distinct:,}")

                # ── citizenship counts (reused in multiple charts) ──────────
                _pc_counts = (
                    _pc_base["pseudo_citizenship"]
                    .value_counts()
                    .reset_index()
                )
                _pc_counts.columns = ["pseudo_citizenship", "n"]

                # Pie charts side-by-side ─────────────────────────────────────
                _pp1, _pp2 = st.columns(2)

                with _pp1:
                    st.markdown("**Pseudo-citizenship composition**")
                    _fig_pc_pie = px.pie(
                        _pc_counts,
                        names="pseudo_citizenship",
                        values="n",
                        title="Pseudo-citizenship composition",
                    )
                    st.plotly_chart(_fig_pc_pie, use_container_width=True, key="fig_pc_pie_comp")

                with _pp2:
                    st.markdown("**Foreigners vs Filipinos**")
                    _pc_fvf_counts = pd.DataFrame({
                        "group": ["Foreigner", "Filipino"],
                        "n": [_pc_foreigners, _pc_filipinos],
                    })
                    _fig_pc_fvf = px.pie(
                        _pc_fvf_counts,
                        names="group",
                        values="n",
                        title="Foreigners vs Filipinos in profiled no-PLE-match set",
                        color_discrete_map={
                            "Foreigner": PALETTE_UNI.get("Foreign", "#9467bd"),
                            "Filipino": PALETTE_UNI.get("Public", "#1f77b4"),
                        },
                    )
                    st.plotly_chart(_fig_pc_fvf, use_container_width=True, key="fig_pc_pie_fvf")

                # Top-15 horizontal bar ───────────────────────────────────────
                st.markdown("**Top pseudo-citizenship groups by count**")
                _top15 = _pc_counts.head(15).sort_values("n")
                _fig_pc_top15 = go.Figure(go.Bar(
                    x=_top15["n"],
                    y=_top15["pseudo_citizenship"],
                    orientation="h",
                    text=_top15["n"].astype(str),
                    textposition="outside",
                    marker_color=PALETTE_UNI.get("Foreign", "#9467bd"),
                    hovertemplate="Citizenship: %{y}<br>Count: %{x}<extra></extra>",
                ))
                _fig_pc_top15.update_layout(
                    title="Top 15 pseudo-citizenship groups",
                    xaxis_title="Examinees",
                    yaxis_title="",
                    height=max(380, len(_top15) * 30),
                )
                st.plotly_chart(_fig_pc_top15, use_container_width=True, key="fig_pc_top15_bar")

                # Stacked % bar: decile composition by citizenship ────────────
                st.markdown("**Bin composition by pseudo-citizenship (top 15 groups)**")
                _pc_top_grps = _pc_counts.head(15)["pseudo_citizenship"].tolist()
                _pc_dec_base = _pc_base[_pc_base["pseudo_citizenship"].isin(_pc_top_grps)].copy()
                if not _pc_dec_base.empty and "PercentileBin" in _pc_dec_base.columns:
                    _, _pc_dec_pct = pct_table(_pc_dec_base, "pseudo_citizenship", "PercentileBin", BIN_ORDER)
                    _pc_dec_pct.index.name = "pseudo_citizenship"
                    _fig_pc_dec = make_stacked_pct_bar(
                        _pc_dec_pct,
                        "Bin composition by pseudo-citizenship",
                        "Pseudo-citizenship",
                        "Percent",
                        BIN_COLORS,
                    )
                    _fig_pc_dec.update_layout(height=520)
                    st.plotly_chart(_fig_pc_dec, use_container_width=True, key="fig_pc_bin_stacked")

                    st.markdown("**Full percentile-bin heatmap by pseudo-citizenship (all bins B1–B10)**")
                    st.caption(
                        "Each row is one pseudo-citizenship group; each column is one percentile bin. "
                        "Values are row percentages — read across a row to see where that group clusters "
                        "across the full score distribution, from the bottom (B1) to the top (B10). "
                        "Red tones flag higher concentration in that bin."
                    )
                    _fig_pc_hm_all = make_heatmap(
                        _pc_dec_pct,
                        "Full bin profile by pseudo-citizenship (row %)",
                        "Percentile bin",
                        "Pseudo-citizenship",
                        "YlOrRd",
                    )
                    _fig_pc_hm_all.update_layout(height=max(450, len(_pc_top_grps) * 32 + 120))
                    st.plotly_chart(_fig_pc_hm_all, use_container_width=True, key="fig_pc_bin_heatmap_all")

                # Top-decile share bar  +  percentile box plot ────────────────
                _pb1, _pb2 = st.columns(2)

                with _pb1:
                    st.markdown("**Top-bin share (B8–B10) by pseudo-citizenship**")
                    if "PercentileBin" in _pc_base.columns:
                        _pc_top_dec = (
                            _pc_base
                            .assign(_is_top=_pc_base["PercentileBin"].isin(["B8", "B9", "B10"]))
                            .groupby("pseudo_citizenship", observed=True)
                            .agg(n=("_is_top", "size"), top_n=("_is_top", "sum"))
                            .reset_index()
                        )
                        _pc_top_dec["top_dec_pct"] = (
                            _pc_top_dec["top_n"] / _pc_top_dec["n"].replace(0, np.nan) * 100
                        ).fillna(0).round(1)
                        _pc_top_dec = _pc_top_dec[_pc_top_dec["n"] >= 3].sort_values("top_dec_pct")
                        if not _pc_top_dec.empty:
                            _fig_pc_topdec = go.Figure(go.Bar(
                                x=_pc_top_dec["top_dec_pct"],
                                y=_pc_top_dec["pseudo_citizenship"],
                                orientation="h",
                                text=[f"{v:.1f}%" for v in _pc_top_dec["top_dec_pct"]],
                                textposition="outside",
                                marker_color=BIN_COLORS["B10"],
                                hovertemplate="Citizenship: %{y}<br>B8-B10 share: %{x:.1f}%<extra></extra>",
                            ))
                            _fig_pc_topdec.update_layout(
                                title="Top-bin share (B8–B10)",
                                xaxis_title="% in B8–B10",
                                yaxis_title="",
                                height=max(360, len(_pc_top_dec) * 30),
                            )
                            st.plotly_chart(_fig_pc_topdec, use_container_width=True, key="fig_pc_topbin_bar")

                with _pb2:
                    st.markdown("**Percentile rank by pseudo-citizenship (n ≥ 5)**")
                    if "NMS_PER_num" in _pc_base.columns:
                        _pc_big = _pc_base.groupby("pseudo_citizenship", observed=True).filter(
                            lambda x: len(x) >= 5
                        )
                        if not _pc_big.empty:
                            _fig_pc_box_pct = px.box(
                                _pc_big,
                                x="pseudo_citizenship",
                                y="NMS_PER_num",
                                points=False,
                                title="Percentile rank by pseudo-citizenship (n ≥ 5)",
                                labels={"NMS_PER_num": "Percentile rank", "pseudo_citizenship": ""},
                            )
                            _fig_pc_box_pct.update_layout(height=430)
                            st.plotly_chart(_fig_pc_box_pct, use_container_width=True, key="fig_pc_box_pct")

                # TRUE raw score box plot ──────────────────────────────────────
                st.markdown("**TRUE raw score by pseudo-citizenship (n ≥ 5)**")
                if "TotalRawScoreTRUE" in _pc_base.columns:
                    _pc_big_raw = _pc_base.groupby("pseudo_citizenship", observed=True).filter(
                        lambda x: len(x) >= 5
                    )
                    if not _pc_big_raw.empty:
                        _fig_pc_box_raw = px.box(
                            _pc_big_raw,
                            x="pseudo_citizenship",
                            y="TotalRawScoreTRUE",
                            points=False,
                            title="TRUE raw score by pseudo-citizenship (n ≥ 5)",
                            labels={"TotalRawScoreTRUE": "Total raw score", "pseudo_citizenship": ""},
                        )
                        _fig_pc_box_raw.update_layout(height=430)
                        st.plotly_chart(_fig_pc_box_raw, use_container_width=True, key="fig_pc_box_raw")

                # ── Summary tables ────────────────────────────────────────────
                st.markdown("**Summary by pseudo-citizenship**")
                _pc_base["_is_top_d"] = _pc_base["PercentileBin"].isin(["B8", "B9", "B10"]) if "PercentileBin" in _pc_base.columns else False
                _pc_base["_is_bot_d"] = _pc_base["PercentileBin"].isin(["B1", "B2", "B3"]) if "PercentileBin" in _pc_base.columns else False
                _pc_summary = (
                    _pc_base
                    .groupby("pseudo_citizenship", observed=True)
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
                _pc_summary["top_decile_pct"] = (
                    _pc_summary["top_decile_n"] / _pc_summary["n_examinees"].replace(0, np.nan) * 100
                ).fillna(0).round(2)
                _pc_summary["bottom_decile_pct"] = (
                    _pc_summary["bottom_decile_n"] / _pc_summary["n_examinees"].replace(0, np.nan) * 100
                ).fillna(0).round(2)
                _pc_summary["top_decile_n"] = _pc_summary["top_decile_n"].astype(int)
                _pc_summary["bottom_decile_n"] = _pc_summary["bottom_decile_n"].astype(int)
                _pc_summary = _pc_summary[
                    ["pseudo_citizenship", "n_examinees", "median_percentile_rank",
                     "median_true_raw_score", "top_decile_n", "top_decile_pct",
                     "bottom_decile_n", "bottom_decile_pct"]
                ].sort_values(["n_examinees", "median_percentile_rank"], ascending=[False, False])
                st.dataframe(_pc_summary, use_container_width=True, hide_index=True)

                _pt1, _pt2 = st.columns(2)
                with _pt1:
                    st.markdown("**Summary by pseudo-citizenship and university type**")
                    if "UNI_TYPE" in _pc_base.columns:
                        _pc_uni_sum = (
                            _pc_base
                            .groupby(["pseudo_citizenship", "UNI_TYPE"], observed=True)
                            .agg(
                                n=("APPNO_CLEAN", "count"),
                                median_percentile_rank=("NMS_PER_num", "median"),
                                median_true_raw_score=("TotalRawScoreTRUE", "median"),
                            )
                            .round(2)
                            .reset_index()
                        )
                        st.dataframe(_pc_uni_sum, use_container_width=True, hide_index=True)

                with _pt2:
                    st.markdown("**Summary by pseudo-citizenship and course group**")
                    if "CourseGroup" in _pc_base.columns:
                        _pc_course_sum = (
                            _pc_base
                            .groupby(["pseudo_citizenship", "CourseGroup"], observed=True)
                            .agg(
                                n=("APPNO_CLEAN", "count"),
                                median_percentile_rank=("NMS_PER_num", "median"),
                                median_true_raw_score=("TotalRawScoreTRUE", "median"),
                            )
                            .round(2)
                            .reset_index()
                        )
                        st.dataframe(_pc_course_sum, use_container_width=True, hide_index=True)

                st.markdown("**Year distribution by pseudo-citizenship**")
                if "Year" in _pc_base.columns:
                    _pc_year_tbl = (
                        _pc_base
                        .groupby(["pseudo_citizenship", "Year"], observed=True)
                        .size()
                        .unstack(fill_value=0)
                    )
                    _pc_year_tbl.index.name = "pseudo_citizenship"
                    st.dataframe(_pc_year_tbl.reset_index(), use_container_width=True, hide_index=True)

                st.markdown("**Matched no-PLE-match records with pseudo-citizenship**")
                _pc_rec_cols = [c for c in [
                    "pseudo_citizenship", "override_applied", "name_based_assessment",
                    "PERSON_KEY", "APPNO_CLEAN", "UNIVERSITY", "UNI_LOCATION", "UNI_TYPE",
                    "Year", "CourseGroup", "PercentileBin", "NMS_PER_num",
                    "TotalRawScoreTRUE", "PLE_STATUS_LABEL",
                ] if c in _pc_base.columns]
                _pc_rec_df = (
                    _pc_base[_pc_rec_cols]
                    .sort_values(
                        ["pseudo_citizenship", "Year", "NMS_PER_num"],
                        ascending=[True, False, False],
                    )
                )
                st.caption(
                    f"{len(_pc_rec_df):,} matched records. "
                    "Sorted by pseudo-citizenship (A→Z), year (newest first), "
                    "percentile rank (highest first)."
                )
                st.dataframe(_pc_rec_df, use_container_width=True, hide_index=True)

                # ── Comparative analysis: foreigners vs Filipino students ──────
                st.divider()
                st.subheader("Comparative analysis: foreigners vs Filipino students")
                st.caption(
                    "Compares (1) actual foreigners (non-Filipino, identified via the profiling CSV), "
                    "(2) Filipinos who attended foreign/international schools, "
                    "(3) all students at public schools, and "
                    "(4) all students at private schools. "
                    "Groups 1 and 2 come from the profiling-matched observable university subset. "
                    "Groups 3 and 4 use all observable best-record examinees at those institution types. "
                    "All groups reflect the current sidebar filters."
                )

                _cmp_parts = []

                _g_for = _uniobs_pc[_uniobs_pc["override_applied"] == "FOREIGN"].copy()
                if not _g_for.empty:
                    _g_for["_cmp_group"] = "Foreigners (non-Filipino)"
                    _cmp_parts.append(_g_for)

                _g_fil_for = _uniobs_pc[
                    (_uniobs_pc["pseudo_citizenship"] == "Filipino") &
                    (_uniobs_pc["UNI_TYPE"] == "Foreign")
                ].copy()
                if not _g_fil_for.empty:
                    _g_fil_for["_cmp_group"] = "Filipinos (foreign schools)"
                    _cmp_parts.append(_g_fil_for)

                _g_pub = F["bestobservable"][F["bestobservable"]["UNI_TYPE"] == "Public"].copy()
                if not _g_pub.empty:
                    _g_pub["_cmp_group"] = "Filipinos (public schools)"
                    _cmp_parts.append(_g_pub)

                _g_prv = F["bestobservable"][F["bestobservable"]["UNI_TYPE"] == "Private"].copy()
                if not _g_prv.empty:
                    _g_prv["_cmp_group"] = "Filipinos (private schools)"
                    _cmp_parts.append(_g_prv)

                if not _cmp_parts:
                    st.info("No comparative data available under the current filters. Ensure Public and/or Private university types are included.")
                else:
                    _cmp_score_cols = [
                        "_cmp_group", "NMS_PER_num", "TotalRawScoreTRUE",
                        "PartIRawScoreTRUE", "PartIIRawScoreTRUE",
                        "PercentileBin", "HAS_CONFIRMED_PLE",
                    ]
                    _cmp_df = pd.concat(
                        [p[[c for c in _cmp_score_cols if c in p.columns]] for p in _cmp_parts],
                        ignore_index=True,
                    )

                    # Summary table ───────────────────────────────────────────
                    st.markdown("**Summary: key score indicators by comparison group**")
                    st.caption(
                        "PLE pass rate uses IS_PLE_ANALYSIS_SAFE. "
                        "Foreigners typically show 0% or near-0% because foreign nationals rarely "
                        "sit Philippine licensure exams."
                    )
                    _cmp_agg = (
                        _cmp_df.groupby("_cmp_group", observed=True)
                        .agg(
                            n=("NMS_PER_num", "count"),
                            median_percentile_rank=("NMS_PER_num", "median"),
                            q25_pct=("NMS_PER_num", lambda x: x.quantile(0.25)),
                            q75_pct=("NMS_PER_num", lambda x: x.quantile(0.75)),
                            median_raw_score=("TotalRawScoreTRUE", "median"),
                        )
                        .round(2)
                        .reset_index()
                        .rename(columns={"_cmp_group": "Group"})
                    )
                    if "HAS_CONFIRMED_PLE" in _cmp_df.columns:
                        _cmp_df["_ple_num"] = (_cmp_df["HAS_CONFIRMED_PLE"] == True).astype(float)
                        _ple_rates = (
                            _cmp_df.groupby("_cmp_group", observed=True)["_ple_num"]
                            .mean()
                            .mul(100)
                            .round(2)
                            .reset_index()
                            .rename(columns={"_cmp_group": "Group", "_ple_num": "PLE pass rate %"})
                        )
                        _cmp_agg = _cmp_agg.merge(_ple_rates, on="Group", how="left")
                    st.dataframe(_cmp_agg, use_container_width=True, hide_index=True)

                    # Boxplots ─────────────────────────────────────────────────
                    _bcol1, _bcol2 = st.columns(2)
                    with _bcol1:
                        st.markdown("**Percentile rank distribution by group**")
                        _cmp_pct_plot = _cmp_df.dropna(subset=["NMS_PER_num"]).copy()
                        if not _cmp_pct_plot.empty:
                            _fig_cmp_pct = px.box(
                                _cmp_pct_plot,
                                x="_cmp_group",
                                y="NMS_PER_num",
                                color="_cmp_group",
                                points=False,
                                title="Percentile rank: foreigners vs Filipinos",
                                labels={"NMS_PER_num": "Percentile rank", "_cmp_group": ""},
                            )
                            _fig_cmp_pct.update_layout(height=460, showlegend=False, xaxis_tickangle=-20)
                            st.plotly_chart(_fig_cmp_pct, use_container_width=True, key="fig_cmp_pct_box")

                    with _bcol2:
                        st.markdown("**TRUE raw score distribution by group**")
                        _cmp_raw_plot = _cmp_df.dropna(subset=["TotalRawScoreTRUE"]).copy()
                        if not _cmp_raw_plot.empty:
                            _fig_cmp_raw = px.box(
                                _cmp_raw_plot,
                                x="_cmp_group",
                                y="TotalRawScoreTRUE",
                                color="_cmp_group",
                                points=False,
                                title="TRUE raw score: foreigners vs Filipinos",
                                labels={"TotalRawScoreTRUE": "Total raw score", "_cmp_group": ""},
                            )
                            _fig_cmp_raw.update_layout(height=460, showlegend=False, xaxis_tickangle=-20)
                            st.plotly_chart(_fig_cmp_raw, use_container_width=True, key="fig_cmp_raw_box")

                    # Full bin heatmap ─────────────────────────────────────────
                    if "PercentileBin" in _cmp_df.columns:
                        _cmp_bin_cnt, _cmp_bin_pct = pct_table(
                            _cmp_df.dropna(subset=["_cmp_group", "PercentileBin"]),
                            "_cmp_group",
                            "PercentileBin",
                            BIN_ORDER,
                        )
                        _cmp_bin_pct.index.name = "_cmp_group"

                        st.markdown("**Full bin heatmap: foreigners vs Filipino groups (all bins B1–B10)**")
                        st.caption(
                            "Row percentages show the full distribution of each group across all ten "
                            "percentile bins. Compare rows to see which groups skew high (B8–B10) "
                            "or low (B1–B3). Green tones indicate higher percentage in that bin."
                        )
                        _fig_cmp_hm = make_heatmap(
                            _cmp_bin_pct,
                            "Bin distribution by comparison group (row %)",
                            "Percentile bin",
                            "Group",
                            "RdYlGn",
                        )
                        _fig_cmp_hm.update_layout(height=400)
                        st.plotly_chart(_fig_cmp_hm, use_container_width=True, key="fig_cmp_all_bins_hm")

                        # Stacked bar
                        st.markdown("**Bin composition by group (stacked %)**")
                        _cmp_bin_pct_labeled = _cmp_bin_pct.copy()
                        _cmp_bin_pct_labeled.index.name = "Group"
                        _fig_cmp_stk = make_stacked_pct_bar(
                            _cmp_bin_pct_labeled,
                            "Bin composition: foreigners vs Filipinos",
                            "Group",
                            "Percent",
                            BIN_COLORS,
                        )
                        _fig_cmp_stk.update_layout(height=480)
                        st.plotly_chart(_fig_cmp_stk, use_container_width=True, key="fig_cmp_stk_bar")

                        # Top vs bottom grouped bar
                        st.markdown("**Top-bin (B8–B10) vs bottom-bin (B1–B3) share by group**")
                        _cmp_topbot = pd.DataFrame({
                            "Group": _cmp_bin_pct.index.tolist(),
                            "Top B8–B10 (%)": _cmp_bin_pct[["B8", "B9", "B10"]].sum(axis=1).values,
                            "Bottom B1–B3 (%)": _cmp_bin_pct[["B1", "B2", "B3"]].sum(axis=1).values,
                        })
                        _cmp_topbot_long = _cmp_topbot.melt(
                            id_vars="Group", var_name="Segment", value_name="Percent"
                        )
                        _fig_cmp_topbot = px.bar(
                            _cmp_topbot_long,
                            x="Group",
                            y="Percent",
                            color="Segment",
                            barmode="group",
                            title="Top vs bottom bin share by group",
                            color_discrete_map={
                                "Top B8–B10 (%)": "#2e7d32",
                                "Bottom B1–B3 (%)": "#c62828",
                            },
                            labels={"Group": "", "Percent": "Percent", "Segment": ""},
                        )
                        _fig_cmp_topbot.update_layout(height=420, xaxis_tickangle=-15)
                        st.plotly_chart(_fig_cmp_topbot, use_container_width=True, key="fig_cmp_topbot_grouped")

                        st.markdown("**Bin distribution table: all groups (row %)**")
                        st.dataframe(
                            _cmp_bin_pct.reset_index().rename(columns={"_cmp_group": "Group"}),
                            use_container_width=True,
                            hide_index=True,
                        )

    with dec_tab3:
        st.caption("Insight: Compare bin profiles across pre-med backgrounds.")
        _, course_pct = pct_table(df, "CourseGroup", "PercentileBin", BIN_ORDER)
        course_pct.index.name = "CourseGroup"
        st.markdown("**Figure 10. Percentile-bin distribution by course group**")
        st.caption("Heatmap values are within-course-group percentages.")
        st.plotly_chart(make_heatmap(course_pct, "Bin Distribution by Course Group", "Bin", "Course group", "OrRd"), use_container_width=True, key="fig_t4_heatmap_course")

        top_course = course_pct[["B8", "B9", "B10"]].sum(axis=1)
        st.markdown("**Figure 11. Share of examinees in B8–B10 by course group**")
        st.caption("The bar chart highlights representation in the top three bins by course group.")
        st.plotly_chart(make_top_share_bar(top_course, "Top Bin Share by Course Group", "Percent in B8-B10", "Course group", PALETTE_COURSE), use_container_width=True, key="fig_t4_top_course")

        course_desc = (
            df.groupby("CourseGroup", observed=True)["NMS_PER_num"]
            .agg(n="count", median="median", q25=lambda x: x.quantile(0.25), q75=lambda x: x.quantile(0.75))
            .round(2)
            .reset_index()
        )
        st.markdown("**Table 12. Percentile summary by course group**")
        st.caption("Values show sample size, median percentile rank, and interquartile range for each course group.")
        st.dataframe(course_desc, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 5
# -----------------------------------------------------------------------------
with tab5:
    st.subheader("Institutional Profile: University Type and Location")
    st.caption("This page focuses on the institutional comparison subset used in the analysis pipeline: Public, Private, and Foreign university types, with location shown as Local or International where available.")

    base = F["uni"].copy()
    uni_base = base.dropna(subset=["UNI_TYPE", "UNI_LOCATION", "PercentileBin"]).copy()

    if uni_base.empty:
        st.info("No university-type records are available under the current filters.")
    else:
        st.caption("Insight: This page follows the institutional comparison subset (Public, Private, Foreign) from the analysis pipeline.")
        type_loc = uni_base.groupby(["UNI_TYPE", "UNI_LOCATION"], observed=True).size().reset_index(name="Count")
        type_loc["Percent of total"] = (type_loc["Count"] / type_loc["Count"].sum() * 100).round(2)
        st.markdown("**Table 13. Institution type by location mix**")
        st.caption("Values show counts and percentages of examinees within each institutional classification.")
        st.dataframe(type_loc.sort_values(["UNI_TYPE", "UNI_LOCATION"]), use_container_width=True)

        st.markdown("**Table 14. Institution type by location matrix**")
        st.caption("Row percentages describe the location mix within each university type. Column percentages show composition within each location.")
        inst_count = pd.crosstab(uni_base["UNI_TYPE"], uni_base["UNI_LOCATION"], margins=True)
        inst_pct_row = (pd.crosstab(uni_base["UNI_TYPE"], uni_base["UNI_LOCATION"], normalize="index") * 100).round(2)
        inst_pct_col = (pd.crosstab(uni_base["UNI_TYPE"], uni_base["UNI_LOCATION"], normalize="columns") * 100).round(2)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Counts (with totals)**")
            st.dataframe(inst_count, use_container_width=True)
            st.markdown("**Row percentages: within UNI_TYPE**")
            st.dataframe(inst_pct_row, use_container_width=True)
        with c2:
            st.markdown("**Column percentages: within UNI_LOCATION**")
            st.dataframe(inst_pct_col, use_container_width=True)

        inst_decile = (
            uni_base.dropna(subset=["UNI_TYPE", "UNI_LOCATION", "PercentileBin"])
            .groupby(["UNI_TYPE", "UNI_LOCATION", "PercentileBin"], observed=True)
            .size()
            .unstack(fill_value=0)
            .reindex(columns=BIN_ORDER, fill_value=0)
        )
        if not inst_decile.empty:
            st.markdown("**Figure 12. Percentile-bin distribution by institution type and location**")
            st.caption("Each row in the heatmap is one institution type-location combination.")
            inst_decile_pct = inst_decile.div(inst_decile.sum(axis=1).replace(0, np.nan), axis=0).mul(100).fillna(0).round(2)
            inst_decile_pct.index = [f"{u} ({l})" for u, l in inst_decile_pct.index]
            st.plotly_chart(
                make_heatmap(
                    inst_decile_pct,
                    "Bin Distribution by Institution Type x Location",
                    "Percentile Bin",
                    "Institution classification",
                    "Blues",
                ),
                use_container_width=True,
                key="fig_t5_heatmap_instloc",
            )

            top_by_inst = inst_decile_pct[["B8", "B9", "B10"]].sum(axis=1).sort_values()
            st.markdown("**Figure 13. Top-bin representation by institution type and location**")
            st.caption("Top-bin representation refers to the combined share in B8–B10.")
            st.plotly_chart(
                make_top_share_bar(
                    top_by_inst,
                    "Top Bin Representation by Institution Type x Location",
                    "Percent in B8-B10",
                    "Institution classification",
                    None,
                ),
                use_container_width=True,
                key="fig_t5_top_instloc",
            )

        st.markdown("**Figure 14. Bin composition by university type**")
        st.caption("Stacked percentages sum to 100% within each university type.")
        _, uni_decile_pct = pct_table(uni_base, "UNI_TYPE", "PercentileBin", BIN_ORDER)
        uni_decile_pct.index.name = "UNI_TYPE"
        st.plotly_chart(
            make_stacked_pct_bar(
                uni_decile_pct,
                "Bin Composition by University Type",
                "University type",
                "Percent",
                PALETTE_UNI,
            ),
            use_container_width=True,
            key="fig_t5_stacked_uni",
        )

        uni_decile_count, _ = pct_table(uni_base, "UNI_TYPE", "PercentileBin", BIN_ORDER)
        uni_decile_summary = uni_decile_count.copy()
        uni_decile_summary["Total students"] = uni_decile_summary.sum(axis=1)
        uni_decile_summary = uni_decile_summary.reset_index()
        st.markdown("**Table 15. Bin counts by university type**")
        st.caption("Values show counts of examinees by bin within each university type.")
        st.dataframe(uni_decile_summary, use_container_width=True)

        st.markdown("**Table 16. Foreign examinee summary**")
        st.caption("Foreign examinees are shown separately because they are a small but policy-relevant subgroup.")
        foreign = uni_base[uni_base["UNI_TYPE"].eq("Foreign")].copy()
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Foreign examinees", f"{len(foreign):,}")
        c2.metric("% of total", f"{(len(foreign) / max(len(uni_base), 1) * 100):.2f}%")
        c3.metric("Median percentile", f"{foreign['NMS_PER_num'].median():.1f}" if not foreign.empty else "n/a")
        c4.metric(
            "Top bin %",
            f"{(foreign['PercentileBin'].isin(['B8', 'B9', 'B10']).mean() * 100):.2f}%" if not foreign.empty else "n/a",
        )

        if not foreign.empty:
            _, foreign_pct = pct_table(foreign, "UNI_TYPE", "PercentileBin", BIN_ORDER)
            foreign_pct.index.name = "UNI_TYPE"
            st.markdown("**Figure 15. Bin distribution among foreign examinees**")
            st.caption("Values show counts and percentages for foreign examinees under the current filters.")
            st.plotly_chart(
                make_stacked_pct_bar(
                    foreign_pct,
                    "Foreign Examinees Bin Distribution",
                    "University type",
                    "Percent",
                    {"Foreign": PALETTE_UNI.get("Foreign", "#9467bd")},
                ),
                use_container_width=True,
                key="fig_t5_foreign_bin",
            )

        st.markdown("**Figure 16. Medical and allied versus other courses by university type**")
        st.caption("Stacked percentages sum to 100% within each university type.")
        med_other = uni_base.copy()
        med_other["Course bucket"] = np.where(med_other["CourseGroup"].eq("Medical & Allied"), "Medical & Allied", "Other Courses")
        med_tbl = (
            med_other.groupby(["UNI_TYPE", "Course bucket"], observed=True)
            .size()
            .unstack(fill_value=0)
            .reindex(columns=["Medical & Allied", "Other Courses"], fill_value=0)
        )
        med_pct = med_tbl.div(med_tbl.sum(axis=1).replace(0, np.nan), axis=0).mul(100).round(2)
        med_pct.index.name = "UNI_TYPE"
        st.plotly_chart(
            make_stacked_pct_bar(
                med_pct,
                "Medical & Allied vs Other Courses by University Type",
                "University type",
                "Percent",
                {"Medical & Allied": "#d62728", "Other Courses": "#7f7f7f"},
            ),
            use_container_width=True,
            key="fig_t5_med_course",
        )
        st.dataframe(med_pct.reset_index(), use_container_width=True)

        st.markdown("**Table 17. University listings by university type**")
        st.caption("Each university listing shows the standardized university name, cleaned location, and applicant count.")
        for uni_type in ["Public", "Private", "Foreign"]:
            table = (
                uni_base[uni_base["UNI_TYPE"] == uni_type]
                .groupby(["UNIVERSITY", "UNI_LOCATION"], observed=True)
                .agg(total_applicants=("APPNO_CLEAN", "count"))
                .reset_index()
                .sort_values("total_applicants", ascending=False)
            )
            with st.expander(f"{uni_type} Universities", expanded=False):
                st.dataframe(table, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 6
# -----------------------------------------------------------------------------
with tab6:
    st.subheader("Pathways from Background to NMAT Outcome")
    st.caption("Flow widths represent examinee counts moving from one background category to one score or outcome category under the current filters.")
    best = F["besttrend"]
    uni = F["uni"]
    observable = F["bestobservable"]

    flow_tab1, flow_tab2, flow_tab3, flow_tab4 = st.tabs(["University → Bin", "Course → Bin", "Bin → PLE", "Top pathways"])

    with flow_tab1:
        st.caption("Insight: Compare how Public, Private, and Foreign flows distribute across bins.")
        st.markdown("**Figure 17. Flow from university type to percentile bin**")
        st.caption("Each flow width represents the count of examinees moving from university type to percentile bin.")
        flow = make_flow(uni, "UNI_TYPE", "PercentileBin", ["Public", "Private", "Foreign"], BIN_ORDER)
        st.plotly_chart(
            make_sankey(flow, "UNI_TYPE", "PercentileBin", "University Type to Bin", None, None),
            use_container_width=True,
            key="fig_t6_sankey_uni",
        )
        st.markdown("**Table 18. University-type to bin flow counts**")
        st.caption("Each row in the flow table is one source-to-target pathway with its count.")
        st.dataframe(flow, use_container_width=True)

    with flow_tab2:
        st.caption("Insight: Compare which course groups feed higher versus lower bins.")
        st.markdown("**Figure 18. Flow from course group to percentile bin**")
        st.caption("Each flow width represents the count of examinees moving from course group to percentile bin.")
        order = [
            c
            for c in ["Medical & Allied", "Natural Sciences", "Social & Behavioral Sciences", "Education", "Engineering & Technology", "Other"]
            if c in best["CourseGroup"].unique()
        ]
        flow = make_flow(best, "CourseGroup", "PercentileBin", order, BIN_ORDER)
        st.plotly_chart(
            make_sankey(flow, "CourseGroup", "PercentileBin", "Course Group to Bin", None, None),
            use_container_width=True,
            key="fig_t6_sankey_course",
        )
        st.markdown("**Table 19. Course-group to bin flow counts**")
        st.caption("Each row in the flow table is one source-to-target pathway with its count.")
        st.dataframe(flow, use_container_width=True)

    with flow_tab3:
        st.caption("Insight: In the observable cohort, this shows how bins map to confirmed or unmatched PLE status.")
        st.markdown("**Figure 19. Flow from percentile bin to PLE status in the observable cohort**")
        st.caption("Bin-to-PLE flow uses only the observable best-record cohort.")
        flow = make_flow(observable, "PercentileBin", "PLE_STATUS_LABEL", BIN_ORDER, PLE_ORDER)
        st.plotly_chart(
            make_sankey(flow, "PercentileBin", "PLE_STATUS_LABEL", "Bin to PLE Status (Observable Cohort)", None, None),
            use_container_width=True,
            key="fig_t6_sankey_ple",
        )
        row_pct = (
            flow.pivot(index="PercentileBin", columns="PLE_STATUS_LABEL", values="count")
            .reindex(index=BIN_ORDER, columns=PLE_ORDER)
            .fillna(0)
        )
        row_pct = row_pct.div(row_pct.sum(axis=1).replace(0, np.nan), axis=0).mul(100).fillna(0).round(2)
        st.markdown("**Table 20. PLE status composition within each bin**")
        st.caption("Bin-to-PLE flow uses only the observable best-record cohort; values are percent within each bin.")
        st.dataframe(row_pct.reset_index(), use_container_width=True)

    with flow_tab4:
        st.caption("Insight: These are the largest pathways into top bins (B8-B10).")
        st.markdown("**Table 21. Largest university-type pathways into B8–B10**")
        top_deciles = ["B8", "B9", "B10"]
        top_uni = (
            uni[uni["PercentileBin"].isin(top_deciles)]
            .groupby(["UNI_TYPE", "PercentileBin"], observed=True)
            .size()
            .reset_index(name="Count")
            .sort_values("Count", ascending=False)
            .head(10)
        )
        top_course = (
            best[best["PercentileBin"].isin(top_deciles)]
            .groupby(["CourseGroup", "PercentileBin"], observed=True)
            .size()
            .reset_index(name="Count")
            .sort_values("Count", ascending=False)
            .head(10)
        )
        c1, c2 = st.columns(2)
        with c1:
            st.dataframe(top_uni, use_container_width=True)
        with c2:
            st.markdown("**Table 22. Largest course-group pathways into B8–B10**")
            st.caption("Top pathways highlight where high-bin representation is most concentrated by count, not by rate.")
            st.dataframe(top_course, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 7
# -----------------------------------------------------------------------------
with tab7:
    st.subheader("PLE Alignment of NMAT Performance")
    st.caption("This page examines how NMAT performance and background characteristics relate to confirmed PLE outcomes within the observable best-record cohort only.")
    df = F["bestobservable"]
    dfuni = F["uniobservable"]

    st.info("This page is restricted to the observable best-record cohort so later NMAT cohorts are not misclassified as non-passers before the licensure window is observable.")

    ple_tab1, ple_tab2, ple_tab3, ple_tab4 = st.tabs(["Status profile", "Bin profile", "Background links", "Policy tables"])

    with ple_tab1:
        st.markdown("**Table 23. Score profile by PLE status**")
        st.caption("Table 23 reports count, median, mean, and interquartile range for each score measure by PLE status.")
        desc_cols = ["TotalRawScoreTRUE", "PartIRawScoreTRUE", "PartIIRawScoreTRUE", "NMS_PER_num", "NMS_GPS", "NMS_APT", "NMS_SA"]
        desc_cols = [c for c in desc_cols if c in df.columns]
        desc = df.groupby("PLE_STATUS_LABEL", observed=True)[desc_cols].agg(["count", "median", "mean", lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)]).round(2)
        st.dataframe(desc, use_container_width=True)

        st.markdown("**Figure 20. TRUE raw score distribution by PLE status**")
        st.caption("The boxplot compares TRUE raw score distributions across confirmed and no-confirmed-match groups.")
        plot_df = df.dropna(subset=["PLE_STATUS_LABEL", "TotalRawScoreTRUE"]).copy()
        fig = px.box(plot_df, x="PLE_STATUS_LABEL", y="TotalRawScoreTRUE", color="PLE_STATUS_LABEL",
                     color_discrete_map=PALETTE_PLE, points=False, title="Total Raw Score by PLE Status")
        fig.update_layout(height=430, showlegend=False)
        st.plotly_chart(fig, use_container_width=True, key="fig_t7_box_raw_ple")

        st.markdown("**Table 24. Mann-Whitney comparison of confirmed passers versus no confirmed match**")
        st.caption("Table 24 compares only confirmed passers with the no-confirmed-match group and includes effect size.")
        mw = mann_whitney_ple(
            df,
            {
                "TotalRawScoreTRUE": "Total Raw Score",
                "PartIRawScoreTRUE": "Part I",
                "PartIIRawScoreTRUE": "Part II",
                "NMS_PER_num": "Percentile Rank",
                "NMS_GPS": "GPS Standard Score",
            },
        )
        st.dataframe(mw, use_container_width=True)

    with ple_tab2:
        st.markdown("**Figure 21. Bin distribution by PLE status**")
        st.caption("This chart reads within PLE status: how bins are distributed across each PLE-status group.")
        ple_dist_count, ple_dist_pct = pct_table(df, "PLE_STATUS_LABEL", "PercentileBin", BIN_ORDER)
        ple_dist_pct = ple_dist_pct.reindex(PLE_ORDER)
        ple_dist_pct.index.name = "PLE_STATUS_LABEL"
        st.plotly_chart(make_stacked_pct_bar(ple_dist_pct, "Bin Distribution by PLE Status", "PLE Status", "Percent", BIN_COLORS), use_container_width=True, key="fig_t7_bin_ple")

        st.markdown("**Figure 22. PLE status composition within each percentile bin**")
        st.caption("This chart reads within bin: how PLE statuses are distributed within each percentile bin.")
        decile_status = (
            df.dropna(subset=["PercentileBin", "PLE_STATUS_LABEL"]) 
            .groupby(["PercentileBin", "PLE_STATUS_LABEL"], observed=True)
            .size()
            .unstack(fill_value=0)
            .reindex(index=BIN_ORDER, columns=PLE_ORDER, fill_value=0)
        )
        decile_status_pct = decile_status.div(decile_status.sum(axis=1).replace(0, np.nan), axis=0).mul(100).fillna(0).round(2)
        decile_status_pct.index.name = "PercentileBin"
        st.plotly_chart(make_stacked_pct_bar(decile_status_pct, "PLE Status Composition within Each Bin", "Bin", "Percent within bin", PALETTE_PLE), use_container_width=True, key="fig_t7_ple_bin")
        st.markdown("**Table 25. Percent distribution of PLE status within each bin**")
        st.caption("Values show percent distribution of PLE status within each percentile bin.")
        st.dataframe(decile_status_pct.reset_index(), use_container_width=True)

    with ple_tab3:
        st.markdown("**Table 26. Course-group representation in the top bins**")
        st.caption("Top-bin survival here means the share of examinees in B8–B10, not a time-to-event survival model.")
        survival_base = F["besttrend"].dropna(subset=["CourseGroup", "PercentileBin"]).copy()
        survival_base["IS_TOP_BIN"] = survival_base["PercentileBin"].isin(["B8", "B9", "B10"])
        survival = (
            survival_base.groupby("CourseGroup", observed=True)
            .agg(total_examinees=("IS_TOP_BIN", "size"), top_decile_n=("IS_TOP_BIN", "sum"))
            .reset_index()
        )
        survival["top_decile_n"] = survival["top_decile_n"].astype(int)
        survival["survival_rate_pct"] = (survival["top_decile_n"] / survival["total_examinees"] * 100).round(2)
        survival = survival.sort_values(["survival_rate_pct", "top_decile_n"], ascending=[False, False])

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Figure 23. Share of examinees in B8–B10 by course group**")
            st.caption("Top-bin survival here means the share of examinees in B8–B10, not a time-to-event survival model.")
            st.dataframe(survival, use_container_width=True)
        with c2:
            st.plotly_chart(
                make_top_share_bar(
                    survival.set_index("CourseGroup")["survival_rate_pct"],
                    "Survival to Top Bins by Course Group",
                    "Percent in B8-B10",
                    "Course group",
                    PALETTE_COURSE,
                ),
                use_container_width=True,
                key="fig_t7_course_top_bin",
            )

        st.markdown("**Table 27. Confirmed PLE alignment by university type in the observable cohort**")
        st.caption("University-type policy table reports observable best records, confirmed passers, no confirmed match, and confirmed PLE share.")
        plelink_uni = (
            dfuni.groupby("UNI_TYPE", observed=True)
            .apply(lambda x: pd.Series({
                "n_observable_best_records": len(x),
                "confirmed_ple_passers": int(x["HAS_CONFIRMED_PLE"].sum()),
                "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
                "confirmed_ple_share_pct": round(x["HAS_CONFIRMED_PLE"].mean() * 100, 2),
            }))
            .reset_index()
        )
        st.dataframe(plelink_uni, use_container_width=True)

    with ple_tab4:
        policybase = df.copy()

        t_year = (
            policybase.groupby("Year", observed=True)
            .apply(lambda x: pd.Series({
                "n_observable_best_records": len(x),
                "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
                "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
                "confirmed_ple_share_pct": round((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2),
            }))
            .reset_index()
            .sort_values("Year")
        )

        t_course = (
            policybase.groupby("CourseGroup", observed=True)
            .apply(lambda x: pd.Series({
                "n_observable_best_records": len(x),
                "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
                "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
                "confirmed_ple_share_pct": round((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2),
                "median_percentile_rank": round(x["NMS_PER_num"].median(), 2),
            }))
            .reset_index()
            .sort_values("confirmed_ple_share_pct", ascending=False)
        )

        t_uni = (
            policybase[policybase["UNI_TYPE"].isin(["Public", "Private", "Foreign"])]
            .groupby("UNI_TYPE", observed=True)
            .apply(lambda x: pd.Series({
                "n_observable_best_records": len(x),
                "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
                "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
                "confirmed_ple_share_pct": round((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2),
                "median_percentile_rank": round(x["NMS_PER_num"].median(), 2),
            }))
            .reset_index()
        )

        st.markdown("**Table 28. Confirmed PLE alignment by NMAT year**")
        st.caption("These policy tables are designed for direct inclusion in narrative reporting and use only the observable best-record cohort.")
        st.dataframe(t_year, use_container_width=True)
        st.markdown("**Table 29. Confirmed PLE alignment by pre-med background**")
        st.dataframe(t_course, use_container_width=True)
        st.markdown("**Table 30. Confirmed PLE alignment by university type**")
        st.dataframe(t_uni, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 8
# -----------------------------------------------------------------------------
with tab8:
    st.subheader("Repeat-Taker Patterns and Score Change")
    st.caption("This page examines how often examinees retake the NMAT and whether their last recorded attempt differs from their first recorded attempt.")
    df = F["trend"]

    attempt_ct = df.groupby("PERSON_KEY", observed=True)["APPNO_CLEAN"].nunique().reset_index(name="attempt_count")
    attempt_summary = (
        attempt_ct["attempt_count"].value_counts()
        .sort_index()
        .rename_axis("Attempts")
        .reset_index(name="Count")
    )
    attempt_summary["Percent"] = (attempt_summary["Count"] / attempt_summary["Count"].sum() * 100).round(2)

    st.markdown("**Figure 24. Distribution of NMAT attempt counts per examinee**")
    st.caption("Each examinee is grouped by the number of unique NMAT applications linked to the same PERSON_KEY.")
    fig = px.bar(attempt_summary, x="Attempts", y="Count", text="Percent", title="NMAT Attempt Count Distribution")
    fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
    fig.update_layout(height=420)
    st.plotly_chart(fig, use_container_width=True, key="fig_t8_attempts")

    st.markdown("**Table 31. Attempt-count distribution**")
    st.caption("Each examinee is grouped by the number of unique NMAT applications linked to the same PERSON_KEY.")
    st.dataframe(attempt_summary, use_container_width=True)

    repeat_persons = attempt_ct.loc[attempt_ct["attempt_count"] > 1, "PERSON_KEY"]
    repeat_df = df[df["PERSON_KEY"].isin(repeat_persons)].copy()
    if not repeat_df.empty:
        repeat_df = repeat_df.sort_values(["PERSON_KEY", "YEAR_INT", "APPNO_CLEAN"])
        first_last = (
            repeat_df.groupby("PERSON_KEY", observed=True)
            .agg(
                first_year=("YEAR_INT", "first"),
                last_year=("YEAR_INT", "last"),
                first_pct=("NMS_PER_num", "first"),
                last_pct=("NMS_PER_num", "last"),
                first_raw=("TotalRawScoreTRUE", "first"),
                last_raw=("TotalRawScoreTRUE", "last"),
                n_attempts=("APPNO_CLEAN", "count"),
            )
            .dropna()
            .reset_index()
        )
        first_last["pct_improvement"] = first_last["last_pct"] - first_last["first_pct"]
        first_last["raw_improvement"] = first_last["last_raw"] - first_last["first_raw"]

        summary = pd.DataFrame({
            "Indicator": [
                "Repeat-taker persons",
                "Analytic repeat takers",
                "Improved percentile rank (%)",
                "Improved raw score (%)",
                "Median percentile change",
                "Median raw score change",
            ],
            "Value": [
                int(repeat_persons.nunique()),
                int(len(first_last)),
                round((first_last["pct_improvement"] > 0).mean() * 100, 2),
                round((first_last["raw_improvement"] > 0).mean() * 100, 2),
                round(first_last["pct_improvement"].median(), 2),
                round(first_last["raw_improvement"].median(), 2),
            ],
        })

        st.markdown("**Table 32. Repeat-taker trajectory summary**")
        st.caption("This table summarizes repeat-taker counts and median changes from first to last attempt. Positive values indicate improvement.")
        c1, c2 = st.columns([1, 2])

        with c1:
            st.dataframe(summary, use_container_width=True)

        with c2:
            long_change = first_last.melt(
                id_vars=["PERSON_KEY", "n_attempts"],
                value_vars=["pct_improvement", "raw_improvement"],
                var_name="Measure",
                value_name="Change",
            )
            long_change["Measure"] = long_change["Measure"].replace({
                "pct_improvement": "Percentile change",
                "raw_improvement": "Raw score change",
            })

            fig = px.box(
                long_change,
                x="Measure",
                y="Change",
                color="Measure",
                points=False,
                title="Change from first to last attempt among repeat takers",
                color_discrete_map={
                    "Percentile change": "#1f77b4",
                    "Raw score change": "#d62728",
                },
            )
            fig.add_hline(y=0, line_dash="dash", line_color="red")
            fig.update_layout(height=420, showlegend=False)
            st.plotly_chart(fig, use_container_width=True, key="fig_t8_box_change")

        scatter_df = first_last.dropna(subset=["first_pct", "last_pct"]).copy()
        if not scatter_df.empty:
            fig = px.scatter(
                scatter_df,
                x="first_pct",
                y="last_pct",
                color="n_attempts",
                size="n_attempts",
                title="First vs last percentile among repeat takers",
                labels={
                    "first_pct": "First-attempt percentile",
                    "last_pct": "Last-attempt percentile",
                    "n_attempts": "Attempts",
                },
                color_continuous_scale="Viridis",
            )
            lo = float(min(scatter_df["first_pct"].min(), scatter_df["last_pct"].min()))
            hi = float(max(scatter_df["first_pct"].max(), scatter_df["last_pct"].max()))
            fig.add_trace(
                go.Scatter(
                    x=[lo, hi],
                    y=[lo, hi],
                    mode="lines",
                    name="No change",
                    line=dict(color="red", dash="dash"),
                )
            )
            fig.update_layout(height=460)
            st.plotly_chart(fig, use_container_width=True, key="fig_t8_scatter_repeat")

        st.subheader("Repeat-taker detail table")
        display_cols = [
            "PERSON_KEY",
            "n_attempts",
            "first_year",
            "last_year",
            "first_pct",
            "last_pct",
            "pct_improvement",
            "first_raw",
            "last_raw",
            "raw_improvement",
        ]
        st.dataframe(
            first_last[display_cols].sort_values(
                ["pct_improvement", "raw_improvement"], ascending=False
            ),
            use_container_width=True,
        )
    else:
        st.info("No repeat takers are available under the current filters.")

    st.divider()
    st.subheader("NMA_AppNo Deterministic Match Histories")
    st.caption("Attempt histories exclusively for records matched deterministically via NMA_AppNo.")

    # Isolate deterministic matches
    appno_matches = df[df["PLE_MATCH_METHOD"].isin(["MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"])]

    if not appno_matches.empty:
        display_cols = ["PERSON_KEY", "APPNO_CLEAN", "Year", "TotalRawScoreTRUE", "NMS_PER_num", "PLE_STATUS_LABEL"]
        st.dataframe(
            appno_matches[display_cols].sort_values(["PERSON_KEY", "Year"]),
            use_container_width=True
        )
    else:
        st.info("No records matched exclusively via NMA_AppNo under the current filters.")

# -----------------------------------------------------------------------------
# TAB 9
# -----------------------------------------------------------------------------
with tab9:
    st.subheader("Subtest Profiles by Institution and Course Background")
    st.caption("This page compares standardized NMAT subtest profiles across university type and course group, with optional raw-score tables for reference.")

    uni_base = F["uni"]
    course_base = F["besttrend"]

    sub_tab1, sub_tab2, sub_tab3 = st.tabs(["University type", "Course group", "Radar profiles"])

    with sub_tab1:
        uni_table = subtest_mean_table(uni_base, "UNI_TYPE", std=True)
        uni_order = [u for u in ["Public", "Private", "Foreign"] if u in uni_table.index]
        if uni_order:
            uni_table = uni_table.reindex(uni_order)

        if uni_table.empty:
            st.info("No standardized subtest scores are available for the selected filters.")
        else:
            st.markdown("**Figure 27. Mean standardized subtest scores by university type**")
            st.caption("Higher values indicate stronger average standardized performance in that subtest dimension.")
            fig = px.imshow(
                uni_table,
                text_auto=".1f",
                aspect="auto",
                color_continuous_scale="RdBu_r",
                title="Mean standardized subtest scores by university type",
                labels={"x": "Subtest", "y": "University type", "color": "Mean score"},
            )
            fig.update_layout(height=450)
            st.plotly_chart(fig, use_container_width=True, key="fig_t9_heatmap_uni")
            st.markdown("**Table 34. Standardized subtest means by university type**")
            st.caption("Higher values indicate stronger average standardized performance in that subtest dimension.")
            st.dataframe(uni_table.reset_index(), use_container_width=True)

            raw_uni_table = subtest_mean_table(uni_base, "UNI_TYPE", std=False)
            if not raw_uni_table.empty:
                with st.expander("Table 35. Raw-score subtest means by university type", expanded=False):
                    st.caption("Raw-score subtest means for reference; these are not standardized scores.")
                    st.dataframe(raw_uni_table.reset_index(), use_container_width=True)

    with sub_tab2:
        course_table = subtest_mean_table(course_base, "CourseGroup", std=True)
        course_order = [c for c in PALETTE_COURSE.keys() if c in course_table.index]
        if course_order:
            course_table = course_table.reindex(course_order)

        if course_table.empty:
            st.info("No course-level standardized subtest scores are available for the selected filters.")
        else:
            fig = px.imshow(
                course_table,
                text_auto=".1f",
                aspect="auto",
                color_continuous_scale="RdBu_r",
                title="Mean standardized subtest scores by course group",
                labels={"x": "Subtest", "y": "Course group", "color": "Mean score"},
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True, key="fig_t9_heatmap_course")
            st.markdown("**Figure 28. Mean standardized subtest scores by course group**")
            st.caption("Higher values indicate stronger average standardized performance in that subtest dimension.")
            st.dataframe(course_table.reset_index(), use_container_width=True)

            raw_course_table = subtest_mean_table(course_base, "CourseGroup", std=False)
            if not raw_course_table.empty:
                with st.expander("Table 37. Raw-score subtest means by course group", expanded=False):
                    st.caption("Raw-score subtest means for reference; these are not standardized scores.")
                    st.dataframe(raw_course_table.reset_index(), use_container_width=True)

    with sub_tab3:
        c1, c2 = st.columns(2)

        with c1:
            if uni_base.empty:
                st.info("No university-type data available for radar plotting.")
            else:
                st.markdown("**Figure 29. Standardized subtest radar profile by university type**")
                st.caption("Radar shapes are descriptive profiles and should be read together with the mean-value tables.")
                fig_uni, tbl_uni = radar_for_group(uni_base[uni_base["UNI_TYPE"].isin(["Public", "Private", "Foreign"])], "UNI_TYPE")
                st.plotly_chart(fig_uni, use_container_width=True, key="fig_t9_radar_uni")
                st.markdown("**Table 38. Radar-profile values by university type**")
                st.dataframe(tbl_uni.reset_index(), use_container_width=True)

        with c2:
            if course_base.empty:
                st.info("No course-group data available for radar plotting.")
            else:
                st.markdown("**Figure 30. Standardized subtest radar profile by course group**")
                st.caption("Radar shapes are descriptive profiles and should be read together with the mean-value tables.")
                fig_course, tbl_course = radar_for_group(course_base, "CourseGroup")
                st.plotly_chart(fig_course, use_container_width=True, key="fig_t9_radar_course")
                st.markdown("**Table 39. Radar-profile values by course group**")
                st.dataframe(tbl_course.reset_index(), use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 10
# -----------------------------------------------------------------------------
with tab10:
    st.subheader("PLE Year Gap and Gender Patterns")
    st.caption("This page summarizes the time between NMAT and confirmed PLE passage, and compares sex-coded performance patterns in the filtered cohorts.")

    gap_tab1, gap_tab2 = st.tabs(["PLE year gap", "Gender patterns"])

    with gap_tab1:
        gap_df = F["bestobservable"].copy()
        gap_df = gap_df[
            (gap_df["PLE_STATUS_LABEL"] == "Confirmed PLE passer") &
            gap_df["PLE_YEAR_GAP"].notna()
        ].copy()

        if gap_df.empty:
            st.info("No confirmed observable PLE year-gap records are available under the current filters.")
        else:
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Confirmed passers", f"{len(gap_df):,}")
            col2.metric("Median year gap", f"{gap_df['PLE_YEAR_GAP'].median():.1f}", help="Median of PLE_YEAR_GAP among confirmed observable passers.")
            col3.metric("Q1 year gap", f"{gap_df['PLE_YEAR_GAP'].quantile(0.25):.1f}", help="25th percentile of PLE_YEAR_GAP among confirmed observable passers.")
            col4.metric("Q3 year gap", f"{gap_df['PLE_YEAR_GAP'].quantile(0.75):.1f}", help="75th percentile of PLE_YEAR_GAP among confirmed observable passers.")

            c1, c2 = st.columns(2)

            with c1:
                st.markdown("**Figure 31. Distribution of NMAT-to-PLE year gap**")
                st.caption("Only confirmed observable PLE passers with non-missing PLE_YEAR_GAP are included.")
                fig = px.histogram(
                    gap_df,
                    x="PLE_YEAR_GAP",
                    nbins=25,
                    title="Distribution of NMAT-to-PLE year gap",
                    labels={"PLE_YEAR_GAP": "PLE year gap"},
                    color_discrete_sequence=["#1f77b4"],
                )
                fig.update_layout(height=420)
                st.plotly_chart(fig, use_container_width=True, key="fig_t10_gap_hist")

            with c2:
                st.markdown("**Figure 32. PLE year gap by course group**")
                st.caption("Only confirmed observable PLE passers with non-missing PLE_YEAR_GAP are included.")
                box_base = gap_df.dropna(subset=["CourseGroup", "PLE_YEAR_GAP"]).copy()
                fig = px.box(
                    box_base,
                    x="CourseGroup",
                    y="PLE_YEAR_GAP",
                    color="CourseGroup",
                    title="PLE year gap by course group",
                    color_discrete_map=PALETTE_COURSE,
                )
                fig.update_layout(height=420, xaxis_title="", yaxis_title="PLE year gap")
                st.plotly_chart(fig, use_container_width=True, key="fig_t10_gap_box")

            gap_summary = (
                gap_df.groupby("CourseGroup", observed=True)
                .agg(
                    confirmed_passers=("PERSON_KEY", "nunique"),
                    median_year_gap=("PLE_YEAR_GAP", "median"),
                    q25_year_gap=("PLE_YEAR_GAP", lambda x: x.quantile(0.25)),
                    q75_year_gap=("PLE_YEAR_GAP", lambda x: x.quantile(0.75)),
                    median_percentile=("NMS_PER_num", "median"),
                )
                .reset_index()
                .sort_values("median_year_gap")
                .round(2)
            )
            st.markdown("**Table 40. Year-gap summary by course group**")
            st.caption("Table 40 reports confirmed passers, median year gap, interquartile range, and median NMAT percentile rank by course group.")
            st.dataframe(gap_summary, use_container_width=True)

    with gap_tab2:
        sex_base = F["besttrend"].dropna(subset=["SEX_CLEAN"]).copy()
        observable_sex = F["bestobservable"].dropna(subset=["SEX_CLEAN"]).copy()

        if sex_base.empty:
            st.info("No sex-coded records are available under the current filters.")
        else:
            c1, c2 = st.columns(2)

            with c1:
                st.markdown("**Table 41. Score summary by sex**")
                st.caption("Sex summaries use records with valid SEX_CLEAN coding only.")
                sex_perf = (
                    sex_base.groupby("SEX_CLEAN", observed=True)
                    .agg(
                        n=("PERSON_KEY", "nunique"),
                        median_raw=("TotalRawScoreTRUE", "median"),
                        median_pct=("NMS_PER_num", "median"),
                        median_gps=("NMS_GPS", "median"),
                    )
                    .reset_index()
                    .round(2)
                )
                st.dataframe(sex_perf, use_container_width=True)

            with c2:
                st.markdown("**Figure 33. Percentile-rank distribution by sex**")
                st.caption("The boxplot shows percentile-rank spread by sex.")
                fig = px.box(
                    sex_base,
                    x="SEX_CLEAN",
                    y="NMS_PER_num",
                    color="SEX_CLEAN",
                    title="Percentile rank by sex",
                    color_discrete_map={"Male": "#1f77b4", "Female": "#e377c2"},
                    points=False,
                )
                fig.update_layout(height=420, xaxis_title="", yaxis_title="Percentile rank")
                st.plotly_chart(fig, use_container_width=True, key="fig_t10_box_sex")

            _, sex_year_pct = pct_table(sex_base, "Year", "SEX_CLEAN", ["Male", "Female"])
            st.markdown("**Figure 34. Sex composition by NMAT year**")
            st.caption("The stacked bar shows the within-year sex mix.")
            fig = make_stacked_pct_bar(
                sex_year_pct,
                "Sex composition by NMAT year",
                "Year",
                "Percent within year",
                {"Male": "#1f77b4", "Female": "#e377c2"},
            )
            st.plotly_chart(fig, use_container_width=True, key="fig_t10_sex_year")

            if not observable_sex.empty:
                _, sex_ple_pct = pct_table(observable_sex, "SEX_CLEAN", "PLE_STATUS_LABEL", PLE_ORDER)
                fig = make_stacked_pct_bar(
                    sex_ple_pct,
                    "PLE status composition by sex (observable cohort)",
                    "Sex",
                    "Percent within sex",
                    PALETTE_PLE,
                )
                st.markdown("**Table 42. PLE status composition by sex in the observable cohort**")
                st.caption("The PLE-status table shows the percent distribution of confirmed and no-confirmed-match outcomes within each sex.")
                st.plotly_chart(fig, use_container_width=True, key="fig_t10_sex_ple")
                st.dataframe(sex_ple_pct.reset_index(), use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 11
# -----------------------------------------------------------------------------
with tab11:
    st.subheader("Statistical Test Results")
    st.caption("This page reports non-parametric tests used to assess whether observed descriptive differences across groups are statistically detectable in the filtered data.")

    stat_tab1, stat_tab2, stat_tab3, stat_tab4 = st.tabs(
        ["Kruskal-Wallis by year", "PLE status tests", "Chi-square tests", "Post hoc"]
    )

    with stat_tab1:
        test_df = F["besttrend"].copy()
        score_map = {
            "TotalRawScoreTRUE": "Total raw score",
            "PartIRawScoreTRUE": "Part I raw score",
            "PartIIRawScoreTRUE": "Part II raw score",
            "NMS_PER_num": "Percentile rank",
            "NMS_GPS": "GPS standard score",
        }
        kw_tbl = kruskal_table(test_df, "Year", score_map)
        if kw_tbl.empty:
            st.info("Not enough data to run year-based Kruskal-Wallis tests.")
        else:
            st.markdown("**Table 43. Kruskal-Wallis tests for score distributions across NMAT years**")
            st.caption("Each row reports the Kruskal-Wallis H-statistic and p-value testing whether the score distribution differs across NMAT years.")
            st.dataframe(kw_tbl, use_container_width=True)

    with stat_tab2:
        ple_test_df = F["bestobservable"].copy()
        mw_tbl = mann_whitney_ple(
            ple_test_df,
            {
                "TotalRawScoreTRUE": "Total raw score",
                "PartIRawScoreTRUE": "Part I raw score",
                "PartIIRawScoreTRUE": "Part II raw score",
                "NMS_PER_num": "Percentile rank",
                "NMS_GPS": "GPS standard score",
            },
        )
        if mw_tbl.empty:
            st.info("Not enough observable PLE-status data for Mann-Whitney tests.")
        else:
            st.markdown("**Table 44. Mann-Whitney comparisons by PLE status (observable cohort)**")
            st.caption("Tests compare confirmed passers vs no confirmed match (and other pairings where applicable). Reported values include U and p-value.")
            st.dataframe(mw_tbl, use_container_width=True)

    with stat_tab3:
        chi_base = F["uni"].copy()
        if chi_base.empty:
            st.info("No university-type records are available for chi-square testing.")
        else:
            observed_tbl, expected_tbl, chi_summary = chi_square_unitype_bin(chi_base)

            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Table 45. Observed counts by university type and percentile bin**")
                st.caption("Cell counts of examinees by university type (rows) and percentile bin (columns).")
                st.dataframe(observed_tbl.reset_index(), use_container_width=True)
                st.markdown("**Table 46. Chi-square summary (university type × bin)**")
                st.caption("Chi-square statistic, degrees of freedom, and p-value testing independence between university type and bin.")
                st.dataframe(chi_summary, use_container_width=True)

            with c2:
                row_pct = observed_tbl.div(observed_tbl.sum(axis=1).replace(0, np.nan), axis=0).mul(100).round(2)
                st.markdown("**Figure 35. University type × bin row percentages**")
                st.caption("Heatmap shows row-wise percent distribution (percent of each university type located in each bin).")
                fig = px.imshow(
                    row_pct,
                    text_auto=".1f",
                    aspect="auto",
                    color_continuous_scale="YlGnBu",
                    title="University type × bin row percentages",
                    labels={"x": "Percentile bin", "y": "University type", "color": "Percent"},
                )
                fig.update_layout(height=450)
                st.plotly_chart(fig, use_container_width=True, key="fig_t11_heatmap_chi")

            with st.expander("Table 47. Expected counts", expanded=False):
                st.caption("Expected cell counts under the null hypothesis of independence between university type and bin.")
                st.dataframe(expected_tbl.reset_index(), use_container_width=True)

    with stat_tab4:
        if not HAS_POSTHOCS:
            st.info("scikit-posthocs is not installed, so Dunn post-hoc output is skipped.")
        else:
            ph_df = F["besttrend"].dropna(subset=["Year", "NMS_PER_num"]).copy()
            if ph_df["Year"].nunique() < 3:
                st.info("Not enough year groups are available for post-hoc testing.")
            else:
                dunn = sp.posthoc_dunn(
                    ph_df,
                    val_col="NMS_PER_num",
                    group_col="Year",
                    p_adjust="bonferroni",
                )
                dunn.index = dunn.index.astype(str)
                dunn.columns = dunn.columns.astype(str)

                st.markdown("**Figure 36. Dunn post-hoc adjusted p-value matrix (percentile rank by year)**")
                st.caption("Bonferroni-adjusted p-values from pairwise Dunn tests; cells < 0.05 indicate significant pairwise differences.")
                fig = px.imshow(
                    dunn,
                    text_auto=".3f",
                    aspect="auto",
                    color_continuous_scale="Viridis_r",
                    title="Dunn post-hoc adjusted p-values for percentile rank by year",
                    labels={"x": "Year", "y": "Year", "color": "Adj. p-value"},
                )
                fig.update_layout(height=520)
                st.plotly_chart(fig, use_container_width=True, key="fig_t11_dunn")
                st.markdown("**Table 48. Dunn post-hoc adjusted p-values**")
                st.dataframe(dunn.reset_index(), use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 12
# -----------------------------------------------------------------------------
with tab12:
    st.subheader("Policy Tables and Downloads")
    st.caption("These tables are formatted as policy-ready reference tables and use the observable best-record cohort for all PLE-linked summaries.")

    policybase = F["bestobservable"].copy()

    if policybase.empty:
        st.info("No observable best-record rows are available under the current filters.")
    else:
        t_year = (
            policybase.groupby("Year", observed=True)
            .apply(lambda x: pd.Series({
                "n_observable_best_records": len(x),
                "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
                "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
                "confirmed_ple_share_pct": round((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2),
            }))
            .reset_index()
            .sort_values("Year")
        )

        t_course = (
            policybase.groupby("CourseGroup", observed=True)
            .apply(lambda x: pd.Series({
                "n_observable_best_records": len(x),
                "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
                "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
                "confirmed_ple_share_pct": round((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2),
                "median_percentile_rank": round(x["NMS_PER_num"].median(), 2),
            }))
            .reset_index()
            .sort_values("confirmed_ple_share_pct", ascending=False)
        )

        t_uni = (
            policybase[policybase["UNI_TYPE"].isin(["Public", "Private", "Foreign"])]
            .groupby("UNI_TYPE", observed=True)
            .apply(lambda x: pd.Series({
                "n_observable_best_records": len(x),
                "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
                "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
                "confirmed_ple_share_pct": round((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2),
                "median_percentile_rank": round(x["NMS_PER_num"].median(), 2),
            }))
            .reset_index()
        )

        survival_base = (
            F["besttrend"]
            .dropna(subset=["CourseGroup", "PercentileBin"])
            .copy()
        )
        survival_base["IS_TOP_BIN"] = survival_base["PercentileBin"].isin(["B8", "B9", "B10"])

        survival = (
            survival_base
            .groupby("CourseGroup", observed=True)
            .agg(
                total_examinees=("IS_TOP_BIN", "size"),
                top_decile_n=("IS_TOP_BIN", "sum"),
            )
            .reset_index()
        )
        survival["top_decile_n"] = survival["top_decile_n"].astype(int)
        survival["survival_rate_pct"] = (
            survival["top_decile_n"] / survival["total_examinees"] * 100
        ).round(2)
        survival = survival.sort_values(
            ["survival_rate_pct", "top_decile_n"],
            ascending=[False, False],
        ).reset_index(drop=True)

        st.markdown("### Table 1. Confirmed PLE alignment by NMAT year")
        st.dataframe(t_year, use_container_width=True)

        st.markdown("### Table 2. Confirmed PLE alignment by pre-med background")
        st.dataframe(t_course, use_container_width=True)

        st.markdown("### Table 3. Confirmed PLE alignment by university type")
        st.dataframe(t_uni, use_container_width=True)

        st.markdown("### Table 4. Survival to top bins by course group")
        c1, c2 = st.columns([1, 1])
        with c1:
            st.dataframe(survival, use_container_width=True)
        with c2:
            st.plotly_chart(
                make_top_share_bar(
                    survival.set_index("CourseGroup")["survival_rate_pct"],
                    "Survival to Top Bins by Course Group",
                    "Percent in B8-B10",
                    "Course group",
                    PALETTE_COURSE,
                ),
                use_container_width=True,
                key="fig_t12_survival",
            )

        st.markdown("### Download policy tables as CSV")
        st.caption("Each download reflects the current filter settings applied in the dashboard.")
        d1, d2, d3, d4 = st.columns(4)
        with d1:
            st.download_button(
                "Download year table",
                data=t_year.to_csv(index=False).encode("utf-8"),
                file_name="policy_table_year.csv",
                mime="text/csv",
            )
        with d2:
            st.download_button(
                "Download course table",
                data=t_course.to_csv(index=False).encode("utf-8"),
                file_name="policy_table_course.csv",
                mime="text/csv",
            )
        with d3:
            st.download_button(
                "Download university table",
                data=t_uni.to_csv(index=False).encode("utf-8"),
                file_name="policy_table_university.csv",
                mime="text/csv",
            )
        with d4:
            st.download_button(
                "Download survival table",
                data=survival.to_csv(index=False).encode("utf-8"),
                file_name="policy_table_top_decile_survival.csv",
                mime="text/csv",
            )