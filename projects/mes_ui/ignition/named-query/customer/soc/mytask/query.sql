DECLARE @DaysBack int = -30, @DT_Start datetime
 
IF @DaysBack > 0 -- If a positive number is given, make it negative.
  SET @DaysBack = -@DaysBack
 
SET @DT_Start = DATEADD(day,@DaysBack,GETDATE()); --Limits query to only pull records  >= this date.
 
SELECT x.ProductFamily as 'Product' ,x.Color,x.Line ,x.StartRunDate as 'Start Run Date'
FROM(
  SELECT DISTINCT (SELECT [Name] FROM dbo.lines l WHERE l.[Name] = 'Line '+SUBSTRING(ps.Extruder,CHARINDEX(' ', ps.Extruder)+2,2) COLLATE DATABASE_DEFAULT) Line
    ,p.Attribute_Char2 COLLATE DATABASE_DEFAULT Color, p.Attribute_Char4 COLLATE DATABASE_DEFAULT ProductFamily
    ,MIN(ps.StartRunDate) StartRunDate
  FROM [NLIASQL01].[InductiveSupplementaryData].[dbo].[ProductionSchedule] ps
  INNER JOIN [NLIASQL01].[InductiveSupplementaryData].[dim].[part] p ON p.PartNumber =  ps.PartNumber AND ps.Plant = '1NL' AND p.MajorSalesGroupDescription1 = 'Decking'
  WHERE ps.[Status] = 'Released' AND ps.StartRunDate >= @DT_Start AND ps.Extruder LIKE 'EXTRUDER%'
  GROUP BY ps.Extruder,p.Attribute_Char2,p.Attribute_Char4
)x
WHERE Line IS NOT NULL
  AND NOT EXISTS (SELECT 1 
                  FROM fb.SOC_Header h 
                  INNER JOIN fb.SOC_FinalValues v ON h.ID = v.HeaderID AND v.RevisionEndDate IS NULL
                  WHERE h.ProductFamily = x.ProductFamily AND h.Color = x.Color AND h.LineID = (SELECT ID FROM dbo.lines l WHERE l.[Name] = x.Line))
ORDER BY StartRunDate;