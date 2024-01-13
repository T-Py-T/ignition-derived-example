exec report.stp_getLinesLossSummaryDetails
        @StartDateTime = :startTime,
        @EndDateTime = :endTime,
        @SiteID = :siteID,
		@line = :lineID,
		@area = :area,
		@shift = :shift,
		@productCode = :productCode,
		@type = :type