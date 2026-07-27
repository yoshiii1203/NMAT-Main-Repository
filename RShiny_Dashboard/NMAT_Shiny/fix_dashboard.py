#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_dashboard.py  (ASCII-safe version)
Inserts dt_export data tables after every plot chunk that lacks one.
Tabset removal and dt_export upgrade already applied in previous partial run.
"""

import re, os, sys

# Force ASCII-safe stdout
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='ascii', errors='replace')

PATH = os.path.join(os.path.dirname(__file__), "NMAT_Dashboard_v2.Rmd")

def find_chunk_end(lines, start):
    for i in range(start + 1, len(lines)):
        if lines[i].rstrip() == "```":
            return i
    return -1

def insert_after_chunk(lines, label, body):
    pat = re.compile(r"^```\{r\s+" + re.escape(label) + r"\b")
    for i, line in enumerate(lines):
        if pat.match(line):
            end = find_chunk_end(lines, i)
            if end < 0:
                print(f"  ERR end-not-found: {label}")
                return lines, False
            insert_lines = [""] + body.split("\n")
            lines = lines[: end + 1] + insert_lines + lines[end + 1 :]
            print(f"  OK  {label}")
            return lines, True
    print(f"  SKIP not-found: {label}")
    return lines, False

with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Also ensure tabset removal and dt_export upgrade in case they weren't applied
n_ts = content.count(" {.tabset}")
if n_ts:
    content = content.replace(" {.tabset}", "")
    print(f"[pre] Removed {n_ts} {{.tabset}} occurrences")

OLD_DOM = '      dom     = "Bfrtip",'
NEW_DOM = '      dom     = "Blfrtip",'
if OLD_DOM in content:
    content = content.replace(OLD_DOM, NEW_DOM, 1)
    print("[pre] Updated dom to Blfrtip")

OLD_PL = "      pageLength = 25\n"
NEW_PL = '      pageLength = 25,\n      lengthMenu = list(c(25, 50, 100, -1), c("25", "50", "100", "All"))\n'
if OLD_PL in content:
    content = content.replace(OLD_PL, NEW_PL, 1)
    print("[pre] Updated pageLength with lengthMenu")

lines = content.split("\n")

INSERTS = [
    # ── Executive Summary ────────────────────────────────────────────────────
    ("p01_trend", """\
```{r p01_trend_tbl, echo=FALSE}
dt_export(s, "Annual NMAT Score Summary by Year")
```"""),

    ("p01_course_pie", """\
```{r p01_course_tbl, echo=FALSE}
dt_export(ct_course, "Course Group Composition - Counts")
```"""),

    ("p01_uni_pie", """\
```{r p01_uni_tbl, echo=FALSE}
dt_export(ct_uni, "University Type Composition - Counts")
```"""),

    # ── Performance Trends ───────────────────────────────────────────────────
    ("p03_trend_fig", """\
```{r p03_trend_tbl, echo=FALSE}
dt_export(s_p03, "Annual Score Summary (Performance Trends)")
```"""),

    ("p03_box_raw", """\
```{r p03_raw_yr_tbl, echo=FALSE}
tbl_p03_raw_yr <- F_besttrend %>%
  dplyr::filter(!is.na(Year), !is.na(TotalRawScoreTRUE)) %>%
  dplyr::group_by(Year) %>%
  dplyr::summarise(n = dplyr::n(),
    median = round(median(TotalRawScoreTRUE, na.rm = TRUE), 2),
    q25    = round(quantile(TotalRawScoreTRUE, .25, na.rm = TRUE), 2),
    q75    = round(quantile(TotalRawScoreTRUE, .75, na.rm = TRUE), 2),
    .groups = "drop")
dt_export(tbl_p03_raw_yr, "Total Raw Score Statistics by Year")
```"""),

    ("p03_box_pct", """\
```{r p03_pct_yr_tbl, echo=FALSE}
tbl_p03_pct_yr <- F_besttrend %>%
  dplyr::filter(!is.na(Year), !is.na(NMS_PER_num)) %>%
  dplyr::group_by(Year) %>%
  dplyr::summarise(n = dplyr::n(),
    median = round(median(NMS_PER_num, na.rm = TRUE), 2),
    q25    = round(quantile(NMS_PER_num, .25, na.rm = TRUE), 2),
    q75    = round(quantile(NMS_PER_num, .75, na.rm = TRUE), 2),
    .groups = "drop")
dt_export(tbl_p03_pct_yr, "Percentile Rank Statistics by Year")
```"""),

    # ── Score Bins by Year ───────────────────────────────────────────────────
    ("p04_heatmap_year", """\
```{r p04_heatmap_year_pct, echo=FALSE}
dt_export(res_yr$pct %>% dplyr::mutate(Year = as.character(Year)),
          "Bin Percentages by Year (row %)")
```"""),

    ("p04_stacked_year", """\
