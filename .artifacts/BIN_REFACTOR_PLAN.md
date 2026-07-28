# NMAT Pipeline & Dashboards — Decile → Bin Refactor Plan

**Author:** Opus orchestration (planning). Application steps delegated to Sonnet agents.
**Date:** 2026-06-01
**Status:** ✅ COMPLETE — all steps executed and verified 2026-06-01.

---

## 1. Goal

Replace the percentile **decile** scheme (`PercentileDecile`, labels `D1..D10`) with a percentile **bin** scheme throughout the pipeline and both dashboards.

### New bin definition (USER-SPECIFIED, authoritative)

| Label | Percentile range |
|-------|------------------|
| B1  | 0–9   |
| B2  | 10–19 |
| B3  | 20–29 |
| B4  | 30–39 |
| B5  | 40–49 |
| B6  | 50–59 |
| B7  | 60–69 |
| B8  | 70–79 |
| B9  | 80–89 |
| B10 | 90–100 (data max is 99) |

**Critical:** bins are **left-closed, right-open** `[a, a+10)` → requires `right=False`.
This DIFFERS from the old deciles which were right-closed (old D1 = `[0,10]`, D2 = `(10,20]`).
So values at exact multiples of 10 shift bucket (e.g. percentile = 10 was D1, becomes B2). This is intended.

### Decisions
- **Column rename:** `PercentileDecile` → **`PercentileBin`** (user chose the clean-schema option).
- **Terminology:** all user-facing "Decile"/"decile" text → "Bin"/"bin".
- **Top edge:** B10 = `[90, 101)` so a theoretical percentile of 100 lands in B10 (current data max = 99).
- **Sentinel:** `NMS_PER_num == -1` (and any value `< 0`) → `NaN` bin (unchanged behavior; −1 is a missing/sentinel value, 23 zeros are real).

### Canonical binning code (identical math in every language)

**Python (pandas):**
```python
import numpy as np
BIN_ORDER = [f"B{i}" for i in range(1, 11)]   # B1..B10
_BIN_EDGES = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 101]
df["PercentileBin"] = pd.cut(
    df["NMS_PER_num"],
    bins=_BIN_EDGES,
    labels=BIN_ORDER,
    right=False,          # left-closed [a, a+10)
    include_lowest=True,
)
df["PercentileBin"] = pd.Categorical(df["PercentileBin"], categories=BIN_ORDER, ordered=True)
```

**R:**
```r
BIN_ORDER <- paste0("B", 1:10)
df$PercentileBin <- cut(df$NMS_PER_num,
  breaks = c(0,10,20,30,40,50,60,70,80,90,101),
  labels = BIN_ORDER, right = FALSE, include.lowest = TRUE)
df$PercentileBin <- factor(df$PercentileBin, levels = BIN_ORDER, ordered = TRUE)
```

---

## 2. Data facts (verified against current dataset/NMAT_Ultima.parquet)

- Rows: 178,927. `NMS_PER_num` non-null: 177,652.
- `NMS_PER_num`: integer-valued, min **−1**, max **99**, no 100s, 23 zeros.
- Current `PercentileDecile` distribution (D1..D10) had 4,141 NaN (includes −1 sentinels + unparseable).
- decile-ish columns present: `NMS_PER`, `NMS_PER_num`, `PercentileDecile`, `PERSON_KEY`.

---

## 3. Pipeline topology (verified)

```
NMAT_CLEANED_DATA.csv ─┐
CEM_DATA.csv           ├─► 1_Data_Cleaning_Pipeline.ipynb ─► dataset/NMAT_FINAL.csv
UNIVS.csv              ┘     (rapidfuzz only; NO LLM/Gemini/API — deterministic)   dataset/output/NMAT_FINAL.parquet
                                   │  creates PercentileDecile @ Cell 29
                                   ▼
NMAT_FINAL.csv + PLE_DATA.csv + PLE_UNMATCHED.csv + output/PLE_STILL_UNMATCHED.csv
        └─► 2_PLE_Matching_Pipeline.ipynb (deterministic; pass-through for bin col)
                 └─► dataset/NMAT_Ultima.csv  +  dataset/NMAT_Ultima.parquet   ◄── dashboards read this
```

