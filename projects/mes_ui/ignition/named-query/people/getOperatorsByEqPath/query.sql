SELECT user_id AS "userId",
    user_name AS "userName",
    equipment_path AS "equipmentPath",
    operator_type AS "operatorType",
    time_reported AS "timeReported",
    time_total_sec AS "timeTotalSec"
FROM human.current_operators
WHERE equipment_path = :equipmentPath
AND operator_type = 'Operator'