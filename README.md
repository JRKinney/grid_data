# ERCOT Forecasting Pipeline

[![CI](https://github.com/JRKinney/ercot-forecasting/actions/workflows/ci.yml/badge.svg)](https://github.com/JRKinney/ercot-forecasting/actions)

## Features
- Data ingestion from Parquet files
- dbt transformations with DuckDB
- Dagster orchestration
- Forecasting models

## Local Setup
```bash
git clone https://github.com/JRKinney/ercot-forecasting.git
cd ercot-forecasting
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
dagster dev
```

Setup .env file based on .env_example (copy .env_example and fill in the blanks)


graph LR
    raw_prices[(raw/parquet)] --> dbt_assets
    dbt_assets --> stg_prices[(staged/parquet)]
    stg_prices --> forecast_asset
    forecast_asset --> predictions[(forecasts/parquet)]


## Project Structure
```bash
tree -L 2 -I '.venv|__pycache__'
```