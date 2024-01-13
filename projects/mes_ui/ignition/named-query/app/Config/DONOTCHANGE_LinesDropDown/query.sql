SELECT l.Name, lc.EquipmentPath  as 'TagPath'
from line l
INNER JOIN lineconfig lc on l.ID = lc.lineID
Where l.AreaID = :AreaID