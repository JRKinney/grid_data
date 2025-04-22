WITH source_data AS (
    SELECT *
    FROM {{
        source('ercot_raw_60_day_disclosures', '60_day_sced_disclosure_sced_smne')
        }}
)

SELECT
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Interval Time" AS interval_time,
    "Interval Number" AS interval_number,
    "Resource Code" AS resource_code,
    "Interval Value" AS interval_value,
    load_date
FROM source_data
