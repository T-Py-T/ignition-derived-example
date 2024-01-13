'''
This contains all OEE calculation functions
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



# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.quality.sp')


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
def testFunction():
	pass
	# Write back to [MES] tag provider with equipment path