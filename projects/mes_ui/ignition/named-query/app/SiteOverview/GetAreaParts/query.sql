SELECT area.Name, areaconfig.EquipmentPath, areaconfig.AreaID
from area
INNER JOIN areaconfig on area.ID=areaconfig.AreaID
Where area.SiteID = :SiteID