from loguru import logger
from gridstatus import Ercot
import pandas as pd
from pathlib import Path
from grid_data.config import DATA_DIR


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
    ):
        self.iso = Ercot()
        # Create the start and end dates for the 60-day disclosures
        self.process_60_day_date_delay(start_date, end_date)
        self.start_date = start_date
        self.end_date = end_date

        self.data_dir = Path(data_dir) if data_dir else DATA_DIR

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
        df = self.iso.get_60_day_dam_disclosure(
            date=self.disclosure_start_date,
            end=self.disclosure_end_date,
        )

        start_date = self.disclosure_start_date.strftime("%Y-%m-%d")
        end_date = self.disclosure_end_date.strftime("%Y-%m-%d")
        timestamp = pd.Timestamp.now().strftime("%Y-%m-%dT%H:%M:%S")

        for df_type, data in df.items():
            data["load_date"] = pd.Timestamp.now()
            data.to_parquet(
                self.data_dir
                / "ercot"
                / "60_day_disclosures"
                / f"60_day_dam_disclosure_{df_type}__{start_date}_{end_date}_{timestamp}_{df_type}.parquet"
            )
