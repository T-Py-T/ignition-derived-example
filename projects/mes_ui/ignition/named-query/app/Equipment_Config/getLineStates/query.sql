-- Select all from dbo.state for a specific line

EXEC [config].[stp_getLineStates] @lineID = :ID