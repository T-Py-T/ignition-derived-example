'''
This contains all OEE calculation functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.downtime.periodic')

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


# TagName Mapping {DBColumnName : TagName}
Top5Dict = {	
		# {DBColumnName : TagName}
		'Name':'Name',
		'Quantity':'Duration'}
DTPlannedDict={
	'Planned':'DowntimePlanned', 
	'Unplanned':'DowntimeUnplanned'}
DTSummaryDict={
	'Production':'SummaryProduction',
	'Changeover':'SummaryChangeover',
	'Downtime':'SummaryDowntime'}


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
def getAllDtEvents(timePeriod):
	""" Description of function purpose
		Args:
			timePeriod (String): 'last shift', 'current shift', etc.
		Returns:
			(int): pyDataset if passing, else -1
		Testing: (script console)
			print(mes.downtime.periodic.getAllDtEvents('current shift'))
		TODO:
	"""
	# Check time range to make sure it one of the avialable types
	if timePeriod in TimePeriodDict.keys():
		#2 get DS from SPROC based on machineRange
		stpRes = mes.downtime.sp.getPeriodAllLinesDTEvents(timePeriod)
	else: return -1 #Failure
	stpResPyDS = system.dataset.toPyDataSet(stpRes)
	if(len(stpResPyDS) > 0): return stpResPyDS
	else: return -1 #Failure

#@timeit
@error_log
#@dump_args
def getAllDtEventsComposite(timePeriod):
	""" Description of function purpose
		Args:
			timePeriod (String): 'last shift', 'current shift', etc.
		Returns:
			(int): pyDataset if passing, else -1
		Testing: (script console)
			print(mes.downtime.periodic.getAllDtEvents('current shift'))
		TODO:
	"""
	# Check time range to make sure it one of the avialable types
	if timePeriod in TimePeriodDict.keys():
		#2 get DS from SPROC based on machineRange
		stpRes = mes.downtime.sp.getPeriodAllLinesDTEventsComposite(timePeriod)
	else: return -1 #Failure
	stpResPyDS = system.dataset.toPyDataSet(stpRes)
	if(len(stpResPyDS) > 0): return stpResPyDS
	else: return -1 #Failure			
	
#@timeit
@error_log
#@dump_args
def getAllDtSummary(timePeriod):
	""" Description of function purpose
		Args:
			timeRangeType (String): 'Shift', 'Run', 'Realtime'
		Returns:
			(int): 1 if passing, else -1
		Testing: (script console)
			print(mes.downtime.periodic.getAllDtSummary('current shift'))
		TODO:
	"""
	# Check time range to make sure it one of the avialable types
	if timePeriod in TimePeriodDict.keys():
		#2 get DS from SPROC based on machineRange
		stpRes = mes.downtime.sp.getPeriodAllLinesStateSummary(timePeriod)
	else: return -1 #Failure
	stpResPyDS = system.dataset.toPyDataSet(stpRes)
	if(len(stpResPyDS) > 0): return stpResPyDS
	else: return -1 #Failure

	
#@timeit
@error_log
#@dump_args
def getAllDtTop5(timePeriod, top5Type='', microDuration=0):
	""" Description of function purpose
		Args:
			timePeriod (String): 'last shift', 'current shift', etc.
		Returns:
			(int): 1 if passing, else -1
		Testing: (script console)
			print(mes.downtime.periodic.getAllDtEvents('current shift'))
		TODO:
	"""
	# Check time range to make sure it one of the avialable types
	if timePeriod in TimePeriodDict.keys():
		#2 get DS from SPROC based on machineRange

		#2 get DS from SPROC based on machineRange
		if top5Type == 'Micro': stpRes = mes.downtime.sp.getPeriodAllLinesTop5DTMicro(timePeriod, microDuration)
		else: stpRes = mes.downtime.sp.getPeriodAllLinesTop5DT(timePeriod, microDuration)
	else: return -1 #Failure
	stpResPyDS = system.dataset.toPyDataSet(stpRes)
	if(len(stpResPyDS) > 0): return stpResPyDS
	else: return -1 #Failure
	
#@timeit
@error_log
#@dump_args
def getAllStateTimeline(timePeriod):
	""" Description of function purpose
		Args:
			timePeriod (String): 'last shift', 'current shift', etc.
		Returns:
			(int): 1 if passing, else -1
		Testing: (script console)
			print(mes.downtime.periodic.getAllDtEvents('current shift'))
		TODO:
	"""
	# Check time range to make sure it one of the avialable types
	if timePeriod in TimePeriodDict.keys():
		#2 get DS from SPROC based on machineRange
		stpRes = mes.downtime.sp.getPeriodAllLinesStateTimeline(timePeriod)
	else: return -1 #Failure
	stpResPyDS = system.dataset.toPyDataSet(stpRes)
	if(len(stpResPyDS) > 0): return stpResPyDS
	else: return -1 #Failure


#@timeit
@error_log
#@dump_args
def getDtTop5(timePeriod, machineRange, machineID, top5Type='', microDuration=micro):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
	Args:
	  	timeRangeType (String): 'Shift', 'Run', 'Realtime'
	  	machineRange (String): 'Area', 'Group', 'Site'
	  	machineID (Int): 1 #PK of that asset (line,area, group, etc.)
	Returns:
		(int): 1 if passing, else -1
	Testing:
	    print(mes.downtime.periodic.getOEE_AQP('Shift','Area', 1))		
	 	
	TODO: Function takes "elapsed time: 0.062" (for only 1 Area 3 machines) 
			RETEST after adding full plant simulator
	"""	

	machineList = ['Site','Area', 'Group']
	
	#print(timePeriod, machineRange, machineID, top5Type, microDuration)

	# Check time range to make sure it one of the avialable types
	if machineRange in machineList and timePeriod in TimePeriodDict.keys():
		#pass
		#2 get DS from SPROC based on machineRange
		if top5Type == 'Micro':
			if machineRange == 'Group': stpRes = mes.downtime.sp.getPeriodGroupTop5DTMicro(timePeriod, machineID, microDuration)
			elif machineRange == 'Area': stpRes = mes.downtime.sp.getPeriodAreaTop5DTMicro(timePeriod, machineID)#, microDuration)
			elif machineRange == 'Site': stpRes = mes.downtime.sp.getPeriodSiteTop5DTMicro(timePeriod, machineID, microDuration)
			else: pass
		else:
			if machineRange == 'Group': stpRes = mes.downtime.sp.getPeriodGroupTop5DT(timePeriod, machineID, microDuration)
			elif machineRange == 'Area': stpRes = mes.downtime.sp.getPeriodAreaTop5DT(timePeriod, machineID) #, microDuration)
			elif machineRange == 'Site': stpRes = mes.downtime.sp.getPeriodSiteTop5DT(timePeriod, machineID, microDuration)
			else: pass
	else: return -1 #Failure
	stpResPyDS = system.dataset.toPyDataSet(stpRes)
	if(len(stpResPyDS) > 0):
		return stpResPyDS
	else:
		return -1 #Failure


#@timeit
@error_log
#@dump_args
def getallPlannedUnplannedDT(timePeriod):
	""" Description of function purpose
		Args:
			timeRangeType (String): 'Shift', 'Run', 'Realtime'
		Returns:
			(int): 1 if passing, else -1
		Testing: (script console)
			print(mes.downtime.periodic.getallPlannedUnplannedDT('current shift'))
		TODO:
	"""
	# Check time range to make sure it one of the avialable types
	if timePeriod in TimePeriodDict.keys():
		#2 get DS from SPROC based on machineRange
		stpRes = mes.downtime.sp.getPeriodAllLinesPlannedUnplannedDT(timePeriod)
	else: return -1 #Failure
	stpResPyDS = system.dataset.toPyDataSet(stpRes)
	if(len(stpResPyDS) > 0): return stpResPyDS
	else: return -1 #Failure
		


#@timeit
@error_log
#@dump_args
def getStateHistory():
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
		  	timeRangeType (String): 'Shift', 'Run', 'Realtime'
		  	machineRange (String): 'Area', 'Group', 'Site'
		  	machineID (Int): 1 #PK of that asset (line,area, group, etc.)
		Returns:
			(int): 1 if passing, else -1
		Testing:
			ds = mes.downtime.sp.getPeriodLineStateTimeline('last shift', 1, 2)
			system.tag.writeBlocking(['[MES]Enterprise/Site/Area/Line/Analysis/Shift/DT/DowntimeEvents'],[ds])	
	"""
	# Write back to [MES] tag provider with equipment path
	pass

##@timeit
#@error_log
##@dump_args
#def writeAllDtEvents(timePeriod, pyDataset):
#	""" Gets Top5 DT DS for each line and returns it as larger dataset
#	Args:
#	  timeRangeFolder (String): 'Shift', 'Run', 'Realtime'
#	  pyDataset (pyDataset): PyDS of all dtEvents that need to be separated.
#	Returns:
#	  (int): 1 if passing, else -1
#	Testing:
#	    print(mes.downtime.periodic.writeAllDtEvents('shift', pyDataset))		
#	TODO: Function takes "elapsed time: 0.106000"
#	"""	
#	
#	writePaths, writeValues = [],[]
#	headers = ['StartDateTime', 'EndDateTime', 'StateID', 'Status', 'Duration', 'COLOR', 'LineID', 'Line', 'EqPath', 'EventID']
#	for lineID in lines:
#		lineData = []
#		if lineID in zip(*pyDataset)[6]:
#			for row in pyDataset:
#				#print row
#				if row['LineID'] == lineID:
#					EQPath = row['EqPath']
#					lineData.append(row)
#		UDTFolder = TimePeriodDict.get(timePeriod)
#		linePath = '[MES]' + EQPath + '/Analysis/' + UDTFolder + '/DT/DowntimeEvents'
#		machineDS = system.dataset.toDataSet(headers, lineData) # Create New Top5 DS for each line
#		columnFilter = ['StartDateTime', 'EndDateTime', 'EventID', 'StateID', 'Status', 'Duration', 'COLOR']
#		filteredDataset = system.dataset.filterColumns(machineDS, columnFilter) #Filter DS (Get rid of unwanted Columns)
#		#print linePath
#		#print UDTFolder		
#		writePaths.append(linePath)
#		writeValues.append(filteredDataset)
#	#print(lines, writePaths, writeValues)
#	system.tag.writeBlocking(writePaths,writeValues)	

#@timeit
@error_log
#@dump_args
def writeAllDtEvents(timePeriod, pyDataset):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
	Args:
	  timeRangeFolder (String): 'Shift', 'Run', 'Realtime'
	  pyDataset (pyDataset): PyDS of all dtEvents that need to be separated.
	Returns:
	  (int): 1 if passing, else -1
	Testing:
	    print(mes.downtime.periodic.writeAllDtEvents('shift', pyDataset))		
	TODO: Function takes "elapsed time: 0.106000"
	"""	
	EQPath = ''
	lineData = []
	
	writePaths, writeValues = [],[]
	headers = ['StartDateTime', 'EndDateTime', 'StateID', 'Status', 'Duration', 'COLOR', 'LineID', 'Line', 'EqPath', 'EventID']
	for lineID in lines:
	        for rowIndex in range(pyDataset.getRowCount()):
	            if pyDataset.getValueAt(rowIndex, 'LineID') == lineID:
	                EQPath = pyDataset.getValueAt(rowIndex, 'EqPath')
	                row = [pyDataset.getValueAt(rowIndex, colName) for colName in headers]
	                lineData.append(row)
	        UDTFolder = TimePeriodDict.get(timePeriod)
		linePath = '[MES]' + EQPath + '/Analysis/' + UDTFolder + '/DT/DowntimeEvents'
		machineDS = system.dataset.toDataSet(headers, lineData) # Create New Top5 DS for each line
		columnFilter = ['StartDateTime', 'EndDateTime', 'EventID', 'StateID', 'Status', 'Duration', 'COLOR']
		filteredDataset = system.dataset.filterColumns(machineDS, columnFilter) #Filter DS (Get rid of unwanted Columns)
		#print linePath
		#print UDTFolder		
		writePaths.append(linePath)
		writeValues.append(filteredDataset)
	#print(lines, writePaths, writeValues)
	system.tag.writeBlocking(writePaths,writeValues)	


#@timeit
@error_log
#@dump_args
def writeAllDtEventsComposite(timePeriod, pyDataset):
    """ Gets Top5 DT DS for each line and returns it as a larger dataset
    Args:
      timeRangeFolder (String): 'Shift', 'Run', 'Realtime'
      pyDataset (pyDataset): PyDS of all dtEvents that need to be separated.
    Returns:
      (int): 1 if passing, else -1
    Testing:
        print(mes.downtime.periodic.writeAllDtEvents('shift', pyDataset))        
    TODO: Function takes "elapsed time: 0.106000"
    """    

    writePaths, writeValues = [],[]
    headers = [
                'StartDateTime', 
                'EndDateTime', 
                'StateID', 
                'Status', 
                'Duration', 
                'COLOR', 
                'LineID', 
                'Line', 
                'EqPath', 
                'EventID',
                'WorkOrder',
                'ProductCode',
                'ParentReason',
                'row_num'
            ]
    EQPath = ''
    lineData = []
    for lineID in lines:
        for rowIndex in range(pyDataset.getRowCount()):
            if pyDataset.getValueAt(rowIndex, 'LineID') == lineID:
                EQPath = pyDataset.getValueAt(rowIndex, 'EqPath')
                print(EQPath)
                row = [pyDataset.getValueAt(rowIndex, colName) for colName in headers]
                lineData.append(row)
               
        UDTFolder = TimePeriodDict.get(timePeriod)
        linePath = '[MES]' + EQPath + '/Analysis/' + UDTFolder + '/DT/DowntimeEventsComposite'
        machineDS = system.dataset.toDataSet(headers, lineData) # Create New Top5 DS for each line
        columnFilter = ['LineID', 'StartDateTime', 'EndDateTime', 'EventID', 
        	'StateID', 'Status', 'Duration', 'WorkOrder', 'ProductCode', 'ParentReason']
        filteredDataset = system.dataset.filterColumns(machineDS, columnFilter) #Filter DS (Get rid of unwanted Columns)
        #print linePath
        #print UDTFolder        
        writePaths.append(linePath)
        writeValues.append(filteredDataset)
        
    system.tag.writeBlocking(writePaths,writeValues)
    
#@timeit
@error_log
#@dump_args
def writeAllDtTop5(timePeriod, pyDataset, top5Type=''):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
	Args:
	  timeRangeFolder (String): 'Shift', 'Run', 'Realtime'
	  pyDataset (pyDataset): PyDS of all dtEvents that need to be separated.
	Returns:
	  (int): 1 if passing, else -1
	Testing:
	    print(mes.downtime.periodic.writeAllDtEvents('shift', pyDataset))		
	TODO: Function takes "elapsed time: 0.106000"
	"""	
	
	#linesDS = mes.config.getAssets.getAllLinesForSite(1)
	writePaths, writeValues = [],[]
	
	timeRangeFolder = 'shift'
	headers = ['LineID', 'Name', 'Quantity', 'EqPath']
	for lineID in lines:
		lineData,EQPath = [],''
		for row in pyDataset:
			if row['LineID'] == lineID:
				EQPath = row['EqPath']
				lineData.append(row)
				
		if EQPath == '': pass # this line isnt in the dataset
		else:
			UDTFolder = TimePeriodDict.get(timePeriod)
			if top5Type == 'Micro': linePath = '[MES]' + EQPath + '/Analysis/' + UDTFolder + '/DT/Top5Micro'
			else: linePath = '[MES]' + EQPath + '/Analysis/' + UDTFolder + '/DT/Top5'	
			machineDS = system.dataset.toDataSet(headers, lineData) # Create New Top5 DS for each line
			columnFilter = ['Name', 'Quantity']
			filteredDataset = system.dataset.filterColumns(machineDS, columnFilter) #Filter DS (Get rid of unwanted Columns)
					
			writePaths.append(linePath)
			writeValues.append(filteredDataset)
	#print linePath
	#print(writePaths, writeValues)
	if len(writePaths) == len(writeValues):system.tag.writeBlocking(writePaths,writeValues)	
	

#@timeit
@error_log
#@dump_args
def writeAllStateTimeline(timePeriod, pyDataset):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
	Args:
	  timeRangeFolder (String): 'Shift', 'Run', 'Realtime'
	  pyDataset (pyDataset): PyDS of all dtEvents that need to be separated.
	Returns:
	  (int): 1 if passing, else -1
	Testing:
	    print(mes.downtime.periodic.writeAllDtEvents('shift', pyDataset))		
	TODO: Function takes "elapsed time: 0.106000"
	"""	
	EQPath = ''
	
	writePaths, writeValues = [],[]

	headers = ['StartDateTime', 'EndDateTime', 'StateID', 'Status', 'Duration', 'COLOR', 'LineID', 'Line', 'EqPath', 'EventID']
	
	for lineID in lines:
		lineData = []
		for row in pyDataset:
			if row['LineID'] == lineID:
				EQPath = row['EqPath']
				lineData.append(row)
		UDTFolder = TimePeriodDict.get(timePeriod)
		linePath = '[MES]' + EQPath + '/Analysis/' + UDTFolder + '/DT/StateHistory'
		machineDS = system.dataset.toDataSet(headers, lineData) # Create New Top5 DS for each line
		pyData = system.dataset.toPyDataSet(machineDS)
		for col in pyData:
			for row in col:
				print row
		columnFilter = ['LineID', 'StartDateTime', 'EndDateTime', 'EventID', 'StateID', 'Status', 'Duration', 'COLOR']
		filteredDataset = system.dataset.filterColumns(machineDS, columnFilter) #Filter DS (Get rid of unwanted Columns)
				
		writePaths.append(linePath)
		writeValues.append(filteredDataset)
	
	#print(writePaths, writeValues)
	system.tag.writeBlocking(writePaths,writeValues)	


#@timeit
@error_log
#@dump_args
def writeDtSummary(timePeriod, pyDataset):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
		  pyDataset (Dataset): 'Shift', 'Run', 'Realtime'
		  tagNameDict (Dictionary): 'Area', 'Group', 'Site'
		Returns:
		  (int): 1 if passing, else -1
		Testing:
			upPyDS = mes.downtime.periodic.getallPlannedUnplannedDT('current shift')
			mes.downtime.periodic.writePlannedUnplannedDT('current shift',upPyDS)
		TODO:
	"""
	# setup global variables
	writeTagPaths, writeTagValues = [], []
		
	columns = pyDataset.getColumnNames()
	for row in pyDataset: #X	#3 Parse through pyDS and get each row (line)
		for key in DTSummaryDict.keys():
			if key in columns: #if we match a known TagName get name and value
				#X	#4a For each row create string for tagPath from equipment path
				EQPath = row["EQPath"]
				tagName = DTSummaryDict.get(key)
				UDTFolder = TimePeriodDict.get(timePeriod)
				currentTagPath = '[MES]' + EQPath + '/Analysis/'+ UDTFolder +'/DT/' + tagName
				#X	#4b add tagpath and value for each column in the row ('/SHIFT/OEE', 0.9023)
				itemValue = row[key]
				itemPath = currentTagPath
				#X	#5 Append tagpath and values to each dataset
				writeTagPaths.append(itemPath)
				writeTagValues.append(itemValue)
	#TROUBLESHOOTING PATH ISSUES
	#for num in range(0, len(writeTagPaths)):
	#	print(writeTagPaths[num], writeTagValues[num])
	
	if len(writeTagPaths) > 0 and len(writeTagValues) > 0:
		# Execute the write operation.
		system.tag.writeBlocking(writeTagPaths, writeTagValues)
		return 1 #SUCCESS
			

#@timeit
@error_log
#@dump_args
def tagWriteDtTop5(timePeriod, valuesList, top5Type=''):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
	Args:
	  timeRangeType (String): 'Shift', 'Run', 'Realtime'
	  machineRange (String): 'Area', 'Group', 'Site'
	  machineID (Int): 1 #PK of that asset (line,area, group, etc.)

	Returns:
	  (int): 1 if passing, else -1
	Testing:
	    print(mes.downtime.periodic.writeDtTop5('Shift','Site', 1))		
	 	
	TODO: Function takes "elapsed time: 0.106000" (for only 1 Pod(Group) of Clarios)
	"""	

 	# setup global variables
 	writeTagPaths, writeTagValues = [], []
 	
 	#print(top5Type,valuesList)
 	UDTFolder = TimePeriodDict.get(timePeriod)
 	
 	for dataset in range(0,len(valuesList)):
 		pyDataset = valuesList[dataset] #<--- what is this its not supposed to be here...... removed 9/18/23
 		if type(pyDataset) == int: return -1 # Datasets are empty
		else: #DS are intact
			EQPath = pyDataset.getValueAt(0,'EqPath')
			columnFilter = ["Name", "Quantity"]
			filteredPyDataset = system.dataset.filterColumns(pyDataset, columnFilter)
			#stpResPyDS = system.dataset.toPyDataSet(stpRes)
		
		if (filteredPyDataset.getRowCount() < 1) : pass #return -1 # Datasets are empty
		else: #DS are intact
			#print(stpRes,EQPath,stpResPyDS)
			
			if top5Type == 'Micro': currentTagPath = '[MES]' + EQPath + '/Analysis/' + UDTFolder + '/DT/Top5Micro'
			else: currentTagPath = '[MES]' + EQPath + '/Analysis/' + UDTFolder + '/DT/Top5'	
			itemValue = filteredPyDataset
			itemPath = currentTagPath
		
			#X	#5 Append tagpath and values to each dataset
			writeTagPaths.append(itemPath)
			writeTagValues.append(itemValue)
	
	#TROUBLESHOOTING PATH ISSUES
	#for num in range(0, len(writeTagPaths)):
		#print(writeTagPaths[num], system.dataset.toPyDataSet(writeTagValues[num]))
		
	
	if (len(writeTagPaths) > 0 and len(writeTagValues) > 0) and (len(writeTagPaths) == len(writeTagValues)):
		# Execute the write operation.
		system.tag.writeBlocking(writeTagPaths, writeTagValues)
		return 1 #SUCCESS
			
	
#@timeit
@error_log
#@dump_args
def writeDtTop5(timeRangeFolder, pyDataset, tagNameDict, top5Type=''):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
	Args:
	  timeRangeType (String): 'Shift', 'Run', 'Realtime'
	  machineRange (String): 'Area', 'Group', 'Site'
	  machineID (Int): 1 #PK of that asset (line,area, group, etc.)
	Returns: (int): 1 if passing, else -1
	Testing: print(mes.downtime.periodic.writeDtTop5('Shift','Site', 1))		
	TODO: Function takes "elapsed time: 0.106000" (for only 1 Pod(Group) of Clarios)
	"""	

 	# setup global variables
 	writeTagPaths, writeTagValues = [], []
 		 
	if (pyDataset.getRowCount() < 1): stpResPyDS = pyDataset #return -1 # Datasets are empty
	else: #DS are intact
		EQPath = pyDataset.getValueAt(0,'EqPath')
		columnFilter = ["Name", "Quantity"]
		filteredPyDataset = system.dataset.filterColumns(pyDataset, columnFilter)
		#stpResPyDS = system.dataset.toPyDataSet(stpRes)
	
	if (filteredPyDataset.getRowCount() < 1) : pass #return -1 # Datasets are empty
	else: #DS are intact
		#print(stpRes,EQPath,stpResPyDS)
		if top5Type == 'Micro': currentTagPath = '[MES]' + EQPath + '/Analysis/' + timeRangeFolder + '/DT/Top5Micro'
		else: currentTagPath = '[MES]' + EQPath + '/Analysis/' + timeRangeFolder + '/DT/Top5'	
		itemValue = filteredPyDataset
		itemPath = currentTagPath
	
		#X	#5 Append tagpath and values to each dataset
		writeTagPaths.append(itemPath)
		writeTagValues.append(itemValue)
		
		if len(writeTagPaths) > 0 and len(writeTagValues) > 0:
			# Execute the write operation.
			system.tag.writeBlocking(writeTagPaths, writeTagValues)
			return 1 #SUCCESS
			
			
#@timeit
@error_log
#@dump_args
def writePlannedUnplannedDT(timePeriod, pyDataset):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
		  pyDataset (Dataset): 'Shift', 'Run', 'Realtime'
		  tagNameDict (Dictionary): 'Area', 'Group', 'Site'
		Returns:
		  (int): 1 if passing, else -1
		Testing:
			upPyDS = mes.downtime.periodic.getallPlannedUnplannedDT('current shift')
			mes.downtime.periodic.writePlannedUnplannedDT('current shift',upPyDS)
		TODO:
	"""
	# setup global variables
	writeTagPaths, writeTagValues = [], []
		
	columns = pyDataset.getColumnNames()
	for row in pyDataset: #X	#3 Parse through pyDS and get each row (line)
		for key in DTPlannedDict.keys():
			if key in columns: #if we match a known TagName get name and value
				#X	#4a For each row create string for tagPath from equipment path
				EQPath = row["EQPath"]
				tagName = DTPlannedDict.get(key)
				UDTFolder = TimePeriodDict.get(timePeriod)
				currentTagPath = '[MES]' + EQPath + '/Analysis/'+ UDTFolder +'/DT/' + tagName
				#X	#4b add tagpath and value for each column in the row ('/SHIFT/OEE', 0.9023)
				itemValue = row[key]
				itemPath = currentTagPath
				#X	#5 Append tagpath and values to each dataset
				writeTagPaths.append(itemPath)
				writeTagValues.append(itemValue)
	#TROUBLESHOOTING PATH ISSUES
	#for num in range(0, len(writeTagPaths)):
	#	print(writeTagPaths[num], writeTagValues[num])
	
	if len(writeTagPaths) > 0 and len(writeTagValues) > 0:
		# Execute the write operation.
		system.tag.writeBlocking(writeTagPaths, writeTagValues)
		return 1 #SUCCESS