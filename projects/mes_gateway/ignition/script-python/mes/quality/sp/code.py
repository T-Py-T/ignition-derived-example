'''
This contains all OEE calculation functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()
#micro = mes.config._scriptHeaders.micro
#siteID = mes.config._scriptHeaders.siteID
#areas = mes.config._scriptHeaders.areas
#lines = mes.config._scriptHeaders.lines
#TimePeriodDict = mes.config._scriptHeaders.TimePeriodDict
#AggregateDict = mes.config._scriptHeaders.AggregateDict



# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.quality.sp')


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     EXAMPLE SP FUNCTION
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#@timeit
#@error_log
#@dump_args
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
## TEST TYPES
##############################################################################
#@timeit
@error_log
#@dump_args
def getTestTypes(SiteID):
	call = system.db.createSProcCall('qms.stp_getTestTypes', db)
	
	call.registerInParam('SiteID', system.db.INTEGER, SiteID)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret



##############################################################################
## TEST ENUMS
##############################################################################
#@timeit
@error_log
#@dump_args
def getTestAttributeDataTypes():
	call = system.db.createSProcCall('qms.stp_getTestAttributeDataTypes', db)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def getTestStatuses(SiteID):
	call = system.db.createSProcCall('qms.stp_getTestStatuses', db)
	
	call.registerInParam('SiteID', system.db.INTEGER, SiteID)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret



##############################################################################
## TESTS
##############################################################################
#@timeit
@error_log
#@dump_args
def insertAndGetNewTest(TestTypeID, PartID = None, MaterialLotID = None):
	call = system.db.createSProcCall('qms.stp_insertAndGetNewTest', db)
	
	call.registerInParam('TestTypeID', system.db.INTEGER, TestTypeID)
	call.registerInParam('PartID', system.db.INTEGER, PartID)
	call.registerInParam('MaterialLotID', system.db.INTEGER, MaterialLotID)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def getTests(SiteID, TestID = None, TestTypeID = None, Label = None, ProductCodeID = None, MaterialLotNumber = None, MaterialID = None, WorkorderID = None, IsPass = None, TestStatusID = None, StartDate = None, EndDate = None):
	call = system.db.createSProcCall('qms.stp_getTests', db)
	
	call.registerInParam('SiteID', system.db.INTEGER, SiteID)
	call.registerInParam('TestID', system.db.INTEGER, TestID)
	call.registerInParam('TestTypeID', system.db.INTEGER, TestTypeID)
	call.registerInParam('Label', system.db.VARCHAR, Label)
	call.registerInParam('ProductCodeID', system.db.INTEGER, ProductCodeID)
	call.registerInParam('MaterialLotNumber', system.db.VARCHAR, MaterialLotNumber)
	call.registerInParam('MaterialID', system.db.INTEGER, MaterialID)
	call.registerInParam('WorkorderID', system.db.INTEGER, WorkorderID)
	call.registerInParam('IsPass', system.db.BOOLEAN, IsPass)
	call.registerInParam('TestStatusID', system.db.INTEGER, TestStatusID)
	call.registerInParam('StartDate', system.db.TIMESTAMP, StartDate)
	call.registerInParam('EndDate', system.db.TIMESTAMP, EndDate)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def updateTest(TestID, IsPass, AttributeValues, PartID = None, MaterialLotID = None, Notes = None):
	call = system.db.createSProcCall('qms.stp_updateTest', db)
	
	call.registerInParam('TestID', system.db.INTEGER, TestID)
	call.registerInParam('PartID', system.db.INTEGER, PartID)
	call.registerInParam('MaterialLotID', system.db.INTEGER, MaterialLotID)
	call.registerInParam('IsPass', system.db.BOOLEAN, IsPass)
	call.registerInParam('Notes', system.db.VARCHAR, Notes)
	call.registerInParam('Values', system.db.VARCHAR, AttributeValues)
	
	try:
		system.db.execSProcCall(call)
		return True
	except Exception as e:
		return False


#@timeit
@error_log
#@dump_args
def updateTestStatus(TestID, StatusName, ChangedBy):
	call = system.db.createSProcCall('qms.stp_updateTestStatus', db)
	
	call.registerInParam('TestID', system.db.INTEGER, TestID)
	call.registerInParam('StatusName', system.db.VARCHAR, StatusName)
	call.registerInParam('ChangedBy', system.db.VARCHAR, ChangedBy)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False


#@timeit
@error_log
#@dump_args
def disableTest(TestID):
	call = system.db.createSProcCall('qms.stp_disableTest', db)
	
	call.registerInParam('TestID', system.db.INTEGER, TestID)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False



##############################################################################
## TEST ATTRIBUTES
##############################################################################
#@timeit
@error_log
#@dump_args
def getTestAttributes(TestTypeID, ProductCodeID = None, MaterialID = None):
	call = system.db.createSProcCall('qms.stp_getTestAttributes', db)
	
	call.registerInParam('TestTypeID', system.db.INTEGER, TestTypeID)
	call.registerInParam('ProductCodeID', system.db.INTEGER, ProductCodeID)
	call.registerInParam('MaterialID', system.db.INTEGER, MaterialID)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def getTestAttributeValues(TestID):
	call = system.db.createSProcCall('qms.stp_getTestAttributeValues', db)
	
	call.registerInParam('TestID', system.db.INTEGER, TestID)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def getPreviousTestTable(TestID):
	call = system.db.createSProcCall('qms.stp_getPreviousTestTable', db)
	
	call.registerInParam('TestID', system.db.INTEGER, TestID)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def insertTestAttribute(TestTypeID, Name, TestAttributeDataTypeID, ProductCodeID = None, MaterialID = None, ValidStartDate = None, ValidEndDate = None, HiHiLimit = None, HiLimit = None, TargetValue = None, LoLimit = None, LoLoLimit = None):
	call = system.db.createSProcCall('qms.stp_insertTestAttribute', db)
	
	call.registerInParam('TestTypeID', system.db.INTEGER, TestTypeID)
	call.registerInParam('Name', system.db.VARCHAR, Name)
	call.registerInParam('TestAttributeDataTypeID', system.db.INTEGER, TestAttributeDataTypeID)
	call.registerInParam('ProductCodeID', system.db.INTEGER, ProductCodeID)
	call.registerInParam('MaterialID', system.db.INTEGER, MaterialID)
	call.registerInParam('ValidStartDate', system.db.TIMESTAMP, ValidStartDate)
	call.registerInParam('ValidEndDate', system.db.TIMESTAMP, ValidEndDate)
	call.registerInParam('HiHiLimit', system.db.FLOAT, HiHiLimit)
	call.registerInParam('HiLimit', system.db.FLOAT, HiLimit)
	call.registerInParam('TargetValue', system.db.FLOAT, TargetValue)
	call.registerInParam('LoLimit', system.db.FLOAT, LoLimit)
	call.registerInParam('LoLoLimit', system.db.FLOAT, LoLoLimit)
	
	try:
		system.db.execSProcCall(call)
		return True
	except Exception as e:
		return False


##@timeit
#@error_log
##@dump_args
#def insertTestAttributeValues(TestID, Values):
#	call = system.db.createSProcCall('qms.stp_insertTestAttributeValues', db)
#	
#	call.registerInParam('TestID', system.db.INTEGER, TestID)
#	call.registerInParam('Values', system.db.VARCHAR, Values)
#	
#	try:
#		system.db.execSProcCall(call)
#		return True
#	except Exception as e:
#		return False


#@timeit
@error_log
#@dump_args
def updateTestAttribute(AttributeID, Name = None, TestAttributeDataTypeID = None, ValidStartDate = None, ValidEndDate = None, HiHiLimit = None, HiLimit = None, TargetValue = None, LoLimit = None, LoLoLimit = None):
	call = system.db.createSProcCall('qms.stp_updateTestAttribute', db)
	
	call.registerInParam('AttributeID', system.db.INTEGER, AttributeID)
	call.registerInParam('Name', system.db.VARCHAR, Name)
	call.registerInParam('TestAttributeDataTypeID', system.db.INTEGER, TestAttributeDataTypeID)
	call.registerInParam('ValidStartDate', system.db.TIMESTAMP, ValidStartDate)
	call.registerInParam('ValidEndDate', system.db.TIMESTAMP, ValidEndDate)
	call.registerInParam('HiHiLimit', system.db.FLOAT, HiHiLimit)
	call.registerInParam('HiLimit', system.db.FLOAT, HiLimit)
	call.registerInParam('TargetValue', system.db.FLOAT, TargetValue)
	call.registerInParam('LoLimit', system.db.FLOAT, LoLimit)
	call.registerInParam('LoLoLimit', system.db.FLOAT, LoLoLimit)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False


#@timeit
@error_log
#@dump_args
def disableTestAttribute(AttributeID):
	call = system.db.createSProcCall('qms.stp_disableTestAttribute', db)
	
	call.registerInParam('AttributeID', system.db.INTEGER, AttributeID)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False



##############################################################################
## TEST REPORTING
##############################################################################
#@timeit
@error_log
#@dump_args
def getTestAttributeTrend(AttributeID, NumberOfSamples):
	call = system.db.createSProcCall('qms.stp_getTestAttributeTrend', db)
	
	call.registerInParam('AttributeID', system.db.INTEGER, AttributeID)
	call.registerInParam('NumberOfSamples', system.db.INTEGER, NumberOfSamples)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def getTestAttributesReport(TestTypeID, NumberOfSamples, ProductCodeID = None, MaterialID = None):
	call = system.db.createSProcCall('qms.stp_getTestAttributesReport', db)
	
	call.registerInParam('TestTypeID', system.db.INTEGER, TestTypeID)
	call.registerInParam('ProductCodeID', system.db.INTEGER, ProductCodeID)
	call.registerInParam('MaterialID', system.db.INTEGER, MaterialID)
	call.registerInParam('NumberOfSamples', system.db.INTEGER, NumberOfSamples)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def getTestAggregatesByProductCode():
	call = system.db.createSProcCall('qms.stp_getTestAggregatesByProductCode', db)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def getTopRejects(StartDate, EndDate = None, NumberOfReasonCodes = 5, ProductCodeID = None):
	call = system.db.createSProcCall('qms.stp_getTopRejects', db)
	
	call.registerInParam('StartDate', system.db.TIMESTAMP, StartDate)
	call.registerInParam('EndDate', system.db.TIMESTAMP, EndDate)
	call.registerInParam('NumberOfReasonCodes', system.db.INTEGER, NumberOfReasonCodes)
	call.registerInParam('ProductCodeID', system.db.INTEGER, ProductCodeID)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


##############################################################################
## NON-CONFORMANCE
##############################################################################
#@timeit
@error_log
#@dump_args
def getNonConformanceReports(TestID = None, SeverityID = None, ReasonID = None, ProductCodeID = None, MaterialLotID = None, StartDate = None, EndDate = None):
	call = system.db.createSProcCall('qms.stp_getNonConformanceReports', db)
	
	call.registerInParam('TestID', system.db.INTEGER, TestID)
	call.registerInParam('SeverityID', system.db.INTEGER, SeverityID)
	call.registerInParam('ReasonID', system.db.INTEGER, ReasonID)
	call.registerInParam('ProductCodeID', system.db.INTEGER, ProductCodeID)
	call.registerInParam('MaterialLotID', system.db.INTEGER, MaterialLotID)
	call.registerInParam('StartDate', system.db.TIMESTAMP, StartDate)
	call.registerInParam('EndDate', system.db.TIMESTAMP, EndDate)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def getNonConformanceReasons(SiteID):
	call = system.db.createSProcCall('qms.stp_getNonConformanceReasons', db)
	
	call.registerInParam('SiteID', system.db.INTEGER, SiteID)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def getSeverities(SiteID):
	call = system.db.createSProcCall('qms.stp_getSeverities', db)
	
	call.registerInParam('SiteID', system.db.INTEGER, SiteID)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def insertNonConformanceReport(TestID, ReasonID, SeverityID, Notes = None):
	call = system.db.createSProcCall('qms.stp_insertNonConformanceReport', db)
	
	call.registerInParam('TestID', system.db.INTEGER, TestID)
	call.registerInParam('ReasonID', system.db.INTEGER, ReasonID)
	call.registerInParam('SeverityID', system.db.INTEGER, SeverityID)
	call.registerInParam('Notes', system.db.VARCHAR, Notes)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False



##############################################################################
## TESTS -- MATERIAL LOT
##############################################################################
#@timeit
@error_log
#@dump_args
def getMaterialLotTest(TestID):
	call = system.db.createSProcCall('qms.stp_getMaterialLotTest', db)
	
	call.registerInParam('TestID', system.db.INTEGER, TestID)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def upsertMaterialLotTest( \
		TestID, MaterialLotID, TestedBy, \
		IsPass = None, Notes = None, \
		Attribute01 = None, Attribute02 = None, Attribute03 = None, Attribute04 = None, Attribute05 = None, \
		Attribute06 = None, Attribute07 = None, Attribute08 = None, Attribute09 = None):
	call = system.db.createSProcCall('qms.stp_upsertMaterialLotTest', db)
	
	call.registerInParam('TestID', system.db.INTEGER, TestID)
	call.registerInParam('MaterialLotID', system.db.INTEGER, MaterialLotID)
	call.registerInParam('TestedBy', system.db.VARCHAR, TestedBy)
	call.registerInParam('IsPass', system.db.BOOLEAN, IsPass)
	call.registerInParam('Notes', system.db.VARCHAR, Notes)
	
	call.registerInParam('Attribute01', system.db.BOOLEAN, Attribute01)
	call.registerInParam('Attribute02', system.db.FLOAT, Attribute02)
	call.registerInParam('Attribute03', system.db.INTEGER, Attribute03)
	call.registerInParam('Attribute04', system.db.BOOLEAN, Attribute04)
	call.registerInParam('Attribute05', system.db.VARCHAR, Attribute05)
	call.registerInParam('Attribute06', system.db.INTEGER, Attribute06)
	call.registerInParam('Attribute07', system.db.FLOAT, Attribute07)
	call.registerInParam('Attribute08', system.db.INTEGER, Attribute08)
	call.registerInParam('Attribute09', system.db.BOOLEAN, Attribute09)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False



##############################################################################
## TESTS -- PART
##############################################################################
#@timeit
@error_log
#@dump_args
def getPartTest(TestID):
	call = system.db.createSProcCall('qms.stp_getPartTest', db)
	
	call.registerInParam('TestID', system.db.INTEGER, TestID)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret


#@timeit
@error_log
#@dump_args
def upsertPartTest( \
		TestID, PartID, TestedBy, \
		IsPass = None, Notes = None, \
		Attribute01 = None, Attribute02 = None, Attribute03 = None, Attribute04 = None, Attribute05 = None, \
		Attribute06 = None, Attribute07 = None, Attribute08 = None, Attribute09 = None, Attribute10 = None):
	call = system.db.createSProcCall('qms.stp_upsertPartTest', db)
	
	call.registerInParam('TestID', system.db.INTEGER, TestID)
	call.registerInParam('PartID', system.db.INTEGER, PartID)
	call.registerInParam('TestedBy', system.db.VARCHAR, TestedBy)
	call.registerInParam('IsPass', system.db.BOOLEAN, IsPass)
	call.registerInParam('Notes', system.db.VARCHAR, Notes)
	
	call.registerInParam('Attribute01', system.db.INTEGER, Attribute01)
	call.registerInParam('Attribute02', system.db.INTEGER, Attribute02)
	call.registerInParam('Attribute03', system.db.FLOAT, Attribute03)
	call.registerInParam('Attribute04', system.db.FLOAT, Attribute04)
	call.registerInParam('Attribute05', system.db.FLOAT, Attribute05)
	call.registerInParam('Attribute06', system.db.BOOLEAN, Attribute06)
	call.registerInParam('Attribute07', system.db.BOOLEAN, Attribute07)
	call.registerInParam('Attribute08', system.db.BOOLEAN, Attribute08)
	call.registerInParam('Attribute09', system.db.VARCHAR, Attribute09)
	call.registerInParam('Attribute10', system.db.INTEGER, Attribute10)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False
		
#@timeit
@error_log
#@dump_args
def getScrapCount(equipmentPath, shiftStartTime):
	"""
	TODO: Function takes "elapsed time: _____"
		
	#Args:
		# SiteID (Integer) : PK for site
	#Testing:
		#StartDateTime = '2022-12-06 06:00:00' 
		#EndDateTime = '2022-12-06 14:00:00'
		#SiteID = 1
		#print(mes.oee.sp.getSiteOEE_AQP(StartDateTime, EndDateTime, SiteID))		
	"""
	
	call = system.db.createSProcCall("scrap.stp_getScrap", db)	
	call.registerInParam("equipment_path", system.db.VARCHAR, equipmentPath)
	call.registerInParam("time_recorded", system.db.DATE, shiftStartTime)
	system.db.execSProcCall(call)
	scalar = system.dataset.toPyDataSet(call.getResultSet())
	return scalar[0][0] 
	
	
	
def getScrapERP():
	call = system.db.createSProcCall('fb.stp__ERPScrapUpdate', db)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False
	
	
