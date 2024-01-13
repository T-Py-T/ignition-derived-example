'''
This contains all validaion
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.schedule.counts')


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
def updateCounts(tags,previousValue,currentValue):
	""" To be used on a tag script and update passed in counters with delta value
		Args:
		  	tags (list): description of argument
		  	Value object
		Returns: 
			None
		Testing: (script console)
			tags = ["[.]shiftRawInfeed", "[.]shiftChange"]
			mes.schedule.counts.updateCounts(tags)
		TODO:
	"""
	#tags = [list of tags passed in]
			#"ReadWriteValue", "Reset Condition"
	#tags = ["[.]shiftRawInfeed", "[.]shiftChange"]
	
	tagValues = system.tag.readBlocking(tags)
	accumulatorValue = 0
	if tagValues[0] is not None: #Accumulator
		accumulatorValue = tagValues[0].value
		resetCondition = False
	if tagValues[1] is not None: #Reset Condition
		resetCondition = tagValues[1].value
	oldValue = 0
	newValue = 0
	if previousValue is not None: oldValue = previousValue.value
	if currentValue is not None: newValue = currentValue.value
	if currentValue < 0: return
		
	# rollover has occurred
	if newValue < oldValue: oldValue = 0
	delta = newValue - oldValue
	accumulatorValue = accumulatorValue + delta
	if resetCondition: accumulatorValue = 0
	system.tag.writeBlocking([tags[0]], [accumulatorValue])