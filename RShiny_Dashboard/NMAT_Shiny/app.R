# =============================================================
# NMAT Performance Dashboard — R Shiny
# Covers all 12 pages from the original Streamlit dashboard.
# Data source: NMAT_Exodus.parquet (enriched by Pipeline 4)
# =============================================================

# ── 1. PACKAGES ───────────────────────────────────────────────
suppressPackageStartupMessages({
  library(shiny)
  library(shinydashboard)
  library(shinyWidgets)   # pickerInput, etc.
  library(arrow)          # read_parquet
  library(dplyr)
  library(tidyr)
  library(ggplot2)
  library(plotly)
  library(DT)
  library(scales)
  library(RColorBrewer)
  library(htmltools)
})

# Optional — Dunn post-hoc test
HAS_DUNN <- requireNamespace("dunn.test", quietly = TRUE)

# ── 2. CONSTANTS ──────────────────────────────────────────────
BIN_ORDER <- paste0("B", 1:10)
PLE_ORDER    <- c("Confirmed PLE passer", "No confirmed PLE match")

PAL_UNI <- c(
  "Public"       = "#1f77b4",
  "Private"      = "#ff7f0e",
  "Foreign"      = "#9467bd",
  "Not Specified"= "#7f7f7f"
)
PAL_COURSE <- c(
  "Medical & Allied"             = "#d62728",
  "Natural Sciences"             = "#2ca02c",
  "Social & Behavioral Sciences" = "#ff9800",
  "Education"                    = "#17becf",
  "Engineering & Technology"     = "#8c564b",
  "Other"                        = "#7f7f7f"
)
PAL_PLE <- c(
  "Confirmed PLE passer"    = "#2e7d32",
  "No confirmed PLE match"  = "#c62828"
)
PAL_BIN <- c(
  B1 = "#8B0000", B2 = "#B22222", B3 = "#D9534F",
  B4 = "#F0AD4E", B5 = "#FFD166", B6 = "#A0D468",
  B7 = "#66C2A5", B8 = "#41B6C4", B9 = "#2C7FB8", B10 = "#253494"
)

NUMERIC_COLS <- c(
  "Year","NMS_PER_num","NMS_GPS","NMS_APT","NMS_SA",
  "NMS_VCss","NMS_IRss","NMS_Qss","NMS_PAss",
  "NMS_BIOss","NMS_PHYss","NMS_SSCss","NMS_CHEMss",
  "TotalRawScoreTRUE","PartIRawScoreTRUE","PartIIRawScoreTRUE",
  "Raw_Verbal","Raw_InductiveReasoning","Raw_Quantitative","Raw_PerceptualAcuity",
  "Raw_Biology","Raw_Physics","Raw_SocialScience","Raw_Chemistry",
  "PLE_YEAR_PASSED","PLE_YEAR_GAP","PLE_MATCH_CONFIDENCE"
)

SUBTEST_STD <- c(
  Verbal       = "NMS_VCss",
  Inductive    = "NMS_IRss",
  Quantitative = "NMS_Qss",
  Perceptual   = "NMS_PAss",
  Biology      = "NMS_BIOss",
  Physics      = "NMS_PHYss",
  Social       = "NMS_SSCss",
  Chemistry    = "NMS_CHEMss"
)
SUBTEST_RAW <- c(
  Verbal       = "Raw_Verbal",
  Inductive    = "Raw_InductiveReasoning",
  Quantitative = "Raw_Quantitative",
  Perceptual   = "Raw_PerceptualAcuity",
  Biology      = "Raw_Biology",
  Physics      = "Raw_Physics",
  Social       = "Raw_SocialScience",
  Chemistry    = "Raw_Chemistry"
)

# ── 3. DATA LOADING ───────────────────────────────────────────
find_parquet <- function() {
  candidates <- c(
    "../../dataset/NMAT_Exodus.parquet",
    "../../dataset/NMAT_Ultima.parquet",
    "../dataset/NMAT_Ultima.parquet",
    "dataset/NMAT_Ultima.parquet",
    "NMAT_Ultima.parquet"
  )
  for (p in candidates) if (file.exists(p)) return(p)
  stop("Cannot find NMAT_Ultima.parquet or NMAT_Exodus.parquet — check working directory.")
}

load_and_prep <- function() {
  df <- arrow::read_parquet(find_parquet())

  for (col in intersect(NUMERIC_COLS, names(df)))
    df[[col]] <- suppressWarnings(as.numeric(df[[col]]))

  df$Year <- as.integer(df$Year)

  for (flag in c("IS_BEST_NMAT_RECORD","IS_PLE_ANALYSIS_SAFE",
                 "IS_PLE_PASSER","HasTRUErawScores","AllRawComponentsPresent")) {
    if (flag %in% names(df))
      df[[flag]] <- as.logical(df[[flag]])
  }

  if ("UNI_TYPE"    %in% names(df)) df$UNI_TYPE    <- ifelse(is.na(df$UNI_TYPE), "Not Specified", df$UNI_TYPE)
  if ("UNI_LOCATION"%in% names(df)) df$UNI_LOCATION<- ifelse(is.na(df$UNI_LOCATION), "Unknown", df$UNI_LOCATION)
  if ("CourseGroup" %in% names(df)) df$CourseGroup  <- ifelse(is.na(df$CourseGroup),  "Unknown",      df$CourseGroup)

  BIN_ORDER <- paste0("B", 1:10)
  # Back-compat: rename old column if present
  if ("PercentileDecile" %in% colnames(df) && !("PercentileBin" %in% colnames(df))) {
    df <- df %>% rename(PercentileBin = PercentileDecile)
  }
  if (!("PercentileBin" %in% colnames(df))) {
    df$PercentileBin <- cut(
      suppressWarnings(as.numeric(df$NMS_PER_num)),
      breaks = c(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 101),
      labels = BIN_ORDER,
      right = FALSE,
      include.lowest = TRUE
    )
  }
  df$PercentileBin <- factor(df$PercentileBin, levels = BIN_ORDER, ordered = TRUE)

  if (!"SEX_CLEAN" %in% names(df)) {
    src <- if ("SEX" %in% names(df)) "SEX" else if ("NMASex" %in% names(df)) "NMASex" else NA
    if (!is.na(src)) {
      s <- as.character(df[[src]])
      s <- ifelse(s == "1","Male", ifelse(s == "2","Female", s))
      df$SEX_CLEAN <- ifelse(s %in% c("Male","Female"), s, NA_character_)
    } else df$SEX_CLEAN <- NA_character_
  }

  if (!"IS_BOARD_OBSERVABLE_COHORT" %in% names(df))
    df$IS_BOARD_OBSERVABLE_COHORT <- !is.na(df$Year) & df$Year <= 2014
  else
    df$IS_BOARD_OBSERVABLE_COHORT <- as.logical(df$IS_BOARD_OBSERVABLE_COHORT)

  if (!"PLE_STATUS_LABEL" %in% names(df)) {
    df$PLE_STATUS_LABEL <- ifelse(
      !is.na(df$IS_PLE_ANALYSIS_SAFE) & df$IS_PLE_ANALYSIS_SAFE,
      "Confirmed PLE passer", "No confirmed PLE match")
  }
  df$PLE_STATUS_LABEL <- factor(df$PLE_STATUS_LABEL, levels = PLE_ORDER)

  df$HAS_CONFIRMED_PLE <- !is.na(df$IS_PLE_ANALYSIS_SAFE) & df$IS_PLE_ANALYSIS_SAFE
  df
}

# Load once at startup (cached in global env)
message("Loading NMAT_Exodus.parquet …")
DF_RAW <- load_and_prep()
message(sprintf("Loaded %s rows × %s cols", nrow(DF_RAW), ncol(DF_RAW)))

# Pre-build permanent subsets
DF_BEST       <- DF_RAW  %>% filter(!is.na(IS_BEST_NMAT_RECORD), IS_BEST_NMAT_RECORD)
DF_TREND      <- DF_RAW  %>% filter(!is.na(Year), Year >= 2006, Year <= 2018)
DF_BESTTREND  <- DF_BEST %>% filter(!is.na(Year), Year >= 2006, Year <= 2018)
DF_BESTOBS    <- DF_BESTTREND %>% filter(IS_BOARD_OBSERVABLE_COHORT)
DF_UNI        <- DF_BESTTREND %>% filter(UNI_TYPE %in% c("Public","Private","Foreign"))
DF_UNIOBS     <- DF_BESTOBS   %>% filter(UNI_TYPE %in% c("Public","Private","Foreign"))

# ── 4. HELPER FUNCTIONS ───────────────────────────────────────

# NULL-coalescing
`%||%` <- function(a, b) if (!is.null(a) && length(a) > 0) a else b

# Apply global sidebar filters to any base subset
apply_filters <- function(df, yrs, courses, sexes) {
  if (!is.null(yrs)     && length(yrs)     > 0) df <- df %>% filter(Year       %in% yrs)
  if (!is.null(courses) && length(courses) > 0) df <- df %>% filter(CourseGroup %in% courses)
  if (!is.null(sexes)   && length(sexes)   > 0) df <- df %>% filter(SEX_CLEAN   %in% sexes)
  df
}

# Flatten any Arrow-backed / list columns so DT can render them
sanitize_for_dt <- function(df) {
  df <- as.data.frame(df, stringsAsFactors = FALSE)
  for (col in names(df)) {
    x <- df[[col]]
    if (is.list(x)) {
      df[[col]] <- vapply(x, function(v) {
        if (is.null(v) || length(v) == 0) NA_character_
        else paste(as.character(v), collapse = "; ")
      }, character(1))
    } else if (inherits(x, c("arrow", "ArrowArray", "ChunkedArray"))) {
      df[[col]] <- as.vector(x)
    }
    if (is.factor(df[[col]])) df[[col]] <- as.character(df[[col]])
  }
  df
}

# DT table with export buttons (Copy / CSV / Excel / Print)
dt_export <- function(data, caption = NULL) {
  data <- sanitize_for_dt(data)
  datatable(data,
    caption = if (!is.null(caption))
      tags$caption(style = "font-weight:bold;font-size:13px;text-align:left", caption),
    extensions = c("Buttons","Scroller"),
    options    = list(
      dom     = "Bfrtip",
      buttons = list(
        list(extend = "copy",  text = "Copy"),
        list(extend = "csv",   text = "CSV",
             filename = gsub("[^A-Za-z0-9_]","_", caption %||% "NMAT_export")),
        list(extend = "excel", text = "Excel",
             filename = gsub("[^A-Za-z0-9_]","_", caption %||% "NMAT_export"),
             title    = caption %||% "NMAT Export"),
        list(extend = "print", text = "Print")
      ),
      scrollX    = TRUE,
      scrollY    = "320px",
      scroller   = TRUE,
      pageLength = 25
    ),
    rownames = FALSE,
    class    = "display compact stripe"
  )
}

# Yearly summary (equivalent to Python get_yearly_summary)
yearly_summary <- function(df) {
  df %>%
    filter(!is.na(Year)) %>%
    group_by(Year) %>%
    summarise(
      n            = n(),
      raw_median   = median(TotalRawScoreTRUE, na.rm = TRUE),
      raw_q25      = quantile(TotalRawScoreTRUE, .25, na.rm = TRUE),
      raw_q75      = quantile(TotalRawScoreTRUE, .75, na.rm = TRUE),
      part1_median = median(PartIRawScoreTRUE,   na.rm = TRUE),
      part2_median = median(PartIIRawScoreTRUE,  na.rm = TRUE),
      per_median   = median(NMS_PER_num,         na.rm = TRUE),
      per_q25      = quantile(NMS_PER_num, .25,  na.rm = TRUE),
      per_q75      = quantile(NMS_PER_num, .75,  na.rm = TRUE),
      .groups      = "drop"
    )
}

# Kruskal-Wallis table
kw_table <- function(df, group_col, col_map) {
  bind_rows(lapply(names(col_map), function(col) {
    if (!col %in% names(df)) return(NULL)
    sub <- df %>% filter(!is.na(.data[[col]]), !is.na(.data[[group_col]]))
    grps <- split(sub[[col]], sub[[group_col]])
    grps <- Filter(function(g) length(g) > 1, grps)
    if (length(grps) < 2) return(NULL)
    tryCatch({
      kt <- kruskal.test(grps)
      k  <- length(grps); n <- nrow(sub)
      eta2 <- max(0, (kt$statistic - k + 1) / (n - k))
      tibble(Score = col_map[[col]], H = round(kt$statistic, 3),
             p_value = ifelse(kt$p.value < .001, "<0.001", round(kt$p.value, 4)),
             eta_squared = round(eta2, 4))
    }, error = function(e) NULL)
  }))
}

# Mann-Whitney by PLE status
mw_ple <- function(df, col_map) {
  g1 <- df %>% filter(PLE_STATUS_LABEL == "Confirmed PLE passer")
  g2 <- df %>% filter(PLE_STATUS_LABEL == "No confirmed PLE match")
  bind_rows(lapply(names(col_map), function(col) {
    if (!col %in% names(df)) return(NULL)
    a <- g1[[col]][!is.na(g1[[col]])]; b <- g2[[col]][!is.na(g2[[col]])]
    if (length(a) < 5 || length(b) < 5) return(NULL)
    tryCatch({
      wt <- wilcox.test(a, b, exact = FALSE)
      W  <- as.numeric(wt$statistic)
      r  <- 1 - 2 * W / (length(a) * length(b))
      tibble(Score = col_map[[col]], U_stat = round(W, 1),
             p_value = ifelse(wt$p.value < .001, "<0.001", round(wt$p.value, 4)),
             effect_r = round(r, 4),
             Confirmed_median = round(median(a), 2),
             NoMatch_median   = round(median(b), 2))
    }, error = function(e) NULL)
  }))
}

# Pct cross-table helper
pct_cross <- function(df, row_col, col_col, col_order = NULL) {
  ct <- df %>%
    filter(!is.na(.data[[row_col]]), !is.na(.data[[col_col]])) %>%
    count(.data[[row_col]], .data[[col_col]]) %>%
    pivot_wider(names_from  = all_of(col_col),
                values_from = n, values_fill = 0L)
  if (!is.null(col_order)) {
    missing <- setdiff(col_order, names(ct))
    for (m in missing) ct[[m]] <- 0L
    keep <- c(row_col, intersect(col_order, names(ct)))
    ct   <- ct[, keep, drop = FALSE]
  }
  totals <- rowSums(ct[, -1, drop = FALSE])
  pct    <- ct
  pct[, -1] <- round(sweep(ct[, -1, drop = FALSE], 1, pmax(totals, 1), "/") * 100, 2)
  list(counts = ct, pct = pct)
}

