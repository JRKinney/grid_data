from loguru import logger
from gridstatus import Ercot
import pandas as pd
from pathlib import Path
from grid_data.config import DATA_DIR
import time
from typing import Callable, Dict, Union


class ErcotFetcher:
    """
    A class for fetching data from the ERCOT ISO.

    Attributes:
        start_date: The start date for fetching data. If None, then it will fetch the latest day of data
        end_date: The end date for fetching data. If None, then it will fetch the latest day of data
        data_dir: The directory to store the data. If None, uses RAW_DATA_DIR from config
    """

    def __init__(
        self,
        start_date: pd.Timestamp | None = None,
        end_date: pd.Timestamp | None = None,
        data_dir: str | None = None,
        retries: int = 3,
    ):
        self.iso = Ercot()
        # Create the start and end dates for the 60-day disclosures
        self.process_60_day_date_delay(start_date, end_date)
        self.start_date = start_date if start_date else (pd.Timestamp.now() - pd.Timedelta(days=3))
        self.end_date = end_date if end_date else (pd.Timestamp.now() - pd.Timedelta(days=2))

        self.start_date_str = self.disclosure_start_date.strftime("%Y-%m-%d")
        self.end_date_str = self.disclosure_end_date.strftime("%Y-%m-%d")
        self.run_timestamp = pd.Timestamp.now().strftime("%Y-%m-%dT%H:%M:%S")

        self.data_dir = Path(data_dir) if data_dir else DATA_DIR
        self.retries = retries

    def process_60_day_date_delay(
        self,
        start_date: pd.Timestamp | None = None,
        end_date: pd.Timestamp | None = None,
    ) -> None:
        """
        A helper function to process the 60-day date delay based on the start and end dates.
        If the start and end dates are before the 60 day delay then it will pass them through.
        If there is no start or end passed, then it will fetch the latest day of data.
        """
        if start_date is None:
            self.disclosure_start_date = pd.Timestamp.now() - pd.Timedelta(days=62)
        else:
            if start_date <= pd.Timestamp.now() - pd.Timedelta(days=62):
                self.disclosure_start_date = start_date
            else:
                self.disclosure_start_date = None

        if end_date is None:
            self.disclosure_end_date = pd.Timestamp.now() - pd.Timedelta(days=61)
        else:
            if end_date <= pd.Timestamp.now() - pd.Timedelta(days=61):
                self.disclosure_end_date = end_date
            else:
                self.disclosure_end_date = None

    def _fetch_data(
        self,
        fetch_function: Callable[[], Union[pd.DataFrame, Dict[str, pd.DataFrame]]],
        function_name: str,
        save_path: str,
        file_prefix: str,
    ) -> None:
        """
        A helper method to handle the common logic of fetching data with retries,
        error handling, and adding load_date.

        Args:
            fetch_function: The function to call for fetching data
            function_name: Name of the function (for logging)
            save_path: Path where to save the data
            file_prefix: Prefix for the saved file

        Returns:
            None (writes to data directory)
        """
        logger.info(f"Fetching {function_name} from {self.start_date} to {self.end_date}")

        for attempt in range(self.retries):
            try:
                df = fetch_function()

                # Handle case where result is a dictionary of dataframes
                if isinstance(df, dict):
                    for df_type, data in df.items():
                        data["load_date"] = pd.Timestamp.now()
                        date_info = f"{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}"
                        data.to_parquet(
                            self.data_dir / save_path / f"{file_prefix}_{df_type}__{date_info}_{df_type}.parquet"
                        )

                # Handle case where result is a single dataframe
                else:
                    df["load_date"] = pd.Timestamp.now()
                    date_info = f"{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}"
                    df.to_parquet(self.data_dir / save_path / f"{file_prefix}__{date_info}.parquet")

            except Exception as e:
                logger.error(f"Error fetching {function_name}: {e}")
                if attempt == self.retries - 1:
                    logger.warning(f"Skipping fetching {function_name}: {e}")
                    return None
                time.sleep(1)

    def fetch_60_day_dam_disclosures(self) -> None:
        """
        Fetches the 60-day DAM disclosure files and saves them to the rawdata directory
        """
        if self.disclosure_start_date is None or self.disclosure_end_date is None:
            logger.info(
                "Will not fetch 60-day DAM disclosure due to start and end dates being set before the 60 day delay"
            )
            return None

        def fetch_func():
            return self.iso.get_60_day_dam_disclosure(
                date=self.disclosure_start_date,
                end=self.disclosure_end_date,
            )

        self._fetch_data(
            fetch_func, "60-day DAM disclosure", "raw/ercot/60_day_disclosures", "60_day_dam_disclosure"
        )

    def fetch_60_day_sced_disclosure(self) -> None:
        """
        Fetches the 60-day Sced disclosure files and saves them to the rawdata directory
        """
        if self.disclosure_start_date is None or self.disclosure_end_date is None:
            logger.info(
                """Will not fetch 60-day Sced disclosure due to start and
                  end dates being set before the 60 day delay"""
            )
            return None

        def fetch_func():
            return self.iso.get_60_day_sced_disclosure(
                date=self.disclosure_start_date,
                end=self.disclosure_end_date,
            )

        self._fetch_data(
            fetch_func, "60-day Sced disclosure", "raw/ercot/60_day_disclosures", "60_day_sced_disclosure"
        )

    def fetch_wind_report(self) -> None:
        """
        Fetches the wind report files and saves them to the rawdata directory
        """

        def fetch_func():
            return self.iso.get_hourly_wind_report(
                date=self.start_date,
                end=self.end_date,
            )

        self._fetch_data(fetch_func, "wind report", "raw/ercot/generation", "wind_report")

    def fetch_solar_report(self) -> None:
        """
        Fetches the solar report files and saves them to the rawdata directory
        """

        def fetch_func():
            return self.iso.get_hourly_solar_report(
                date=self.start_date,
                end=self.end_date,
            )

        self._fetch_data(fetch_func, "solar report", "raw/ercot/generation", "solar_report")

    def fetch_as_prices(self) -> None:
        """
        Fetches the ancillary service prices files and saves them to the rawdata directory
        """

        def fetch_func():
            return self.iso.get_as_prices(
                date=self.start_date,
                end=self.end_date,
            )

        self._fetch_data(fetch_func, "ancillary service prices", "raw/ercot/prices", "as_prices")

    def fetch_as_plan(self) -> None:
        """
        Fetches the ancillary service plan files and saves them to the rawdata directory
        """

        def fetch_func():
            return self.iso.get_as_plan(
                date=self.start_date,
                end=self.end_date,
            )

        self._fetch_data(fetch_func, "ancillary service plan", "raw/ercot/market_plans", "as_plan")

    def fetch_zonal_rt_spp(self) -> None:
        """
        Fetches the real-time spp for load zones and saves them to the rawdata directory
        """

        def fetch_func():
            return self.iso.get_spp(
                self.start_date,
                self.end_date,
                market="REAL_TIME_15_MIN",  # 'DAY_AHEAD_HOURLY'
                locations="ALL",
                location_type="Load Zone",
            )

        self._fetch_data(fetch_func, "real-time spp for load zones", "raw/ercot/prices", "zonal_rt_spp")

    def fetch_zonal_da_spp(self) -> None:
        """
        Fetches the day-ahead spp for load zones and saves them to the rawdata directory
        """

        def fetch_func():
            return self.iso.get_spp(
                self.start_date,
                self.end_date,
                market="DAY_AHEAD_HOURLY",
                locations="ALL",
                location_type="Load Zone",
            )

        self._fetch_data(fetch_func, "day-ahead spp for load zones", "raw/ercot/prices", "zonal_da_spp")

    def fetch_load_forecast(self) -> None:
        """
        Fetches the load forecast for load zones and saves them to the rawdata directory
        """

        def fetch_func():
            return self.iso.get_load_forecast(
                self.start_date,
                self.end_date,
            )

        self._fetch_data(fetch_func, "load forecast", "raw/ercot/load", "zonal_load_forecast")

    def fetch_resource_outage_capacity(self) -> None:
        """
        Fetches the resource outage capacity and saves them to the rawdata directory
        """

        def fetch_func():
            return self.iso.get_hourly_resource_outage_capacity(
                self.start_date,
                self.end_date,
            )

        self._fetch_data(
            fetch_func, "resource outage capacity", "raw/ercot/generation", "resource_outage_capacity"
        )

    def fetch_reported_outages(self) -> None:
        """
        Fetches the reported outages and saves them to the rawdata directory
        """

        def fetch_func():
            return self.iso.get_reported_outages(
                self.start_date,
                self.end_date,
            )

        self._fetch_data(fetch_func, "reported outages", "raw/ercot/generation", "reported_outages")

    def fetch_temperature_forecast(self) -> None:
        """
        Fetches the temperature forecast for weather zones and saves them to the rawdata directory
        """

        def fetch_func():
            return self.iso.get_temperature_forecast_by_weather_zone(
                self.start_date,
                self.end_date,
            )

        self._fetch_data(fetch_func, "temperature forecast", "raw/ercot/weather", "temperature_forecast")

    def fetch_system_wide_actual_load(self) -> None:
        """
        Fetches the system wide actual load and saves them to the rawdata directory
        """

        def fetch_func():
            return self.iso.get_system_wide_actual_load(
                self.start_date,
                self.end_date,
            )

        self._fetch_data(fetch_func, "system wide actual load", "raw/ercot/load", "system_wide_actual_load")

    def fetch_unplanned_resource_outages(self) -> None:
        """
        Fetches the unplanned resource outages and saves them to the rawdata directory
        """

        def fetch_func():
            return self.iso.get_unplanned_resource_outages(
                self.start_date,
                self.end_date,
            )

        self._fetch_data(
            fetch_func, "unplanned resource outages", "raw/ercot/generation", "unplanned_resource_outages"
        )

    def fetch_short_term_system_adequacy(self) -> None:
        """
        Fetches the short term system adequacy and saves them to the rawdata directory
        """

        def fetch_func():
            return self.iso.get_short_term_system_adequacy(
                self.start_date,
                self.end_date,
            )

        self._fetch_data(
            fetch_func, "short term system adequacy", "raw/ercot/generation", "short_term_system_adequacy"
        )
