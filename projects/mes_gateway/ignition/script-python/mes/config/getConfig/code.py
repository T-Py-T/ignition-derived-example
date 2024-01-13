"""
This contains all mes config functions
"""
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.config.getConfig')


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
def TestFunction():
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:

		Returns:
		
		Testing:
	"""
	# Write back to [MES] tag provider with equipment path
	pass

#def getAllThresholds():
#	ds = mes.config.sp.getThresholds()
#	thresholds = gpa.data.datasetToJson(ds)
#	
#	otherRow = None
#	
#	for row in thresholds:
#		if row.get('Name') == 'Other':
#			otherRow = row
#			break
#			
#	gpa.frontEnd.localUI.THRESHOLD_FAIL = row.get('Bad')
#	gpa.frontEnd.localUI.THRESHOLD_WARNING = row.get('Warning')
#	
#	print(gpa.frontEnd.localUI.THRESHOLD_FAIL)