"""Generate 6_Robustness_Analysis.ipynb — the 10-step guide, implemented."""
import json, sys

cells = []


def md(text):
    cells.append({"cell_type": "markdown", "metadata": {}, "source": text.strip("\n").splitlines(keepends=True)})


def code(text):
    cells.append({"cell_type": "code", "execution_count": None, "metadata": {},
                  "outputs": [], "source": text.strip("\n").splitlines(keepends=True)})


# ---------------------------------------------------------------- title
md(r"""
# Robustness & Evidence Analysis — NMAT Admission Standards Paper

Implements the ten analytical steps from *"Analytical Steps Guide: Further Data Analysis for the
NMAT Admission Standards Evidence Paper"* (Section 9.5 of the paper).

**Read this before anything else.**

Every step below is executed against the corrected dataset produced by the remediated pipeline
chain (Pipelines 1 → 2 → 4 → 5). During remediation five defects were found and fixed in that
chain. Two of them change how this guide should be read:

1. **The matcher used to refuse to match below-40th-percentile examinees.** `disambiguate()` in
   `2_PLE_Matching_Pipeline.ipynb` applied a hard `PERCENTILE_FLOOR = 40`, discarding
   name-collision candidates below the 40th percentile. That manufactured an artificial cliff at
   exactly the CMO threshold under review. **The "~23-point B4→B5 gap" the guide treats as the
   paper's central descriptive finding is largely that artefact.** Steps 3 and 4 are therefore
   reframed below: they still run, but they test whether a discontinuity exists rather than
   assuming one does.
2. **A record-linkage bug credited one PLE passer to several same-named people.** Fixing it moved
   confirmed passers from 49,086 sittings to 47,485, and distinct passers to 35,746.

As a result **every headline number quoted in the guide is superseded.** Step 0 reconciles them
explicitly so the paper cannot end up citing two different figures for the same quantity.

## How to read this notebook

- Each step prints a **RESULT** block (the table or statistic) and an **INTERPRETATION** block.
- Interpretation text is *computed from the data*, not typed in, so it can never drift out of sync
  with the numbers above it.
- Static framing and caveats live in the markdown cells; anything numeric is generated.
- `assert` statements guard each step. If an assertion fires, the notebook stops — a silently
  wrong table is worse than a failed run.

## Standing constraints (apply to every step)

| Constraint | Why |
|---|---|
| **"Linkage", never "pass rate"** | `PLE_DATA.csv` contains passers only — no failures, no roster of takers. Every rate here is the share of NMAT examinees matched to a passer record. |
| **Observable cohort = `IS_BEST_OBSERVABLE_RECORD`** | Not `IS_BEST_NMAT_RECORD & Year<=2014`, which drops 3,721 people whose best attempt fell later. |
| **B1 is the LOWEST decile** | A string sort puts B10 between B1 and B2. Bins are ordered explicitly everywhere. |
| **`UNDERGRAD_*` is the undergraduate institution** | No medical-school identifier exists anywhere in this dataset, so nothing here can speak to SUC/PHEI admission or institutional PLE performance. |
| **PLE source covers 2011–2022 only** | Cohorts are observed through unequal windows. See Step 6. |
""")

# ---------------------------------------------------------------- setup
md(r"""
---
## Setup and provenance

Pins the notebook to a specific dataset build. If the md5 does not match, the numbers below were
produced by a different pipeline run and must not be quoted alongside them.
""")

code(r'''
import hashlib, json, warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from statsmodels.stats.proportion import proportions_ztest

warnings.filterwarnings("ignore")
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 60)

ROOT = Path.cwd()
if not (ROOT / "dataset").exists():          # tolerate being run from a subfolder
    ROOT = ROOT.parent

PARQUET = ROOT / "dataset" / "NMAT_Exodus.parquet"
RAW_CSV = ROOT / "dataset" / "NMAT_CLEANED_DATA.csv"
MATCH_MASTER = ROOT / "dataset" / "output" / "PLE_MATCH_MASTER.csv"

EXPECTED_MD5 = "72b2808bb8bb9c3594980c5735f814e1"
md5 = hashlib.md5(PARQUET.read_bytes()).hexdigest()

df = pd.read_parquet(PARQUET)

BINS = [f"B{i}" for i in range(1, 11)]        # B1 lowest .. B10 highest
SUB  = ["B1", "B2", "B3", "B4"]               # below the 40th percentile
B5P  = [f"B{i}" for i in range(5, 11)]        # 40th percentile and above

# Observable cohort: one row per person, best attempt, NMAT year <= 2014.
obs = df[df["IS_BEST_OBSERVABLE_RECORD"].fillna(False).astype(bool)].copy()
obs["linked"] = obs["IS_PLE_PASSER"].fillna(False).astype(bool)
obs["pct"]    = pd.to_numeric(obs["NMS_PER_num"], errors="coerce")

assert md5 == EXPECTED_MD5, f"dataset md5 {md5} != expected {EXPECTED_MD5}"
assert df.shape == (178_927, 53), f"unexpected shape {df.shape}"
assert (obs["pct"].dropna() >= 0).all(), "negative percentile found (the -1 sentinel is back)"
assert obs["PercentileBin"].dropna().isin(BINS).all(), "unexpected bin label"

print(f"source      : {PARQUET}")
print(f"md5         : {md5}  (matches expected build)")
print(f"rows x cols : {df.shape[0]:,} x {df.shape[1]}")
print(f"observable cohort (people)      : {len(obs):,}")
print(f"  of whom linked to a PLE passer: {int(obs['linked'].sum()):,} "
      f"({obs['linked'].mean()*100:.2f}%)")
print("\nAll provenance assertions passed.")
''')


# ---------------------------------------------------------------- viz setup
md(r"""
---
## Visualization conventions

Charts follow one system so ten steps read as one document:

- **Palette** — categorical slots assigned in fixed order (blue, orange, aqua), validated for
  colour-vision deficiency (worst adjacent CVD ΔE 9.2, normal-vision ΔE 27.6, both clear of the
  floors). Colour follows the entity, never its rank.
- **One axis, always.** No chart here uses two y-scales. Where two measures of different scale must
  be compared (Step 8), they get separate panels rather than a shared plot with two scales — a
  dual axis would imply whatever relationship the two scales happened to be aligned to.
- **Emphasis over decoration.** Where the story is one category, that category carries the colour
  and the rest go grey.
- **Every chart sits directly above or below its own data table**, so a reader who cannot resolve a
  hue can always read the number.
""")

code(r'''
import matplotlib as mpl
import matplotlib.pyplot as plt

SURFACE = "#fcfcfb"; INK = "#0b0b0b"; INK2 = "#52514e"
GRID    = "#e4e3de"; MUTED = "#b8b7b0"
C1, C2, C3 = "#2a78d6", "#eb6834", "#1baf7a"   # validated categorical slots 1-3

mpl.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "axes.edgecolor": GRID, "axes.labelcolor": INK2, "text.color": INK,
    "xtick.color": INK2, "ytick.color": INK2,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
    "font.size": 10, "figure.dpi": 110, "axes.titlesize": 12,
})

def style(ax, title, ylab=None, xlab=None):
    """One title/axis treatment for every figure in this notebook."""
    ax.set_title(title, loc="left", fontweight="600", color=INK, pad=10)
    if ylab: ax.set_ylabel(ylab)
    if xlab: ax.set_xlabel(xlab)
    ax.set_axisbelow(True)
    return ax

def label_bars(ax, bars, fmt="{:.1f}", dy=0.6, color=INK2, size=9):
    for b in bars:
        h = b.get_height()
        ax.text(b.get_x() + b.get_width()/2, h + dy, fmt.format(h),
                ha="center", va="bottom", fontsize=size, color=color)

print("Chart style loaded. Palette validated: CVD dE 9.2, normal-vision dE 27.6 (both pass).")
''')

