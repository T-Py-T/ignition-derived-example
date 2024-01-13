'''
This contains all WorkOrder tag calls
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()

# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.workorder.tag')

#@timeit
@error_log
#@dump_args
def fb_changeWO(params):
	"""
	    Handles the process of updating the Work Order (WO) in an ERP system and managing the corresponding job runs.
	    Parameters:
	    params (dict): A dictionary containing key information required for processing the Work Order. Expected keys are:
	        - 'tagPath' (str): The path to the tag containing job and configuration information.
	        - 'currentValue' (object): An object representing the current value, typically containing a 'value' attribute that holds the new Work Order name.
	
	    Output:
	    The function does not return any value but performs operations that involve reading and writing to system tags,
	    updating job runs, and logging the process. In case of an error, it raises an exception and logs the error message.
    """
	tagPath = '/'.join(params.get('tagPath').split('/')[:-2])
	try:
		erpUpdate = mes.schedule.sp.fb_erpUpdate()
		if not erpUpdate: logger.error('Failed to update ERP Schedule')
		
		runID = system.tag.read(tagPath + '/jobs/currentJob/runID').value
		woName = params.get('currentValue').value
		lineID = system.tag.read(tagPath + '/config/LineID').value
		jobParams = { 'runID': runID, 'woName': woName, 'lineID': lineID }

		mes.schedule.jobs.endJobFromTag(tagPath, jobParams)
		logger.info('Run ended.')
		res = mes.schedule.jobs.setNextRunFromTag(tagPath, jobParams)
		if res: logger.info('Run started successfully.')
		else: raise Exception('No Run ID found.')
	except Exception as e:
		logger.error('There was an error ending the run: ' + str(e))
	else:
		logger.info('The operation is successfully completed')
		
	logger.info('Finished switching schedule.')