- **Notebook 1** is the SOLE creator of the bin/decile column (Cell 29). It is deterministic: Cell 3 config states "No Gemini, no web search, no API calls"; matching = `rapidfuzz` with `FUZZY_MATCH_MIN_SCORE=88`, `FUZZY_MATCH_MIN_GAP=5`. `DsPy_verified.csv` already exists and is reloaded (Cell 23). Re-running will NOT change non-bin columns.
- **Notebook 2** never references the bin column; `nmat_ultima = pd.concat([nmat, ple_flags_df])` carries it through verbatim. Writes to `ROOT/NMAT_Ultima.{csv,parquet}` where `ROOT = dataset/`.

---

## 4. Exact edits

### 4A. `1_Data_Cleaning_Pipeline.ipynb` (3 code cells reference it: 29, 35, 37)

**Cell 29** — change the `pd.cut` block. FROM:
```python
nmat_base["NMS_PER_num"] = to_num(nmat_base["NMS_PER"])
nmat_base["PercentileDecile"] = pd.cut(
    nmat_base["NMS_PER_num"],
    bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    labels=["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10"],
    include_lowest=True
)
```
TO:
```python
nmat_base["NMS_PER_num"] = to_num(nmat_base["NMS_PER"])
# Percentile BIN scheme: left-closed [a, a+10) -> B1=0-9, B2=10-19, ... B10=90-100
nmat_base["PercentileBin"] = pd.cut(
    nmat_base["NMS_PER_num"],
    bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 101],
    labels=["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"],
    right=False,
    include_lowest=True
)
```

**Cell 35** — in `priority_cols` list, replace `"PercentileDecile",` with `"PercentileBin",`.

**Cell 37** — rewrite QA block:
```python
qa_3 = nmat_final["PercentileBin"].value_counts(dropna=False).reset_index()
qa_3.columns = ["PercentileBin", "count"]
...
qa_3.to_csv(OUTDIR / "12_qa_bins.csv", index=False)
...
display(qa_3.sort_values("PercentileBin"))
```
(keep other qa_* lines intact)

