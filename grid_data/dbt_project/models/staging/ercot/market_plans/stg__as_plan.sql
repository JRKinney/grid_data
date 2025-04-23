WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_market_plans', 'as_plan') }}
)

SELECT
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Publish Time" AS publish_time,
    "NSPIN" AS nspin,
    "REGDN" AS regdn,
    "REGUP" AS regup,
    "RRS" AS rrs,
    "ECRS" AS ecrs,
    load_date
FROM source_data
