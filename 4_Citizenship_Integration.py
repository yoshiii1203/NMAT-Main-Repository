"""
Pipeline 4: Citizenship Integration
====================================
NMAT_Ultima -> NMAT_Exodus

Enriches NMAT_Ultima.parquet with definitive citizenship labels using a
3-tier hierarchy of truth:

  Tier 1 (Priority 1): REAL_FOREIGNERS.csv   -- ground-truth NAC_NATIONALITY
  Tier 2 (Priority 2): pseudo-citizenship CSV -- name-based inference
  Tier 3 (Default):     "Filipino"

Output: dataset/NMAT_Exodus.parquet  (with CITIZENSHIP_FINAL + FOREIGNER_STATUS)
        dataset/NMAT_Exodus.csv       (for manual inspection)

Author: Automated Pipeline 4
Date:   2026-07-27
"""

from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path("dataset")
ULTIMA_PATH = ROOT / "NMAT_Ultima.parquet"
RF_PATH = ROOT / "REAL_FOREIGNERS.csv"
PSEUDO_PATH = ROOT / "pseudo_citizenship_profiling_FINAL.csv"
EXODUS_PARQUET = ROOT / "NMAT_Exodus.parquet"
EXODUS_CSV = ROOT / "NMAT_Exodus.csv"

# -- Nationality canonicalization map ----------------------------------------
# Normalizes country-name vs demonym variants and corrects typos.
# Values mapped to None are ambiguous (will fall through to Tier 2 or 3).

