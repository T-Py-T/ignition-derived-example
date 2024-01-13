SELECT t.id, tpc.id as "toolProductCodeId", equipment_name as "equipmentName", 
material_uuid as "materialUuid", 
tpc.standard_rate_minute as "standardRateMinute"
from equipment.tool t 
LEFT JOIN equipment.tool_product_code tpc ON t.id = tpc.tool_id
where tpc.material_uuid = :materialUuid
and t.time_retired is null and tpc.time_retired is null