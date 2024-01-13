exec [sched].[stp_addProductCodeSegments]
		@ProductCodeID = :productCodeID,
		@SegmentID = :segmentID,
		@InputSegmentID = :inputSegmentID,
		@OutputSegmentID = :outputSegmentID,
		@SegmentOrder = :segmentOrder