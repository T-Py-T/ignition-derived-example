SELECT reason_code, id as "value", reason_name as "label" FROM scrap.reason WHERE reason_category_id = :reasonCategoryId