# Sankey via plotly
make_sankey <- function(flow_df, src_col, tgt_col, value_col = "n",
                        title = "") {
  src_nodes <- unique(as.character(flow_df[[src_col]]))
  tgt_nodes <- unique(as.character(flow_df[[tgt_col]]))
  nodes     <- c(src_nodes, tgt_nodes)
  idx       <- setNames(seq_along(nodes) - 1L, nodes)

  srcs <- as.integer(idx[as.character(flow_df[[src_col]])])
  tgts <- as.integer(idx[as.character(flow_df[[tgt_col]])])
  vals <- as.numeric(flow_df[[value_col]])

  plot_ly(
    type        = "sankey",
    arrangement = "snap",
    node = list(label = nodes, pad = 16, thickness = 18,
                line = list(color = "black", width = 0.4)),
    link = list(source = srcs, target = tgts, value = vals)
  ) %>% layout(title = title, height = 520, font = list(size = 12))
}

# Subtest mean table
subtest_means <- function(df, group_col, use_std = TRUE) {
  cols <- if (use_std) SUBTEST_STD else SUBTEST_RAW
  avail <- cols[cols %in% names(df)]
  if (length(avail) == 0 || !group_col %in% names(df)) return(NULL)
  df %>%
    filter(!is.na(.data[[group_col]])) %>%
    group_by(.data[[group_col]]) %>%
    summarise(across(all_of(avail), ~ round(mean(.x, na.rm = TRUE), 2)),
              .groups = "drop") %>%
    rename_with(~ names(avail)[match(.x, avail)], all_of(avail))
}

