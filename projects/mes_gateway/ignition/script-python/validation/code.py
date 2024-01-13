'''
This contains all validation functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders
import re

# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('validation')

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()
#areas = sh.getAreas()
#siteID = sh.getSiteId()
#micro = sh.getMicro()

regexPatterns = {
	'emailPattern': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
	'passwordPattern': r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$'
}





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


#### BEN PLEASE CHANGE ME !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#emailPattern = re.compile(r'^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*$', re.I)

#modelPathPattern = re.compile(r'([^/\\]+)', re.I)


#@timeit
@error_log
#@dump_args
def isValidRegex(checkString, regex):
	regexPattern = regexPatterns[regex]
	
	return re.match(regexPattern, checkString) is not None