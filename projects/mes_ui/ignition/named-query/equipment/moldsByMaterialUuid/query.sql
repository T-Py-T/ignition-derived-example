SELECT equipment_name as "equipmentName", cavity_count as "cavityCount"
FROM equipment.mold m 
JOIN equipment.mold_product_code mpc ON m.id = mpc.mold_id
WHERE mpc.material_uuid = :materialUuid