SELECT COALESCE((
SELECT SUM(quantity) 
FROM scrap.scrap_log 
WHERE equipment_path =  :equipmentPath 
AND time_recorded >=  :ShiftStartTime 
),0)