SELECT -- area.ID, 
	a.Name as 'Title', ac.EquipmentPath as 'TagPath'
from area a
INNER JOIN areaconfig ac on a.ID=ac.AreaID
Where a.SiteID = :SiteID