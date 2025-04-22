WITH source_data AS (
    SELECT *
    FROM {{
        source('ercot_raw_60_day_disclosures', '60_day_sced_disclosure_sced_load_resource')
        }}
)

SELECT
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "SCED Time Stamp" AS sced_time_stamp,
    "Repeated Hour Flag" AS repeated_hour_flag,
    "QSE" AS qse, -- noqa
    "DME" AS dme, -- noqa
    "Resource Name" AS resource_name,
    "Telemetered Resource Status" AS telemetered_resource_status,
    "Max Power Consumption" AS max_power_consumption,
    "Low Power Consumption" AS low_power_consumption,
    "Real Power Consumption" AS real_power_consumption,
    "AS Responsibility for RRS" AS as_responsibility_for_rrs,
    "AS Responsibility for RRSFFR" AS as_responsibility_for_rrsffr,
    "AS Responsibility for NonSpin" AS as_responsibility_for_nonspin,
    "AS Responsibility for RegUp" AS as_responsibility_for_regup,
    "AS Responsibility for RegDown" AS as_responsibility_for_regdown,
    "AS Responsibility for ECRS" AS as_responsibility_for_ecrs,
    "SCED Bid to Buy Curve-MW1" AS sced_bid_to_buy_curve_mw1,
    "SCED Bid to Buy Curve-Price1" AS sced_bid_to_buy_curve_price1,
    "SCED Bid to Buy Curve-MW2" AS sced_bid_to_buy_curve_mw2,
    "SCED Bid to Buy Curve-Price2" AS sced_bid_to_buy_curve_price2,
    "SCED Bid to Buy Curve-MW3" AS sced_bid_to_buy_curve_mw3,
    "SCED Bid to Buy Curve-Price3" AS sced_bid_to_buy_curve_price3,
    "SCED Bid to Buy Curve-MW4" AS sced_bid_to_buy_curve_mw4,
    "SCED Bid to Buy Curve-Price4" AS sced_bid_to_buy_curve_price4,
    "SCED Bid to Buy Curve-MW5" AS sced_bid_to_buy_curve_mw5,
    "SCED Bid to Buy Curve-Price5" AS sced_bid_to_buy_curve_price5,
    "SCED Bid to Buy Curve-MW6" AS sced_bid_to_buy_curve_mw6,
    "SCED Bid to Buy Curve-Price6" AS sced_bid_to_buy_curve_price6,
    "SCED Bid to Buy Curve-MW7" AS sced_bid_to_buy_curve_mw7,
    "SCED Bid to Buy Curve-Price7" AS sced_bid_to_buy_curve_price7,
    "SCED Bid to Buy Curve-MW8" AS sced_bid_to_buy_curve_mw8,
    "SCED Bid to Buy Curve-Price8" AS sced_bid_to_buy_curve_price8,
    "SCED Bid to Buy Curve-MW9" AS sced_bid_to_buy_curve_mw9,
    "SCED Bid to Buy Curve-Price9" AS sced_bid_to_buy_curve_price9,
    "SCED Bid to Buy Curve-MW10" AS sced_bid_to_buy_curve_mw10,
    "SCED Bid to Buy Curve-Price10" AS sced_bid_to_buy_curve_price10,
    "HASL" AS hasl, -- noqa
    "HDL" AS hdl, -- noqa
    "LASL" AS lasl, -- noqa
    "LDL" AS ldl, -- noqa
    "Base Point" AS base_point,
    load_date
FROM source_data
