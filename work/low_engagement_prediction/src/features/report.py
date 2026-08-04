"""
Generate feature engineering report.
"""

from pathlib import Path
import json


class FeatureReport:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.artifact_dir = (
            self.project_root
            / "artifacts"
            / "features"
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

        with open(
            self.artifact_dir / "feature_metadata.json",
            encoding="utf-8",
        ) as f:

            metadata = json.load(f)

        report = "# Feature Engineering Report\n\n"

        report += f"- Rows: **{metadata['rows']}**\n"
        report += f"- Columns: **{metadata['columns']}**\n\n"

        report += "## Engineered Features\n\n"

        for feature in metadata["engineered_features"]:
            report += f"- {feature}\n"

        with open(
            self.report_dir / "feature_engineering_report.md",
            "w",
            encoding="utf-8",
        ) as f:

            f.write(report)

        print(" Feature engineering report generated.")