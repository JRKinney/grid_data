Start Dagster UI:
```
dagster dev -m ercot_dagster
```


Scheduling:
```
# jobs/schedules.py
from dagster import define_asset_job, ScheduleDefinition

daily_ercot_job = define_asset_job(name="daily_ercot_refresh")

basic_schedule = ScheduleDefinition(
    job=daily_ercot_job,
    cron_schedule="@daily",
)
```

# Read example with duckdb
import duckdb
conn = duckdb.connect(database='ercot.db')
conn.execute("""
  CREATE TABLE prices AS 
  SELECT * FROM 'data/raw/prices/*.parquet'
""")

## Quick Start
1. Clone repo
2. `pip install -e .`
3. `dagster dev`
4. Materialize assets in UI


Mermaid viz:
graph LR
    raw_prices[(raw/parquet)] --> dbt_assets
    dbt_assets --> stg_prices[(staged/parquet)]
    stg_prices --> forecast_asset
    forecast_asset --> predictions[(forecasts/parquet)]



dagster job execute -m ercot_dagster -j all_assets_job