SELECT iv.id, key, value, group_name as "groupName", ivg.id as "groupId"
FROM systemconfig.ignition_value iv 
INNER JOIN systemconfig.ignition_value_group ivg on iv.ignition_value_group_id = ivg.id
ORDER BY ivg.id, key