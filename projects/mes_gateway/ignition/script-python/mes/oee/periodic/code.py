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

#logger.info(str(siteID))
#logger.info(str(micro))
#logger.info(str(areas))


# TagName Mapping {DBColumnName : TagName}
OEETagDict={'Start':'DateTimeStart', 
	'End':'DateTimeEnd', 'Infeed':'Infeed','Reject':'Reject', 
	'Total':'Outfeed','PlannedMins':'PlannedMinutes','Downtime':'Downtime',
	'Runtime':'Runtime','A':'Availability','Q':'Quality','P':'Performance', 
	'Scrap':'Scrap','OEE':'OEE','TEEP':'TEEP'} #'MTBS':'MTBS','MTBF':'MTBF','MTTR':'MTTR'}


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
def calcLineOEEHour():
	pass
	# Write back to [MES] tag provider with equipment path
	
	
#@timeit
@error_log
#@dump_args
def calcLineOEERun():
	pass
	# Write back to [MES] tag provider with equipment path


#@timeit
@error_log
#@dump_args
def getAllLinesOEE_AQP(timePeriod,SiteID):
	""" Description of function purpose
		Args:
			timeRangeType (String): 'Shift', 'Run', 'Realtime'
	  		machineRange (String): 'Area', 'Group', 'Site'
	  		machineID (Int): 1 #PK of that asset (line,area, group, etc.)
		Returns:
			(int): 1 if passing, else -1
		Testing: (script console)
			print(mes.downtime.periodic.getAllLinesOEE_AQP('Shift', 1))
		TODO:
	"""
	#print(timePeriod, TimePeriodDict.keys())
	# Check time range to make sure it one of the avialable types
	if timePeriod in TimePeriodDict.keys(): stpRes = mes.oee.sp.getPeriodAllLinesOEE_AQP(timePeriod, SiteID, micro)
	else: return -1 #Failure
	
	stpResPyDS = system.dataset.toPyDataSet(stpRes)
	if(len(stpResPyDS) > 0): return stpResPyDS
	else: return -1 #Failure


#@timeit
@error_log
#@dump_args
def getOEE_AQP(timePeriod,machineRange,machineID):
	""" Description of function purpose
		Args:
			timeRangeType (String): 'Shift', 'Run', 'Realtime'
	  		machineRange (String): 'Area', 'Group', 'Site'
	  		machineID (Int): 1 #PK of that asset (line,area, group, etc.)
		Returns:
			(int): 1 if passing, else -1
		Testing: (script console)
			print(mes.downtime.periodic.getOEE_AQP('Shift','Area', 1))
		TODO:
	"""
	#print(machineRange,AggregateDict.keys(), timeRangeType, TimePeriodDict.keys())
	# Check time range to make sure it one of the avialable types
	if machineRange in AggregateDict.keys():
		
		#2 get DS from SPROC based on machineRange
		if machineRange == 'Group': stpRes = mes.oee.sp.getPeriodOEE_AQP(timePeriod, machineID)
		elif machineRange == 'Area': stpRes = mes.oee.sp.getPeriodAreaOEE_AQP(timePeriod, machineID)
		elif machineRange == 'Site': stpRes = mes.oee.sp.getPeriodSiteOEE_AQP(timePeriod)
		else: pass
	else: return -1 #Failure
	stpResPyDS = system.dataset.toPyDataSet(stpRes)
	if(len(stpResPyDS) > 0): return stpResPyDS
	else: return -1 #Failure


#@timeit
@error_log
#@dump_args
def getOEETable(timePeriod,machineRange,machineID):
	""" Description of function purpose
		Args:
			timeRangeType (String): 'Shift', 'Run', 'Realtime'
	  		machineRange (String): 'Area', 'Group', 'Site'
	  		machineID (Int): 1 #PK of that asset (line,area, group, etc.)
		Returns:
			(int): 1 if passing, else -1
		Testing: (script console)
			print(mes.downtime.periodic.getOEE_AQP('Shift','Area', 1))
		TODO:
	"""
	
	# Check time range to make sure it one of the avialable types
	if machineRange in AggregateDict.keys(): # and timePeriod in TimePeriodDict.keys():
		#2 get DS from SPROC based on machineRange
		if machineRange == 'Group': stpRes = mes.oee.sp.getPeriodGroupOEETable(timePeriod, machineID)
		elif machineRange == 'Area': stpRes = mes.oee.sp.getPeriodAreaOEETable(timePeriod, machineID)
		elif machineRange == 'Site': stpRes = mes.oee.sp.getPeriodSiteOEETable(timePeriod, machineID)
		else: pass
	else: return -1 #Failure
	
	stpResPyDS = system.dataset.toPyDataSet(stpRes)
	if(len(stpResPyDS) > 0): return stpResPyDS
	else: return -1 #,-1 #Failure


