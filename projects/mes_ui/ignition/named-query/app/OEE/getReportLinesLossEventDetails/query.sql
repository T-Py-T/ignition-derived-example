exec report.stp_getLinesLossEventDetails
        @StartDateTime = :startTime,
        @EndDateTime = :endTime,
        @SiteID = :siteID,
		@line = :lineID,
		@area = :areaID,
		@shift = :shift,
		@type = :type,
		@productCode = :productCode