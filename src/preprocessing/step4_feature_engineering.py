import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/processed/step3_labeled.csv")
OUTPUT_PATH = Path("data/processed/step4_features.csv")

def main():
    df = pd.read_csv(INPUT_PATH)

    before = len(df)

    # Drop rows with missing critical fields
    df = df.dropna(subset=["Chromosome", "Start", "ReferenceAllele", "AlternateAllele"])

    # Ensure correct types
    df["Chromosome"] = df["Chromosome"].astype(str)
    df["Start"] = pd.to_numeric(df["Start"], errors="coerce")
    df = df.dropna(subset=["Start"])

    # Feature engineering
    df["ref_len"] = df["ReferenceAllele"].astype(str).str.len()
    df["alt_len"] = df["AlternateAllele"].astype(str).str.len()

    # Mutation length difference
    df["len_diff"] = df["alt_len"] - df["ref_len"]

    # Normalize position
    max_pos = df["Start"].max()
    df["position_norm"] = df["Start"] / max_pos

    final_df = df[
        [
            "Chromosome",
            "ref_len",
            "alt_len",
            "len_diff",
            "position_norm",
            "label"
        ]
    ]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    final_df.to_csv(OUTPUT_PATH, index=False)

    print("Step 4 complete (numeric mutation features).")
    print(f"Rows before: {before}")
    print(f"Rows after:  {len(final_df)}")
    print("Sample:")
    print(final_df.head())

if __name__ == "__main__":
    main()
