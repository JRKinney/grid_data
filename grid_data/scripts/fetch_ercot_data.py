from ercot_fetcher_utils import ErcotFetcher
import argparse
import pandas as pd


def valid_date(date_string):
    """Convert string date to pandas Timestamp"""
    try:
        return pd.Timestamp(date_string)
    except ValueError:
        msg = f"Not a valid date: '{date_string}'. Expected format: YYYY-MM-DD"
        raise argparse.ArgumentTypeError(msg)


if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Fetch ERCOT 60-day DAM disclosures")

    # Add date arguments
    parser.add_argument("--start-date", type=valid_date, help="Start date in YYYY-MM-DD format")
    parser.add_argument("--end-date", type=valid_date, help="End date in YYYY-MM-DD format")

    # Parse arguments
    args = parser.parse_args()

    # Initialize fetcher with provided dates
    ercot_fetcher = ErcotFetcher(start_date=args.start_date, end_date=args.end_date)

    # Fetch disclosures
    ercot_fetcher.fetch_60_day_dam_disclosures()
    ercot_fetcher.fetch_60_day_sced_disclosure()
    ercot_fetcher.fetch_wind_report()
    ercot_fetcher.fetch_solar_report()
    ercot_fetcher.fetch_as_prices()
    ercot_fetcher.fetch_as_plan()
    ercot_fetcher.fetch_zonal_rt_spp()
    ercot_fetcher.fetch_zonal_da_spp()
    ercot_fetcher.fetch_load_forecast()
    ercot_fetcher.fetch_resource_outage_capacity()
    ercot_fetcher.fetch_reported_outages()
    ercot_fetcher.fetch_temperature_forecast()
    ercot_fetcher.fetch_system_wide_actual_load()
    ercot_fetcher.fetch_unplanned_resource_outages()
    ercot_fetcher.fetch_short_term_system_adequacy()
