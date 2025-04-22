WITH source_data AS (
    SELECT *
    FROM {{
        source('ercot_raw_60_day_disclosures', '60_day_dam_disclosure_dam_load_resource')
        }}
)

SELECT
    "Time" AS time,
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Load Resource Name" AS load_resource_name,
    "Max Power Consumption for Load Resource"
        AS max_power_consumption_for_load_resource,
    "Low Power Consumption for Load Resource"
        AS low_power_consumption_for_load_resource,
    "RegUp Awarded" AS regup_awarded,
    "RegUp MCPC" AS regup_mcpc,
    "RegDown Awarded" AS regdown_awarded,
    "RegDown MCPC" AS regdown_mcpc,
    "RRSPFR Awarded" AS rrspfr_awarded,
    "RRSFFR Awarded" AS rrsffr_awarded,
    "RRSUFR Awarded" AS rrsufr_awarded,
    "RRS MCPC" AS rrs_mcpc,
    "ECRSSD Awarded" AS ecrssd_awarded,
    "ECRSMD Awarded" AS ecrsmd_awarded,
    "ECRS MCPC" AS ecrs_mcpc,
    "NonSpin Awarded" AS nonspin_awarded,
    "NonSpin MCPC" AS nonspin_mcpc,
    load_date
FROM source_data
