EXEC [qms].[stp_getScrapPareto]
		@StartTime = :startTime,
		@EndTime = :endTime,
		@LineID = :lineID,
		@Shift = :shift,
		@ProductCode = :productCode,
		@Top = :top