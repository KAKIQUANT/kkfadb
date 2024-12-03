from .interface import FactorStorage
import clickhouse_connect
from typing import Optional, List
import pandas as pd
import json
from ..factors.base import BaseFactor

class ClickHouseFactorStorage(FactorStorage):
    def __init__(self, host: str, port: int, username: str, password: str):
        self.client = clickhouse_connect.get_client(
            host=host,
            port=port,
            username=username,
            password=password
        )
        self._ensure_tables()

    def _ensure_tables(self):
        """Create necessary tables if they don't exist"""
        self.client.command("""
            CREATE TABLE IF NOT EXISTS factors (
                name String,
                description String,
                category String,
                version String,
                metadata String,
                code String,
                created_at DateTime,
                updated_at DateTime
            ) ENGINE = MergeTree()
            ORDER BY name
        """)

        self.client.command("""
            CREATE TABLE IF NOT EXISTS factor_data (
                factor_name String,
                date Date,
                symbol String,
                value Float64
            ) ENGINE = MergeTree()
            ORDER BY (factor_name, date, symbol)
        """)

    def save_factor(self, factor: BaseFactor) -> None:
        self.client.command("""
            INSERT INTO factors 
            (name, description, category, version, metadata, created_at, updated_at)
            VALUES
            """, parameters=[
                factor.name,
                factor.description,
                factor.category,
                factor.version,
                json.dumps(factor.metadata),
                factor.created_at,
                factor.updated_at
            ])

    def save_factor_data(self, name: str, data: pd.DataFrame) -> None:
        # Assuming data has MultiIndex (date, symbol) and factor values
        df = data.reset_index()
        df['factor_name'] = name
        self.client.insert_df('factor_data', df) 