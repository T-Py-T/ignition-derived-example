Select distinct
t1.ProductFamily as 'Product',
t1.ID,
t1.Color as 'Color',
t3.CategoryValue as 'Rate',
t4.Tool as 'ToolID',
t5.Name as 'Line'
from [MES].[fb].[SOC_Header] t1
inner join [MES].[fb].[SOC_FinalValues] t2
on (t2.HeaderID = t1.ID and t2.RevisionEndDate IS NULL)
inner join  [MES].[fb].[SOC_Categories] t3
on t3.ID = t2.CategoryID
inner join [MES].[fb].[SOC_ToolLines] t4
on (t4.ID = t1.ToolID AND t4.ActiveEndDate IS NULL)
inner join [MES].[dbo].[lines] t5
on t5.ID = t1.LineID
Order by t5.Name