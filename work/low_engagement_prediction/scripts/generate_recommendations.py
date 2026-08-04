"""
Module 7

Editorial Recommendation Engine
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT))

from src.recommendations.recommender import (
    RecommendationEngine,
)

from src.recommendations.report import (
    RecommendationReport,
)


def main():

    print("=" * 60)
    print("Module 7 - Editorial Recommendation Engine")
    print("=" * 60)

    engine = RecommendationEngine()

    engine.run()

    report = RecommendationReport()

    report.generate()

    print("\nModule 7 completed successfully.")


if __name__ == "__main__":
    main()