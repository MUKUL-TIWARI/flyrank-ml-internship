"""
Reporting utilities for Module 2.

Converts JSON profiling artifacts into a Markdown report.
"""

from __future__ import annotations

import json
from pathlib import Path


class ProfileReport:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.profile_dir = (
            self.project_root
            / "artifacts"
            / "profiling"
        )

        self.report_dir = (
            self.project_root
            / "reports"
        )

        self.report_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def build_markdown(self):

        report = "# Data Quality Report\n\n"

        profile_files = sorted(
            self.profile_dir.glob("*_profile.json")
        )

        for file in profile_files:

            with open(file, encoding="utf-8") as f:
                profile = json.load(f)

            report += f"## {profile['table']}\n\n"

            report += f"- Rows: **{profile['rows']}**\n"
            report += f"- Columns: **{profile['columns']}**\n"
            report += f"- Memory: **{profile['memory_mb']} MB**\n"
            report += f"- Duplicate Rows: **{profile['duplicate_rows']}**\n\n"

            report += "### Missing Values\n\n"

            report += "| Column | Missing | % |\n"
            report += "|--------|---------|---|\n"

            for column, values in profile["missing_values"].items():

                report += (
                    f"| {column} | "
                    f"{values['count']} | "
                    f"{values['percent']} |\n"
                )

            report += "\n---\n\n"

        report_path = (
            self.report_dir
            / "data_quality_report.md"
        )

        with open(
            report_path,
            "w",
            encoding="utf-8",
        ) as f:
            f.write(report)

        print(f"✓ Report saved: {report_path.name}")