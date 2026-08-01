"""
Module 1
Warehouse Discovery Runner
"""

from pathlib import Path
import os
import sys

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT / "src"))

from ingestion.database import DatabaseManager
from ingestion.inspector import WarehouseInspector
from ingestion.warehouse import TABLES


def main():

    load_dotenv(PROJECT_ROOT / ".env")

    token = os.getenv("HF_TOKEN")

    if not token:
        raise RuntimeError("HF_TOKEN not found.")

    print("=" * 60)
    print("Search Intelligence Decision Support Platform")
    print("Module 1 - Warehouse Discovery")
    print("=" * 60)

    database = DatabaseManager(token)

    connection = database.connect()

    inspector = WarehouseInspector(connection, TABLES)

    inspector.inspect_all()

    database.close()


if __name__ == "__main__":
    main()