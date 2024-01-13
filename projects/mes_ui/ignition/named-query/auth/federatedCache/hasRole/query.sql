SELECT * 
FROM human.federated_user_cache 
JOIN human.federated_user_roles_cache ON human.federated_user_cache.id = human.federated_user_roles_cache.user_id
JOIN auth.roles ON auth.roles.roleid = human.federated_user_roles_cache.role_id
WHERE human.federated_user_cache.id = :userId
AND auth.roles.rolename = :rolename