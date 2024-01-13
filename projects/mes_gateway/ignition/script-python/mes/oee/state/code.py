'''
This contains all tag heirarchy workorder functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.oee.state')

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()




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
def getLineState(statusType, line, lineConfigDS, lineCellsDS, lineState=None):
	"""
	TODO: Function takes "elapsed time: 0.335000" (Boooooo!!!!))
		1. Find other ways to optimize (only look once)
		2. Prioritize Fault Int over state
		3. Add logic to check for line faults and mode if cellconfig == 0
		4. Add logic to look for first reason that is not blocked
			if blocked go up (lower number in cell order)
	#Args:
		# statusType (String): 'fault', 'mode' or 'state'
		# line (String): line name 
		# lineConfigDS (Dataset): Contains line config parameters 
		# lineCellsDS (Dataset): contains all cell info for line
		#  lineState (Integer): Used to check raw line state
	#Testing:
		#configRead = system.tag.readBlocking(['[default]Clarios/Toledo/AGM Assembly/Line9/config/LineConfigDS','[default]Clarios/Toledo/AGM Assembly/Line9/config/LineCellsConfigDS'])
		#lineName = 'Line9'
		#print(mes.state.getLineStatus('state', lineName, configRead[0].value, configRead[1].value))		
	"""
	cellsPyDS, lineConfigPyDS = system.dataset.toPyDataSet(lineCellsDS), system.dataset.toPyDataSet(lineConfigDS)
		#check if DSs are empty
		
	if ( len(lineConfigPyDS) < 1) : return 0 # (cellsPyDS will be empty if there is a line with no cells (standalone)
	elif ( len(cellsPyDS) < 1 and lineState != None) : return lineState
	else: #DS are intact
		# There is only 1 row, so no FOR loop needed
		readPath = lineConfigPyDS.getValueAt(0, 'EquipmentPath')
		detectType = lineConfigPyDS.getValueAt(0, 'EquipmentDowntimeDetectiontType')	
		
		# TODO ***********
		#Parallel cells only
		#configCellsRunning = lineConfigPyDS.getValueAt(0, 'MinCellsRunning')	
		
		# TODO **** Check Mode for reasons to skip calcs (Changeover, Maintenance, etc)
		#if lineMode in PlannedDTReasons:
		#	#move line mode into state
		#	status = lineMode
		
		# Step 3 turn data for Cells into a Dict for quick lookup
		# **** Cells are in reverse CellOrder for ease of use
		cellsDict, cellTagList = {}, []
		numCellsRunning, lowestOrder, highestStatus, initialStatus, initialDate = 0, 100, 0, 1, system.date.now()
		status = 1
		
		for row  in range(0, len(cellsPyDS)):  # a row for each cell
			innerCellDict = {}
			cellName = cellsPyDS.getValueAt(row, 'Name')
			cellIsKeyCell = cellsPyDS.getValueAt(row, 'KeyCell')
			cellOrder = cellsPyDS.getValueAt(row, 'CellOrder')
			statusPath = '[default]' + readPath +'/'+ cellName +'/'+ statusType # (String): 'mode' or 'state'
			tagReadValue = system.tag.readBlocking([statusPath])
			cellStatus = tagReadValue[0].value
			cellTimestamp = tagReadValue[0].timestamp
			
			# Skip updating the state if cellOrder is zero
			if cellOrder == 0: continue
			
			#For key cell
			if cellIsKeyCell: keyCellStatus = cellStatus
			#For inital cell
			#if innerCellDict['status'] != 1 and innerCellDict['statusTime'] < initialDate:
			if cellStatus != 1 and cellTimestamp < initialDate:
				#if cellStatus == 4 and cellOrder != 1: pass # ignore blocked cell (go to next higher cell order) 
				#else:
				initialDate = cellTimestamp
				initialStatus = cellStatus
			#For equipmentState cell (Check Highest Value)
			if cellStatus > highestStatus: 
				highestStatus = cellStatus
				highestCell  =  cellName
				
			#For parallel Cells
			if cellStatus == 1:
				numCellsRunning += 1 

		#For parallel Cells
		#if numCellsRunning < configCellsRunning: parallelCellStatus = 0
		#else: parallelCellStatus = 1
		
		#Step 4 Return Correct status (Equiment Mode, Key reason, etc)
		if detectType == 1: 
			status = highestStatus # Equipment Mode
		if detectType == 2: 
			status = initialStatus # Initial Cell (sooner timestamp)
		if detectType == 3: 
			# TODO ******** Test status
			#status = parallelCellStatus
			status = 1 # Parallel Cells	
		if detectType == 4: 
			status = keyCellStatus # Key Cell 
			
		
		#if verbose: print(detectType, status, cellsDict)
	if status >= 0: return status
	else: return 99999
	#print(getLineStatus('mode', lineName, lineConfigDS, lineCellsDS))