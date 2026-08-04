"""
Module 3
Data Preprocessing
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT / "src"))

from preprocessing.preprocessor import DataPreprocessor
from preprocessing.report import PreprocessingReport


def main():

    print("=" * 60)
    print("Module 3 - Data Preprocessing")
    print("=" * 60)

    preprocessor = DataPreprocessor()

    datasets = [
        "dim_clients",
        "dim_content",
        "fact_content_daily_performance",
        "fact_content_query_90d",
    ]

    for dataset in datasets:
        preprocessor.preprocess(dataset)

    preprocessor.save_summary()

    report = PreprocessingReport()
    report.generate()

    print("\nModule 3 completed successfully.")


if __name__ == "__main__":
    main()