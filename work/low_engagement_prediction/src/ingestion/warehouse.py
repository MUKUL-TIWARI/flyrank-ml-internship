"""
FlyRank warehouse metadata.
"""

DATASET_ROOT = "hf://datasets/FlyRank/internship-warehouse"

TABLES = {
    "dim_clients": f"{DATASET_ROOT}/dim_clients.parquet",
    "dim_content": f"{DATASET_ROOT}/dim_content.parquet",
    "fact_content_daily_performance": (
        f"{DATASET_ROOT}/fact_content_daily_performance_sample.parquet"
    ),
    "fact_content_query_90d": (
        f"{DATASET_ROOT}/fact_content_query_90d.parquet"
    ),
}