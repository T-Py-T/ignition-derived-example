exec [qms].[stp_UpsertTestType]
		@TestName =  :TestName ,
		@TestTypeCategoryID =  :TestTypeCategory ,
		@Description =  :Description ,
		@SiteID =  :SiteID ,
		@IsEnabled =  :IsEnabled 