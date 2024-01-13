SELECT sc.EquipmentPath as 'TagPath'
from sites s
INNER JOIN siteconfig  sc on s.ID=sc.SiteID
Where s.ID = :SiteID