# ── 5. UI ─────────────────────────────────────────────────────
ui <- dashboardPage(
  skin = "blue",

  dashboardHeader(title = "NMAT Dashboard 2006–2018", titleWidth = 280),

  dashboardSidebar(
    width = 280,
    sidebarMenu(
      id = "sidebar_menu",
      menuItem("🏠 Executive Summary",    tabName = "p01", icon = icon("house")),
      menuItem("🧪 Data Integrity",        tabName = "p02", icon = icon("database")),
      menuItem("📈 Trends & Stability",    tabName = "p03", icon = icon("chart-line")),
      menuItem("📊 Score Bins & Background",  tabName = "p04", icon = icon("bar-chart")),
      menuItem("🏫 University Type",       tabName = "p05", icon = icon("university")),
      menuItem("🔄 Flow & Pathways",       tabName = "p06", icon = icon("random")),
      menuItem("🎯 PLE Alignment",         tabName = "p07", icon = icon("bullseye")),
      menuItem("🔁 Repeat Takers",         tabName = "p08", icon = icon("redo")),
      menuItem("🧠 Subtests & Profiles",   tabName = "p09", icon = icon("brain")),
      menuItem("⏰ Year Gap & Gender",      tabName = "p10", icon = icon("clock")),
      menuItem("📐 Statistical Tests",     tabName = "p11", icon = icon("calculator")),
      menuItem("📋 Policy Tables & Export",tabName = "p12", icon = icon("download"))
    ),
    hr(),
    tags$div(style = "padding:0 12px",
      tags$b("Global filters"),
      pickerInput("f_year",   "Year",         choices = NULL, multiple = TRUE,
                  options = list(`actions-box` = TRUE, size = 8)),
      pickerInput("f_course", "Course group", choices = NULL, multiple = TRUE,
                  options = list(`actions-box` = TRUE, size = 8)),
      pickerInput("f_sex",    "Sex",          choices = NULL, multiple = TRUE,
                  options = list(`actions-box` = TRUE))
    )
  ),

  dashboardBody(
    tags$head(tags$style(HTML("
      .content-wrapper { background: #f4f6f9; }
      .box { border-top: 3px solid #3c8dbc; border-radius: 4px; }
      .box-header { background: #fff; }
      .small-box { border-radius: 4px; }
      .dataTables_wrapper { font-size: 13px; }
      h4.section-q { color: #1a237e; margin-top: 18px; }
      .page-intro { background:#e8f4f8; border-left:4px solid #3c8dbc; padding:12px 16px;
                    margin-bottom:18px; border-radius:2px; font-size:14px; }
      .section-header { background:#f0f4ff; border-left:3px solid #1a237e; padding:8px 14px;
                        margin:18px 0 10px 0; border-radius:2px; font-size:14px; font-weight:600;
                        color:#1a237e; }
      .chart-caption { color:#666; font-size:12px; margin:-6px 0 12px 0; padding:0 4px; }
      .method-note { background:#fff8e1; border:1px solid #ffe082; padding:8px 12px;
                     border-radius:3px; font-size:13px; margin:8px 0; }
      hr.section-break { border:none; border-top:2px solid #e0e0e0; margin:22px 0; }
    "))),

    tabItems(

      # ─── PAGE 1: Executive Summary ──────────────────────────
      tabItem("p01",
        h2("Executive Summary"),
        tags$div(class="page-intro",
          tags$b("Overview: "), "Key performance metrics, score distributions, and institutional composition
          for NMAT examinees from 2006 to 2018. All figures use the best NMAT record per person and the
          TRUE raw score where available."
        ),
        fluidRow(
          valueBoxOutput("vb_n_best",    width = 3),
          valueBoxOutput("vb_n_years",   width = 3),
          valueBoxOutput("vb_med_raw",   width = 3),
          valueBoxOutput("vb_med_pct",   width = 3)
        ),
        fluidRow(
          valueBoxOutput("vb_unique",    width = 3),
          valueBoxOutput("vb_repeat",    width = 3),
          valueBoxOutput("vb_obs",       width = 3),
          valueBoxOutput("vb_ple_share", width = 3)
        ),
        fluidRow(
          box(title = "Annual Score & Volume Profile", width = 12,
              plotlyOutput("p01_trend", height = "680px"))
        ),
        fluidRow(
          box(title = "Course-Group Composition", width = 6,
              plotlyOutput("p01_course_pie")),
          box(title = "University-Type Composition", width = 6,
              plotlyOutput("p01_uni_pie"))
        ),
        fluidRow(
          box(title = "Summary Indicators", width = 6,
              DTOutput("p01_summary_tbl"))
        )
      ),

      # ─── PAGE 2: Data Integrity ─────────────────────────────
      tabItem("p02",
        h2("Data Integrity & Cohort Checks"),
        tags$div(class="page-intro",
          tags$b("Cohort definitions: "),
          "All rows = every cleaned NMAT record. Best-record = highest percentile per person. ",
          "Observable cohort = best-record examinees with NMAT year ≤ 2014 (enough time has passed ",
          "to observe a PLE outcome). Raw-score validation checks the Part I + Part II = Total formula."
        ),
        fluidRow(
          valueBoxOutput("vb_all_rows",  width = 3),
          valueBoxOutput("vb_best_rows", width = 3),
          valueBoxOutput("vb_true_raw",  width = 3),
          valueBoxOutput("vb_obs_rows",  width = 3)
        ),
        fluidRow(
          box(title = "Analysis Cohorts", width = 6,
              DTOutput("p02_cohort_tbl")),
          box(title = "Raw-Score Validation", width = 6,
              DTOutput("p02_rawscore_tbl"))
        ),
        fluidRow(
          box(title = "UNI_TYPE Distribution", width = 4,
              DTOutput("p02_unitype_dist")),
          box(title = "Course Group Distribution", width = 4,
              DTOutput("p02_course_dist")),
          box(title = "PLE Status Distribution", width = 4,
              DTOutput("p02_ple_dist"))
        )
      ),

      # ─── PAGE 3: Trends & Stability ─────────────────────────
      tabItem("p03",
        h2("Performance Trends & Year-to-Year Stability"),
        tags$div(class="page-intro",
          tags$b("What to look for: "),
          "The four-panel trend chart shows median raw scores, part scores, percentile ranks, and ",
          "exam volume across 2006–2018. Shaded bands show the interquartile range (IQR). ",
          "The Kruskal-Wallis table tests whether score distributions differ significantly across years; ",
          "eta-squared ≥ 0.01 indicates a practically meaningful effect."
        ),
        fluidRow(
          box(title = "Annual Score Trends", width = 12, collapsible = TRUE,
              plotlyOutput("p03_trend_fig", height = "700px"))
        ),
        fluidRow(
          box(title = "Total Raw Score by Year", width = 6,
              plotlyOutput("p03_box_raw")),
          box(title = "Percentile Rank by Year", width = 6,
              plotlyOutput("p03_box_pct"))
        ),
        fluidRow(
          box(title = "Kruskal-Wallis Tests — Score Distributions Across Years",
              width = 12, status = "info",
              DTOutput("p03_kw_tbl"))
        )
      ),

      # ─── PAGE 4: Score Bins & Background ────────────────────
      tabItem("p04",
        h2("Score Bin Distribution by Year and Background"),
        tabBox(width = 12,
          tabPanel("By Year",
            plotlyOutput("p04_heatmap_year"),
            tags$p(class="chart-caption", "Each cell shows the percentage of examinees in that bin for the given year. Darker = higher concentration."),
            hr(class="section-break"),
            DTOutput("p04_count_year"),
            tags$p(class="chart-caption", "Raw count of best-record examinees per bin per year."),
            hr(class="section-break"),
            plotlyOutput("p04_stacked_year"),
            tags$p(class="chart-caption", "Stacked bars: bin composition (%) by exam year."),
            hr(class="section-break"),
            plotlyOutput("p04_topbottom_year"),
            tags$p(class="chart-caption", "Trend lines: share of examinees in the top-scoring (B8–B10) vs bottom-scoring (B1–B3) bins over time.")
          ),
          tabPanel("By University Type",
            plotlyOutput("p04_heatmap_uni"),
            tags$p(class="chart-caption",
              "Row percentages: each cell shows the % of examinees from that university type in each bin."),
            hr(class="section-break"),
            plotlyOutput("p04_top_uni"),
            tags$p(class="chart-caption",
              "Share of examinees from each university type that scored in the top bins (B8–B10)."),
            hr(class="section-break"),
            DTOutput("p04_chi_summary"),
            tags$p(class="chart-caption",
              "Chi-square test for independence between university type and percentile bin. Cramér's V measures effect size (0 = no association, 1 = perfect)."),
            hr(class="section-break"),
            tags$div(class="section-header", "Bin distribution by year, faceted by university type"),
            tags$p(style="color:#555;font-size:13px;margin-bottom:8px;",
              "Each panel shows one university type. Bars are stacked by percentile bin. Use this to track how the bin composition of each sector evolved across exam years."),
            plotlyOutput("p04_yr_uni_bin_facet", height="540px"),
            hr(class="section-break"),
            tags$div(class="section-header", "Record-level listings by university type"),
            tags$p(style="color:#555;font-size:13px;margin-bottom:8px;",
              "All best-record examinees (2006–2018) for each university type, sorted by year (newest first) then percentile rank (highest first). Use the search box to look up specific institutions."),
            tabBox(width = 12, id = "p04_rec_tabs",
              tabPanel("Foreign",  DTOutput("p04_rec_foreign")),
              tabPanel("Public",   DTOutput("p04_rec_public")),
              tabPanel("Private",  DTOutput("p04_rec_private"))
            ),
            hr(class="section-break"),
            tags$div(class="section-header", "No-PLE-match listings by university type"),
            tags$div(class="method-note",
              tags$b("Observable cohort only (NMAT year ≤ 2014): "),
              "Examinees who sat the NMAT in 2014 or earlier but have no confirmed PLE match. ",
              "This cohort has had sufficient time to attempt the boards; the absence of a match is ",
              "analytically meaningful rather than a data lag."
            ),
            tabBox(width = 12, id = "p04_nople_tabs",
              tabPanel("Foreign",  DTOutput("p04_nople_foreign")),
              tabPanel("Public",   DTOutput("p04_nople_public")),
              tabPanel("Private",  DTOutput("p04_nople_private"))
            ),
            hr(class="section-break"),
            tags$div(class="section-header", "Citizenship profile — no-PLE-match examinees"),
            tags$p(style="color:#555;font-size:13px;margin-bottom:8px;",
              "Links no-PLE-match records to a profiling file via APPNOCLEAN. Citizenship is an inferred nationality label derived from name patterns and registration data. The metrics below describe NMAT performance by inferred citizenship group."),
            uiOutput("p04_pseudo_ui")
          ),
          tabPanel("By Course Group",
            plotlyOutput("p04_heatmap_course"),
            tags$p(class="chart-caption", "Row percentages by course group and percentile bin."),
            hr(class="section-break"),
            plotlyOutput("p04_top_course"),
            tags$p(class="chart-caption", "Top-bin (B8–B10) share for each pre-medical course background."),
            hr(class="section-break"),
            DTOutput("p04_course_pct_tbl"),
            tags$p(class="chart-caption", "Full bin percentage table by course group.")
          )
        )
      ),

      # ─── PAGE 5: University Type Analysis ───────────────────
      tabItem("p05",
        h2("Institutional Profile: University Type & Location"),
        tags$div(class="page-intro",
          tags$b("What to look for: "),
          "How NMAT performance varies by institutional type (Public, Private, Foreign) and location. ",
          "The heatmap shows bin distributions across institution × location combinations. ",
          "The foreign examinee summary highlights a distinct performance profile compared to domestic students."
        ),
        fluidRow(
          box(title = "Institution Type × Location Mix", width = 6,
              DTOutput("p05_type_loc")),
          box(title = "Counts Matrix", width = 6,
              DTOutput("p05_matrix"))
        ),
        fluidRow(
          box(title = "Bin Distribution by Institution × Location",
              width = 12, plotlyOutput("p05_inst_heatmap"))
        ),
        fluidRow(
          box(title = "Top-Bin (B8–B10) Share", width = 6,
              plotlyOutput("p05_top_bin_bar")),
          box(title = "Bin Composition by University Type", width = 6,
              plotlyOutput("p05_stacked_bin"))
        ),
        fluidRow(
          box(title = "Foreign Examinee Summary", width = 4,
              valueBoxOutput("vb_foreign_n",   width = 12),
              valueBoxOutput("vb_foreign_pct", width = 12),
              valueBoxOutput("vb_foreign_med", width = 12),
              valueBoxOutput("vb_foreign_top", width = 12)),
          box(title = "Medical & Allied vs Other — by University Type", width = 8,
              plotlyOutput("p05_med_other"))
        ),
        fluidRow(
          box(title = "University Listings (by type)", width = 12,
              tabBox(width = 12,
                tabPanel("Public",  DTOutput("p05_tbl_public")),
                tabPanel("Private", DTOutput("p05_tbl_private")),
                tabPanel("Foreign", DTOutput("p05_tbl_foreign"))
              ))
        )
      ),

      # ─── PAGE 6: Flow & Pathways ────────────────────────────
      tabItem("p06",
        h2("Pathways: Background → NMAT Outcome"),
        tags$div(class="page-intro",
          tags$b("Sankey diagrams — reading guide: "),
          "Each flow shows how examinees move from a background category (left) to a NMAT outcome bin (right). ",
          "Node width is proportional to the count. Hover over a link to see the exact count. ",
          "The 'Bin → PLE' tab uses the observable cohort only (NMAT ≤ 2014)."
        ),
        tabBox(width = 12,
          tabPanel("University → Bin",
            plotlyOutput("p06_sankey_uni", height = "520px"),
            DTOutput("p06_flow_uni_tbl")),
          tabPanel("Course → Bin",
            plotlyOutput("p06_sankey_course", height = "520px"),
            DTOutput("p06_flow_course_tbl")),
          tabPanel("Bin → PLE",
            plotlyOutput("p06_sankey_ple", height = "520px"),
            DTOutput("p06_flow_ple_tbl")),
          tabPanel("Top Pathways",
            fluidRow(
              box(width = 6, DTOutput("p06_top_uni_tbl")),
              box(width = 6, DTOutput("p06_top_course_tbl"))
            ))
        )
      ),

      # ─── PAGE 7: PLE Alignment ──────────────────────────────
      tabItem("p07",
        h2("PLE Alignment of NMAT Performance"),
        tags$div(class="alert alert-info",
          "Restricted to the observable best-record cohort (NMAT year ≤ 2014) to avoid
           misclassifying later cohorts as non-passers before their licensure window."),
        tags$div(class="method-note",
          tags$b("Score profile tab: "), "Median and quartile scores split by PLE status. Mann-Whitney U tests each score dimension; effect size r ≥ 0.1 is small, ≥ 0.3 medium, ≥ 0.5 large. ",
          tags$b("Bin profile tab: "), "Bar chart shows confirmed PLE pass rate per bin — the red dashed line marks 50%. ",
          tags$b("Background Links tab: "), "Top-bin survival by course group + PLE alignment by university type."
        ),
        tabBox(width = 12,
          tabPanel("Score Profile",
            DTOutput("p07_score_profile"),
            plotlyOutput("p07_boxplot"),
            DTOutput("p07_mw_tbl")),
          tabPanel("Bin Profile",
            plotlyOutput("p07_bin_status_stacked"),
            plotlyOutput("p07_bin_pass_bar"),
            DTOutput("p07_bin_pct_tbl")),
          tabPanel("Background Links",
            DTOutput("p07_survival_tbl"),
            plotlyOutput("p07_survival_bar"),
            DTOutput("p07_uni_ple_tbl")),
          tabPanel("Policy Tables",
            DTOutput("p07_by_year"),
            DTOutput("p07_by_course"),
            DTOutput("p07_by_uni"))
        )
      ),

      # ─── PAGE 8: Repeat Takers ──────────────────────────────
      tabItem("p08",
        h2("Repeat-Taker Patterns & Score Change"),
        tags$div(class="page-intro",
          tags$b("Repeat takers: "),
          "Persons who sat the NMAT more than once. The scatter plot compares first vs last percentile — ",
          "points above the red diagonal improved; below it declined. The box plot shows the distribution ",
          "of change scores (positive = improvement, negative = decline)."
        ),
        fluidRow(
          box(title = "Attempt Count Distribution", width = 6,
              plotlyOutput("p08_attempt_bar")),
          box(title = "Attempt Count Table", width = 6,
              DTOutput("p08_attempt_tbl"))
        ),
        fluidRow(
          box(title = "Repeat-Taker Summary", width = 4,
              DTOutput("p08_repeat_summary")),
          box(title = "Change: First vs Last Attempt", width = 8,
              plotlyOutput("p08_box_change"))
        ),
        fluidRow(
          box(title = "First vs Last Percentile — Scatter", width = 12,
              plotlyOutput("p08_scatter"))
        ),
        fluidRow(
          box(title = "Repeat-Taker Detail Table", width = 12,
              DTOutput("p08_detail"))
        )
      ),

      # ─── PAGE 9: Subtests & Profiles ────────────────────────
      tabItem("p09",
        h2("Subtest Profiles by Institution and Course Background"),
        tags$div(class="page-intro",
          tags$b("What to look for: "),
          "Mean standardized subtest scores (NMS standard score scale, centered near 500) by institutional background and course group. ",
          "The heatmap uses a diverging red-blue scale: blue cells indicate above-average performance, red below-average. ",
          "The radar chart overlays multiple groups for direct visual comparison."
        ),
        tabBox(width = 12,
          tabPanel("By University Type",
            plotlyOutput("p09_heatmap_uni"),
            tags$p(class="chart-caption", "Mean standardized subtest scores by university type. Scores are on the NMS standard score scale (mean ≈ 500). Blue = above average, red = below average."),
            DTOutput("p09_std_tbl_uni"),
            DTOutput("p09_raw_tbl_uni")),
          tabPanel("By Course Group",
            plotlyOutput("p09_heatmap_course"),
            tags$p(class="chart-caption", "Mean standardized subtest scores by pre-medical course background."),
            DTOutput("p09_std_tbl_course"),
            DTOutput("p09_raw_tbl_course")),
          tabPanel("Radar Profiles",
            fluidRow(
              box(width = 6, plotlyOutput("p09_radar_uni")),
              box(width = 6, plotlyOutput("p09_radar_course"))
            ))
        )
      ),

      # ─── PAGE 10: Year Gap & Gender ─────────────────────────
      tabItem("p10",
        h2("PLE Year Gap and Gender Patterns"),
        tags$div(class="page-intro",
          tags$b("PLE Year Gap: "),
          "Number of years between NMAT exam year and the year the examinee passed the PLE (confirmed passers only). ",
          "A shorter gap may indicate stronger academic preparation. ",
          tags$b("Gender Patterns: "),
          "Score distributions and PLE alignment rates by sex (observable cohort)."
        ),
        tabBox(width = 12,
          tabPanel("PLE Year Gap",
            fluidRow(
              valueBoxOutput("vb_gap_n",   width = 3),
              valueBoxOutput("vb_gap_med", width = 3),
              valueBoxOutput("vb_gap_q25", width = 3),
              valueBoxOutput("vb_gap_q75", width = 3)
            ),
            fluidRow(
              box(width = 6, plotlyOutput("p10_gap_hist")),
              box(width = 6, plotlyOutput("p10_gap_box"))
            ),
            DTOutput("p10_gap_summary")
          ),
          tabPanel("Gender Patterns",
            fluidRow(
              box(width = 6, DTOutput("p10_sex_summary")),
              box(width = 6, plotlyOutput("p10_sex_box"))
            ),
            plotlyOutput("p10_sex_year_bar"),
            plotlyOutput("p10_sex_ple_bar"),
            DTOutput("p10_sex_ple_tbl")
          )
        )
      ),

      # ─── PAGE 11: Statistical Tests ─────────────────────────
      tabItem("p11",
        h2("Statistical Test Results"),
        tags$div(class="page-intro",
          tags$b("Statistical tests used: "),
          "Kruskal-Wallis H (non-parametric ANOVA) for year-to-year differences; Mann-Whitney U for PLE status comparisons; ",
          "Chi-square for university-type × bin independence; Dunn post-hoc for pairwise year comparisons. ",
          "Effect sizes (eta², r, Cramér's V) distinguish statistical significance from practical importance."
        ),
        tabBox(width = 12,
          tabPanel("Kruskal-Wallis (by Year)",
            tags$div(class="method-note",
              tags$b("Kruskal-Wallis H test: "),
              "A non-parametric one-way ANOVA testing whether the distribution of each score metric ",
              "differs significantly across NMAT exam years. ",
              tags$b("Eta-squared (η²): "), "effect size — 0.01 = small, 0.06 = medium, 0.14 = large."
            ),
            DTOutput("p11_kw_year")),
          tabPanel("Mann-Whitney (PLE Status)",
            tags$div(class="method-note",
              tags$b("Mann-Whitney U test: "),
              "Compares score distributions between confirmed PLE passers and the no-confirmed-match group ",
              "(observable cohort only, NMAT ≤ 2014). ",
              tags$b("Effect size r: "), "0.1 = small, 0.3 = medium, 0.5 = large."
            ),
            DTOutput("p11_mw_ple")),
          tabPanel("Chi-Square (University × Bin)",
            fluidRow(
              box(width = 6, DTOutput("p11_chi_observed")),
              box(width = 6, DTOutput("p11_chi_summary"))
            ),
            plotlyOutput("p11_chi_heatmap"),
            DTOutput("p11_chi_expected")),
          tabPanel("Post-Hoc Dunn (by Year)",
            uiOutput("p11_dunn_ui"))
        )
      ),

      # ─── PAGE 12: Policy Tables & Export ────────────────────
      tabItem("p12",
        h2("Policy Tables & Downloads"),
        tags$div(class="page-intro",
          tags$b("Policy tables: "),
          "These tables summarise PLE board exam alignment rates by year, course group, and university type ",
          "for the observable cohort (NMAT ≤ 2014). Use the download buttons to export individual tables as CSV, ",
          "or download all four as a single Excel workbook."
        ),
        fluidRow(
          box(title = "Confirmed PLE Alignment by NMAT Year", width = 12,
              DTOutput("p12_by_year"))
        ),
        fluidRow(
          box(title = "Confirmed PLE Alignment by Pre-Med Background", width = 12,
              DTOutput("p12_by_course"))
        ),
        fluidRow(
          box(title = "Confirmed PLE Alignment by University Type", width = 12,
              DTOutput("p12_by_uni"))
        ),
        fluidRow(
          box(title = "Top-Bin Survival by Course Group", width = 6,
              DTOutput("p12_survival")),
          box(title = "Download Full Pack", width = 6,
              br(),
              downloadButton("dl_year",     "Year Table (CSV)"),     br(), br(),
              downloadButton("dl_course",   "Course Table (CSV)"),   br(), br(),
              downloadButton("dl_uni",      "Uni Type Table (CSV)"), br(), br(),
              downloadButton("dl_survival", "Survival Table (CSV)"), br(), br(),
              tags$hr(),
              tags$p(tags$b("All four tables in one Excel workbook:")),
              downloadButton("dl_excel_pack", "Download Excel Pack (.xlsx)",
                             class = "btn-success"))
        )
      )
    )
  )
)

# ── 6. SERVER ─────────────────────────────────────────────────
server <- function(input, output, session) {

  # ── Populate filter choices from data ─────────────────────
  observe({
    yrs  <- sort(unique(na.omit(DF_BESTTREND$Year)))
    crs  <- sort(unique(na.omit(DF_BESTTREND$CourseGroup)))
    sexs <- sort(unique(na.omit(DF_BESTTREND$SEX_CLEAN)))
    updatePickerInput(session, "f_year",   choices = yrs,  selected = yrs)
    updatePickerInput(session, "f_course", choices = crs,  selected = crs)
    updatePickerInput(session, "f_sex",    choices = sexs, selected = sexs)
  })

  # ── Reactive filtered subsets ──────────────────────────────
  F_besttrend <- reactive({
    apply_filters(DF_BESTTREND, input$f_year, input$f_course, input$f_sex)
  })
  F_bestobs <- reactive({
    apply_filters(DF_BESTOBS, input$f_year, input$f_course, input$f_sex)
  })
  F_uni <- reactive({
    apply_filters(DF_UNI, input$f_year, input$f_course, input$f_sex)
  })
  F_uniobs <- reactive({
    apply_filters(DF_UNIOBS, input$f_year, input$f_course, input$f_sex)
  })
  F_trend <- reactive({
    apply_filters(DF_TREND, input$f_year, input$f_course, input$f_sex)
  })

  # ══════════════════════════════════════════════════════════
  # PAGE 1 — Executive Summary
  # ══════════════════════════════════════════════════════════
  output$vb_n_best    <- renderValueBox(valueBox(
    format(nrow(F_besttrend()), big.mark = ","), "Best-record examinees", icon("users"), "blue"))
  output$vb_n_years   <- renderValueBox(valueBox(
    n_distinct(F_besttrend()$Year), "Years covered", icon("calendar"), "blue"))
  output$vb_med_raw   <- renderValueBox(valueBox(
    round(median(F_besttrend()$TotalRawScoreTRUE, na.rm = TRUE), 1),
    "Median TRUE raw score", icon("star"), "green"))
  output$vb_med_pct   <- renderValueBox(valueBox(
    round(median(F_besttrend()$NMS_PER_num, na.rm = TRUE), 1),
    "Median percentile rank", icon("percent"), "green"))
  output$vb_unique    <- renderValueBox(valueBox(
    format(n_distinct(F_besttrend()$PERSON_KEY), big.mark = ","),
    "Unique examinees", icon("id-card"), "light-blue"))
  output$vb_repeat    <- renderValueBox(valueBox({
    ct <- F_trend() %>% group_by(PERSON_KEY) %>% summarise(n = n_distinct(APPNO_CLEAN))
    format(sum(ct$n > 1), big.mark = ",")
  }, "Repeat takers", icon("redo"), "light-blue"))
  output$vb_obs       <- renderValueBox(valueBox(
    format(nrow(F_bestobs()), big.mark = ","),
    "Observable cohort", icon("eye"), "yellow"))
  output$vb_ple_share <- renderValueBox(valueBox(
    paste0(round(mean(F_bestobs()$HAS_CONFIRMED_PLE, na.rm = TRUE) * 100, 2), "%"),
    "Confirmed PLE share (observable)", icon("check-circle"), "yellow"))

  output$p01_trend <- renderPlotly({
    s <- yearly_summary(F_besttrend())
    fig <- subplot(
      plot_ly(s, x = ~Year) %>%
        add_ribbons(ymin = ~raw_q25, ymax = ~raw_q75,
                    fillcolor = "rgba(31,119,180,.25)", line = list(color = "lightblue"),
                    name = "IQR raw", showlegend = FALSE) %>%
        add_lines(y = ~raw_median, name = "Median raw",
                  line = list(color = "#1f77b4", width = 3)) %>%
        layout(yaxis = list(title = "Total Raw Score")),
      plot_ly(s, x = ~Year) %>%
        add_lines(y = ~part1_median, name = "Part I",
                  line = list(color = "#2ca02c", width = 3)) %>%
        add_lines(y = ~part2_median, name = "Part II",
                  line = list(color = "#ff7f0e", width = 3)) %>%
        layout(yaxis = list(title = "Part Score")),
      plot_ly(s, x = ~Year) %>%
        add_ribbons(ymin = ~per_q25, ymax = ~per_q75,
                    fillcolor = "rgba(255,127,14,.22)", line = list(color = "lightsalmon"),
                    name = "IQR pct", showlegend = FALSE) %>%
        add_lines(y = ~per_median, name = "Median pct",
                  line = list(color = "#d62728", width = 3)) %>%
        layout(yaxis = list(title = "Percentile Rank")),
      plot_ly(s, x = ~Year, y = ~n, type = "bar", name = "Examinees") %>%
        layout(yaxis = list(title = "Count")),
      nrows = 2, shareX = FALSE, titleX = TRUE
    ) %>% layout(
      height = 680,
      hovermode = "x unified",
      annotations = list(
        list(text = "Median Raw Score (±IQR)", x = 0.225, y = 1.03,
             xref = "paper", yref = "paper", showarrow = FALSE,
             font = list(size = 13, color = "#333")),
        list(text = "Part I vs Part II Raw Score", x = 0.775, y = 1.03,
             xref = "paper", yref = "paper", showarrow = FALSE,
             font = list(size = 13, color = "#333")),
        list(text = "Median Percentile (±IQR)", x = 0.225, y = 0.47,
             xref = "paper", yref = "paper", showarrow = FALSE,
             font = list(size = 13, color = "#333")),
        list(text = "Examinee Count by Year", x = 0.775, y = 0.47,
             xref = "paper", yref = "paper", showarrow = FALSE,
             font = list(size = 13, color = "#333"))
      )
    )
    fig
  })

  output$p01_course_pie <- renderPlotly({
    ct <- F_besttrend() %>% count(CourseGroup)
    plot_ly(ct, labels = ~CourseGroup, values = ~n, type = "pie",
            marker = list(colors = PAL_COURSE[ct$CourseGroup]))
  })
  output$p01_uni_pie <- renderPlotly({
    ct <- F_besttrend() %>% count(UNI_TYPE)
    plot_ly(ct, labels = ~UNI_TYPE, values = ~n, type = "pie",
            marker = list(colors = PAL_UNI[ct$UNI_TYPE]))
  })
  output$p01_summary_tbl <- renderDT({
    df <- F_besttrend()
    tbl <- tibble(
      Indicator = c("Median Total Raw Score","Median Part I Raw Score",
                    "Median Part II Raw Score","Median Percentile Rank",
                    "Top-bin share B8–B10 (%)","Bottom-bin share B1–B3 (%)"),
      Value = c(
        round(median(df$TotalRawScoreTRUE, na.rm=T), 1),
        round(median(df$PartIRawScoreTRUE, na.rm=T), 1),
        round(median(df$PartIIRawScoreTRUE, na.rm=T), 1),
        round(median(df$NMS_PER_num, na.rm=T), 1),
        round(mean(df$PercentileBin %in% c("B8","B9","B10"), na.rm=T)*100, 2),
        round(mean(df$PercentileBin %in% c("B1","B2","B3"), na.rm=T)*100, 2)
      )
    )
    dt_export(tbl, "Summary Indicators")
  })

  # ══════════════════════════════════════════════════════════
  # PAGE 2 — Data Integrity
  # ══════════════════════════════════════════════════════════
  output$vb_all_rows  <- renderValueBox(valueBox(
    format(nrow(DF_RAW),      big.mark=","), "All NMAT rows", icon("table"), "blue"))
  output$vb_best_rows <- renderValueBox(valueBox(
    format(nrow(DF_BEST),     big.mark=","), "Best-record rows", icon("filter"), "blue"))
  output$vb_true_raw  <- renderValueBox(valueBox(
    format(sum(DF_RAW$HasTRUErawScores == TRUE, na.rm=T), big.mark=","),
    "Rows with TRUE raw scores", icon("check"), "green"))
  output$vb_obs_rows  <- renderValueBox(valueBox(
    format(nrow(DF_BESTOBS), big.mark=","), "Observable best-record rows", icon("eye"), "yellow"))

  output$p02_cohort_tbl <- renderDT({
    tbl <- tibble(
      `Analytic subset` = c("All cleaned NMAT rows","Best record per person",
                            "Best-record 2006–2018","Best-record (observable, ≤2014)",
                            "Confirmed PLE-matched rows"),
      `Row count` = c(nrow(DF_RAW), nrow(DF_BEST), nrow(DF_BESTTREND),
                      nrow(DF_BESTOBS),
                      sum(DF_RAW$IS_PLE_ANALYSIS_SAFE == TRUE, na.rm=T))
    )
    dt_export(tbl, "Analysis Cohorts")
  })

  output$p02_rawscore_tbl <- renderDT({
    df  <- DF_RAW
    ok  <- complete.cases(df[, c("TotalRawScoreTRUE","PartIRawScoreTRUE","PartIIRawScoreTRUE")])
    mis <- abs(df$TotalRawScoreTRUE[ok] -
               df$PartIRawScoreTRUE[ok] -
               df$PartIIRawScoreTRUE[ok]) > 0.01
    svd <- if ("StoredVsDerivedMismatch" %in% names(df))
             sum(as.numeric(df$StoredVsDerivedMismatch) > 0, na.rm=T) else NA_integer_
    cvd <- if ("CalcVsDerivedMismatch" %in% names(df))
             sum(as.numeric(df$CalcVsDerivedMismatch) > 0, na.rm=T) else NA_integer_
    tbl <- tibble(Check = c("Complete Total+Part I+Part II rows",
                            "Formula mismatches (Total ≠ I + II)",
                            "Stored-vs-derived mismatch flag",
                            "Calc-vs-derived mismatch flag"),
                  Count = c(sum(ok), sum(mis, na.rm=T), svd, cvd))
    dt_export(tbl, "Raw-Score Validation")
  })

  output$p02_unitype_dist <- renderDT(
    dt_export(as.data.frame(table(UNI_TYPE = DF_RAW$UNI_TYPE)), "UNI_TYPE Distribution"))
  output$p02_course_dist  <- renderDT(
    dt_export(as.data.frame(table(CourseGroup = DF_RAW$CourseGroup)), "Course Group Distribution"))
  output$p02_ple_dist     <- renderDT(
    dt_export(as.data.frame(table(PLE_Status = DF_RAW$PLE_STATUS_LABEL)), "PLE Status Distribution"))

  # ══════════════════════════════════════════════════════════
  # PAGE 3 — Trends & Stability
  # ══════════════════════════════════════════════════════════
  output$p03_trend_fig <- renderPlotly({
    s   <- yearly_summary(F_besttrend())
    fig <- subplot(
      plot_ly(s, x = ~Year) %>%
        add_ribbons(ymin = ~raw_q25, ymax = ~raw_q75,
                    fillcolor = "rgba(31,119,180,.2)", line = list(color="lightblue"),
                    showlegend = FALSE) %>%
        add_lines(y = ~raw_median, line = list(color="#1f77b4",width=3), name="Median raw"),
      plot_ly(s, x = ~Year) %>%
        add_lines(y = ~part1_median, name="Part I",  line=list(color="#2ca02c",width=3)) %>%
        add_lines(y = ~part2_median, name="Part II", line=list(color="#ff7f0e",width=3)),
      plot_ly(s, x = ~Year) %>%
        add_ribbons(ymin = ~per_q25, ymax = ~per_q75,
                    fillcolor = "rgba(214,39,40,.15)", line=list(color="lightsalmon"),
                    showlegend=FALSE) %>%
        add_lines(y = ~per_median, line=list(color="#d62728",width=3), name="Median pct"),
      plot_ly(s, x = ~Year, y = ~n, type="bar", name="Examinees"),
      nrows=2, shareX=FALSE, titleX=TRUE
    ) %>% layout(
      height = 700,
      hovermode = "x unified",
      annotations = list(
        list(text = "Median Raw Score (±IQR)", x = 0.225, y = 1.03,
             xref = "paper", yref = "paper", showarrow = FALSE,
             font = list(size = 13, color = "#333")),
        list(text = "Part I vs Part II Raw Score", x = 0.775, y = 1.03,
             xref = "paper", yref = "paper", showarrow = FALSE,
             font = list(size = 13, color = "#333")),
        list(text = "Median Percentile (±IQR)", x = 0.225, y = 0.47,
             xref = "paper", yref = "paper", showarrow = FALSE,
             font = list(size = 13, color = "#333")),
        list(text = "Examinee Count by Year", x = 0.775, y = 0.47,
             xref = "paper", yref = "paper", showarrow = FALSE,
             font = list(size = 13, color = "#333"))
      )
    )
    fig
  })

  output$p03_box_raw <- renderPlotly({
    df <- F_besttrend() %>% filter(!is.na(Year), !is.na(TotalRawScoreTRUE))
    plot_ly(df, x = ~factor(Year), y = ~TotalRawScoreTRUE, type="box", boxpoints=FALSE,
            marker=list(color="#1f77b4")) %>%
      layout(title="Total Raw Score by Year", xaxis=list(title="Year"),
             yaxis=list(title="Score"))
  })
  output$p03_box_pct <- renderPlotly({
    df <- F_besttrend() %>% filter(!is.na(Year), !is.na(NMS_PER_num))
    plot_ly(df, x = ~factor(Year), y = ~NMS_PER_num, type="box", boxpoints=FALSE,
            marker=list(color="#d62728")) %>%
      layout(title="Percentile Rank by Year", xaxis=list(title="Year"),
             yaxis=list(title="Percentile"))
  })

  output$p03_kw_tbl <- renderDT(
    dt_export(kw_table(F_besttrend(), "Year",
      list(TotalRawScoreTRUE="Total Raw Score", PartIRawScoreTRUE="Part I",
           PartIIRawScoreTRUE="Part II", NMS_PER_num="Percentile Rank",
           NMS_GPS="GPS Standard Score")),
      "Kruskal-Wallis — Year"))

  # ══════════════════════════════════════════════════════════
  # PAGE 4 — Score Bins & Background
  # ══════════════════════════════════════════════════════════
  bin_heatmap <- function(df, group_col, title) {
    res <- pct_cross(df, group_col, "PercentileBin", BIN_ORDER)
    mat <- as.matrix(res$pct[, BIN_ORDER])
    rownames(mat) <- res$pct[[group_col]]
    plot_ly(z = mat, x = BIN_ORDER, y = rownames(mat), type = "heatmap",
            colorscale = "YlOrRd", text = round(mat, 1),
            texttemplate = "%{text}", showscale = TRUE) %>%
      layout(title = title, xaxis = list(title = "Bin"),
             yaxis = list(title = ""))
  }

  output$p04_heatmap_year  <- renderPlotly(bin_heatmap(F_besttrend(), "Year", "Bin % by Year"))
  output$p04_count_year    <- renderDT({
    res <- pct_cross(F_besttrend(), "Year", "PercentileBin", BIN_ORDER)
    dt_export(res$counts, "Bin Counts by Year")
  })
  output$p04_stacked_year  <- renderPlotly({
    res <- pct_cross(F_besttrend(), "Year", "PercentileBin", BIN_ORDER)
    long <- res$pct %>%
      mutate(Year = as.integer(Year)) %>%
      pivot_longer(-Year, names_to="Bin", values_to="Pct") %>%
      mutate(Bin = factor(Bin, BIN_ORDER))
    plot_ly(long, x=~Year, y=~Pct, color=~Bin, type="bar",
            colors=PAL_BIN) %>%
      layout(barmode="stack", title="Bin Composition by Year",
             yaxis=list(title="Percent"))
  })
  output$p04_topbottom_year <- renderPlotly({
    res <- pct_cross(F_besttrend(), "Year", "PercentileBin", BIN_ORDER)
    s   <- res$pct %>%
      mutate(Year   = as.integer(Year),
             top    = rowSums(select(., any_of(c("B8","B9","B10"))), na.rm = TRUE),
             bottom = rowSums(select(., any_of(c("B1","B2","B3"))), na.rm = TRUE))
    plot_ly(s, x=~Year) %>%
      add_lines(y=~top,    name="Top B8–B10",    line=list(color="#2e7d32",width=3)) %>%
      add_lines(y=~bottom, name="Bottom B1–B3",  line=list(color="#c62828",width=3)) %>%
      layout(title="Top vs Bottom Bin Share by Year",
             yaxis=list(title="Percent"))
  })

  output$p04_heatmap_uni   <- renderPlotly(bin_heatmap(F_uni(), "UNI_TYPE", "Bin % by University Type"))
  output$p04_top_uni       <- renderPlotly({
    res <- pct_cross(F_uni(), "UNI_TYPE", "PercentileBin", BIN_ORDER)
    top <- res$pct %>% mutate(Top_B8_B10 = B8 + B9 + B10) %>%
      select(UNI_TYPE, Top_B8_B10) %>% arrange(Top_B8_B10)
    plot_ly(top, y=~UNI_TYPE, x=~Top_B8_B10, type="bar", orientation="h",
            marker=list(color=PAL_UNI[top$UNI_TYPE])) %>%
      layout(title="Top Bin Share by University Type",
             xaxis=list(title="Percent in B8–B10"), yaxis=list(title=""))
  })
  output$p04_chi_summary   <- renderDT({
    df  <- F_uni() %>% filter(!is.na(UNI_TYPE), !is.na(PercentileBin))
    ct  <- table(df$UNI_TYPE, df$PercentileBin)
    tryCatch({
      ch  <- chisq.test(ct)
      n   <- sum(ct); r <- nrow(ct); c <- ncol(ct)
      V   <- sqrt(ch$statistic / (n * min(r-1, c-1)))
      tbl <- tibble(chi2 = round(ch$statistic,4),
                    p_value = ifelse(ch$p.value < .001,"<0.001", round(ch$p.value,4)),
                    df = ch$parameter, n = n, cramers_v = round(V,4))
      dt_export(tbl, "Chi-Square: University Type × Bin")
    }, error = function(e) dt_export(tibble(Error = conditionMessage(e))))
  })

  output$p04_heatmap_course <- renderPlotly(
    bin_heatmap(F_besttrend(), "CourseGroup", "Bin % by Course Group"))
  output$p04_top_course     <- renderPlotly({
    res <- pct_cross(F_besttrend(), "CourseGroup", "PercentileBin", BIN_ORDER)
    top <- res$pct %>% mutate(Top_B8_B10 = B8+B9+B10) %>%
      select(CourseGroup, Top_B8_B10) %>% arrange(Top_B8_B10)
    plot_ly(top, y=~CourseGroup, x=~Top_B8_B10, type="bar", orientation="h",
            marker=list(color=PAL_COURSE[top$CourseGroup])) %>%
      layout(title="Top Bin Share by Course Group",
             xaxis=list(title="Percent in B8–B10"))
  })
  output$p04_course_pct_tbl <- renderDT({
    res <- pct_cross(F_besttrend(), "CourseGroup", "PercentileBin", BIN_ORDER)
    dt_export(res$pct, "Bin % by Course Group")
  })

  # ── PAGE 4 PARITY: Faceted stacked bar Year × UNI_TYPE × Bin ─────────────
  output$p04_yr_uni_bin_facet <- renderPlotly({
    df <- F_uni() %>%
      filter(UNI_TYPE %in% c("Public","Private","Foreign"),
             !is.na(PercentileBin), !is.na(Year)) %>%
      count(Year, UNI_TYPE, PercentileBin) %>%
      mutate(PercentileBin = factor(PercentileBin, BIN_ORDER),
             Year = as.character(Year))
    if (nrow(df) == 0) return(plot_ly() %>% layout(title="No data available"))
    fig <- plot_ly()
    uni_types <- c("Foreign","Private","Public")
    for (i in seq_along(uni_types)) {
      sub <- df %>% filter(UNI_TYPE == uni_types[i])
      for (b in BIN_ORDER) {
        bsub <- sub %>% filter(PercentileBin == b)
        if (nrow(bsub) == 0) next
        fig <- fig %>% add_bars(
          data = bsub, x = ~Year, y = ~n,
          name = b, legendgroup = b,
          showlegend = (i == 1),
          marker = list(color = PAL_BIN[[b]]),
          xaxis = if (i == 1) "x" else paste0("x", i),
          yaxis = if (i == 1) "y" else paste0("y", i)
        )
      }
    }
    fig <- fig %>% layout(
      barmode = "stack",
      title   = "Examinees per bin by year and university type",
      grid    = list(rows = 1, columns = 3, pattern = "independent"),
      xaxis   = list(title = "Foreign", domain = c(0, 0.30)),
      xaxis2  = list(title = "Private", domain = c(0.35, 0.65)),
      xaxis3  = list(title = "Public",  domain = c(0.70, 1.00)),
      yaxis   = list(title = "Examinees"),
      yaxis2  = list(title = ""),
      yaxis3  = list(title = ""),
      height  = 520,
      annotations = list(
        list(x=0.15, y=1.05, xref="paper", yref="paper", text="Foreign",
             showarrow=FALSE, font=list(size=13)),
        list(x=0.50, y=1.05, xref="paper", yref="paper", text="Private",
             showarrow=FALSE, font=list(size=13)),
        list(x=0.85, y=1.05, xref="paper", yref="paper", text="Public",
             showarrow=FALSE, font=list(size=13))
      )
    )
    fig
  })

  # ── PAGE 4 PARITY: Record-level listings by UNI_TYPE ─────────────────────
  p04_rec_cols <- reactive({
    intersect(
      c("PERSON_KEY","APPNO_CLEAN","UNIVERSITY","UNI_LOCATION","Year","CourseGroup",
        "PercentileBin","NMS_PER_num","TotalRawScoreTRUE"),
      names(F_uni())
    )
  })
  make_rec_tbl <- function(df, utype, display_cols, caption) {
    sub <- df %>%
      filter(UNI_TYPE == utype) %>%
      arrange(desc(Year), desc(NMS_PER_num)) %>%
      select(all_of(display_cols))
    dt_export(sub, caption)
  }
  output$p04_rec_foreign <- renderDT({
    req(nrow(F_uni()) > 0)
    make_rec_tbl(F_uni(), "Foreign", p04_rec_cols(),
                 "Foreign examinee records")
  })
  output$p04_rec_public  <- renderDT({
    req(nrow(F_uni()) > 0)
    make_rec_tbl(F_uni(), "Public", p04_rec_cols(),
                 "Public university examinee records")
  })
  output$p04_rec_private <- renderDT({
    req(nrow(F_uni()) > 0)
    make_rec_tbl(F_uni(), "Private", p04_rec_cols(),
                 "Private university examinee records")
  })

  # ── PAGE 4 PARITY: No PLE match listings by UNI_TYPE ─────────────────────
  p04_nople_cols <- reactive({
    intersect(
      c("PERSON_KEY","APPNO_CLEAN","UNIVERSITY","UNI_LOCATION","Year","CourseGroup",
        "PercentileBin","NMS_PER_num","TotalRawScoreTRUE","PLE_STATUS_LABEL"),
      names(F_uniobs())
    )
  })
  make_nople_tbl <- function(df, utype, display_cols, caption) {
    sub <- df %>%
      filter(UNI_TYPE == utype,
             PLE_STATUS_LABEL == "No confirmed PLE match") %>%
      arrange(desc(Year), desc(NMS_PER_num)) %>%
      select(all_of(display_cols))
    dt_export(sub, caption)
  }
  output$p04_nople_foreign <- renderDT({
    req(nrow(F_uniobs()) > 0)
    make_nople_tbl(F_uniobs(), "Foreign", p04_nople_cols(),
                   "Foreign — No PLE match (observable cohort)")
  })
  output$p04_nople_public  <- renderDT({
    req(nrow(F_uniobs()) > 0)
    make_nople_tbl(F_uniobs(), "Public", p04_nople_cols(),
                   "Public — No PLE match (observable cohort)")
  })
  output$p04_nople_private <- renderDT({
    req(nrow(F_uniobs()) > 0)
    make_nople_tbl(F_uniobs(), "Private", p04_nople_cols(),
                   "Private — No PLE match (observable cohort)")
  })

  # ── PAGE 4 PARITY: Citizenship profile ─────────────────────────────

  pc_base_r <- reactive({
    df <- F_uniobs()
    df[!is.na(df$PLE_STATUS_LABEL) & df$PLE_STATUS_LABEL == "No confirmed PLE match" & !is.na(df$CITIZENSHIP_FINAL), ]
  })

  output$p04_pseudo_ui <- renderUI({
    
    base <- pc_base_r()
    if (is.null(base) || nrow(base) == 0) {
      return(tags$div(class="alert alert-warning",
        "No profiled no-PLE-match records match the current filters."))
    }
    tagList(
      fluidRow(
        valueBoxOutput("vb_pc_total",  width = 3),
        valueBoxOutput("vb_pc_foreign",width = 3),
        valueBoxOutput("vb_pc_filipino",width= 3),
        valueBoxOutput("vb_pc_distinct",width= 3)
      ),
      fluidRow(
        box(title="Citizenship composition",      width=6, plotlyOutput("p04_pc_pie_comp")),
        box(title="Foreigners vs Filipinos",             width=6, plotlyOutput("p04_pc_pie_fvf"))
      ),
      fluidRow(
        box(title="Top 15 citizenship groups",    width=12, plotlyOutput("p04_pc_top15_bar"))
      ),
      fluidRow(
        box(title="Bin composition by citizenship (top 15)", width=12, plotlyOutput("p04_pc_bin_stacked"))
      ),
      fluidRow(
        box(title="Top-bin share (B8–B10) by citizenship", width=6, plotlyOutput("p04_pc_topbin_bar")),
        box(title="Percentile rank by citizenship (n>=5)",  width=6, plotlyOutput("p04_pc_box_pct"))
      ),
      fluidRow(
        box(title="TRUE raw score by citizenship (n>=5)",   width=12, plotlyOutput("p04_pc_box_raw"))
      ),
      fluidRow(
        box(title="Summary by citizenship",                 width=12, DTOutput("p04_pc_summary_tbl"))
      ),
      fluidRow(
        box(title="By citizenship and university type",     width=6,  DTOutput("p04_pc_uni_tbl")),
        box(title="By citizenship and course group",        width=6,  DTOutput("p04_pc_course_tbl"))
      ),
      fluidRow(
        box(title="Year distribution by citizenship",       width=12, DTOutput("p04_pc_year_tbl"))
      ),
      fluidRow(
        box(title="Matched no-PLE-match records with citizenship", width=12, DTOutput("p04_pc_rec_tbl"))
      )
    )
  })

  output$vb_pc_total   <- renderValueBox({
    base <- pc_base_r()
    req(!is.null(base))
    valueBox(format(nrow(base), big.mark=","), "Profiled no-PLE-match records", icon("users"), "purple")
  })
  output$vb_pc_foreign <- renderValueBox({
    base <- pc_base_r()
    req(!is.null(base))
    n <- if ("FOREIGNER_STATUS" %in% names(base)) sum(base$FOREIGNER_STATUS == "Verified Foreigner", na.rm=TRUE) else 0L
    valueBox(format(n, big.mark=","), "Foreigners", icon("globe"), "purple")
  })
  output$vb_pc_filipino <- renderValueBox({
    base <- pc_base_r()
    req(!is.null(base))
    n <- sum(base$CITIZENSHIP_FINAL == "Filipino", na.rm=TRUE)
    valueBox(format(n, big.mark=","), "Filipinos", icon("flag"), "blue")
  })
  output$vb_pc_distinct <- renderValueBox({
    base <- pc_base_r()
    req(!is.null(base))
    valueBox(n_distinct(base$CITIZENSHIP_FINAL), "Distinct labels", icon("list"), "light-blue")
  })

  output$p04_pc_pie_comp <- renderPlotly({
    base <- pc_base_r(); req(!is.null(base))
    ct <- base %>% count(CITIZENSHIP_FINAL) %>% arrange(desc(n))
    plot_ly(ct, labels=~CITIZENSHIP_FINAL, values=~n, type="pie") %>%
      layout(title="Citizenship composition", showlegend=TRUE)
  })
  output$p04_pc_pie_fvf <- renderPlotly({
    base <- pc_base_r(); req(!is.null(base))
    nf <- if ("FOREIGNER_STATUS" %in% names(base)) sum(base$FOREIGNER_STATUS == "Verified Foreigner", na.rm=TRUE) else 0L
    np <- sum(base$CITIZENSHIP_FINAL == "Filipino", na.rm=TRUE)
    ct <- data.frame(group=c("Foreigner","Filipino"), n=c(nf, np))
    plot_ly(ct, labels=~group, values=~n, type="pie",
            marker=list(colors=c("#9467bd","#1f77b4"))) %>%
      layout(title="Foreigners vs Filipinos")
  })
  output$p04_pc_top15_bar <- renderPlotly({
    base <- pc_base_r(); req(!is.null(base))
    top15 <- base %>% count(CITIZENSHIP_FINAL) %>% arrange(desc(n)) %>% head(15)
    plot_ly(top15, x=~n, y=~reorder(CITIZENSHIP_FINAL, n), type="bar", orientation="h",
            marker=list(color="#9467bd"),
            text=~as.character(n), textposition="outside") %>%
      layout(title="Top 15 citizenship groups (descending)",
             xaxis=list(title="Examinees", showgrid=TRUE),
             yaxis=list(title="", autorange="reversed"),
             height=max(420, nrow(top15)*34),
             margin=list(l=150))
  })
  output$p04_pc_bin_stacked <- renderPlotly({
    base <- pc_base_r(); req(!is.null(base), "PercentileBin" %in% names(base))
    top_grps <- (base %>% count(CITIZENSHIP_FINAL) %>% arrange(desc(n)) %>% head(15))$CITIZENSHIP_FINAL
    sub <- base %>% filter(CITIZENSHIP_FINAL %in% top_grps)
    if (nrow(sub) == 0) return(plot_ly() %>% layout(title="No data"))
    res <- pct_cross(sub, "CITIZENSHIP_FINAL", "PercentileBin", BIN_ORDER)
    long <- res$pct %>% pivot_longer(-CITIZENSHIP_FINAL, names_to="Bin", values_to="Pct") %>%
      mutate(Bin = factor(Bin, BIN_ORDER))
    plot_ly(long, x=~CITIZENSHIP_FINAL, y=~Pct, color=~Bin, type="bar",
            colors=PAL_BIN) %>%
      layout(barmode="stack", title="Bin composition by citizenship",
             xaxis=list(title="Citizenship"), yaxis=list(title="Percent"), height=520)
  })
  output$p04_pc_topbin_bar <- renderPlotly({
    base <- pc_base_r(); req(!is.null(base), "PercentileBin" %in% names(base))
    td <- base %>%
      mutate(is_top = PercentileBin %in% c("B8","B9","B10")) %>%
      group_by(CITIZENSHIP_FINAL) %>%
      summarise(n=n(), top_n=sum(is_top, na.rm=TRUE), .groups="drop") %>%
      filter(n >= 3) %>%
      mutate(top_pct = round(top_n/n*100, 1)) %>%
      arrange(top_pct)
    if (nrow(td) == 0) return(plot_ly() %>% layout(title="No data"))
    plot_ly(td, x=~top_pct, y=~CITIZENSHIP_FINAL, type="bar", orientation="h",
            marker=list(color=PAL_BIN[["B10"]]),
            text=~paste0(top_pct,"%"), textposition="outside") %>%
      layout(title="Top-bin share (B8–B10)", xaxis=list(title="% in B8–B10"),
             yaxis=list(title=""), height=max(360, nrow(td)*30))
  })
  output$p04_pc_box_pct <- renderPlotly({
    base <- pc_base_r(); req(!is.null(base), "NMS_PER_num" %in% names(base))
    big <- base %>% group_by(CITIZENSHIP_FINAL) %>% filter(n() >= 5) %>% ungroup()
    if (nrow(big) == 0) return(plot_ly() %>% layout(title="No data (n<5)"))
    plot_ly(big, x=~CITIZENSHIP_FINAL, y=~NMS_PER_num, type="box", boxpoints=FALSE) %>%
      layout(title="Percentile rank by citizenship (n>=5)",
             xaxis=list(title=""), yaxis=list(title="Percentile rank"), height=430)
  })
  output$p04_pc_box_raw <- renderPlotly({
    base <- pc_base_r(); req(!is.null(base), "TotalRawScoreTRUE" %in% names(base))
    big <- base %>% group_by(CITIZENSHIP_FINAL) %>% filter(n() >= 5) %>% ungroup()
    if (nrow(big) == 0) return(plot_ly() %>% layout(title="No data (n<5)"))
    plot_ly(big, x=~CITIZENSHIP_FINAL, y=~TotalRawScoreTRUE, type="box", boxpoints=FALSE) %>%
      layout(title="TRUE raw score by citizenship (n>=5)",
             xaxis=list(title=""), yaxis=list(title="Total raw score"), height=430)
  })
  output$p04_pc_summary_tbl <- renderDT({
    base <- pc_base_r(); req(!is.null(base))
    has_bin <- "PercentileBin" %in% names(base)
    s <- base %>%
      mutate(
        is_top = if (has_bin) PercentileBin %in% c("B8","B9","B10") else FALSE,
        is_bot = if (has_bin) PercentileBin %in% c("B1","B2","B3")  else FALSE
      ) %>%
      group_by(CITIZENSHIP_FINAL) %>%
      summarise(
        n_examinees             = n(),
        median_percentile_rank  = round(median(NMS_PER_num, na.rm=TRUE), 2),
        median_true_raw_score   = round(median(TotalRawScoreTRUE, na.rm=TRUE), 2),
        top_bin_n               = as.integer(sum(is_top, na.rm=TRUE)),
        bottom_bin_n            = as.integer(sum(is_bot, na.rm=TRUE)),
        .groups="drop"
      ) %>%
      mutate(
        top_bin_pct    = round(top_bin_n    / pmax(n_examinees, 1) * 100, 2),
        bottom_bin_pct = round(bottom_bin_n / pmax(n_examinees, 1) * 100, 2)
      ) %>%
      arrange(desc(n_examinees), desc(median_percentile_rank))
    dt_export(s, "Summary by citizenship")
  })
  output$p04_pc_uni_tbl <- renderDT({
    base <- pc_base_r(); req(!is.null(base), "UNI_TYPE" %in% names(base))
    s <- base %>%
      group_by(CITIZENSHIP_FINAL, UNI_TYPE) %>%
      summarise(n=n(),
                median_percentile_rank  = round(median(NMS_PER_num, na.rm=TRUE), 2),
                median_true_raw_score   = round(median(TotalRawScoreTRUE, na.rm=TRUE), 2),
                .groups="drop")
    dt_export(s, "By citizenship and university type")
  })
  output$p04_pc_course_tbl <- renderDT({
    base <- pc_base_r(); req(!is.null(base), "CourseGroup" %in% names(base))
    s <- base %>%
      group_by(CITIZENSHIP_FINAL, CourseGroup) %>%
      summarise(n=n(),
                median_percentile_rank = round(median(NMS_PER_num, na.rm=TRUE), 2),
                median_true_raw_score  = round(median(TotalRawScoreTRUE, na.rm=TRUE), 2),
                .groups="drop")
    dt_export(s, "By citizenship and course group")
  })
  output$p04_pc_year_tbl <- renderDT({
    base <- pc_base_r(); req(!is.null(base), "Year" %in% names(base))
    s <- base %>%
      filter(!is.na(Year)) %>%
      group_by(CITIZENSHIP_FINAL, Year) %>%
      summarise(n=n(), .groups="drop") %>%
      pivot_wider(names_from=Year, values_from=n, values_fill=0L)
    dt_export(s, "Year distribution by citizenship")
  })
  output$p04_pc_rec_tbl <- renderDT({
    base <- pc_base_r(); req(!is.null(base))
    rec_cols <- intersect(
      c("CITIZENSHIP_FINAL","FOREIGNER_STATUS","name_based_assessment",
        "PERSON_KEY","APPNO_CLEAN","UNIVERSITY","UNI_LOCATION","UNI_TYPE",
        "Year","CourseGroup","PercentileBin","NMS_PER_num",
        "TotalRawScoreTRUE","PLE_STATUS_LABEL"),
      names(base)
    )
    s <- base[, rec_cols, drop=FALSE] %>%
      arrange(CITIZENSHIP_FINAL, desc(Year), desc(NMS_PER_num))
    dt_export(s, "Matched no-PLE-match records with citizenship")
  })

  # ══════════════════════════════════════════════════════════
  # PAGE 5 — University Type Analysis
  # ══════════════════════════════════════════════════════════
  output$p05_type_loc <- renderDT({
    df  <- F_uni() %>% filter(!is.na(UNI_LOCATION))
    tbl <- df %>% count(UNI_TYPE, UNI_LOCATION) %>%
      mutate(`% of total` = round(n / sum(n) * 100, 2))
    dt_export(tbl, "Institution Type × Location")
  })
  output$p05_matrix <- renderDT({
    df  <- F_uni() %>% filter(!is.na(UNI_LOCATION))
    tbl <- as.data.frame.matrix(addmargins(table(df$UNI_TYPE, df$UNI_LOCATION)))
    tbl$UNI_TYPE <- rownames(tbl); rownames(tbl) <- NULL
    dt_export(tbl, "Count Matrix")
  })
  output$p05_inst_heatmap <- renderPlotly({
    df  <- F_uni() %>% filter(!is.na(UNI_LOCATION), !is.na(PercentileBin)) %>%
      mutate(inst = paste0(UNI_TYPE," (",UNI_LOCATION,")"))
    res <- pct_cross(df, "inst", "PercentileBin", BIN_ORDER)
    mat <- as.matrix(res$pct[, BIN_ORDER])
    rownames(mat) <- res$pct$inst
    plot_ly(z=mat, x=BIN_ORDER, y=rownames(mat), type="heatmap",
            colorscale="Blues", texttemplate="%{z:.1f}") %>%
      layout(title="Bin % by Institution × Location",
             xaxis=list(title="Bin"), yaxis=list(title=""))
  })
  output$p05_top_bin_bar <- renderPlotly({
    df  <- F_uni() %>% filter(!is.na(UNI_LOCATION), !is.na(PercentileBin)) %>%
      mutate(inst = paste0(UNI_TYPE," (",UNI_LOCATION,")"))
    res <- pct_cross(df, "inst", "PercentileBin", BIN_ORDER)
    top <- res$pct %>% mutate(Top=B8+B9+B10) %>% select(inst, Top) %>% arrange(Top)
    plot_ly(top, y=~inst, x=~Top, type="bar", orientation="h") %>%
      layout(title="B8–B10 Share by Institution × Location",
             xaxis=list(title="Percent in B8–B10"))
  })
  output$p05_stacked_bin <- renderPlotly({
    res  <- pct_cross(F_uni(), "UNI_TYPE", "PercentileBin", BIN_ORDER)
    long <- res$pct %>% pivot_longer(-UNI_TYPE, names_to="Bin", values_to="Pct") %>%
      mutate(Bin=factor(Bin, BIN_ORDER))
    plot_ly(long, x=~UNI_TYPE, y=~Pct, color=~Bin, type="bar",
            colors=PAL_BIN) %>%
      layout(barmode="stack", title="Bin Composition by University Type",
             yaxis=list(title="Percent"))
  })
  foreign_df <- reactive({ F_uni() %>% filter(UNI_TYPE == "Foreign") })
  output$vb_foreign_n   <- renderValueBox(valueBox(
    format(nrow(foreign_df()), big.mark=","), "Foreign examinees", icon("globe"), "purple"))
  output$vb_foreign_pct <- renderValueBox(valueBox(
    paste0(round(nrow(foreign_df())/max(nrow(F_uni()),1)*100,2),"%"),
    "% of total", icon("percent"), "purple"))
  output$vb_foreign_med <- renderValueBox(valueBox(
    round(median(foreign_df()$NMS_PER_num, na.rm=T), 1),
    "Median percentile", icon("bar-chart"), "purple"))
  output$vb_foreign_top <- renderValueBox(valueBox(
    paste0(round(mean(foreign_df()$PercentileBin %in% c("B8","B9","B10"), na.rm=T)*100, 2),"%"),
    "Top bin %", icon("trophy"), "purple"))
  output$p05_med_other <- renderPlotly({
    df <- F_uni() %>%
      mutate(bucket = ifelse(CourseGroup == "Medical & Allied","Medical & Allied","Other Courses"))
    res <- pct_cross(df, "UNI_TYPE", "bucket")
    long <- res$pct %>% pivot_longer(-UNI_TYPE, names_to="Bucket", values_to="Pct")
    plot_ly(long, x=~UNI_TYPE, y=~Pct, color=~Bucket, type="bar",
            colors=c("Medical & Allied"="#d62728","Other Courses"="#7f7f7f")) %>%
      layout(barmode="stack", title="Medical & Allied vs Other by University Type")
  })
  make_uni_tbl <- function(type_name) {
    df <- F_uni() %>% filter(UNI_TYPE == type_name)
    if (nrow(df) == 0 || !"UNIVERSITY" %in% names(df)) return(tibble())
    df %>% group_by(UNIVERSITY, UNI_LOCATION) %>%
      summarise(Total_applicants = n(), .groups="drop") %>%
      arrange(desc(Total_applicants))
  }
  output$p05_tbl_public  <- renderDT(dt_export(make_uni_tbl("Public"),  "Public Universities"))
  output$p05_tbl_private <- renderDT(dt_export(make_uni_tbl("Private"), "Private Universities"))
  output$p05_tbl_foreign <- renderDT(dt_export(make_uni_tbl("Foreign"), "Foreign Universities"))

  # ══════════════════════════════════════════════════════════
  # PAGE 6 — Flow & Pathways
  # ══════════════════════════════════════════════════════════
  make_flow <- function(df, src, tgt, src_order=NULL, tgt_order=NULL) {
    ct <- df %>% filter(!is.na(.data[[src]]), !is.na(.data[[tgt]])) %>%
      count(.data[[src]], .data[[tgt]])
    names(ct)[1:2] <- c("source","target")
    if (!is.null(src_order)) {
      ct$source <- factor(ct$source, levels = src_order)
    }
    if (!is.null(tgt_order)) {
      ct$target <- factor(ct$target, levels = tgt_order)
    }
    ct <- ct %>% arrange(source, target)
    ct$source <- as.character(ct$source)
    ct$target <- as.character(ct$target)
    ct
  }

  output$p06_sankey_uni <- renderPlotly({
    flow <- make_flow(F_uni(), "UNI_TYPE","PercentileBin",
                      c("Public","Private","Foreign"), BIN_ORDER)
    make_sankey(flow, "source","target","n","University Type → Bin")
  })
  output$p06_flow_uni_tbl <- renderDT({
    flow <- make_flow(F_uni(), "UNI_TYPE","PercentileBin")
    dt_export(flow, "Flow: University → Bin")
  })

  output$p06_sankey_course <- renderPlotly({
    crs_order <- intersect(names(PAL_COURSE), unique(F_besttrend()$CourseGroup))
    flow <- make_flow(F_besttrend(), "CourseGroup","PercentileBin", crs_order, BIN_ORDER)
    make_sankey(flow, "source","target","n","Course Group → Bin")
  })
  output$p06_flow_course_tbl <- renderDT({
    flow <- make_flow(F_besttrend(), "CourseGroup","PercentileBin")
    dt_export(flow, "Flow: Course → Bin")
  })

  output$p06_sankey_ple <- renderPlotly({
    flow <- make_flow(F_bestobs(), "PercentileBin","PLE_STATUS_LABEL",
                      BIN_ORDER, PLE_ORDER)
    make_sankey(flow, "source","target","n","Bin → PLE Status (Observable Cohort)")
  })
  output$p06_flow_ple_tbl <- renderDT({
    flow <- make_flow(F_bestobs(), "PercentileBin","PLE_STATUS_LABEL")
    flow$pct_pass <- round(
      flow$n / ave(flow$n, flow$source, FUN=sum) * 100, 2)
    dt_export(flow, "Flow: Bin → PLE Status")
  })

  output$p06_top_uni_tbl <- renderDT({
    top <- F_uni() %>% filter(PercentileBin %in% c("B8","B9","B10")) %>%
      count(UNI_TYPE, PercentileBin) %>% arrange(desc(n)) %>% head(10)
    dt_export(top, "Top Pathways: University → B8–B10")
  })
  output$p06_top_course_tbl <- renderDT({
    top <- F_besttrend() %>% filter(PercentileBin %in% c("B8","B9","B10")) %>%
      count(CourseGroup, PercentileBin) %>% arrange(desc(n)) %>% head(10)
    dt_export(top, "Top Pathways: Course → B8–B10")
  })

  # ══════════════════════════════════════════════════════════
  # PAGE 7 — PLE Alignment
  # ══════════════════════════════════════════════════════════
  score_cols_ple <- list(
    TotalRawScoreTRUE ="Total Raw Score", PartIRawScoreTRUE="Part I",
    PartIIRawScoreTRUE="Part II", NMS_PER_num="Percentile Rank",
    NMS_GPS="GPS Standard Score", NMS_APT="Aptitude Score", NMS_SA="Special Area Score"
  )

  output$p07_score_profile <- renderDT({
    df   <- F_bestobs()
    cols <- intersect(names(score_cols_ple), names(df))
    out  <- df %>% filter(!is.na(PLE_STATUS_LABEL)) %>%
      group_by(PLE_STATUS_LABEL) %>%
      summarise(across(all_of(cols),
        list(n = ~sum(!is.na(.)), median = ~round(median(.x, na.rm=T),2),
             mean = ~round(mean(.x, na.rm=T),2),
             q25  = ~round(quantile(.x,.25,na.rm=T),2),
             q75  = ~round(quantile(.x,.75,na.rm=T),2)),
        .names = "{.col}__{.fn}"), .groups="drop")
    dt_export(out, "Score Profile by PLE Status")
  })

  output$p07_boxplot <- renderPlotly({
    df <- F_bestobs() %>% filter(!is.na(PLE_STATUS_LABEL), !is.na(TotalRawScoreTRUE))
    plot_ly(df, x=~PLE_STATUS_LABEL, y=~TotalRawScoreTRUE, type="box",
            color=~PLE_STATUS_LABEL, colors=PAL_PLE, boxpoints=FALSE) %>%
      layout(title="Total Raw Score by PLE Status", showlegend=FALSE,
             xaxis=list(title=""), yaxis=list(title="Total Raw Score"))
  })

  output$p07_mw_tbl <- renderDT({
    col_map <- list(TotalRawScoreTRUE="Total Raw Score", PartIRawScoreTRUE="Part I",
                    PartIIRawScoreTRUE="Part II", NMS_PER_num="Percentile Rank",
                    NMS_GPS="GPS Standard Score")
    dt_export(mw_ple(F_bestobs(), col_map), "Mann-Whitney: PLE Status Comparison")
  })

  output$p07_bin_status_stacked <- renderPlotly({
    res  <- pct_cross(F_bestobs(), "PLE_STATUS_LABEL", "PercentileBin", BIN_ORDER)
    long <- res$pct %>% pivot_longer(-PLE_STATUS_LABEL, names_to="Bin", values_to="Pct") %>%
      mutate(Bin = factor(Bin, BIN_ORDER))
    plot_ly(long, x=~PLE_STATUS_LABEL, y=~Pct, color=~Bin, type="bar",
            colors=PAL_BIN) %>%
      layout(barmode="stack", title="Bin Distribution by PLE Status",
             xaxis=list(title=""), yaxis=list(title="Percent"))
  })

  output$p07_bin_pass_bar <- renderPlotly({
    df  <- F_bestobs() %>% filter(!is.na(PercentileBin))
    res <- df %>% group_by(PercentileBin) %>%
      summarise(n = n(),
                passers  = sum(PLE_STATUS_LABEL == "Confirmed PLE passer", na.rm=T),
                pass_pct = round(passers/n*100, 1), .groups="drop") %>%
      mutate(PercentileBin = factor(PercentileBin, BIN_ORDER),
             color = PAL_BIN[as.character(PercentileBin)])
    plot_ly(res, x=~PercentileBin, y=~pass_pct, type="bar",
            marker=list(color=res$color),
            text=~paste0(pass_pct,"%"), textposition="outside") %>%
      layout(
        title      = "Confirmed PLE Pass Rate by NMAT Bin (Observable Cohort)",
        xaxis      = list(title = "Percentile Bin", categoryorder = "array",
                          categoryarray = BIN_ORDER),
        yaxis      = list(title = "Confirmed PLE Pass Rate (%)", range = c(0, 105)),
        showlegend = FALSE,
        shapes     = list(list(
          type = "line", x0 = -0.5, x1 = length(BIN_ORDER) - 0.5,
          y0   = 50, y1 = 50,
          xref = "x", yref = "y",
          line = list(color = "red", dash = "dash", width = 1.5)
        )),
        annotations = list(list(
          x = length(BIN_ORDER) - 0.5, y = 50,
          text = "50%", showarrow = FALSE, xanchor = "left",
          font = list(color = "red", size = 11)
        ))
      )
  })

  output$p07_bin_pct_tbl <- renderDT({
    res <- pct_cross(F_bestobs(), "PercentileBin", "PLE_STATUS_LABEL", PLE_ORDER)
    dt_export(res$pct, "PLE Status % within Each Bin")
  })

  output$p07_survival_tbl <- renderDT({
    df <- F_besttrend() %>% filter(!is.na(CourseGroup), !is.na(PercentileBin))
    s  <- df %>% group_by(CourseGroup) %>%
      summarise(total = n(), top_n = sum(PercentileBin %in% c("B8","B9","B10"), na.rm=T),
                top_pct = round(top_n/total*100, 2), .groups="drop") %>%
      arrange(desc(top_pct))
    dt_export(s, "Top-Bin Survival by Course Group")
  })
  output$p07_survival_bar <- renderPlotly({
    df <- F_besttrend() %>% filter(!is.na(CourseGroup), !is.na(PercentileBin))
    s  <- df %>% group_by(CourseGroup) %>%
      summarise(top_pct = round(mean(PercentileBin %in% c("B8","B9","B10"), na.rm=T)*100, 2),
                .groups="drop") %>% arrange(top_pct)
    plot_ly(s, y=~CourseGroup, x=~top_pct, type="bar", orientation="h",
            marker=list(color=PAL_COURSE[s$CourseGroup])) %>%
      layout(title="B8–B10 Survival by Course Group",
             xaxis=list(title="% in B8–B10"))
  })

  output$p07_uni_ple_tbl <- renderDT({
    tbl <- F_uniobs() %>% group_by(UNI_TYPE) %>%
      summarise(n_observable = n(), confirmed = sum(HAS_CONFIRMED_PLE, na.rm=T),
                no_match = n() - sum(HAS_CONFIRMED_PLE, na.rm=T),
                pct = round(mean(HAS_CONFIRMED_PLE, na.rm=T)*100, 2), .groups="drop")
    dt_export(tbl, "PLE Alignment by University Type")
  })

  make_policy_tables <- function(obs_df) {
    by_year <- obs_df %>% group_by(Year) %>%
      summarise(n = n(), confirmed = sum(HAS_CONFIRMED_PLE, na.rm=T),
                no_match = n() - confirmed,
                pct = round(confirmed/n*100, 2), .groups="drop") %>% arrange(Year)
    by_course <- obs_df %>% group_by(CourseGroup) %>%
      summarise(n = n(), confirmed = sum(HAS_CONFIRMED_PLE, na.rm=T),
                no_match = n() - confirmed,
                pct = round(confirmed/n*100, 2),
                med_pct = round(median(NMS_PER_num, na.rm=T), 2), .groups="drop") %>%
      arrange(desc(pct))
    by_uni <- obs_df %>% filter(UNI_TYPE %in% c("Public","Private","Foreign")) %>%
      group_by(UNI_TYPE) %>%
      summarise(n = n(), confirmed = sum(HAS_CONFIRMED_PLE, na.rm=T),
                no_match = n() - confirmed,
                pct = round(confirmed/n*100, 2),
                med_pct = round(median(NMS_PER_num, na.rm=T), 2), .groups="drop")
    list(by_year = by_year, by_course = by_course, by_uni = by_uni)
  }

  policy_tbls <- reactive({ make_policy_tables(F_bestobs()) })

  output$p07_by_year   <- renderDT(dt_export(policy_tbls()$by_year,   "PLE Alignment by Year"))
  output$p07_by_course <- renderDT(dt_export(policy_tbls()$by_course, "PLE Alignment by Course"))
  output$p07_by_uni    <- renderDT(dt_export(policy_tbls()$by_uni,    "PLE Alignment by University Type"))

  # ══════════════════════════════════════════════════════════
  # PAGE 8 — Repeat Takers
  # ══════════════════════════════════════════════════════════
  repeat_data <- reactive({
    df      <- F_trend()
    attempt <- df %>% group_by(PERSON_KEY) %>%
      summarise(n_attempts = n_distinct(APPNO_CLEAN), .groups="drop")
    repeats <- attempt %>% filter(n_attempts > 1) %>% pull(PERSON_KEY)
    rep_df  <- df %>% filter(PERSON_KEY %in% repeats) %>%
      arrange(PERSON_KEY, Year, APPNO_CLEAN) %>%
      group_by(PERSON_KEY) %>%
      summarise(
        first_year = first(Year), last_year = last(Year),
        first_pct  = first(NMS_PER_num), last_pct  = last(NMS_PER_num),
        first_raw  = first(TotalRawScoreTRUE), last_raw = last(TotalRawScoreTRUE),
        n_attempts = n_distinct(APPNO_CLEAN), .groups="drop") %>%
      filter(!is.na(first_pct), !is.na(last_pct)) %>%
      mutate(pct_change = last_pct - first_pct, raw_change = last_raw - first_raw)
    list(attempt = attempt, rep_df = rep_df)
  })

  output$p08_attempt_bar <- renderPlotly({
    ct <- repeat_data()$attempt %>%
      count(n_attempts) %>% mutate(pct = round(n/sum(n)*100,2))
    plot_ly(ct, x=~n_attempts, y=~n, type="bar",
            text=~paste0(pct,"%"), textposition="outside") %>%
      layout(title="NMAT Attempt Count Distribution",
             xaxis=list(title="Attempts"), yaxis=list(title="Count"))
  })
  output$p08_attempt_tbl <- renderDT({
    ct <- repeat_data()$attempt %>% count(n_attempts) %>%
      mutate(Percent = round(n/sum(n)*100,2))
    names(ct)[1:2] <- c("Attempts","Count")
    dt_export(ct, "Attempt Count Distribution")
  })

  output$p08_repeat_summary <- renderDT({
    rd  <- repeat_data()
    tbl <- tibble(
      Indicator = c("Repeat-taker persons","Analytic repeat takers",
                    "Improved percentile (%)","Improved raw score (%)",
                    "Median percentile change","Median raw score change"),
      Value = c(
        sum(rd$attempt$n_attempts > 1),
        nrow(rd$rep_df),
        round(mean(rd$rep_df$pct_change > 0, na.rm=T)*100, 2),
        round(mean(rd$rep_df$raw_change > 0, na.rm=T)*100, 2),
        round(median(rd$rep_df$pct_change, na.rm=T), 2),
        round(median(rd$rep_df$raw_change, na.rm=T), 2)
      )
    )
    dt_export(tbl, "Repeat-Taker Summary")
  })

  output$p08_box_change <- renderPlotly({
    rd   <- repeat_data()$rep_df %>%
      select(pct_change, raw_change) %>%
      pivot_longer(everything(), names_to="Measure", values_to="Change") %>%
      mutate(Measure = recode(Measure,
        pct_change="Percentile change", raw_change="Raw score change"))
    plot_ly(rd, x=~Measure, y=~Change, type="box", color=~Measure, boxpoints=FALSE) %>%
      layout(
        title      = "Change from First to Last Attempt",
        showlegend = FALSE,
        yaxis      = list(title = "Change (last – first)"),
        shapes     = list(list(
          type = "line", x0 = -0.5, x1 = 1.5,
          y0   = 0, y1 = 0,
          xref = "x", yref = "y",
          line = list(color = "red", dash = "dash", width = 1.5)
        ))
      )
  })

  output$p08_scatter <- renderPlotly({
    rd <- repeat_data()$rep_df %>% filter(!is.na(first_pct), !is.na(last_pct))
    lo <- min(rd$first_pct, rd$last_pct, na.rm=T)
    hi <- max(rd$first_pct, rd$last_pct, na.rm=T)
    plot_ly(rd, x=~first_pct, y=~last_pct, color=~n_attempts, type="scatter",
            mode="markers", marker=list(size=5, opacity=.5),
            text=~paste0("Attempts: ", n_attempts),
            hovertemplate="%{text}<br>First: %{x}<br>Last: %{y}<extra></extra>") %>%
      add_segments(
        x = lo, xend = hi, y = lo, yend = hi,
        inherit = FALSE,
        line = list(color = "red", dash = "dash", width = 1.5),
        name = "No change", showlegend = TRUE
      ) %>%
      layout(title="First vs Last Percentile — Repeat Takers",
             xaxis=list(title="First-attempt percentile"),
             yaxis=list(title="Last-attempt percentile"))
  })
  output$p08_detail <- renderDT(dt_export(repeat_data()$rep_df %>%
    arrange(desc(pct_change)), "Repeat-Taker Detail"))

  # ══════════════════════════════════════════════════════════
  # PAGE 9 — Subtests & Profiles
  # ══════════════════════════════════════════════════════════
  subtest_heatmap <- function(tbl, title) {
    if (is.null(tbl) || nrow(tbl) == 0) return(plot_ly() %>% layout(title="No data"))
    g_col   <- names(tbl)[1]
    mat_raw <- as.data.frame(tbl)[, -1, drop = FALSE]
    mat     <- matrix(
      as.numeric(as.matrix(mat_raw)),
      nrow     = nrow(tbl),
      ncol     = ncol(mat_raw),
      dimnames = list(as.character(tbl[[g_col]]), colnames(mat_raw))
    )
    plot_ly(z=mat, x=colnames(mat), y=rownames(mat), type="heatmap",
            colorscale="RdBu", reversescale=TRUE,
            texttemplate="%{z:.1f}", showscale=TRUE) %>%
      layout(title=title, xaxis=list(title="Subtest"), yaxis=list(title=""))
  }
  radar_plot <- function(tbl, title) {
    if (is.null(tbl) || nrow(tbl) == 0) return(plot_ly() %>% layout(title="No data"))
    g_col <- names(tbl)[1]
    cats  <- names(tbl)[-1]
    fig   <- plot_ly(type="scatterpolar", fill="toself")
    for (i in seq_len(nrow(tbl))) {
      vals <- as.numeric(unlist(tbl[i, -1], use.names = FALSE))
      fig  <- fig %>% add_trace(
        r = c(vals, vals[1]), theta = c(cats, cats[1]), name = tbl[[g_col]][i])
    }
    fig %>% layout(title=title,
                   polar=list(radialaxis=list(visible=TRUE, range=c(450,550))),
                   showlegend=TRUE)
  }

  output$p09_heatmap_uni    <- renderPlotly(subtest_heatmap(
    subtest_means(F_uni() %>% filter(UNI_TYPE %in% c("Public","Private","Foreign")),
                  "UNI_TYPE"), "Mean Std Subtest by University Type"))
  output$p09_std_tbl_uni    <- renderDT(dt_export(
    subtest_means(F_uni(), "UNI_TYPE"), "Std Subtest Means by University Type"))
  output$p09_raw_tbl_uni    <- renderDT(dt_export(
    subtest_means(F_uni(), "UNI_TYPE", use_std=FALSE), "Raw Subtest Means by University Type"))

  output$p09_heatmap_course <- renderPlotly(subtest_heatmap(
    subtest_means(F_besttrend(), "CourseGroup"), "Mean Std Subtest by Course Group"))
  output$p09_std_tbl_course <- renderDT(dt_export(
    subtest_means(F_besttrend(), "CourseGroup"), "Std Subtest Means by Course Group"))
  output$p09_raw_tbl_course <- renderDT(dt_export(
    subtest_means(F_besttrend(), "CourseGroup", use_std=FALSE), "Raw Subtest Means by Course Group"))

  output$p09_radar_uni    <- renderPlotly(radar_plot(
    subtest_means(F_uni() %>% filter(UNI_TYPE %in% c("Public","Private","Foreign")),
                  "UNI_TYPE"), "Radar: University Type"))
  output$p09_radar_course <- renderPlotly(radar_plot(
    subtest_means(F_besttrend(), "CourseGroup"), "Radar: Course Group"))

  # ══════════════════════════════════════════════════════════
  # PAGE 10 — Year Gap & Gender
  # ══════════════════════════════════════════════════════════
  gap_df <- reactive({
    F_bestobs() %>%
      filter(PLE_STATUS_LABEL == "Confirmed PLE passer", !is.na(PLE_YEAR_GAP))
  })

  output$vb_gap_n   <- renderValueBox(valueBox(
    format(nrow(gap_df()), big.mark=","), "Confirmed passers with gap data", icon("check"), "green"))
  output$vb_gap_med <- renderValueBox(valueBox(
    round(median(gap_df()$PLE_YEAR_GAP, na.rm=T),1), "Median year gap", icon("clock"), "green"))
  output$vb_gap_q25 <- renderValueBox(valueBox(
    round(quantile(gap_df()$PLE_YEAR_GAP,.25,na.rm=T),1), "Q1 year gap", icon("clock"), "light-blue"))
  output$vb_gap_q75 <- renderValueBox(valueBox(
    round(quantile(gap_df()$PLE_YEAR_GAP,.75,na.rm=T),1), "Q3 year gap", icon("clock"), "light-blue"))

  output$p10_gap_hist <- renderPlotly({
    plot_ly(gap_df(), x=~PLE_YEAR_GAP, type="histogram", nbinsx=20,
            marker=list(color="#1f77b4")) %>%
      layout(title="Distribution of NMAT-to-PLE Year Gap",
             xaxis=list(title="Year gap"), yaxis=list(title="Count"))
  })
  output$p10_gap_box  <- renderPlotly({
    df <- gap_df() %>% filter(!is.na(CourseGroup))
    plot_ly(df, x=~CourseGroup, y=~PLE_YEAR_GAP, type="box",
            color=~CourseGroup, colors=PAL_COURSE, boxpoints=FALSE) %>%
      layout(title="PLE Year Gap by Course Group", showlegend=FALSE)
  })
  output$p10_gap_summary <- renderDT({
    tbl <- gap_df() %>% group_by(CourseGroup) %>%
      summarise(confirmed_passers = n(),
                median_gap = round(median(PLE_YEAR_GAP, na.rm=T),1),
                q25 = round(quantile(PLE_YEAR_GAP,.25,na.rm=T),1),
                q75 = round(quantile(PLE_YEAR_GAP,.75,na.rm=T),1),
                median_pct = round(median(NMS_PER_num, na.rm=T),1), .groups="drop") %>%
      arrange(median_gap)
    dt_export(tbl, "Year-Gap Summary by Course Group")
  })

  sex_base <- reactive({ F_besttrend() %>% filter(!is.na(SEX_CLEAN)) })
  output$p10_sex_summary <- renderDT({
    tbl <- sex_base() %>% group_by(SEX_CLEAN) %>%
      summarise(n = n_distinct(PERSON_KEY),
                med_raw = round(median(TotalRawScoreTRUE,na.rm=T),1),
                med_pct = round(median(NMS_PER_num,na.rm=T),1),
                med_gps = round(median(NMS_GPS,na.rm=T),1), .groups="drop")
    dt_export(tbl, "Score Summary by Sex")
  })
  output$p10_sex_box  <- renderPlotly({
    df <- sex_base()
    plot_ly(df, x=~SEX_CLEAN, y=~NMS_PER_num, type="box",
            color=~SEX_CLEAN, colors=c(Male="#1f77b4",Female="#e377c2"),
            boxpoints=FALSE) %>%
      layout(title="Percentile Rank by Sex", showlegend=FALSE)
  })
  output$p10_sex_year_bar <- renderPlotly({
    res  <- pct_cross(sex_base(), "Year","SEX_CLEAN", c("Male","Female"))
    long <- res$pct %>% pivot_longer(-Year, names_to="Sex", values_to="Pct")
    plot_ly(long, x=~Year, y=~Pct, color=~Sex, type="bar",
            colors=c(Male="#1f77b4",Female="#e377c2")) %>%
      layout(barmode="stack", title="Sex Composition by Year", yaxis=list(title="Percent"))
  })
  output$p10_sex_ple_bar <- renderPlotly({
    obs_sex <- F_bestobs() %>% filter(!is.na(SEX_CLEAN))
    res  <- pct_cross(obs_sex, "SEX_CLEAN","PLE_STATUS_LABEL", PLE_ORDER)
    long <- res$pct %>% pivot_longer(-SEX_CLEAN, names_to="Status", values_to="Pct")
    plot_ly(long, x=~SEX_CLEAN, y=~Pct, color=~Status, type="bar", colors=PAL_PLE) %>%
      layout(barmode="stack", title="PLE Status by Sex (Observable)",
             yaxis=list(title="Percent"))
  })
  output$p10_sex_ple_tbl <- renderDT({
    obs_sex <- F_bestobs() %>% filter(!is.na(SEX_CLEAN))
    res     <- pct_cross(obs_sex, "SEX_CLEAN","PLE_STATUS_LABEL", PLE_ORDER)
    dt_export(res$pct, "PLE Status % by Sex")
  })

  # ══════════════════════════════════════════════════════════
  # PAGE 11 — Statistical Tests
  # ══════════════════════════════════════════════════════════
  score_map_full <- list(
    TotalRawScoreTRUE ="Total raw score", PartIRawScoreTRUE="Part I raw score",
    PartIIRawScoreTRUE="Part II raw score", NMS_PER_num="Percentile rank",
    NMS_GPS="GPS standard score"
  )

  output$p11_kw_year <- renderDT(
    dt_export(kw_table(F_besttrend(), "Year", score_map_full),
              "Kruskal-Wallis Across NMAT Years"))

  output$p11_mw_ple  <- renderDT(
    dt_export(mw_ple(F_bestobs(), score_map_full),
              "Mann-Whitney by PLE Status (Observable Cohort)"))

  output$p11_chi_observed <- renderDT({
    df  <- F_uni() %>% filter(!is.na(UNI_TYPE), !is.na(PercentileBin))
    ct  <- as.data.frame.matrix(table(df$UNI_TYPE, df$PercentileBin))
    for (b in setdiff(BIN_ORDER, names(ct))) ct[[b]] <- 0L
    ct$UNI_TYPE <- rownames(ct); rownames(ct) <- NULL
    avail <- intersect(BIN_ORDER, names(ct))
    dt_export(ct[, c("UNI_TYPE", avail), drop = FALSE],
              "Observed Counts: UNI_TYPE × Bin")
  })
  output$p11_chi_summary <- renderDT({
    df  <- F_uni() %>% filter(!is.na(UNI_TYPE), !is.na(PercentileBin))
    ct  <- table(df$UNI_TYPE, df$PercentileBin)
    tryCatch({
      ch  <- chisq.test(ct); n <- sum(ct)
      V   <- sqrt(ch$statistic / (n * min(nrow(ct)-1, ncol(ct)-1)))
      tbl <- tibble(chi2=round(ch$statistic,4),
                    p_value=ifelse(ch$p.value<.001,"<0.001",round(ch$p.value,4)),
                    df=ch$parameter, n=n, cramers_v=round(V,4))
      dt_export(tbl, "Chi-Square Summary")
    }, error=function(e) dt_export(tibble(Error=conditionMessage(e))))
  })
  output$p11_chi_heatmap <- renderPlotly({
    df  <- F_uni() %>% filter(!is.na(UNI_TYPE), !is.na(PercentileBin))
    ct  <- as.data.frame.matrix(table(df$UNI_TYPE, df$PercentileBin))
    for (b in setdiff(BIN_ORDER, names(ct))) ct[[b]] <- 0L
    avail <- intersect(BIN_ORDER, names(ct))
    ct_sub <- ct[, avail, drop = FALSE]
    pct <- round(sweep(ct_sub, 1, pmax(rowSums(ct_sub), 1), "/") * 100, 2)
    plot_ly(z=as.matrix(pct), x=avail, y=rownames(pct), type="heatmap",
            colorscale="YlGnBu", texttemplate="%{z:.1f}") %>%
      layout(title="University Type × Bin (Row Percentages)",
             xaxis=list(title="Bin"), yaxis=list(title=""))
  })
  output$p11_chi_expected <- renderDT({
    df  <- F_uni() %>% filter(!is.na(UNI_TYPE), !is.na(PercentileBin))
    ct  <- table(df$UNI_TYPE, df$PercentileBin)
    tryCatch({
      ch  <- chisq.test(ct)
      exp <- as.data.frame(round(ch$expected, 2))
      for (b in setdiff(BIN_ORDER, names(exp))) exp[[b]] <- NA_real_
      exp$UNI_TYPE <- rownames(exp); rownames(exp) <- NULL
      avail <- intersect(BIN_ORDER, names(exp))
      dt_export(exp[, c("UNI_TYPE", avail), drop = FALSE], "Expected Counts")
    }, error=function(e) dt_export(tibble(Error=conditionMessage(e))))
  })

  output$p11_dunn_ui <- renderUI({
    if (!HAS_DUNN) {
      return(tags$div(class="alert alert-warning",
        "Install the dunn.test package to enable post-hoc tests:  ",
        tags$code('install.packages("dunn.test")')))
    }
    tagList(
      tags$div(class="alert alert-info",
        tags$b("Dunn post-hoc test (Bonferroni adjustment)"),
        tags$br(),
        "Pairwise comparisons of percentile rank distributions across all NMAT years (2006–2018). ",
        "The table lists each year-pair, Z-statistic, and Bonferroni-adjusted p-value. ",
        "The heatmap shows the full p-value matrix — blue cells indicate significant differences (p < 0.05)."
      ),
      h4("Pairwise comparison table"),
      DTOutput("p11_dunn_tbl"),
      hr(),
      h4("P-value matrix heatmap"),
      tags$p(style="color:#555;font-size:12px;",
             "Values close to 0 (dark cells) indicate significantly different distributions between those two years."),
      plotlyOutput("p11_dunn_heat", height="500px")
    )
  })
  output$p11_dunn_tbl  <- renderDT({
    if (!HAS_DUNN) return(datatable(data.frame(Message="Install dunn.test to enable this table.")))
    df  <- F_besttrend() %>% filter(!is.na(Year), !is.na(NMS_PER_num))
    res <- tryCatch({
      invisible(capture.output(
        r <- dunn.test::dunn.test(df$NMS_PER_num, as.character(df$Year),
                                  method="bonferroni", altp=TRUE)
      ))
      r
    }, error = function(e) NULL)
    if (is.null(res)) return(datatable(data.frame(Error="Dunn test failed; check data.")))
    tbl <- tibble(
      Comparison    = res$comparisons,
      Z             = round(res$Z, 3),
      P_adjusted    = round(res$altP.adjusted, 5),
      Significant   = ifelse(res$altP.adjusted < .05, "Yes", "No")
    ) %>% arrange(P_adjusted)
    dt_export(tbl, "Dunn Post-Hoc (Bonferroni-adjusted, sorted by p-value)")
  })
  output$p11_dunn_heat <- renderPlotly({
    if (!HAS_DUNN) return(plot_ly() %>% layout(title="Install dunn.test to enable"))
    df   <- F_besttrend() %>% filter(!is.na(Year), !is.na(NMS_PER_num))
    yrs  <- sort(unique(df$Year))
    res  <- tryCatch({
      invisible(capture.output(
        r <- dunn.test::dunn.test(df$NMS_PER_num, as.character(df$Year),
                                  method="bonferroni", altp=TRUE)
      ))
      r
    }, error = function(e) NULL)
    if (is.null(res)) return(plot_ly() %>% layout(title="Dunn test failed"))
    yrs_chr <- as.character(yrs)
    mat  <- matrix(NA_real_, nrow=length(yrs_chr), ncol=length(yrs_chr),
                   dimnames=list(yrs_chr, yrs_chr))
    diag(mat) <- 1
    comps <- strsplit(trimws(res$comparisons), "\\s+-\\s+")
    for (i in seq_along(comps)) {
      a <- trimws(as.character(comps[[i]][1]))
      b <- trimws(as.character(comps[[i]][2]))
      if (a %in% rownames(mat) && b %in% colnames(mat)) {
        mat[a,b] <- res$altP.adjusted[i]
        mat[b,a] <- res$altP.adjusted[i]
      }
    }
    plot_ly(z=round(mat,4), x=colnames(mat), y=rownames(mat), type="heatmap",
            colorscale="Viridis", reversescale=TRUE, texttemplate="%{z:.3f}") %>%
      layout(title="Dunn Post-Hoc p-value Matrix (Percentile by Year)",
             xaxis=list(title="Year"), yaxis=list(title="Year"))
  })

  # ══════════════════════════════════════════════════════════
  # PAGE 12 — Policy Tables & Export
  # ══════════════════════════════════════════════════════════
  output$p12_by_year   <- renderDT(dt_export(policy_tbls()$by_year,   "PLE Alignment by Year"))
  output$p12_by_course <- renderDT(dt_export(policy_tbls()$by_course, "PLE Alignment by Course"))
  output$p12_by_uni    <- renderDT(dt_export(policy_tbls()$by_uni,    "PLE Alignment by University Type"))

  output$p12_survival  <- renderDT({
    df <- F_besttrend() %>% filter(!is.na(CourseGroup), !is.na(PercentileBin))
    s  <- df %>% group_by(CourseGroup) %>%
      summarise(total=n(), top_n=sum(PercentileBin %in% c("B8","B9","B10"), na.rm=T),
                top_pct=round(top_n/total*100,2), .groups="drop") %>% arrange(desc(top_pct))
    dt_export(s, "Top-Bin Survival by Course Group")
  })

  # Individual CSV downloads
  make_csv <- function(df) {
    tmp <- tempfile(fileext=".csv"); write.csv(df, tmp, row.names=FALSE); readBin(tmp,"raw",n=1e6)
  }
  output$dl_year     <- downloadHandler("ple_by_year.csv",
    content=function(f) write.csv(policy_tbls()$by_year,   f, row.names=FALSE))
  output$dl_course   <- downloadHandler("ple_by_course.csv",
    content=function(f) write.csv(policy_tbls()$by_course, f, row.names=FALSE))
  output$dl_uni      <- downloadHandler("ple_by_uni.csv",
    content=function(f) write.csv(policy_tbls()$by_uni,    f, row.names=FALSE))

  survival_tbl_reactive <- reactive({
    df <- F_besttrend() %>% filter(!is.na(CourseGroup), !is.na(PercentileBin))
    df %>% group_by(CourseGroup) %>%
      summarise(total=n(), top_n=sum(PercentileBin %in% c("B8","B9","B10"), na.rm=T),
                top_pct=round(top_n/total*100,2), .groups="drop") %>% arrange(desc(top_pct))
  })
  output$dl_survival <- downloadHandler("ple_survival.csv",
    content=function(f) write.csv(survival_tbl_reactive(), f, row.names=FALSE))

  # Excel workbook (all 4 sheets)
  output$dl_excel_pack <- downloadHandler(
    filename = "NMAT_Policy_Tables.xlsx",
    content  = function(file) {
      if (!requireNamespace("openxlsx", quietly=TRUE)) {
        showNotification("Install openxlsx: install.packages('openxlsx')", type="error")
        return()
      }
      pt <- policy_tbls()
      wb <- openxlsx::createWorkbook()
      openxlsx::addWorksheet(wb, "By Year");     openxlsx::writeData(wb, 1, pt$by_year)
      openxlsx::addWorksheet(wb, "By Course");   openxlsx::writeData(wb, 2, pt$by_course)
      openxlsx::addWorksheet(wb, "By UniType");  openxlsx::writeData(wb, 3, pt$by_uni)
      openxlsx::addWorksheet(wb, "Survival");    openxlsx::writeData(wb, 4, survival_tbl_reactive())
      openxlsx::saveWorkbook(wb, file, overwrite=TRUE)
    }
  )
}

# ── 7. RUN ────────────────────────────────────────────────────
shinyApp(ui = ui, server = server)
