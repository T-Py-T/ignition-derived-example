# Setting modal titles
errorMessage = "Error in your configuration - Code: 01"
successMessage = "Added switch succesfully!"
ipAddressError = "IP Address not valid - Code: 02"
nccError = "NCC number is not a integer - Code: 04"
databaseConnectionError = "Error connecting to the database - Code: 03"
errorModalTitle = "Error!"
errorModalName = "errorModal"
agreeModalName = "agreeModal"


def addSwitch(params):
    import re
    # Regex pattern to check for valid IP Address
    pattern = '^(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))$'
    
    # Starting logger
    logger = system.util.getLogger("addSwitchLogger")
    
    # Grabbing variables from parameter
    assetID = params.get("assetID")
    ncc = params.get("ncc")
    switch = params.get("switch")
    plc = params.get("plc")
    
    system.perspective.print(params)
    
    # Check for required fields
    if not all([assetID, ncc, switch]):
        modalParams = {"ModalName": errorModalName, "Message": errorMessage}
        logger.warn(errorMessage)
        return errorMessage

    # Check for valid IP
    if not re.search(pattern, assetID):
        modalParams = {"ModalName": errorModalName, "Message": ipAddressError}
        logger.warn(ipAddressError)
        return ipAddressError

    try:
        # Do the database operation here
        # system.db.runPrepUpdate('INSERT INTO switches (asset_id, ncc, switch, "PlcAddress") VALUES (?, ?, ?, ?)', [assetID, ncc, switch, plc], db)
        
        modalParams = {"ModalName": agreeModalName, "Message": successMessage}
        logger.info(successMessage)
        return 1
    except Exception as e:
        modalParams = {"ModalName": errorModalName, "Message": databaseConnectionError}
        logger.warn(str(e))
        return databaseConnectionError
			
def addComment(params):
	# Starting logger
	logger = system.util.getLogger("addComment")
	
	if params["Feedback"] is not None: 
		try:
			logger.info('Added Comment')
#			res = system.db.runNamedQuery("App/addComment", params)	
			return 1
		except:
			modalParams = {"ModalName": errorModalName, "Message": databaseConnectionError}
#			system.perspective.openPopup(errorModalName, "Components/Modals/Modal", params=modalParams, title=errorModalTitle)
			logger.warn(databaseConnectionError)			
			return databaseConnectionError
	
	