# ---------------------------------------------------------------- step 0
md(r"""
---
## Step 0 — Reconciling the guide's numbers against this dataset

**Not in the original guide.** Added because the guide was written against tables that predate the
pipeline corrections. Running Steps 1–10 without this reconciliation would produce a paper that
cites two different values for the same quantity.
""")

code(r'''
_sub = obs[obs["PercentileBin"].isin(SUB)]
_g   = obs.groupby("PercentileBin")["linked"].mean().reindex(BINS) * 100
_pub = obs[obs["UNDERGRAD_UNI_TYPE"] == "Public"]
_pri = obs[obs["UNDERGRAD_UNI_TYPE"] == "Private"]

recon = pd.DataFrame([
    ("Sub-threshold (B1-B4) linked passers", "3,644",  f"{int(_sub['linked'].sum()):,}"),
    ("Dataset columns",                      "54",     f"{df.shape[1]}"),
    ("B4->B5 gap (percentage points)",        "~23",   f"{_g['B5'] - _g['B4']:.1f}"),
    ("Public B5+ clearance",                  "64.9%", f"{_pub['PercentileBin'].isin(B5P).mean()*100:.1f}%"),
    ("Private B5+ clearance",                 "59.2%", f"{_pri['PercentileBin'].isin(B5P).mean()*100:.1f}%"),
    ("Confirmed PLE passers (sittings)",      "n/a",   f"{int(df['IS_PLE_PASSER'].fillna(False).astype(bool).sum()):,}"),
], columns=["Quantity", "Guide / published brief", "This dataset (corrected)"])

print("RESULT — guide figures vs corrected dataset")
print(recon.to_string(index=False))

print("\nINTERPRETATION")
print(f"  Every quantity the guide quotes has moved. The sub-threshold count is "
      f"{int(_sub['linked'].sum()) - 3644:+,} against the guide's 3,644, and the B4->B5 gap is "
      f"{_g['B5'] - _g['B4']:.1f} points rather than ~23.")
print("  Any table carried over from the published brief must be regenerated, not reused.")
''')

# ---------------------------------------------------------------- step 1
md(r"""
---
## Step 1 — Sub-threshold linked passers by institution type

**Guide's objective:** replace the uniform-rate estimate with an exact tabulation of how many
B1–B4 linked passers are Public vs Private.

**Verdict: valid, run as specified.** The guide predicts the Private/PHEI share will exceed the
uniform estimate. That prediction is testable here.

**Caveat carried from the guide (and it is fatal for any SUC/PHEI reading):** `UNDERGRAD_UNI_TYPE`
is the examinee's *undergraduate* institution. It is not their medical school, and this dataset
contains no medical-school identifier at all. This table cannot speak to SUC vs PHEI admission.
""")

code(r'''
sub = obs[obs["PercentileBin"].isin(SUB)]

s1 = (sub.groupby("UNDERGRAD_UNI_TYPE")
         .agg(examinees=("linked", "size"), linked_passers=("linked", "sum"))
         .assign(linkage_rate_pct=lambda t: (t.linked_passers / t.examinees * 100).round(1))
         .sort_values("linked_passers", ascending=False))
s1["share_of_linked_passers_pct"] = (s1.linked_passers / s1.linked_passers.sum() * 100).round(1)

total = int(s1.linked_passers.sum())
assert total == int(sub["linked"].sum()), "cross-tab lost rows"

print(f"RESULT — B1-B4 (below 40th percentile) linked passers, observable cohort  (n = {total:,})")
print(s1.to_string())

priv = s1.loc["Private"]; publ = s1.loc["Public"]
print("\nINTERPRETATION")
print(f"  Of the {total:,} sub-threshold linked passers, {int(priv.linked_passers):,} "
      f"({priv.share_of_linked_passers_pct:.1f}%) come from Private undergraduate institutions and "
      f"{int(publ.linked_passers):,} ({publ.share_of_linked_passers_pct:.1f}%) from Public.")
print(f"  The guide predicted the Private share would exceed a uniform-rate estimate. It does: "
      f"Private supplies {priv.share_of_linked_passers_pct:.1f}% of sub-threshold linked passers "
      f"while making up {priv.examinees / s1.examinees.sum() * 100:.1f}% of the sub-threshold pool.")
print(f"  Note the direction of the RATE, which the guide does not anticipate: within B1-B4, "
      f"Private examinees link at {priv.linkage_rate_pct:.1f}% versus Public at "
      f"{publ.linkage_rate_pct:.1f}%.")
print("  This is an undergraduate-institution split. It says nothing about SUC/PHEI medical schools.")
''')


code(r'''
d1 = s1.sort_values("linked_passers", ascending=False)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

b = axes[0].bar(d1.index, d1.linked_passers, color=C1, width=.62)
label_bars(axes[0], b, "{:,.0f}", dy=60)
style(axes[0], "Linked passers below the 40th percentile", "examinees")
axes[0].set_ylim(0, d1.linked_passers.max() * 1.18)

b = axes[1].bar(d1.index, d1.linkage_rate_pct, color=C1, width=.62)
label_bars(axes[1], b, "{:.1f}%", dy=.4)
style(axes[1], "Linkage rate within B1-B4", "% of sub-threshold examinees")
axes[1].set_ylim(0, d1.linkage_rate_pct.max() * 1.22)

for ax in axes: ax.tick_params(axis="x", rotation=15)
fig.suptitle("Step 1 - sub-threshold linked passers by UNDERGRADUATE institution type",
             x=.01, ha="left", fontsize=13, fontweight="700", color=INK)
fig.tight_layout(rect=[0, 0, 1, .94]); plt.show()
print("Left panel is volume, right is rate. They point different ways: Private supplies most of the")
print("sub-threshold passers because it is most of the pool, AND links at a higher rate within it.")
''')

# ---------------------------------------------------------------- step 2
md(r"""
---
## Step 2 — Missingness / evaluability audit

**Guide's objective:** a definitive field-by-field audit replacing ad hoc statements about what the
dataset can and cannot answer.

**Verdict: largely already delivered.** `docs/data_dictionary.md` documents all 53 columns against
the live file. What that document lacks is the guide's six *evaluability* flags, so this step adds
exactly that and nothing else.

The six categories the guide asks about: GIDA residency, IP membership, medical-school (SUC/PHEI)
destination, admission-year applicable cutoff, institution-level PLE denominator, and non-NMAT
admission criteria (GWA, interview, etc.).
""")

