SELECT id, standard_rate_minute as "standardRateMinute", planning_rate_minute as "planningRateMinute"
FROM equipment.rate r
WHERE r.equipment_path = :equipmentPath