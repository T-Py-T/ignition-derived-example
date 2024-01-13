SELECT id, time_begin as "timeBegin", time_end as "timeEnd"
FROM sap.planned_outage
WHERE time_end >= now()
