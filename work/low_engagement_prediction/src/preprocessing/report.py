"""
Generate preprocessing report.
"""

from pathlib import Path
import json


class PreprocessingReport:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.artifact_dir = (
            self.project_root
            / "artifacts"
            / "preprocessing"
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
            self.artifact_dir / "preprocessing_summary.json",
            encoding="utf-8",
        ) as f:

            summary = json.load(f)

        report = "# Data Preprocessing Report\n\n"

        for dataset in summary:

            report += (
                f"## {dataset['dataset']}\n\n"
            )

            report += (
                f"- Original Rows: **{dataset['original_rows']}**\n"
            )

            report += (
                f"- Final Rows: **{dataset['final_rows']}**\n"
            )

            report += (
                f"- Duplicates Removed: **{dataset['duplicates_removed']}**\n\n"
            )

        with open(
            self.report_dir / "preprocessing_report.md",
            "w",
            encoding="utf-8",
        ) as f:

            f.write(report)

        print("✓ Preprocessing report generated.")