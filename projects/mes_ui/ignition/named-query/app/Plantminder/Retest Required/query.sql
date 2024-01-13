SELECT 
bill_of_lading, 
lot_number, 
origination_silo_name, 
critical_shear, 
status, 
CASE
	WHEN test_status = 0 THEN 'No Result'
	WHEN test_status = 1 THEN 'Fail'
	WHEN test_status = 2 THEN 'Retest Required'
	WHEN test_status = 3 THEN 'Pass'
	ELSE 'No Test Data'
	END
AS 'test_status'  
FROM COA_3NL_data
WHERE status = 2 and (test_status = 2 or test_status = 1)