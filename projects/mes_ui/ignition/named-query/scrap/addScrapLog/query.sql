INSERT INTO scrap.scrap_log
           (reason_id
           ,recorded_user_id
           ,line_id
           ,equipment_path
           ,product_code
           ,planned_order
           ,quantity
           ,shift
           ,is_reject_boolean
           ,time_recorded
           ,is_badge)
VALUES (:reasonId
		,:userId
		,:lineID
		,:eqPath
		,:productCode
		,:plannedOrder
		,:quantity
		,:shift
		,:isRejectBoolean
		,:time
		,:isBadge)