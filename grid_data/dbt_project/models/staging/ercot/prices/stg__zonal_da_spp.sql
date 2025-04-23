WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_prices', 'zonal_da_spp') }}
)

SELECT
    "Time" AS time,
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Location" AS location,
    "Location Type" AS location_type,
    "Market" AS market,
    "SPP" AS spp,
    load_date
FROM source_data
