SELECT mr.id, material_uuid as "materialUuid", mr.standard_rate_minute as "standardRateMinute"
FROM equipment.rate r
JOIN equipment.material_rate mr ON r.id = mr.rate_id
WHERE r.equipment_path = :equipmentPath