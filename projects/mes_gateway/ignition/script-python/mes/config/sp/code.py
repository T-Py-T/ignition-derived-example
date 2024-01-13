"""
This contains all mes config functions
"""
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()






# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.config.sp')


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
def disableCurrentShift(shiftID):
	""" Adds area in DB
		TODO: None
		Args: SiteID as int, areaName as str
		Returns: None    
		Testing: (script console)
			mes.config.sp.addArea(siteID, areaName)
	"""

	call = system.db.createSProcCall('config.stp_disableCurrentShift', db)
	call.registerInParam('ShiftID', system.db.INTEGER, shiftID)
	call.registerOutParam('Status', system.db.VARCHAR)
	
	system.db.execSProcCall(call)
	status = call.getOutParamValue('Status')
	return status


#@timeit
@error_log
#@dump_args
def addArea(siteID, areaName):
	""" Adds area in DB
		TODO: None
		Args: SiteID as int, areaName as str
		Returns: None    
		Testing: (script console)
			mes.config.sp.addArea(siteID, areaName)
	"""

	call = system.db.createSProcCall('config.stp_addArea', db)
	call.registerInParam('SiteID', system.db.INTEGER, siteID)
	call.registerInParam('AreaName', system.db.VARCHAR, areaName)
	call.registerOutParam('ErrorMessage', system.db.VARCHAR)
	
	system.db.execSProcCall(call)
	status = call.getOutParamValue('ErrorMessage')
	if status == 'Success':
		return True
	else: return status

#@timeit
@error_log
#@dump_args
def addEnterprise(enterpriseName):
	""" Adds Enterprise in DB
			TODO: None
			Args: enterpriseName as str
			Returns: None    
			Testing: (script console)
				mes.config.sp.addEnterprise(enterpriseName)
		"""
	call = system.db.createSProcCall('config.stp_addEnterprise', db)
	call.registerInParam('EnterpriseName', system.db.VARCHAR, enterpriseName)
	system.db.execSProcCall(call)

#@timeit
@error_log
#@dump_args
def addCell(lineID,cellName):
	""" Adds cell in DB
		TODO: None
		Args: lineID as int, cellName as str
		Returns: None    
		Testing: (script console)
			mes.config.sp.addCell(lineID,cellName)
	"""
	#db=db
	call = system.db.createSProcCall('config.stp_addCell', db)
	call.registerInParam('LineID', system.db.INTEGER, lineID)
	call.registerInParam('CellName', system.db.VARCHAR, cellName)
	system.perspective.print(call)
	system.perspective.print(system.db.execSProcCall(call))
	
	
	
#@timeitA
@error_log
#@dump_args
def addLine(AreaID, LineName):
	""" Adds Line in DB
		TODO: None
		Args: AreaID as int, LineName as str
		Returns: None    
		Testing: (script console)
			mes.config.sp.AddLine(AreaID, LineName)
	"""
	#db=db
	call = system.db.createSProcCall('config.stp_addLine', db)
	call.registerInParam('AreaID', system.db.INTEGER, AreaID)
	call.registerInParam('LineName', system.db.VARCHAR, LineName)
	system.db.execSProcCall(call)


#@timeit
@error_log
#@dump_args
def addSite(enterpriseID, siteName):
	""" Adds Site in DB
		TODO: None
		Args: siteID as int
		Returns: None    
		Testing: (script console)
			mes.config.sp.addSite(EnterpriseID, SiteName)
	"""
	#db=db
	call = system.db.createSProcCall('config.stp_addSite', db)
	call.registerInParam('EnterpriseID', system.db.INTEGER, enterpriseID)
	call.registerInParam('SiteName', system.db.VARCHAR, siteName)
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False

#@timeit
@error_log
#@dump_args
def setEquipmentEnable(equipmentID, equipmentType, enable):
    """ 
    Sets the enable status of equipment in DB
    Args: 
        equipmentID (int): The ID of the equipment.
        equipmentType (str): The type of the equipment. Should be one of ('cell', 'line', 'area', 'enterprise', 'site').
        enable (int): The enable status. 1 for enable and 0 for disable.
    Raises:
        ValueError: If the equipmentType is not one of the valid options.
    Returns: 
        None
    Usage: 
        Call this function in the Ignition script console using the following syntax:
        mes.config.sp.setEquipmentEnable(equipmentID, equipmentType, enable)
    """
    # Check equipmentType is valid
    if equipmentType not in ('cell', 'line', 'area', 'enterprise', 'site'):
        raise ValueError("Invalid equipment type")

    call = system.db.createSProcCall('config.stp_setEnable', db)
    call.registerInParam('ID', system.db.INTEGER, equipmentID)
    call.registerInParam('Enable', system.db.BIT, enable)
    call.registerInParam('EqType', system.db.VARCHAR, equipmentType)
    system.db.execSProcCall(call)
    
