EXEC [dashboard].[stp_saveUserConfig] 
		@UserName = :userName, 
		@LeftDashboard = :leftDashboard, 
		@RightDashboard = :rightDashboard,
		@LineID = :lineID