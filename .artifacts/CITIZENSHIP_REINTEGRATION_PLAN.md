# Citizenship Reintegration Plan: Incorporating `REAL_FOREIGNERS.csv`

## 1. Context & Objective
**Current State:** 
The analytical workflow and dashboards (`dashboard.py` and `NMAT_Dashboard_v2.Rmd`) currently rely on an on-the-fly join with `pseudo_citizenship_profiling_FINAL.csv` to infer whether unmatched NMAT examinees are foreigners based on name and university profiling.

**New Asset:** 
We have acquired `REAL_FOREIGNERS.csv` containing ~32,500 ground-truth records with explicit nationalities (`NAC_NATIONALITY`) and Application Numbers (`NMA_AppNo`).

**Objective:** 
Reintegrate these ground-truth labels into the workflow seamlessly, without disrupting the existing Data Cleaning (Pipeline 1), PLE Matching (Pipeline 2), and Analysis (Pipeline 3) stages. We also need to update the dashboards to reflect accurate, verified citizenship data rather than pseudo-profiles.

---

## 2. Proposed Strategy: The 4th Pipeline
Modifying Pipelines 1, 2, or 3 could introduce regressions to the core data matching logic. The cleanest and most robust approach is to introduce a **Pipeline 4: Citizenship & Profiling Integration** (`4_Citizenship_Integration.ipynb`). 

This pipeline will act as a final data enrichment step before the dashboards consume the data.

### Advantages of this approach:
- **Separation of Concerns:** Core cleaning and PLE matching logic remains untouched.
- **Performance:** Baking citizenship directly into `NMAT_Ultima.parquet` eliminates the need for both Python and R dashboards to perform heavy left-joins on-the-fly.
- **Single Source of Truth:** Dashboards will consume a single, unified dataset that resolves conflicts between actual records and pseudo-profiles.

---

## 3. Implementation Steps

### Step 1: Create `4_Citizenship_Integration.ipynb`
This notebook will:
1. **Ingest Data:** Load `dataset/NMAT_Ultima.parquet`, `dataset/REAL_FOREIGNERS.csv`, and `dataset/pseudo_citizenship_profiling_FINAL.csv`.
2. **Clean Keys:** Standardize `NMA_AppNo` from `REAL_FOREIGNERS.csv` to match the `APPNO_CLEAN` format.
3. **Merge:** Left-join both the real foreigner data and the pseudo-citizenship data into the Ultima dataframe using `APPNO_CLEAN` (or `PERSON_KEY`).
4. **Resolve Citizenship (Hierarchy of Truth):**
   Create a definitive `CITIZENSHIP_FINAL` column based on:
   - **Priority 1 (Ground Truth):** `NAC_NATIONALITY` from `REAL_FOREIGNERS.csv` (e.g., "Indian", "American", "Korean").
   - **Priority 2 (Inferred):** `pseudo_citizenship` for cases where real data is missing but the profile strongly indicates foreign status.
   - **Priority 3 (Default):** "Filipino".
   Create a `FOREIGNER_STATUS` flag (e.g., `Verified Foreigner`, `Likely Foreigner`, `Filipino`) for high-level comparisons.
5. **Output:** Export the enriched dataset, overwriting `dataset/NMAT_Ultima.parquet` (or saving as `NMAT_Ultima_Enhanced.parquet`).

### Step 2: Refactor `dashboard.py` (Streamlit)
1. **Remove On-the-fly Joins:** Delete the code blocks that load `pseudo_citizenship_profiling_FINAL.csv` and merge it into `_uniobs_pc`.
2. **Update UI & Logic:**
   - Rename the "Pseudo-citizenship profile" section to **"Citizenship & Foreigner Profile"**.
   - Point all relevant pie charts, bar charts, and boxplots to use `CITIZENSHIP_FINAL` instead of `pseudo_citizenship`.
   - Update the "Foreigners vs Filipinos" comparative analysis to leverage `FOREIGNER_STATUS` instead of `override_applied`.
3. **Sidebar Enhancement:** (Optional) Add `CITIZENSHIP_FINAL` or `FOREIGNER_STATUS` as a global filter in the sidebar.

### Step 3: Refactor R Shiny Dashboard (`NMAT_Dashboard_v2.Rmd` & `app.R`)
1. **Remove On-the-fly Joins:** Similar to the Python dashboard, remove the `local({})` blocks that load and merge the pseudo-citizenship CSV.
2. **Update Visuals:** Map the R data visualizations to use the newly baked `CITIZENSHIP_FINAL` and `FOREIGNER_STATUS` columns from the parquet file.
3. **Update Labels:** Change all text references from "Pseudo-citizenship" to "Citizenship" or "Verified Nationality".

---

## 4. Conclusion
By treating the integration as a **Data Enrichment Pipeline (Pipeline 4)**, we ensure data integrity, simplify dashboard codebases, and drastically improve the reliability of the foreigner analysis segment. 

This plan can be executed sequentially, starting with the Jupyter notebook and ending with the dashboard refactoring.