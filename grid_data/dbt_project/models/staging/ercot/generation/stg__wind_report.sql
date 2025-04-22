WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_generation', 'wind_report') }}
)

SELECT
    "Publish Time" AS publish_time,
    "Time" AS time,
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "GEN SYSTEM WIDE" AS gen_system_wide,
    "COP HSL SYSTEM WIDE" AS cop_hsl_system_wide,
    "STWPF SYSTEM WIDE" AS stwpf_system_wide,
    "WGRPP SYSTEM WIDE" AS wgrpp_system_wide,
    "GEN LZ SOUTH HOUSTON" AS gen_lz_south_houston,
    "COP HSL LZ SOUTH HOUSTON" AS cop_hsl_lz_south_houston,
    "STWPF LZ SOUTH HOUSTON" AS stwpf_lz_south_houston,
    "WGRPP LZ SOUTH HOUSTON" AS wgrpp_lz_south_houston,
    "GEN LZ WEST" AS gen_lz_west,
    "COP HSL LZ WEST" AS cop_hsl_lz_west,
    "STWPF LZ WEST" AS stwpf_lz_west,
    "WGRPP LZ WEST" AS wgrpp_lz_west,
    "GEN LZ NORTH" AS gen_lz_north,
    "COP HSL LZ NORTH" AS cop_hsl_lz_north,
    "STWPF LZ NORTH" AS stwpf_lz_north,
    "WGRPP LZ NORTH" AS wgrpp_lz_north,
    "HSL SYSTEM WIDE" AS hsl_system_wide,
    load_date
FROM source_data
