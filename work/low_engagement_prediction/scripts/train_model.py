"""
Module 5
Model Training
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT / "src"))

from models.trainer import ModelTrainer
from models.report import ModelReport


def main():

    print("=" * 60)
    print("Module 5 - Model Training")
    print("=" * 60)

    trainer = ModelTrainer()

    trainer.run()

    report = ModelReport()

    report.generate()

    print("\nModule 5 completed successfully.")


if __name__ == "__main__":
    main()