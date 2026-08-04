"""
Module 2
Exploratory Data Analysis
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT / "src"))

from eda.analyzer import DataAnalyzer
from eda.report import EDAReport


def main():

    print("=" * 60)
    print("Module 2 - Exploratory Data Analysis")
    print("=" * 60)

    analyzer = DataAnalyzer()

    datasets = [
        "dim_clients",
        "dim_content",
        "fact_content_daily_performance",
        "fact_content_query_90d",
    ]

    for dataset in datasets:
        analyzer.analyze_dataset(dataset)

    analyzer.save_summary()

    report = EDAReport()
    report.generate()

    print("\nModule 2 completed successfully.")


if __name__ == "__main__":
    main()