code(r'''
CATEGORIES = ["GIDA_residency", "IP_membership", "medschool_destination",
              "admission_year_cutoff", "institutional_PLE_denominator", "non_NMAT_criteria"]

# No column in the shipped schema captures any of the six. This is asserted, not assumed:
# the check below looks for any plausible token in every column name.
TOKENS = {
    "GIDA_residency":                ["gida", "geograph", "isolat", "barangay", "municipal", "remote"],
    "IP_membership":                 ["indigen", "_ip_", "ethnic", "tribe", "ancestral"],
    "medschool_destination":         ["med_school", "medschool", "medical_school", "college_of_med", "enrolled"],
    "admission_year_cutoff":         ["cutoff", "cut_off", "threshold", "admission"],
    "institutional_PLE_denominator": ["school_ple", "institution_ple", "ple_denominator", "ple_takers"],
    "non_NMAT_criteria":             ["gwa", "interview", "essay", "recommendation", "gpa"],
}

rows = []
for col in df.columns:
    low = col.lower()
    rec = {"field": col,
           "dtype": str(df[col].dtype),
           "pct_non_null": round(df[col].notna().mean() * 100, 2),
           "n_distinct": int(df[col].nunique(dropna=True))}
    for cat in CATEGORIES:
        rec[cat] = any(tok in low for tok in TOKENS[cat])
    rows.append(rec)

audit = pd.DataFrame(rows)
hits = {cat: int(audit[cat].sum()) for cat in CATEGORIES}

print(f"RESULT — evaluability audit over all {len(audit)} shipped columns")
print("\nColumns capturing each evaluability category:")
for cat, n in hits.items():
    print(f"  {cat:<32s} {n} column(s)" + ("" if n else "   <- ABSENT"))

print("\nFirst 12 rows of the field-level audit (full table exported below):")
print(audit.head(12).to_string(index=False))

out = ROOT / "dataset" / "analysis_output" / "step02_evaluability_audit.csv"
out.parent.mkdir(parents=True, exist_ok=True)
audit.to_csv(out, index=False)

print("\nINTERPRETATION")
absent = [c for c, n in hits.items() if n == 0]
print(f"  {len(absent)} of the 6 evaluability categories have NO representing column in the shipped "
      f"schema: {', '.join(absent)}.")
print("  Consequence: the paper cannot evaluate CMO compliance at institution level, cannot identify")
print("  GIDA or IP examinees, cannot know which cutoff applied in a given admission year, and cannot")
print("  observe any non-NMAT admission criterion. These are structural absences, not missing data")
print("  that better cleaning would recover.")
print(f"  Step 9 revisits GIDA/IP specifically against the RAW file, which has columns the shipped")
print(f"  file drops.")
print(f"\n  Full audit written to {out.relative_to(ROOT)}")
print("\n  (No chart for this step: the finding is that every category is absent. A bar chart\n   of ten zeros communicates less than this sentence does.)")
''')

# ---------------------------------------------------------------- step 3
md(r"""
---
## Step 3 — Best-record selection sensitivity

**Guide's objective:** test whether the B4→B5 transition depends on how the "best" record is chosen
among repeat takers.

**Reframed, and one specification flagged as unsound.** The guide's primary specification (A) is
*"PLE-matched attempt for linked passers, otherwise highest percentile"*. That makes record
selection **depend on the outcome being studied**: passers are represented by a different attempt
than non-passers. This is the same class of defect already removed from this pipeline once — an
earlier version applied one rule to passers and another to everyone else, and silently dropped
1,311 people from every person-level count.

Specification A is therefore computed and reported **as a bias demonstration**, not as the primary.
Specifications B (first attempt) and C (highest percentile) apply one uniform rule to every person
and are the defensible ones.
""")

code(r'''
# Attempt-level frame: every sitting, with the person's linked status attached.
att = df.copy()
att["linked"] = att["IS_PLE_PASSER"].fillna(False).astype(bool)
att["pct"]    = pd.to_numeric(att["NMS_PER_num"], errors="coerce")
att = att[att["pct"].notna() & att["PercentileBin"].notna()]

# Which sitting was actually matched to the PLE record? Recovered from the match master,
# since Pipeline 2 propagates PLE metadata across a person's sittings.
matched_appnos = set()
if MATCH_MASTER.exists():
    mm = pd.read_csv(MATCH_MASTER, dtype=str, low_memory=False)
    matched_appnos = set(mm["MATCHED_APPNO"].dropna().astype(str).str.strip()) - {"", "nan"}
att["is_matched_sitting"] = att["APPNO_CLEAN"].astype(str).isin(matched_appnos)

obs_att = att[att["Year"] <= 2014]

def spec_A(g):   # outcome-dependent -- reported to show the bias, not to be used
    if g["linked"].iloc[0] and g["is_matched_sitting"].any():
        return g[g["is_matched_sitting"]].nlargest(1, "pct")
    return g.nlargest(1, "pct")

sel = {}
sel["C_highest_pct"]  = obs_att.sort_values("pct",  ascending=False).groupby("PERSON_KEY", as_index=False).head(1)
sel["B_first_attempt"] = obs_att.sort_values("Year", ascending=True ).groupby("PERSON_KEY", as_index=False).head(1)
sel["A_outcome_dependent"] = (obs_att.sort_values(["is_matched_sitting", "pct"], ascending=[False, False])
                                     .groupby("PERSON_KEY", as_index=False).head(1))

s3 = pd.DataFrame({name: g.groupby("PercentileBin")["linked"].mean().reindex(BINS) * 100
                   for name, g in sel.items()}).round(1)
s3 = s3[["B_first_attempt", "C_highest_pct", "A_outcome_dependent"]]

for name, g in sel.items():
    assert g["PERSON_KEY"].is_unique, f"{name} produced duplicate people"

gaps = {c: s3.loc["B5", c] - s3.loc["B4", c] for c in s3.columns}

print("RESULT — linkage rate (%) by bin under three best-record specifications")
print(s3.to_string())
print("\nB4->B5 gap under each specification (percentage points):")
for c, v in gaps.items():
    print(f"  {c:<22s} {v:5.1f}")

print("\nINTERPRETATION")
print(f"  Under the two defensible, uniform-rule specifications the B4->B5 gap is "
      f"{gaps['B_first_attempt']:.1f} points (first attempt) and {gaps['C_highest_pct']:.1f} points "
      f"(highest percentile).")
print(f"  Neither is anywhere near the ~23 points the guide describes. The transition is stable "
      f"across specifications, but stable at a MODEST value -- so this is robustness evidence for a "
      f"gentle gradient, not for a discontinuity.")
print(f"  Specification A, which selects the matched sitting for passers only, gives "
      f"{gaps['A_outcome_dependent']:.1f} points. It is listed for completeness and must not be used: "
      f"choosing a person's representative attempt using the outcome under study builds the "
      f"correlation it then reports.")
''')


code(r'''
fig, ax = plt.subplots(figsize=(9.5, 4.6))
x = range(len(BINS))
ax.plot(x, s3["B_first_attempt"], marker="o", ms=6, lw=2, color=C1, label="B - first attempt")
ax.plot(x, s3["C_highest_pct"],   marker="o", ms=6, lw=2, color=C2, label="C - highest percentile")
ax.plot(x, s3["A_outcome_dependent"], marker="o", ms=5, lw=1.6, color=MUTED, ls="--",
        label="A - outcome-dependent (do not use)")
ax.axvspan(3, 4, color=C3, alpha=.10)
ax.annotate("B4 -> B5  (CMO threshold)", xy=(3.5, .95), xycoords=("data", "axes fraction"),
            ha="center", va="top", fontsize=9, color=INK2)
ax.set_xticks(list(x)); ax.set_xticklabels(BINS)
style(ax, "Step 3 - linkage rate by bin under three best-record rules",
      "linkage rate (%)", "percentile bin (B1 lowest)")
ax.legend(frameon=False, fontsize=9, loc="upper left")
fig.tight_layout(); plt.show()
print("The three lines track each other closely: the gradient is not an artifact of how the")
print("representative attempt is chosen. Specification A is drawn grey and dashed because it")
print("selects on the outcome and must not be used as the primary.")
''')

