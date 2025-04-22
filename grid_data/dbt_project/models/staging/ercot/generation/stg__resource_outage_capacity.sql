WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_generation', 'resource_outage_capacity') }}
)

SELECT
    "Publish Time" AS publish_time,
    "Time" AS time,
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Total Resource MW Zone South" AS total_resource_mw_zone_south,
    "Total Resource MW Zone North" AS total_resource_mw_zone_north,
    "Total Resource MW Zone West" AS total_resource_mw_zone_west,
    "Total Resource MW Zone Houston" AS total_resource_mw_zone_houston,
    "Total Resource MW" AS total_resource_mw,
    "Total IRR MW Zone South" AS total_irr_mw_zone_south,
    "Total IRR MW Zone North" AS total_irr_mw_zone_north,
    "Total IRR MW Zone West" AS total_irr_mw_zone_west,
    "Total IRR MW Zone Houston" AS total_irr_mw_zone_houston,
    "Total IRR MW" AS total_irr_mw,
    "Total New Equip Resource MW Zone South"
        AS total_new_equip_resource_mw_zone_south,
    "Total New Equip Resource MW Zone North"
        AS total_new_equip_resource_mw_zone_north,
    "Total New Equip Resource MW Zone West"
        AS total_new_equip_resource_mw_zone_west,
    "Total New Equip Resource MW Zone Houston"
        AS total_new_equip_resource_mw_zone_houston,
    "Total New Equip Resource MW" AS total_new_equip_resource_mw,
    load_date
FROM source_data