#@timeit
@error_log
#@dump_args
def deleteScrapReason(params):
    """ 
        Deletes a scrap reason or reason category in the database based on the provided parameters.
        Args: 
            params (dict): The dictionary of parameters. It should include the following keys:
                id (int): The ID of the reason or reason category.
                type (str): The type of deletion operation. It can be 'reason' or 'reason_category'.
        Raises:
            ValueError: If the params do not include the necessary keys.
            Exception: If the execution of the stored procedure fails.
        Returns: 
            None: The function doesn't return a value. It performs a database operation based on the parameters.
        Usage: 
            Call this function in the Ignition script console using the following syntax:
            deleteScrapReason({
              "id": 1,
              "type": "reason"
            })
        """
    system.perspective.print(params)
    
    # Check that the necessary keys are included in the params dictionary
    required_keys = ['ID', 'type']
    for key in required_keys:
        if key not in params:
            raise ValueError("KeyError: {}. Please ensure 'params' dictionary contains correct keys.".format(key))

    if params['type'] == 'reason':
        sproc = 'config.stp_deleteScrapReason'
    elif params['type'] == 'reason_category':
        sproc = 'config.stp_deleteScrapReasonCategory'
    else:
        raise ValueError("Invalid type specified. Type must be either 'reason' or 'reason_category'.")
    
    call = system.db.createSProcCall(sproc)
    call.registerInParam('ID', system.db.INTEGER, params['ID'])
    
    # Registering an out parameter to get the status of the execution
    call.registerOutParam('Status', system.db.VARCHAR)

    system.db.execSProcCall(call)
    
    # Check the status of the execution
    status = call.getOutParamValue('Status')
    print(status)
    if status != 'success':
        result = {"status": "failure", "message": "The execution of the stored procedure failed with status {}".format(status)}
    else:
        result = {"status": "success", "message": "The execution of the stored procedure was successful"}
    
    return result
    
#@timeit
@error_log
#@dump_args
def deleteDowntimeCategory(params):
    """ 
        Deletes a downtime category in the database based on the provided parameters.
        Args: 
            params (dict): The dictionary of parameters. It should include the following keys:
                id (int): The ID of the downtime category.
        Raises:
            ValueError: If the params do not include the necessary keys.
            Exception: If the execution of the stored procedure fails.
        Returns: 
            dict: A dictionary containing the status and message of the operation.
        Usage: 
            Call this function in the Ignition script console using the following syntax:
            deleteDowntimeCategory({
              "categoryID": 1
            })
        """
    
    # Check that the necessary key is included in the params dictionary
    required_key = 'categoryID'
    if required_key not in params:
        raise ValueError("KeyError: {}. Please ensure 'params' dictionary contains correct key.".format(required_key))
    
    sproc = 'config.stp_deleteDowntimeCategory'
    
    call = system.db.createSProcCall(sproc)
    call.registerInParam('CategoryID', system.db.INTEGER, params['categoryID'])
    
    # Registering an out parameter to get the status of the execution
    call.registerOutParam('Status', system.db.VARCHAR)

    system.db.execSProcCall(call)
    
    # Check the status of the execution
    status = call.getOutParamValue('Status')
    if status != 'Success':
        result = {"status": "failure", "message": "The execution of the stored procedure failed with status {}".format(status)}
    else:
        result = {"status": "success", "message": "The execution of the stored procedure was successful"}
    
    return result

#@timeit
@error_log
#@dump_args
def addEditScrapReason(params):
    """ 
        Adds or edits a scrap reason in the database based on the provided parameters.
        Args: 
            params (dict): The dictionary of parameters. It should include the following keys:
                id (int): The ID of the reason. If 0 or not given, a new reason will be added.
                reason_name (str): The name of the reason.
                reason_description (str): The description of the reason.
                time_retired (datetime): The retirement time of the reason.
                reason_category_id (int): The ID of the reason category.
                reason_code (int): The code of the reason.
        Raises:
            ValueError: If the params do not include the necessary keys.
            Exception: If the execution of the stored procedure fails.
        Returns: 
            None: The function doesn't return a value. It performs database operations based on the parameters.
        Usage: 
            Call this function in the Ignition script console using the following syntax:
            addEditScrapReason({
              "id": 1,
              "time_retired": datetime.datetime.now(),
              "reason_name": "New/Changed",
              "reason_description": "This is a new/changed reason",
              "reason_category_id": 1,
              "reason_code": 44
            })
        """
    
    # Check that the necessary keys are included in the params dictionary
    required_keys = ['id', 'time_retired', 'reason_name', 'reason_description', 'reason_category_id', 'reason_code']
    for key in required_keys:
        if key not in params:
            raise ValueError("KeyError: {}. Please ensure 'params' dictionary contains correct keys.".format(key))
   
    call = system.db.createSProcCall('config.stp_addEditScrapReason', db)
    call.registerInParam('ReasonID', system.db.INTEGER, params['id'])
    call.registerInParam('TimeRetired', system.db.TIMESTAMP, params['time_retired'])
    call.registerInParam('ReasonName', system.db.VARCHAR, params['reason_name'])
    call.registerInParam('ReasonDescription', system.db.VARCHAR, params['reason_description'])
    call.registerInParam('ReasonCategoryID', system.db.INTEGER, params['reason_category_id'])
    call.registerInParam('ReasonCode', system.db.INTEGER, params['reason_code'])
    
    # Registering an out parameter to get the status of the execution
    call.registerOutParam('status', system.db.VARCHAR)

    system.db.execSProcCall(call)
    
    # Check the status of the execution
    status = call.getOutParamValue('status')
    print status
    if status != 'success':
        result = {"status": "failure", "message": "The execution of the stored procedure failed with status {}".format(status)}
        
    else:
        result = {"status": "success", "message": "The execution of the stored procedure was successful"}
    
    return result
    
