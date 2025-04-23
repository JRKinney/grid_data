WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_market_plans', 'as_plan') }}
)

SELECT
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Publish Time" AS publish_time,
    "NSPIN" AS nspin, -- noqa
    "REGDN" AS regdn, -- noqa
    "REGUP" AS regup, -- noqa
    "RRS" AS rrs, -- noqa
    "ECRS" AS ecrs, -- noqa
    load_date
FROM source_data
