# Auditor 10 — Documentation Verification Report

Scope: `docs/data_dictionary.md`, `docs/pipeline_architecture.md`, `docs/tree_dir.txt`, root `tree_dir.txt`, `CLAUDE.md`, `README.md`, `changelog.md`, `requirements.txt` (root + both dashboards), both dashboard `README.md`s, `00_RUN_ME.ipynb`.
Ground truth: `dataset/NMAT_Exodus.parquet` (178,927 × 54, byte-identical across all 3 copies per shared context) and actual code, verified with `./.venv/Scripts/python.exe`.
Out of scope: `reports/` (not read, per instructions).

---

## 1. Master claim-verification table

| # | Document | Location | Claim | Status | Correct value / note |
|---|----------|----------|-------|--------|----------------------|
| 1 | CLAUDE.md | L119 | Column list includes `PERSON_NAME` | **WRONG** | Column does not exist. Real name column is `NMA_College`/`PERSON_KEY` only; no name column survived slimming. |
| 2 | CLAUDE.md | L125 | Flags include `IS_BOARD_OBSERVABLE_COHORT` | **WRONG** | Column does not exist in the 54-col parquet. |
| 3 | CLAUDE.md | L127 | `PLE_MATCH_STATUS` listed as a live PLE-linking column with values `"Confirmed PLE passer"`/`"No confirmed PLE match"` | **WRONG** | Column does not exist in Exodus. It DID exist pre-slimming and was one of the 64 columns explicitly removed (`docs/pipeline_architecture.md` L438 lists it under "PLE extended" removed columns) — so CLAUDE.md contradicts the project's own removal record. |
| 4 | `docs/data_dictionary.md` | L141 | `IS_PLE_ANALYSIS_SAFE` = "Strict PLE linkage flag... True only when match is `FINAL_MATCH`, `MANUAL_APPNO_MATCH`, or `DETERMINISTIC_APPNO`" | **WRONG** | CONFIRMED: `IS_PLE_ANALYSIS_SAFE` is a byte-for-byte duplicate of `IS_PLE_PASSER` (`(df.IS_PLE_ANALYSIS_SAFE==df.IS_PLE_PASSER).all()==True`, both 49,986 True). There is no `FINAL_MATCH` value in `PLE_MATCH_METHOD` (actual values: `EXACT` 54,437 / `MANUAL_APPNO_MATCH` 2,776 / `DETERMINISTIC_APPNO` 91 / null 121,623). Non-null `PLE_MATCH_METHOD` = 57,304 ≠ 49,986. The documented derivation logic does not produce the documented count. |
| 5 | `docs/data_dictionary.md` | L47, L82, L179–183, L203–205 | "observable cohort (Year <= 2014)" is what `IS_PLE_ANALYSIS_SAFE`/related PLE flags encode | **WRONG** | `(IS_PLE_ANALYSIS_SAFE == (Year<=2014)).all() == False`. True for 4,288 rows in 2015, 3,673 in 2016, 1,136 in 2017, 19 in 2018 — the flag does not implement the Year≤2014 rule at all. |
| 6 | `README.md` | L258 | "Observable cohort ... All PLE analyses restricted to Year <= 2014" | **STALE/MISLEADING** | True as a stated *design intent*, but no dataset column implements it — `IS_PLE_ANALYSIS_SAFE` (the flag docs tell readers to use) does not equal `Year<=2014`. Any consumer following the docs' advice to filter on the flag gets the wrong cohort. |
| 7 | `docs/pipeline_architecture.md` | L244–251, L469–471 | Same Year≤2014 / observable-cohort framing, "Cohort sizes: 64,501 best-observable rows, 29,269 confirmed PLE passers" | **PARTIALLY WRONG** | Row count 64,501 is CONFIRMED correct (`(df.Year<=2014 & IS_BEST_NMAT_RECORD).sum()==64501`). Passer count is off: actual best-record PLE passers within Year≤2014 = 29,273, not 29,269 (off by 4, minor). The broader claim that any dataset flag "restricts to Year<=2014" is unsupported — see #5. |
| 8 | `docs/data_dictionary.md` | L86, L90 + `docs/pipeline_architecture.md` L141–147 + README L67, L255 + CLAUDE.md L91, L147 | "42.2% of stored raw score totals were incorrect" / "107,422 mismatches" applied to describe the **final dataset** | **WRONG (denominator mismatch)** | The 42.2%/107,422 figure is CONFIRMED CORRECT but only at the intermediate `CEM_DATA.csv` level (107,422 / 254,308 = 42.24%, per `docs/pipeline_architecture.md` L144). In the final `NMAT_Exodus.parquet`, `StoredRawTotal` is non-null for only 99,316/178,927 rows, and of those, **56,065 mismatch `TotalRawScoreTRUE`** — that is **56.45% of the 99,316 non-null rows**, or **31.33% of all 178,927 rows**. Docs never disclose that "42.2%" is a different-stage, different-denominator statistic; every doc that repeats "42.2%" in the context of the Exodus/final dataset is factually wrong for that dataset. |
| 9 | `docs/pipeline_architecture.md` | L373, L395 + CLAUDE.md L109 | "129 raw nationalities canonicalized to 96 (canonical) values" | **PARTIALLY WRONG** | 129 raw values CONFIRMED CORRECT (`REAL_FOREIGNERS.csv['NAC_NATIONALITY'].nunique()==129`). "96 canonical" does not match anything: `docs/pipeline_architecture.md` L402 separately claims `CITIZENSHIP_FINAL` = "108 unique" (self-contradicting the "96" claim 33 lines earlier in the same file), and the actual parquet has **`CITIZENSHIP_FINAL.nunique() == 91`**. Three different numbers (96, 108, 91) exist for the same quantity across the doc set; none but 91 is correct. |
| 10 | `docs/data_dictionary.md` | L158 | "`CITIZENSHIP_FINAL` ... 108 unique values" | **WRONG** | Actual: 91. |
| 11 | `docs/data_dictionary.md` | L55 | `UNI_TYPE`: Public 18.9%, Private 79.1%, Foreign 1.7%, Not Specified 0.3% | **WRONG (all 4 values)** | Actual (CONFIRMED): Private 76.83% (137,476), Public 20.85% (37,304), Foreign 1.29% (2,315), Not Specified 1.02% (1,832). All four percentages are off; Public/Private are swapped in magnitude direction and Not Specified is overstated 3.4× vs actual... no, understated (doc says 0.3%, actual 1.02%, i.e. doc understates by ~3.4×). |
| 12 | `docs/data_dictionary.md` | L39 | AppNo formats: "6-digit (legacy, 0.4%), 7-digit (standard, 13.4%), 10-digit (newer, 85.3%)" | **PARTIALLY WRONG** | 7-digit (13.41%) and 10-digit (85.25%) are CONFIRMED essentially correct. 6-digit is wrong: actual is 2,402/178,927 = **1.34%**, not 0.4% (off by ~3.4×). |
| 13 | `docs/data_dictionary.md` | L82 | `PercentileBin` missing "~0.7%" | **WRONG** | Actual: 4,141/178,927 = **2.31%** missing (matches shared-context number). The doc appears to have copy-pasted the `NMS_PER_num` missing rate (0.71%, which IS correct for that column) onto `PercentileBin`. |
| 14 | `docs/data_dictionary.md` | L119–120, 131 | `AllRawComponentsPresent`, `HasTRUErawScores`, `StoredVsDerivedMismatch`, `CalcVsDerivedMismatch` typed as `bool`/`float` | **WRONG (dtype)** | CONFIRMED: all four are stored as Python/pandas **`str`**, not bool/float (`df[c].dtype == object`, values are the literal strings `'True'`/`'False'` or `'1.0'`/`'0.0'`/`NaN`). `bool("False") == True` — any naive truthiness check on these columns silently treats "False" as truthy. `HasCEMMatch` has the same bug (also `str`, doc says `bool`). |
| 15 | `docs/data_dictionary.md` | L119, L131 | `AllRawComponentsPresent`/`CalcVsDerivedMismatch` described as varying diagnostic flags | **MISLEADING** | Both are CONFIRMED constant (`nunique()==1`) — dead columns that carry no information, contrary to their documented "True when..." semantics implying variability. |
| 16 | CLAUDE.md | L171 | "`dataset/UNIVS.csv` — University reference list (2,981 verified names)" | **WRONG** | `UNIVS.csv` itself has **3,022 rows** (CONFIRMED). 2,981 is the count of *matched* records from a different, smaller audit file (`DsPy_verified.csv`, 4,367 rows: 2,981 matched + 1,386 unmatched = 4,367, CONFIRMED consistent internally) — not UNIVS.csv's row count. CLAUDE.md conflates the reference table size with a match-rate statistic from an unrelated audit file. |
| 17 | CLAUDE.md | L9–12 | "consumed by 3 dashboard implementations," lists root `dashboard.py` first as if primary | **STALE (per user's own correction)** | User states the live dashboards are under `streamlit_dashboard/` (`main_dashboard/` and `CHED_relevant_dashboard/`), each with its **own local copy** of `NMAT_Exodus.parquet`. Root `dashboard.py` is legacy. The "3 dashboards sharing one parquet" narrative is wrong on two counts: (a) root `dashboard.py` is not a live consumer, (b) there is no single shared parquet — three physically separate byte-identical copies exist. |
| 18 | CLAUDE.md | L153–154 | "`dashboard.py` — Main Streamlit app (2,800 lines), single entry point for production" | **STALE** | Actual line count 3,206 (not "2,800"; "2,800+" in the intro line is technically true but understates by ~400 lines and, more importantly, it is not the production entry point per the user's correction — see #17. `streamlit_dashboard/main_dashboard/dashboard.py` (3,207 lines) is effectively a duplicate/fork of root `dashboard.py`, not documented anywhere as such. |
| 19 | CLAUDE.md | L234–241 | RShiny presented as an actively maintained parity target ("Mirrors all 12 Streamlit tabs exactly") | **STALE (per user)** | User has abandoned RShiny. Also factually the tab count itself is stale — see #20. `_SHARED_CONTEXT.md` explicitly instructs auditors to ignore `RShiny_Dashboard/`. |
| 20 | CLAUDE.md L227, README.md L226, `docs/pipeline_architecture.md` (implicit), CHED_relevant README (not applicable) | "12 tabs/pages" for the Streamlit dashboard | **WRONG** | CONFIRMED by reading `streamlit_dashboard/main_dashboard/dashboard.py` L726–743: the dashboard defines **13 tabs** (`tab1`...`tab13`), the 13th being "⚖️ CHED Compliance" — added later per `changelog.md` ("`86c2bdb` Add CHED Compliance page (Page 13) to Streamlit dashboard"). Every doc that says "12 pages/tabs" is stale and omits the CHED Compliance page. |
| 21 | CLAUDE.md L262–265, L235 | "DuckDB is used in `data_aggregator` for query optimization" / "DuckDB queries in `data_aggregator/helpers.py` are ~2–3× faster than pandas" | **WRONG** | CONFIRMED by grep: **no file under `data_aggregator/` imports or references `duckdb`** — `helpers.py` and all 13 page scripts use only `pandas`/`numpy`/`scipy`. `duckdb` is actually imported by root `dashboard.py` and `streamlit_dashboard/main_dashboard/dashboard.py` (both `import duckdb` present), not by `data_aggregator`. The doc attributes the dependency to the wrong subsystem in three separate places. |
| 22 | root `requirements.txt` | whole file | Declares dependencies for `dashboard.py` (root) | **WRONG (missing dep)** | Root `dashboard.py` does `import duckdb` (L17) but root `requirements.txt` has no `duckdb` line. Following CLAUDE.md/README's documented setup (`pip install -r requirements.txt` then `streamlit run dashboard.py`) fails with `ModuleNotFoundError: No module named 'duckdb'`. (`streamlit_dashboard/main_dashboard/requirements.txt` correctly includes `duckdb`; only the root file is missing it.) |
| 23 | root `requirements.txt` vs `1_Data_Cleaning_Pipeline.ipynb` | whole file | Pipeline 1 re-runnable via documented setup | **WRONG (missing dep)** | CONFIRMED: `1_Data_Cleaning_Pipeline.ipynb` still imports/uses `rapidfuzz` (2 references, part of the Tier-3 university fuzzy-match cascade documented in `docs/pipeline_architecture.md` L157, "Fuzzy match (rapidfuzz, score >= 88, gap >= 5)"). `rapidfuzz` was removed from `requirements.txt` per `changelog.md` (`24e271e Remove rapidfuzz dependency, update requirements.txt`) as part of the PLE-matching de-fuzzy refactor — but Pipeline 1's *university-matching* fuzzy step (a separate use of rapidfuzz, unrelated to PLE matching) was not updated to match. Re-running Pipeline 1 from a clean `pip install -r requirements.txt` environment will fail on `import rapidfuzz`. |
| 24 | `README.md` | L207–214 (Option D) | ```cd data_aggregator``` then ```.venv\Scripts\python.exe run_all.py``` | **BROKEN COMMAND, CONFIRMED BY EXECUTION** | `data_aggregator/run_all.py` L11 hardcodes `SCRIPTS_DIR = Path("data_aggregator")` and L29 hardcodes `VENV_PYTHON = os.path.join(".venv", "Scripts", "python.exe")` — both relative to CWD. I verified by `cd`-ing into `data_aggregator/` and testing both paths: neither `data_aggregator/data_aggregator/` nor `data_aggregator/.venv/Scripts/python.exe` exists. Following the documented `cd data_aggregator` step makes every page script "SKIP (script not found)" and/or the subprocess call fail to locate the interpreter. The script must instead be run from the **repo root** as `python data_aggregator/run_all.py` (or the equivalent venv path), the opposite of what the doc says. CLAUDE.md L67–68 has the same broken `cd data_aggregator && python run_all.py` instruction. |
| 25 | `docs/data_dictionary.md` L39 core-identifier note, CLAUDE.md L9 | Row/col shape "178,927 rows × 54 columns" | VERIFIED | CONFIRMED exact match to parquet shape, all 3 physical copies. |
| 26 | `README.md` L5, `docs/*` | File size "10.5 MB" for Exodus, "27.9 MB" for `.bak`, "62.4% smaller" | VERIFIED | CONFIRMED: 11,007,467 bytes ≈ 10.5 MB; 29,277,141 bytes ≈ 27.9 MB; reduction = 62.4%. |
| 27 | `docs/pipeline_architecture.md` L28–33, L101–104, L117–119, L163–164, L187, L230, L264, L323, L491–499 | Row/column counts for every intermediate pipeline file (`NMAT_CLEANED_DATA.csv` 178,927×29; `CEM_DATA.csv` 254,308×36; `UNIVS.csv` 3,022×8; `PLE_DATA.csv` 43,630; `PLE_UNMATCHED.csv` 6,600; `REAL_FOREIGNERS.csv` 32,501×29; `pseudo_citizenship_profiling_FINAL.csv` 871×13; `NMAT_FINAL.parquet` 178,927×101; `NMAT_Ultima.parquet` 178,927×115; `PLE_MATCH_MASTER.csv` 43,601; `PLE_PASSERS_IN_NMAT.csv` 36,305; `PLE_STILL_UNMATCHED.csv` 7,207 in / `_v2.csv` 6,433 out; `NMAT_Exodus.parquet.bak` 118 cols) | VERIFIED | CONFIRMED — every one of these figures matched the actual files exactly on direct load. This is by far the most accurate part of the documentation set; the pipeline architecture's *file inventory* is trustworthy even though several of its *derived percentages* (StoredRawTotal 42.2%, canonicalization 96/108) are not. |
| 28 | `docs/pipeline_architecture.md` L239–242 | PLE match-status breakdown: FINAL_MATCH 36,395 (83.4%), AMBIGUOUS 772 (1.8%), NO_VALID_MATCH 2,298 (5.3%), UNMATCHED_NO_APPNO 4,135 (9.5%) | VERIFIED (partially, via proxy files) | `PLE_AMBIGUOUS_REVIEW.csv` = 772 rows CONFIRMED matches the 772 AMBIGUOUS count exactly. Other buckets not independently re-derivable from files present, treated as UNVERIFIABLE but internally consistent (sums to 43,600 ≈ 43,601 `PLE_MATCH_MASTER.csv` rows). |
| 29 | `docs/data_dictionary.md` L142, README L259, CLAUDE.md L141 | "25% of examinees took NMAT 2+ times" / "max 9 attempts" | VERIFIED | CONFIRMED: 33,714/134,869 unique `PERSON_KEY` = 25.00% have 2+ rows; max rows for one PERSON_KEY = 9. |
| 30 | `docs/data_dictionary.md` L145 | `PLE_YEAR_PASSED` range "2011–2022" | VERIFIED | CONFIRMED: min 2011.0, max 2022.0. |
| 31 | `docs/data_dictionary.md` L47 | `Year` "2006–2018... all 13 years represented" | VERIFIED | CONFIRMED: 13 unique years, 2006–2018. |
| 32 | `docs/data_dictionary.md` L140 | `IS_PLE_PASSER` "49,986 rows marked True" | VERIFIED | CONFIRMED. |
| 33 | `docs/data_dictionary.md` L159 | `FOREIGNER_STATUS` counts Filipino 146,413 / Verified Foreigner 32,501 / Likely Foreigner 13 | VERIFIED | CONFIRMED exact match. |
| 34 | `docs/data_dictionary.md` L132 | `HasCEMMatch` "True when the NMAT record has a matched CEM row (178,882 of 178,927 have CEM data)" | VERIFIED (count only) | Count CONFIRMED exact (178,882 True / 45 False); dtype claim (`bool`) is wrong — see #14. |
| 35 | `docs/data_dictionary.md` L160 | `name_based_assessment` "~99.5%" missing, "871 records" | VERIFIED | CONFIRMED: 99.51% missing, non-null count consistent with the 871-row profiling file. |
| 36 | `docs/data_dictionary.md` CourseGroup L57 | 6 categories named: Medical & Allied, Natural Sciences, Social & Behavioral Sciences, Education, Engineering & Technology, Other | VERIFIED | CONFIRMED: `nunique()==6`, all 6 names match exactly. |
| 37 | `docs/data_dictionary.md` UNI_LOCATION L56 | 3 values: Local, International, Unknown | VERIFIED | CONFIRMED: `nunique()==3`, names match; doc gives no percentages for this column so nothing further to check. |
| 38 | `streamlit_dashboard/CHED_relevant_dashboard/README.md` L9–14 | 6 tabs: National Profile / B4+ vs B5+ Thresholds / PLE-Passer Linkage / Institution and Foreign Context / Key Evidence for Policy Review / Data-Methods-Limitations | VERIFIED | CONFIRMED against `dashboard.py` L274–281 — exact match, 6 tabs, correct labels. This dashboard's own README is the most accurate document in the whole audit set. |
| 39 | `streamlit_dashboard/main_dashboard/README.md`, CHED README | `pip install -r requirements.txt && streamlit run dashboard.py` | VERIFIED (runnable, path-correct) | Both local requirements.txt files cover their respective dashboard.py's imports (see requirements-completeness section below); commands are simple and correctly scoped to their own directory. |
| 40 | `changelog.md` L80–83 | "Total commits: 36. Latest: `7fa0f18` (2026-07-28)" | **STALE** | `git log` shows commits after `7fa0f18` (per repo status: `dc46a04`, `ff45adf`, `1d4eda2`, `08d196a` — the entire forensic-audit suite — are absent from the changelog, all dated after the changelog's last entry). The changelog was not updated for the most recent 4+ commits. |
| 41 | `changelog.md` | Entire file | Does it document the `docs/` move and dictionary/architecture doc creation? | VERIFIED | Entries `be08185` (move docs to docs/), `76f1bf2` (data dictionary), `60acfc1` (pipeline architecture) are present and match actual doc locations. |
| 42 | `docs/tree_dir.txt`, root `tree_dir.txt` | Directory listing | **STALE** | Neither tree lists `streamlit_dashboard/` (containing both live dashboards!) or `forensic_audit/` at all — both directories exist in the repo (confirmed via `ls`) but are completely absent from both tree files. Both trees also still list `vault/` and `reports/` as if current. This is the single most misleading doc in the set: a newcomer using `tree_dir.txt` to orient themselves would never discover the actual live dashboards. |
| 43 | `00_RUN_ME.ipynb` | Single cell: `pip install pandas numpy pyarrow matplotlib seaborn scipy scikit-posthocs plotly kaleido unidecode tqdm streamlit` | **INCONSISTENT WITH requirements.txt** | Installs `matplotlib` and `seaborn`, neither of which appears in root `requirements.txt` nor is imported by any current-generation `.py` pipeline/dashboard file found (grep for `^import matplotlib`/`^import seaborn` across root, `data_aggregator/`, `streamlit_dashboard/` returned nothing beyond the notebook itself — likely legacy from an earlier charting approach before Plotly). Not a broken command, but it installs unnecessary/stale packages and omits `duckdb` (needed by both live `dashboard.py` files). |
| 44 | CLAUDE.md L300–307 "Dependencies & Versions" | Lists `duckdb` as a dependency "(used in data_aggregator for query optimization)" | **WRONG** | Same root cause as #21 — misattributes duckdb's actual consumer (the two Streamlit dashboards) to data_aggregator, and simultaneously the root `requirements.txt` this section is nominally describing doesn't list duckdb at all (see #22). |

---

## 2. Full 54-column data-dictionary verification table

Columns are the actual 54 in `dataset/NMAT_Exodus.parquet` (all 3 physical copies byte-identical). "Doc" = `docs/data_dictionary.md`. Missing% and nunique computed directly from the parquet.

| Column | Actual dtype | Doc dtype | Actual missing% | Doc missing% | Status | Note |
|---|---|---|---|---|---|---|
| `APPNO_CLEAN` | str | string | 0.0% | 0% | VERIFIED | nunique 178,926 (1 dup, per shared context). Format breakdown: 10-digit 85.25% (doc 85.3% ✓), 7-digit 13.41% (doc 13.4% ✓), 6-digit **1.34%** (doc says 0.4% — WRONG, ~3.4x off). |
| `PERSON_KEY` | str | string | 0.0% | 0% | VERIFIED | nunique 134,869. |
| `SEX` | str | string | 0.03% (45 rows) | ~0.03% | VERIFIED | Values Male/Female + 45 null. |
| `Year` | int64 | int | 0.0% | 0% | VERIFIED | 2006–2018, 13 unique. |
| `NMA_College` | str | string | 0.0% | 0% | VERIFIED | nunique 3,251 (doc: "3,251 unique values" — exact match). |
| `UNIVERSITY` | str | string | 0.0% | 0% | UNVERIFIED (nunique) | Doc claims 2,907 unique — not independently re-derived here but plausible given UNIVS.csv (3,022 rows) as source; not contradicted by other evidence. |
| `UNI_TYPE` | str | string | 0.0% | 0% | **WRONG (%s)** | 4 values CONFIRMED complete (Private/Public/Foreign/Not Specified) but all 4 percentages wrong — see master table #11. Correct: Private 76.83% (137,476), Public 20.85% (37,304), Foreign 1.29% (2,315), Not Specified 1.02% (1,832). |
| `UNI_LOCATION` | str | string | 0.0% | 0% | VERIFIED | 3 values (Local 97.68%/174,780, International 1.29%/2,315, Unknown 1.02%/1,832) — names match doc, doc gives no %s to check. |
| `CourseGroup` | str | string | 0.0% | 0% | VERIFIED | All 6 names + counts: Medical & Allied 48.14% (86,140), Natural Sciences 31.24% (55,900), Social & Behavioral Sciences 12.31% (22,022), Other 5.51% (9,855), Education 2.33% (4,162), Engineering & Technology 0.47% (848). |
| `NMS_VCss` | int64 | (unstated) | 0.0% | — | VERIFIED | nunique 127. |
| `NMS_IRss` | int64 | (unstated) | 0.0% | — | VERIFIED | nunique 133. |
| `NMS_Qss` | int64 | (unstated) | 0.0% | — | VERIFIED | nunique 147. |
| `NMS_PAss` | int64 | (unstated) | 0.0% | — | VERIFIED | nunique 135. |
| `NMS_BIOss` | int64 | (unstated) | 0.0% | — | VERIFIED | nunique 135. |
| `NMS_PHYss` | int64 | (unstated) | 0.0% | — | VERIFIED | nunique 135. |
| `NMS_SSCss` | int64 | (unstated) | 0.0% | — | VERIFIED | nunique 135. |
| `NMS_CHEMss` | int64 | (unstated) | 0.0% | — | VERIFIED | nunique 138. |
| `NMS_APT` | int64 | float | 0.0% | 0% | **WRONG (dtype)** | Actual dtype int64, doc says float. Minor. |
| `NMS_SA` | int64 | float | 0.0% | 0% | **WRONG (dtype)** | Same as above. |
| `NMS_GPS` | int64 | float | 0.0% | 0% | **WRONG (dtype)** | Same as above. |
| `NMS_PER_num` | float64 | float | 0.71% | 0.7% | VERIFIED | 1,275 missing rows, matches. |
| `PercentileBin` | str | string | **2.31%** | ~0.7% | **WRONG** | 4,141 nulls; doc figure appears copy-pasted from `NMS_PER_num`. |
| `TotalRawScoreTRUE` | float64 | float | 0.03% | ~0.03% | VERIFIED | |
| `PartIRawScoreTRUE` | float64 | float | 0.03% | ~0.03% | VERIFIED | |
| `PartIIRawScoreTRUE` | float64 | float | 0.03% | ~0.03% | VERIFIED | |
| `Raw_Verbal` | float64 | (unstated) | 0.03% | — | VERIFIED | nunique 31 (0-30 scale plausible). |
| `Raw_InductiveReasoning` | float64 | (unstated) | 0.03% | — | VERIFIED | nunique 31. |
| `Raw_Quantitative` | float64 | (unstated) | 0.03% | — | VERIFIED | nunique 31. |
| `Raw_PerceptualAcuity` | float64 | (unstated) | 0.03% | — | VERIFIED | nunique 31. |
| `Raw_Biology` | float64 | (unstated) | 0.03% | — | VERIFIED | nunique 31. |
| `Raw_Physics` | float64 | (unstated) | 0.03% | — | VERIFIED | nunique 31. |
| `Raw_SocialScience` | float64 | (unstated) | 0.03% | — | VERIFIED | nunique 31. |
| `Raw_Chemistry` | float64 | (unstated) | 0.03% | — | VERIFIED | nunique 31. |
| `APT_CEM` | float64 | float | 0.03% | ~0.03% | VERIFIED | |
| `SA_CEM` | float64 | float | 0.03% | ~0.03% | VERIFIED | |
| `GPS_CEM` | float64 | float | 0.03% | ~0.03% | VERIFIED | |
| `Percentile_CEM` | float64 | float | 2.34% | ~2.3% | VERIFIED | matches shared-context 4,182 nulls. |
| `AllRawComponentsPresent` | **str** | bool | 0.03% | ~0.03% | **WRONG (dtype + dead)** | Stored as str ("True"/"False"), `nunique()==1` — constant, contradicts "True when all 8 present" semantics implying variance. `bool("False")==True` risk for any naive consumer. |
| `HasTRUErawScores` | **str** | bool | 0.0% | 0% | **WRONG (dtype)** | Stored as str, not bool. Same truthiness risk. |
| `StoredRawTotal` | float64 | float | **44.49%** (99,316 non-null) | ~44% | VERIFIED (missing%) | But see mismatch-rate error below. |
| `CalculatedRawTotal_Source` | float64 | float | 0.03% | ~0.03% | VERIFIED | |
| `StoredVsDerivedMismatch` | **str** | float | 44.49% | ~44% | **WRONG (dtype + rate)** | Stored as str ('1.0'/'0.0'/NaN), not float. Mismatch count is **56,065** (56.45% of the 99,316 non-null rows / 31.33% of all rows) — NOT the "107,422 mismatches"/42.2% the doc states (that figure belongs to the earlier `CEM_DATA.csv`-level, 254,308-row computation). |
| `CalcVsDerivedMismatch` | **str** | float | 0.03% | ~0.03% | **WRONG (dtype)** | Stored as str; `nunique()==1` (always "0.0") — CONFIRMED "always 0" claim, but dtype wrong. |
| `HasCEMMatch` | **str** | bool | 0.0% | 0% | **WRONG (dtype)** | Stored as str; count (178,882 True/45 False) is correct. |
| `IS_PLE_PASSER` | bool | bool | 0.0% | 0% | VERIFIED | 49,986 True — matches doc. |
| `IS_PLE_ANALYSIS_SAFE` | bool | bool | 0.0% | 0% | **WRONG (semantics)** | Type/count correct (49,986 True) but semantics are false — see master table #4/#5: it is a pure duplicate of `IS_PLE_PASSER`, not the documented FINAL_MATCH/MANUAL_APPNO_MATCH/DETERMINISTIC_APPNO logic, and not Year≤2014. |
| `IS_BEST_NMAT_RECORD` | bool | bool | 0.0% | 0% | VERIFIED | True count 133,804/178,927. |
| `PLE_MATCH_METHOD` | str | string | 67.97% | ~68% | VERIFIED (missing%) | Values are `EXACT`/`MANUAL_APPNO_MATCH`/`DETERMINISTIC_APPNO`, NOT `FINAL_MATCH` as the `IS_PLE_ANALYSIS_SAFE` description implies (doc's own two entries for these two columns contradict each other on vocabulary). |
| `PLE_YEAR_PASSED` | float64 | float | 69.53% | ~69% | VERIFIED | Range 2011–2022 matches doc. |
| `PLE_YEAR_GAP` | float64 | float | 72.70% | ~72% | VERIFIED | |
| `PLE_MATCH_CONFIDENCE` | float64 | float | 67.97% | ~68% | VERIFIED | |
| `CITIZENSHIP_FINAL` | str | string | 0.0% | 0% | **WRONG (nunique)** | Actual nunique **91**, doc says "108 unique values" (also contradicts `pipeline_architecture.md`'s separate "96 canonical" claim). Top values match: Filipino 146,413, India 26,491 (doc: 26,490, off-by-1 — negligible), Nepal 1,158, Thailand 1,062, United States 839, Nigeria 639 — all CONFIRMED close/exact. |
| `FOREIGNER_STATUS` | str | string | 0.0% | 0% | VERIFIED | Filipino 146,413 / Verified Foreigner 32,501 / Likely Foreigner 13 — exact match, all 3 values listed. |
| `name_based_assessment` | str | string | 99.51% | ~99.5% | VERIFIED | |

**Columns that exist but are effectively undocumented / under-documented in `data_dictionary.md`:** none are fully missing from the table (all 54 have an entry), but 8 NMS subtest standard-score columns (`NMS_VCss` … `NMS_CHEMss`) have no dtype/missing%/domain row in the formal per-column table (only prose description in a separate section) — inconsistent formatting versus the rest of the dictionary, worth normalizing in a rewrite.

---

## 3. Findings table

| ID | Severity | Status | Title | Location |
|---|---|---|---|---|
| F1 | CRITICAL | CONFIRMED | `IS_PLE_ANALYSIS_SAFE` is a duplicate of `IS_PLE_PASSER`, not "Year≤2014, deterministic-only" as documented | `docs/data_dictionary.md:141`, `docs/pipeline_architecture.md:244-251`, `README.md:258`, `CLAUDE.md:125,138` |
| F2 | CRITICAL | CONFIRMED | "42.2% / 107,422 mismatches" StoredRawTotal claim is stated as describing the final Exodus dataset but is actually a CEM_DATA.csv-stage (254,308-row) statistic; the real Exodus-stage mismatch rate is 56.45% of 99,316 non-null rows (56,065 mismatches) | `docs/data_dictionary.md:86,90,124,128,130`, `docs/pipeline_architecture.md:141-147`, `README.md:67,255`, `CLAUDE.md:91,147` |
| F3 | HIGH | CONFIRMED | Phantom columns `PERSON_NAME`, `IS_BOARD_OBSERVABLE_COHORT`, `PLE_MATCH_STATUS` documented as live dataset columns; none exist in the 54-col parquet | `CLAUDE.md:119,125,127` |
| F4 | HIGH | CONFIRMED | `data_aggregator/run_all.py` uses CWD-relative paths (`Path("data_aggregator")`, `.venv/Scripts/python.exe`) that break exactly when invoked per the documented `cd data_aggregator && python run_all.py` instructions | `README.md:207-214`, `CLAUDE.md:67-68`, `data_aggregator/run_all.py:11,29` |
| F5 | HIGH | CONFIRMED | Root `requirements.txt` is missing `duckdb`, which root `dashboard.py` imports; documented setup (`pip install -r requirements.txt && streamlit run dashboard.py`) fails | `requirements.txt` (root), `dashboard.py:17` |
| F6 | HIGH | CONFIRMED | `1_Data_Cleaning_Pipeline.ipynb` still requires `rapidfuzz` (university Tier-3 fuzzy match) but `rapidfuzz` was removed from `requirements.txt` project-wide in commit `24e271e`; Pipeline 1 cannot be re-run from a clean documented install | `requirements.txt` (root), `1_Data_Cleaning_Pipeline.ipynb`, `changelog.md:74` |
| F7 | HIGH | CONFIRMED | "DuckDB used in `data_aggregator`" is fabricated/misattributed 3× in CLAUDE.md; `data_aggregator/` imports no duckdb anywhere, while the actual duckdb consumers (root `dashboard.py`, `streamlit_dashboard/main_dashboard/dashboard.py`) are undocumented as such | `CLAUDE.md:235,263,300-307` |
| F8 | HIGH | CONFIRMED | Every doc claiming "12 tabs/pages" for the Streamlit dashboard is stale; the live dashboard has 13 tabs (CHED Compliance added later) | `CLAUDE.md:227`, `README.md:226`, `streamlit_dashboard/main_dashboard/dashboard.py:726-743`, `changelog.md` (`86c2bdb`) |
| F9 | HIGH | CONFIRMED | `CITIZENSHIP_FINAL` nunique documented as 3 different, mutually contradictory numbers across docs (96 canonical / 108 unique / actual 91) | `docs/pipeline_architecture.md:373,402`, `CLAUDE.md:109`, `docs/data_dictionary.md:158` |
| F10 | MEDIUM | CONFIRMED | `UNI_TYPE` value-domain percentages wrong for all 4 categories | `docs/data_dictionary.md:55` |
| F11 | MEDIUM | CONFIRMED | 5 boolean-ish columns stored as `str`, documented as `bool`/`float`; naive truthiness (`bool("False")==True`) is a live footgun for anyone writing new dashboard code from the doc | `docs/data_dictionary.md:119,120,129,130,131,132` |
| F12 | MEDIUM | CONFIRMED | Both `tree_dir.txt` files omit `streamlit_dashboard/` and `forensic_audit/` entirely (the actual live dashboards and the newest audit suite) while still listing stale/abandoned dirs (`vault/`, `reports/`) | `docs/tree_dir.txt`, `tree_dir.txt` (root) |
| F13 | MEDIUM | CONFIRMED | `changelog.md` "Total commits: 36, Latest 7fa0f18" is stale — 4+ commits (forensic audit suite) postdate it | `changelog.md:80-81` |
| F14 | MEDIUM | CONFIRMED | `PercentileBin` missing% documented as ~0.7%, actual 2.31% (looks copy-pasted from `NMS_PER_num`'s correct 0.7%) | `docs/data_dictionary.md:82` |
| F15 | LOW | CONFIRMED | AppNo "6-digit legacy" share documented as 0.4%, actual 1.34% | `docs/data_dictionary.md:39` |
| F16 | LOW | CONFIRMED | `NMS_APT`/`NMS_SA`/`NMS_GPS` documented as `float`, actual dtype `int64` | `docs/data_dictionary.md:78-80` |
| F17 | LOW | CONFIRMED | `UNIVS.csv` mis-described as "2,981 verified names" (that's the DsPy_verified.csv match count); actual UNIVS.csv row count is 3,022 | `CLAUDE.md:171` |
| F18 | LOW | CONFIRMED | `00_RUN_ME.ipynb` installs unused `matplotlib`/`seaborn` and omits `duckdb`, inconsistent with root `requirements.txt` and actual imports | `00_RUN_ME.ipynb`, `requirements.txt` |
| F19 | LOW | CONFIRMED | Observable-cohort PLE-passer count off by 4 (doc 29,269 vs actual 29,273) | `docs/pipeline_architecture.md:251` |
| F20 | LOW | UNVERIFIABLE | `dashboard.py` "2,800+ lines" (actual 3,206) — technically not false but materially understates and the file itself is not the production entry point per user correction | `CLAUDE.md:10,154` |

---

## 4. Corrected canonical facts (for lifting directly into rewritten docs)

**Dataset**
- `dataset/NMAT_Exodus.parquet`: **178,927 rows × 54 columns**, 11,007,467 bytes (10.5 MB), md5 `8034a0e72e1ff4d4e3e0334e91c4bccf`. Byte-identical to `streamlit_dashboard/main_dashboard/NMAT_Exodus.parquet` and `streamlit_dashboard/CHED_relevant_dashboard/NMAT_Exodus.parquet` — **three separate physical copies, not one shared file consumed via a common path.** Any change to one must be manually propagated to the other two; there is no symlink/single-source-of-truth mechanism today.
- `.bak` full backup: 178,927 × 118 cols, 29,277,141 bytes (27.9 MB). Reduction 62.4% — CORRECT as documented.

**Real entry points (supersedes CLAUDE.md's "root dashboard.py is source of truth")**
- `streamlit_dashboard/main_dashboard/dashboard.py` (3,207 lines, 13 tabs) — live main dashboard, reads its own local `NMAT_Exodus.parquet` copy, imports `duckdb` (covered by its own `requirements.txt`).
- `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py` (1,262 lines, 6 tabs, matches its own README exactly) — live CHED-specific dashboard, reads its own local parquet copy, does NOT use duckdb.
- Root `dashboard.py` (3,206 lines) and `dashboard.py.bak` — legacy, per user; effectively a near-duplicate of `streamlit_dashboard/main_dashboard/dashboard.py` (1 line different). Root `requirements.txt` is broken for it anyway (missing `duckdb`).
- RShiny (`RShiny_Dashboard/NMAT_Shiny/app.R`, 2,190 lines) — abandoned per user; do not treat as a parity target.

**Key flag definitions (real behavior, not documented behavior)**
- `IS_PLE_PASSER` == `IS_PLE_ANALYSIS_SAFE` (byte-identical, 49,986 True each). Treat as one flag until the pipeline is fixed to actually diverge per the documented intent (deterministic-match-only vs. Year≤2014 restriction — neither is currently implemented as a distinct column). Anyone wanting the Year≤2014 "observable cohort" must filter on `Year <= 2014` directly; no boolean column does this for them.
- `IS_BEST_NMAT_RECORD`: True for 133,804/178,927 rows; one row per `PERSON_KEY` (134,869 unique persons). 25.00% of persons (33,714) have 2+ NMAT attempts, max 9 attempts — CONFIRMED CORRECT as currently documented.
- PLE match counts (mutually inconsistent, pick one and document why): `IS_PLE_PASSER==True` 49,986 | `PLE_YEAR_PASSED.notna()` 54,528 | `PLE_MATCH_METHOD.notna()` 57,304 | `PLE_YEAR_GAP.notna()` 48,842. `PLE_MATCH_METHOD` values are `EXACT` (54,437) / `MANUAL_APPNO_MATCH` (2,776) / `DETERMINISTIC_APPNO` (91) — never `FINAL_MATCH`, contrary to `data_dictionary.md`.

**Score recalibration (correctly scoped)**
- At the `CEM_DATA.csv` stage (254,308 rows): `STU_RSCORE` (stored total) wrong in 107,422 rows = **42.2%** — this specific figure IS correct, but only for this file/stage.
- At the final `NMAT_Exodus.parquet` stage: `StoredRawTotal` is non-null for only 99,316/178,927 rows (55.5% are null — the field is *sparse*, most rows never had a stored total to be wrong about). Of the 99,316 non-null rows, 56,065 (**56.45%**) mismatch `TotalRawScoreTRUE`; as a share of all 178,927 rows that's **31.33%**. Rewritten docs should present both stage-specific numbers explicitly and never let "42.2%" stand alone next to the final dataset's shape.

**Citizenship**
- `REAL_FOREIGNERS.csv['NAC_NATIONALITY']` raw cardinality: **129** unique values — CONFIRMED correct as documented.
- Final `CITIZENSHIP_FINAL` cardinality in Exodus: **91** unique values (not 96, not 108 — both of those appear elsewhere in the docs and are both wrong).
- `FOREIGNER_STATUS`: Filipino 146,413 (81.83%) / Verified Foreigner 32,501 (18.16%) / Likely Foreigner 13 (0.01%) — 3 values, CONFIRMED correct as documented.

**UNI_TYPE (correct percentages for rewrite)**
- Private 137,476 (76.83%) / Public 37,304 (20.85%) / Foreign 2,315 (1.29%) / Not Specified 1,832 (1.02%). (Docs currently say 79.1/18.9/1.7/0.3 — all four wrong.)

**Real data flow**
```
Raw CSVs (NMAT_CLEANED_DATA, CEM_DATA, UNIVS, PLE_DATA, PLE_UNMATCHED)
  -> Pipeline 1 (1_Data_Cleaning_Pipeline.ipynb, needs pandas+rapidfuzz+unidecode)
       -> dataset/output/NMAT_FINAL.parquet (178,927 x 101)   [CONFIRMED]
  -> Pipeline 2 (2_PLE_Matching_Pipeline.ipynb, deterministic only)
       -> dataset/NMAT_Ultima.parquet (178,927 x 115)          [CONFIRMED]
       -> dataset/output/PLE_MATCH_MASTER.csv (43,601 rows)    [CONFIRMED]
       -> dataset/output/PLE_PASSERS_IN_NMAT.csv (36,305 rows) [CONFIRMED]
  -> Pipeline 3 (3_NMAT_PLE_Analysis.ipynb) -> dataset/analysis_output/ (98 files present, not independently recounted as 59 CSV+36 PNG)
  -> Pipeline 4 (4_Citizenship_Integration.py, needs REAL_FOREIGNERS.csv + pseudo_citizenship_profiling_FINAL.csv)
       -> dataset/NMAT_Exodus.parquet (178,927 x 54)           [CONFIRMED, final]
       -> manually copied to streamlit_dashboard/main_dashboard/ and streamlit_dashboard/CHED_relevant_dashboard/ (NOT automated — three independent physical files today)
  -> streamlit_dashboard/main_dashboard/dashboard.py  (live, 13 tabs)
  -> streamlit_dashboard/CHED_relevant_dashboard/dashboard.py (live, 6 tabs)
  -> data_aggregator/ (static markdown, no duckdb, must be invoked as `python data_aggregator/run_all.py` from repo root, NOT `cd data_aggregator`)
  -> forensic_audit/ (root-level directory, not documented in either tree_dir.txt, contains forensic_audit_v5_final.py etc. — CLAUDE.md's forensic_audit commands are path-correct)
```

**Setup reproducibility checklist (what actually breaks for a new user following the docs)**
1. `pip install -r requirements.txt` (root) then `streamlit run dashboard.py` → **fails**, `ModuleNotFoundError: duckdb` (F5).
2. `cd data_aggregator && python run_all.py` (as README/CLAUDE.md instruct) → **fails silently into all-SKIP**, wrong relative paths (F4). Must run `python data_aggregator/run_all.py` from repo root instead.
3. Re-running Pipeline 1 from a clean `pip install -r requirements.txt` → **fails**, `ModuleNotFoundError: rapidfuzz` (F6).
4. `cd streamlit_dashboard/main_dashboard && pip install -r requirements.txt && streamlit run dashboard.py` → works, this local requirements.txt is complete.
5. `cd streamlit_dashboard/CHED_relevant_dashboard && pip install -r requirements.txt && streamlit run dashboard.py` → works, complete and correct.
6. `forensic_audit/*.py` commands in CLAUDE.md → all 3 named scripts exist at the stated paths, commands are correct as written.
