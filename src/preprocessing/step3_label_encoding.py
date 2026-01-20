import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/processed/step2_clean_variants.csv")
OUTPUT_PATH = Path("data/processed/step3_labeled.csv")

LABEL_MAP = {
    "benign": 0,
    "likely benign": 0,
    "pathogenic": 1,
    "likely pathogenic": 1
}

def main():
    df = pd.read_csv(INPUT_PATH)

    # Normalize label text
    df["ClinicalSignificance"] = df["ClinicalSignificance"].str.lower()

    # Map labels
    df["label"] = df["ClinicalSignificance"].map(LABEL_MAP)

    # Safety check
    df = df.dropna(subset=["label"])
    df["label"] = df["label"].astype(int)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print("Step 3 complete (label encoding).")
    print("Label distribution:")
    print(df["label"].value_counts())

if __name__ == "__main__":
    main()
