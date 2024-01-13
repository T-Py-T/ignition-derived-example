SELECT tpc.id as "toolProductCodeId", tpcl.id as "toolProductCodeLineId",
material_uuid as "materialUuid", 
tpc.standard_rate_minute as "standardRateMinute",
tpcl.standard_rate_minute as "lineOverrideRate",
tpcl.equipment_path as "equipmentPath",
tpcl.time_retired as "timeRetired"
from equipment.tool_product_code tpc 
LEFT JOIN equipment.tool_product_code_line tpcl ON tpc.id = tpcl.tool_product_code_id
where tpc.id = :toolProductCodeId