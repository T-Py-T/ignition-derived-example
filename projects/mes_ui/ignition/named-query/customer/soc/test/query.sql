
select * from (SELECT REPLACE(TagName,'_',' ') TagName, SOCValue
 
FROM fb.SOC_FinalValues v

INNER JOIN fb.SOC_Header h ON h.ID = v.HeaderID AND h.ProductFamily = :Product AND h.Color = :Color
 
INNER JOIN dbo.lines l ON l.ID = h.LineID AND l.[Name] = :Line
 
INNER JOIN fb.SOC_ToolLines tl ON tl.IsEnabled = 1 AND tl.ID = h.ToolID AND tl.Tool = :ToolID
 
INNER JOIN fb.SOC_Categories c ON c.IsEnabled = 1 AND c.ID = v.CategoryID AND CategoryName = 'barrel_zone' and CategoryValue = :Rate

UNION

SELECT REPLACE(TagName,'_',' ') TagName, SOCValue
 
FROM fb.SOC_FinalValues v

INNER JOIN fb.SOC_Header h ON h.ID = v.HeaderID AND h.ProductFamily = :Product AND h.Color = :Color
 
INNER JOIN dbo.lines l ON l.ID = h.LineID AND l.[Name] = :Line
 
INNER JOIN fb.SOC_ToolLines tl ON tl.IsEnabled = 1 AND tl.ID = h.ToolID AND tl.Tool = :ToolID
 
INNER JOIN fb.SOC_Categories c ON c.IsEnabled = 1 AND c.ID = v.CategoryID AND CategoryName = 'die_zone' and CategoryValue = :Rate

UNION

SELECT REPLACE(TagName,'_',' ') TagName, SOCValue
 
FROM fb.SOC_FinalValues v

INNER JOIN fb.SOC_Header h ON h.ID = v.HeaderID AND h.ProductFamily = :Product AND h.Color = :Color
 
INNER JOIN dbo.lines l ON l.ID = h.LineID AND l.[Name] = :Line
 
INNER JOIN fb.SOC_ToolLines tl ON tl.IsEnabled = 1 AND tl.ID = h.ToolID AND tl.Tool = :ToolID
 
INNER JOIN fb.SOC_Categories c ON c.IsEnabled = 1 AND c.ID = v.CategoryID AND CategoryName = 'capstock_mb' and CategoryValue = :Rate

UNION

SELECT REPLACE(TagName,'_',' ') TagName, SOCValue
 
FROM fb.SOC_FinalValues v

INNER JOIN fb.SOC_Header h ON h.ID = v.HeaderID AND h.ProductFamily = :Product AND h.Color = :Color
 
INNER JOIN dbo.lines l ON l.ID = h.LineID AND l.[Name] = :Line
 
INNER JOIN fb.SOC_ToolLines tl ON tl.IsEnabled = 1 AND tl.ID = h.ToolID AND tl.Tool = :ToolID
 
INNER JOIN fb.SOC_Categories c ON c.IsEnabled = 1 AND c.ID = v.CategoryID AND CategoryName = 'co_extruders' and CategoryValue = :Rate

UNION

SELECT REPLACE(TagName,'_',' ') TagName, SOCValue
 
FROM fb.SOC_FinalValues v

INNER JOIN fb.SOC_Header h ON h.ID = v.HeaderID AND h.ProductFamily = :Product AND h.Color = :Color
 
INNER JOIN dbo.lines l ON l.ID = h.LineID AND l.[Name] = :Line
 
INNER JOIN fb.SOC_ToolLines tl ON tl.IsEnabled = 1 AND tl.ID = h.ToolID AND tl.Tool = :ToolID
 
INNER JOIN fb.SOC_Categories c ON c.IsEnabled = 1 AND c.ID = v.CategoryID AND CategoryName = 'general_setup' and CategoryValue = :Rate

UNION

SELECT REPLACE(TagName,'_',' ') TagName, SOCValue
 
FROM fb.SOC_FinalValues v

INNER JOIN fb.SOC_Header h ON h.ID = v.HeaderID AND h.ProductFamily = :Product AND h.Color = :Color
 
INNER JOIN dbo.lines l ON l.ID = h.LineID AND l.[Name] = :Line
 
INNER JOIN fb.SOC_ToolLines tl ON tl.IsEnabled = 1 AND tl.ID = h.ToolID AND tl.Tool = :ToolID
 
INNER JOIN fb.SOC_Categories c ON c.IsEnabled = 1 AND c.ID = v.CategoryID AND CategoryName = 'secondary_embosser' and CategoryValue = :Rate

WHERE v.RevisionEndDate IS NULL) a

