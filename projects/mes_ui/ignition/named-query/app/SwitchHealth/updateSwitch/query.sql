exec [dbo].[stp_updateSwitch]
		@AssetID = :assetID,
		@Ncc = :ncc,
		@Switch = :switch,
		@ID = :switchID,
		@PlcAddress = :plcAddress
		