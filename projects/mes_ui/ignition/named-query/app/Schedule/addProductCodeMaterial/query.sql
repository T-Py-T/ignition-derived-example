exec [sched].[stp_addProductCodeMaterial]
		@ProductCodeID = :productCodeID,
		@MaterialID = :materialID,
		@RequiredQuantity = :requiredQuantity