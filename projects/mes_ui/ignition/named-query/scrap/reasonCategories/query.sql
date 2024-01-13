SELECT id, reason_category_name as "reasonCategoryName"
FROM scrap.reason_category 
WHERE time_retired IS NULL