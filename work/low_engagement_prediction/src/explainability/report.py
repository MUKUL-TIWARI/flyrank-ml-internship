"""
Model Explainability Report
"""

from pathlib import Path

import pandas as pd


class ExplainabilityReport:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.explain_dir = (
            self.project_root
            / "artifacts"
            / "explainability"
        )

        self.report_dir = (
            self.project_root
            / "reports"
        )

        self.report_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate(self):

        print("Generating explainability report...")

        top_features = pd.read_csv(

            self.explain_dir
            / "top_features.csv"

        )

        report = self.report_dir / "model_explainability.md"

        with open(

            report,

            "w",

            encoding="utf-8",

        ) as f:

            f.write("# Model Explainability\n\n")

            f.write(
                "## Model\n\n"
            )

            f.write(
                "Random Forest Classifier\n\n"
            )

            f.write(
                "## Top 10 Important Features\n\n"
            )

            for index, row in top_features.iterrows():

                f.write(

                    f"{index + 1}. "

                    f"**{row['features']}** "

                    f"(Importance: {row['importance']:.4f})\n"

                )

            f.write("\n")

            f.write(
                "## Interpretation\n\n"
            )

            f.write(
                "The Random Forest model ranks features "
                "based on their contribution to prediction quality. "
                "Features with higher importance values had a greater "
                "influence on identifying webpages that may require "
                "editorial review.\n\n"
            )

            f.write(
                "These insights help explain the model's decisions "
                "and provide transparency for editorial teams when "
                "prioritizing content updates.\n"
            )

        print(" Explainability report generated.")