

logger = system.util.getLogger('mes.enterprise.periodic')
'''
This contains all OEE Stored Porcedure functions
'''
from decorators import error_log, timeit, dump_args


NULL = mes.config._scriptHeaders.NULL #Default global value for NULL database value
dbDateFormat = mes.config._scriptHeaders.dbDateFormat
db = mes.config._scriptHeaders.db
#micro = mes.config._scriptHeaders.micro
#siteID = mes.config._scriptHeaders.siteID
#areas = mes.config._scriptHeaders.areas
#lines = mes.config._scriptHeaders.lines
#TimePeriodDict = mes.config._scriptHeaders.TimePeriodDict
#AggregateDict = mes.config._scriptHeaders.AggregateDict







#@timeit
@error_log
#@dump_args  
def getScrap(equipmentPath, startDate, endDate):
	'''
		returns scrap on an hour by hour basis
	'''
	query = """SELECT SUM(quantity) as scrap, date_trunc('hour', time_recorded) as "roundedTime" 
			FROM scrap.scrap_log
			WHERE equipment_path = ? 
			AND time_recorded BETWEEN ? AND ?
			GROUP BY date_trunc('hour', time_recorded)
			"""
	results = system.db.runPrepQuery(query, [equipmentPath, startDate, endDate], appDB)
	return results


#@timeit
@error_log
#@dump_args  
def getNonRejectScrap(equipmentPath, startDate, endDate):
	'''
		returns scrap on an hour by hour basis
	'''
	query = """SELECT SUM(quantity) as scrap, date_trunc('hour', time_recorded) as "roundedTime" 
			FROM scrap.scrap_log sl
			JOIN scrap.reason sr on sl.reason_id = sr.id
			WHERE equipment_path = ? AND sr.reason_name != 'Machine Rejected'
			AND is_reject = False
			AND time_recorded BETWEEN ? AND ?
			GROUP BY date_trunc('hour', time_recorded)
			"""
	results = system.db.runPrepQuery(query, [equipmentPath, startDate, endDate], appDB)
	return results


#@timeit
@error_log
#@dump_args  
def getScrapCount(equipmentPath, startDate, endDate):
	'''
		returns scrap entries within time range
	'''
	query = """SELECT COUNT(quantity) as "scrapCount"
			FROM scrap.scrap_log
			WHERE equipment_path = ? 
			AND time_recorded BETWEEN ? AND ?
			"""
	results = system.db.runPrepQuery(query, [equipmentPath, startDate, endDate], appDB)
	return results


#@timeit
@error_log
#@dump_args  
def getStartedWorkorders(equipmentPath, startDate, endDate):
	pass


#@timeit
@error_log
#@dump_args  
def getLineUtilization(equipmentPath, startDate, endDate):
	pass