```{r p04_stacked_yr_tbl, echo=FALSE}
dt_export(res_stk$pct %>% dplyr::mutate(Year = as.character(Year)),
          "Bin Composition by Year (%)")
```"""),

    ("p04_topbottom_year", """\
```{r p04_topbot_tbl, echo=FALSE}
tbl_tb <- s_tb %>%
  dplyr::select(Year, top, bottom) %>%
  dplyr::rename(Top_B8_B10_pct = top, Bottom_B1_B3_pct = bottom)
dt_export(tbl_tb, "Top vs Bottom Bin Share by Year")
```"""),

    # ── Score Bins by University Type ────────────────────────────────────────
    ("p04_heatmap_uni", """\
```{r p04_heatmap_uni_tbl, echo=FALSE}
dt_export(res_uni$pct, "Bin Percentages by University Type (row %)")
```"""),

    ("p04_top_uni", """\
```{r p04_top_uni_tbl, echo=FALSE}
dt_export(top_uni, "Top Bin Share (B8-B10) by University Type")
```"""),

    ("p04_faceted", """\
```{r p04_faceted_tbl, echo=FALSE}
df_fac_wide <- df_fac %>%
  tidyr::pivot_wider(names_from = PercentileBin, values_from = n, values_fill = 0L)
dt_export(df_fac_wide, "Examinees by Year, University Type, and Bin (Counts)")
```"""),

    # ── Pseudo-citizenship ───────────────────────────────────────────────────
    ("p04_pc_pie_fvf", """\
```{r p04_pc_fvf_tbl, echo=FALSE}
if (pc_available) dt_export(ct_fvf, "Foreigners vs Filipinos (Counts)")
```"""),

    ("p04_pc_top15", """\
```{r p04_pc_top15_tbl, echo=FALSE}
if (pc_available) dt_export(top15_pc, "Top 15 Pseudo-citizenship Groups by Count")
```"""),

    ("p04_pc_stacked", """\
```{r p04_pc_stacked_tbl, echo=FALSE}
if (pc_available && "PercentileBin" %in% names(pc_base)) {
  top15g <- (pc_base %>% dplyr::count(pseudo_citizenship) %>%
               dplyr::arrange(dplyr::desc(n)) %>% head(15))$pseudo_citizenship
  sub15  <- pc_base %>% dplyr::filter(pseudo_citizenship %in% top15g)
  if (nrow(sub15) > 0) {
    res15 <- pct_cross(sub15, "pseudo_citizenship", "PercentileBin", BIN_ORDER)
    dt_export(res15$pct, "Bin % by Pseudo-citizenship Top 15 (row %)")
  }
}
```"""),

    ("p04_pc_heatmap_all", """\
```{r p04_pc_heatmap_all_tbl, echo=FALSE}
if (pc_available && "PercentileBin" %in% names(pc_base)) {
  res_all <- pct_cross(pc_base, "pseudo_citizenship", "PercentileBin", BIN_ORDER)
  dt_export(res_all$pct, "Full Bin % by Pseudo-citizenship (row %)")
}
```"""),

    ("p04_pc_topbin", """\
```{r p04_pc_topbin_tbl, echo=FALSE}
if (pc_available && "PercentileBin" %in% names(pc_base)) {
  td2 <- pc_base %>%
    dplyr::mutate(is_top = PercentileBin %in% c("B8","B9","B10"),
                  is_bot = PercentileBin %in% c("B1","B2","B3")) %>%
    dplyr::group_by(pseudo_citizenship) %>%
    dplyr::summarise(n       = dplyr::n(),
                     top_n   = sum(is_top, na.rm = TRUE),
                     bot_n   = sum(is_bot, na.rm = TRUE),
                     .groups = "drop") %>%
    dplyr::filter(n >= 3) %>%
    dplyr::mutate(top_pct = round(top_n / n * 100, 1),
                  bot_pct = round(bot_n / n * 100, 1)) %>%
    dplyr::arrange(dplyr::desc(top_pct))
  dt_export(td2, "Top & Bottom Bin Share by Pseudo-citizenship")
}
```"""),

    ("p04_pc_box_pct", """\
```{r p04_pc_box_pct_tbl, echo=FALSE}
if (pc_available && "NMS_PER_num" %in% names(pc_base)) {
  stats_pct <- pc_base %>%
    dplyr::group_by(pseudo_citizenship) %>%
    dplyr::filter(dplyr::n() >= 5) %>%
    dplyr::summarise(n      = dplyr::n(),
                     median = round(median(NMS_PER_num, na.rm = TRUE), 2),
                     q25    = round(quantile(NMS_PER_num, .25, na.rm = TRUE), 2),
                     q75    = round(quantile(NMS_PER_num, .75, na.rm = TRUE), 2),
                     .groups = "drop") %>%
    dplyr::arrange(dplyr::desc(median))
  dt_export(stats_pct, "Percentile Rank Stats by Pseudo-citizenship (n>=5)")
}
```"""),

    ("p04_pc_box_raw", """\
