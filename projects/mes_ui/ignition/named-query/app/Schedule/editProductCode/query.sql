exec [sched].[stp_editProductCode]
		@ProductCodeID = :productCodeID,
		@ProductCode = :productCode,
		@Description = :description,
		@Enabled = :enabled,
		@IdealRunRate = :idealRunRate,
		@RateUoM = :rateUoM,
		@PerUnitCost = :perUnitCost,
		@Instructions = :instructions