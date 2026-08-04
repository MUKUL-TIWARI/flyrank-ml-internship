"""
Module 1
Download FlyRank datasets
"""

from pathlib import Path
import os
import sys

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT / "src"))

from ingestion.database import DatabaseManager
from ingestion.downloader import DatasetDownloader
from ingestion.warehouse import TABLES


def main():

    load_dotenv(PROJECT_ROOT / ".env")

    token = os.getenv("HF_TOKEN")

    if not token:
        raise RuntimeError("HF_TOKEN not found.")

    print("=" * 60)
    print("Module 1 - Data Ingestion")
    print("=" * 60)

    database = DatabaseManager(token)

    connection = database.connect()

    downloader = DatasetDownloader(
        connection,
        TABLES,
    )

    downloader.download()

    database.close()

    print("\nModule 1 completed.")


if __name__ == "__main__":
    main()