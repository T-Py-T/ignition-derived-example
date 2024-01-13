exec [sched].[stp_addProductCode]
		@ProductCode = :productCode,
		@Description = :description,
		@Enabled = :enabled,
		@IdealRunRate = :idealRunRate,
		@RateUoM = :rateUoM,
		@PerUnitCost = :perUnitCost,
		@Instructions = :instructions