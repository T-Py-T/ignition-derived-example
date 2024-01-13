SELECT t.id, tpc.id as "toolProductCodeId", tpcl.id as "toolProductCodeLineId", equipment_name as "equipmentName", 
material_uuid as "materialUuid", 
tpc.standard_rate_minute as "standardRateMinute",
tpcl.standard_rate_minute as "lineOverrideRate",
tpcl.equipment_path as "equipmentPath",
tpc.time_retired as "timeRetired"
from equipment.tool t 
LEFT JOIN equipment.tool_product_code tpc ON t.id = tpc.tool_id and tpc.time_retired is null 
LEFT JOIN equipment.tool_product_code_line tpcl ON tpc.id = tpcl.tool_product_code_id and tpcl.time_retired is null
where equipment_name = :equipmentName