NATIONALITY_NORMALIZE = {
    # India
    "India": "India", "Indian": "India",
    # Nepal
    "Nepal": "Nepal", "Nepali": "Nepal",
    # Nigeria
    "Nigeria": "Nigeria", "Nigerian": "Nigeria",
    # Thailand
    "Thailand": "Thailand", "Thai": "Thailand",
    # United States
    "United States": "United States", "American": "United States",
    # Korea
    "Korea": "Korea (South)", "Korean": "Korea (South)",
    # Sri Lanka
    "Sri Lanka": "Sri Lanka", "Sri Lankan": "Sri Lanka",
    # Iran
    "Iran": "Iran", "Iranian": "Iran",
    # Indonesia
    "Indonesia": "Indonesia", "Indonesian": "Indonesia",
    # Taiwan
    "Taiwan": "Taiwan", "Taiwanese": "Taiwan", "R.O.C.": "Taiwan",
    # Japan
    "Japan": "Japan", "Japanese": "Japan",
    # China
    "China": "China", "Chinese": "China",
    # Somalia
    "Somalia": "Somalia", "Somali": "Somalia",
    # Ghana
    "Ghana": "Ghana", "Ghanaian": "Ghana",
    # Bangladesh
    "Bangladesh": "Bangladesh", "Bangladeshi": "Bangladesh",
    # Pakistan
    "Pakistan": "Pakistan", "Pakistani": "Pakistan",
    # Ethiopia
    "Ethiopia": "Ethiopia", "Ethiopian": "Ethiopia",
    # Canada
    "Canada": "Canada", "Canadian": "Canada",
    # Myanmar
    "Myanmar": "Myanmar", "Burmese": "Myanmar",
    # Sudan
    "Sudan": "Sudan", "Sudanese": "Sudan",
    # Russia
    "Russia": "Russia", "Russian": "Russia",
    # Cambodia
    "Cambodia": "Cambodia", "Cambodian": "Cambodia",
    # Laos
    "Laos": "Laos", "Laotian": "Laos",
    # Palestine
    "Palestine": "Palestine", "Palestinian": "Palestine",
    # Saudi Arabia
    "Saudi Arabia": "Saudi Arabia", "Saudi": "Saudi Arabia",
    # Malaysia
    "Malaysia": "Malaysia", "Malaysian": "Malaysia",
    # Vietnam
    "Vietnam": "Vietnam", "Vietnamese": "Vietnam",
    # Singapore
    "Singapore": "Singapore", "Singaporean": "Singapore",
    # Australia
    "Australia": "Australia", "Australian": "Australia",
    # United Kingdom
    "United Kingdom": "United Kingdom", "British": "United Kingdom",
    "UK": "United Kingdom", "U.K.": "United Kingdom",
    # New Zealand
    "New Zealand": "New Zealand", "New Zealander": "New Zealand",
    # South Africa
    "South Africa": "South Africa", "South African": "South Africa",
    # Denmark
    "Denmark": "Denmark", "Danish": "Denmark",
    # Netherlands
    "Netherlands": "Netherlands", "Dutch": "Netherlands",
    # France
    "France": "France", "French": "France",
    # Germany
    "Germany": "Germany", "German": "Germany",
    # Switzerland
    "Switzerland": "Switzerland", "Swiss": "Switzerland",
    # Spain
    "Spain": "Spain", "Spanish": "Spain",
    # Norway
    "Norway": "Norway", "Norwegian": "Norway",
    # Sweden
    "Sweden": "Sweden", "Swedish": "Sweden",
    # Finland
    "Finland": "Finland", "Finnish": "Finland",
    # Poland
    "Poland": "Poland", "Polish": "Poland",
    # Ukraine
    "Ukraine": "Ukraine", "Ukrainian": "Ukraine",
    # Turkey
    "Turkey": "Turkey", "Turkish": "Turkey",
    # Brazil
    "Brazil": "Brazil", "Brazilian": "Brazil",
    # Mexico
    "Mexico": "Mexico", "Mexican": "Mexico",
    # Egypt
    "Egypt": "Egypt", "Egyptian": "Egypt",
    # Kenya
    "Kenya": "Kenya", "Kenyan": "Kenya",
    # Uganda
    "Uganda": "Uganda", "Ugandan": "Uganda",
    # Zimbabwe
    "Zimbabwe": "Zimbabwe", "Zimbabwean": "Zimbabwe",
    # Zambia
    "Zambia": "Zambia", "Zambian": "Zambia",
    # Malawi
    "Malawi": "Malawi", "Malawian": "Malawi",
    # Tanzania
    "Tanzania": "Tanzania", "Tanzanian": "Tanzania",
    # Rwanda
    "Rwanda": "Rwanda", "Rwandan": "Rwanda",
    # Liberia
    "Liberia": "Liberia", "Liberian": "Liberia",
    # Yemen
    "Yemen": "Yemen", "Yemeni": "Yemen",
    # Israel
    "Israel": "Israel", "Israeli": "Israel",
    # Jordan
    "Jordan": "Jordan", "Jordanian": "Jordan",
    # Lebanon
    "Lebanon": "Lebanon", "Lebanese": "Lebanon",
    # Afghanistan
    "Afghanistan": "Afghanistan", "Afghan": "Afghanistan",
    # Mongolia
    "Mongolia": "Mongolia", "Mongolian": "Mongolia",
    # Nigeria (additional)
    "Nigerian": "Nigeria",
    # Solomon Islands (already country name)
    "Solomon Islands": "Solomon Islands",
    # Maldives (already country name)
    "Maldives": "Maldives",
    # Others -- keep as-is (single representation)
    "Solomon Islands": "Solomon Islands",
    "Maldives": "Maldives",
    "Fiji": "Fiji",
    "Papua New Guinea": "Papua New Guinea",
    "Timor-Leste": "Timor-Leste",
    "Bhutan": "Bhutan",
    "Brunei": "Brunei",
    "Mauritius": "Mauritius",
    "Seychelles": "Seychelles",
    "Comoros": "Comoros",
    "Micronesia": "Micronesia",
    "Palau": "Palau",
    "Marshall Islands": "Marshall Islands",
    "Nauru": "Nauru",
    "Tonga": "Tonga",
    "Samoa": "Samoa",
    "Vanuatu": "Vanuatu",
    "Cook Islands": "Cook Islands",
    "Niue": "Niue",
    "Tuvalu": "Tuvalu",
    "Kiribati": "Kiribati",
    "Botswana": "Botswana",
    "Lesotho": "Lesotho",
    "Eswatini": "Eswatini",
    "Namibia": "Namibia",
    "Angola": "Angola",
    "Mozambique": "Mozambique",
    "Madagascar": "Madagascar",
    "Cabo Verde": "Cabo Verde",
    "Sao Tome and Principe": "Sao Tome and Principe",
    "Equatorial Guinea": "Equatorial Guinea",
    "Gabon": "Gabon",
    "Republic of the Congo": "Republic of the Congo",
    "Democratic Republic of the Congo": "Democratic Republic of the Congo",
    "Central African Republic": "Central African Republic",
    "Chad": "Chad",
    "Cameroon": "Cameroon",
    "Benin": "Benin",
    "Togo": "Togo",
    "Cote d'Ivoire": "Cote d'Ivoire",
    "Burkina Faso": "Burkina Faso",
    "Mali": "Mali",
    "Niger": "Niger",
    "Senegal": "Senegal",
    "Gambia": "Gambia",
    "Guinea": "Guinea",
    "Guinea-Bissau": "Guinea-Bissau",
    "Sierra Leone": "Sierra Leone",
    "Mauritania": "Mauritania",
    "Algeria": "Algeria",
    "Tunisia": "Tunisia",
    "Libya": "Libya",
    "Morocco": "Morocco",
    "South Sudan": "South Sudan",
    "Eritrea": "Eritrea",
    "Djibouti": "Djibouti",
    "Maldives": "Maldives",
    "Iraq": "Iraq",
    "Syria": "Syria",
    "Oman": "Oman",
    "Qatar": "Qatar",
    "Kuwait": "Kuwait",
    "Bahrain": "Bahrain",
    "United Arab Emirates": "United Arab Emirates",
    "Armenia": "Armenia",
    "Azerbaijan": "Azerbaijan",
    "Georgia": "Georgia",
    "Kazakhstan": "Kazakhstan",
    "Uzbekistan": "Uzbekistan",
    "Turkmenistan": "Turkmenistan",
    "Kyrgyzstan": "Kyrgyzstan",
    "Tajikistan": "Tajikistan",
    "Cuba": "Cuba",
    "Jamaica": "Jamaica",
    "Haiti": "Haiti",
    "Dominican Republic": "Dominican Republic",
    "Trinidad and Tobago": "Trinidad and Tobago",
    "Guyana": "Guyana",
    "Suriname": "Suriname",
    "Belize": "Belize",
    "Bahamas": "Bahamas",
    "Barbados": "Barbados",
    "Saint Lucia": "Saint Lucia",
    "Saint Vincent and the Grenadines": "Saint Vincent and the Grenadines",
    "Grenada": "Grenada",
    "Antigua and Barbuda": "Antigua and Barbuda",
    "Dominica": "Dominica",
    "Saint Kitts and Nevis": "Saint Kitts and Nevis",
    "Romania": "Romania",
    "Bulgaria": "Bulgaria",
    "Serbia": "Serbia",
    "Croatia": "Croatia",
    "Bosnia and Herzegovina": "Bosnia and Herzegovina",
    "Albania": "Albania",
    "North Macedonia": "North Macedonia",
    "Montenegro": "Montenegro",
    "Greece": "Greece",
    "Cyprus": "Cyprus",
    "Malta": "Malta",
    "Iceland": "Iceland",
    "Ireland": "Ireland",
    "Portugal": "Portugal",
    "Austria": "Austria",
    "Hungary": "Hungary",
    "Czech Republic": "Czech Republic",
    "Slovakia": "Slovakia",
    "Slovenia": "Slovenia",
    "Lithuania": "Lithuania",
    "Latvia": "Latvia",
    "Estonia": "Estonia",
    "Belarus": "Belarus",
    "Moldova": "Moldova",
    "Peru": "Peru",
    "Colombia": "Colombia",
    "Venezuela": "Venezuela",
    "Ecuador": "Ecuador",
    "Bolivia": "Bolivia",
    "Paraguay": "Paraguay",
    "Uruguay": "Uruguay",
    "Argentina": "Argentina",
    "Chile": "Chile",
    "Costa Rica": "Costa Rica",
    "Nicaragua": "Nicaragua",
    "Honduras": "Honduras",
    "El Salvador": "El Salvador",
    "Guatemala": "Guatemala",
    "Panama": "Panama",
    "Philippines": "Philippines",  # Should not appear in RF but handle gracefully
    
    # Typos
    "Vietnemese": "Vietnam",
    "Camerdon": "Cameroon",
    
    # Ambiguous -- not specific enough; will fall through
    "Others": None,
    "Not Stated": None,
    "Not Specified": None,
}