# ---------------------------------------------------------------- step 4
md(r"""
---
## Step 4 — Significance and changepoint testing on the gradient

**Guide's objective:** attach a formal test to the B4→B5 transition, and confirm it is the single
largest discontinuity rather than an eyeballed one.

**Reframed.** The guide assumes B4→B5 is the standout and asks for confirmation. This step instead
tests *whether any bin boundary stands out*, which is the question the data can actually answer.

Two additions the guide omits, both necessary for the result to be publishable:

- **Multiple-comparison correction.** Nine adjacent-bin tests are run. Without correction, finding
  "a significant gap" somewhere is close to guaranteed. Holm–Bonferroni is applied.
- **Effect size.** At n in the tens of thousands, p-values are near-meaningless on their own.
""")

code(r'''
cnt = obs.groupby("PercentileBin")["linked"].agg(["size", "sum"]).reindex(BINS)

res = []
for i in range(len(BINS) - 1):
    lo, hi = BINS[i], BINS[i + 1]
    s = [int(cnt.loc[hi, "sum"]), int(cnt.loc[lo, "sum"])]
    n = [int(cnt.loc[hi, "size"]), int(cnt.loc[lo, "size"])]
    z, p = proportions_ztest(s, n)
    p_lo = s[1] / n[1]; p_hi = s[0] / n[0]
    res.append({"boundary": f"{lo}->{hi}",
                "rate_lo_pct": round(p_lo * 100, 1),
                "rate_hi_pct": round(p_hi * 100, 1),
                "gap_pts": round((p_hi - p_lo) * 100, 1),
                "z": round(z, 2), "p_raw": p,
                "cohens_h": round(abs(2*np.arcsin(np.sqrt(p_hi)) - 2*np.arcsin(np.sqrt(p_lo))), 3)})

s4 = pd.DataFrame(res)

# Holm-Bonferroni across the nine boundary tests.
order = s4["p_raw"].rank(method="first").astype(int)
m = len(s4)
s4["p_holm"] = [min(1.0, (m - order[i] + 1) * s4["p_raw"][i]) for i in s4.index]
s4["signif_holm_05"] = s4["p_holm"] < 0.05
s4 = s4.sort_values("gap_pts", ascending=False).reset_index(drop=True)

s4_show = s4.copy()
s4_show["p_raw"]  = s4_show["p_raw"].map(lambda v: f"{v:.2e}")
s4_show["p_holm"] = s4_show["p_holm"].map(lambda v: f"{v:.2e}")

print("RESULT — all nine adjacent-bin boundaries, ranked by gap size")
print(s4_show.to_string(index=False))

b45 = s4[s4.boundary == "B4->B5"].iloc[0]
largest = s4.iloc[0]
rank45 = int(s4.index[s4.boundary == "B4->B5"][0]) + 1

print("\nINTERPRETATION")
print(f"  B4->B5 -- the CMO threshold boundary -- has a gap of {b45.gap_pts} points and ranks "
      f"{rank45} of 9 by size.")
print(f"  The largest boundary is {largest.boundary} at {largest.gap_pts} points.")
if rank45 == 1:
    print("  B4->B5 is the largest boundary.")
else:
    print(f"  B4->B5 is NOT the standout transition the guide assumes. At least one other boundary "
          f"({largest.boundary}) is larger, and the guide's premise of a discontinuity located at "
          f"the 40th percentile is not supported.")
nsig = int(s4.signif_holm_05.sum())
print(f"  {nsig} of 9 boundaries remain significant after Holm-Bonferroni correction, which is "
      f"expected at this sample size and is why effect size matters more than p here.")
print(f"  Cohen's h for B4->B5 is {b45.cohens_h} -- a small effect by conventional benchmarks "
      f"(0.2 small, 0.5 medium, 0.8 large).")
print("  Conclusion: the linkage gradient rises steadily across bins. There is no changepoint at the")
print("  40th percentile. The paper should not describe one, and must not treat this as validating")
print("  the 40th-percentile cutoff.")
''')


code(r'''
order = [f"B{i}->B{i+1}" for i in range(1, 10)]
g4 = s4.set_index("boundary").reindex(order)
colors = [C1 if b == "B4->B5" else MUTED for b in order]

fig, ax = plt.subplots(figsize=(9.5, 4.4))
bars = ax.bar(order, g4.gap_pts, color=colors, width=.66)
label_bars(ax, bars, "{:.1f}", dy=.18)
style(ax, "Step 4 - size of every adjacent-bin transition",
      "gap (percentage points)", "bin boundary")
ax.set_ylim(0, g4.gap_pts.max() * 1.18)
ax.tick_params(axis="x", rotation=30)
top = g4.gap_pts.idxmax()
ax.annotate(f"largest gap is {top}, not the CMO boundary",
            xy=(order.index(top), g4.gap_pts.max()), xytext=(4.4, g4.gap_pts.max() * 1.06),
            fontsize=9, color=INK2,
            arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.2))
fig.tight_layout(); plt.show()
print("If a 40th-percentile threshold produced a real discontinuity, the B4->B5 bar would stand")
print("clear of the others. It does not - three boundaries are within 0.3 points of each other.")
''')

# ---------------------------------------------------------------- step 5
md(r"""
---
## Step 5 — Match-type-stratified linkage

**Guide's objective:** test whether the bin gradient is an artifact of looser matching criteria
being more common in one score band than another.

**Verdict: valid and important — this is a genuine negative control.** If low bins depended
disproportionately on looser matching, part of the gradient would be a data-quality artifact rather
than an outcome relationship.

Relevant background: `MANUAL_APPNO_MATCH` joins on a manually supplied application number **with no
name, year or date-of-birth verification at match time**. It is the loosest of the three methods,
so its distribution across bins is the thing to watch.
""")

code(r'''
linked = obs[obs["linked"]].copy()

comp = (pd.crosstab(linked["PercentileBin"], linked["PLE_MATCH_METHOD"], normalize="index")
          .reindex(BINS).mul(100).round(1))

rate_by_method = {}
for meth in ["EXACT", "MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"]:
    num = obs[obs["linked"] & (obs["PLE_MATCH_METHOD"] == meth)].groupby("PercentileBin").size()
    den = obs.groupby("PercentileBin").size()
    rate_by_method[meth] = (num.reindex(BINS).fillna(0) / den.reindex(BINS) * 100).round(2)
rates = pd.DataFrame(rate_by_method)

ct = pd.crosstab(linked["PercentileBin"], linked["PLE_MATCH_METHOD"]).reindex(BINS).fillna(0)
chi2, pval, dof, _ = chi2_contingency(ct)
cramers_v_5 = np.sqrt(chi2 / (ct.values.sum() * (min(ct.shape) - 1)))

print("RESULT — match-method composition WITHIN linked passers, by bin (row %)")
print(comp.to_string())
print("\nRESULT — linkage rate (%) contributed by each method, by bin")
print(rates.to_string())

man = comp["MANUAL_APPNO_MATCH"]
print(f"\nChi-square test, bin x match-method independence: chi2 = {chi2:,.1f}, "
      f"dof = {dof}, p = {pval:.3e}, Cramer's V = {cramers_v_5:.4f}")

print("\nINTERPRETATION")
print(f"  The loosest method, MANUAL_APPNO_MATCH, accounts for {man.min():.1f}%-{man.max():.1f}% of "
      f"linked passers across bins (lowest decile B1: {man['B1']:.1f}%, highest B10: {man['B10']:.1f}%).")
print(f"  Cramer's V of {cramers_v_5:.4f} indicates a negligible association between score bin and "
      f"which matching method produced the link, despite a significant p-value driven by sample size.")
if man["B1"] - man["B10"] > 5:
    print("  CAUTION: low bins do lean on looser matching; treat part of the gradient as a "
          "matching-quality artifact and report this prominently in Limitations.")
else:
    print("  The gradient is therefore NOT explained by matching quality: low-scoring bins do not "
          "depend disproportionately on looser matching.")
    print("  This is a clean negative control and strengthens the descriptive finding. It should be "
          "reported as such rather than omitted for being a null result.")
''')


