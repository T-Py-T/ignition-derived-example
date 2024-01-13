SELECT r.id, r.reason_name as "reasonName", r.reason_code as "reasonCode", rc.reason_category_name as "reasonCategoryName", r.reason_category_id as "reasonCategoryId"
FROM scrap.Reason r 
INNER JOIN scrap.reason_category rc ON r.reason_category_id = rc.id