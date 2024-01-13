SELECT ID
	,ProductCode
	,Description
	,IdealRunRate
FROM productcodes
WHERE ID IN (SELECT DISTINCT ProductCodeID FROM dbo.testattributes)
ORDER BY ProductCode