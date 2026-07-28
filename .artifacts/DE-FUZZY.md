# Comprehensive Refactoring Plan: Eliminating Fuzzy Matching for Deterministic Lineage (DE-FUZZY.md)

## Objective
Transition the NMAT-PLE matching pipelines to a strictly deterministic architecture. All fuzzy matching logic will be eliminated and replaced by exact matching utilizing the NMA_AppNo identifier. Downstream analytical components (Pipeline 3 and the Streamlit Dashboard) will be gracefully refactored to support this binary linkage output.

---

## Phase 1: Refactoring `2_PLE_Matching_Pipeline.ipynb`
**Goal:** Remove all fuzzy matching code, parameters, and outputs. Implement a deterministic matcher using the provided `PLE_STILL_UNMATCHED.csv`.

1. **Remove Fuzzy Dependencies & Parameters (Cells 1 & 2):**
   - Remove `rapidfuzz` from the installation list (`!pip install...`) and the imports (`from rapidfuzz import process, fuzz`).
   - Delete the fuzzy configurations: `FUZZY_ACCEPT_SCORE`, `FUZZY_REVIEW_SCORE`, and `FUZZY_GAP_MIN`.
   - Add a new path variable: `PLE_STILL_UNMATCHED_PATH = ROOT / "output" / "PLE_STILL_UNMATCHED.csv"`.

2. **Load & Clean New Deterministic Source (Cell 4):**
   - Load `PLE_STILL_UNMATCHED.csv` as a new DataFrame (`ple_still_unmatched`).
   - Clean the target identifier column using the `clean_appno()` function. *(Note: The column containing the AppNo in this file may be named `MATCHED_APPNO` or `NMA_AppNo`. Target it specifically for extraction).*

3. **Delete Fuzzy Matching Logic (Cell 10):**
   - **Delete Cell 10 entirely.** This removes the `STAGE 2: Fuzzy name match` routine.

4. **Implement Deterministic NMA_AppNo Matching (New Cell 10 Replacement):**
   - Create a new stage (`STAGE 2: Deterministic AppNo Match`).
   - Filter `ple_still_unmatched` into two datasets:
     - **Has AppNo:** Records where the extracted `NMA_AppNo` is not empty. Match these directly against the `nmat_by_appno` dictionary. Assign successful hits with `MATCH_STATUS = "FINAL_MATCH"` and `MATCH_METHOD = "DETERMINISTIC_APPNO"`.
     - **Empty AppNo:** Records where the `NMA_AppNo` is blank. 
   - **Handling Empty AppNo values:** Iterate over the records with an empty AppNo. If they lack an AppNo *and* cannot be linked via `CEM_DATA` (i.e., lacking an active link in the NMAT master data), flag them explicitly. Assign `MATCH_STATUS = "UNMATCHED_NO_APPNO"` and `MATCH_REASON = "Empty NMA_AppNo and no determinable CEM data link"`.

5. **Update Aggregation & Safe Statuses (Cells 11 & 12):**
   - Modify the master match table concatenation to merge `stage0_final`, `exact_final`, and your new `deterministic_final` DataFrames.
   - Update `accepted_statuses` and `analysis_safe` variables to strictly include: `{"FINAL_MATCH", "MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"}`. Remove all `FUZZY_*` designations.

---

## Phase 2: Refactoring `3_NMAT_PLE_Analysis.ipynb`
**Goal:** Safely update downstream analysis to consume a strictly binary PLE status ("Confirmed PLE passer" vs "No confirmed PLE match"), handling the disappearance of ambiguous outputs without causing KeyError exceptions.

1. **Update Global Plot Styles (Analysis Cell 2):**
   - Remove `"Ambiguous match"` from the `PLE_ORDER` list.
   - Remove the `"Ambiguous match"` key-value pair from the `PALETTE_PLE` dictionary.

2. **Update Status Label Derivation (Analysis Cell 3):**
   - Refactor the `ple_label(row)` function to drop ambiguous logic:
     ```python
     def ple_label(row):
         if row.get("IS_PLE_ANALYSIS_SAFE") == True:
             return "Confirmed PLE passer"
         else:
             return "No confirmed PLE match"
     ```

3. **Safeguard Flow Visualizations (Analysis Cell 11D):**
   - In **Section 5C**, update `PLE_FLOW_ORDER` and `PLE_FLOW_COLORS` to exclusively contain the two binary categories. The `make_flow_table` function will automatically handle the cleaned dimensions without throwing KeyError exceptions for the missing third group.

4. **Update Policy Tables (Analysis Cell 20):**
   - Remove the calculation column `"ambiguous_matches": int((x["PLE_STATUS_LABEL"] == "Ambiguous match").sum())` from `table_year`, `table_course`, and `table_uni`.

---

## Phase 3: Refactoring `dashboard.py`
**Goal:** Eradicate fuzzy UI references, strip ambiguous status definitions, and expose the deterministic attempt histories.

1. **Global Configuration Updates:**
   - Remove `"Ambiguous match"` from `PLE_ORDER` and `PALETTE_PLE`.
   - In the `REQUIRED_PIPELINE_COLS` list, add `"PLE_MATCH_METHOD"`. This allows the dashboard to identify rows explicitly matched by `NMA_AppNo`.

2. **Refactor Helper Functions:**
   - Modify `derive_ple_status(row)` to strictly return a binary output (passer vs. no match), eliminating the `AMBIGUOUS` conditional branch.

3. **UI Text Cleanup:**
   - In the `st.expander("Read this first...")` section within the Header, delete the bullet point explaining ambiguous PLE matches.

4. **Implement AppNo Match History Feature:**
   - In the sidebar navigation, either add a new page or append to `"🔁 Repeat Takers"`.
   - Add the following component to query and display deterministic NMA_AppNo histories:
     ```python
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
     ```

## Execution Verification
After executing the modifications, run `00_RUN_ME.ipynb` to execute the whole pipeline sequentially. 
1. Check `dataset/output/PLE_MATCH_MASTER.csv` to ensure `FUZZY` methods no longer exist.
2. Verify `NMAT_Ultima.parquet` contains no ambiguous or fuzzy flags.
3. Boot the streamlit dashboard via `streamlit run dashboard.py` and inspect the "NMA_AppNo Deterministic Match Histories" table to confirm historical attempts are successfully linked.