#@timeit
@error_log
#@dump_args    
def addEditStateTypes(params):
    """ 
        Adds or edits a state type in the database based on the provided parameters.
        Args: 
            params (dict): The dictionary of parameters. It should include the following keys:
                id (int): The ID of the state type. If 0 or not given, a new state type will be added.
                state_type_name (str): The name of the state type.
        Raises:
            ValueError: If the params do not include the necessary keys.
            Exception: If the execution of the stored procedure fails.
        Returns: 
            dict: A dictionary containing the status and message of the operation.
        Usage: 
            Call this function in the Ignition script console using the following syntax:
            addEditStateTypes({
              "stateID": 1,
              "stateTypeName": "New State Type"
            })
    """

    # Check that the necessary keys are included in the params dictionary
    required_keys = ['stateID', 'stateTypeName']
    for key in required_keys:
        if key not in params:
            raise ValueError("KeyError: {}. Please ensure 'params' dictionary contains correct keys.".format(key))

    call = system.db.createSProcCall('config.stp_addEditStateTypes')
    call.registerInParam('StateTypeID', system.db.INTEGER, params['stateID'])
    call.registerInParam('StateTypeName', system.db.VARCHAR, params['stateTypeName'])

    # Registering an out parameter to get the status of the execution
    call.registerOutParam('Status', system.db.VARCHAR)

    system.db.execSProcCall(call)
    
    # Check the status of the execution
    status = call.getOutParamValue('Status')
    print(status)
    if status != 'Success':
        result = {"status": "failure", "message": "The execution of the stored procedure failed with status {}".format(status)}
    else:
        result = {"status": "success", "message": "The execution of the stored procedure was successful"}
    
    return result
    
#@timeit
@error_log
#@dump_args
def addEditScrapReasonCategory(params):
    """ 
        Adds or edits a scrap reason category in the database based on the provided parameters.
        Args: 
            params (dict): The dictionary of parameters. It should include the following keys:
                id (int): The ID of the category. If 0 or not given, a new category will be added.
                reason_category_name (str): The name of the reason category.
                reason_category_description (str): The description of the reason category.
                time_retired (datetime): The retirement time of the reason category.
        Raises:
            ValueError: If the params do not include the necessary keys.
            Exception: If the execution of the stored procedure fails.
        Returns: 
            None: The function doesn't return a value. It performs database operations based on the parameters.
        Usage: 
            Call this function in the Ignition script console using the following syntax:
            addEditScrapReasonCategory({
              "id": 1,
              "time_retired": datetime.datetime.now(),
              "reason_category_name": "New/Changed",
              "reason_category_description": "This is a new/changed reason category"
            })
        """
    
    # Check that the necessary keys are included in the params dictionary
    required_keys = ['id', 'time_retired', 'reason_category_name', 'reason_category_description']
    for key in required_keys:
        if key not in params:
            raise ValueError("KeyError: {}. Please ensure 'params' dictionary contains correct keys.".format(key))

    call = system.db.createSProcCall('config.stp_addEditScrapReasonCategory', db)
    call.registerInParam('CategoryID', system.db.INTEGER, params['id'])
    call.registerInParam('TimeRetired', system.db.TIMESTAMP, params['time_retired'])
    call.registerInParam('ReasonCategoryName', system.db.VARCHAR, params['reason_category_name'])
    call.registerInParam('ReasonCategoryDescription', system.db.VARCHAR, params['reason_category_description'])

    # Registering an out parameter to get the status of the execution
    call.registerOutParam('Status', system.db.VARCHAR)

    system.db.execSProcCall(call)
    
    # Check the status of the execution
    status = call.getOutParamValue('Status')
    print status
    if status != 'success':
        result = {"status": "failure", "message": "The execution of the stored procedure failed with status {}".format(status)}
        
    else:
        result = {"status": "success", "message": "The execution of the stored procedure was successful"}
    
    return result

