"""
Data profiling engine for the Search Intelligence Decision Support Platform.

This module profiles FlyRank warehouse tables and exports profiling
results as JSON.
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


class DataProfiler:
    """Profile warehouse tables."""

    def __init__(self, connection, tables):

        self.conn = connection
        self.tables = tables

        self.project_root = Path(__file__).resolve().parents[2]

        self.output_dir = (
            self.project_root
            / "artifacts"
            / "profiling"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def profile_table(self, table_name: str, table_path: str):

        print(f"\nProfiling {table_name}...")

        
        # Development mode:
        # Use a sample for very large tables.
        if table_name == "fact_content_daily_performance":

            query = f"""
            SELECT *
            FROM read_parquet('{table_path}')
            USING SAMPLE 100000 ROWS
            """

        else:
            query = f"""
            SELECT *
            FROM read_parquet('{table_path}')
            """
        df = self.conn.execute(query).fetchdf()

        profile = {
            "table": table_name,
            "rows": int(df.shape[0]),
            "columns": int(df.shape[1]),
            "memory_mb": round(
                df.memory_usage(deep=True).sum()
                / 1024
                / 1024,
                2,
            ),
            "duplicate_rows": int(df.duplicated().sum()),
            "missing_values": {},
            "unique_values": {},
            "dtypes": {},
            "numeric_summary": {},
        }

        # Missing values
        for column in df.columns:

            profile["missing_values"][column] = {
                "count": int(df[column].isna().sum()),
                "percent": round(
                    float(df[column].isna().mean() * 100),
                    2,
                ),
            }

        # Unique values
        for column in df.columns:

            profile["unique_values"][column] = int(
                df[column].nunique(dropna=True)
            )

        # Data types
        for column in df.columns:

            profile["dtypes"][column] = str(df[column].dtype)

        # Numeric summary
        numeric_df = df.select_dtypes(
            include="number"
        )

        if not numeric_df.empty:

            summary = numeric_df.describe().T

            profile["numeric_summary"] = (
                summary.round(4)
                .to_dict(orient="index")
            )

        output_file = (
            self.output_dir
            / f"{table_name}_profile.json"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                profile,
                f,
                indent=4,
            )

        print(f"✓ Saved {output_file.name}")

        return profile

    def profile_all(self):

        profiles = []

        print("\n" + "=" * 60)
        print("FlyRank Data Profiling")
        print("=" * 60)

        for table_name, table_path in self.tables.items():

            try:

                profile = self.profile_table(
                    table_name,
                    table_path,
                )

                profiles.append(profile)

            except Exception as e:

                print(
                    f"✗ Failed to profile {table_name}"
                )
                print(e)

        print("=" * 60)
        print("Profiling completed.")
        print("=" * 60)

        return profiles