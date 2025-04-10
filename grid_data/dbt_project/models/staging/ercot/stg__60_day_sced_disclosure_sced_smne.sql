
WITH source_data AS (
    SELECT
        *
    FROM {{ source('ercot_raw_60_day_disclosures', '60_day_sced_disclosure_sced_smne') }}
)

SELECT
    "Interval Start",
    "Interval End",
    "Interval Time",
    "Interval Number",
    "Resource Code",
    "Interval Value",
    "load_date"
FROM source_data
