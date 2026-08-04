"""
Module 6
Model Explainability
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT))

from src.explainability.explainer import ModelExplainer
from src.explainability.report import ExplainabilityReport


def main():

    print("=" * 60)
    print("Module 6 - Model Explainability")
    print("=" * 60)

    explainer = ModelExplainer()

    explainer.run()

    report = ExplainabilityReport()

    report.generate()

    print("\nModule 6 completed successfully.")


if __name__ == "__main__":
    main()