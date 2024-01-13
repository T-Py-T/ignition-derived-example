SELECT t.id, tpc.id as "toolProductCodeId", equipment_name as "equipmentName", 
material_uuid as "materialUuid", 
tpc.standard_rate_minute as "standardRateMinute",
tpc.time_retired as "timeRetired"
from equipment.tool t 
LEFT JOIN equipment.tool_product_code tpc ON t.id = tpc.tool_id
where t.id = :toolId