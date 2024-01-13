SELECT equipment_path as "equipmentPath"
FROM equipment.configured_line 
WHERE sap_cell_name = :sapCellName