WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_load', 'system_wide_actual_load') }}
)

SELECT
    "Time" AS time, -- noqa
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Demand" AS demand, -- noqa
    load_date
FROM source_data
