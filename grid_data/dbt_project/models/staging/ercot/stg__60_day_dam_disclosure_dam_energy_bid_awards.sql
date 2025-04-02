SELECT
    "Time",
    "Interval Start",
    "Interval End",
    "Settlement Point",
    "QSE Name",
    "Energy Only Bid Award in MW",
    "Settlement Point Price",
    "Bid ID",
    "load_date"
FROM {{ source('ercot_raw', '60_day_disclosures') }}
WHERE REGEXP_MATCHES(filename, '60_day_dam_disclosure_dam_energy_bid_awards.*\.parquet')