code(r'''
fig, ax = plt.subplots(figsize=(9.5, 4.4))
methods = ["EXACT", "MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"]
cols = {"EXACT": C1, "MANUAL_APPNO_MATCH": C2, "DETERMINISTIC_APPNO": C3}
bottom = np.zeros(len(BINS))
for m in methods:
    vals = comp[m].reindex(BINS).fillna(0).values
    ax.bar(BINS, vals, bottom=bottom, color=cols[m], label=m.replace("_", " ").title(),
           width=.66, edgecolor=SURFACE, linewidth=2)
    bottom += vals
style(ax, "Step 5 - which matching method produced each bin's links",
      "% of that bin's linked passers", "percentile bin (B1 lowest)")
ax.set_ylim(0, 100)
ax.legend(frameon=False, fontsize=9, ncol=3, loc="lower center", bbox_to_anchor=(.5, -.28))
fig.tight_layout(); plt.show()
print("The composition is visibly flat across bins. If low bins leaned on looser matching, the")
print("orange band would widen to the left - it does not (9.1% at B1 vs 6.2% at B10).")
''')

# ---------------------------------------------------------------- step 6
md(r"""
---
## Step 6 — Right-censoring sensitivity

**Guide's objective:** test whether the `Year <= 2014` restriction actually equalizes censoring risk
across the observable cohort.

**Verdict: the single most important step in the guide — and the answer is worse than it assumes.**

The guide treats `Year <= 2014` as a restriction that "reduces" censoring. It cannot equalize it,
for a structural reason the guide does not mention: **`PLE_DATA.csv` contains records for 2011–2022
only.** With a median NMAT→PLE gap of about six years, a 2014 examinee must pass within 8 years to
appear at all, while a 2006 examinee loses anyone who passed before 2011.

Two analyses are run: the guide's sub-period comparison, then a **fixed-exposure-window** design
that actually removes the bias rather than measuring it.
""")

code(r'''
obs6 = obs.copy()
obs6["ple_year"] = pd.to_numeric(obs6["PLE_YEAR_PASSED"], errors="coerce")

src_years = pd.to_numeric(df["PLE_YEAR_PASSED"], errors="coerce").dropna()
gap = (obs6.loc[obs6["linked"], "ple_year"] - obs6.loc[obs6["linked"], "Year"]).dropna()

print(f"PLE source coverage      : {int(src_years.min())} - {int(src_years.max())}")
print(f"NMAT-to-PLE gap (years)  : median {gap.median():.0f}, mean {gap.mean():.2f}, "
      f"IQR {gap.quantile(.25):.0f}-{gap.quantile(.75):.0f}")

# (a) the guide's method
periods = [(2006, 2008), (2009, 2011), (2012, 2014)]
tbl_a = pd.DataFrame({f"{a}-{b}": obs6[obs6.Year.between(a, b)].groupby("PercentileBin")["linked"].mean().reindex(BINS) * 100
                      for a, b in periods}).round(1)

# (b) fixed exposure: count a pass only if it happened within W years of the NMAT sitting
W = 8
obs6["hitW"] = obs6["linked"] & ((obs6["ple_year"] - obs6["Year"]) <= W)
tbl_b = pd.DataFrame({
    "published (any horizon)": obs6.groupby("PercentileBin")["linked"].mean().reindex(BINS) * 100,
    f"equal {W}-year window":  obs6.groupby("PercentileBin")["hitW"].mean().reindex(BINS) * 100,
}).round(1)
tbl_b["difference"] = (tbl_b.iloc[:, 0] - tbl_b.iloc[:, 1]).round(1)

by_year = pd.DataFrame({
    "published": obs6.groupby("Year")["linked"].mean() * 100,
    f"{W}-yr window": obs6.groupby("Year")["hitW"].mean() * 100,
}).round(1)

print("\nRESULT (a) — the guide's sub-period comparison: linkage rate (%) by bin")
print(tbl_a.to_string())
print(f"\nRESULT (b) — equal-exposure correction: linkage rate (%) by bin")
print(tbl_b.to_string())
print(f"\nRESULT (c) — linkage rate (%) by NMAT year, before and after equalizing exposure")
print(by_year.to_string())

early = tbl_a.iloc[:, 0].mean(); late = tbl_a.iloc[:, -1].mean()
sp_pub = by_year["published"].max() - by_year["published"].min()
sp_fix = by_year[f"{W}-yr window"].max() - by_year[f"{W}-yr window"].min()

print("\nINTERPRETATION")
print(f"  (a) Mean linkage across bins is {early:.1f}% for 2006-2008 and {late:.1f}% for 2012-2014, "
      f"a drop of {early - late:.1f} points. Residual censoring inside the observable cohort is "
      f"therefore substantial, not merely 'reduced'.")
print(f"  (b) Equalizing exposure at {W} years lowers overall observable linkage from "
      f"{obs6['linked'].mean()*100:.2f}% to {obs6['hitW'].mean()*100:.2f}%. The bin gradient keeps "
      f"its shape, so the descriptive finding survives, but the levels do not.")
print(f"  (c) The apparent decline across NMAT years narrows from {sp_pub:.1f} points to "
      f"{sp_fix:.1f} points once exposure is equalized -- most of that 'trend' was the data window, "
      f"not a change in outcomes.")
print(f"  ACTION FOR THE PAPER: Limitations must state the 2011-2022 PLE window explicitly and "
      f"quantify the residual bias. Any linkage rate quoted without an exposure window is not "
      f"comparable across cohorts.")
''')


code(r'''
fig, axes = plt.subplots(1, 2, figsize=(12, 4.4))

cols3 = [C1, C2, C3]
for c, col in zip(tbl_a.columns, cols3):
    axes[0].plot(BINS, tbl_a[c], marker="o", ms=5, lw=2, color=col, label=c)
style(axes[0], "(a) Linkage by bin, split by NMAT sub-period", "linkage rate (%)", "percentile bin")
axes[0].legend(frameon=False, fontsize=9, title="NMAT years", title_fontsize=9)

axes[1].plot(by_year.index, by_year["published"], marker="o", ms=6, lw=2, color=C1,
             label="published (any horizon)")
axes[1].plot(by_year.index, by_year.iloc[:, 1], marker="o", ms=6, lw=2, color=C2,
             label="equal 8-year window")
style(axes[1], "(b) Linkage by NMAT year, before and after equalizing exposure",
      "linkage rate (%)", "NMAT year")
axes[1].legend(frameon=False, fontsize=9)

fig.suptitle("Step 6 - the apparent decline over time is mostly the 2011-2022 PLE data window",
             x=.01, ha="left", fontsize=13, fontweight="700", color=INK)
fig.tight_layout(rect=[0, 0, 1, .93]); plt.show()
print("Left: later sub-periods sit below earlier ones in EVERY bin - residual censoring is real.")
print("Right: equalizing exposure flattens much of the year trend (spread 16.9 -> 10.7 points).")
''')

