"""
This contains all event tag event triggers functions
"""
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.oee.tag')

sh = ScriptHeaders() #Use class to get common variables accross all scripts
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     EXAMPLE FUNCTION
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#@timeit
#@error_log
#@dump_args
#def exampleFunction(arg1):
#	""" Description of function purpose
#		Args:
#		  	arg1 (type): description of argument
#		Returns:
#			(type): description of argument
#		Testing: (script console)
#			system.downtime.periodic.exampleFunction(arg1)
#		TODO:
#			_ - Finish adding ______
#	"""
#	# Write back to [MES] tag provider with equipment path
#	pass


#@timeit
@error_log
#@dump_args
def countEventInsert(timestamp, lineID, countTypeID, count, runID, db=db):
	""" Inserts counter value (on change) to counthistory table
	TODO: None
	
	Args:	#data fields from tag used for SPROC
		timestamp (datetime): event timestamp
		countTagID (int): reference path (tagPath, line, cell, etc)
		countTypeID (int): reference type (1=Infeed, 2=Outfeed, 3=Reject/Waste, etc)
		count (int): value from countDelta

	Returns: None 
	
	Testing: (script console)
		mes.oee.tag.countEventInsert(system.date.now(), 1, 1, 21,1)
	"""
	call = system.db.createSProcCall("tag.stp_insertCountEvent", db)
	call.registerInParam("eventTimestamp", system.db.TIMESTAMP, timestamp)
	call.registerInParam("lineID", system.db.INTEGER, lineID)
	call.registerInParam("countTypeID", system.db.INTEGER, countTypeID)
	call.registerInParam("counts", system.db.INTEGER, count)
	#call.registerInParam("runID", system.db.INTEGER, NULL)
	if runID == 0: call.registerInParam("runID", system.db.INTEGER, NULL)
	else: call.registerInParam("runID", system.db.INTEGER, runID)
	system.db.execSProcCall(call)

	
#@timeit
@error_log
#@dump_args
def modeEventInsert(line , cell, timeStart, timeEnd, modeID, db=db):
	""" Inserts counter value (on change) to eventsmes table
	TODO:
		None
	Args:	#data fields from tag used for SPROC
		line (string):
		cell (string):
		timeStart (datetime):
		timeEnd (datetime): 
		modeID (int):
	Returns: None  
 
	Testing: (script console)
		line,cell, val = 18, 10, 2
		start = system.date.format(system.date.addHours(system.date.now(), -8), "yyyy-MM-dd HH:mm:ss")
		end = system.date.format(system.date.now(), "yyyy-MM-dd HH:mm:ss")
		mes.oee.tag.modeEventInsert(line, cell, start, end, val)	
	"""
	call = system.db.createSProcCall("tag.stp_insertModeEvent", db) #MSSQL
	call.registerInParam("lineID", system.db.INTEGER, line)
	call.registerInParam("cellID", system.db.INTEGER, cell)
	call.registerInParam("timeStart", system.db.TIMESTAMP, timeStart)
	call.registerInParam("timeEnd", system.db.TIMESTAMP, timeEnd)
	call.registerInParam("modeID", system.db.INTEGER, modeID)
	system.db.execSProcCall(call)


#@timeit
@error_log
#@dump_args
def stateEventInsert(line , cell, timeStart, timeEnd, stateID, db=db):
	""" Inserts counter value (on change) to eventsmes table
		TODO:
			None
		Args:	#data fields from tag used for SPROC
			line (string):
			cell (string):
			timeStart (datetime):
			timeEnd (datetime): 
			stateID (int):
	Returns:
	        None      
	Testing: (script console)
		line,cell, val = 18, 10, 2
		end = system.date.format(system.date.addMinutes(system.date.now(), 1), "yyyy-MM-dd HH:mm:ss")
		start = system.date.format(system.date.now(), "yyyy-MM-dd HH:mm:ss")
		mes.oee.tag.stateEventInsert(line, cell, start, end, val)	
	"""
	call = system.db.createSProcCall("tag.stp_insertStateEvent", db)
	call.registerInParam("lineID", system.db.INTEGER, line)
	call.registerInParam("cellID", system.db.INTEGER, cell)
	call.registerInParam("timeStart", system.db.TIMESTAMP, timeStart)
	call.registerInParam("timeEnd", system.db.TIMESTAMP, timeEnd)
	call.registerInParam("stateID", system.db.INTEGER, stateID)
	system.db.execSProcCall(call)


#@timeit
@error_log
#@dump_args
def stateCurrent(line , cell, timeStart, stateID, db=db):
	""" Inserts counter value (on change) to eventsmes table
		TODO:
			None
		Args:	#data fields from tag used for SPROC
			line (string):
			cell (string):
			timeStart (datetime):
			timeEnd (datetime): 
			stateID (int):
	Returns:
	        None      
	Testing: (script console)
		mes.oee.tag.stateCurrent(line, cell, start, end, val)	
	"""
	call = system.db.createSProcCall("tag.stp_upsertCurrentState", db)
	call.registerInParam("lineID", system.db.INTEGER, line)
	call.registerInParam("cellID", system.db.INTEGER, cell)
	call.registerInParam("CurrentDateTime", system.db.TIMESTAMP, timeStart)
	call.registerInParam("stateID", system.db.INTEGER, stateID)
	system.db.execSProcCall(call)


#@timeit
@error_log
#@dump_args
def modeCurrent(line , timeStart, modeID, db=db):
	""" Inserts counter value (on change) to eventsmes table
		TODO:
			None
		Args:	#data fields from tag used for SPROC
			line (string):
			cell (string):
			timeStart (datetime):
			timeEnd (datetime): 
			stateID (int):
	Returns:
	        None      
	Testing: (script console)
		line,val = 1,  2
		mes.oee.tag.modeCurrent(line, start, val)	
	"""
	call = system.db.createSProcCall("tag.stp_upsertCurrentMode", db)
	call.registerInParam("lineID", system.db.INTEGER, line)
	call.registerInParam("CurrentDateTime", system.db.TIMESTAMP, timeStart)
	call.registerInParam("modeID", system.db.INTEGER, modeID)
	system.db.execSProcCall(call)