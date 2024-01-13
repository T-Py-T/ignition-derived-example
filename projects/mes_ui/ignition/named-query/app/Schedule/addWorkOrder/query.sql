exec [sched].[stp_addWorkOrder]
		@WorkOrder = :workOrder,
		@Quantity = :quantity,
		@Closed = :closed,
		@Hide = :hide,
		@ProductCodeID = :productCodeID,
		@RequiredEndDate = :requiredEndDate