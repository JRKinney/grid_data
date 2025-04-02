SELECT
    "Time",
    "Interval Start",
    "Interval End",
    "Load Resource Name",
    "Max Power Consumption for Load Resource",
    "Low Power Consumption for Load Resource",
    "RegUp Awarded",
    "RegUp MCPC",
    "RegDown Awarded",
    "RegDown MCPC",
    "RRSPFR Awarded",
    "RRSFFR Awarded",
    "RRSUFR Awarded",
    "RRS MCPC",
    "ECRSSD Awarded",
    "ECRSMD Awarded",
    "ECRS MCPC",
    "NonSpin Awarded",
    "NonSpin MCPC",
    "load_date"
FROM {{ source('ercot_raw', '60_day_disclosures') }}
WHERE REGEXP_MATCHES(filename, '60_day_dam_disclosure_dam_load_resource.*\.parquet')