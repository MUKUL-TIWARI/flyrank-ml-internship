"""
Warehouse inspection utilities.

This module discovers the FlyRank warehouse, exports schemas,
sample records, and generates project documentation.
"""

from pathlib import Path
import json


class WarehouseInspector:
    """Inspect FlyRank warehouse tables."""

    def __init__(self, connection, tables):
        self.conn = connection
        self.tables = tables
        self.summary = []

        self.project_root = Path(__file__).resolve().parents[2]

        self.output_dir = self.project_root / "artifacts" / "discovery"
        self.docs_dir = self.project_root / "docs"

        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.docs_dir.mkdir(parents=True, exist_ok=True)

    def inspect_table(self, table_name: str, table_path: str):
        """Inspect a single table."""

        row_count = self.conn.execute(
            f"""
            SELECT COUNT(*)
            FROM read_parquet('{table_path}')
            """
        ).fetchone()[0]

        schema = self.conn.execute(
            f"""
            DESCRIBE
            SELECT *
            FROM read_parquet('{table_path}')
            """
        ).fetchdf()

        sample = self.conn.execute(
            f"""
            SELECT *
            FROM read_parquet('{table_path}')
            LIMIT 10
            """
        ).fetchdf()

        return row_count, schema, sample

    def save_schema(self, table_name, schema):
        schema.to_csv(
            self.output_dir / f"{table_name}_schema.csv",
            index=False,
        )

    def save_sample(self, table_name, sample):
        sample.to_csv(
            self.output_dir / f"{table_name}_sample.csv",
            index=False,
        )

    def save_summary(self):
        with open(
            self.output_dir / "warehouse_summary.json",
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(self.summary, f, indent=4)

    def generate_inventory_markdown(self):
        inventory = "# FlyRank Warehouse Inventory\n\n"

        for table in self.summary:
            inventory += f"## {table['table']}\n\n"
            inventory += f"- Rows: **{table['rows']}**\n"
            inventory += f"- Columns: **{table['columns']}**\n\n"

        with open(
            self.docs_dir / "data_inventory.md",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(inventory)

    def generate_dictionary_markdown(self):
        dictionary = "# FlyRank Data Dictionary\n\n"

        for table in self.summary:

            schema_path = (
                self.output_dir /
                f"{table['table']}_schema.csv"
            )

            dictionary += f"## {table['table']}\n\n"

            if schema_path.exists():

                with open(schema_path, encoding="utf-8") as f:
                    lines = f.readlines()

                dictionary += "| Column | Type |\n"
                dictionary += "|--------|------|\n"

                for line in lines[1:]:
                    values = line.strip().split(",")

                    if len(values) >= 2:
                        dictionary += (
                            f"| {values[0]} | {values[1]} |\n"
                        )

            dictionary += "\n"

        with open(
            self.docs_dir / "data_dictionary.md",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(dictionary)

    def inspect_all(self):

        print("\n" + "=" * 60)
        print("FlyRank Warehouse Discovery")
        print("=" * 60 + "\n")

        for table_name, table_path in self.tables.items():

            print(f"Inspecting: {table_name}")

            try:

                row_count, schema, sample = self.inspect_table(
                    table_name,
                    table_path,
                )

                self.save_schema(table_name, schema)
                self.save_sample(table_name, sample)

                self.summary.append(
                    {
                        "table": table_name,
                        "rows": row_count,
                        "columns": len(schema),
                        "schema_file": f"{table_name}_schema.csv",
                        "sample_file": f"{table_name}_sample.csv",
                    }
                )

                print(f"✓ Rows     : {row_count}")
                print(f"✓ Columns  : {len(schema)}")
                print("✓ Schema   : saved")
                print("✓ Sample   : saved\n")

            except Exception as e:

                print(f"✗ Failed: {table_name}")
                print(e)
                print()

        self.save_summary()
        self.generate_inventory_markdown()
        self.generate_dictionary_markdown()

        print("=" * 60)
        print("Warehouse discovery completed successfully.")
        print(f"Artifacts : {self.output_dir}")
        print(f"Docs      : {self.docs_dir}")
        print("=" * 60)