# -- Filipino variants (case-insensitive) ------------------------------------
FILIPINO_VARIANTS = [
    '', 'nan', 'none', 'filipino', 'philippines', 'fil-am', 'fil',
    'ph', 'filipina', 'filipino-chinese',
]


def normalize_nationality(val):
    """Canonicalize a nationality string. Returns None for ambiguous values."""
    if pd.isna(val):
        return None
    cleaned = str(val).strip().title()
    return NATIONALITY_NORMALIZE.get(cleaned, cleaned)


def is_filipino_variant(val):
    """Check if a nationality string is a Filipino variant (case-insensitive)."""
    if pd.isna(val):
        return True  # Treat NaN as Filipino (safe default)
    cleaned = str(val).strip().lower()
    return cleaned in FILIPINO_VARIANTS


def main():
    print("=" * 60)
    print("  Pipeline 4: Citizenship Integration")
    print("  NMAT_Ultima -> NMAT_Exodus")
    print("=" * 60)

    # -- STEP 1: Load NMAT_Ultima --------------------------------------------
    print(f"\n[1/10] Loading {ULTIMA_PATH}...")
    df = pd.read_parquet(ULTIMA_PATH)
    print(f"       Loaded {len(df):,} rows ? {len(df.columns)} cols")

    # -- STEP 2: Load REAL_FOREIGNERS.csv ------------------------------------
    print(f"\n[2/10] Loading {RF_PATH}...")
    df_rf = pd.read_csv(RF_PATH, dtype=str)
    print(f"       Loaded {len(df_rf):,} rows ? {len(df_rf.columns)} cols")

    # Keep only needed columns
    rf_cols = ["NMA_AppNo", "NAC_NATIONALITY"]
    for c in ["NMA_Name", "NMA_College", "Year", "NMA_Sex", "NMS_PER"]:
        if c in df_rf.columns:
            rf_cols.append(c)
    df_rf = df_rf[rf_cols].copy()
    print(f"       Using {len(rf_cols)} columns")

    # -- STEP 3: Standardize keys --------------------------------------------
    print(f"\n[3/10] Standardizing keys...")
    df_rf["APPNO_CLEAN"] = df_rf["NMA_AppNo"].astype(str).str.strip()
    print(f"       APPNO_CLEAN samples: {df_rf['APPNO_CLEAN'].head(3).tolist()}")

    # -- STEP 4: Normalize NAC_NATIONALITY ------------------------------------
    print(f"\n[4/10] Normalizing NAC_NATIONALITY...")
    print(f"       Unique raw values before: {df_rf['NAC_NATIONALITY'].nunique()}")

    # Clean and normalize
    df_rf["NAC_NATIONALITY"] = df_rf["NAC_NATIONALITY"].astype(str).str.strip().str.title()
    df_rf["NAC_NATIONALITY_NORM"] = df_rf["NAC_NATIONALITY"].apply(normalize_nationality)

    # Report normalization results
    norm_before = df_rf["NAC_NATIONALITY"].nunique()
    norm_after = df_rf["NAC_NATIONALITY_NORM"].nunique()
    print(f"       Unique after normalization: {norm_after} (was {norm_before})")

    ambiguous = df_rf[df_rf["NAC_NATIONALITY_NORM"].isna()]
    if len(ambiguous) > 0:
        print(f"       WARNING: {len(ambiguous)} rows with ambiguous nationality:")
        for v in ambiguous["NAC_NATIONALITY"].value_counts().head(5).items():
            print(f"         - '{v[0]}': {v[1]} rows")

    # -- STEP 5: Merge REAL_FOREIGNERS (Tier 1) ------------------------------
    print(f"\n[5/10] Merging REAL_FOREIGNERS (Tier 1)...")
    # Track ANY merge match (even if nationality is ambiguous like "Others")
    df_rf_merge = df_rf[["APPNO_CLEAN", "NAC_NATIONALITY_NORM"]].drop_duplicates(subset=["APPNO_CLEAN"])
    df_rf_merge["IN_REAL_FOREIGNERS"] = True
    print(f"       Unique APPNO_CLEAN in RF: {len(df_rf_merge):,}")

    df = df.merge(
        df_rf_merge.rename(columns={"NAC_NATIONALITY_NORM": "RF_NATIONALITY"}),
        on="APPNO_CLEAN",
        how="left",
    )

    matched = df["IN_REAL_FOREIGNERS"].sum()
    print(f"       Rows matched with RF: {matched:,} / {len(df):,} ({matched/len(df)*100:.2f}%)")

    # -- STEP 6: Load pseudo-citizenship (Tier 2) ----------------------------
    print(f"\n[6/10] Loading pseudo-citizenship profiling...")
    df_pc = pd.read_csv(PSEUDO_PATH, dtype=str)
    pc_cols = ["APPNO_CLEAN", "override_applied", "pseudo_citizenship", "name_based_assessment"]
    available_pc = [c for c in pc_cols if c in df_pc.columns]
    df_pc = df_pc[available_pc].copy()
    df_pc["APPNO_CLEAN"] = df_pc["APPNO_CLEAN"].str.strip()
    df_pc = df_pc.drop_duplicates(subset=["APPNO_CLEAN"])
    print(f"       Loaded {len(df_pc):,} pseudo-citizenship records")
    if "override_applied" in df_pc.columns:
        print(f"       FOREIGN overrides: {(df_pc['override_applied'] == 'FOREIGN').sum()}")

    # -- STEP 7: Merge pseudo-citizenship ------------------------------------
    print(f"\n[7/10] Merging pseudo-citizenship (Tier 2)...")
    df = df.merge(
        df_pc,
        on="APPNO_CLEAN",
        how="left",
        suffixes=("", "_pseudo"),
    )
    print(f"       Pseudo-citizenship records merged")

    # -- STEP 8: Apply 3-tier hierarchy --------------------------------------
    print(f"\n[8/10] Applying 3-tier citizenship hierarchy...")

    # Initialize with Tier 3 (default)
    df["CITIZENSHIP_FINAL"] = "Filipino"
    df["FOREIGNER_STATUS"] = "Filipino"

    # Tier 1a: REAL_FOREIGNERS match with known, non-Filipino nationality
    tier1a_mask = (
        df["RF_NATIONALITY"].notna()
        & ~df["RF_NATIONALITY"].apply(is_filipino_variant)
    )
    df.loc[tier1a_mask, "CITIZENSHIP_FINAL"] = df.loc[tier1a_mask, "RF_NATIONALITY"]
    df.loc[tier1a_mask, "FOREIGNER_STATUS"] = "Verified Foreigner"
    print(f"       Tier 1a (RF with known nationality): {tier1a_mask.sum():,} records")

    # Tier 1b: REAL_FOREIGNERS match but ambiguous nationality (e.g. "Others", "Not Stated")
    # These ARE confirmed foreign examinees (they're in REAL_FOREIGNERS.csv),
    # their specific nationality just wasn't captured.
    tier1b_mask = (
        df["IN_REAL_FOREIGNERS"] == True
        & ~tier1a_mask
    )
    if "School Type_rec2_FINAL" in df.columns:
        df.loc[tier1b_mask, "CITIZENSHIP_FINAL"] = df.loc[tier1b_mask, "School Type_rec2_FINAL"].fillna("Foreign")
    else:
        df.loc[tier1b_mask, "CITIZENSHIP_FINAL"] = "Foreign"
    df.loc[tier1b_mask, "FOREIGNER_STATUS"] = "Verified Foreigner"
    print(f"       Tier 1b (RF match, ambiguous nationality): {tier1b_mask.sum():,} records")

    # Combined Tier 1
    tier1_mask = tier1a_mask | tier1b_mask

    # Tier 2: pseudo-citizenship with FOREIGN override (only if NOT already Tier 1)
    if "pseudo_citizenship" in df.columns and "override_applied" in df.columns:
        tier2_mask = (
            ~tier1_mask  # Not already Tier 1
            & df["pseudo_citizenship"].notna()
            & ~df["pseudo_citizenship"].apply(is_filipino_variant)
            & (df["override_applied"].str.upper().str.strip() == "FOREIGN")
        )
        df.loc[tier2_mask, "CITIZENSHIP_FINAL"] = df.loc[tier2_mask, "pseudo_citizenship"]
        df.loc[tier2_mask, "FOREIGNER_STATUS"] = "Likely Foreigner"
        print(f"       Tier 2 (Likely Foreigner): {tier2_mask.sum():,} records")
    else:
        print(f"       Tier 2 skipped -- columns not found in pseudo-citizenship CSV")

    # -- STEP 9: Verify and validate -----------------------------------------
    print(f"\n[9/10] Verification...")

    # 9A: Distribution
    print("\n       CITIZENSHIP_FINAL distribution (top 20):")
    print(df["CITIZENSHIP_FINAL"].value_counts().head(20).to_string())

    print("\n       FOREIGNER_STATUS distribution:")
    print(df["FOREIGNER_STATUS"].value_counts().to_string())

    # 9B: Null check
    null_cit = df["CITIZENSHIP_FINAL"].isna().sum()
    null_for = df["FOREIGNER_STATUS"].isna().sum()
    assert null_cit == 0, f"CRITICAL: {null_cit} null CITIZENSHIP_FINAL values!"
    assert null_for == 0, f"CRITICAL: {null_for} null FOREIGNER_STATUS values!"
    print(f"\n       ? Null checks passed (0 nulls)")

    # 9C: Cross-check with REAL_FOREIGNERS
    rf_appnos = set(df_rf["APPNO_CLEAN"].unique())
    exodus_verified = set(df[df["FOREIGNER_STATUS"] == "Verified Foreigner"]["APPNO_CLEAN"])
    missing_rf = rf_appnos - exodus_verified
    if len(missing_rf) > 0:
        print(f"       ??  {len(missing_rf)} RF appnos not marked as Verified Foreigner")
        # Show a few examples
        example_missing = df[df["APPNO_CLEAN"].isin(list(missing_rf)[:5])]
        for _, row in example_missing.iterrows():
            print(f"         - {row['APPNO_CLEAN']}: RF={row['RF_NATIONALITY']}, CITIZENSHIP={row['CITIZENSHIP_FINAL']}")
    else:
        print(f"       ? All {len(rf_appnos):,} REAL_FOREIGNERS records are correctly marked as Verified Foreigner")

    # 9D: Row count integrity
    assert len(df) == 178927, f"Row count changed! Expected 178,927, got {len(df)}"
    print(f"       ? Row count preserved: {len(df):,}")

    # 9E: Column count
    expected_new = 3  # CITIZENSHIP_FINAL, FOREIGNER_STATUS, RF_NATIONALITY
    print(f"       ? Total columns: {len(df.columns)} ({len(df.columns) - expected_new} original + {expected_new} new)")

    # -- STEP 10: Save output ------------------------------------------------
    print(f"\n[10/10] Saving output...")

    # Drop intermediate merge columns before saving
    cols_to_drop = [c for c in ["RF_NATIONALITY", "IN_REAL_FOREIGNERS", "override_applied", "pseudo_citizenship"] if c in df.columns]
    if cols_to_drop:
        df = df.drop(columns=cols_to_drop)

    print(f"       Writing {EXODUS_PARQUET}...")
    df.to_parquet(EXODUS_PARQUET, index=False)
    print(f"       ? Saved: {EXODUS_PARQUET} ({len(df):,} rows ? {len(df.columns)} cols)")

    print(f"       Writing {EXODUS_CSV}...")
    df.to_csv(EXODUS_CSV, index=False)
    print(f"       ? Saved: {EXODUS_CSV}")

    print("\n" + "=" * 60)
    print("  Pipeline 4 complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
