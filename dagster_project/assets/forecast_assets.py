from dagster import asset, get_dagster_logger
import duckdb
import pandas as pd

@asset(deps=[ercot_dbt_assets])
def ercot_price_forecast():
    logger = get_dagster_logger()
    
    # Read from dbt models
    conn = duckdb.connect(database='grid_data.db')
    df = conn.execute("""
        SELECT * FROM stg_prices  # Your dbt model
    """).df()
    
    logger.info(f"Loaded {len(df)} records for forecasting")
    
    # Your forecasting logic here
    forecasts = ...
    
    # Write predictions
    forecasts.to_parquet("data/forecasts/next_day.parquet")
    return forecasts