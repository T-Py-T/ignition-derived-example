exec [sched].[stp_addSchedule]
		@LineID = :lineID,
		@WorkOrderID = :workOrderID,
		@Note = :note,
		@ScheduleStartDateTime = :scheduleStartDateTime,
		@ScheduleEndDateTime = :scheduleEndDateTime,
		@Quantity = :quantity,
		@EnteredBy = :enteredBy
		