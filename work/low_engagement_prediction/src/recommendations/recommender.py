"""
Editorial Recommendation Engine

Generates ranked recommendations for
editorial teams based on model predictions.
"""

from pathlib import Path
import json

import matplotlib.pyplot as plt
import pandas as pd


class RecommendationEngine:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.model_dir = (
            self.project_root
            / "artifacts"
            / "models"
        )

        self.output_dir = (
            self.project_root
            / "artifacts"
            / "recommendations"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def load_predictions(self):

        print("Loading editorial recommendations...")

        self.df = pd.read_csv(

            self.model_dir
            / "editorial_recommendations.csv"

        )

    def rank_recommendations(self):

        print("Ranking recommendations...")

        self.df = self.df.sort_values(

            by="editorial_probability",

            ascending=False,

        )

        self.top100 = self.df.head(100).copy()

        self.top100.to_csv(

            self.output_dir
            / "ranked_editorial_recommendations.csv",

            index=False,

        )

        print(" Top 100 recommendations saved.")

    def generate_summary(self):

        summary = {

            "total_pages": int(
                len(self.df)
            ),

            "recommendation_counts":

                self.df[
                    "recommendation"
                ]
                .value_counts()
                .to_dict(),

            "average_probability": round(

                float(

                    self.df[
                        "editorial_probability"
                    ].mean()

                ),

                4,

            ),

        }

        with open(

            self.output_dir
            / "recommendation_summary.json",

            "w",

            encoding="utf-8",

        ) as f:

            json.dump(

                summary,

                f,

                indent=4,

            )

        print(" Recommendation summary saved.")

    def plot_distribution(self):

        counts = (

            self.df[
                "recommendation"
            ]
            .value_counts()

        )

        plt.figure(figsize=(8, 5))

        counts.plot(kind="bar")

        plt.title(
            "Editorial Recommendation Distribution"
        )

        plt.xlabel(
            "Recommendation"
        )

        plt.ylabel(
            "Number of Pages"
        )

        plt.tight_layout()

        plt.savefig(

            self.output_dir
            / "recommendation_distribution.png",

            dpi=300,

        )

        plt.close()

        print(" Recommendation distribution plot saved.")

    def run(self):

        self.load_predictions()

        self.rank_recommendations()

        self.generate_summary()

        self.plot_distribution()