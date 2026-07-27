# ============================================================
# setup.R — Run this ONCE before launching the app
# ============================================================
# Installs all required packages for the NMAT R Shiny Dashboard.
# Run from RStudio: source("setup.R") or Rscript setup.R

required <- c(
  "shiny",           # base framework
  "shinydashboard",  # sidebar + box layout
  "shinyWidgets",    # pickerInput (multi-select with actions-box)
  "arrow",           # read_parquet (reads NMAT_Ultima.parquet)
  "dplyr",           # data wrangling
  "tidyr",           # pivot_wider / pivot_longer
  "ggplot2",         # static charts (used as ggplotly base)
  "plotly",          # interactive charts + Sankey diagrams
  "DT",              # interactive tables with CSV/Excel/Print export
  "scales",          # number formatting
  "RColorBrewer",    # colour palettes
  "htmltools",       # tags$caption etc.
  "openxlsx",        # Excel workbook export (Policy Tables page)
  "dunn.test",       # Dunn post-hoc test (Page 11)
  "flexdashboard"    # Dashboard utilities
)

# Identify missing packages
missing <- required[!sapply(required, requireNamespace, quietly = TRUE)]

# Install missing packages if any
if (length(missing) == 0) {
  message("All packages already installed.")
} else {
  message("Installing: ", paste(missing, collapse = ", "))
  install.packages(missing, dependencies = TRUE)
  message("Done. You can now run: shiny::runApp()")
}
