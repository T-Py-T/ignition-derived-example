SELECT t.id, tpc.id as "toolProductCodeId", equipment_name as "equipmentName", material_uuid as "materialUuid", tpc.standard_rate_minute as "standardRateMinute"
from equipment.tool t 
JOIN equipment.tool_product_code tpc ON t.id = tpc.tool_id
where equipment_name = :equipmentName