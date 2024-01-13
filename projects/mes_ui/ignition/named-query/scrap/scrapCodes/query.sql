SELECT r.id, r.reason_name as "reasonName", r.reason_code as "reasonCode", rc.reason_category_name as "reasonCategoryName", rc.id as "reasonCategoryId"
FROM scrap.reason r 
RIGHT JOIN scrap.reason_category rc ON r.reason_category_id = rc.id
WHERE r.time_retired IS NULL and rc.time_retired IS NULL