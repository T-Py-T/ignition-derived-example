exec [sched].[stp_getAllEquipmentSchedule]
		@StartDateTime = :startDateTime,
		@EndDateTime = :endDateTime,
		@AreaID = :areaID,
		@LineID = :lineID,
		@ProductCodeID = :productCodeID