```{r p04_pc_box_raw_tbl, echo=FALSE}
if (pc_available && "TotalRawScoreTRUE" %in% names(pc_base)) {
  stats_raw <- pc_base %>%
    dplyr::group_by(pseudo_citizenship) %>%
    dplyr::filter(dplyr::n() >= 5) %>%
    dplyr::summarise(n      = dplyr::n(),
                     median = round(median(TotalRawScoreTRUE, na.rm = TRUE), 2),
                     q25    = round(quantile(TotalRawScoreTRUE, .25, na.rm = TRUE), 2),
                     q75    = round(quantile(TotalRawScoreTRUE, .75, na.rm = TRUE), 2),
                     .groups = "drop") %>%
    dplyr::arrange(dplyr::desc(median))
  dt_export(stats_raw, "TRUE Raw Score Stats by Pseudo-citizenship (n>=5)")
}
```"""),

    # ── Comparative groups ───────────────────────────────────────────────────
    ("p04_cmp_heatmap", """\
```{r p04_cmp_heatmap_tbl, echo=FALSE}
if (!is.null(cmp_df) && nrow(cmp_df) > 0 && "PercentileBin" %in% names(cmp_df)) {
  res_cmp2 <- pct_cross(cmp_df, "cmp_group", "PercentileBin", BIN_ORDER)
  dt_export(res_cmp2$pct, "Bin % by Comparison Group (row %)")
}
```"""),

    ("p04_cmp_stacked", """\
```{r p04_cmp_stacked_tbl, echo=FALSE}
if (!is.null(cmp_df) && nrow(cmp_df) > 0 && "PercentileBin" %in% names(cmp_df)) {
  res_cmp3 <- pct_cross(cmp_df, "cmp_group", "PercentileBin", BIN_ORDER)
  dt_export(res_cmp3$counts, "Bin Counts by Comparison Group")
}
```"""),

    ("p04_cmp_topbot", """\
```{r p04_cmp_topbot_tbl, echo=FALSE}
if (!is.null(cmp_df) && nrow(cmp_df) > 0 && "PercentileBin" %in% names(cmp_df)) {
  dt_export(cmp_tb, "Top vs Bottom Bin % by Comparison Group")
}
```"""),

    # ── Score Bins by Course Group ───────────────────────────────────────────
    ("p04_top_course", """\
```{r p04_top_course_tbl, echo=FALSE}
dt_export(top_cg, "Top Bin Share (B8-B10) by Course Group")
```"""),

    # ── University Type Analysis ─────────────────────────────────────────────
    ("p05_inst_heatmap", """\
```{r p05_inst_heatmap_tbl, echo=FALSE}
dt_export(res_p05c$pct, "Bin % by Institution x Location (row %)")
```"""),

    ("p05_top_bin_bar", """\
```{r p05_top_bin_bar_tbl, echo=FALSE}
dt_export(top_p05d, "Top Bin (B8-B10) Share by Institution x Location")
```"""),

    ("p05_stacked_bin", """\
```{r p05_stacked_bin_tbl, echo=FALSE}
dt_export(res_p05e$pct, "Bin Composition by University Type (%)")
```"""),

    ("p05_med_other", """\
```{r p05_med_other_tbl, echo=FALSE}
dt_export(res_p05f$pct, "Medical & Allied vs Other Courses by University Type (%)")
```"""),

    # ── PLE Alignment ────────────────────────────────────────────────────────
    ("p07_boxplot", """\
```{r p07_boxplot_tbl, echo=FALSE}
tbl_ple_scores <- F_bestobs %>%
  dplyr::filter(!is.na(PLE_STATUS_LABEL)) %>%
  dplyr::group_by(PLE_STATUS_LABEL) %>%
  dplyr::summarise(n            = dplyr::n(),
    median_raw   = round(median(TotalRawScoreTRUE, na.rm = TRUE), 2),
    q25_raw      = round(quantile(TotalRawScoreTRUE, .25, na.rm = TRUE), 2),
    q75_raw      = round(quantile(TotalRawScoreTRUE, .75, na.rm = TRUE), 2),
    median_pct   = round(median(NMS_PER_num, na.rm = TRUE), 2),
    q25_pct      = round(quantile(NMS_PER_num, .25, na.rm = TRUE), 2),
    q75_pct      = round(quantile(NMS_PER_num, .75, na.rm = TRUE), 2),
    .groups      = "drop")
dt_export(tbl_ple_scores, "Score Statistics by PLE Status")
```"""),

    ("p07_bin_stacked", """\
