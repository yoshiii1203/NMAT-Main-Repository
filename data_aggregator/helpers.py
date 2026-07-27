"""
Shared helper functions for data extraction scripts.
Replicates dashboard.py computation logic for standalone use.
"""
import numpy as np
import pandas as pd
from datetime import datetime
from config import BIN_ORDER, PLE_ORDER


def load_data():
    """Load NMAT_Exodus_Lite.parquet and create all data subsets matching the dashboard."""
    df = pd.read_parquet("dataset/NMAT_Exodus_Lite.parquet")
    
    # Ensure required derived columns
    if "PLE_STATUS_LABEL" not in df.columns:
        df["PLE_STATUS_LABEL"] = np.where(
            df["IS_PLE_ANALYSIS_SAFE"] == True,
            "Confirmed PLE passer", "No confirmed PLE match"
        )
    if "HAS_CONFIRMED_PLE" not in df.columns:
        df["HAS_CONFIRMED_PLE"] = df["IS_PLE_ANALYSIS_SAFE"] == True
    if "IS_BOARD_OBSERVABLE_COHORT" not in df.columns:
        df["IS_BOARD_OBSERVABLE_COHORT"] = df["Year"] <= 2014
    
    # Parse Year
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    
    # Create subsets (mirroring dashboard.py load_data_and_subsets)
    subsets = {}
    subsets["all"] = df
    subsets["best"] = df[df["IS_BEST_NMAT_RECORD"] == True].copy() if "IS_BEST_NMAT_RECORD" in df.columns else df
    subsets["trend"] = df[df["Year"].between(2006, 2018, inclusive="both")].copy()
    subsets["besttrend"] = subsets["best"][subsets["best"]["Year"].between(2006, 2018, inclusive="both")].copy()
    subsets["bestobservable"] = subsets["besttrend"][subsets["besttrend"]["IS_BOARD_OBSERVABLE_COHORT"] == True].copy()
    subsets["uni"] = subsets["besttrend"][subsets["besttrend"]["UNI_TYPE"].isin(["Public", "Private", "Foreign"])].copy()
    subsets["uniobservable"] = subsets["bestobservable"][subsets["bestobservable"]["UNI_TYPE"].isin(["Public", "Private", "Foreign"])].copy()
    subsets["plesafe"] = df[df["IS_PLE_ANALYSIS_SAFE"] == True].copy() if "IS_PLE_ANALYSIS_SAFE" in df.columns else df.iloc[0:0]
    subsets["plebest"] = subsets["plesafe"][subsets["plesafe"]["IS_BEST_NMAT_RECORD"] == True].copy() if not subsets["plesafe"].empty else df.iloc[0:0]
    
    return df, subsets


def write_header(f, title, subset_name, page_num):
    """Write markdown header for a page output file."""
    f.write(f"# Page {page_num}: {title}\n\n")
    f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
    f.write(f"**Data source:** NMAT_Exodus_Lite.parquet (Pipeline 4)\n\n")
    f.write(f"**Data subset:** `{subset_name}`\n\n")
    f.write(f"**Filters:** None (full unfiltered dataset)\n\n")
    f.write("---\n\n")


def pct_table(df, group_col, cat_col, cat_order=None):
    """Cross-tabulation: counts and row percentages."""
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


def yearly_summary(df):
    """Compute annual summary statistics matching dashboard's get_yearly_summary()."""
    return (
        df.groupby("Year", observed=True)
        .agg(
            n=("TotalRawScoreTRUE", "size"),
            median_raw=("TotalRawScoreTRUE", "median"),
            q25_raw=("TotalRawScoreTRUE", lambda x: x.quantile(0.25)),
            q75_raw=("TotalRawScoreTRUE", lambda x: x.quantile(0.75)),
            median_pct=("NMS_PER_num", "median"),
            q25_pct=("NMS_PER_num", lambda x: x.quantile(0.25)),
            q75_pct=("NMS_PER_num", lambda x: x.quantile(0.75)),
            median_gps=("NMS_GPS", "median"),
            median_apt=("NMS_APT", "median"),
            median_sa=("NMS_SA", "median"),
        )
        .reset_index()
    )


