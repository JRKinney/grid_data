WITH source_data AS (
    SELECT *
    FROM {{
        source('ercot_raw_60_day_disclosures', '60_day_dam_disclosure_dam_energy_bids')
        }}
)

SELECT
    "Time" AS "time", -- noqa
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Settlement Point" AS settlement_point,
    "QSE Name" AS qse_name,
    "Energy Only Bid MW1" AS energy_only_bid_mw1,
    "Energy Only Bid Price1" AS energy_only_bid_price1,
    "Energy Only Bid MW2" AS energy_only_bid_mw2,
    "Energy Only Bid Price2" AS energy_only_bid_price2,
    "Energy Only Bid MW3" AS energy_only_bid_mw3,
    "Energy Only Bid Price3" AS energy_only_bid_price3,
    "Energy Only Bid MW4" AS energy_only_bid_mw4,
    "Energy Only Bid Price4" AS energy_only_bid_price4,
    "Energy Only Bid MW5" AS energy_only_bid_mw5,
    "Energy Only Bid Price5" AS energy_only_bid_price5,
    "Energy Only Bid MW6" AS energy_only_bid_mw6,
    "Energy Only Bid Price6" AS energy_only_bid_price6,
    "Energy Only Bid MW7" AS energy_only_bid_mw7,
    "Energy Only Bid Price7" AS energy_only_bid_price7,
    "Energy Only Bid MW8" AS energy_only_bid_mw8,
    "Energy Only Bid Price8" AS energy_only_bid_price8,
    "Energy Only Bid MW9" AS energy_only_bid_mw9,
    "Energy Only Bid Price9" AS energy_only_bid_price9,
    "Energy Only Bid MW10" AS energy_only_bid_mw10,
    "Energy Only Bid Price10" AS energy_only_bid_price10,
    "Energy Only Bid ID" AS energy_only_bid_id,
    "Multi-Hour Block Indicator" AS multi_hour_block_indicator,
    "Block/Curve indicator" AS block_curve_indicator,
    load_date
FROM source_data
