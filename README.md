
1. Create virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

graph LR
    raw_prices[(raw/parquet)] --> dbt_assets
    dbt_assets --> stg_prices[(staged/parquet)]
    stg_prices --> forecast_asset
    forecast_asset --> predictions[(forecasts/parquet)]