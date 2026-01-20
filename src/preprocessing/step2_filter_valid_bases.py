import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/processed/step1_filtered.csv")
OUTPUT_PATH = Path("data/processed/step2_clean_variants.csv")

def main():
    df = pd.read_csv(INPUT_PATH)

    before_count = len(df)

    # Drop missing alleles
    df = df.dropna(subset=["ReferenceAllele", "AlternateAllele"])

    # Remove structural variants & symbolic alleles
    invalid_tokens = {"del", "dup", "ins", "-", "."}

    df = df[
        ~df["ReferenceAllele"].str.lower().isin(invalid_tokens) &
        ~df["AlternateAllele"].str.lower().isin(invalid_tokens)
    ]

    after_count = len(df)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print("Step 2 complete (clean variants).")
    print(f"Rows before cleaning: {before_count}")
    print(f"Rows after cleaning:  {after_count}")
    print(f"Removed rows:         {before_count - after_count}")

if __name__ == "__main__":
    main()