#@timeit
@error_log
#@dump_args
def writeOEE_AQP(timePeriod, pyDataset):
    print("Processing for timePeriod: {}".format(timePeriod))
    writeTagPaths, writeTagValues = [], []

    columns = pyDataset.getColumnNames()
    print("Columns in the dataset: {}".format(columns))

    for row in pyDataset:
        for key in OEETagDict.keys():
            if key in columns:
                EQPath = row["EQPath"]
                tagName = OEETagDict.get(key)
                UDTFolder = TimePeriodDict.get(timePeriod)
                currentTagPath = '[MES]' + EQPath + '/Analysis/'+ UDTFolder +'/OEE/' + tagName
                print("Current Tag Path: {}".format(currentTagPath))

                itemValue = row[key]
                itemPath = currentTagPath
                writeTagPaths.append(itemPath)
                writeTagValues.append(itemValue)
                print("Appending Tag Path: {} with Value: {}".format(itemPath, itemValue))

    if len(writeTagPaths) > 0 and len(writeTagValues) > 0:
        print("Executing system tag write...")
        system.tag.writeBlocking(writeTagPaths, writeTagValues)
        print("Write successful.")
        return 1

    print("No tags written.")


#@timeit
@error_log
#@dump_args
def writeOEETable(timePeriod, pyDataset): #, tagNameDict, top5Type=''):
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
		TODO: Function takes "elapsed time: 0._______" 
	"""	

 	# setup global variables
	writeTagPaths, writeTagValues = [], []
 	#print(pyDataset.getColumnNames())
 		 	 
	if (pyDataset.getRowCount() < 1): stpResPyDS = pyDataset #return -1 # Datasets are empty
	else: #DS are intact
		headers = ['AreaID', 'EqPath', 'LineID', 'Line', 'OEE', 'Running', 'PlannedOrder', 'RunProgress', 'ProgressPercent', 'TimeRemaining', 'Operator']
		#print(pyDataset, areas)
		for areaID in areas:
			areaData,EQPath = [],''
			for row in pyDataset:
				if row['AreaID'] == areaID:
					EQPath = row['EqPath']
					areaData.append(row)
					
			if EQPath == '': pass # this line isnt in the dataset
			else:
				UDTFolder = TimePeriodDict.get(timePeriod)
				linePath = '[MES]' + EQPath + '/Analysis/' + UDTFolder + '/OEE/OEETable'
				#print(headers, areaData)
				machineDS = system.dataset.toDataSet(headers, areaData) # Create New Top5 DS for each line
				columnFilter = ["Line", "OEE","Running", "PlannedOrder","RunProgress","ProgressPercent","TimeRemaining","Operator"]
				filteredDataset = system.dataset.filterColumns(machineDS, columnFilter) #Filter DS (Get rid of unwanted Columns)
						
				writeTagPaths.append(linePath)
				writeTagValues.append(filteredDataset)
				
	#TROUBLESHOOTING PATH ISSUES
	#for num in range(0, len(writeTagPaths)):
	#	print(writeTagPaths[num], writeTagValues[num])
	
	#print(writePaths, writeValues)
	if len(writeTagPaths) == len(writeTagValues): system.tag.writeBlocking(writeTagPaths,writeTagValues)	


@timeit
@error_log
#@dump_args
def productionChartTransform(EqPath):
	""" Description of function purpose
		Args:
			EqPath (String): 'Enterprise/Site/Area/Line'
		Returns:
			Dataset of converted rows (for tag Write)
			# --(JSON): a json object of the converted rows for the production chart
		Testing: (script console)
			print(mes.oee.periodic.productionChartTransform(eqPath))
		TODO: stuff
	"""
	import random
	
	_ret = []
	_rows = 8*4 #32 rows (every 15 minutes for 8 hours)
	
	#tagPaths
	#defaultProvider = '[default]'
	providerPath = '[default]' + EqPath

	historyPath = providerPath + '/calculatedValues/shiftGoodParts' # Make a new shiftCounts Tag in the Calculated Values
	countIdealPath = providerPath + '/calculatedValues/shiftIdealParts' # Make a new ShiftIdeal Tag in the Calculated Valuesshift (Reference TEEP from (OEE UDT in [MES)]
	countTargetPath = providerPath + '/calculatedValues/shiftGoodPartsTarget' # Make a new ShiftTarget Tag in the Calculated Values (Area config Target for this value)
	columnName = EqPath + '/calculatedValues/shiftGoodParts'	
	shiftStartPath = providerPath + '/calculatedValues/time/shiftStartTime'
	shiftStart = system.tag.readBlocking([shiftStartPath])[0].value
	shiftEnd = system.date.now()

	_time_start = system.date.toMillis(shiftStart)
	_time_end = system.date.toMillis(shiftEnd)
	_time_step = (_time_end - _time_start)/_rows
		
	historizedData = system.dataset.toPyDataSet(system.tag.queryTagHistory(paths = [historyPath], startDate = shiftStart, endDate = shiftEnd, returnSize = _rows+1, aggregationMode = 'LastValue'))#, intervalMinutes = _tm_step))			
	
	_low_start = 0.0
	_low_end = system.tag.readBlocking([countTargetPath])[0].value
	_low_step = (_low_end - _low_start) / _rows
	_high_start = 0.0
	_high_end = system.tag.readBlocking([countIdealPath])[0].value # already converted (minutes * IdealRate)
	_high_step = (_high_end - _high_start) / _rows
	
	lastval = 0
	lasthigh = 0
	
	dsHeaders, dsValues = ["time","Target","Ideal Rate","Current Rate"], []
	
	for idx in range(_rows+1):
		ctm = _time_start + _time_step*idx
		clow = _low_start + _low_step*idx
		chigh = _high_start + _high_step*idx
		cval = historizedData[idx][columnName]
		if cval < lastval: 
			#_ret.append( { "time": ctm, "low": clow, "high": chigh, "val": "" }) #(OLD JSON RETURN)
			dsValues.append([ctm, clow, chigh, 0])
		else:
			#_ret.append( { "time": ctm, "low": clow, "high": chigh, "val": cval }) #(OLD JSON RETURN)
			dsValues.append([ctm, clow, chigh,  cval])
			lastval = cval
			lasthigh = int(chigh)
	
	testDS = system.dataset.toDataSet(dsHeaders, dsValues)
	return testDS
	#return _ret #(OLD JSON RETURN)

#@timeit
@error_log
#@dump_args		
def updateOEETablePeriodic():
	# get lineID
	res = mes.config.getAssets.getAllLinesForSite(siteID)
	py = system.dataset.toPyDataSet(res)
	# Initialize EQPaths list
	EQPaths = []
	# Loop through the rows in the result
	for row in py:
	    lineID = row['lineID']
	    
	    # Construct the SQL query with the current lineID
	    query =\
	    """
	    SELECT linePath FROM [MES].[config].[vw_productionmodel]
	    WHERE lineID = """+str(lineID)+""" AND lineEnabled <> 0
	    """
	    # Execute the query
	    linePath_result = system.db.runQuery(query)
	    # Assuming the result contains a single row with a 'linePath' column
	    if linePath_result:
	        EQPaths.append(linePath_result[0]['linePath'])
	# Print the EQPaths list
	#print(EQPaths)
	
	######################PART TWO#####################
	for EQPath in EQPaths:
		paths = [
		            '[default]'+EQPath+'/jobs/currentJob/runId',
		            '[default]'+EQPath+'/jobs/currentJob/RunCounts/runGoodParts',
		            '[default]'+EQPath+'/jobs/currentJob/RunCounts/runRawReject',
		            '[default]'+EQPath+'/calculatedValues/oeeAvailability',
		            '[default]'+EQPath+'/calculatedValues/oeePerformance',
		            '[default]'+EQPath+'/calculatedValues/oeeQuality',
		            '[default]'+EQPath+'/calculatedValues/oee'
		        ]
		values = system.tag.readBlocking(paths)
		print EQPath
		ID = values[0].value
		GoodCount = values[1].value
		WasteCount = values[2].value
		print GoodCount
		print WasteCount
		if GoodCount is None or WasteCount is None or GoodCount == '' or WasteCount == '' or GoodCount == 'None' or WasteCount == 'None' or GoodCount == 0 or WasteCount == 0:
		    Total = 0
		else:
		    Total = GoodCount + WasteCount
		Availability = values[3].value
		Performance = values[4].value
		Quality = values[5].value
		OEE = values[6].value
		#print(ID,GoodCount,WasteCount,Total, Availability, Performance, Quality, OEE)
		
		query = \
		"""UPDATE runs
		SET
		    TotalCount = """+str(Total)+""",
		    WasteCount = """+str(WasteCount)+""",
		    GoodCount = """+str(GoodCount)+""",
		    Availibility = """+str(Availability)+""",
		    Performance = """+str(Performance)+""",
		    Quality = """+str(Quality)+""",
		    OEE = """+str(OEE)+"""
		WHERE ID = """+str(ID)+""""""
		#print query
		if GoodCount is None or WasteCount is None or GoodCount == '' or WasteCount == '' or GoodCount == 'None' or WasteCount == 'None' or GoodCount == 0 or WasteCount == 0:
			pass
		else:
			system.db.runUpdateQuery(query)
	#getOEETable with updated values
	#print('Finished Updating Queries')
	for areaID in areas:
		try:
			pyDataset = mes.oee.periodic.getOEETable('current shift', 'Area', areaID)
			if pyDataset == -1:
				logger.info('OEE Table is Empty')
			else:
				mes.oee.periodic.writeOEETable('current shift', pyDataset)
			print('Updated Area ID:'+str(areaID))
		except:
			print 'Failed on'+str(areaID)
