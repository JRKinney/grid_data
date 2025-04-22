WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_generation', 'reported_outages') }}
)

SELECT
    "Time" AS time, -- noqa
    "Combined Unplanned" AS combined_unplanned,
    "Combined Planned" AS combined_planned,
    "Combined Total" AS combined_total,
    "Dispatchable Unplanned" AS dispatchable_unplanned,
    "Dispatchable Planned" AS dispatchable_planned,
    "Dispatchable Total" AS dispatchable_total,
    "Renewable Unplanned" AS renewable_unplanned,
    "Renewable Planned" AS renewable_planned,
    "Renewable Total" AS renewable_total,
    load_date
FROM source_data
