'''
This contains all OEE calculation functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.schedule.shiftControl')

#@timeit
@error_log
#@dump_args	
def setEndOfShiftPulse():	
	# FUNCTION: Updates row data with given data
	# PARAMETERS: 
	# TESTING: 
	#	mes.schedule.shiftControl.setEndOfShiftPulse()

	##### Set K1EndOfShift = True, K2EndOfShift = True;
	paths, values = ['<Eq Path>/calculatedValues/EndOfShift'], [True]
	system.tag.writeBlocking(paths, values)
	time.sleep(1)# Intentional Delay to simulate pulse values
	paths, values = ['<Eq Path>/calculatedValues/EndOfShift'], [False]
	system.tag.writeBlocking(paths, values)