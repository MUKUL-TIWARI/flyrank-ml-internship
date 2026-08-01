"""
Warehouse metadata.
"""
DATASET_ROOT = "hf://datasets/FlyRank/internship-warehouse"

USE_SAMPLE = True

if USE_SAMPLE:
    FACT_DAILY = f"{DATASET_ROOT}/fact_content_daily_performance_sample.parquet"
else:
    FACT_DAILY = f"{DATASET_ROOT}/fact_content_daily_performance/**/*.parquet"

TABLES = {
    "dim_clients": f"{DATASET_ROOT}/dim_clients.parquet",
    "dim_content": f"{DATASET_ROOT}/dim_content.parquet",
    "fact_content_daily_performance": FACT_DAILY,
    "fact_content_query_90d": f"{DATASET_ROOT}/fact_content_query_90d.parquet",
}