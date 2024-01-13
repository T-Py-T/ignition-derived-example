SELECT auth.credential.cardformatkey 
FROM auth.credential
JOIN auth.cardformat ON auth.credential.cardformatkey = auth.cardformat.cardformatkey
WHERE auth.credential.personkey = :userId
AND auth.cardformat.facilitycode = 3269