ORDER BY CASE 
WHEN TagName = 'feed barrel zone' THEN 1
WHEN TagName = 'barrel zone 1' THEN 2
WHEN TagName = 'barrel zone 2' THEN 3
WHEN TagName = 'barrel zone 3' THEN 4
WHEN TagName = 'barrel zone 4' THEN 5
WHEN TagName = 'barrel zone 5' THEN 6
WHEN TagName = 'barrel zone 6' THEN 7
WHEN TagName = 'barrel zone 7' THEN 8
WHEN TagName = 'barrel zone 8' THEN 9
WHEN TagName = 'barrel zone 9' THEN 10
WHEN TagName = 'barrel zone 10' THEN 11
WHEN TagName = 'barrel zone 11' THEN 12
WHEN TagName = 'barrel zone 12' THEN 13
WHEN TagName = 'adapter temp' THEN 14 
WHEN TagName = 'die zone 1' THEN 15
WHEN TagName = 'die zone 2' THEN 16
WHEN TagName = 'die zone 3' THEN 17
WHEN TagName = 'die zone 4' THEN 18
WHEN TagName = 'die zone 5' THEN 19
WHEN TagName = 'die zone 6' THEN 20
WHEN TagName = 'die zone 7' THEN 21
WHEN TagName = 'die zone 8' THEN 22
WHEN TagName = 'die zone 9' THEN 23
WHEN TagName = 'die zone 10' THEN 24
WHEN TagName = 'die zone 11' THEN 25
WHEN TagName = 'die zone 12' THEN 26
WHEN TagName = 'die zone 13' THEN 27
WHEN TagName = 'die zone 14' THEN 28
WHEN TagName = 'capstock MB hopper 1' THEN 29
WHEN TagName = 'capstock MB hopper 2' THEN 30
WHEN TagName = 'capstock MB hopper 4' THEN 31
WHEN TagName = 'co extruder rpm s1' THEN 32
WHEN TagName = 'co ex barrel temp z1 s1' THEN 33
WHEN TagName = 'co ex barrel temp z2 s1' THEN 34
WHEN TagName = 'co ex barrel temp z3 s1' THEN 35
WHEN TagName = 'co ex barrel temp z4 s1' THEN 36
WHEN TagName = 'co ex tool die temp z1 s1' THEN 37
WHEN TagName = 'co ex tool die temp z2 s1' THEN 38
WHEN TagName = 'co ex tool die temp z3 s1' THEN 39
WHEN TagName = 'co ex clamp temp s1' THEN 40
WHEN TagName = 'co extruder rpm s2' THEN 41
WHEN TagName = 'co ex barrel temp z1 s2' THEN 42
WHEN TagName = 'co ex barrel temp z2 s2' THEN 43
WHEN TagName = 'co ex barrel temp z3 s2' THEN 44
WHEN TagName = 'co ex barrel temp z4 s2' THEN 45
WHEN TagName = 'co ex tool die temp z1 s2' THEN 46
WHEN TagName = 'co ex tool die temp z2 s2' THEN 47
WHEN TagName = 'co ex tool die temp z3 s2' THEN 48
WHEN TagName = 'co ex clamp temp s2' THEN 49
WHEN TagName = 'co ex load range s1' THEN 50
WHEN TagName = 'co ex melt pressure s1' THEN 51
WHEN TagName = 'co ex melt temp s1' THEN 52
WHEN TagName = 'co ex load range s2' THEN 53
WHEN TagName = 'co ex melt pressure s2' THEN 54
WHEN TagName = 'co ex melt temp s2' THEN 55
WHEN TagName = 'extruder rpm' THEN 56
WHEN TagName = 'main drive current' THEN 57
WHEN TagName = 'secondary_emboss_side1_bottom_wheel_air_pressure' THEN 58
WHEN TagName = 'secondary_emboss_side1_top_wheel_air_pressure' THEN 59
WHEN TagName = 'secondary_emboss_side1_top_wheel_temp' THEN 60
WHEN TagName = 'secondary_emboss_side1_bottom_wheel_temp' THEN 61
WHEN TagName = 'secondary_emboss_side1_brush_run_sec' THEN 62
WHEN TagName = 'secondary_emboss_side1_brush_interval_min' THEN 63
WHEN TagName = 'secondary_emboss_side2_bottom_wheel_air_pressure' THEN 64
WHEN TagName = 'secondary_emboss_side2_top_wheel_air_pressure' THEN 65
WHEN TagName = 'secondary_emboss_side2_top_wheel_temp' THEN 66
WHEN TagName = 'secondary_emboss_side2_bottom_wheel_temp' THEN 67
WHEN TagName = 'secondary_emboss_side2_brush_run_sec' THEN 68
WHEN TagName = 'secondary_emboss_side2_brush_interval_min' THEN 69

ELSE 70
END asc