```{r p07_bin_stacked_tbl, echo=FALSE}
dt_export(res_p07_bin$pct, "Bin Distribution by PLE Status (%)")
```"""),

    ("p07_pass_bar", """\
```{r p07_pass_bar_tbl, echo=FALSE}
dt_export(res_p07_pass %>% dplyr::select(-color),
          "Confirmed PLE Pass Rate by NMAT Bin")
```"""),

    # ── Repeat Takers ────────────────────────────────────────────────────────
    ("p08_box_change", """\
```{r p08_change_stats_tbl, echo=FALSE}
tbl_rpt_change <- repeat_data$rep_df %>%
  dplyr::summarise(
    n_repeat          = dplyr::n(),
    improved_pct_n    = sum(pct_change > 0, na.rm = TRUE),
    improved_pct_pct  = round(mean(pct_change > 0, na.rm = TRUE) * 100, 2),
    median_pct_change = round(median(pct_change, na.rm = TRUE), 2),
    mean_pct_change   = round(mean(pct_change, na.rm = TRUE), 2),
    sd_pct_change     = round(sd(pct_change, na.rm = TRUE), 2),
    improved_raw_n    = sum(raw_change > 0, na.rm = TRUE),
    improved_raw_pct  = round(mean(raw_change > 0, na.rm = TRUE) * 100, 2),
    median_raw_change = round(median(raw_change, na.rm = TRUE), 2),
    mean_raw_change   = round(mean(raw_change, na.rm = TRUE), 2),
    sd_raw_change     = round(sd(raw_change, na.rm = TRUE), 2)
  )
dt_export(tbl_rpt_change, "Repeat-Taker Score Change Summary Statistics")
```"""),

    ("p08_scatter", """\
```{r p08_scatter_tbl, echo=FALSE}
dt_export(
  rd_p08_sc %>%
    dplyr::select(PERSON_KEY, n_attempts, first_year, last_year,
                  first_pct, last_pct, pct_change, first_raw, last_raw, raw_change) %>%
    dplyr::arrange(dplyr::desc(abs(pct_change))),
  "Repeat-Taker First vs Last Attempt - Full Detail"
)
```"""),

    # ── Year Gap & Gender ────────────────────────────────────────────────────
    ("p10_gap_hist", """\
```{r p10_gap_hist_tbl, echo=FALSE}
tbl_gap_dist <- gap_df %>%
  dplyr::filter(!is.na(PLE_YEAR_GAP)) %>%
  dplyr::count(PLE_YEAR_GAP) %>%
  dplyr::mutate(pct = round(n / sum(n) * 100, 2)) %>%
  dplyr::arrange(PLE_YEAR_GAP)
dt_export(tbl_gap_dist, "NMAT-to-PLE Year Gap Distribution")
```"""),

    ("p10_sex_box", """\
```{r p10_sex_box_tbl, echo=FALSE}
tbl_sex_box <- sex_base %>%
  dplyr::group_by(SEX_CLEAN) %>%
  dplyr::summarise(n           = dplyr::n(),
    median_pct  = round(median(NMS_PER_num, na.rm = TRUE), 2),
    q25_pct     = round(quantile(NMS_PER_num, .25, na.rm = TRUE), 2),
    q75_pct     = round(quantile(NMS_PER_num, .75, na.rm = TRUE), 2),
    median_raw  = round(median(TotalRawScoreTRUE, na.rm = TRUE), 2),
    .groups     = "drop")
dt_export(tbl_sex_box, "Percentile Rank & Raw Score Statistics by Sex")
```"""),

    ("p10_sex_year", """\
```{r p10_sex_yr_tbl, echo=FALSE}
tbl_sex_yr <- pct_cross(
  sex_base %>% dplyr::filter(!is.na(Year)),
  "Year", "SEX_CLEAN", c("Male", "Female")
)
dt_export(tbl_sex_yr$pct, "Sex Composition by NMAT Year (%)")
```"""),

    # ── Statistical Tests ────────────────────────────────────────────────────
    ("p11_chi_heatmap", """\
```{r p11_chi_heatmap_tbl, echo=FALSE}
pct_chi3_df <- as.data.frame(pct_chi3)
pct_chi3_df$UNI_TYPE <- rownames(pct_chi3_df)
rownames(pct_chi3_df) <- NULL
avail_b <- intersect(BIN_ORDER, names(pct_chi3_df))
dt_export(pct_chi3_df[, c("UNI_TYPE", avail_b), drop = FALSE],
          "University Type x Bin Row Percentages")
```"""),
]

ok_count = 0
for label, body in INSERTS:
    lines, ok = insert_after_chunk(lines, label, body)
    if ok:
        ok_count += 1

print(f"\n[3] {ok_count}/{len(INSERTS)} tables inserted")

content = "\n".join(lines)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

line_count = len(lines)
print(f"File written. Lines: {line_count}")
