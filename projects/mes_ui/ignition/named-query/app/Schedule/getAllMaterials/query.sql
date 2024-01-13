--SELECT *
--FROM materials 

EXEC [sched].[stp_getMaterials] @siteID = :ID

