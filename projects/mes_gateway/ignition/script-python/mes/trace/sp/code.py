'''
This contains all Track and Trace Stored Porcedure functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.trace.sp')


# EXAMPLE SP
#def groupOEE_AQP(StartDateTime, EndDateTime, GroupID, LineID):
#	call = system.db.createSProcCall("dbo.stp_getGroupOEE_AQP", db)	
#	call.registerInParam("StartDateTime", system.db.TIMESTAMP, StartDateTime)
#	call.registerInParam("EndDateTime", system.db.TIMESTAMP, EndDateTime)
#	call.registerInParam("GroupID", system.db.INTEGER, GroupID)
#	call.registerInParam("LineID", system.db.INTEGER, LineID)
#	system.db.execSProcCall(call)
#	ret = call.getResultSet()
#	return ret



##############################################################################
## PART HANDLING
##############################################################################
#@timeit
@error_log
#@dump_args
def insertAndGetNewPart(ProductCodeID, CellID, Label, ScheduleID):
	call = system.db.createSProcCall('tat.stp_insertAndGetNewPart', db)
	
	call.registerInParam('ProductCodeID', system.db.INTEGER, ProductCodeID)
	call.registerInParam('CellID', system.db.INTEGER, CellID)
	call.registerInParam('Label', system.db.VARCHAR, Label)
	call.registerInParam('ScheduleID', system.db.INTEGER, ScheduleID)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def getParts(StartTime = None, EndTime = None, Label = None, LabelExactMatch = False, ProductCodeID = None, Workorder = None, InventoryID = None, AccumulatorID = None, GetCompletedOnly = False, GetWIPOnly = False):
	call = system.db.createSProcCall('tat.stp_getParts', db)
	
	call.registerInParam('StartTime', system.db.TIMESTAMP, StartTime)
	call.registerInParam('EndTime', system.db.TIMESTAMP, EndTime)
	call.registerInParam('Label', system.db.VARCHAR, Label)
	call.registerInParam('LabelExactMatch', system.db.BOOLEAN, LabelExactMatch)
	call.registerInParam('ProductCodeID', system.db.INTEGER, ProductCodeID)
	call.registerInParam('Workorder', system.db.VARCHAR, Workorder)
	call.registerInParam('InventoryID', system.db.INTEGER, InventoryID)
	call.registerInParam('AccumulatorID', system.db.INTEGER, AccumulatorID)
	call.registerInParam('GetCompletedOnly', system.db.BOOLEAN, GetCompletedOnly)
	call.registerInParam('GetWIPOnly', system.db.BOOLEAN, GetWIPOnly)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def getPartExactLabelMatch(Label):
	call = system.db.createSProcCall('tat.stp_getPartExactLabelMatch', db)
	
	call.registerInParam('Label', system.db.VARCHAR, Label)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret



##############################################################################
## PART HISTORY
##############################################################################
#@timeit
@error_log
#@dump_args
def getFullPartHistory(PartID = None, Label = None, Workorder = None, ProductCode = None, StartTime = None, EndTime = None):
	call = system.db.createSProcCall('tat.stp_getFullPartHistory', db)
	
	call.registerInParam('PartID', system.db.INTEGER, PartID)
	call.registerInParam('Label', system.db.VARCHAR, Label)
	call.registerInParam('Workorder', system.db.VARCHAR, Workorder)
	call.registerInParam('ProductCode', system.db.VARCHAR, ProductCode)
	call.registerInParam('StartTime', system.db.TIMESTAMP, StartTime)
	call.registerInParam('EndTime', system.db.TIMESTAMP, EndTime)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def insertPartHistoryRecord(EventTypeID, PartID = None, Label = None, LineLocation = None, CellID = None, AccumulatorID = None, InventoryID = None, TimeScanned = None, Notes = None, Metadata = None):
	call = system.db.createSProcCall('tat.stp_insertPartHistoryRecord', db)
	
	call.registerInParam('EventTypeID', system.db.INTEGER, EventTypeID)
	call.registerInParam('PartID', system.db.INTEGER, PartID)
	call.registerInParam('Label', system.db.VARCHAR, Label)
	call.registerInParam('LineLocation', system.db.VARCHAR, LineLocation)
	call.registerInParam('AccumulatorID', system.db.INTEGER, AccumulatorID)
	call.registerInParam('InventoryID', system.db.INTEGER, InventoryID)
	call.registerInParam('TimeScanned', system.db.TIMESTAMP, TimeScanned)
	call.registerInParam('Notes', system.db.VARCHAR, Notes)
	call.registerInParam('Metadata', system.db.VARCHAR, Metadata)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False


#@timeit
@error_log
#@dump_args
def updateCompletePart(PartID, CellID, TimeCompleted = None):
	call = system.db.createSProcCall('tat.stp_updateCompletePart', db)
	
	call.registerInParam('PartID', system.db.INTEGER, PartID)
	call.registerInParam('CellID', system.db.INTEGER, CellID)
	call.registerInParam('TimeCompleted', system.db.TIMESTAMP, TimeCompleted)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False



##############################################################################
## INVENTORIES
##############################################################################
#@timeit
@error_log
#@dump_args
def getInventories(SiteID):
	call = system.db.createSProcCall('tat.stp_getInventories', db)
	call.registerInParam('SiteID', system.db.INTEGER, SiteID)
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def addPartToInventory(InventoryID, PartID, InventoryLocation = None):
	call = system.db.createSProcCall('tat.stp_addPartToInventory', db)
	
	call.registerInParam('InventoryID', system.db.INTEGER, InventoryID)
	call.registerInParam('InventoryLocation', system.db.VARCHAR, InventoryLocation)
	call.registerInParam('PartID', system.db.INTEGER, PartID)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False


#@timeit
@error_log
#@dump_args
def removePartFromInventory(InventoryID, PartID):
	call = system.db.createSProcCall('tat.stp_removePartFromInventory', db)
	
	call.registerInParam('InventoryID', system.db.INTEGER, InventoryID)
	call.registerInParam('PartID', system.db.INTEGER, PartID)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False



##############################################################################
## ACCUMULATORS
##############################################################################
#@timeit
@error_log
#@dump_args
def getAccumulators(SiteID, GetDisabled = False):
	call = system.db.createSProcCall('tat.stp_getAccumulators', db)
	
	call.registerInParam('SiteID', system.db.INTEGER, SiteID)
	call.registerInParam('GetDisabled', system.db.BOOLEAN, GetDisabled)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def addPartToAccumulator(AccumulatorID, PartID):
	call = system.db.createSProcCall('tat.stp_addPartToAccumulator', db)
	
	call.registerInParam('AccumulatorID', system.db.INTEGER, AccumulatorID)
	call.registerInParam('PartID', system.db.INTEGER, PartID)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False


#@timeit
@error_log
#@dump_args
def removePartFromAccumulator(AccumulatorID, PartID):
	call = system.db.createSProcCall('tat.stp_removePartFromAccumulator', db)
	
	call.registerInParam('AccumulatorID', system.db.INTEGER, AccumulatorID)
	call.registerInParam('PartID', system.db.INTEGER, PartID)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False



##############################################################################
## MATERIALS AND MATERIAL LOTS
##############################################################################
#@timeit
@error_log
#@dump_args
def getMaterials(SiteID, GetDisabled = False):
	call = system.db.createSProcCall('tat.stp_getMaterials', db)
	
	call.registerInParam('SiteID', system.db.INTEGER, SiteID)
	call.registerInParam('GetDisabled', system.db.BOOLEAN, GetDisabled)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def insertMaterial(SiteID, Name, Description = None):
	call = system.db.createSProcCall('tat.stp_insertAndGetNewMaterial', db)
	
	call.registerInParam('SiteID', system.db.INTEGER, SiteID)
	call.registerInParam('Name', system.db.VARCHAR, Name)
	call.registerInParam('Description', system.db.VARCHAR, Description)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret.getValueAt(0, 'ID')


#@timeit
@error_log
#@dump_args
def updateMaterial(MaterialID, Name = None, Description = None, IsEnabled = None):
	call = system.db.createSProcCall('tat.stp_updateMaterial', db)
	
	call.registerInParam('MaterialID', system.db.INTEGER, MaterialID)
	call.registerInParam('Name', system.db.VARCHAR, Name)
	call.registerInParam('Description', system.db.VARCHAR, Description)
	call.registerInParam('IsEnabled', system.db.BOOLEAN, IsEnabled)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False


#@timeit
@error_log
#@dump_args
def deleteMaterial(MaterialID):
	call = system.db.createSProcCall('tat.stp_deleteMaterial', db)
	
	call.registerInParam('MaterialID', system.db.INTEGER, MaterialID)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False


#@timeit
@error_log
#@dump_args
def getMaterialLots(SiteID, MaterialID = None, GetZeroQty = False, GetDisabled = False):
	call = system.db.createSProcCall('tat.stp_getMaterialLots', db)
	
	call.registerInParam('SiteID', system.db.INTEGER, SiteID)
	call.registerInParam('MaterialID', system.db.INTEGER, MaterialID)
	call.registerInParam('GetZeroQty', system.db.BOOLEAN, GetZeroQty)
	call.registerInParam('GetDisabled', system.db.BOOLEAN, GetDisabled)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def insertMaterialLot(MaterialID, LotNumber, RemainingQty, Description = None):
	call = system.db.createSProcCall('tat.stp_insertAndGetNewMaterialLot', db)
	
	call.registerInParam('MaterialID', system.db.INTEGER, MaterialID)
	call.registerInParam('LotNumber', system.db.VARCHAR, LotNumber)
	call.registerInParam('RemainingQty', system.db.DECIMAL, RemainingQty)
	call.registerInParam('Description', system.db.VARCHAR, Description)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret.getValueAt(0, 'ID')


#@timeit
@error_log
#@dump_args
def updateMaterialLot(MaterialLotID, MaterialID = None, LotNumber = None, RemainingQty = None, Description = None, IsEnabled = None):
	call = system.db.createSProcCall('tat.stp_updateMaterialLot', db)
	
	call.registerInParam('MaterialLotID', system.db.INTEGER, MaterialLotID)
	call.registerInParam('MaterialID', system.db.INTEGER, MaterialID)
	call.registerInParam('LotNumber', system.db.VARCHAR, LotNumber)
	call.registerInParam('RemainingQty', system.db.DECIMAL, RemainingQty)
	call.registerInParam('Description', system.db.VARCHAR, Description)
	call.registerInParam('IsEnabled', system.db.BOOLEAN, IsEnabled)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False


#@timeit
@error_log
#@dump_args
def deleteMaterialLot(MaterialLotID):
	call = system.db.createSProcCall('tat.stp_deleteMaterialLot', db)
	
	call.registerInParam('MaterialLotID', system.db.INTEGER, MaterialLotID)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False

def addInventory(Name, SiteID):
	call = system.db.createSProcCall('tat.stp_insertInventory', db)
	
	call.registerInParam('Name', system.db.VARCHAR, Name)
	call.registerInParam('SiteID', system.db.INTEGER, SiteID)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False

def addAccumulator(Name, SiteID):
	call = system.db.createSProcCall('tat.stp_insertAccumulator', db)
	
	call.registerInParam('Name', system.db.VARCHAR, Name)
	call.registerInParam('SiteID', system.db.INTEGER, SiteID)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False
		
def RemoveInventory(ID):
	call = system.db.createSProcCall('tat.stp_removeInventory', db)
	
	call.registerInParam('ID', system.db.INTEGER, ID)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False
		
def RemoveAccumulator(ID):
	call = system.db.createSProcCall('tat.stp_removeAccumulator', db)
	
	call.registerInParam('ID', system.db.INTEGER, ID)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False