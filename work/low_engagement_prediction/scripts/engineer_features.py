"""
Module 4
Feature Engineering
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT / "src"))

from features.feature_engineering import FeatureEngineer
from features.report import FeatureReport


def main():

    print("=" * 60)
    print("Module 4 - Feature Engineering")
    print("=" * 60)

    engineer = FeatureEngineer()

    engineer.run()

    report = FeatureReport()

    report.generate()

    print("\nModule 4 completed successfully.")


if __name__ == "__main__":
    main()