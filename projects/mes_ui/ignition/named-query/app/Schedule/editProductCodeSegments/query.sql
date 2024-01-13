exec [sched].[stp_editProductCodeSegments]
		@ProductCodeID = :productCodeID,
		@SegmentID = :segmentID,
		@InputSegmentID = :inputSegmentID,
		@OutputSegmentID = :outputSegmentID,
		@SegmentOrder = :segmentOrder,
		@ProductCodeSegmentID = :productSegmentID
		