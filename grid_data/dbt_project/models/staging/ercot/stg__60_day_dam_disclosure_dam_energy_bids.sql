WITH source_data AS (
    SELECT 
        *
    FROM {{ source('ercot_raw', '60_day_dam_disclosure_dam_energy_bids') }} 
)

SELECT
    "Time",
    "Interval Start",
    "Interval End",
    "Settlement Point",
    "QSE Name",
    "Energy Only Bid MW1",
    "Energy Only Bid Price1",
    "Energy Only Bid MW2",
    "Energy Only Bid Price2",
    "Energy Only Bid MW3",
    "Energy Only Bid Price3",
    "Energy Only Bid MW4",
    "Energy Only Bid Price4",
    "Energy Only Bid MW5",
    "Energy Only Bid Price5",
    "Energy Only Bid MW6",
    "Energy Only Bid Price6",
    "Energy Only Bid MW7",
    "Energy Only Bid Price7",
    "Energy Only Bid MW8",
    "Energy Only Bid Price8",
    "Energy Only Bid MW9",
    "Energy Only Bid Price9",
    "Energy Only Bid MW10",
    "Energy Only Bid Price10",
    "Energy Only Bid ID",
    "Multi-Hour Block Indicator",
    "Block/Curve indicator",
    "load_date"
FROM source_data
