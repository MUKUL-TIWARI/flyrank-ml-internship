"""
Download FlyRank datasets.
"""

from pathlib import Path


class DatasetDownloader:

    def __init__(self, connection, tables):

        self.conn = connection
        self.tables = tables

        self.output_dir = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "raw"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def download(self):

        for table_name, table_path in self.tables.items():

            print(f"Downloading {table_name}...")

            df = self.conn.execute(
                f"""
                SELECT *
                FROM read_parquet('{table_path}')
                """
            ).fetchdf()

            output = (
                self.output_dir
                / f"{table_name}.parquet"
            )

            df.to_parquet(
                output,
                index=False,
            )

            print(f"✓ Saved {output.name}")