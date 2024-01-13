EXEC [oee].[stp_getDatesLineProductionCounts] 
		@StartDateTime = :startDate, 
		@EndDateTime = :endDate,
		@lineID = :lineID,
		@Interval = :interval