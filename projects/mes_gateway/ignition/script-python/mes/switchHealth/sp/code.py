from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = 'Switch_Structure'



# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.switchHealth.sp')


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
def addSwitch(assetID, ncc, switch, plc):
	""" adds switch to the database
	TODO: Needs to be converted to sproc.
	Args: assetID: string, ncc: int, switch: int, plc: string
	Returns: bool    
	Testing: (script console)
		mes.switchHealth.sp.addSwitch(assetID, ncc, switch, plc)
	"""
	ret = system.db.runPrepUpdate('INSERT INTO switches (asset_id, ncc, switch, "PlcAddress") VALUES (?, ?, ?, ?)', [assetID, ncc, switch, plc], db)
	return ret
	
#	call = system.db.createSProcCall('stp_addSwitch', db)
#	call.registerInParam('ncc', system.db.VARCHAR, ncc)
#	call.registerInParam('assetID', system.db.INTEGER, assetID)
#	call.registerInParam('switch', system.db.INTEGER, switch)
#	call.registerInParam('plc', system.db.VARCHAR, plc)
#	system.db.execSProcCall(call)
#	ret = call.getReturnValue()
#	return ret