WITH source_data AS (
    SELECT
        *
    FROM {{ source('ercot_raw_60_day_disclosures', '60_day_dam_disclosure_dam_energy_bid_awards') }}
)

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
FROM source_data
