# ERCOT Forecasting Pipeline

[![CI](https://github.com/JRKinney/ercot-forecasting/actions/workflows/ci.yml/badge.svg)](https://github.com/JRKinney/ercot-forecasting/actions)

## Features
- Data ingestion from Parquet files
- dbt transformations with DuckDB
- Dagster orchestration
- Forecasting models

## Local Setup
1. Run setup commands
```bash
git clone https://github.com/JRKinney/ercot-forecasting.git
cd ercot-forecasting
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
dagster dev
python grid_data/scripts/initiate_db.py
```

2. Setup .env file based on .env_example (copy .env_example and fill in the blanks). For ERCOT this requires a API key which anyone can get. Follow the instructions on [the ercot website](https://www.ercot.com/services/api): 

3. Test dbt setup
```bash
cd grid_data/dbt_project && dbt debug
```

4. Fetch some data
```bash
python grid_data/scripts/fetch_ercot_data.py
```

5. Run some dbt models
```
dbt run --models staging.ercot
```

6. Look at the models (do this however you'd like but I will use the [duckdb CLI](https://duckdb.org/docs/stable/clients/cli/overview) )
If you have not already `brew install duckdb`
```bash
duckdb
```
```sql
select * from stg__60_day_dam_disclosure_dam_energy_bid_awards limit 100
```

graph LR
    raw_prices[(raw/parquet)] --> dbt_assets
    dbt_assets --> stg_prices[(staged/parquet)]
    stg_prices --> forecast_asset
    forecast_asset --> predictions[(forecasts/parquet)]


## Project Structure
├── Dockerfile
├── NOTES.md
├── README.md
├── __init__.py
├── docker-compose.yml
├── grid_data
│   ├── config.py
│   ├── dagster_project
│   ├── data
│   ├── dbt_project
│   └── scripts
├── grid_data.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── requires.txt
│   └── top_level.txt
└── pyproject.toml

Recreate with
```bash
tree -L 2 -I '.venv|__pycache__'
```