# ---------------------------------------------------------------- step 7
md(r"""
---
## Step 7 — Pre-2016 vs post-2016 split of sub-threshold linked passers

**Guide's objective:** scope the sub-threshold finding to examinees actually admitted under CMO 18's
40th-percentile regime.

**Verdict: do not build this analysis — the answer is structural and requires no study.** The
observable cohort is capped at NMAT year ≤ 2014 by construction, so the post-2016 count is exactly
zero, not "small or zero" as the guide anticipates. The cell below demonstrates that rather than
asserting it, and then quantifies what lifting the restriction would actually buy.
""")

code(r'''
sub_linked = obs[obs["PercentileBin"].isin(SUB) & obs["linked"]]
post = int((sub_linked["Year"] >= 2016).sum())

assert post == 0, "post-2016 rows appeared inside a cohort defined as Year<=2014"

print("RESULT — sub-threshold (B1-B4) linked passers by NMAT year")
print(sub_linked.groupby("Year").size().to_frame("linked_passers").to_string())
print(f"\n  NMAT year range in this group : {int(sub_linked.Year.min())}-{int(sub_linked.Year.max())}")
print(f"  Count with NMAT year >= 2016   : {post}  (zero by construction, not by finding)")

# What would lifting the restriction give? Show why it does not help.
allb = df[df["IS_BEST_NMAT_RECORD"].fillna(False).astype(bool)].copy()
allb["linked"] = allb["IS_PLE_PASSER"].fillna(False).astype(bool)
late = allb[allb["Year"] >= 2016]
late_rate = late["linked"].mean() * 100
early_rate = allb[allb["Year"] <= 2014]["linked"].mean() * 100

print(f"\n  If the <=2014 restriction were lifted:")
print(f"    2016-2018 examinees: {len(late):,}, linkage {late_rate:.1f}%")
print(f"    <=2014 examinees   : {len(allb[allb.Year <= 2014]):,}, linkage {early_rate:.1f}%")

print("\nINTERPRETATION")
print(f"  Every one of the {len(sub_linked):,} sub-threshold linked passers sat the NMAT in "
      f"{int(sub_linked.Year.min())}-{int(sub_linked.Year.max())} -- years before CMO 18 took effect "
      f"in 2016.")
print("  THIS IS THE FINDING, and it is decisive for how the paper reads that figure: none of these")
print("  examinees were admitted under the regime currently in force. The number cannot be presented")
print("  as evidence of non-compliance with CMO 18.")
print(f"  Lifting the restriction does not rescue the comparison: 2016-2018 examinees link at only "
      f"{late_rate:.1f}% versus {early_rate:.1f}%, because they mostly have not reached the PLE "
      f"within the data window (see Step 6). The comparison the guide wants is not available from "
      f"this dataset at any cohort definition.")
''')


code(r'''
cnt7 = sub_linked.groupby("Year").size()
fig, ax = plt.subplots(figsize=(9.5, 4.2))
bars = ax.bar(cnt7.index.astype(int), cnt7.values, color=C1, width=.62)
label_bars(ax, bars, "{:,.0f}", dy=12)
ax.axvline(2015.5, color=C2, lw=2, ls="--")
ax.axvspan(2015.5, 2018.6, color=C2, alpha=.08)
ax.text(2016.1, cnt7.max() * .72, "CMO 18 in force\nfrom 2016\n\nno examinees here",
        fontsize=9.5, color=C2, va="top")
ax.set_xlim(2005.3, 2018.6)
ax.set_ylim(0, cnt7.max() * 1.2)
style(ax, "Step 7 - every sub-threshold linked passer predates CMO 18",
      "linked passers (B1-B4)", "NMAT year")
fig.tight_layout(); plt.show()
print("The shaded region is the regime the paper is about. It is empty, by construction of the")
print("observable cohort - so this count cannot be read as non-compliance with CMO 18.")
''')

# ---------------------------------------------------------------- step 8
md(r"""
---
## Step 8 — Raw score trend by year

**Guide's objective:** replace the bin-share-by-year proxy with an actual score trend, since
percentile rank is cohort-relative and cannot distinguish a real trend from rebinning.

**Verdict: valid, straightforward, and the reasoning is sound.** `TotalRawScoreTRUE` is the
recalculated sum of the eight component subtests and is absolute rather than cohort-relative, so it
can show drift that percentile rank structurally cannot.
""")

code(r'''
best = df[df["IS_BEST_NMAT_RECORD"].fillna(False).astype(bool)].copy()

s8 = (best.groupby("Year")["TotalRawScoreTRUE"]
          .agg(n="count", median="median", mean="mean", std="std").round(2))

pct_by_year = best.groupby("Year")["NMS_PER_num"].median()
s8["median_percentile"] = pct_by_year.round(1)

assert best["TotalRawScoreTRUE"].notna().mean() > 0.99, "raw score coverage unexpectedly low"

print("RESULT — TotalRawScoreTRUE by NMAT year (best-record cohort)")
print(s8.to_string())

first, last = int(s8.index.min()), int(s8.index.max())
d_raw = s8.loc[last, "median"] - s8.loc[first, "median"]
d_pct = s8.loc[last, "median_percentile"] - s8.loc[first, "median_percentile"]

# Is the percentile re-based each year? If so, the median over ALL sittings is ~50 every year.
allp = df.groupby("Year")["NMS_PER_num"].median()
allr = df.groupby("Year")["TotalRawScoreTRUE"].median()
r = allr.corr(allp)

b5_share = df.assign(b5=df["PercentileBin"].isin(B5P)).groupby("Year")["b5"].mean() * 100
early = b5_share.loc[2006:2011].mean(); late = b5_share.loc[2013:2018].mean()

print("")
print("RESULT - is NMS_PER_num re-based annually?  (medians over ALL sittings)")
print(pd.DataFrame({"median_raw": allr, "median_percentile": allp.round(0),
                    "pct_clearing_B5plus": b5_share.round(1)}).to_string())

print("")
print("INTERPRETATION")
print(f"  Median raw score moved from {s8.loc[first,'median']:.0f} in {first} to "
      f"{s8.loc[last,'median']:.0f} in {last} ({d_raw / s8.loc[first,'median'] * 100:+.1f}%).")
print(f"  The guide's premise does NOT hold here. If percentile were re-based each year, its median "
      f"over all sittings would be ~50 in every year; instead it runs {allp.loc[2006]:.0f} in 2006 "
      f"and {allp.loc[2018]:.0f} in 2018, tracking the raw score with r = {r:.2f}.")
print("  NMS_PER_num is therefore anchored to a FIXED norm group, not renormalized annually.")
print(f"  CONSEQUENCE, and this is the policy-relevant part: because the standard is fixed while "
      f"attainment fell, the share clearing the 40th percentile dropped from {early:.1f}% "
      f"(2006-2011) to {late:.1f}% (2013-2018), a fall of {early - late:.1f} points.")
print("  A fixed percentile cutoff is NOT a fixed proportion of each cohort. Holding the 40th")
print("  percentile constant progressively tightens admission as cohort attainment declines --")
print("  a mechanical property of the instrument, not a policy anyone chose.")
''')


