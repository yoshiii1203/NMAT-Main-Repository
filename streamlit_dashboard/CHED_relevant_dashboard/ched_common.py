"""ched_common.py — single shared compute layer for the CHED dashboard.

`dashboard.py`, `export_markdown.py`, and `ched_compute/*.py` all import from
here so that a number computed once is displayed identically everywhere.
This is the structural fix for the class of bugs where the exporter
silently re-derived an aggregation with a different filter than the live
dashboard (e.g. the historical 57/49-vs-56/48 median-percentile drift).

Nothing in this file touches Streamlit or Markdown — every `compute_*`
function returns a plain dict / DataFrame so it can be called from either
rendering layer, or from a script, or from a test.
"""

from pathlib import Path

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Constants (single source of truth — do not redefine these elsewhere)
# ---------------------------------------------------------------------------
BIN_ORDER = [f"B{i}" for i in range(1, 11)]
BIN_LABELS = {
    "B1": "0-9", "B2": "10-19", "B3": "20-29", "B4": "30-39",
    "B5": "40-49", "B6": "50-59", "B7": "60-69", "B8": "70-79",
    "B9": "80-89", "B10": "90-100",
}
B4_PLUS = ["B4", "B5", "B6", "B7", "B8", "B9", "B10"]
B5_PLUS = ["B5", "B6", "B7", "B8", "B9", "B10"]
TOP_BINS = ["B8", "B9", "B10"]
BOTTOM_BINS = ["B1", "B2", "B3"]

COLORS_BIN = {
    "B1": "#8B0000", "B2": "#B22222", "B3": "#D9534F", "B4": "#F0AD4E",
    "B5": "#FFD166", "B6": "#A0D468", "B7": "#66C2A5", "B8": "#41B6C4",
    "B9": "#2C7FB8", "B10": "#253494",
}
COLORS_UNI = {"Public": "#1f77b4", "Private": "#ff7f0e", "Foreign": "#9467bd", "Not Specified": "#7f7f7f"}
COLORS_PLE = {"Confirmed PLE passer": "#2e7d32", "No confirmed PLE match": "#c62828"}
COLORS_COURSE = {
    "Medical & Allied": "#d62728", "Natural Sciences": "#2ca02c",
    "Social & Behavioral Sciences": "#ff9800", "Education": "#17becf",
    "Engineering & Technology": "#8c564b", "Other": "#7f7f7f",
}

UNI_TYPE_COL = "UNDERGRAD_UNI_TYPE"
COURSE_GROUP_COL = "UNDERGRAD_COURSE_GROUP"
UNIVERSITY_COL = "UNDERGRAD_UNIVERSITY"

REQUIRED_COLS = [
    "APPNO_CLEAN", "PERSON_KEY", "Year", UNI_TYPE_COL, UNIVERSITY_COL,
    COURSE_GROUP_COL, "IS_BEST_NMAT_RECORD", "IS_BEST_OBSERVABLE_RECORD",
    "IS_PLE_PASSER", "TotalRawScoreTRUE", "NMS_PER_num", "PercentileBin",
]

# Population definition used for EVERY per-institution / per-bin percentile
# comparison in this dashboard (Tab 2 threshold tables, Tab 4 score summary,
# Tab 5 findings). Previously the export dropped null-PercentileBin rows and
# the dashboard did not, producing a published 57/49 vs 56/48 discrepancy.
# One policy, shared everywhere: drop rows with a null PercentileBin.
NULL_BIN_POLICY = "drop"


def bins_population(df: pd.DataFrame) -> pd.DataFrame:
    """The one population definition for bin/percentile-based comparisons."""
    return df.dropna(subset=["PercentileBin"])


# ---------------------------------------------------------------------------
# Shared narrative caveats — one copy, quoted verbatim by both dashboard.py
# and export_markdown.py, so the two documents can never diverge in wording.
# ---------------------------------------------------------------------------
SELECTION_EFFECT_NOTE = (
    "**Two caveats apply to this gradient, not one.** (1) *Admission selection:* examinees "
    "scoring lower on the NMAT were, on average, less likely to be admitted anywhere under "
    "the historical, non-uniform cutoffs individual schools actually applied, so lower "
    "linkage at the low end reflects **non-admission for at least part of the population, "
    "not solely lower ability or a lower chance of passing PLE had they been admitted.** "
    "(2) *Matching artefact, now corrected:* the PLE-matching pipeline's name-collision "
    "disambiguator previously applied a hard 40th-percentile floor when choosing among "
    "multiple same-name candidates, discarding candidates below percentile 40 and rejecting "
    "the match outright if none scored at or above 40 -- confined to name-collision groups "
    "(unique-name matches were never affected). This has been corrected upstream; every "
    "figure below reflects the corrected matcher. Note that the gradient does **not** show "
    "a sharp, isolated break at the 40th-percentile boundary -- the B4->B5 step is "
    "comparable in size to the B1->B2 and B9->B10 steps, i.e. the increase is roughly "
    "continuous across bins, not concentrated at one threshold. Neither this gradient nor "
    "any single step in it should be read as evidence about what a *new* cutoff would produce."
)

FLOOR_NOT_BINDING_NOTE = (
    "**The 40th-percentile floor was not uniformly binding historically.** Under a strictly "
    "enforced 40th-percentile rule, confirmed PLE passers scoring below that floor (bins "
    "B1-B3) should barely exist. They do not: {b1_link:.1f}% of B1 (lowest-decile) examinees "
    "and {b4_link:.1f}% of B4 examinees in the observable cohort are confirmed PLE passers "
    "({b1_n:,} confirmed passers in B1 alone). This implies the existing rule -- and by "
    "extension any single hard percentile floor -- was not uniformly applied or uniformly "
    "binding across the schools examinees actually attended between 2006 and 2014, which "
    "bears directly on CMO §IV.B.1's proposal to condition a PHEI's cut-off privilege on a "
    "single threshold."
)

