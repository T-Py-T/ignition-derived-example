SELECT 
bill_of_lading, 
lot_number, 
origination_silo_name, 
silo_name, 
second_destination_silo_name, 
critical_shear, 
seq, 
test_status, 
status 
FROM COA_3NL_data
WHERE (status = 3 or status = 4) and (test_status = 3 or test_status = 4)