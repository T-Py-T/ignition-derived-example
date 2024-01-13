SELECT id, cavity_count as "cavityCount", row_count as "rowCount", column_count as "columnCount", standard_rate_minute as "standardRateMinute"
FROM equipment.mold m
WHERE m.equipment_name = :equipmentName