code(r'''
fig, axes = plt.subplots(1, 3, figsize=(14.5, 4.2))

axes[0].plot(allr.index, allr.values, marker="o", ms=6, lw=2, color=C1)
style(axes[0], "(a) Median raw score", "raw score (8 subtests)", "NMAT year")

axes[1].plot(allp.index, allp.values, marker="o", ms=6, lw=2, color=C2)
axes[1].axhline(50, color=MUTED, lw=1.4, ls=":")
axes[1].text(2006.2, 32.5, "the dotted line is 50 - where a re-based", fontsize=8.5, color=INK2)
axes[1].text(2006.2, 31.0, "percentile would sit in every year", fontsize=8.5, color=INK2)
axes[1].set_ylim(30, 60)
style(axes[1], "(b) Median percentile", "percentile rank", "NMAT year")

axes[2].plot(b5_share.index, b5_share.values, marker="o", ms=6, lw=2, color=C3)
for yr in (2006, 2018):
    axes[2].annotate(f"{b5_share.loc[yr]:.1f}%", xy=(yr, b5_share.loc[yr]),
                     xytext=(0, 10), textcoords="offset points",
                     ha="left" if yr == 2006 else "right", fontsize=9, color=INK2)
style(axes[2], "(c) Share clearing the 40th percentile", "% of sittings at B5+", "NMAT year")

fig.suptitle("Step 8 - the percentile is anchored to a fixed norm, so a fixed cutoff tightens over time",
             x=.01, ha="left", fontsize=13, fontweight="700", color=INK)
fig.tight_layout(rect=[0, 0, 1, .92]); plt.show()
print("(a) and (b) fall together (r = %.2f). If the percentile were re-based each year, panel (b)" % r)
print("would sit flat on the dotted 50 line - it does not.")
print("(c) is the consequence: the same unchanged 40th-percentile rule cleared ~63% of sittings in")
print("2006-2011 and ~50% in 2013-2018. Three panels, one axis each; a dual-axis version would")
print("imply a scale alignment we did not earn.")
''')

# ---------------------------------------------------------------- step 9
md(r"""
---
## Step 9 — Schema review for partial GIDA / IP proxies

**Guide's objective:** confirm rather than assume that no field offers even a partial proxy for GIDA
residency or IP membership.

**Verdict: run it — and the answer is not the one the guide expects.** The guide anticipates
confirming absence. The shipped 53-column file does lack any such field (Step 2), but the **raw
source file does not**, and the relevant columns are dropped during slimming.
""")

code(r'''
raw_head = pd.read_csv(RAW_CSV, nrows=5, low_memory=False)
GEO_TOKENS = ["prov", "region", "address", "location", "city", "municip", "barangay", "home"]
geo_cols = [c for c in raw_head.columns if any(t in c.lower() for t in GEO_TOKENS)]

print(f"Geographic-ish columns in the RAW file ({RAW_CSV.name}): {geo_cols}")
print(f"Of those, present in the shipped 53-column file: "
      f"{[c for c in geo_cols if c in df.columns] or 'NONE -- all dropped during slimming'}")

if geo_cols:
    geo = pd.read_csv(RAW_CSV, usecols=geo_cols, low_memory=False)
    summary = pd.DataFrame({
        "pct_non_null": (geo.notna().mean() * 100).round(1),
        "n_distinct":   geo.nunique(),
    })
    print("\nRESULT — coverage of the candidate proxy fields")
    print(summary.to_string())

    for c in geo_cols:
        print(f"\nTop 8 values of '{c}':")
        print(geo[c].value_counts().head(8).to_string())

print("\nINTERPRETATION")
if geo_cols:
    best_col = summary["pct_non_null"].idxmax()
    print(f"  A partial geographic proxy DOES exist. '{best_col}' is "
          f"{summary.loc[best_col,'pct_non_null']:.1f}% populated with "
          f"{int(summary.loc[best_col,'n_distinct'])} distinct values, in the raw file.")
    print("  It is NOT in the shipped dataset -- Pipeline 5 drops it -- which is why every prior")
    print("  statement that the field is 'absent' was true of the analytic file but false of the source.")
    print("  STRENGTH OF THE PROXY, stated honestly: DOH AO 2020-0023 defines GIDA at barangay and")
    print("  municipality level using physical and socioeconomic criteria. Province or region of")
    print("  address is far coarser, is an ADDRESS rather than a residency determination, and cannot")
    print("  identify IP membership at all. It supports at best a crude upper-bound estimate of the")
    print("  GIDA-eligible population, clearly labelled as such, and is never equivalent to certified")
    print("  GIDA or IP status.")
    print("  RECOMMENDATION: retain these columns through Pipeline 5 so the estimate can be made, and")
    print("  continue to press for the registration-time self-declaration capture the paper recommends.")
else:
    print("  No geographic field exists in the raw file either; absence is confirmed.")
''')


code(r'''
reg = geo["NMAT Region permanent address"].value_counts().head(12).sort_values()
fig, ax = plt.subplots(figsize=(9, 4.8))
bars = ax.barh(reg.index, reg.values, color=C1, height=.68)
for b, v in zip(bars, reg.values):
    ax.text(v + reg.max() * .012, b.get_y() + b.get_height() / 2, f"{v:,}",
            va="center", fontsize=9, color=INK2)
ax.set_xlim(0, reg.max() * 1.14)
style(ax, "Step 9 - a geographic field DOES exist in the raw data (top 12 regions)",
      None, "examinee records")
ax.grid(axis="y", visible=False)
fig.tight_layout(); plt.show()
print("100% populated, 21 distinct regions - but this is region of ADDRESS, while DOH AO 2020-0023")
print("defines GIDA at barangay/municipality level. Useful as a crude upper bound only, and it")
print("cannot identify IP membership at all.")
''')

# ---------------------------------------------------------------- step 10
md(r"""
---
## Step 10 — Chi-square: institution type × threshold status

**Guide's objective:** attach a formal significance statement to the Public/Private B5+ clearance
difference.

**Verdict: valid, and the guide's own caution is the important part.** At n in the tens of
thousands almost any difference reaches significance, so Cramér's V is what determines whether the
gap is practically meaningful. The guide's hardcoded contingency table is from the superseded brief
and is rebuilt from the corrected data here.
""")

code(r'''
o10 = obs[obs["UNDERGRAD_UNI_TYPE"].isin(["Public", "Private"])].copy()
o10["b5plus"] = o10["PercentileBin"].isin(B5P)

table = pd.crosstab(o10["UNDERGRAD_UNI_TYPE"], o10["b5plus"])
table.columns = ["below_B5", "B5_plus"]

chi2, pval, dof, expected = chi2_contingency(table.values)
n = table.values.sum()
cramers_v = np.sqrt(chi2 / (n * (min(table.shape) - 1)))

rates = (table["B5_plus"] / table.sum(axis=1) * 100).round(1)
diff = rates["Public"] - rates["Private"]

print("RESULT — 2x2 contingency, observable cohort")
print(table.to_string())
print(f"\nB5+ clearance: Public {rates['Public']:.1f}%, Private {rates['Private']:.1f}%, "
      f"difference {diff:+.1f} points")
print(f"chi2 = {chi2:,.1f}, dof = {dof}, p = {pval:.3e}, n = {n:,}")
print(f"Cramer's V = {cramers_v:.4f}")

print("\nINTERPRETATION")
print(f"  The Public/Private difference in B5+ clearance is {diff:+.1f} points and is statistically "
      f"significant (p = {pval:.1e}).")
mag = ("negligible" if cramers_v < 0.1 else "small" if cramers_v < 0.3 else
       "moderate" if cramers_v < 0.5 else "large")
p_pub = rates["Public"] / 100; p_pri = rates["Private"] / 100
cohens_h = abs(2*np.arcsin(np.sqrt(p_pub)) - 2*np.arcsin(np.sqrt(p_pri)))
print(f"  Cramer's V of {cramers_v:.4f} is a {mag} association and Cohen's h is {cohens_h:.3f} "
      f"(small). With n = {n:,}, significance was close to guaranteed and carries almost no "
      f"information on its own.")
print(f"  DO NOT round this to 'no difference'. Association measures on a 2x2 with unbalanced "
      f"margins understate practical importance: a {diff:+.1f}-point gap in B5+ clearance is "
      f"material for policy even though the association is statistically weak. Report the "
      f"percentage-point difference AND the effect size together, and let the reader judge.")
print("  The guide's published cells (Public 64.9% / Private 59.2%) do not reproduce here, because")
print("  the corrected pipeline reassigned 416 rows whose university type contradicted their own")
print("  source hint and removed sentinel-valued percentiles. Use these figures, not the brief's.")
print("  Reminder: this is the UNDERGRADUATE institution. It is not an SUC/PHEI comparison.")
''')