def write_dataframe(f, df, caption=None):
    """Write a pandas DataFrame as a markdown table."""
    if caption:
        f.write(f"**{caption}**\n\n")
    f.write(df.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    f.write("\n\n")


def kruskal_table(df, group_col, score_cols):
    """Compute Kruskal-Wallis tests for multiple score columns (matching dashboard)."""
    from scipy import stats as sp_stats
    
    results = []
    groups = df[group_col].dropna().unique()
    valid_groups = [g for g in groups if len(df[df[group_col] == g]) >= 5]
    
    for score_name, score_col in score_cols.items():
        data = {g: df[df[group_col] == g][score_col].dropna().values for g in valid_groups}
        valid_data = {k: v for k, v in data.items() if len(v) >= 5}
        
        if len(valid_data) < 2:
            continue
        
        h_stat, p_val = sp_stats.kruskal(*valid_data.values())
        
        # Eta-squared approximation (matching dashboard)
        n_total = sum(len(v) for v in valid_data.values())
        k = len(valid_data)
        eta2 = (h_stat - k + 1) / (n_total - k) if n_total > k else 0
        
        # Interpret effect size
        if eta2 < 0.01:
            effect = "Negligible"
        elif eta2 < 0.06:
            effect = "Small"
        elif eta2 < 0.14:
            effect = "Medium"
        else:
            effect = "Large"
        
        results.append({
            "Score Variable": score_name,
            "H-statistic": round(h_stat, 4),
            "p-value": p_val,
            "Eta-squared": round(max(0, eta2), 4),
            "Effect Size": effect,
            "Groups compared": len(valid_data),
            "Total N": n_total,
        })
    
    return pd.DataFrame(results)


def mannwhitney_table(df, group_col, score_cols):
    """Compute Mann-Whitney U tests for group comparisons."""
    from scipy import stats as sp_stats
    
    results = []
    groups = df[group_col].dropna().unique()
    if len(groups) != 2:
        return pd.DataFrame()
    
    g1, g2 = groups
    
    for score_name, score_col in score_cols.items():
        s1 = df[df[group_col] == g1][score_col].dropna()
        s2 = df[df[group_col] == g2][score_col].dropna()
        
        if len(s1) < 2 or len(s2) < 2:
            continue
        
        u_stat, p_val = sp_stats.mannwhitneyu(s1, s2, alternative="two-sided")
        
        # Rank-biserial correlation (effect size)
        n1, n2 = len(s1), len(s2)
        r = 1 - (2 * u_stat) / (n1 * n2)
        
        results.append({
            "Score Variable": score_name,
            f"Median ({g1})": round(s1.median(), 2),
            f"Median ({g2})": round(s2.median(), 2),
            "U-statistic": round(u_stat, 2),
            "p-value": p_val,
            "Effect size (r)": round(r, 4),
            "N1": n1,
            "N2": n2,
        })
    
    return pd.DataFrame(results)


def chi_square_table(df, row_col, col_col):
    """Compute Chi-square test of independence with expected frequencies."""
    from scipy import stats as sp_stats
    
    contingency = pd.crosstab(df[row_col], df[col_col])
    chi2, p_val, dof, expected = sp_stats.chi2_contingency(contingency)
    
    # Cramer's V
    n = contingency.sum().sum()
    min_dim = min(contingency.shape) - 1
    cramer_v = np.sqrt(chi2 / (n * min_dim)) if min_dim > 0 else 0
    
    expected_df = pd.DataFrame(
        expected,
        index=contingency.index,
        columns=contingency.columns,
    )
    
    return {
        "chi2": round(chi2, 4),
        "p_value": p_val,
        "dof": dof,
        "cramer_v": round(cramer_v, 4),
        "n": int(n),
        "observed": contingency,
        "expected": expected_df,
    }
