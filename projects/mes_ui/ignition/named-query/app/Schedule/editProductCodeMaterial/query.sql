exec [sched].[stp_editProductCodeMaterial]
		@ProductCodeID = :productCodeID,
		@MaterialID = :materialID,
		@RequiredQuantity = :requiredQuantity,
		@ProductCodeMaterialID = :productCodeMaterialID