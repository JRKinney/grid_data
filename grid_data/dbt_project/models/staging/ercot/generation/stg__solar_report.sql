WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_generation', 'solar_report') }}
)

SELECT
    "Publish Time" AS publish_time,
    "Time" AS "time",
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "GEN SYSTEM WIDE" AS gen_system_wide,
    "COP HSL SYSTEM WIDE" AS cop_hsl_system_wide,
    "STPPF SYSTEM WIDE" AS stppf_system_wide,
    "PVGRPP SYSTEM WIDE" AS pvgrpp_system_wide,
    "GEN CenterWest" AS gen_centerwest,
    "COP HSL CenterWest" AS cop_hsl_centerwest,
    "STPPF CenterWest" AS stppf_centerwest,
    "PVGRPP CenterWest" AS pvgrpp_centerwest,
    "GEN NorthWest" AS gen_northwest,
    "COP HSL NorthWest" AS cop_hsl_northwest,
    "STPPF NorthWest" AS stppf_northwest,
    "PVGRPP NorthWest" AS pvgrpp_northwest,
    "GEN FarWest" AS gen_farwest,
    "COP HSL FarWest" AS cop_hsl_farwest,
    "STPPF FarWest" AS stppf_farwest,
    "PVGRPP FarWest" AS pvgrpp_farwest,
    "GEN FarEast" AS gen_fareast,
    "COP HSL FarEast" AS cop_hsl_fareast,
    "STPPF FarEast" AS stppf_fareast,
    "PVGRPP FarEast" AS pvgrpp_fareast,
    "GEN SouthEast" AS gen_southeast,
    "COP HSL SouthEast" AS cop_hsl_southeast,
    "STPPF SouthEast" AS stppf_southeast,
    "PVGRPP SouthEast" AS pvgrpp_southeast,
    "GEN CenterEast" AS gen_centereast,
    "COP HSL CenterEast" AS cop_hsl_centereast,
    "STPPF CenterEast" AS stppf_centereast,
    "PVGRPP CenterEast" AS pvgrpp_centereast,
    "HSL SYSTEM WIDE" AS hsl_system_wide,
    load_date
FROM source_data