#@timeit
@error_log
#@dump_args
def addEditDowntimeCategory(params):
    """
        Adds or edits a downtime category in the database based on the provided parameters.
        Args:
            params (dict): The dictionary of parameters. It should include the following keys:
                category_id (int): The ID of the category. If 0 or not given, a new category will be added.
                category_name (str): The name of the category.
        Raises:
            ValueError: If the params do not include the necessary keys.
            Exception: If the execution of the stored procedure fails.
        Returns:
            dict: A dictionary containing the status and a message indicating the result of the execution.
        Usage:
            Call this function in the Ignition script console using the following syntax:
            addEditDowntimeCategory({
              "categoryID": 1,
              "categoryName": "New/Changed Category"
            })
    """

    # Check that the necessary keys are included in the params dictionary
    required_keys = ['categoryID', 'categoryName']
    for key in required_keys:
        if key not in params:
            raise ValueError("KeyError: {}. Please ensure 'params' dictionary contains correct keys.".format(key))

    call = system.db.createSProcCall('config.stp_addEditDowntimeCategory', db)
    call.registerInParam('CategoryID', system.db.INTEGER, params['categoryID'])
    call.registerInParam('CategoryName', system.db.VARCHAR, params['categoryName'])

    # Registering an out parameter to get the status of the execution
    call.registerOutParam('Status', system.db.VARCHAR)

    system.db.execSProcCall(call)

    # Check the status of the execution
    status = call.getOutParamValue('Status')
    if status != 'Success':
        result = {"status": "failure", "message": "The execution of the stored procedure failed with status: {}".format(status)}
    else:
        result = {"status": "success", "message": "The execution of the stored procedure was successful"}

    return result

#@timeit
@error_log
#@dump_args
def deleteAsset(params):
    """ 
        Deletes an asset from the database based on the provided parameters.
        Args: 
            params (dict): The dictionary of parameters. It should include the following keys:
                ID (int): The ID of the asset.
                EqType (str): The type of the asset ('enterprise', 'site', 'area', 'line', or 'cell').
        Raises:
            ValueError: If the params do not include the necessary keys.
            Exception: If the execution of the stored procedure fails.
        Returns: 
            None: The function doesn't return a value. It performs database operations based on the parameters.
        Usage: 
            Call this function in the Ignition script console using the following syntax:
            deleteAsset({
              "ID": 1,
              "EqType": "site"
            })
        """
    
    # Check that the necessary keys are included in the params dictionary
    required_keys = ['ID', 'EqType']
    for key in required_keys:
        if key not in params:
            raise ValueError("KeyError: {}. Please ensure 'params' dictionary contains correct keys.".format(key))

    call = system.db.createSProcCall('config.stp_deleteAsset', db)
    call.registerInParam('ID', system.db.INTEGER, params['ID'])
    call.registerInParam('Type', system.db.VARCHAR, params['EqType'])

    # Registering an out parameter to get the status of the execution
    call.registerOutParam('Status', system.db.VARCHAR)

    system.db.execSProcCall(call)
    
    # Check the status of the execution
    status = call.getOutParamValue('Status')
    print status
    if status != 'success':
        result = {"status": "failure", "message": "The execution of the stored procedure failed with status {}".format(status)}
        
    else:
        result = {"status": "success", "message": "The execution of the stored procedure was successful"}
    
    return result
    
#@timeit
@error_log
#@dump_args
def addEditLineShift(params):
	""" 
	    Deletes an asset from the database based on the provided parameters.
	    Args: 
	        params (dict): The dictionary of parameters. It should include the following keys:
	            ID (int): The ID of the asset.
	            EqType (str): The type of the asset ('enterprise', 'site', 'area', 'line', or 'cell').
	    Raises:
	        ValueError: If the params do not include the necessary keys.
	        Exception: If the execution of the stored procedure fails.
	    Returns: 
	        None: The function doesn't return a value. It performs database operations based on the parameters.
	    Usage: 
	        Call this function in the Ignition script console using the following syntax:
	        deleteAsset({
	          "ID": 1,
	          "EqType": "site"
	        })
	    """
	logger.info('fn params: ' + str(params))
	call = system.db.createSProcCall('config.stp_upsertLineShifts', db)
	call.registerInParam('ShiftID', system.db.INTEGER, params['ShiftID'])
	call.registerInParam('SiteID', system.db.INTEGER, params['SiteID'])
	call.registerInParam('LineID', system.db.INTEGER, params['LineID'])
	call.registerInParam('ShiftName', system.db.VARCHAR, params['ShiftName'])
	call.registerInParam('ShiftNumber', system.db.INTEGER, params['ShiftNumber'])
	call.registerInParam('StartTime', system.db.VARCHAR, params['StartTime'])
	call.registerInParam('ShiftLength', system.db.INTEGER, params['ShiftLength'])
	call.registerInParam('DayModifier', system.db.INTEGER, params['DayModifier'])
	call.registerInParam('ScheduleStart', system.db.TIMESTAMP, params['StartDate'])
	call.registerInParam('ScheduleEnd', system.db.TIMESTAMP, params['EndDate'])
	
	call.registerOutParam('Status', system.db.VARCHAR)
	
	system.db.execSProcCall(call)
	
	# Check the status of the execution
	status = call.getOutParamValue('Status')
	
	if status != 'success':
	    result = {"status": "failure", "message": "The execution of the stored procedure failed with status {}".format(status)}
	    
	else:
	    result = {"status": "success", "message": "The execution of the stored procedure was successful"}
	
	return result
	

	
    
