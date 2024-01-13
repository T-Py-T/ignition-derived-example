SELECT mpc.id, material_uuid as "materialUuid"
FROM equipment.mold m
JOIN equipment.mold_product_code mpc ON m.id = mpc.mold_id
WHERE m.equipment_name = :equipmentName