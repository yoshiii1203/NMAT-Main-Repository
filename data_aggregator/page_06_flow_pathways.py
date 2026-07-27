"""
Page 06 — Flow Pathways Analysis
==================================
Output: page_results/06_flow_pathways.md

Analyses:
  1. Sankey flow data: UNI_TYPE -> PercentileBin (grouped counts)
  2. Sankey flow data: CourseGroup -> PercentileBin
  3. Sankey flow data: PercentileBin -> PLE_STATUS_LABEL (observable cohort only)
  4. Top 10 pathways: UNI_TYPE -> top bins (B8-B10)
  5. Top 10 pathways: CourseGroup -> top bins
  6. Flow tables with counts for each pathway

Data subsets:
  - UNI_TYPE flow: "uni" (besttrend, Public/Private/Foreign)
  - CourseGroup flow: "besttrend"
  - PLE flow: "bestobservable" (besttrend <= 2014)
Filters: None (full unfiltered dataset)
"""
import sys
sys.path.append("data_aggregator")

import numpy as np
import pandas as pd

from config import BIN_ORDER, PLE_ORDER
from helpers import write_header, write_dataframe

MD_PATH = "page_results/06_flow_pathways.md"


def load_subsets():
    """Load required subsets directly from parquet (avoids load_data copies)."""
    import pyarrow.parquet as pq
    table = pq.read_table("dataset/NMAT_Exodus_Lite.parquet")
    df = table.to_pandas()
    del table

    # Compute derived columns
    if "Year" in df.columns:
        df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    if "PLE_STATUS_LABEL" not in df.columns:
        df["PLE_STATUS_LABEL"] = np.where(
            df["IS_PLE_ANALYSIS_SAFE"] == True,
            "Confirmed PLE passer", "No confirmed PLE match"
        )

    # besttrend: IS_BEST_NMAT_RECORD == True, Year 2006-2018
    mask_best = (
        (df.get("IS_BEST_NMAT_RECORD", pd.Series([True] * len(df))) == True)
        & (df["Year"].between(2006, 2018, inclusive="both"))
    )
    best = df.loc[mask_best].copy()

    # uni: besttrend + UNI_TYPE in Public/Private/Foreign
    mask_uni = mask_best & (df["UNI_TYPE"].isin(["Public", "Private", "Foreign"]))
    uni = df.loc[mask_uni].copy()

    # bestobservable: besttrend + Year <= 2014
    mask_obs = mask_best & (df["Year"] <= 2014)
    observable = df.loc[mask_obs].copy()

    # Free main df
    del df

    return uni, best, observable


def make_flow(df, source_col, target_col, source_order=None, target_order=None):
    """Build sankey flow table (counts) from source to target category."""
    tmp = (
        df.dropna(subset=[source_col, target_col])
        .groupby([source_col, target_col], observed=True)
        .size()
        .reset_index(name="count")
    )
    if source_order is not None:
        tmp[source_col] = pd.Categorical(tmp[source_col], categories=source_order, ordered=True)
    if target_order is not None:
        tmp[target_col] = pd.Categorical(tmp[target_col], categories=target_order, ordered=True)
    tmp = tmp.dropna(subset=[source_col, target_col]).sort_values([source_col, target_col])
    return tmp.reset_index(drop=True)


def top_pathways(df, group_col, top_bins, n=10):
    """Top-N pathways into specified top bins, by group."""
    top = (
        df[df["PercentileBin"].isin(top_bins)]
        .groupby([group_col, "PercentileBin"], observed=True)
        .size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=False)
        .head(n)
    )
    return top.reset_index(drop=True)


