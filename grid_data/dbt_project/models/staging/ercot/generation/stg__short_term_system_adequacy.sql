WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_generation', 'short_term_system_adequacy') }}
)

SELECT
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Publish Time" AS publish_time,
    "Capacity Generation Resource South" AS capacity_generation_resource_south,
    "Capacity Generation Resource North" AS capacity_generation_resource_north,
    "Capacity Generation Resource West" AS capacity_generation_resource_west,
    "Capacity Generation Resource Houston"
        AS capacity_generation_resource_houston,
    "Capacity Load Resource South" AS capacity_load_resource_south,
    "Capacity Load Resource North" AS capacity_load_resource_north,
    "Capacity Load Resource West" AS capacity_load_resource_west,
    "Capacity Load Resource Houston" AS capacity_load_resource_houston,
    "Offline Available MW South" AS offline_available_mw_south,
    "Offline Available MW North" AS offline_available_mw_north,
    "Offline Available MW West" AS offline_available_mw_west,
    "Offline Available MW Houston" AS offline_available_mw_houston,
    "Available Capacity Generation" AS available_capacity_generation,
    "Available Capacity Reserve" AS available_capacity_reserve,
    "Capacity Generation Resource Total" AS capacity_generation_resource_total,
    "Capacity Load Resource Total" AS capacity_load_resource_total,
    "Offline Available MW Total" AS offline_available_mw_total
FROM source_data