### 4B. `2_PLE_Matching_Pipeline.ipynb`
No bin/decile references. Pass-through. No edit required for correctness, but verify it does not hard-reference the old name (it doesn't). Re-run to regenerate Ultima from the new NMAT_FINAL.

### 4C. `dashboard.py` (full mechanical transform)
- `DECILE_ORDER` → `BIN_ORDER = [f"B{i}" for i in range(1,11)]`.
- `DECILE_COLORS` dict keys `D1..D10` → `B1..B10` (rename to `BIN_COLORS`).
- `ensure_required_columns`: read/derive `PercentileBin`; fallback `pd.cut` uses `right=False`, edges `[0,...,90,101]`, labels B1..B10. If parquet has `PercentileBin`, coerce to ordered categorical; keep a back-compat shim that renames `PercentileDecile`→`PercentileBin` if only the old name is present.
- Replace every `"PercentileDecile"` column ref → `"PercentileBin"`.
- Replace top/bottom membership tests: `["D8","D9","D10"]`→`["B8","B9","B10"]`, `["D1","D2","D3"]`→`["B1","B2","B3"]`. Single-decile refs `"D1".."D10"` → `"B1".."B10"` (e.g. `["D8","D9","D10"]` sums, `pct[["D8","D9","D10"]]`, `add_segments x="D1"/xend="D10"` etc.).
- All user-facing strings "Decile"/"decile" → "Bin"/"bin" (titles, captions, axis labels, tab label "📊 Deciles & Background" → "📊 Score Bins & Background", figure/table titles).
- `chi_square_unitype_decile` and similar helpers: use `BIN_ORDER`.
- Pseudo-citizenship subsection (recently added in `dec_tab2`): every `PercentileDecile`, `D8/D9/D10`, `D1/D2/D3`, DECILE_COLORS, "decile" → bin equivalents.
- Keep all chart `key=` strings unique (existing keys may say "decile" — fine to leave as internal keys, but prefer not to break uniqueness; do NOT duplicate keys).
- Do not change cohort logic, filters, stats, or any non-bin behavior.

### 4D. `RShiny_Dashboard/NMAT_Shiny/app.R` (port to bins + full parity)
- Line 27 `DECILE_ORDER <- paste0("D",1:10)` → `BIN_ORDER <- paste0("B",1:10)`.
- Lines 48–52 `PAL_DECILE` (D1..D10 colors) → `PAL_BIN` (B1..B10), same hex ramp.
- Lines 115–120 data prep: read `PercentileBin` from parquet; fallback `cut(..., right=FALSE, breaks=c(0,...,90,101), labels=BIN_ORDER)`; back-compat rename if only `PercentileDecile` present; `factor(levels=BIN_ORDER, ordered=TRUE)`.
- Replace ALL `PercentileDecile` (~120) → `PercentileBin`; ALL `DECILE_ORDER` (~45) → `BIN_ORDER`; `PAL_DECILE` → `PAL_BIN`.
- Replace hardcoded `c("D8","D9","D10")`→`c("B8","B9","B10")`, `c("D1","D2","D3")`→`c("B1","B2","B3")`, `select(., D8,D9,D10)`/`D8+D9+D10` etc. → B equivalents, `x="D1"/xend="D10"` → B.
- All titles/labels "Decile" → "Bin"; menuItem "📊 Deciles & Background" → "📊 Score Bins & Background".
- **Parity sweep:** ensure every page/figure/table/insight present in the current `dashboard.py` exists in `app.R` — including the recently added items in the Deciles/Bins & Background page: (a) faceted stacked bar (year × UNI_TYPE × bin), (b) record-level listings by UNI_TYPE (Foreign/Public/Private), (c) "No PLE match" record listings by UNI_TYPE (observable cohort), (d) the full **Pseudo-citizenship profile for no-PLE-match examinees** subsection (loads `dataset/pseudo_citizenship_profiling_FINAL.csv`, merges on APPNO_CLEAN/APPNOCLEAN trimmed-string key, 4 metrics, 2 pies, top-15 bar, stacked bin% bar, top-bin share bar, percentile box, raw-score box, 5 tables). Use `arrow::read_parquet` for data and `readr`/`read.csv` for the CSV; gracefully `validate`/`req` when CSV missing.

---

## 5. Execution order (dependencies)
1. Snapshot current `dataset/NMAT_Ultima.parquet` stats (rows, columns, NMS_PER_num describe, decile dist) → baseline for regression.
2. Edit notebook 1 (cells 29, 35, 37).
3. Run notebook 1 (deterministic). Verify NMAT_FINAL.parquet: has `PercentileBin` (B1..B10), no `PercentileDecile`, expected bin distribution, same row count & other columns as before.
4. Run notebook 2. Verify `dataset/NMAT_Ultima.parquet`: `PercentileBin` present/B-labels, row count 178,927, column set = previous − `PercentileDecile` + `PercentileBin`, all other key distributions unchanged.
5. Refactor dashboard.py (Sonnet agent). Smoke-test: `python -c "import ast; ast.parse(open('dashboard.py',encoding='utf-8').read())"` + a headless load harness that imports load + builds subsets and checks `BIN_ORDER`/`PercentileBin`.
6. Port app.R (Sonnet agent). Verify with `Rscript -e 'parse("app.R")'` if R present; else static grep checks (no residual `PercentileDecile`/`DECILE_ORDER`/`D8","D9` outside comments).
7. Final cross-check + remove temp files (`_tmp_*.py`).

## 6. Regression guardrails
- Row counts must match exactly (178,927 in Ultima).
- Column set: only delta is `PercentileDecile`→`PercentileBin`.
- `NMS_PER_num.describe()` unchanged.
- Sum of B1..B10 counts + NaN == total; NaN count ≈ prior decile NaN (4,141) since sentinel handling unchanged.
- Spot check: percentile values exactly = 10,20,...,90 now fall in B2,B3,...,B10 (one bucket higher than the old right-closed deciles for those exact edges).

## 7. Out of scope (documented follow-ups — NOT done now)
- `3_NMAT_PLE_Analysis.ipynb` (5.6MB) references `PercentileDecile` + `DECILE_ORDER` and will need the same rename before it is next run; its `dataset/analysis_output/*decile*.csv` exports will then become bin-based. The user scoped today's work to notebooks 1 & 2, dashboard.py, and app.R only.