def run():
    print("Loading data subsets...")
    uni, best, observable = load_subsets()
    print(f"  uni: {len(uni):,}")
    print(f"  besttrend: {len(best):,}")
    print(f"  bestobservable: {len(observable):,}")

    top_bins = ["B8", "B9", "B10"]

    with open(MD_PATH, "w", encoding="utf-8") as f:
        write_header(f, "Flow Pathways Analysis (Page 06)", "besttrend + uni + bestobservable", 6)

        f.write("**Subsets used:**\n")
        f.write(f"- **uni** (UNI_TYPE flow): besttrend, UNI_TYPE in [Public, Private, Foreign] — "
                f"{len(uni):,} records\n")
        f.write(f"- **besttrend** (CourseGroup flow): best NMAT record, Year 2006-2018 — "
                f"{len(best):,} records\n")
        f.write(f"- **bestobservable** (Bin -> PLE flow): besttrend, Year <= 2014 — "
                f"{len(observable):,} records\n\n")
        f.write("---\n\n")

        # ── 1. UNI_TYPE -> PercentileBin ──
        f.write("## 1. Sankey Flow: UNI_TYPE -> PercentileBin\n\n")
        f.write("Source: `uni` subset (besttrend, Public/Private/Foreign)\n\n")

        source_order_uni = ["Public", "Private", "Foreign"]
        flow_uni = make_flow(uni, "UNI_TYPE", "PercentileBin",
                             source_order=source_order_uni, target_order=BIN_ORDER)
        write_dataframe(
            f, flow_uni,
            "Table 06-1. University-type to percentile bin flow counts"
        )

        # Pivot for matrix view
        f.write("### 1b. Flow matrix (UNI_TYPE rows, PercentileBin columns)\n\n")
        flow_uni_pivot = (
            flow_uni.pivot(index="UNI_TYPE", columns="PercentileBin", values="count")
            .reindex(index=source_order_uni, columns=BIN_ORDER)
            .fillna(0).astype(int)
        )
        write_dataframe(
            f, flow_uni_pivot.reset_index(),
            "Table 06-2. UNI_TYPE -> PercentileBin flow matrix"
        )

        f.write("### 1c. Row percentages (within UNI_TYPE)\n\n")
        flow_uni_pct = flow_uni_pivot.div(flow_uni_pivot.sum(axis=1).replace(0, np.nan),
                                          axis=0).mul(100).round(2)
        write_dataframe(
            f, flow_uni_pct.reset_index(),
            "Table 06-3. UNI_TYPE -> PercentileBin row percentages"
        )

        f.write("---\n\n")

        # ── 2. CourseGroup -> PercentileBin ──
        f.write("## 2. Sankey Flow: CourseGroup -> PercentileBin\n\n")
        f.write("Source: `besttrend` subset\n\n")

        course_order = [
            "Medical & Allied", "Natural Sciences", "Social & Behavioral Sciences",
            "Education", "Engineering & Technology", "Other",
        ]
        existing_courses = [c for c in course_order if c in best["CourseGroup"].unique()]
        flow_course = make_flow(best, "CourseGroup", "PercentileBin",
                                source_order=existing_courses, target_order=BIN_ORDER)
        write_dataframe(
            f, flow_course,
            "Table 06-4. Course group to percentile bin flow counts"
        )

        f.write("### 2b. Flow matrix (CourseGroup rows, PercentileBin columns)\n\n")
        flow_course_pivot = (
            flow_course.pivot(index="CourseGroup", columns="PercentileBin", values="count")
            .reindex(index=existing_courses, columns=BIN_ORDER)
            .fillna(0).astype(int)
        )
        write_dataframe(
            f, flow_course_pivot.reset_index(),
            "Table 06-5. CourseGroup -> PercentileBin flow matrix"
        )

        f.write("### 2c. Row percentages (within CourseGroup)\n\n")
        flow_course_pct = flow_course_pivot.div(
            flow_course_pivot.sum(axis=1).replace(0, np.nan), axis=0
        ).mul(100).round(2)
        write_dataframe(
            f, flow_course_pct.reset_index(),
            "Table 06-6. CourseGroup -> PercentileBin row percentages"
        )

        f.write("---\n\n")

        # ── 3. PercentileBin -> PLE_STATUS_LABEL (observable cohort) ──
        f.write("## 3. Sankey Flow: PercentileBin -> PLE_STATUS_LABEL\n\n")
        f.write("Source: `bestobservable` subset (besttrend, Year <= 2014)\n\n")

        flow_ple = make_flow(observable, "PercentileBin", "PLE_STATUS_LABEL",
                             source_order=BIN_ORDER, target_order=PLE_ORDER)
        write_dataframe(
            f, flow_ple,
            "Table 06-7. Percentile bin to PLE status flow counts (observable cohort)"
        )

        f.write("### 3b. PLE status composition within each bin (row %)\n\n")
        flow_ple_pivot = (
            flow_ple.pivot(index="PercentileBin", columns="PLE_STATUS_LABEL", values="count")
            .reindex(index=BIN_ORDER, columns=PLE_ORDER)
            .fillna(0)
        )
        flow_ple_pct = flow_ple_pivot.div(
            flow_ple_pivot.sum(axis=1).replace(0, np.nan), axis=0
        ).mul(100).round(2)
        write_dataframe(
            f, flow_ple_pct.reset_index(),
            "Table 06-8. PLE status row percentages within each bin"
        )

        f.write("### 3c. Confirmed PLE passer rate by bin\n\n")
        ple_rate_rows = []
        for bin_label in BIN_ORDER:
            if bin_label in flow_ple_pct.index:
                rate = flow_ple_pct.loc[bin_label, "Confirmed PLE passer"]
                n_ple = int(flow_ple_pivot.loc[bin_label, "Confirmed PLE passer"]) if bin_label in flow_ple_pivot.index else 0
                n_total = int(flow_ple_pivot.loc[bin_label].sum()) if bin_label in flow_ple_pivot.index else 0
            else:
                rate = 0.0
                n_ple = 0
                n_total = 0
            ple_rate_rows.append({
                "PercentileBin": bin_label,
                "Confirmed PLE Passers": n_ple,
                "Total in Bin": n_total,
                "PLE Pass Rate (%)": round(rate, 2),
            })
        ple_rate_df = pd.DataFrame(ple_rate_rows)
        write_dataframe(f, ple_rate_df, "Table 06-9. PLE pass rate by percentile bin")

        f.write("---\n\n")

        # ── 4. Top 10 pathways: UNI_TYPE -> top bins (B8-B10) ──
        f.write("## 4. Top 10 Pathways: UNI_TYPE -> B8-B10\n\n")
        f.write("Source: `uni` subset (besttrend, Public/Private/Foreign)\n\n")

        top_uni = top_pathways(uni, "UNI_TYPE", top_bins, n=10)
        write_dataframe(
            f, top_uni,
            "Table 06-10. Top 10 UNI_TYPE pathways into B8-B10"
        )

        top_uni_ranked = top_uni.copy()
        top_uni_ranked.insert(0, "Rank", range(1, len(top_uni_ranked) + 1))
        write_dataframe(
            f, top_uni_ranked,
            "Table 06-11. Top 10 UNI_TYPE pathways (ranked)"
        )

        f.write("### 4b. Full summary: UNI_TYPE top-bin counts\n\n")
        top_uni_full = (
            uni[uni["PercentileBin"].isin(top_bins)]
            .groupby(["UNI_TYPE", "PercentileBin"], observed=True)
            .size()
            .reset_index(name="Count")
            .sort_values(["UNI_TYPE", "PercentileBin"])
        )
        write_dataframe(
            f, top_uni_full,
            "Table 06-12. Full UNI_TYPE -> top-bin breakdown"
        )

        f.write("---\n\n")

        # ── 5. Top 10 pathways: CourseGroup -> top bins ──
        f.write("## 5. Top 10 Pathways: CourseGroup -> B8-B10\n\n")
        f.write("Source: `besttrend` subset\n\n")

        top_course = top_pathways(best, "CourseGroup", top_bins, n=10)
        write_dataframe(
            f, top_course,
            "Table 06-13. Top 10 CourseGroup pathways into B8-B10"
        )

        top_course_ranked = top_course.copy()
        top_course_ranked.insert(0, "Rank", range(1, len(top_course_ranked) + 1))
        write_dataframe(
            f, top_course_ranked,
            "Table 06-14. Top 10 CourseGroup pathways (ranked)"
        )

        f.write("### 5b. Full summary: CourseGroup top-bin counts\n\n")
        top_course_full = (
            best[best["PercentileBin"].isin(top_bins)]
            .groupby(["CourseGroup", "PercentileBin"], observed=True)
            .size()
            .reset_index(name="Count")
            .sort_values(["CourseGroup", "PercentileBin"])
        )
        write_dataframe(
            f, top_course_full,
            "Table 06-15. Full CourseGroup -> top-bin breakdown"
        )

        f.write("---\n\n")

        # ── 6. Cross-flow comparison tables ──
        f.write("## 6. Cross-Flow Comparisons\n\n")

        f.write("### 6a. Top-bin rate by UNI_TYPE\n\n")
        top_rate_uni = (
            uni.groupby("UNI_TYPE", observed=True)
            .apply(
                lambda g: pd.Series({
                    "Total N": len(g),
                    "Top Bin N": g["PercentileBin"].isin(top_bins).sum(),
                    "Top Bin Rate (%)": round(
                        g["PercentileBin"].isin(top_bins).mean() * 100, 2
                    ),
                }),
                include_groups=False,
            )
            .reset_index()
        )
        write_dataframe(f, top_rate_uni, "Table 06-16. Top-bin rate by UNI_TYPE")

        f.write("### 6b. Top-bin rate by CourseGroup\n\n")
        top_rate_course = (
            best.groupby("CourseGroup", observed=True)
            .apply(
                lambda g: pd.Series({
                    "Total N": len(g),
                    "Top Bin N": g["PercentileBin"].isin(top_bins).sum(),
                    "Top Bin Rate (%)": round(
                        g["PercentileBin"].isin(top_bins).mean() * 100, 2
                    ),
                }),
                include_groups=False,
            )
            .reset_index()
        )
        write_dataframe(f, top_rate_course, "Table 06-17. Top-bin rate by CourseGroup")

        f.write("### 6c. Top-bin rate by UNI_TYPE x CourseGroup\n\n")
        uni_course_cross = (
            uni.groupby(["UNI_TYPE", "CourseGroup"], observed=True)
            .apply(
                lambda g: pd.Series({
                    "Total N": len(g),
                    "Top Bin N": g["PercentileBin"].isin(top_bins).sum(),
                    "Top Bin Rate (%)": round(
                        g["PercentileBin"].isin(top_bins).mean() * 100, 2
                    ),
                }),
                include_groups=False,
            )
            .reset_index()
            .sort_values("Top Bin Rate (%)", ascending=False)
        )
        write_dataframe(
            f, uni_course_cross,
            "Table 06-18. Top-bin rate by UNI_TYPE x CourseGroup"
        )

        f.write("### 6d. Course composition within each UNI_TYPE\n\n")
        course_comp = (
            uni.groupby(["UNI_TYPE", "CourseGroup"], observed=True)
            .size()
            .reset_index(name="Count")
        )
        course_comp["Percent within UNI_TYPE"] = (
            course_comp.groupby("UNI_TYPE", observed=True)["Count"]
            .transform(lambda x: x / x.sum() * 100)
        ).round(2)
        course_comp = course_comp.sort_values(["UNI_TYPE", "Count"], ascending=[True, False])
        write_dataframe(
            f, course_comp,
            "Table 06-19. Course composition within each UNI_TYPE"
        )

        f.write("\n---\n")
        f.write("*Analysis complete. Generated by page_06_flow_pathways.py*\n")

    print(f"[OK] Page 06 written to {MD_PATH}")


def save():
    """Alias for run()."""
    run()


if __name__ == "__main__":
    run()
