exec [sched].[stp_editMaterialLot]
		@materialLotID = :materialLotID,
		@lotNumber = :lotNumber,
		@quantity = :quantity,
		@materialID = :materialID