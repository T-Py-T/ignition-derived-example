-- Select all from dbo.lineconfig for a specific line

EXEC [config].[stp_getLineConfig] @lineID = :ID