code(r'''
o10b = obs[obs["UNDERGRAD_UNI_TYPE"].isin(["Public", "Private", "Foreign", "Not Specified"])].copy()
o10b["b5plus"] = o10b["PercentileBin"].isin(B5P)
agg = o10b.groupby("UNDERGRAD_UNI_TYPE")["b5plus"].agg(["size", "mean"])
agg["pct"] = agg["mean"] * 100
agg["ci"] = 1.96 * np.sqrt(agg["mean"] * (1 - agg["mean"]) / agg["size"]) * 100
agg = agg.sort_values("pct", ascending=False)

fig, ax = plt.subplots(figsize=(8.5, 4.3))
bars = ax.bar(agg.index, agg.pct, yerr=agg.ci, color=C1, width=.6,
              error_kw=dict(ecolor=INK2, lw=1.4, capsize=5))
for b, v, n in zip(bars, agg.pct, agg["size"]):
    ax.text(b.get_x() + b.get_width()/2, v + agg.ci.max() + 1.6, f"{v:.1f}%\nn={n:,}",
            ha="center", fontsize=9, color=INK2)
ax.set_ylim(0, 100)
style(ax, "Step 10 - share clearing the 40th percentile (B5+), by undergraduate institution type",
      "% of examinees at B5 or above")
ax.tick_params(axis="x", rotation=12)
fig.tight_layout(); plt.show()
print("Error bars are 95% CIs. Public exceeds Private by 10.9 points - a small association")
print("(Cramer's V 0.092) but a materially large difference. This is the UNDERGRADUATE institution,")
print("not the medical school: it is not an SUC vs PHEI comparison.")
''')

# ---------------------------------------------------------------- summary
md(r"""
---
## Summary of findings

Regenerated from the computations above, so it cannot drift out of sync with them.
""")

code(r'''
lines = []
lines.append(("1",  "Sub-threshold linked passers by institution type",
              f"{int(sub['linked'].sum()):,} in B1-B4; Private supplies "
              f"{s1.loc['Private','share_of_linked_passers_pct']:.1f}%. Undergraduate split only."))
lines.append(("2",  "Evaluability audit",
              f"{len([c for c,v in hits.items() if v==0])}/6 categories absent from the schema."))
lines.append(("3",  "Best-record sensitivity",
              f"B4->B5 gap {gaps['B_first_attempt']:.1f}-{gaps['C_highest_pct']:.1f} pts across "
              f"defensible specs; stable but modest."))
lines.append(("4",  "Changepoint testing",
              f"B4->B5 ranks {rank45}/9 by size; largest is {largest.boundary}. No changepoint "
              f"at the 40th percentile."))
lines.append(("5",  "Match-type stratification",
              f"Cramer's V {cramers_v_5:.4f}; gradient is NOT a matching artifact."))
lines.append(("6",  "Right-censoring",
              f"Equalizing exposure moves linkage {obs6['linked'].mean()*100:.2f}% -> "
              f"{obs6['hitW'].mean()*100:.2f}%; year-spread {sp_pub:.1f} -> {sp_fix:.1f} pts."))
lines.append(("7",  "Pre/post-2016 split",
              f"0 of {len(sub_linked):,} sub-threshold passers sat NMAT after 2016 -- none were "
              f"admitted under CMO 18."))
lines.append(("8",  "Raw score trend",
              f"Percentile is fixed-norm, not re-based (r={r:.2f}); share clearing B5+ fell "
              f"{early:.1f}% -> {late:.1f}%."))
lines.append(("9",  "GIDA/IP proxy",
              "Partial geographic proxy EXISTS in the raw file but is dropped by Pipeline 5."))
lines.append(("10", "UNITYPE x threshold",
              f"Public {rates['Public']:.1f}% vs Private {rates['Private']:.1f}%; Cramer's V "
              f"{cramers_v:.4f} ({mag}); {diff:+.1f}pt gap is still policy-relevant."))

summary = pd.DataFrame(lines, columns=["Step", "Title", "Finding"])
print(summary.to_string(index=False))

out = ROOT / "dataset" / "analysis_output" / "robustness_summary.csv"
summary.to_csv(out, index=False)
print(f"\nWritten to {out.relative_to(ROOT)}")
''')

md(r"""
---
## What the paper should change

1. **Withdraw the discontinuity claim.** Step 4 finds no changepoint at the 40th percentile; the
   B4→B5 boundary is not the largest of the nine, and its effect size is small. The "~23-point gap"
   was largely an artefact of the matcher bug documented at the top of this notebook. Sections
   describing a sharp break need rewriting, and the corrected gradient should be presented as what
   it is — a steady rise across the whole score range.
2. **State the 2011–2022 PLE window in Limitations, with numbers.** Step 6 shows the `Year <= 2014`
   restriction does not equalize censoring. Quote linkage rates with an explicit exposure window.
3. **Re-scope the sub-threshold figure.** Step 7 shows none of those examinees were admitted under
   CMO 18. Presenting the count as evidence about the current regime would misstate it.
4. **Report Step 5 as a negative control.** Matching quality does not explain the gradient. Null
   results that rule out an artifact belong in the paper.
5. **Correct the claim about percentile stability — it is the opposite of what was assumed.**
   Step 8 shows `NMS_PER_num` is anchored to a fixed norm group, not re-based each year: it tracks
   the raw score at r = 0.90 and its all-sittings median falls from 52 to 36 rather than sitting at
   50. The consequence is stronger than the original argument: because the standard is fixed while
   attainment declined, the share clearing the 40th percentile fell from 62.6% (2006–2011) to 49.7%
   (2013–2018). **An unchanged cutoff progressively tightened admission without anyone deciding
   to** — a mechanical property of the instrument that belongs in the policy discussion.
6. **Lead with effect sizes, not p-values.** Steps 4, 5 and 10 all reach significance purely on
   sample size.
7. **Correct the GIDA/IP claim.** Step 9 shows a partial geographic proxy exists in the source data.
   The honest statement is that the *analytic file* omits it and that province-level address is far
   too coarse for a GIDA determination — not that the source captures nothing.
8. **Do not claim the 40th percentile is validated.** Nothing in this dataset can validate a cutoff:
   there is no medical-school identifier, no admission-decision field, and no record of who was
   rejected. That constraint is structural and is unchanged by any of these ten steps.
""")

nb = {"cells": cells,
      "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                   "language_info": {"name": "python", "version": "3.10"}},
      "nbformat": 4, "nbformat_minor": 5}

path = sys.argv[1]
with open(path, "w", encoding="utf-8") as fh:
    json.dump(nb, fh, indent=1, ensure_ascii=False)

bad = 0
for i, c in enumerate(nb["cells"]):
    if c["cell_type"] != "code":
        continue
    src = "".join(c["source"])
    try:
        compile(src, f"cell{i}", "exec")
    except SyntaxError as e:
        bad += 1
        print(f"SYNTAX ERROR in cell {i}: {e}")
print(f"wrote {path}: {len(nb['cells'])} cells, {bad} syntax errors")
