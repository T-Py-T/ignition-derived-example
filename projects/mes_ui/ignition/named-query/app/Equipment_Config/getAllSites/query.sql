select s.ID, s.Name, sc.EquipmentPath as 'TagPath', s.IsEnabled  from dbo.sites s
join siteconfig sc on s.ID = sc.SiteID 
where s.EnterpriseID  = :enterpriseID and IsEnabled <> 0