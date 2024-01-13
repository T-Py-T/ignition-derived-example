
'''
This contains all Local UI Scripts functions
'''
from decorators import error_log, timeit, dump_args

#Default global value for NULL database value
NULL = None
logger = system.util.getLogger('gpa.frontEnd.locaUI')
db = 'MSSQL_MES'
THRESHOLD_FAIL = 65
THRESHOLD_WARNING = 85

GATEWAY_THRESHOLD_FAIL = 85
GATEWAY_THRESHOLD_WARNING = 65

class Constants:
	# Strings that control style classes for cards/text fields
	TEXT_ERROR = 'TextFields/TextField TextFields/TextFailure'
	TEXT_NORMAL = 'TextFields/TextField'
	DROP_DOWN_NORMAL = 'TextFields/Dropdown'
	DROP_DOWN_ERROR = 'TextFields/Dropdown TextFields/TextFailure'
	CARD_ROOT = 'Cards/Root'
	CARD_WARNING = 'Cards/RootWarning'
	CARD_ERROR = 'Cards/RootFailure'
	CARD_SUCCESS = 'Cards/RootSuccess'
	OUTLINE_WARNING = 'Cards/WarningOutline'
	OUTLINE_ERROR = 'Cards/ErrorOutline'
	
	# other common strings
	ALL = 'All'
	VALUE = 'value'
	POLL_RATE = '10000'
	WARNING = 'warning'
	ERROR = 'fail'
	SUCCESS = 'success'
	
	# standard colors
	ERROR_COLOR = '#C8102E' # red
	WARNING_COLOR = '#F08F2C' # orange
	LBLUE_COLOR = '#78BFE2' # light blue


#@timeit
@error_log
#@dump_args
def getComponentStatus(value):
    if value >= GATEWAY_THRESHOLD_FAIL:
        return gpa.frontEnd.localUI.Constants.ERROR
    elif value >= GATEWAY_THRESHOLD_WARNING and value < GATEWAY_THRESHOLD_FAIL:
        return gpa.frontEnd.localUI.Constants.WARNING
    else:
        return ''
		
#@timeit
@error_log
#@dump_args
def getRateStatus(value):
	# Will return a string depending on threshold (Gateway Status Page)
	if value < THRESHOLD_WARNING:
		return gpa.frontEnd.localUI.Constants.ERROR
	elif value < THRESHOLD_FAIL:
		return gpa.frontEnd.localUI.Constants.WARNING
	else: 	# Fall back value
		return ''


#@timeit
@error_log
#@dump_args
def getOutlineColor(value, params):
	if value < params['bad']:
		return localUI.Constants.OUTLINE_ERROR
	elif value < params['warning']:
		return localUI.Constants.OUTLINE_WARNING
	else:
		return ''


#@timeit
@error_log
#@dump_args	
def splitPath(pathName):
	split = pathName.split('/')
	return split[len(split) -1]
	
	
	
#@timeit
@error_log
#@dump_args
def getFinalState(dictionaryOfStates):
	""" Description of function purpose
		Args:
			dictionaryOfStates: A Python dictionary containing the state strings
		Returns:
			(string): time in milliseconds
		Testing: (script console)
			print(gpa.frontEnd.localUI.getFinalState(pythonDictionary)
		TODO: stuff
	"""
	if gpa.frontEnd.localUI.Constants.ERROR in dictionaryOfStates.values():
		return gpa.frontEnd.localUI.Constants.ERROR
	elif gpa.frontEnd.localUI.Constants.WARNING in dictionaryOfStates.values():
		return gpa.frontEnd.localUI.Constants.WARNING
	else:
		return ""	
#@timeit
@error_log
#@dump_args		
def getDashboardArray(data, side):
	pydata = system.dataset.toPyDataSet(data)
	dashboard = pydata.getColumnAsList(side)[0]
	
	return system.util.jsonDecode(dashboard)
	
#@timeit
@error_log
#@dump_args	
def convert(type, input):
	import datetime 
	if type == 'min': return str(datetime.timedelta(minutes=input)) 
	if type == 'sec': return str(datetime.timedelta(seconds=input))

#@timeit
@error_log
#@dump_args	
def throwError(msg):
	errorParams = {
		"ModalName": "ErrorModal",
		"ErrorMessage": 'An error occured: ' + str(msg),
	}
	
	system.perspective.openPopup("ErrorModal", "GlobalComponents/Modals/ErrorModal", errorParams)
	logger.error('An error occured: ' + str(msg))

#@timeit
@error_log
#@dump_args	
def throwSuccess(msg):
	successParams = {
		"ModalName": "ErrorModal",
		"ErrorMessage": str(msg) + ' successfully.',
	}
	
	system.perspective.openPopup("ErrorModal", "GlobalComponents/Modals/ErrorModal", successParams)
	logger.info(str(msg))