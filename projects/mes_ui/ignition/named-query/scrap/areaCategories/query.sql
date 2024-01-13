SELECT a.id, a.equipment_path as "equipmentPath", rc.reason_category_name as "reasonCategoryName"
FROM scrap.area_category a
RIGHT JOIN scrap.reason_category rc ON a.reason_category_id = rc.id