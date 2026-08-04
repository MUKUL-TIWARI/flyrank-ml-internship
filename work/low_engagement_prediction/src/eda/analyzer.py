"""
Exploratory Data Analysis utilities.
"""

from pathlib import Path
import json

import pandas as pd


class DataAnalyzer:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.raw_dir = self.project_root / "data" / "raw"

        self.artifact_dir = (
            self.project_root
            / "artifacts"
            / "eda"
        )

        self.artifact_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.summary = []

    def analyze_dataset(self, dataset_name):

        print(f"\nAnalyzing {dataset_name}...")

        df = pd.read_parquet(
            self.raw_dir / f"{dataset_name}.parquet"
        )

        rows = len(df)
        cols = len(df.columns)
        duplicates = int(df.duplicated().sum())
        memory = round(
            df.memory_usage(deep=True).sum()
            / 1024
            / 1024,
            2,
        )

        missing = (
            df.isnull()
            .sum()
            .reset_index()
        )

        missing.columns = [
            "column",
            "missing_values",
        ]

        missing["missing_percent"] = round(
            missing["missing_values"]
            / rows
            * 100,
            2,
        )

        missing.to_csv(

            self.artifact_dir
            / f"{dataset_name}_summary.csv",

            index=False,

        )

        self.summary.append(
            {
                "dataset": dataset_name,
                "rows": rows,
                "columns": cols,
                "duplicates": duplicates,
                "memory_mb": memory,
            }
        )

        print(f" Rows       : {rows}")
        print(f" Columns    : {cols}")
        print(f" Duplicates : {duplicates}")
        print(f" Memory(MB) : {memory}")

    def save_summary(self):

        with open(

            self.artifact_dir
            / "dataset_summary.json",

            "w",

            encoding="utf-8",

        ) as f:

            json.dump(
                self.summary,
                f,
                indent=4,
            )