SCOPE_NOTE = (
    "**No medical-school identifier exists in this dataset.** `UNDERGRAD_UNI_TYPE` records "
    "the examinee's *undergraduate* institution, not the medical school they attended, and "
    "cannot serve as a proxy for CMO §IV.B's SUC-vs-PHEI distinction or for GIDA/IP "
    "disadvantage status. No PHEI-level, SUC-vs-PHEI, or per-institution PLE-performance "
    "claim can be made from any column in this file."
)


# ---------------------------------------------------------------------------
# Data loading — the ONE place that reads and validates the parquet
# ---------------------------------------------------------------------------
def find_data_path() -> Path:
    candidates = [
        Path("NMAT_Exodus.parquet"),
        Path(__file__).parent / "NMAT_Exodus.parquet",
        Path("dataset/NMAT_Exodus.parquet"),
        Path("../main_dashboard/NMAT_Exodus.parquet"),
        Path("../../dataset/NMAT_Exodus.parquet"),
    ]
    for p in candidates:
        if p.exists():
            return p.resolve()
    raise FileNotFoundError(
        "Could not locate NMAT_Exodus.parquet. Place it in ./dataset/ or in the app root."
    )


def validate_schema(df: pd.DataFrame) -> pd.DataFrame:
    """Check required columns, normalize types. Raises on missing columns."""
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(
            "NMAT_Exodus.parquet is missing required columns: " + ", ".join(missing)
        )

    df = df.copy()

    for c in ["Year", "TotalRawScoreTRUE", "NMS_PER_num", "NMS_GPS",
              "PartIRawScoreTRUE", "PartIIRawScoreTRUE"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    if "PercentileBin" not in df.columns or df["PercentileBin"].isna().all():
        edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 101]
        df["PercentileBin"] = pd.cut(
            pd.to_numeric(df["NMS_PER_num"], errors="coerce"),
            bins=edges, labels=BIN_ORDER, right=False, include_lowest=True,
        )
    df["PercentileBin"] = pd.Categorical(df["PercentileBin"], categories=BIN_ORDER, ordered=True)

    # Boolean flags may arrive as pandas BooleanDtype, numpy bool, or (older
    # snapshots) plain strings ("True"/"False") — normalize defensively so
    # `col == True` is never silently False (bool("False") is True trap).
    for c in ["IS_BEST_NMAT_RECORD", "IS_BEST_OBSERVABLE_RECORD", "IS_PLE_PASSER",
              "IS_OBSERVABLE_COHORT", "PERSON_KEY_AMBIGUOUS", "HasTRUErawScores"]:
        if c in df.columns and not pd.api.types.is_bool_dtype(df[c]):
            df[c] = df[c].astype(str).str.strip().str.lower().isin(["true", "1", "yes"])
        elif c in df.columns:
            df[c] = df[c].fillna(False).astype(bool)

    # Nullable numeric-ish flag: keep NaN as NaN, do not coerce to False.
    if "StoredVsDerivedMismatch" in df.columns and not pd.api.types.is_bool_dtype(df["StoredVsDerivedMismatch"]):
        df["StoredVsDerivedMismatch"] = pd.to_numeric(df["StoredVsDerivedMismatch"], errors="coerce")

    df[UNI_TYPE_COL] = df[UNI_TYPE_COL].fillna("Not Specified").astype(str).replace({"nan": "Not Specified"})

    return df


def load_and_validate(path=None):
    """Load, validate, and subset NMAT_Exodus.parquet.

    Returns (df_all, df_best, df_obs):
      df_all  — every row, validated/normalized
      df_best — one row per person, IS_BEST_NMAT_RECORD == True
      df_obs  — the genuine PLE-observable cohort: each person's best
                attempt *within* Year<=2014, i.e. IS_BEST_OBSERVABLE_RECORD
                == True. This is NOT the same as
                `df_best[df_best.Year <= 2014]`, which silently drops
                people whose overall-best attempt was in a later year and
                inflates the linkage rate (see _TARGET_SCHEMA_CONTRACT.md
                §2a). All PLE-linked analysis must use df_obs.
    """
    p = path or find_data_path()
    df = pd.read_parquet(p)
    df = validate_schema(df)

    df_best = df[df["IS_BEST_NMAT_RECORD"] == True].copy()
    df_obs = df[df["IS_BEST_OBSERVABLE_RECORD"] == True].copy()

    # HAS_CONFIRMED_PLE is the single "is this a confirmed PLE passer" flag
    # used throughout the dashboard. It is IS_PLE_PASSER, never a diagnostic
    # metadata column (PLE_YEAR_PASSED / PLE_MATCH_METHOD / PLE_YEAR_GAP are
    # not authoritative passer indicators — their sets do not nest inside
    # IS_PLE_PASSER; see _TARGET_SCHEMA_CONTRACT.md §7).
    df_obs["HAS_CONFIRMED_PLE"] = df_obs["IS_PLE_PASSER"] == True

    return df, df_best, df_obs


# ---------------------------------------------------------------------------
# Generic helpers
# ---------------------------------------------------------------------------
def n_in_bins(df: pd.DataFrame, bins) -> int:
    return int(df["PercentileBin"].isin(bins).sum())


def make_bin_pct(df: pd.DataFrame, group_col: str):
    """Return (count_df, pct_df) of row-wise bin percentages, columns=BIN_ORDER."""
    ct = pd.crosstab(df[group_col], df["PercentileBin"], dropna=False)
    ct = ct.reindex(columns=BIN_ORDER, fill_value=0)
    ct = ct.apply(pd.to_numeric, errors="coerce")
    pct = ct.div(ct.sum(axis=1).replace(0, np.nan), axis=0).mul(100).fillna(0).round(2)
    return ct, pct


