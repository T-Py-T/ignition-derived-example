DECLARE	@return_value int

EXEC	@return_value = [qms].[stp_UpsertTestTypeCategory]
		@ID = :categoryID,
		@TestCategoryName =  :TestCategoryName 

SELECT	'Return Value' = @return_value