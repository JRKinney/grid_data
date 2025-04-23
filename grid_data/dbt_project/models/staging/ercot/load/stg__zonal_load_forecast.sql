WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_load', 'zonal_load_forecast') }}
)

SELECT
    "Time" AS time, -- noqa
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Publish Time" AS publish_time,
    "North" AS north, -- noqa
    "South" AS south, -- noqa
    "West" AS west, -- noqa
    "Houston" AS houston, -- noqa
    "System Total" AS system_total,
    load_date
FROM source_data