##@timeit
#@error_log
##@dump_args
#def addEditDowntimeReason(params):
#    """ 
#        Adds or edits a mode in the database based on the provided parameters.
#        Args: 
#            params (dict): The dictionary of parameters. It should include the following keys:
#                id (int): The ID of the mode. If 0 or not given, a new mode will be added.
#                ReasonCode (int): The reason code of the mode.
#                IconPath (str): The icon path of the mode.
#                DisplayColor (str): The display color of the mode.
#                Description (str): The description of the mode.
#                AltCode (int): The alternate code of the mode.
#        Raises:
#            ValueError: If the params do not include the necessary keys.
#            Exception: If the execution of the stored procedure fails.
#        Returns: 
#            None: The function doesn't return a value. It performs database operations based on the parameters.
#        Usage: 
#            Call this function in the Ignition script console using the following syntax:
#            addEditMode({
#              "id": 1,
#              "ReasonCode": 101,
#              "IconPath": "/path/to/icon",
#              "DisplayColor": "#FFFFFF",
#              "Description": "This is a description",
#              "AltCode": 202
#            })
#        """
#    
#    # Check that the necessary keys are included in the params dictionary
#    required_keys = ['id', 'ReasonCode', 'IconPath', 'DisplayColor', 'Description', 'AltCode']
#    for key in required_keys:
#        if key not in params:
#            raise ValueError("KeyError: {}. Please ensure 'params' dictionary contains correct keys.".format(key))
#
#    call = system.db.createSProcCall('dbo.stp_addEditDowntimeReason', db)
#    call.registerInParam('ID', system.db.INTEGER, params['id'])
#    call.registerInParam('ReasonCode', system.db.INTEGER, params['ReasonCode'])
#    call.registerInParam('IconPath', system.db.VARCHAR, params['IconPath'])
#    call.registerInParam('DisplayColor', system.db.VARCHAR, params['DisplayColor'])
#    call.registerInParam('Description', system.db.VARCHAR, params['Description'])
#    call.registerInParam('AltCode', system.db.INTEGER, params['AltCode'])
#
#    # Registering an out parameter to get the status of the execution
#    call.registerOutParam('Status', system.db.VARCHAR)
#
#    system.db.execSProcCall(call)
#    
#    # Check the status of the execution
#    status = call.getOutParamValue('Status')
#    print status
#    if status != 'success':
#        raise Exception("The execution of the stored procedure failed with status {}".format(status))
#    else: return True
    

#
##@timeit
#@error_log
##@dump_args
#def disableArea(areaID):
#	""" Disables cell in DB
#		TODO: None
#		Args: areaID as int
#		Returns: None    
#		Testing: (script console)
#			mes.config.sp.disableCell(areaID)
#	"""
#	#db=db
#	call = system.db.createSProcCall('config.stp_disableArea', db)
#	call.registerInParam('ID', system.db.INTEGER, areaID)
#	system.db.execSProcCall(call)
#
##@timeit
#@error_log
##@dump_args
#def disableEnterprise(enterpriseID):
#	""" Disables enterprise in DB
#		TODO: None
#		Args: enterpriseID as int
#		Returns: None    
#		Testing: (script console)
#			mes.config.sp.disableEnterprise(enterpriseID)
#	"""
#	
#	call = system.db.createSProcCall('config.stp_disableEnterprise', db)
#	call.registerInParam('ID', system.db.INTEGER, enterpriseID)
#	system.db.execSProcCall(call)
#
##@timeit
#@error_log
##@dump_args
#def disableCell(cellID):
#	""" Disables cell in DB
#		TODO: None
#		Args: cellID as int
#		Returns: None    
#		Testing: (script console)
#			mes.config.sp.disableCell(cellID)
#	"""
#	#db=db
#	call = system.db.createSProcCall('config.stp_disableCell', db)
#	call.registerInParam('ID', system.db.INTEGER, cellID)
#	system.db.execSProcCall(call)
#	
#	
#	
##@timeit
#@error_log
##@dump_args
#def disableLine(LineID):
#	""" Disables cell in DB
#		TODO: None
#		Args: lineID as int
#		Returns: None    
#		Testing: (script console)
#			mes.config.sp.disableLine(LineID)
#	"""
#	#db=db
#	call = system.db.createSProcCall('config.stp_disableLine', db)
#	call.registerInParam('ID', system.db.INTEGER, LineID)
#	system.db.execSProcCall(call)
#
#
##@timeit
#@error_log
##@dump_args
#def disableSite(SiteID):
#	""" Disables cell in DB
#		TODO: None
#		Args: siteID as int
#		Returns: None    
#		Testing: (script console)
#			mes.config.sp.disableSite(SiteID)
#	"""
#	#db=db
#	call = system.db.createSProcCall('config.stp_disableSite', db)
#	call.registerInParam('ID', system.db.INTEGER, SiteID)
#	system.db.execSProcCall(call)


