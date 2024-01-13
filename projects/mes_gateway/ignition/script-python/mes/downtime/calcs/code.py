'''
This contains all Downtime calculation functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.downtime.calcs')

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()
areas = sh.getAreas()
TimePeriodDict = sh.getTimePeriodDict()
AggregateDict = sh.getAggregateDict()
siteID = sh.getSiteId()
micro = sh.getMicro()
lines = sh.getLines()


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
def updateAllSiteAreasDtTop5(timePeriod):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
		  timeRangeType (String): 'Shift', 'Run', 'Realtime'
		  machineRange (String): 'Area', 'Group', 'Site'
		  machineID (Int): 1 #PK of that asset (line,area, group, etc.)
		Returns:
		  (int): 1 if passing, else -1
		Testing:
			pyDS = mes.oee.periodic.getOEETable('last shift', 'Shift', 'Area', 2)
			mes.downtime.updateAllSiteAreasDtTop5('current shift')		
		TODO: Find a way to add the PyDS together and try to write the OEE_AQP all at once (1 write call)
	"""	
	UDTFolder = 'Shift'
	
	top5DSList, micro5DSList = [],[]
	
	#allTop5DS = mes.downtime.periodic.getDtTop5(timePeriod, UDTFolder, machineType, machineID)#, micro)
	
	# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	# ****** Need to fix this so that microstops can be shown properly
	#micro = 60 # cutoff for microstop in seconds
	
	siteTop5PyDS = mes.downtime.periodic.getDtTop5(timePeriod, 'Site', siteID)#, micro)
	if siteTop5PyDS == -1:	raise Exception("No data returned!")
	top5DSList.append(siteTop5PyDS)
	
	siteMicroPyDS = mes.downtime.periodic.getDtTop5(timePeriod, 'Site', siteID, top5Type='Micro')#, micro)
	if siteMicroPyDS == -1:	pass #raise Exception("No data returned!")
	else: micro5DSList.append(siteMicroPyDS)
	mes.downtime.periodic.tagWriteDtTop5(timePeriod, top5DSList)
	mes.downtime.periodic.tagWriteDtTop5(timePeriod, micro5DSList, top5Type='Micro')
	
	
	for areaID in areas:
		areaTop5PyDS = mes.downtime.periodic.getDtTop5(timePeriod, 'Area', areaID)#, micro)
		if areaTop5PyDS == -1:pass #raise Exception("No data returned!")
		top5DSList.append(areaTop5PyDS)
		
		areaMicroPyDS = mes.downtime.periodic.getDtTop5(timePeriod, 'Area', areaID, top5Type='Micro')#, micro)
		if areaMicroPyDS == -1:	pass #raise Exception("No data returned!")
		else: micro5DSList.append(areaMicroPyDS)
		mes.downtime.periodic.tagWriteDtTop5(timePeriod, top5DSList)
		mes.downtime.periodic.tagWriteDtTop5(timePeriod, micro5DSList, top5Type='Micro')
	
	# ****** Need to rework to allow passing list of tagPaths,Values for the system.tag.writeBlocking
	
	#print(top5DSList)
	#print(micro5DSList)
	#############################Original 9/18/23
	#mes.downtime.periodic.tagWriteDtTop5(timePeriod, top5DSList)
	#mes.downtime.periodic.tagWriteDtTop5(timePeriod, micro5DSList, top5Type='Micro')


#@timeit
@error_log
#@dump_args
def updateAllLinesDTop5(timePeriod):
	top5PyDS = mes.downtime.periodic.getAllDtTop5(timePeriod, microDuration=micro)
	if top5PyDS == -1:	raise Exception("No data returned!")
	mes.downtime.periodic.writeAllDtTop5(timePeriod, top5PyDS)

	top5mPyDS = mes.downtime.periodic.getAllDtTop5(timePeriod, top5Type='Micro', microDuration=micro)
	if top5mPyDS == -1:	raise Exception("No data returned!")
	mes.downtime.periodic.writeAllDtTop5(timePeriod, top5mPyDS, top5Type='Micro')


#@timeit
@error_log
#@dump_args
def updateAllPlannedUnplannedDT(timePeriod):
	upPyDS = mes.downtime.periodic.getallPlannedUnplannedDT(timePeriod)
	if upPyDS == -1: raise Exception("No data returned!")
	mes.downtime.periodic.writePlannedUnplannedDT(timePeriod,upPyDS)


#@timeit
@error_log
#@dump_args
def updateAllDowntimeEvents(timePeriod):
	eventsPyDS = mes.downtime.periodic.getAllDtEvents(timePeriod)
	if eventsPyDS == -1: raise Exception("No data returned!")
	mes.downtime.periodic.writeAllDtEvents(timePeriod, eventsPyDS)
	
	

#@timeit
@error_log
#@dump_args
def updateAllDowntimeEventsComposite(timePeriod):
	eventsPyDS = mes.downtime.periodic.getAllDtEventsComposite(timePeriod)
	if eventsPyDS == -1: raise Exception("No data returned!")
	mes.downtime.periodic.writeAllDtEventsComposite(timePeriod, eventsPyDS)
	
	
#@timeit
@error_log
#@dump_args
def updateAllDowntimeSummary(timePeriod):
	sumPyDS = mes.downtime.periodic.getAllDtSummary(timePeriod)
	if sumPyDS == -1: raise Exception("No data returned!")
	mes.downtime.periodic.writeDtSummary(timePeriod, sumPyDS)


#@timeit
@error_log
#@dump_args
def updateAllStateTimeline(timePeriod):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
			timeRangeType (String): 'Shift', 'Run', 'Realtime'
		Returns:
		  (int): 1 if passing, else -1
		Testing:
			mes.downtime.calcs.updateAllStateTimeline(timePeriod)
		TODO:
	"""	
	timelinePyDS = mes.downtime.periodic.getAllStateTimeline(timePeriod)
	if timelinePyDS == -1: raise Exception("No data returned!")
	mes.downtime.periodic.writeAllStateTimeline(timePeriod, timelinePyDS)


#@timeit
@error_log
#@dump_args
def updateAllStateHistory(timePeriod):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
		  timeRangeType (String): 'Shift', 'Run', 'Realtime'
		Returns:
		  (int): 1 if passing, else -1
		Testing:
			mes.downtime.calcs.updateAllStateHistory(timePeriod)	
		TODO:
	"""	
	timelinePyDS = mes.downtime.periodic.getAllStateTimeline(timePeriod)
	if timelinePyDS == -1: raise Exception("No data returned!")
	mes.downtime.periodic.writeAllStateTimeline(timePeriod, timelinePyDS)