{{ 
  config(
    materialized='view',
    tags=['hourly']
  ) 
}}

SELECT
  timestamp::TIMESTAMP AS recorded_at,
  region_code,
  price::FLOAT AS usd_per_mwh
FROM {{ source('ercot_raw', 'prices') }}
WHERE price > 0  -- Filter invalid records