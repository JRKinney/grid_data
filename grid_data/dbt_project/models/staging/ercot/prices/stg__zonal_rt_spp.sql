WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_prices', 'zonal_rt_spp') }}
)

SELECT
    "Time" AS time, -- noqa
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Location" AS location, -- noqa
    "Location Type" AS location_type,
    "Market" AS market, -- noqa
    "SPP" AS spp, -- noqa
    load_date
FROM source_data
