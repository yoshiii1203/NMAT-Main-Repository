"""
helpers.py — Shared functions for CHED computation suite.

Loading and subsetting delegates to ../ched_common.py -- the same module
dashboard.py and export_markdown.py use -- so this "third pipeline" can
never again drift from the live dashboard the way it did before (see
audit 06 findings F2-F4: a missing dtype-coercion step here produced a
self-contradicting "0 (99.97%)" statistic in 06_data_limitations.md).
"""

import datetime
import os
import sys

import pandas as pd
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import ched_common as cc

from config import (
    OUTPUT_DIR,
    BIN_ORDER,
    PLE_OBSERVABLE_MAX_YEAR,
    DATA_CAVEAT,
    OBSERVABLE_CAVEAT,
    LINKAGE_LABEL,
)


def load_data() -> pd.DataFrame:
    """Load and validate NMAT_Exodus.parquet via ched_common (shared dtype
    coercion -- fixes the string-as-boolean bug for every script here, not
    just 06)."""
    df, _, _ = cc.load_and_validate()
    return df


def create_subsets(df: pd.DataFrame) -> dict:
    """Return dict of commonly used subsets.

    Returns:
        dict with keys:
          'full'                    — all records
          'best'                    — best record per person (IS_BEST_NMAT_RECORD)
          'best_pre2015'            — the genuine observable cohort: each person's best
                                       attempt among Year <= 2014 rows (IS_BEST_OBSERVABLE_RECORD).
                                       NOT `best[best.Year <= 2014]`, which silently drops people
                                       whose overall-best attempt fell after 2014 (contract §2a).
          'best_ple_matched'        — best records that are confirmed PLE passers (IS_PLE_PASSER)
          'best_ple_matched_pre2015'— confirmed PLE passers within the observable cohort
          'uni'                     — best records at Public/Private undergraduate institutions
    """
    best = df[df["IS_BEST_NMAT_RECORD"] == True].copy()
    best_pre2015 = df[df["IS_BEST_OBSERVABLE_RECORD"] == True].copy()
    best_pre2015["HAS_CONFIRMED_PLE"] = best_pre2015["IS_PLE_PASSER"] == True

    best_ple_matched = best[best["IS_PLE_PASSER"] == True].copy()
    best_ple_matched_pre2015 = best_pre2015[best_pre2015["HAS_CONFIRMED_PLE"]].copy()

    uni = best[best[cc.UNI_TYPE_COL].isin(["Public", "Private"])].copy()

    return {
        "full": df,
        "best": best,
        "best_pre2015": best_pre2015,
        "best_ple_matched": best_ple_matched,
        "best_ple_matched_pre2015": best_ple_matched_pre2015,
        "uni": uni,
    }


def create_clean_subset(df_obs: pd.DataFrame) -> pd.DataFrame:
    """Return strictest defensible PLE subset: confirmed passer, >=5yr gap, Filipino."""
    if "HAS_CONFIRMED_PLE" not in df_obs.columns:
        df_obs = df_obs.copy()
        df_obs["HAS_CONFIRMED_PLE"] = df_obs["IS_PLE_PASSER"] == True
    return df_obs[
        (df_obs["HAS_CONFIRMED_PLE"])
        & (df_obs["PLE_YEAR_GAP"] >= 5)
        & (df_obs["FOREIGNER_STATUS"] == "Filipino")
    ].copy()


def today_str() -> str:
    """Return today's date as a string for markdown."""
    return datetime.datetime.now().strftime("%B %d, %Y")


def write_md(script_number: str, content: str) -> str:
    """Write content to markdown file and return the path."""
    path = os.path.join(OUTPUT_DIR, f"{script_number}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def pct(val: float, decimals: int = 2) -> str:
    """Format a float as a percentage string."""
    return f"{val:.{decimals}f}%"


def fmt(val, decimals: int = 2) -> str:
    """Format a number with commas (if int) or decimal places (if float)."""
    if isinstance(val, (int, np.integer)):
        return f"{val:,}"
    elif isinstance(val, (float, np.floating)):
        if pd.isna(val):
            return "N/A"
        return f"{val:,.{decimals}f}"
    return str(val)


def make_metric_table(metrics: list) -> str:
    """Build a simple 2-column metric card table.

    metrics: list of (label, value_str) tuples.
    """
    lines = ["| Metric | Value |", "|--------|-------|"]
    for label, value in metrics:
        lines.append(f"| **{label}** | {value} |")
    return "\n".join(lines)


def compute_linkage_rate(
    numer: int, denom: int, label: str = LINKAGE_LABEL
) -> str:
    """Compute a linkage rate with appropriate label."""
    if denom == 0:
        return "N/A (no examinees)"
    rate = (numer / denom) * 100
    return f"{rate:.2f}% ({numer:,} / {denom:,})"


def write_output(script_number: str, title: str, body: str) -> str:
    """Assemble full markdown output, write, and return path."""
    df, _, _ = cc.load_and_validate()
    header = f"""# {title}

**Date:** {today_str()}
**Data Source:** `NMAT_Exodus.parquet` ({len(df):,} records, {df.shape[1]} columns)
**Script:** `ched_compute/{script_number}.py`

---

"""
    caveats = f"\n{DATA_CAVEAT}\n{OBSERVABLE_CAVEAT}\n"
    full = header + body + caveats
    path = write_md(script_number, full)
    return path
