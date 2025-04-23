WITH source_data AS (
    SELECT *
    FROM {{
        source('ercot_raw_60_day_disclosures', '60_day_dam_disclosure_dam_energy_bid_awards')
        }}
)

SELECT
    "Time" AS "time", -- noqa
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Settlement Point" AS settlement_point,
    "QSE Name" AS qse_name,
    "Energy Only Bid Award in MW" AS energy_only_bid_award_in_mw,
    "Settlement Point Price" AS settlement_point_price,
    "Bid ID" AS bid_id,
    load_date
FROM source_data
