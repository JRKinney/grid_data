WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_generation', 'unplanned_resource_outages') }}
)

SELECT
    "Current As Of" AS current_as_of,
    "Publish Time" AS publish_time,
    "Actual Outage Start" AS actual_outage_start,
    "Planned End Date" AS planned_end_date,
    "Actual End Date" AS actual_end_date,
    "Resource Name" AS resource_name,
    "Resource Unit Code" AS resource_unit_code,
    "Fuel Type" AS fuel_type,
    "Outage Type" AS outage_type,
    "Nature Of Work" AS nature_of_work,
    "Available MW Maximum" AS available_mw_maximum,
    "Available MW During Outage" AS available_mw_during_outage,
    "Effective MW Reduction Due to Outage" AS effective_mw_reduction_due_to_outage,
    load_date
FROM source_data
