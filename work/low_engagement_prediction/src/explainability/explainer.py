"""
Model Explainability

Generates feature importance artifacts.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


class ModelExplainer:

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
            / "explainability"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def load_feature_importance(self):

        print("Loading feature importance...")

        self.importance = pd.read_csv(

            self.model_dir
            / "random_forest_feature_importance.csv"

        )

    def save_top_features(self):

        self.top_features = (

            self.importance
            .head(10)
            .copy()

        )

        self.top_features.to_csv(

            self.output_dir
            / "top_features.csv",

            index=False,

        )

        print(" Top features saved.")

    def plot_feature_importance(self):

        plt.figure(figsize=(10, 6))

        plt.barh(

            self.top_features["features"],

            self.top_features["importance"],

        )

        plt.xlabel("Importance")

        plt.ylabel("Feature")

        plt.title(
            "Top 10 Feature Importance"
        )

        plt.gca().invert_yaxis()

        plt.tight_layout()

        plt.savefig(

            self.output_dir
            / "feature_importance.png",

            dpi=300,

        )

        plt.close()

        print(" Feature importance plot saved.")

    def run(self):

        self.load_feature_importance()

        self.save_top_features()

        self.plot_feature_importance()