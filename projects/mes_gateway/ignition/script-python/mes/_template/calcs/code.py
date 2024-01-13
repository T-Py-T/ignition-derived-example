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
logger = system.util.getLogger('mes.quality.calcs')


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
def testFunction():
	""" Description of function purpose
		Args:
		  	arg1 (type): description of argument
		Returns:
			(type): description of argument
		Testing: (script console)
			system.downtime.periodic.exampleFunction(arg1)
		TODO:
			_ - Finish adding ______
	"""
	pass
	# Write back to [MES] tag provider with equipment path