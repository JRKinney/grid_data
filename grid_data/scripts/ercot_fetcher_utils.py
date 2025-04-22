from loguru import logger
from gridstatus import Ercot
import pandas as pd
from pathlib import Path
from grid_data.config import DATA_DIR
import time


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

    def fetch_60_day_dam_disclosures(self) -> None:
        """
        fetches the 60-day DAM disclosure files and saves them to the rawdata directory
        """
        if self.disclosure_start_date is None or self.disclosure_end_date is None:
            logger.info(
                "Will not fetch 60-day DAM disclosure due to start and end dates being set before the 60 day delay"
            )
            return None

        logger.info(
            f"Fetching 60-day DAM disclosure from {self.disclosure_start_date} to {self.disclosure_end_date}"
        )
        for _ in range(self.retries):
            try:
                df = self.iso.get_60_day_dam_disclosure(
                    date=self.disclosure_start_date,
                    end=self.disclosure_end_date,
                )
                break
            except Exception as e:
                logger.error(f"Error fetching 60-day DAM disclosure: {e}")
                time.sleep(1)

        for df_type, data in df.items():
            data["load_date"] = pd.Timestamp.now()
            date_info = f"{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}"
            data.to_parquet(
                self.data_dir
                / "raw"
                / "ercot"
                / "60_day_disclosures"
                / f"60_day_dam_disclosure_{df_type}__{date_info}_{df_type}.parquet"
            )

    def fetch_60_day_sced_disclosure(self) -> None:
        """
        fetches the 60-day Sced disclosure files and saves them to the rawdata directory
        """
        if self.disclosure_start_date is None or self.disclosure_end_date is None:
            logger.info(
                "Will not fetch 60-day DAM disclosure due to start and end dates being set before the 60 day delay"
            )
            return None

        logger.info(
            f"Fetching 60-day Sced disclosure from {self.disclosure_start_date} to {self.disclosure_end_date}"
        )
        for _ in range(self.retries):
            try:
                df = self.iso.get_60_day_sced_disclosure(
                    date=self.disclosure_start_date,
                    end=self.disclosure_end_date,
                )
                break
            except Exception as e:
                logger.error(f"Error fetching 60-day Sced disclosure: {e}")
                time.sleep(1)

        for df_type, data in df.items():
            data["load_date"] = pd.Timestamp.now()
            date_info = f"{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}"
            data.to_parquet(
                self.data_dir
                / "raw"
                / "ercot"
                / "60_day_disclosures"
                / f"60_day_sced_disclosure_{df_type}__{date_info}_{df_type}.parquet"
            )

    def fetch_wind_report(self) -> None:
        """
        fetches the wind report files and saves them to the rawdata directory
        """
        logger.info(f"Fetching wind report from {self.start_date} to {self.end_date}")
        for _ in range(self.retries):
            try:
                df = self.iso.get_hourly_wind_report(
                    date=self.start_date,
                    end=self.end_date,
                )
                break
            except Exception as e:
                logger.error(f"Error fetching wind report: {e}")
                time.sleep(1)

        df.to_parquet(
            self.data_dir
            / "raw"
            / "ercot"
            / "generation"
            / f"wind_report__{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}.parquet"
        )

    def fetch_solar_report(self) -> None:
        """
        fetches the solar report files and saves them to the rawdata directory
        """
        logger.info(f"Fetching solar report from {self.start_date} to {self.end_date}")
        for _ in range(self.retries):
            try:
                df = self.iso.get_hourly_solar_report(
                    date=self.start_date,
                    end=self.end_date,
                )
                break
            except Exception as e:
                logger.error(f"Error fetching solar report: {e}")
                time.sleep(1)

        df.to_parquet(
            self.data_dir
            / "raw"
            / "ercot"
            / "generation"
            / f"solar_report__{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}.parquet"
        )

    def fetch_as_prices(self) -> None:
        """
        fetches the ancillary service prices files and saves them to the rawdata directory
        """
        logger.info(f"Fetching ancillary service prices from {self.start_date} to {self.end_date}")
        for _ in range(self.retries):
            try:
                df = self.iso.get_as_prices(
                    date=self.start_date,
                    end=self.end_date,
                )
                break
            except Exception as e:
                logger.error(f"Error fetching ancillary service prices: {e}")
                time.sleep(1)

        df.to_parquet(
            self.data_dir
            / "raw"
            / "ercot"
            / "prices"
            / f"as_prices__{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}.parquet"
        )

    def fetch_as_plan(self) -> None:
        """
        fetches the ancillary service plan files and saves them to the rawdata directory
        """
        logger.info(f"Fetching ancillary service plan from {self.start_date} to {self.end_date}")
        for _ in range(self.retries):
            try:
                df = self.iso.get_as_plan(
                    date=self.start_date,
                    end=self.end_date,
                )
                break
            except Exception as e:
                logger.error(f"Error fetching ancillary service plan: {e}")
                time.sleep(1)

        df.to_parquet(
            self.data_dir
            / "raw"
            / "ercot"
            / "market_plans"
            / f"as_plan__{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}.parquet"
        )

    def fetch_zonal_rt_spp(self) -> None:
        """
        fetches the real-time spp for load zones and saves them to the rawdata directory
        """
        logger.info(f"Fetching real-time spp for load zones from {self.start_date} to {self.end_date}")
        for _ in range(self.retries):
            try:
                df = self.iso.get_spp(
                    self.start_date,
                    self.end_date,
                    market="REAL_TIME_15_MIN",  # 'DAY_AHEAD_HOURLY'
                    locations="ALL",
                    location_type="Load Zone",
                )
                break
            except Exception as e:
                logger.error(f"Error fetching real-time spp for load zones: {e}")
                time.sleep(1)

        df.to_parquet(
            self.data_dir
            / "raw"
            / "ercot"
            / "prices"
            / f"zonal_rt_spp__{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}.parquet"
        )

    def fetch_zonal_da_spp(self) -> None:
        """
        fetches the day-ahead spp for load zones and saves them to the rawdata directory
        """
        logger.info(f"Fetching day-ahead spp for load zones from {self.start_date} to {self.end_date}")
        for _ in range(self.retries):
            try:
                df = self.iso.get_spp(
                    self.start_date,
                    self.end_date,
                    market="DAY_AHEAD_HOURLY",
                    locations="ALL",
                    location_type="Load Zone",
                )
                break
            except Exception as e:
                logger.error(f"Error fetching day-ahead spp for load zones: {e}")
                time.sleep(1)

        df.to_parquet(
            self.data_dir
            / "raw"
            / "ercot"
            / "prices"
            / f"zonal_da_spp__{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}.parquet"
        )

    def fetch_load_forecast(self) -> None:
        """
        fetches the load forecast for load zones and saves them to the rawdata directory
        """
        logger.info(f"Fetching load forecast from {self.start_date} to {self.end_date}")
        for _ in range(self.retries):
            try:
                df = self.iso.get_load_forecast(
                    self.start_date,
                    self.end_date,
                )
                break
            except Exception as e:
                logger.error(f"Error fetching load forecast: {e}")
                time.sleep(1)

        df.to_parquet(
            self.data_dir
            / "raw"
            / "ercot"
            / "load"
            / f"zonal_load_forecast__{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}.parquet"
        )

    def fetch_resource_outage_capacity(self) -> None:
        """
        fetches the resource outage capacity and saves them to the rawdata directory
        """
        logger.info(f"Fetching resource outage capacity from {self.start_date} to {self.end_date}")
        for _ in range(self.retries):
            try:
                df = self.iso.get_hourly_resource_outage_capacity(
                    self.start_date,
                    self.end_date,
                )
                break
            except Exception as e:
                logger.error(f"Error fetching resource outage capacity: {e}")
                time.sleep(1)

        df.to_parquet(
            self.data_dir
            / "raw"
            / "ercot"
            / "generation"
            / f"resource_outage_capacity__{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}.parquet"
        )

    def fetch_reported_outages(self) -> None:
        """
        fetches the reported outages and saves them to the rawdata directory
        """
        logger.info(f"Fetching reported outages from {self.start_date} to {self.end_date}")
        for _ in range(self.retries):
            try:
                df = self.iso.get_reported_outages(
                    self.start_date,
                    self.end_date,
                )
                break
            except Exception as e:
                logger.error(f"Error fetching reported outages: {e}")
                time.sleep(1)

        df.to_parquet(
            self.data_dir
            / "raw"
            / "ercot"
            / "generation"
            / f"reported_outages__{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}.parquet"
        )

    def fetch_temperature_forecast(self) -> None:
        """
        fetches the temperature forecast for weather zones and saves them to the rawdata directory
        """
        logger.info(f"Fetching temperature forecast from {self.start_date} to {self.end_date}")
        for _ in range(self.retries):
            try:
                df = self.iso.get_temperature_forecast_by_weather_zone(
                    self.start_date,
                    self.end_date,
                )
                break
            except Exception as e:
                logger.error(f"Error fetching temperature forecast: {e}")
                time.sleep(1)

        df.to_parquet(
            self.data_dir
            / "raw"
            / "ercot"
            / "weather"
            / f"temperature_forecast__{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}.parquet"
        )

    def fetch_system_wide_actual_load(self) -> None:
        """
        fetches the system wide actual load and saves them to the rawdata directory
        """
        logger.info(f"Fetching system wide actual load from {self.start_date} to {self.end_date}")
        for _ in range(self.retries):
            try:
                df = self.iso.get_system_wide_actual_load(
                    self.start_date,
                    self.end_date,
                )
                break
            except Exception as e:
                logger.error(f"Error fetching system wide actual load: {e}")
                time.sleep(1)

        df.to_parquet(
            self.data_dir
            / "raw"
            / "ercot"
            / "load"
            / f"system_wide_actual_load__{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}.parquet"
        )

    def fetch_unplanned_resource_outages(self) -> None:
        """
        fetches the unplanned resource outages and saves them to the rawdata directory
        """
        logger.info(f"Fetching unplanned resource outages from {self.start_date} to {self.end_date}")
        for _ in range(self.retries):
            try:
                df = self.iso.get_unplanned_resource_outages(
                    self.start_date,
                    self.end_date,
                )
                break
            except Exception as e:
                logger.error(f"Error fetching unplanned resource outages: {e}")
                time.sleep(1)

        df.to_parquet(
            self.data_dir
            / "raw"
            / "ercot"
            / "generation"
            / f"unplanned_resource_outages__{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}.parquet"
        )

    def fetch_short_term_system_adequacy(self) -> None:
        """
        fetches the short term system adequacy and saves them to the rawdata directory
        """
        logger.info(f"Fetching short term system adequacy from {self.start_date} to {self.end_date}")
        for _ in range(self.retries):
            try:
                df = self.iso.get_short_term_system_adequacy(
                    self.start_date,
                    self.end_date,
                )
                break
            except Exception as e:
                logger.error(f"Error fetching short term system adequacy: {e}")
                time.sleep(1)

        df.to_parquet(
            self.data_dir
            / "raw"
            / "ercot"
            / "generation"
            / f"short_term_system_adequacy__{self.start_date_str}_{self.end_date_str}_{self.run_timestamp}.parquet"
        )