#@timeit
@error_log
#@dump_args
def getAllCells(GetDisabledCells = 0):
	""" gets machine cellID needed for state history insert
		TODO: None
		Args: None
		Returns:Dataset    
		Testing: (script console)
			mes.config.sp.getAllCells()
	"""
	call = system.db.createSProcCall('ui.stp_getAllCells', db)
	call.registerInParam('GetDisabledCells', system.db.BOOLEAN, GetDisabledCells)
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	return ret
	


#@timeit
@error_log
#@dump_args
def getProductCodes():
	""" gets machine cellID needed for state history insert
		TODO: None
		Args: None
		Returns:Dataset    
		Testing: (script console)
			mes.config.sp.getProductCodes()
	"""
	call = system.db.createSProcCall('ui.stp_getAllProductCodesDropdown', db)
	# call.registerInParam('SiteID', system.db.BOOLEAN, SiteID)
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	return ret


#@timeit
@error_log
#@dump_args
def getCellID(line, cellName, db=db):
	"""
	Gets machine cellID needed for state history insert.
	TODO: None
	Args:
		line (string): The production line.
		cellName (string): The name of the cell.
	Returns:
		The cell ID if found, otherwise returns None.
	Testing: (script console)
		now = system.date.format(system.date.now(), "yyyy-MM-dd HH:mm:ss")
		mes.config.getCellID('Line9','Stacker')
	"""
	call = system.db.createSProcCall("tag.stp_getCellID", db)
	call.registerInParam("line", system.db.VARCHAR, line)
	call.registerInParam("cell", system.db.VARCHAR, cellName)
	system.db.execSProcCall(call)
	scalar = system.dataset.toPyDataSet(call.getResultSet())

	if scalar and len(scalar) > 0:
		return scalar[0][0]  # get value at row 0 column 0
	else:
		return -1


#@timeit
@error_log
#@dump_args
def getCellOrder(line, cellName, db=db):
	""" gets machine cellID needed for state history insert
		TODO: None
		Args:	#data fields from tag used for SPROC
			line (string):
			cellName (string):
	Returns:None      
	Testing: (script console)
		now = system.date.format(system.date.now(), "yyyy-MM-dd HH:mm:ss")
		mes.events.getCellID('Line9','Stacker')
	"""
	call = system.db.createSProcCall("tag.stp_getCellOrder", db)
	call.registerInParam("line", system.db.VARCHAR, line)
	call.registerInParam("cell", system.db.VARCHAR, cellName)
	system.db.execSProcCall(call)
	scalar = system.dataset.toPyDataSet(call.getResultSet())
	
	if scalar and len(scalar) > 0:
		return scalar[0][0]  # get value at row 0 column 0
	else:
		return -1


#@timeit
@error_log
#@dump_args
def getGroupName(line, db=db):
	""" gets groupName for a gievn line
		TODO: None
		Args:	#data fields from tag used for SPROC
			line (string):
	Returns:None      
	Testing: (script console)
		mes.events.getGroupName('Line9')
	"""
	call = system.db.createSProcCall("tag.stp_getGroup", db)
	call.registerInParam("line", system.db.VARCHAR, line)
	system.db.execSProcCall(call)
	scalar = system.dataset.toPyDataSet(call.getResultSet())
	
	if scalar and len(scalar) > 0:
		return scalar[0][0]  # get value at row 0 column 0
	else:
		return -1



#@timeit
@error_log
#@dump_args
def getLineConfig(line, db=db):
	""" TODO: None
		Args:line (string):
		Returns:None      
		Testing: mes.config.getLineConfig('SFN1')
	"""
	call = system.db.createSProcCall("tag.stp_getLineConfig", db)
	call.registerInParam("line", system.db.VARCHAR, line)
	system.db.execSProcCall(call)
	return call.getResultSet()


