"""
Database connection utilities.
"""

from __future__ import annotations

import duckdb


class DatabaseManager:
    """Manage DuckDB connections."""

    def __init__(self, hf_token: str):
        self.hf_token = hf_token
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = duckdb.connect(database=":memory:")

            self.connection.execute(
                f"""
                CREATE SECRET hf_token (
                    TYPE HUGGINGFACE,
                    TOKEN '{self.hf_token}'
                );
                """
            )

        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None