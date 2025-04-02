from ercot_fetcher_utils import ErcotFetcher

if __name__ == "__main__":
    ercot_fetcher = ErcotFetcher()
    ercot_fetcher.fetch_60_day_dam_disclosure()
