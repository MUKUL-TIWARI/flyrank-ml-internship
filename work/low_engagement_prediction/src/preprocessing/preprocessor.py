"""
Data preprocessing utilities.
"""

from pathlib import Path
import json

import pandas as pd
from pandas.api.types import is_datetime64_any_dtype


class DataPreprocessor:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.raw_dir = self.project_root / "data" / "raw"

        self.processed_dir = (
            self.project_root
            / "data"
            / "processed"
        )

        self.artifact_dir = (
            self.project_root
            / "artifacts"
            / "preprocessing"
        )

        self.processed_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.artifact_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.summary = []

    def preprocess(self, dataset_name):

        print(f"\nPreprocessing {dataset_name}...")

        df = pd.read_parquet(
            self.raw_dir / f"{dataset_name}.parquet"
        )

        original_rows = len(df)

        # Remove duplicate rows
        duplicates_removed = int(df.duplicated().sum())
        df = df.drop_duplicates()

        # Fill missing values
        for column in df.columns:

            if pd.api.types.is_bool_dtype(df[column]):

                df[column] = df[column].fillna(False)

            elif pd.api.types.is_datetime64_any_dtype(df[column]):

                pass

            elif pd.api.types.is_numeric_dtype(df[column]):

                  median = df[column].median()

                  if pd.notna(median):
                        df[column] = df[column].fillna(median)

            else:
                df[column] = df[column].fillna("Unknown")


        output = (
            self.processed_dir
            / f"{dataset_name}_clean.parquet"
        )

        df.to_parquet(
            output,
            index=False,
        )

        self.summary.append(
            {
                "dataset": dataset_name,
                "original_rows": original_rows,
                "final_rows": len(df),
                "duplicates_removed": duplicates_removed,
            }
        )

        print(f" Saved {output.name}")

    def save_summary(self):

        with open(
            self.artifact_dir / "preprocessing_summary.json",
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                self.summary,
                f,
                indent=4,
            )