WITH source_data AS (
    SELECT *
    FROM {{
        source('ercot_raw_60_day_disclosures', '60_day_dam_disclosure_dam_gen_resource')
        }}
)

SELECT
    "Time" AS time, -- noqa
    "Interval Start" AS interval_start,
    "Interval End" AS interval_end,
    "QSE" AS qse, -- noqa
    "DME" AS dme, -- noqa
    "Resource Name" AS resource_name,
    "Resource Type" AS resource_type,
    "QSE submitted Curve-MW1" AS qse_submitted_curve_mw1,
    "QSE submitted Curve-Price1" AS qse_submitted_curve_price1,
    "QSE submitted Curve-MW2" AS qse_submitted_curve_mw2,
    "QSE submitted Curve-Price2" AS qse_submitted_curve_price2,
    "QSE submitted Curve-MW3" AS qse_submitted_curve_mw3,
    "QSE submitted Curve-Price3" AS qse_submitted_curve_price3,
    "QSE submitted Curve-MW4" AS qse_submitted_curve_mw4,
    "QSE submitted Curve-Price4" AS qse_submitted_curve_price4,
    "QSE submitted Curve-MW5" AS qse_submitted_curve_mw5,
    "QSE submitted Curve-Price5" AS qse_submitted_curve_price5,
    "QSE submitted Curve-MW6" AS qse_submitted_curve_mw6,
    "QSE submitted Curve-Price6" AS qse_submitted_curve_price6,
    "QSE submitted Curve-MW7" AS qse_submitted_curve_mw7,
    "QSE submitted Curve-Price7" AS qse_submitted_curve_price7,
    "QSE submitted Curve-MW8" AS qse_submitted_curve_mw8,
    "QSE submitted Curve-Price8" AS qse_submitted_curve_price8,
    "QSE submitted Curve-MW9" AS qse_submitted_curve_mw9,
    "QSE submitted Curve-Price9" AS qse_submitted_curve_price9,
    "QSE submitted Curve-MW10" AS qse_submitted_curve_mw10,
    "QSE submitted Curve-Price10" AS qse_submitted_curve_price10,
    "Start Up Hot" AS start_up_hot,
    "Start Up Inter" AS start_up_inter,
    "Start Up Cold" AS start_up_cold,
    "Min Gen Cost" AS min_gen_cost,
    "HSL" AS hsl, -- noqa
    "LSL" AS lsl, -- noqa
    "Resource Status" AS resource_status,
    "Awarded Quantity" AS awarded_quantity,
    "Settlement Point Name" AS settlement_point_name,
    "Energy Settlement Point Price" AS energy_settlement_point_price,
    "RegUp Awarded" AS regup_awarded,
    "RegUp MCPC" AS regup_mcpc,
    "RegDown Awarded" AS regdown_awarded,
    "RegDown MCPC" AS regdown_mcpc,
    "RRSPFR Awarded" AS rrspfr_awarded,
    "RRSFFR Awarded" AS rrsffr_awarded,
    "RRSUFR Awarded" AS rrsufr_awarded,
    "RRS MCPC" AS rrs_mcpc,
    "ECRSSD Awarded" AS ecrssd_awarded,
    "ECRS MCPC" AS ecrs_mcpc,
    "NonSpin Awarded" AS nonspin_awarded,
    "NonSpin MCPC" AS nonspin_mcpc,
    load_date
FROM source_data
