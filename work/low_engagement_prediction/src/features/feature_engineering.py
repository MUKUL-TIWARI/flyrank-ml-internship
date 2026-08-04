"""
Feature engineering utilities.
"""

from pathlib import Path
import json

import pandas as pd


class FeatureEngineer:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.processed_dir = (
            self.project_root
            / "data"
            / "processed"
        )

        self.artifact_dir = (
            self.project_root
            / "artifacts"
            / "features"
        )

        self.artifact_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def load_data(self):

        print("Loading datasets...")

        self.content = pd.read_parquet(
            self.processed_dir /
            "dim_content_clean.parquet"
        )

        self.daily = pd.read_parquet(
            self.processed_dir /
            "fact_content_daily_performance_clean.parquet"
        )

        self.query = pd.read_parquet(
            self.processed_dir /
            "fact_content_query_90d_clean.parquet"
        )

    def aggregate_daily(self):

        print("Aggregating daily performance...")

        self.daily = (
            self.daily
            .groupby(
                ["client_hash_id", "content_hash_id"],
                as_index=False,
            )
            .agg(
                {
                    "gsc_impressions": "sum",
                    "gsc_clicks": "sum",
                    "gsc_avg_position": "mean",
                    "ga4_pageviews": "sum",
                    "ga4_sessions": "sum",
                    "ga4_users": "sum",
                    "ga4_engaged_sessions": "sum",
                    "ga4_total_engagement_sec": "sum",
                    "sessions_ai": "sum",
                }
            )
        )

    def aggregate_query(self):

        print("Aggregating query data...")

        self.query = (
            self.query
            .groupby(
                ["client_hash_id", "content_hash_id"],
                as_index=False,
            )
            .agg(
                {
                    "content_visible_query_count": "max",
                    "rare_query_count": "sum",
                    "impressions_90d": "sum",
                    "clicks_90d": "sum",
                }
            )
        )

    def merge(self):

        print("Merging datasets...")

        df = self.content.merge(
            self.daily,
            on=[
                "client_hash_id",
                "content_hash_id",
            ],
            how="left",
        )

        df = df.merge(
            self.query,
            on=[
                "client_hash_id",
                "content_hash_id",
            ],
            how="left",
        )

        self.df = df

    def engineer_features(self):

        print("Engineering features...")

        eps = 1e-6

        df = self.df

        df["ctr"] = (
            df["gsc_clicks"]
            /
            (df["gsc_impressions"] + eps)
        )

        df["engagement_rate"] = (
            df["ga4_engaged_sessions"]
            /
            (df["ga4_sessions"] + eps)
        )

        df["avg_engagement_time"] = (
            df["ga4_total_engagement_sec"]
            /
            (df["ga4_sessions"] + eps)
        )

        df["ai_ratio"] = (
            df["sessions_ai"]
            /
            (df["ga4_sessions"] + eps)
        )

        self.df = df

    def save(self):

        output = (
            self.artifact_dir
            / "feature_store.parquet"
        )

        self.df.to_parquet(
            output,
            index=False,
        )

        metadata = {

            "rows": int(self.df.shape[0]),

            "columns": int(self.df.shape[1]),

            "engineered_features": [

                "ctr",
                "engagement_rate",
                "avg_engagement_time",
                "ai_ratio",

            ],

        }

        with open(
            self.artifact_dir /
            "feature_metadata.json",
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                metadata,
                f,
                indent=4,
            )

        with open(
            self.artifact_dir /
            "feature_summary.md",
            "w",
            encoding="utf-8",
        ) as f:

            f.write("# Feature Store\n\n")

            f.write(
                f"Rows: {self.df.shape[0]}\n\n"
            )

            f.write(
                f"Columns: {self.df.shape[1]}\n\n"
            )

            f.write("Engineered Features\n\n")

            for feature in metadata["engineered_features"]:

                f.write(f"- {feature}\n")

        print("Feature Store saved.")

    def run(self):

        self.load_data()

        self.aggregate_daily()

        self.aggregate_query()

        self.merge()

        self.engineer_features()

        self.save()