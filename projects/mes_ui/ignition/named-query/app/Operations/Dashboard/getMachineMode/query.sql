--SELECT CurrentDateTime, LineID, ModeID, u.ID, u.Description
--FROM modecurrent
--LEFT JOIN mode u ON u.ID = ModeID
--WHERE LineID = :LineID

SELECT ReasonCode, Description FROM modes 
WHERE ReasonCode = :ModeID