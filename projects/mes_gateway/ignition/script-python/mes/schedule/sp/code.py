'''
This contains all Enterptise Reporting Stored Porcedure functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()

#siteID = mes.config._scriptHeaders.siteID
#areas = mes.config._scriptHeaders.areas
#lines = mes.config._scriptHeaders.lines
#TimePeriodDict = mes.config._scriptHeaders.TimePeriodDict
#AggregateDict = mes.config._scriptHeaders.AggregateDict



# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.schedule.sp')


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

#@timeit
@error_log
#@dump_args
def getNextJob(scheduleID):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
		  pyDataset (Dataset): 'Shift', 'Run', 'Realtime'
		  tagNameDict (Dictionary): 'Area', 'Group', 'Site'
		Returns:
		  (int): 1 if passing, else -1
		Testing:
			pyDS = mes.oee.periodic.getOEE_AQP('yesterday', 'Shift', 'Area', 1)
			mes.oee.periodic.writeOEE_AQP('Shift', pyDS)
		TODO:
	"""
	call = system.db.createSProcCall("sched.stp_getNextJob", db)	
	call.registerInParam("scheduleID", system.db.INTEGER, scheduleID)
	system.db.execSProcCall(call)
	res = call.getResultSet()
	ret = system.dataset.toPyDataSet(res)
	return ret

def getAllEquipmentSchedule(params):
	call = system.db.createSProcCall("sched.stp_getAllEquipmentSchedule", db='MSSQL_MES')	
	call.registerInParam("AreaID", system.db.INTEGER, params['areaID'])
	call.registerInParam("ProductCodeID", system.db.INTEGER, params['productCodeID'])
	call.registerInParam("StartDateTime", system.db.TIMESTAMP, params['startDateTime'])
	call.registerInParam("EndDateTime", system.db.TIMESTAMP, params['endDateTime'])
	system.db.execSProcCall(call)
	res = call.getResultSet()
	ret = system.dataset.toPyDataSet(res)
	return ret

#@timeit
@error_log
#@dump_args
def runConsumeMaterials(params):
	"""Executes the stored procedure 'sched.stp_runConsumeMaterials' to consume materials
	    required for a given product code and order quantity.
	    Args:
	        params (dict): A dictionary containing the following keys:
	            'productCodeID' (int): The ID of the product code for which materials need to be consumed.
	            'orderQuantity' (int): The quantity of the product to be ordered.
	    Returns:
	        dict: A dictionary containing the result of the execution:
	            - If successful:
	                {'status': 'success', 'message': 'The execution of the stored procedure was successful', 'ds': (dataset)}
	            - If failed:
	                {'status': 'failure', 'message': 'The execution of the stored procedure failed with status (status)'}
	    Note:
	        The output parameter 'Status' from the stored procedure is captured and returned as 'status' in the result dictionary.
	        The result dataset (if successful) will be available as 'ds' in the result dictionary.	
	    Testing:
	        # Example usage:
	        params = {'productCodeID': 123, 'orderQuantity': 100}
	        result = runConsumeMaterials(params)	
	        # Check if the execution was successful
	        if result['status'] == 'success':
	            # Access the dataset containing the consumed materials information
	            dataset = result['ds']
	            # Process the dataset as needed
	            print(dataset)
	        else:
	            # Print the failure message if execution failed
	            print(result['message'])	
	    TODO:
	        None
	"""
	call = system.db.createSProcCall("sched.stp_runConsumeMaterials", db)	
	call.registerInParam("ProductCodeID", system.db.INTEGER, params.get('productCodeID'))
	call.registerInParam("OrderQuantity", system.db.INTEGER, params.get('orderQuantity'))
	call.registerOutParam('Status', system.db.VARCHAR)
	
	system.db.execSProcCall(call)
    
    # Fetch the result set before getting the output parameter
	res = call.getResultSet()
	ret = system.dataset.toPyDataSet(res)
	
    # Now get the output parameter
	status = call.getOutParamValue('Status')
	print(status)
	if status != 'Success':
	    result = {"status": "failure", "message": "The execution of the stored procedure failed with status {}".format(status)}
	else:
		result = {"status": "success", "message": "The execution of the stored procedure was successful", "ds": ret}
	
	return result

##############################################################################
## MATERIALS
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



##############################################################################
## MATERIAL LOTS
##############################################################################
#@timeit
@error_log
#@dump_args
def getMaterialLots(SiteID, MaterialID = None, MaterialLotNumber = None, GetZeroQty = False, GetDisabled = False):
	call = system.db.createSProcCall('tat.stp_getMaterialLots', db)
	
	call.registerInParam('SiteID', system.db.INTEGER, SiteID)
	call.registerInParam('MaterialID', system.db.INTEGER, MaterialID)
	call.registerInParam('MaterialLotNumber', system.db.VARCHAR, MaterialLotNumber)
	call.registerInParam('GetZeroQty', system.db.BOOLEAN, GetZeroQty)
	call.registerInParam('GetDisabled', system.db.BOOLEAN, GetDisabled)
	
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	
	return ret
	
#@timeit
@error_log
#@dump_args
def runEnd(params):
    call = system.db.createSProcCall('sched.stp_runEnd', db)
    call.registerInParam('RunID', system.db.INTEGER, params.get('runID'))
    
    try:
        system.db.execSProcCall(call)
        return True
    except:
        return False

#@timeit
@error_log
#@dump_args
def getScheduleID(workOrder, lineID):
    call = system.db.createSProcCall('sched.stp_getScheduleIDFromTag', db)
    call.registerInParam('WorkOrder', system.db.VARCHAR, workOrder)
    call.registerInParam('LineID', system.db.INTEGER, lineID)
    
    try:
        system.db.execSProcCall(call)
        resultSet = call.getResultSet()
       
        if resultSet and resultSet.rowCount > 0:
            return resultSet.getValueAt(0, 0)  
        else:
            return None 
    except:
        return False
        
#@timeit
@error_log
#@dump_args
def startRun(scheduleID):
    call = system.db.createSProcCall('sched.stp_runStart', db)
    call.registerInParam('ScheduleID', system.db.INTEGER, scheduleID)
    
    try:
        system.db.execSProcCall(call)
        return True
    except:
        return False
        
#@timeit
@error_log
#@dump_args
def fb_resequenceSchedule(params):
    call = system.db.createSProcCall('fb.stp_resequenceSchedule', db)
    call.registerInParam('ScheduleID', system.db.INTEGER, params.get('schedID'))
    call.registerInParam('LineID', system.db.INTEGER, params.get('lineID'))
    call.registerInParam('NewSeq', system.db.INTEGER, params.get('seq'))
    
    try:
        system.db.execSProcCall(call)
        return True
    except:
        return False    
        
#@timeit
@error_log
#@dump_args
def fb_woMoveDeleteTracking(params):
    call = system.db.createSProcCall('fb.stp_woMoveDeleteTracking', db)
    call.registerInParam('LineID', system.db.INTEGER, params.get('LineID'))
    call.registerInParam('WONum', system.db.VARCHAR, params.get('WONum'))
    call.registerInParam('WOAutoId', system.db.INTEGER, params.get('WOAutoId'))
    call.registerInParam('TabTo', system.db.INTEGER, params.get('TabTo'))
    call.registerInParam('TabFrom', system.db.INTEGER, params.get('TabFrom'))
    call.registerInParam('AdjSeqFrom', system.db.INTEGER, params.get('AdjSeqFrom'))
    call.registerInParam('AdjSeqTo', system.db.INTEGER, params.get('AdjSeqTo'))
    call.registerInParam('Reason', system.db.VARCHAR, params.get('Reason'))
    call.registerInParam('Reason_Type', system.db.VARCHAR, params.get('Reason_Type'))
    call.registerInParam('ComputerName', system.db.VARCHAR, params.get('ComputerName'))
    call.registerInParam('CreatedBy', system.db.VARCHAR, params.get('CreatedBy'))
    call.registerInParam('Part_Number', system.db.VARCHAR, params.get('PartNumber'))
    call.registerInParam('CreateDate', system.db.TIMESTAMP, params.get('CreateDate'))
    
    try:
        system.db.execSProcCall(call)
        return True
    except Exception as e:
        logger.error(str(e))
        return False
        
#@timeit
@error_log
#@dump_args
def fb_erpUpdate():
	call = system.db.createSProcCall('fb.stp__ERPUpdate')
	
	try:
		system.db.execSProcCall(call)
		return True
	except Exception as e:
		logger.error(str(e))
        return False
       	
#@timeit
@error_log
#@dump_args
def testFunction():
	pass
	# Write back to [MES] tag provider with equipment path
