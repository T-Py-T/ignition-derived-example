exec [sched].[stp_editWorkOrder]
		@WorkOrderName = :workOrderName,
		@WorkOrderID = :workOrderID,
		@Quantity = :quantity,
		@Closed = :closed,
		@Hide = :hide,
		@ProductCodeID = :productCodeID,
		@RequiredEndDate = :requiredEndDate