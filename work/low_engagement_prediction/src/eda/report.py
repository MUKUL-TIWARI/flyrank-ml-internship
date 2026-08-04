"""
Generate EDA report.
"""

from pathlib import Path
import json


class EDAReport:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.artifact_dir = (
            self.project_root
            / "artifacts"
            / "eda"
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
            self.artifact_dir / "dataset_summary.json",
            encoding="utf-8",
        ) as f:

            summary = json.load(f)

        report = "# Exploratory Data Analysis Report\n\n"

        for dataset in summary:

            report += (
                f"## {dataset['dataset']}\n\n"
            )

            report += (
                f"- Rows: **{dataset['rows']}**\n"
            )

            report += (
                f"- Columns: **{dataset['columns']}**\n"
            )

            report += (
                f"- Duplicate Rows: **{dataset['duplicates']}**\n"
            )

            report += (
                f"- Memory Usage: **{dataset['memory_mb']} MB**\n\n"
            )

        with open(
            self.report_dir / "eda_report.md",
            "w",
            encoding="utf-8",
        ) as f:

            f.write(report)

        print("EDA report generated.")