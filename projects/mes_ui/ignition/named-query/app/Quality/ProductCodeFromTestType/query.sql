select DISTINCT(t.ProductCodeID) as 'ID', p.ProductCode , p.Description, p.IdealRunRate  FROM [MES].[dbo].[testattributes] t
join productcodes p on p.ID = t.ProductCodeID
  where TestTypeID =  :TestTypeID 