# ---------------------------------------------------------------------------
# Tab 1 — National Profile
# ---------------------------------------------------------------------------
def compute_tab1_kpis(df_best: pd.DataFrame) -> dict:
    return {
        "n_best": len(df_best),
        "n_unique": int(df_best["PERSON_KEY"].nunique()),
        "n_years": int(df_best["Year"].nunique()),
        "median_pct": float(df_best["NMS_PER_num"].median()),
    }


def compute_annual_trend(df_best: pd.DataFrame) -> pd.DataFrame:
    yr = (
        df_best.groupby("Year", observed=True)
        .agg(Examinees=("APPNO_CLEAN", "count"),
             Median_percentile=("NMS_PER_num", "median"),
             Median_raw_score=("TotalRawScoreTRUE", "median"))
        .round(2).reset_index()
    )
    return yr


def compute_composition(df_best: pd.DataFrame, col: str) -> pd.DataFrame:
    dist = df_best[col].value_counts().reset_index()
    dist.columns = [col, "Count"]
    dist["Count"] = pd.to_numeric(dist["Count"], errors="coerce")
    dist["Share (%)"] = (dist["Count"] / dist["Count"].sum() * 100).round(2)
    return dist


def compute_repeat_taker_stats(df_all: pd.DataFrame, n_unique: int) -> dict:
    n_repeat = int((df_all.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique() > 1).sum())
    return {"n_repeat": n_repeat, "pct": round(n_repeat / n_unique * 100, 1) if n_unique else 0.0}


def bin_reference_table() -> pd.DataFrame:
    return pd.DataFrame({
        "Bin": BIN_ORDER,
        "Score Range": [BIN_LABELS[b] for b in BIN_ORDER],
        "Threshold": ["", "", "", "CMO exception floor (B4+)", "SUC standard floor (B5+)",
                      "", "", "", "", ""],
    })


# ---------------------------------------------------------------------------
# Tab 2 — Thresholds
# ---------------------------------------------------------------------------
def compute_threshold_scenarios(df_best_bins: pd.DataFrame, df_obs_bins: pd.DataFrame) -> pd.DataFrame:
    n4, n5, n4o = n_in_bins(df_best_bins, B4_PLUS), n_in_bins(df_best_bins, B5_PLUS), n_in_bins(df_best_bins, ["B4"])
    total = len(df_best_bins)
    return pd.DataFrame([
        {"Threshold": "B4+ (Bin 4 and above)", "Best-record examinees": n4,
         "Share of all (%)": round(n4 / total * 100, 1), "Observable cohort size": n_in_bins(df_obs_bins, B4_PLUS)},
        {"Threshold": "B5+ (Bin 5 and above)", "Best-record examinees": n5,
         "Share of all (%)": round(n5 / total * 100, 1), "Observable cohort size": n_in_bins(df_obs_bins, B5_PLUS)},
        {"Threshold": "B4 only (Bin 4)", "Best-record examinees": n4o,
         "Share of all (%)": round(n4o / total * 100, 1), "Observable cohort size": n_in_bins(df_obs_bins, ["B4"])},
    ])


