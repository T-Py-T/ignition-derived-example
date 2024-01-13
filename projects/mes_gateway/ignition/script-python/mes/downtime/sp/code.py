'''
This contains all Downtime Code Highlighting Stored Porcedure functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders


sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()
dbDateFormat = sh.getDateFormat()
micro = sh.getMicro()
siteID = sh.getSiteId()

#NULL = mes.config._scriptHeaders.NULL #Default global value for NULL database value
#dbDateFormat = mes.config._scriptHeaders.dbDateFormat
#db = mes.config._scriptHeaders.db
#micro = mes.config._scriptHeaders.micro
#siteID = mes.config._scriptHeaders.siteID
#areas = mes.config._scriptHeaders.areas
#lines = mes.config._scriptHeaders.lines
#TimePeriodDict = mes.config._scriptHeaders.TimePeriodDict
#AggregateDict = mes.config._scriptHeaders.AggregateDict


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.downtime.periodic')


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     EXAMPLE SP FUNCTION
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#@timeit
#@error_log
#@dump_args
#def groupOEE_AQP(StartDateTime, EndDateTime, GroupID, LineID):
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
def getPeriodLineStateTimeline(timePeriod, lineID, interval):
	"""
	TODO: Function takes "elapsed time: 0.110"
	Args:
		StartDateTime (String): timestamp
		EndDateTime (String): timestamp 
		GroupID (Integer) : PK for group
	Testing:
		StartDateTime = '2022-12-06 06:00:00' 
		EndDateTime = '2022-12-06 14:00:00'
		GroupID = 1
		print(mes.oee.sp.getGroupOEE_AQP(StartDateTime, EndDateTime, GroupID))		
	"""
	call = system.db.createSProcCall("dt.stp_getPeriodLineProgress", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	call.registerInParam("lineID", system.db.INTEGER, lineID)
	call.registerInParam("interval", system.db.INTEGER, interval)
	system.db.execSProcCall(call)
	return call.getResultSet()


#@timeit
@error_log
#@dump_args
def getPeriodAllLinesPlannedUnplannedDT(timePeriod):
	"""
	TODO: Function takes "elapsed time: _____"
	Args:
		timePeriod (String) : 'current shift','yesterday'
	Testing:
		print(mes.downtime.sp.getPeriodAllLinesPlannedUnplannedDT('current shift'))	
	"""
	call = system.db.createSProcCall("dt.stp_getPeriodAllLinesPlannedUnplannedDT", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	system.db.execSProcCall(call)
	return call.getResultSet()	


#@timeit
@error_log
#@dump_args
def getPeriodAllLinesStateSummary(timePeriod):
	"""
	TODO: Function takes "elapsed time: _____"
	Args:
		Site ID (Integer) : PK for area
	Testing:
		print(mes.downtime.sp.getPeriodAllLinesStateSummary('yesterday'))		
	"""
	call = system.db.createSProcCall("dt.stp_getPeriodAllLinesStateSummary", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	system.db.execSProcCall(call)
	return call.getResultSet()	

#@timeit
@error_log
#@dump_args
def getPeriodAllLinesDTEvents(timePeriod):
	"""
	TODO: Function takes "elapsed time: _____"
	Args:
		Site ID (Integer) : PK for area
	Testing:
		print(mes.downtime.sp.getPeriodAllLinesDTEvents('current shift'))		
	"""
	call = system.db.createSProcCall("dt.stp_getPeriodAllLinesDTEvents", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	system.db.execSProcCall(call)
	return call.getResultSet()	

#@timeit
@error_log
#@dump_args
def getPeriodAllLinesDTEventsComposite(timePeriod):
	"""
	TODO: Function takes "elapsed time: _____"
	Args:
		Site ID (Integer) : PK for area
	Testing:
		print(mes.downtime.sp.getPeriodAllLinesDTEventsComposite('current shift'))		
	"""
	call = system.db.createSProcCall("dt.stp_getPeriodAllLinesDTEventsCompositeByLine", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	system.db.execSProcCall(call)
	return call.getResultSet()	
	
#@timeit
@error_log
#@dump_args
def getPeriodAllLinesStateTimeline(timePeriod, interval=0):
	"""
	TODO: Function takes "elapsed time: _____"
	Args:
		Site ID (Integer) : PK for area
	Testing:
		print(mes.downtime.sp.getPeriodAllLinesStateTimeline('current shift'))		
	"""
	call = system.db.createSProcCall("dt.stp_getPeriodAllLinesStateTimeline", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	call.registerInParam("interval", system.db.INTEGER, interval)
	system.db.execSProcCall(call)
	return call.getResultSet()	

#@timeit
@error_log
#@dump_args
def getPeriodAllLinesTop5DTMicro(timePeriod, microDuration):
	"""
	TODO: Function takes "elapsed time: _____"
	Args:
		timePeriod (String) : 'current shift','yesterday'
	Testing:
		print(mes.downtime.sp.getPeriodAllLinesStateSummary('current shift'))	
	"""
	call = system.db.createSProcCall("dt.stp_getPeriodAllLinesTop5DTMicro", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	call.registerInParam("microDuration", system.db.INTEGER, microDuration)
	system.db.execSProcCall(call)
	return call.getResultSet()	
	

#@timeit
@error_log
#@dump_args
def getPeriodAllLinesTop5DT(timePeriod, microDuration):
	"""
	TODO: Function takes "elapsed time: _____"
	Args:
		timePeriod (String) : 'current shift','yesterday'
	Testing:
		print(mes.downtime.sp.getPeriodAllLinesStateSummary('current shift'))	
	"""
	call = system.db.createSProcCall("dt.stp_getPeriodAllLinesTop5DT", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	call.registerInParam("microDuration", system.db.INTEGER, microDuration)
	system.db.execSProcCall(call)
	return call.getResultSet()	
	

#@timeit
@error_log
#@dump_args
def getPeriodLineCallsEvents(timePeriod, lineID):
	"""
	#TODO: Function takes "elapsed time: _____"
	#Args:
		# timePeriod (String): Name of shift
		# lineID (Integer) : PK for line
	#Testing:
		#timePeriod = 'current shift'
		#lineID = 20
		#print(mes.downtime.sp.getPeriodLineCallsEvents(timePeriod, lineID))		
	"""
	call = system.db.createSProcCall("dt.stp_getPeriodLineCallsEvents", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	call.registerInParam("lineID", system.db.INTEGER, lineID)
	system.db.execSProcCall(call)
	return call.getResultSet()
	
#@timeit
@error_log
#@dump_args
def getCallsPreviousEventID(lineID):
	"""
	#TODO: Function takes "elapsed time: _____"
	#Args:
		# lineID (Integer) : PK for line
	#Testing:
		#lineID = 20
		#print(mes.downtime.sp.getCallsPreviousEventID(lineID))		
	"""
	call = system.db.createSProcCall("dt.stp_getCallsPreviousEventID", db)	
	call.registerInParam("lineID", system.db.INTEGER, lineID)
	system.db.execSProcCall(call)
	return call.getResultSet()

#@timeit
@error_log
#@dump_args
def checkEventReasonID(eventID):
	"""
	#TODO: Function takes "elapsed time: _____"
	#Args:
		# reasonID (Integer) : PK for line
	#Testing:
		#reasonID = 20
		#print(mes.downtime.sp.checkEventReasonID(reasonID))		
	"""
	call = system.db.createSProcCall("dt.stp_checkModeEventID", db)	
	call.registerInParam("EventID", system.db.INTEGER, eventID)
	system.db.execSProcCall(call)
	return call.getResultSet()

#@timeit
@error_log
#@dump_args
def upsertEventCallsReason(modeEventID, reasonID, userName, notes):
	"""
	#TODO: Function takes "elapsed time: _____"
	#Args:
		# modeEventID (Integer) : PK for line
		# reasonID (Integer) : PK for line
		# userName (String) : String username
		# notes (String) : String notes.
	#Testing:
		#reasonID = 20
		#print(mes.downtime.sp.upsertEventCallsReason(modeEventID, reasonID, userName, notes)))		
	"""
	call = system.db.createSProcCall("dt.stp_upsertEventCallsReason", db)	
	call.registerInParam("modeEventID", system.db.INTEGER, modeEventID)
	call.registerInParam("reasonID", system.db.INTEGER, reasonID)
	call.registerInParam("sequence", system.db.INTEGER, 1)
	call.registerInParam("userName", system.db.VARCHAR, userName)
	call.registerInParam("notes", system.db.VARCHAR, notes)
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False

#@timeit
@error_log
#@dump_args
def getGroupDT_Top5(StartDateTime, EndDateTime, GroupID):
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
		#print(mes.downtime.sp.getGroupOEE_AQP(StartDateTime, EndDateTime, GroupID))		
	"""
	call = system.db.createSProcCall("oee.stp_GroupDT_Top5", "MSSQL_MES")	
	call.registerInParam("StartDateTime", system.db.TIMESTAMP, StartDateTime)
	call.registerInParam("EndDateTime", system.db.TIMESTAMP, EndDateTime)
	call.registerInParam("GroupID", system.db.INTEGER, GroupID)
	system.db.execSProcCall(call)
	return call.getResultSet()


#@timeit
@error_log
#@dump_args
def getPeriodAreaTop5DT(timePeriod, areaID, lineID=0, microDuration=micro):
	"""
	#TODO: Function takes "elapsed time: _____"
		
	#Args:
		# StartDateTime (String): timestamp
		# AreaID (Integer) : PK for area
	#Testing:
		#timePeriod = 'last shift'
		#areaID = 1
		#print(mes.downtime.sp.getPeriodAreaTop5DT(timePeriod, areaID))		
	"""
	call = system.db.createSProcCall("dt.stp_getPeriodAreaTop5DT", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	call.registerInParam("areaID", system.db.INTEGER, areaID)
	call.registerInParam("lineID", system.db.INTEGER, lineID)
	call.registerInParam("microDuration", system.db.INTEGER, microDuration)
	system.db.execSProcCall(call)
	return call.getResultSet()
	
	
#@timeit
@error_log
#@dump_args
def getPeriodAreaTop5DTMicro(timePeriod, areaID, lineID=0, microDuration=micro):
	"""
	#TODO: Function takes "elapsed time: _____"
		
	#Args:
		# StartDateTime (String): timestamp
		# AreaID (Integer) : PK for area
	#Testing:
		#timePeriod = 'last shift'
		#areaID = 1
		#print(mes.downtime.sp.getPeriodAreaTop5DT(timePeriod, areaID))		
	"""
	call = system.db.createSProcCall("dt.stp_getPeriodAreaTop5DTMicro", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	call.registerInParam("areaID", system.db.INTEGER, areaID)
	call.registerInParam("lineID", system.db.INTEGER, lineID)
	call.registerInParam("microDuration", system.db.INTEGER, microDuration)
	system.db.execSProcCall(call)
	return call.getResultSet()
	

#@timeit
@error_log
#@dump_args
def getPeriodSiteTop5DT(timePeriod, siteID, microDuration=micro):
	"""
	#TODO: Function takes "elapsed time: _____"
	#Args:
		# StartDateTime (String): timestamp
		# SiteID (Integer) : PK for site
	#Testing:
		#timePeriod = 'last shift'
		#siteID = 1
		#print(mes.downtime.sp.getPeriodSiteTop5DT(timePeriod, siteID))		
	"""
	call = system.db.createSProcCall("dt.stp_getPeriodSiteTop5DT", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	call.registerInParam("siteID", system.db.INTEGER, siteID)
	call.registerInParam("microDuration", system.db.INTEGER, microDuration)
	system.db.execSProcCall(call)
	return call.getResultSet()


#@timeit
@error_log
#@dump_args
def getPeriodSiteTop5DTMicro(timePeriod, siteID, microDuration=micro):
	"""
	#TODO: Function takes "elapsed time: _____"
	#Args:
		# StartDateTime (String): timestamp
		# SiteID (Integer) : PK for site
	#Testing:
		#timePeriod = 'last shift'
		#siteID = 1
		#print(mes.downtime.sp.getPeriodSiteTop5DT(timePeriod, siteID))		
	"""
	call = system.db.createSProcCall("dt.stp_getPeriodSiteTop5DTMicro", db)	
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	call.registerInParam("siteID", system.db.INTEGER, siteID)
	call.registerInParam("microDuration", system.db.INTEGER, microDuration)
	system.db.execSProcCall(call)
	return call.getResultSet()


#@timeit
@error_log
#@dump_args
def splitDTReasonsForEvent(stateEventID, split1Duration,split1ReasonID, split1Notes, split2Duration, split2ReasonID, split2Notes,userName):
	"""
	#TODO: Function takes "elapsed time: _____"
	#Args:
		# StartDateTime (String): timestamp
		# SiteID (Integer) : PK for site
	#Testing:
		#timePeriod = 'last shift'
		#siteID = 1
		#print(mes.downtime.sp.splitDTReasonsForEvent(stateEventID, split1Duration,split1ReasonID, split1Notes, split2Duration, split2ReasonID, split2Notes,userName))		
	"""
	call = system.db.createSProcCall("dt.stp_splitDTReasonsForEvent", db)
	call.registerInParam("stateEventID", system.db.INTEGER, stateEventID)
	call.registerInParam("split1Duration", system.db.INTEGER, split1Duration)
	call.registerInParam("split1ReasonID", system.db.INTEGER, split1ReasonID)
	call.registerInParam("split1Notes", system.db.VARCHAR, split1Notes)
	call.registerInParam("split2Duration", system.db.INTEGER, split2Duration)
	call.registerInParam("split2ReasonID", system.db.INTEGER, split2ReasonID)
	call.registerInParam("split2Notes", system.db.VARCHAR, split2Notes)
	call.registerInParam("userName", system.db.VARCHAR, userName)
	system.db.execSProcCall(call)
	return call.getResultSet()