#@timeit
@error_log
#@dump_args
def getLineCellConfig(line, db=db):
	""" gets line tagID needed for count history insert
		TODO: None
		Args:	#data fields from tag used for SPROC
			line (string):
	Returns:None      
	Testing: (script console)
		mes.config.getLineCellConfig('Line9')
	"""
	call = system.db.createSProcCall("tag.stp_getLineCellConfig", db)	
	call.registerInParam("line", system.db.VARCHAR, line)
	system.db.execSProcCall(call)
	return call.getResultSet()


#@timeit
@error_log
#@dump_args
def getLineID(line, db=db):
	""" gets line tagID needed for count history insert
		TODO: None
		Args:	#data fields from tag used for SPROC
			line (string):
	Returns:None      
	Testing: (script console)
		print(mes.config.getLineID("SFN1"))
	"""
	call = system.db.createSProcCall("tag.stp_getLineID", db)		
	call.registerInParam("line", system.db.VARCHAR, line)
	system.db.execSProcCall(call)
	scalar = system.dataset.toPyDataSet(call.getResultSet())
	
	if scalar and len(scalar) > 0:
		return scalar[0][0]  # get value at row 0 column 0
	else:
		return -1

#@timeit
@error_log
#@dump_args
def getShiftTimes(timePeriod, db=db):
	""" gets StartDate,EndDate for time period
		TODO: None
		Args:	#data fields from tag used for SPROC
			line (string):
	Returns:None      
	Testing: (script console)
		print(mes.config.getLineID("current shift"))
	"""
	'SELECT @timeStart = StartTime, @timeEnd = EndTime FROM GetTimeRange(@timePeriod, NULL);'
	system.db.runPrepQuery(query, args, tx)
	call = system.db.createSProcCall("dbo.GetTimeRange", db)		
	call.registerInParam("timePeriod", system.db.VARCHAR, timePeriod)
	system.db.execSProcCall(call)
	scalar = system.dataset.toPyDataSet(call.getResultSet())
	
	if scalar and len(scalar) > 0:
		return scalar[0][0]  # get value at row 0 column 0
	else:
		return -1

#@timeit
@error_log
#@dump_args
def addEditLineState(params, db=db):
	#raise params
	system.perspective.print(params)
	call = system.db.createSProcCall("config.stp_addEditLineState", db)
	system.perspective.print("Sproc Call Created")
	call.registerInParam("StateID", system.db.INTEGER, params['StateID'])
	call.registerInParam("LineID", system.db.INTEGER, params['LineID'])
	call.registerInParam("ReasonCode", system.db.INTEGER, params['ReasonCode'])
	call.registerInParam("IconPath", system.db.VARCHAR, params['IconPath'])
	call.registerInParam("DisplayColor", system.db.VARCHAR, params['DisplayColor'])
	call.registerInParam("Description", system.db.VARCHAR, params['Description'])
	call.registerInParam("AltCode", system.db.VARCHAR, params['AltCode'])
	call.registerInParam("RecordDowntime", system.db.BIT, params['RecordDowntime'])
	call.registerInParam("PlannedDowntime", system.db.BIT, params['PlannedDowntime'])
	call.registerInParam("OperatorSelectable", system.db.BIT, params['OperatorSelectable'])
	call.registerInParam("SubReasonOf", system.db.INTEGER, params['SubReasonOf'])
	call.registerInParam("StateTypeID", system.db.INTEGER, params['StateTypeID'])
	call.registerInParam("DowntimeCategoryCode", system.db.INTEGER, params['DowntimeCategoryCode'])
	system.perspective.print(call)
	try:
	    system.db.execSProcCall(call)
	    system.perspective.print("Sproc Call Executed")
	    return True
	except Exception as e:
	    msg = 'There was an error: ' + str(e)
	    system.perspective.print(msg)
	    return msg
	    
#@timeit
@error_log
#@dump_args
def addEditMode(params, db=db):
	
	call = system.db.createSProcCall("config.stp_addEditMode", db)
	call.registerInParam("ModeID", system.db.INTEGER, params['ModeID'])
	call.registerInParam("ReasonCode", system.db.INTEGER, params['ReasonCode'])
	call.registerInParam("IconPath", system.db.VARCHAR, params['IconPath'])
	call.registerInParam("DisplayColor", system.db.VARCHAR, params['DisplayColor'])
	call.registerInParam("Description", system.db.VARCHAR, params['Description'])
	call.registerInParam("AltCode", system.db.VARCHAR, params['AltCode'])
	
	try:
	    system.db.execSProcCall(call)
	    return True
	except Exception as e:
	    msg = 'There was an error: ' + str(e)
	    return msg

