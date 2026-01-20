import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw/variant_summary.txt")
OUTPUT_PATH = Path("data/processed/step1_filtered.csv")

USE_COLS = [
    "Chromosome",
    "Start",
    "ReferenceAllele",
    "AlternateAllele",
    "ClinicalSignificance"
]

VALID_LABELS = {
    "pathogenic",
    "likely pathogenic",
    "benign",
    "likely benign"
}

def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    chunks = []
    chunk_size = 100_000  # safe & fast

    for chunk in pd.read_csv(
        RAW_DATA_PATH,
        sep="\t",
        usecols=USE_COLS,
        chunksize=chunk_size,
        low_memory=False
    ):
        chunk["ClinicalSignificance"] = chunk["ClinicalSignificance"].str.lower()
        chunk = chunk[chunk["ClinicalSignificance"].isin(VALID_LABELS)]
        chunks.append(chunk)

    df = pd.concat(chunks, ignore_index=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print("Step 1 complete.")
    print(df["ClinicalSignificance"].value_counts())

if __name__ == "__main__":
    main()
