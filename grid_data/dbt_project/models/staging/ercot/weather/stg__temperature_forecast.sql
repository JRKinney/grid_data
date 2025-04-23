WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_weather', 'temperature_forecast') }}
)

SELECT
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Publish Time" AS publish_time,
    "Coast" AS coast, -- noqa
    "East" AS east, -- noqa
    "Far West" AS far_west,
    "North" AS north, -- noqa
    "North Central" AS north_central,
    "South Central" AS south_central,
    "Southern" AS southern, -- noqa
    "West" AS west, -- noqa
    load_date
FROM source_data