#@timeit
@error_log
#@dump_args
def editAreaConfig(params, db=db):

	call = system.db.createSProcCall("config.stp_editAreaConfig", db)
	call.registerInParam("AreaID", system.db.INTEGER, params['AreaID'])
	call.registerInParam("SiteID", system.db.INTEGER, params['SiteID'])
	call.registerInParam("EquipmentPath", system.db.VARCHAR, params['EquipmentPath'])
	call.registerInParam("EquipmentConfigRate", system.db.FLOAT, params['EquipmentConfigRate'])
	call.registerInParam("EquipmentTargetRate", system.db.FLOAT, params['EquipmentTargetRate'])
    
	try:
		system.db.execSProcCall(call)
		return True
	except Exception as e:
		msg = 'There was an error: ' + str(e)
	return msg

#@timeit
@error_log
#@dump_args
def editCellConfig(params, db=db):

    call = system.db.createSProcCall("config.stp_editCellConfig", db)   
    call.registerInParam("CellID", system.db.INTEGER, params['CellID'])
    call.registerInParam("Name", system.db.VARCHAR, params['Name'])
    call.registerInParam("IsEnabled", system.db.BIT, params['IsEnabled'])
    call.registerInParam("LineID", system.db.INTEGER, params['LineID'])
    call.registerInParam("CellOrder", system.db.INTEGER, params['CellOrder'])
    call.registerInParam("KeyCell", system.db.BIT, params['KeyCell'])
    
    try:
        system.db.execSProcCall(call)
        return True
    except Exception as e:
        msg = 'There was an error: ' + str(e)
        return msg

#@timeit
@error_log
#@dump_args
def editLineConfig(params, db=db):
	
	call = system.db.createSProcCall("config.stp_editLineConfig", db)   
	call.registerInParam("LineID", system.db.INTEGER, params['LineID'])
	#call.registerInParam("IsEnabled", system.db.BIT, params['IsEnabled'])
	call.registerInParam("EquipmentPath", system.db.VARCHAR, params['EquipmentPath'])
	call.registerInParam("EquipmentSchedule", system.db.VARCHAR, params['EquipmentSchedule'])
	call.registerInParam("EquipmentHasInfeed", system.db.BIT, params['EquipmentHasInfeed'])
	call.registerInParam("EquipmentHasOutfeed", system.db.BIT, params['EquipmentHasOutfeed'])
	call.registerInParam("EquipmentHasReject", system.db.BIT, params['EquipmentHasReject'])
	call.registerInParam("EquipmentHasCells", system.db.BIT, params['EquipmentHasCells'])
	call.registerInParam("EquipmentLotHandlingMode", system.db.VARCHAR, params['EquipmentLotHandlingMode'])
	call.registerInParam("EquipmentZeroLotThreshold", system.db.FLOAT, params['EquipmentZeroLotThreshold'])
	call.registerInParam("EquipmentZeroLotThresholdMethod", system.db.VARCHAR, params['EquipmentZeroLotThresholdMethod'])
	call.registerInParam("EquipmentCellOrder", system.db.INTEGER, params['EquipmentCellOrder'])
	call.registerInParam("MicroDuration", system.db.INTEGER, params['MicroDuration'])
	call.registerInParam("EquipmentMinCellsRunningThreshold", system.db.INTEGER, params['EquipmentMinCellsRunningThreshold'])
	call.registerInParam("EquipmentDowntimeDetectiontType", system.db.INTEGER, params['EquipmentDowntimeDetectiontType'])
	call.registerInParam("EquipmentActiveType", system.db.VARCHAR, params['EquipmentActiveType'])
	call.registerInParam("EquipmentConfigRate", system.db.FLOAT, params['EquipmentConfigRate'])
	call.registerInParam("EquipmentTargetRate", system.db.FLOAT, params['EquipmentTargetRate'])
	
	try:
	    system.db.execSProcCall(call)
	    return True
	except Exception as e:
	    msg = 'There was an error: ' + str(e)
	    return msg
	    
	    
#@timeit
@error_log
#@dump_args
def getThresholds():
	""" gets machine cellID needed for state history insert
		TODO: None
		Args: None
		Returns:Dataset    
		Testing: (script console)
			mes.config.sp.getAllCells()
	"""
	call = system.db.createSProcCall('config.stp_getAllThresholds', db)
	system.db.execSProcCall(call)
	ret = call.getResultSet()
	return ret
#@timeit
@error_log
#@dump_args
def getLineStatesDS(LineID):
    """ gets machine cellID needed for state history insert
        TODO: None
        Args: None
        Returns:Dataset    
        Testing: (script console)
            mes.config.sp.getAllCells()
    """
    call = system.db.createSProcCall('config.stp_getLineStatesDS', db)
    call.registerInParam('LineID', system.db.INTEGER, LineID)
    system.db.execSProcCall(call)
    ret = call.getResultSet()
    return ret
