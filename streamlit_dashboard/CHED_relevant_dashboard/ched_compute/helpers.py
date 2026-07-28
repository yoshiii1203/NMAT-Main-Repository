"""
helpers.py — Shared functions for CHED computation suite.
"""

import datetime
import pandas as pd
import numpy as np
from config import (
    EXODUS_PATH,
    OUTPUT_DIR,
    BIN_ORDER,
    PLE_OBSERVABLE_MAX_YEAR,
    DATA_CAVEAT,
    OBSERVABLE_CAVEAT,
    LINKAGE_LABEL,
)


def load_data() -> pd.DataFrame:
    """Load NMAT_Exodus.parquet and return full DataFrame."""
    df = pd.read_parquet(EXODUS_PATH)
    df["Year"] = df["Year"].astype(int)
    return df


def create_subsets(df: pd.DataFrame) -> dict:
    """Return dict of commonly used subsets.

    Returns:
        dict with keys:
          'full'                    — all records
          'best'                    — best record per person
          'best_pre2015'            — best records, Year <= PLE_OBSERVABLE_MAX_YEAR
          'best_ple_matched'        — best records that matched PLE (IS_PLE_PASSER == True)
          'best_ple_matched_pre2015'— best PLE-matched, Year <= PLE_OBSERVABLE_MAX_YEAR
          'uni'                     — best records at Public/Private HEIs
    """
    best = df[df["IS_BEST_NMAT_RECORD"] == True].copy()
    best_pre2015 = best[best["Year"] <= PLE_OBSERVABLE_MAX_YEAR].copy()

    best_ple_matched = best[best["IS_PLE_ANALYSIS_SAFE"] == True].copy() if "IS_PLE_ANALYSIS_SAFE" in best.columns else best[best["IS_PLE_PASSER"] == True].copy()
    best_ple_matched_pre2015 = best_ple_matched[
        best_ple_matched["Year"] <= PLE_OBSERVABLE_MAX_YEAR
    ].copy()

    uni = best[best["UNI_TYPE"].isin(["Public", "Private"])].copy()

    return {
        "full": df,
        "best": best,
        "best_pre2015": best_pre2015,
        "best_ple_matched": best_ple_matched,
        "best_ple_matched_pre2015": best_ple_matched_pre2015,
        "uni": uni,
    }


def create_clean_subset(df_obs: pd.DataFrame) -> pd.DataFrame:
    """Return strictest defensible PLE subset: best record, IS_PLE_ANALYSIS_SAFE, >=5yr gap, Filipino."""
    return df_obs[
        (df_obs["IS_PLE_ANALYSIS_SAFE"] == True)
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
    header = f"""# {title}

**Date:** {today_str()}
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/{script_number}.py`

---

"""
    caveats = f"\n{DATA_CAVEAT}\n{OBSERVABLE_CAVEAT}\n"
    full = header + body + caveats
    path = write_md(script_number, full)
    return path


# Re-export for convenience
import os
