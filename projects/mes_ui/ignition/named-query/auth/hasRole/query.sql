SELECT * 
FROM auth.person
JOIN auth.userroles ON auth.person.personkey = auth.userroles.userid
JOIN auth.roles ON auth.roles.roleid = auth.userroles.roleid
WHERE auth.person.personkey = :userId
AND auth.roles.rolename = :rolename