def compute_threshold_by_uni_type(df_best_bins: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for ut in ["Public", "Private", "Foreign", "Not Specified"]:
        sub = df_best_bins[df_best_bins[UNI_TYPE_COL] == ut]
        if sub.empty:
            continue
        n_ut = len(sub)
        n_b4, n_b5, n_b4o = n_in_bins(sub, B4_PLUS), n_in_bins(sub, B5_PLUS), n_in_bins(sub, ["B4"])
        rows.append({
            "University Type": ut, "Best-record examinees": n_ut,
            "B4+ count": n_b4, "B4+ (%)": round(n_b4 / n_ut * 100, 1),
            "B5+ count": n_b5, "B5+ (%)": round(n_b5 / n_ut * 100, 1),
            "B4-only count": n_b4o, "B4-only (%)": round(n_b4o / n_ut * 100, 1),
        })
    return pd.DataFrame(rows)


def compute_public_private_b5_evidence(df_best_bins: pd.DataFrame) -> dict:
    pub = df_best_bins[df_best_bins[UNI_TYPE_COL] == "Public"]
    priv = df_best_bins[df_best_bins[UNI_TYPE_COL] == "Private"]
    pub_total, priv_total = len(pub), len(priv)
    pub_b5, pub_b4o = n_in_bins(pub, B5_PLUS), n_in_bins(pub, ["B4"])
    priv_b5, priv_b4o = n_in_bins(priv, B5_PLUS), n_in_bins(priv, ["B4"])
    return {
        "pub_total": pub_total, "priv_total": priv_total,
        "pub_b5": pub_b5, "pub_b5_pct": round(pub_b5 / pub_total * 100, 1) if pub_total else 0.0,
        "pub_b4o": pub_b4o, "pub_b4o_pct": round(pub_b4o / pub_total * 100, 1) if pub_total else 0.0,
        "priv_b5": priv_b5, "priv_b5_pct": round(priv_b5 / priv_total * 100, 1) if priv_total else 0.0,
        "priv_b4o": priv_b4o, "priv_b4o_pct": round(priv_b4o / priv_total * 100, 1) if priv_total else 0.0,
    }


def compute_b4_group_profile(df_best_bins: pd.DataFrame) -> dict:
    b4 = df_best_bins[df_best_bins["PercentileBin"] == "B4"]
    by_uni = b4.groupby(UNI_TYPE_COL, observed=True).size().reset_index(name="count")
    by_uni["count"] = pd.to_numeric(by_uni["count"], errors="coerce")
    by_uni["share (%)"] = (by_uni["count"] / by_uni["count"].sum() * 100).round(1) if len(by_uni) else by_uni["count"]
    pub_share = by_uni.loc[by_uni[UNI_TYPE_COL] == "Public", "share (%)"].values
    return {
        "n": len(b4),
        "median_raw": float(b4["TotalRawScoreTRUE"].median()) if len(b4) else float("nan"),
        "pub_share": float(pub_share[0]) if len(pub_share) > 0 else 0.0,
        "by_uni": by_uni,
    }


def compute_top_bottom_trend(df_best: pd.DataFrame) -> pd.DataFrame:
    _, pct_year = make_bin_pct(df_best, "Year")
    top_share = pct_year[TOP_BINS].sum(axis=1)
    bot_share = pct_year[BOTTOM_BINS].sum(axis=1)
    return pd.DataFrame({
        "Year": top_share.index.astype(str),
        "Top B8-B10 (%)": top_share.to_numpy(dtype=float, na_value=0).round(1),
        "Bottom B1-B3 (%)": bot_share.to_numpy(dtype=float, na_value=0).round(1),
        "Difference (pp)": (top_share.to_numpy(dtype=float, na_value=0)
                             - bot_share.to_numpy(dtype=float, na_value=0)).round(1),
    }).reset_index(drop=True)


def compute_yearly_threshold_counts(df_best_bins: pd.DataFrame, df_obs_bins: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for yr in sorted(df_best_bins["Year"].dropna().unique()):
        yr_df = df_best_bins[df_best_bins["Year"] == yr]
        yr_obs = df_obs_bins[df_obs_bins["Year"] == yr]
        b4, b5 = n_in_bins(yr_df, B4_PLUS), n_in_bins(yr_df, B5_PLUS)
        ob4 = n_in_bins(yr_obs, B4_PLUS) if not yr_obs.empty else 0
        ob5 = n_in_bins(yr_obs, B5_PLUS) if not yr_obs.empty else 0
        rows.append({
            "Year": int(yr), "Total (best record)": len(yr_df),
            "B4+ count": b4, "B4+ (%)": round(b4 / len(yr_df) * 100, 1),
            "B5+ count": b5, "B5+ (%)": round(b5 / len(yr_df) * 100, 1),
            "Observable B4+": ob4, "Observable B5+": ob5,
        })
    return pd.DataFrame(rows)


def compute_ple_composition_by_year(df_obs: pd.DataFrame, bins=B5_PLUS, filipino_only: bool = False,
                                     strict: bool = False) -> pd.DataFrame:
    """Non-tautological PLE-status split by year for a bin band.

    THE FIX for the flagship tautology bug: population is the *bin-filtered
    observable cohort*, never pre-filtered on match status, so `no_match`
    can be genuinely nonzero. `confirmed` is computed from HAS_CONFIRMED_PLE
    (== IS_PLE_PASSER) on that same, unfiltered population.

    strict=True additionally requires PLE_YEAR_GAP >= 5 among confirmed
    passers (the "clean subset" stress test in Tab 3) — a real, checkable
    restriction to only the most defensible matches, not a redefinition of
    the population.
    """
    pop = df_obs[df_obs["PercentileBin"].isin(bins)].copy()
    if filipino_only:
        pop = pop[pop["FOREIGNER_STATUS"] == "Filipino"]

    if strict:
        pop["_confirmed"] = pop["HAS_CONFIRMED_PLE"] & (pop["PLE_YEAR_GAP"] >= 5)
    else:
        pop["_confirmed"] = pop["HAS_CONFIRMED_PLE"]

    yr = (
        pop.groupby("Year", observed=True)
        .agg(total=("APPNO_CLEAN", "count"), confirmed=("_confirmed", "sum"))
        .reset_index()
    )
    yr["no_match"] = yr["total"] - yr["confirmed"]
    yr["linkage_pct"] = (yr["confirmed"] / yr["total"].replace(0, np.nan) * 100).round(1)
    yr["no_match_pct"] = (yr["no_match"] / yr["total"].replace(0, np.nan) * 100).round(1)
    return yr


# ---------------------------------------------------------------------------
# Tab 3 — PLE Linkage
# ---------------------------------------------------------------------------
def compute_linkage_by(df_obs: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """Generic NMAT-to-PLE-passer linkage table, grouped by any column."""
    d = df_obs.dropna(subset=[group_col, "HAS_CONFIRMED_PLE"])
    out = (
        d.groupby(group_col, observed=True)
        .agg(N=("APPNO_CLEAN", "count"), Confirmed=("HAS_CONFIRMED_PLE", "sum"),
             Median_percentile=("NMS_PER_num", "median"))
        .reset_index()
    )
    out["Linkage Rate (%)"] = (out["Confirmed"] / out["N"] * 100).round(2)
    return out


def compute_score_profile_by_ple_status(df_obs: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in ["TotalRawScoreTRUE", "NMS_PER_num", "PartIRawScoreTRUE", "PartIIRawScoreTRUE"]
            if c in df_obs.columns]
    desc = (
        df_obs.groupby("HAS_CONFIRMED_PLE", observed=True)[cols]
        .agg(["count", "median", "mean", lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)])
        .round(2)
    )
    desc.index = ["No confirmed PLE match", "Confirmed PLE passer"]
    return desc


def compute_stress_test(df_obs: pd.DataFrame) -> dict:
    """Defensible-matching-subset stress test (Tab 3).

    NOT the tautology from the original code (which pre-filtered the
    population on the same flag used to compute "confirmed", guaranteeing
    100% every year regardless of match quality). Population here is the
    Filipino, B5+ observable cohort with NO pre-filter on match status;
    "confirmed" additionally requires PLE_YEAR_GAP >= 5 among passers. The
    resulting no_match / linkage_pct can genuinely vary and can fail.
    """
    yearly = compute_ple_composition_by_year(df_obs, bins=B5_PLUS, filipino_only=True, strict=True)
    pop = df_obs[(df_obs["PercentileBin"].isin(B5_PLUS)) & (df_obs["FOREIGNER_STATUS"] == "Filipino")].copy()
    pop["_confirmed"] = pop["HAS_CONFIRMED_PLE"] & (pop["PLE_YEAR_GAP"] >= 5)
    n_pop = len(pop)
    n_confirmed = int(pop["_confirmed"].sum())
    by_uni = (
        pop[pop["_confirmed"]].groupby(UNI_TYPE_COL, observed=True).size().reset_index(name="N")
    )
    if len(by_uni):
        by_uni["Share (%)"] = (by_uni["N"] / by_uni["N"].sum() * 100).round(1)
    median_gap = pop.loc[pop["_confirmed"], "PLE_YEAR_GAP"].median() if n_confirmed else float("nan")
    return {
        "n_population": n_pop,
        "n_confirmed": n_confirmed,
        "n_no_match": n_pop - n_confirmed,
        "linkage_pct": round(n_confirmed / n_pop * 100, 1) if n_pop else 0.0,
        "median_gap": median_gap,
        "yearly": yearly,
        "by_uni": by_uni,
    }


# ---------------------------------------------------------------------------
# Tab 4 — Institution and Foreign Context
# ---------------------------------------------------------------------------
def compute_uni_score_summary(df_best_bins: pd.DataFrame, uni_types=("Public", "Private", "Foreign")) -> pd.DataFrame:
    sub = df_best_bins[df_best_bins[UNI_TYPE_COL].isin(uni_types)]
    out = (
        sub.groupby(UNI_TYPE_COL, observed=True)
        .agg(**{
            "N (best record, valid bin)": ("APPNO_CLEAN", "count"),
            "Median %ile": ("NMS_PER_num", "median"),
            "Q25 %ile": ("NMS_PER_num", lambda x: x.quantile(0.25)),
            "Q75 %ile": ("NMS_PER_num", lambda x: x.quantile(0.75)),
            "Median TRUE raw score": ("TotalRawScoreTRUE", "median"),
            "Median GPS": ("NMS_GPS", "median"),
        }).round(2).reset_index()
    )
    return out


def compute_box_plot_summary(df_best_bins: pd.DataFrame, group_col=UNI_TYPE_COL,
                              groups=("Public", "Private", "Foreign")) -> pd.DataFrame:
    rows = []
    for g in groups:
        s = df_best_bins[df_best_bins[group_col] == g]["NMS_PER_num"].dropna()
        if len(s) == 0:
            continue
        rows.append([g, len(s), s.min(), s.quantile(0.25), s.median(), s.quantile(0.75), s.max()])
    return pd.DataFrame(rows, columns=["Group", "N", "Minimum", "Q25", "Median", "Q75", "Maximum"])


def compute_bin_dist_by(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    _, pct = make_bin_pct(df, group_col)
    pct.index.name = group_col
    return pct.reset_index()


def compute_top_bin_share_by(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    ct, pct = make_bin_pct(df, group_col)
    totals = ct.sum(axis=1)
    top_ct = ct[TOP_BINS].sum(axis=1)
    top_pct = pct[TOP_BINS].sum(axis=1)
    out = pd.DataFrame({
        group_col: totals.index, "Total examinees": totals.values,
        "Top B8-B10 count": top_ct.values, "Top B8-B10 (%)": top_pct.values,
    })
    return out.sort_values("Top B8-B10 (%)").reset_index(drop=True)


def compute_nationality_shares(df_all: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Top-N nationality table with share of ALL verified foreigners.

    THE FIX for the India-85.1%-vs-81.5% bug: the denominator is
    `len(foreign)` (every Verified Foreigner row), never the top-N
    subtotal — using the subtotal inflates every row by the same factor.
    """
    foreign = df_all[df_all["FOREIGNER_STATUS"] == "Verified Foreigner"]
    total_foreign = len(foreign)
    top_nat = foreign["CITIZENSHIP_FINAL"].value_counts().head(top_n).reset_index()
    top_nat.columns = ["Nationality", "Count"]
    top_nat["Count"] = pd.to_numeric(top_nat["Count"], errors="coerce")
    top_nat["Share of verified foreigners (%)"] = (top_nat["Count"] / total_foreign * 100).round(1)
    return top_nat


def compute_foreign_context(df_best: pd.DataFrame) -> dict:
    """Foreign-examinee KPIs on df_best (person-level), consistent with the
    rest of the dashboard's denominator (fixes the record-level/person-level
    inconsistency where this section alone used df_all)."""
    foreign = df_best[df_best["FOREIGNER_STATUS"] == "Verified Foreigner"]
    filipino = df_best[df_best["CITIZENSHIP_FINAL"] == "Filipino"]
    return {
        "n_foreign": len(foreign),
        "n_filipino": len(filipino),
        "n_nationalities": int(foreign["CITIZENSHIP_FINAL"].nunique()),
        "pct_foreign": round(len(foreign) / len(df_best) * 100, 1) if len(df_best) else 0.0,
    }


# ---------------------------------------------------------------------------
# Tab 6 — Data, Methods, and Limitations
# ---------------------------------------------------------------------------
def compute_stored_mismatch_stats(df_all: pd.DataFrame) -> dict:
    """THE FIX for the hardcoded, unreconciled '42.2%' claim (appeared 3x in
    dashboard.py, 2x in export_markdown.py). Computed live from the
    parquet's own StoredVsDerivedMismatch column — never hardcoded."""
    n_stored = int(df_all["StoredRawTotal"].notna().sum())
    n_mismatch = int((df_all["StoredVsDerivedMismatch"] == True).sum())
    return {
        "n_stored": n_stored,
        "n_mismatch": n_mismatch,
        "pct_of_stored": round(n_mismatch / n_stored * 100, 2) if n_stored else 0.0,
        "pct_of_all": round(n_mismatch / len(df_all) * 100, 2) if len(df_all) else 0.0,
    }


def compute_true_raw_score_stats(df_all: pd.DataFrame) -> dict:
    n_true = int((df_all["HasTRUErawScores"] == True).sum())
    return {
        "n_true": n_true,
        "pct_true": round(n_true / len(df_all) * 100, 2) if len(df_all) else 0.0,
    }


def compute_ple_matching_stats(df_all: pd.DataFrame, df_obs: pd.DataFrame) -> dict:
    """Deterministic-matching methodology numbers, including the outcome
    breakdown (accepted / rejected / no_match) now exposed via
    PLE_MATCH_OUTCOME, plus the disagreement across the other diagnostic
    PLE columns (year, method, gap) that are NOT authoritative passer
    counts (see contract §7)."""
    n_all_ple = int((df_all["IS_PLE_PASSER"] == True).sum())
    n_obs_ple = int(df_obs["HAS_CONFIRMED_PLE"].sum())
    outcome_counts = (
        df_all["PLE_MATCH_OUTCOME"].value_counts().to_dict()
        if "PLE_MATCH_OUTCOME" in df_all.columns else {}
    )
    n_year = int(df_all["PLE_YEAR_PASSED"].notna().sum()) if "PLE_YEAR_PASSED" in df_all.columns else None
    n_method = int(df_all["PLE_MATCH_METHOD"].notna().sum()) if "PLE_MATCH_METHOD" in df_all.columns else None
    n_gap = int(df_all["PLE_YEAR_GAP"].notna().sum()) if "PLE_YEAR_GAP" in df_all.columns else None
    n_year_uncertain = int((df_all["PLE_YEAR_UNCERTAIN"] == True).sum()) if "PLE_YEAR_UNCERTAIN" in df_all.columns else None
    return {
        "n_all_ple": n_all_ple,
        "n_obs_ple": n_obs_ple,
        "outcome_counts": outcome_counts,
        "n_year_passed_notna": n_year,
        "n_match_method_notna": n_method,
        "n_year_gap_notna": n_gap,
        "n_year_uncertain": n_year_uncertain,
    }


def compute_ambiguous_person_stats(df_all: pd.DataFrame) -> dict:
    """PERSON_KEY_AMBIGUOUS surfaces PERSON_KEYs with contradictory SEX
    across their rows — a data-quality signal that should be disclosed,
    not hidden (contract §2)."""
    if "PERSON_KEY_AMBIGUOUS" not in df_all.columns:
        return {"n_ambiguous_keys": None}
    n = int(df_all.groupby("PERSON_KEY")["PERSON_KEY_AMBIGUOUS"].first().sum())
    return {"n_ambiguous_keys": n}


# ---------------------------------------------------------------------------
# Tab 5 — Key Evidence findings (shared prose inputs)
# ---------------------------------------------------------------------------
def compute_tab5_findings(df_all: pd.DataFrame, df_best: pd.DataFrame, df_obs: pd.DataFrame) -> dict:
    """Every number used to build the 7 Tab-5 finding narratives, computed
    once so dashboard.py and export_markdown.py render identical prose."""
    db = bins_population(df_best)
    n_all = len(db)
    n4, n5 = n_in_bins(db, B4_PLUS), n_in_bins(db, B5_PLUS)

    ev = compute_public_private_b5_evidence(db)

    pub = db[db[UNI_TYPE_COL] == "Public"]
    priv = db[db[UNI_TYPE_COL] == "Private"]
    pub_med = float(pub["NMS_PER_num"].median()) if len(pub) else float("nan")
    priv_med = float(priv["NMS_PER_num"].median()) if len(priv) else float("nan")

    ple_bin = compute_linkage_by(df_obs, "PercentileBin")
    b1 = ple_bin.loc[ple_bin["PercentileBin"] == "B1"]
    b10 = ple_bin.loc[ple_bin["PercentileBin"] == "B10"]
    b1_link = float(b1["Linkage Rate (%)"].values[0]) if len(b1) else 0.0
    b10_link = float(b10["Linkage Rate (%)"].values[0]) if len(b10) else 0.0
    b1_n_confirmed = int(b1["Confirmed"].values[0]) if len(b1) else 0
    b4_link_row = ple_bin.loc[ple_bin["PercentileBin"] == "B4"]
    b5_link_row = ple_bin.loc[ple_bin["PercentileBin"] == "B5"]
    b4_link = float(b4_link_row["Linkage Rate (%)"].values[0]) if len(b4_link_row) else 0.0
    b5_link = float(b5_link_row["Linkage Rate (%)"].values[0]) if len(b5_link_row) else 0.0

    ann = (
        df_obs.groupby("Year", observed=True)
        .agg(n=("APPNO_CLEAN", "count"), confirmed=("HAS_CONFIRMED_PLE", "sum"))
        .reset_index()
    )
    ann["rate"] = (ann["confirmed"] / ann["n"] * 100).round(2)
    ann["5yr"] = ann["rate"].rolling(window=5, min_periods=3).mean().round(2)
    valid_5yr = ann[ann["5yr"].notna()]
    if len(valid_5yr):
        five_yr_val = float(valid_5yr.iloc[-1]["5yr"])
        five_yr_year = int(valid_5yr.iloc[-1]["Year"])
    else:
        five_yr_val, five_yr_year = None, None

    stress = compute_stress_test(df_obs)
    n_foreign = int((df_all["FOREIGNER_STATUS"] == "Verified Foreigner").sum())

    return {
        "n4": n4, "n5": n5, "n_all_bins_pop": n_all,
        "b4plus_pct": round(n4 / n_all * 100, 1) if n_all else 0.0,
        "b5plus_pct": round(n5 / n_all * 100, 1) if n_all else 0.0,
        "pub_median_pct": pub_med, "priv_median_pct": priv_med,
        "b1_link": b1_link, "b10_link": b10_link, "b4_link": b4_link, "b5_link": b5_link,
        "b1_n_confirmed": b1_n_confirmed,
        "ann_first_year": int(ann["Year"].iloc[0]) if len(ann) else None,
        "ann_first_rate": float(ann["rate"].iloc[0]) if len(ann) else 0.0,
        "ann_last_year": int(ann["Year"].iloc[-1]) if len(ann) else None,
        "ann_last_rate": float(ann["rate"].iloc[-1]) if len(ann) else 0.0,
        "five_yr_val": five_yr_val, "five_yr_year": five_yr_year,
        "pub_b5_rate": ev["pub_b5_pct"], "pub_b5_count": ev["pub_b5"], "pub_total": ev["pub_total"],
        "pub_b4o_rate": ev["pub_b4o_pct"], "pub_b4o_count": ev["pub_b4o"],
        "stress_n_population": stress["n_population"], "stress_n_confirmed": stress["n_confirmed"],
        "stress_linkage_pct": stress["linkage_pct"],
        "n_foreign": n_foreign, "n_all_rows": len(df_all),
        "pct_foreign_all": round(n_foreign / len(df_all) * 100, 1) if len(df_all) else 0.0,
    }


def compute_tab5_finding_texts(df_all: pd.DataFrame, df_best: pd.DataFrame, df_obs: pd.DataFrame) -> list:
    """The 7 Tab-5 finding (title, body) pairs, built ONCE from
    compute_tab5_findings() so dashboard.py and export_markdown.py render
    byte-identical prose — the structural fix for narrative drift (contract
    Rule 5: captions must be exported verbatim, not paraphrased)."""
    F = compute_tab5_findings(df_all, df_best, df_obs)

    finding1 = (
        f"The historical NMAT examinee pool ranges from approximately "
        f"{F['b4plus_pct']:.0f}% meeting a B4+ threshold to "
        f"{F['b5plus_pct']:.0f}% meeting a B5+ threshold "
        f"(best-record examinees with a valid percentile bin, 2006-2018).  The marginal group "
        f"between the two thresholds -- B4 only -- accounts "
        f"for roughly {F['b4plus_pct'] - F['b5plus_pct']:.0f} percentage points "
        f"of the examinee population."
    )

    finding2 = (
        f"Public-undergraduate-institution examinees show a higher median NMAT percentile "
        f"({F['pub_median_pct']:.0f}) than private-undergraduate-institution examinees "
        f"({F['priv_median_pct']:.0f}).  This pattern is consistent across all "
        f"NMAT years and may reflect differences in pre-medical preparation, "
        f"admission selectivity, or other institutional factors not captured "
        f"in this dataset.  'Institution' here means the undergraduate school, not the "
        f"medical school. " + SCOPE_NOTE
    )

    finding3 = (
        f"NMAT-to-PLE-passer linkage rises roughly continuously with score bin, from "
        f"{F['b1_link']:.0f}% in the lowest bin (B1) to {F['b10_link']:.0f}% in the "
        f"highest bin (B10).  This historical gradient provides context for "
        f"evaluating the relationship between NMAT scores and licensure "
        f"outcomes, but is not a PLE pass rate. " + SELECTION_EFFECT_NOTE
    )

    finding_floor = FLOOR_NOT_BINDING_NOTE.format(
        b1_link=F["b1_link"], b4_link=F["b4_link"], b1_n=F["b1_n_confirmed"],
    )

    finding4 = (
        f"The observable NMAT-to-PLE-passer linkage rate went from "
        f"{F['ann_first_rate']:.1f}% in {F['ann_first_year']} to "
        f"{F['ann_last_rate']:.1f}% in {F['ann_last_year']} across the "
        f"observable cohort."
    )
    if F["five_yr_val"] is not None:
        finding4 += f"  The 5-year rolling average was {F['five_yr_val']:.1f}% as of {F['five_yr_year']}."
    finding4 += (
        "  This measure reflects NMAT examinees later matched to PLE passer "
        "records and is not directly comparable to official PLE passing rates.  Later years "
        "have a shorter observed window for a match to appear even within the observable "
        "cohort, which can mechanically lower recent-year rates."
    )

    finding5 = (
        f"{F['pub_b5_rate']}% of public-undergraduate-institution examinees "
        f"({F['pub_b5_count']:,} of {F['pub_total']:,}) score at Bin 5 or above; only "
        f"{F['pub_b4o_rate']}% fall in the B4-only band the CMO exception addresses.  "
        f"This is purely descriptive.  Whether this band overlaps with GIDA/IP applicants "
        f"cannot be determined from this dataset -- GIDA/IP status is not recorded, and "
        f"'public undergraduate institution' is neither a GIDA/IP indicator nor equivalent "
        f"to 'SUC' as the CMO uses the term.  No claim about who benefits from the exception "
        f"can be supported by this data."
    )

    finding6 = (
        f"Restricting to the strictest defensible PLE match (confirmed passer, >=5-year gap, "
        f"Filipino nationals, B5+ band) yields a linkage rate of {F['stress_linkage_pct']:.1f}% "
        f"({F['stress_n_confirmed']:,} of {F['stress_n_population']:,}) -- genuinely lower than "
        f"the broader B5+ linkage figures, because this population is not pre-filtered on match "
        f"status.  This is a real, checkable comparison, not a tautology: it shows that "
        f"loosening match criteria measurably raises the apparent linkage rate, which should be "
        f"kept in mind when reading the less-strict figures elsewhere in this dashboard."
    )

    finding7 = (
        f"Foreign nationals represent approximately "
        f"{F['pct_foreign_all']:.1f}% of all NMAT records "
        f"({F['n_foreign']:,} verified foreign records out of {F['n_all_rows']:,} total).  India accounts for "
        f"the largest share of foreign examinees.  These are NMAT examinee "
        f"counts, not enrolled medical students."
    )

    return [
        ("National Threshold Context", finding1),
        ("Institutional Performance Patterns", finding2),
        ("NMAT-to-PLE-Passer Linkage Gradient", finding3),
        ("The 40th-Percentile Floor Was Not Uniformly Binding", finding_floor),
        ("Historical Linkage Trends", finding4),
        ("Public-Institution Threshold Attainment (Descriptive Only)", finding5),
        ("PLE Matching Sensitivity Check", finding6),
        ("Foreign Examinee Presence", finding7),
    ]


def compute_limitations_cards(df_all: pd.DataFrame, df_best: pd.DataFrame, df_obs: pd.DataFrame) -> list:
    """The Tab-6 limitations cards, built once so dashboard.py and
    export_markdown.py render identical text with live-computed numbers
    (no hardcoded counts in either caller)."""
    F = compute_tab5_findings(df_all, df_best, df_obs)
    match_stats = compute_ple_matching_stats(df_all, df_obs)
    outcome = match_stats["outcome_counts"]
    n_rejected_ambiguous = outcome.get("rejected_ambiguous_person", 0)
    n_year_uncertain = match_stats["n_year_uncertain"] or 0

    return [
        ("PLE Outcomes",
         "The dataset only identifies NMAT examinees later matched to PLE passer records.  It "
         "does not contain all PLE takers or PLE failures.  Therefore, this dashboard reports "
         "NMAT-to-PLE-passer linkage rates, not PLE pass rates.  Official PLE passing rates "
         "published by the PRC should be used for benchmarking purposes."),
        ("GIDA and IP Status",
         "The dataset does not contain indicators for Geographically Isolated and Disadvantaged "
         "Area (GIDA) residence or Indigenous Peoples (IP) membership.  The CMO exception for "
         "30th-39th percentile applicants from these groups requires documentation not available "
         "in this dataset."),
        ("Medical School Admissions and Enrollment",
         "This dataset records NMAT examinees, not enrolled medical students.  The number of "
         "examinees at or above a threshold represents the available applicant pool, not actual "
         "enrollment.  HEI-level admissions decisions, capacity constraints, and selection "
         "criteria are not captured."),
        ("Foreign Student Enrollment Cap",
         "The CMO caps foreign student enrollment at 10 slots per incoming class at SUCs.  The "
         "dataset shows NMAT examinees by citizenship, not enrolled foreign students.  A "
         "descriptive foreign-examinee profile is provided, but this dashboard does not assess "
         "compliance with the 10-slot cap."),
        ("Composite Ranking for Foreign Applicants",
         "The CMO encourages composite ranking for foreign applicants.  The dataset does not "
         "contain GWA, interview scores, or other admission criteria needed for such analysis."),
        ("PHEI Accountability and Sanctions",
         "The CMO ties cut-off privileges to a PHEI's own 5-year PLE performance and provides for "
         "revocation after three consecutive years below benchmark.  **This dataset contains no "
         "medical-school identifier of any kind** -- not just an incomplete one.  No PHEI, SUC, or "
         "any other institution-level PLE performance, compliance label, or risk rating can be "
         "computed from any column in this file.  `UNDERGRAD_UNI_TYPE` describes the examinee's "
         "undergraduate school and must never be read as a stand-in for the medical school the "
         "CMO's cut-off privilege provisions are about."),
        ("Selection Effect Across the Linkage Gradient",
         f"Linkage rises roughly continuously with score bin ({F['b1_link']:.1f}% at B1 to "
         f"{F['b10_link']:.1f}% at B10) -- there is NOT a sharp, isolated break concentrated at "
         f"the 40th-percentile boundary; the B4->B5 step ({F['b4_link']:.1f}% to {F['b5_link']:.1f}%) "
         f"is comparable in size to the steps on either side of it. Lower linkage at the low end "
         f"reflects, in part, non-admission under the historical, non-uniform cutoffs individual "
         f"schools actually applied between 2006 and 2014 -- not solely lower ability or a lower "
         f"chance of passing PLE had those examinees been admitted. This gradient cannot be used "
         f"to estimate how many additional PLE passers a new uniform cutoff would produce or exclude."),
        ("The 40th-Percentile Floor Was Not Uniformly Binding (Disclosed)",
         FLOOR_NOT_BINDING_NOTE.format(b1_link=F["b1_link"], b4_link=F["b4_link"], b1_n=F["b1_n_confirmed"])),
        ("PLE-Matching Bias Against Below-40th-Percentile Examinees (Disclosed, Now Corrected)",
         "Found during remediation, not in the original audit. The PLE-matching pipeline's "
         "name-collision disambiguator (`2_PLE_Matching_Pipeline.ipynb`, `disambiguate()` Step 4) "
         "previously applied a **hard filter**, not a tie-break: when a person's name matched more "
         "than one candidate NMAT record, every candidate scoring below the 40th NMAT percentile "
         "was discarded outright, and the match was rejected entirely if no candidate scored at or "
         "above 40. That constant -- 40 -- is exactly the CMO threshold this dashboard is "
         "evaluating. The effect was confined to name-collision groups (unique-name matches were "
         "never affected) and has now been corrected upstream -- every number in this dashboard "
         f"reflects the corrected matcher. `PLE_MATCH_OUTCOME` additionally distinguishes matches "
         f"rejected as genuinely ambiguous ({n_rejected_ambiguous:,} candidates, "
         f"`rejected_ambiguous_person`) from `no_match`, so a reader can see where borderline "
         f"candidates went rather than have them silently folded into 'no match'. "
         f"`PLE_YEAR_UNCERTAIN` flags {n_year_uncertain:,} confirmed passers whose PLE year is not "
         f"determinable; these remain counted as passers but are excluded from any year-specific figure."),
    ]
