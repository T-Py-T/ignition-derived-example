SELECT areas.ID, 
	areas.Name as 'Title', areaconfig.EquipmentPath as 'TagPath', IsEnabled
from areas
INNER JOIN areaconfig on areas.ID=areaconfig.AreaID
Where areas.SiteID = :siteID AND areas.IsEnabled <> 0
