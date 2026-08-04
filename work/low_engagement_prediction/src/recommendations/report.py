"""
Recommendation Report
"""

from pathlib import Path
import json


class RecommendationReport:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.artifact_dir = (
            self.project_root
            / "artifacts"
            / "recommendations"
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

        print(" Generating recommendation report...")

        with open(

            self.artifact_dir
            / "recommendation_summary.json",

            "r",

            encoding="utf-8",

        ) as f:

            summary = json.load(f)

        report = (
            self.report_dir
            / "recommendation_report.md"
        )

        with open(

            report,

            "w",

            encoding="utf-8",

        ) as f:

            f.write("# Editorial Recommendation Report\n\n")

            f.write(
                f"**Total Pages Analysed:** "
                f"{summary['total_pages']}\n\n"
            )

            f.write(
                f"**Average Editorial Probability:** "
                f"{summary['average_probability']:.4f}\n\n"
            )

            f.write(
                "## Recommendation Distribution\n\n"
            )

            for category, count in summary[
                "recommendation_counts"
            ].items():

                f.write(
                    f"- **{category}** : {count}\n"
                )

            f.write("\n")

            f.write(
                "## Interpretation\n\n"
            )

            f.write(
                "The recommendation engine ranks webpages "
                "using the probability predicted by the "
                "Random Forest model.\n\n"
            )

            f.write(
                "Pages with higher probabilities should "
                "be prioritised for editorial review, "
                "while lower-probability pages can be "
                "monitored as part of regular maintenance.\n"
            )

        print(" Recommendation report generated.")