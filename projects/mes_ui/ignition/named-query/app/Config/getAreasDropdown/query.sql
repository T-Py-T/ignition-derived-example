SELECT area.ID, area.Name, areaconfig.EquipmentPath
from area
INNER JOIN areaconfig on area.ID=areaconfig.AreaID
Where area.SiteID = :SiteID