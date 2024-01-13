SELECT id, equipment_name as "equipmentName", standard_rate_minute as "standardRateMinute"
from equipment.tool
where equipment_name = :equipmentName