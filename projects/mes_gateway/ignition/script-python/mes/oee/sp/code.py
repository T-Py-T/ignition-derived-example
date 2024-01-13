'''
This contains all OEE Stored Porcedure functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders


sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()
areas = sh.getAreas()
siteID = sh.getSiteId()
micro = sh.getMicro()



# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.oee.sp')


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     EXAMPLE SP FUNCTION
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#@timeit
#@error_log
#@dump_args
#def fakeFunction(StartDateTime, EndDateTime, GroupID, LineID):
#	call = system.db.createSProcCall("dbo.stp_getGroupOEE_AQP", db)	
#	call.registerInParam("StartDateTime", system.db.TIMESTAMP, StartDateTime)
#	call.registerInParam("EndDateTime", system.db.TIMESTAMP, EndDateTime)
#	call.registerInParam("GroupID", system.db.INTEGER, GroupID)
#	call.registerInParam("LineID", system.db.INTEGER, LineID)
#	system.db.execSProcCall(call)
#	ret = call.getResultSet()
#	return ret


#@timeit
@error_log
#@dump_args
def getGroupOEE_AQP(StartDateTime, EndDateTime, GroupID):
	"""
	TODO: Function takes "elapsed time: 0.110"
	#Args:
		# StartDateTime (String): timestamp
		# EndDateTime (String): timestamp 
		# GroupID (Integer) : PK for group
	#Testing:
		#StartDateTime = '2022-12-06 06:00:00' 
		#EndDateTime = '2022-12-06 14:00:00'
		#GroupID = 1
		#print(mes.oee.sp.getGroupOEE_AQP(StartDateTime, EndDateTime, GroupID))		
	"""
	
	call = system.db.createSProcCall("oee.stp_getGroupOEE_AQP", db)	
	call.registerInParam("StartDateTime", system.db.TIMESTAMP, StartDateTime)
	call.registerInParam("EndDateTime", system.db.TIMESTAMP, EndDateTime)
	call.registerInParam("GroupID", system.db.INTEGER, GroupID)
	call.registerInParam("LineID", system.db.INTEGER, LineID)
	system.db.execSProcCall(call)
	return call.getResultSet()


#@timeit
@error_log
#@dump_args
def getPeriodAllLinesOEE_AQP(TimePeriod, SiteID=siteID, MicroDuration=micro,
							StartDateTime=None,EndDateTime=None ):
	"""
	TODO: Function takes "elapsed time: _____"
		
	#Args:
		# StartDateTime (String): timestamp
		# EndDateTime (String): timestamp 
		# Site ID (Integer) : PK for area
	#Testing:
		#print(mes.oee.sp.getPeriodAllLinesOEE_AQP('yesterday', 1))	
	"""
	
	call = system.db.createSProcCall("oee.stp_getPeriodAllLinesOEE_AQP", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, TimePeriod)
	call.registerInParam("StartDateTime", system.db.TIMESTAMP, StartDateTime)
	call.registerInParam("EndDateTime", system.db.TIMESTAMP, EndDateTime)
	call.registerInParam("SiteID", system.db.INTEGER, SiteID)
	call.registerInParam("microDur", system.db.INTEGER, MicroDuration)
	system.db.execSProcCall(call)
	return call.getResultSet()	

	
#@timeit
@error_log
#@dump_args
def getPeriodAreaOEE_AQP(TimePeriod, AreaID=None, SiteID=siteID):
	"""
	TODO: Function takes "elapsed time: _____"
		
	#Args:
		# AreaID (Integer) : PK for area
	#Testing:
		#print(mes.oee.sp.getPeriodAreaOEE_AQP('yesterday', 1))	
	"""
	
	call = system.db.createSProcCall("oee.stp_getPeriodAreaOEE_AQP", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, TimePeriod)
	call.registerInParam("AreaID", system.db.INTEGER, AreaID)
	call.registerInParam("SiteID", system.db.INTEGER, SiteID)
	system.db.execSProcCall(call)
	return call.getResultSet()

#@timeit
@error_log
#@dump_args
def getPeriodAreaOEETable(TimePeriod, AreaID, SiteID=siteID, MicroDuration=micro):
	"""
	TODO: Function takes "elapsed time: _____"
		
	#Args:
		# AreaID (Integer) : PK for area
	#Testing:
		#print(mes.oee.sp.getPeriodAreaOEETable('yesterday', 2))	
	"""
	call = system.db.createSProcCall("oee.stp_getPeriodAreaOEETable", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, TimePeriod)
	call.registerInParam("AreaID", system.db.INTEGER, AreaID)
	call.registerInParam("SiteID", system.db.INTEGER, SiteID)
	call.registerInParam("microDur", system.db.INTEGER, MicroDuration)
	system.db.execSProcCall(call)
	return call.getResultSet()


#@timeit
@error_log
#@dump_args
def getPeriodSiteOEE_AQP(TimePeriod, SiteID=siteID, MicroDuration=micro):
	"""
	TODO: Function takes "elapsed time: _____"
		
	#Args:
		# SiteID (Integer) : PK for site
	#Testing:
		#StartDateTime = '2022-12-06 06:00:00' 
		#EndDateTime = '2022-12-06 14:00:00'
		#SiteID = 1
		#print(mes.oee.sp.getSiteOEE_AQP(StartDateTime, EndDateTime, SiteID))		
	"""
	
	call = system.db.createSProcCall("oee.stp_getPeriodSiteOEE_AQP", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, TimePeriod)
	call.registerInParam("SiteID", system.db.INTEGER, SiteID)
	call.registerInParam("microDur", system.db.INTEGER, MicroDuration)
	system.db.execSProcCall(call)
	return call.getResultSet()
	
#@timeit
@error_log
#@dump_args
def getPeriodParetoChart(startTime, endTime, lineID, productCodeID, interval):
	"""
    This function generates a Pareto chart for a specific period, line, and product code, using data from a stored procedure.

    Args:
        startTime (Timestamp): The starting time of the period.
        endTime (Timestamp): The ending time of the period.
        lineID (Integer): The ID of the production line.
        productCodeID (Integer): The ID of the product code.
        interval (Integer): The interval for data aggregation.

    Returns:
        ResultSet: A result set containing the data for the Pareto chart.

    Testing:
        # Example usage:
        # StartDateTime = '2022-12-06 06:00:00' 
        # EndDateTime = '2022-12-06 14:00:00'
        # LineID = 1
        # ProductCodeID = 101
        # Interval = 60 (minutes)
        # result = getPeriodParetoChart(StartDateTime, EndDateTime, LineID, ProductCodeID, Interval)
        # print(result)
    """

	call = system.db.createSProcCall("testing.test_getDatesLineProductionCounts", db)	
	call.registerInParam("StartDateTime", system.db.TIMESTAMP, startTime)
	call.registerInParam("EndDateTime", system.db.TIMESTAMP, endTime)
	call.registerInParam("LineID", system.db.INTEGER, lineID)
	call.registerInParam("ProductCodeID", system.db.INTEGER, productCodeID)
	call.registerInParam("interval", system.db.INTEGER, interval)
	system.db.execSProcCall(call)
	pyData = system.dataset.toPyDataSet(call.getResultSet())
	return pyData