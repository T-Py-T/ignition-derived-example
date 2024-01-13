'''
This contains all OEE calculation functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.oee.calcs')

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()
areas = sh.getAreas()
TimePeriodDict = sh.getTimePeriodDict()
AggregateDict = sh.getAggregateDict()
siteID = sh.getSiteId()
micro = sh.getMicro()

#logger.info(str(siteID))
#logger.info(str(micro))
#logger.info(str(areas))



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
def updateAllSiteAreasOEE_AQP(timePeriod):
	""" Gets OEE_AQP DS for each line and returns it as larger dataset
		Args:
		  timeRangeType (String): 'Shift', 'Run', 'Realtime'
		  machineRange (String): 'Area', 'Group', 'Site'
		  machineID (Int): 1 #PK of that asset (line,area, group, etc.)
		Returns:
		  (int): 1 if passing, else -1
		Testing:
			mes.oee.calcs.updateAllSiteAreasOEE_AQP(timePeriod)		
		TODO: 
			_ - Use only 1 Write for performance
			_ - genereate empty DS (keeps failing "column numbers dont match")
			_ - add Site to this list
	"""	
	#timePeriod = 'current shift'
	UDTFolder = 'Shift'
	machineType = 'Site'
	machineID = siteID #Site
	
	# Get site values and write them to the tags
	sitePyDS = mes.oee.periodic.getOEE_AQP(timePeriod, machineType, siteID)
	
	if sitePyDS == -1: #If site fails
		# Just return Area Data
		machineType = 'Area'
		areaPyDS = mes.oee.periodic.getOEE_AQP(timePeriod, machineType, NULL)  #We want all Areas
	 	
	 	# Write back to [MES] tag provider with equipment path
		mes.oee.periodic.writeOEE_AQP(timePeriod, system.dataset.toPyDataSet(areaPyDS))
		
		raise Exception("No Site data returned!")
	
	else: #Combine data
		machineType = 'Area'
		areaPyDS = mes.oee.periodic.getOEE_AQP(timePeriod, machineType, NULL)  #We want all Areas
		
		if sitePyDS == -1: raise Exception("No Area data returned!")
		else: sitePyDS = system.dataset.appendDataset(sitePyDS, areaPyDS)	
		
	 	# Write back to [MES] tag provider with equipment path
		mes.oee.periodic.writeOEE_AQP(timePeriod, system.dataset.toPyDataSet(sitePyDS))


#@timeit
@error_log
#@dump_args
def updateAllLinesOEE_AQP(timePeriod):
	""" Gets OEE_AQP DS for each line and returns it as larger dataset
		Args:
		  timeRangeType (String): 'Shift', 'Run', 'Realtime'
		  machineRange (String): 'Area', 'Group', 'Site'
		  machineID (Int): 1 #PK of that asset (line,area, group, etc.)
		Returns:
		  (int): 1 if passing, else -1
		Testing:
			mes.oee.calcs.updateAllOEE_AQP()		
		TODO: 
	"""	
	
	# Add All Lines DS to previous "allDS"
	linesPyDS = mes.oee.periodic.getAllLinesOEE_AQP(timePeriod, siteID)
	if linesPyDS == -1: raise Exception("No data returned!")
	else:
		# Write back to [MES] tag provider with equipment path
		#mes.oee.periodic.writeOEE_AQP(UDTFolder, system.dataset.toPyDataSet(allDS))
		mes.oee.periodic.writeOEE_AQP(timePeriod, linesPyDS)	


#@timeit
@error_log
#@dump_args
def updateAllAreaOEE_table(timePeriod):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
		  timeRangeType (String): 'Shift', 'Run', 'Realtime'
		  machineRange (String): 'Area', 'Group', 'Site'
		  machineID (Int): 1 #PK of that asset (line,area, group, etc.)
		Returns:
		  (int): 1 if passing, else -1
		Testing:
			pyDS = mes.oee.periodic.getOEETable('last shift', 'Shift', 'Area', 2)
			mes.oee.periodic.writeOEETable('Shift', pyDS)		
		TODO: Find a way to add the PyDS together and try to write the OEE_AQP all at once (1 write call)
	"""	
	UDTFolder = 'Shift'
	machineType = 'Area'
		#TODO: Need to convert to query or store in tag structure (query tag?)
	machineID = siteID #Site
	
	##Setup empty DS for appending new DS to
	headers= ['AreaID', 'EqPath', 'LineID', 'Line', 'OEE', 'Running', 'PlannedOrder', 'RunProgress', 'ProgressPercent', 'TimeRemaining', 'Operator']
	data = [] #[0, '', 0, '', 0.0, 0, '', 0.0, '', 0, '']
	fakeDS = system.dataset.toDataSet(headers, data)
	testingDS = mes.oee.periodic.getOEETable(timePeriod, machineType, machineID)
	
	if testingDS == -1: OEETableDS = system.dataset.clearDataset(fakeDS) #raise Exception("No data returned!")
	else: OEETableDS = system.dataset.clearDataset(testingDS)
	print testingDS
	print OEETableDS
	for areaID in areas:
		areaOEETablePyDS = mes.oee.periodic.getOEETable(timePeriod, machineType, areaID)
		if areaOEETablePyDS == -1: pass #raise Exception("No data returned!")
		else: OEETableDS = system.dataset.appendDataset(OEETableDS, areaOEETablePyDS)
	
	# ****** Need to rework to allow passing list of tagPaths,Values for the system.tag.writeBlocking
	pyOEETableDS = system.dataset.toPyDataSet(OEETableDS)
	#print(pyOEETableDS)
	
	mes.oee.periodic.writeOEETable(timePeriod, pyOEETableDS)


#@timeit
@error_log
#@dump_args
def calcLineOEERun():
	pass
	# Write back to [MES] tag provider with equipment path
	
