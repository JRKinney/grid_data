WITH source_data AS (
    SELECT *
    FROM {{ source('ercot_raw_prices', 'as_prices') }}
)

SELECT
    "Time" AS time, -- noqa
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "Market" AS market, -- noqa
    "Non-Spinning Reserves" AS non_spinning_reserves,
    "Regulation Down" AS regulation_down,
    "Regulation Up" AS regulation_up,
    "Responsive Reserves" AS responsive_reserves,
    "ERCOT Contingency Reserve Service" AS ercot_contingency_reserve_service,
    load_date
FROM source_data
