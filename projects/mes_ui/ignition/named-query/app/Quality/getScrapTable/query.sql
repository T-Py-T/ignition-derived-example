EXEC [qms].[stp_getScrapTable]
		@StartTime = :startTime,
		@EndTime = :endTime,
		@LineID = :lineID,
		@Shift = :shift,
		@ProductCode = :productCode,
		@Top = :top