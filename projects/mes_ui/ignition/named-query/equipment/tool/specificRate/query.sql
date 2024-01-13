SELECT CASE WHEN "line" IS NULL THEN (CASE WHEN "product" IS NULL THEN "tool" ELSE "prodcut" END) else "line" end as rate from
(
SELECT t.equipment_name,
t.standard_rate_minute as "tool", 
tpc.standard_rate_minute as "product",
tpcl.standard_rate_minute as "line"
FROM equipment.tool t
LEFT JOIN equipment.tool_product_code tpc ON t.id = tpc.tool_id and material_uuid = :materialUuid
LEFT JOIN equipment.tool_product_code_line tpcl on tpcl.tool_product_code_id = tpc.id and equipment_path = :equipmentPath
where equipment_name = :equipmentName ) as f