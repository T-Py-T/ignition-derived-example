'''
This contains all OEE calculation functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders
import os

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.schedule.jobs')

STR_Jobs					= "jobs"
STR_CURRENT_JOB 			= "currentJob"
STR_PREVIOUS_JOB 			= "previousJob"
STR_NEXT_JOB 				= "nextJob"

MODE_DISABLED				= 0
MODE_PRODUCTION				= 1
MODE_CHANGEOVER				= 2
MODE_IDLE					= 3
MODE_MAINTENANCE			= 4
MODE_OTHER					= 5
MODE_MAINTENANCE_CALLED		= 10
MODE_MAINTENANCE_IN_PROGRESS= 11
MODE_MAINTENANCE_LEFT		= 12
MODE_QUALITY_CALLED			= 20
MODE_QUALITY_IN_PROGRESS    = 21
MODE_QUALITY_LEFT			= 22
MODE_TEAM_LEAD_CALLED		= 30
MODE_TEAM_LEAD_IN_PROGRESS  = 31
MODE_TEAM_LEAD_LEFT			= 32



NAME_OPERATIONS_RESPONSE 	= "OperationsResponse"
NAME_OPERATIONS_REQUEST 	= "OperationsRequest"
NAME_RESPONSE_SEGMENT	 	= "ResponseSeqment"
NAME_REQUEST_SEGMENT	 	= "RequestSegment"


#### REFERENCE DICT ########
# TagName Mapping {DBColumnName : TagName}
#OEETagDict={'Start':'DateTimeStart', 
#	'End':'DateTimeEnd', 'Infeed':'Infeed','Reject':'Reject', 
#	'Total':'Outfeed','PlannedMins':'PlannedMinutes','Downtime':'Downtime',
#	'Runtime':'Runtime','A':'Availability','Q':'Quality','P':'Performance', 
#	'Scrap':'Scrap','OEE':'OEE','TEEP':'TEEP'} #'MTBS':'MTBS','MTBF':'MTBF','MTTR':'MTTR'}

# TagName Mapping {DBColumnName : TagName}
JobTagDict ={
		'costCenter':'costCenter',
		'costPerUnit': 'costPerUnit',
		'inputMaterial': 'inputMaterial',
		'manualChecks': 'manualChecks',
		'materialCost': 'materialCost',
		'minutesRemaining': 'minutesRemaining',
		'opRespUuid': 'opRespUuid',
		'opScheduleUuid': 'opScheduleUuid',
		'partCountMultiplier': 'partCountMultiplier',
		'platform': 'platform',
		'priceUnit': 'priceUnit',
		'printerLabels': 'printerLabels',
		'productCode': 'productCode',
		'productCodeID': 'productCodeID',
		'recipeId': 'recipeId',
		'respSegUuid': 'respSegUuid',
		'runId': 'runId',
		'runStartTime': 'runStartTime',
		'SAPEarnedHoursRate': 'SAPEarnedHoursRate',
		'scheduleRate': 'scheduleRate',
		'setupComplete': 'setupComplete',
		'standardRate': 'standardRate',
		'targetChangeoverTime': 'targetChangeoverTime',
		'targetQuantity': 'targetQuantity',
		'tool': 'tool',
		'tooling': 'tooling',
		'workOrder': 'workOrder',
		'workorderProgress': 'workorderProgress',
		'workOrderQuantity': 'workOrderQuantity',
		'scheduleProgress': 'scheduleProgress',
		'scheduleQuantity': 'scheduleQuantity'		
}

#@timeit
#@error_log
#@dump_args
#def testFunction():
#	pass
	# Write back to [MES] tag provider with equipment path


# TTURNER COMMENTS

# comments!!A

#@timeit
@error_log
#@dump_args
def callGetJobData(scheduleID):
	""" Calls the sp getNextJob
		Args:
		  scheduleID (int)
		Returns:
		  (pyDataset): dataset
		Testing:
			mes.schedule.jobs.callGetJobData(2)
		TODO:
	"""
	try:
		return mes.schedule.sp.getNextJob(scheduleID)
	except Exception as e:
		raise e

def updateJob(scheduleID, eqPath, job):
    """ Calls the callNextJob function and the writeNextJob function
        Args:
          pyDataset (Dataset): 
          eqPath (String): 'Enterprise/Site/Area/Line'
          Returns:
          (int): 1 if passing, else -1
        Testing:
            pyDS = mes.oee.periodic.getOEE_AQP('yesterday', 'Shift', 'Area', 1)
            mes.oee.periodic.writeOEE_AQP('Shift', pyDS)
        TODO:
    """
    try:
        jobTypes = ['nextJob', 'previousJob', 'currentJob']

        if job not in jobTypes: raise ValueError("Invalid job type. Must be 'nextJob', 'previousJob', or 'currentJob'.")

        jobPath = getJobPath(eqPath, job)
#        clearJob(jobPath)
        jobData = callGetJobData(scheduleID)
        writeJob(jobData, jobPath)
        return 1

    except Exception as e:
        raise e
			

# calls the GPAcallGetNextJob
# calls GPAwriteNextJob
 
	
#@timeit
@error_log
#@dump_args
def writeJob(pyDataset, eqPath):
	# setup global variables
	writeTagPaths, writeTagValues = [], []
		
	columns = pyDataset.getColumnNames()
	for row in pyDataset: #X	#3 Parse through pyDS and get each row (line)
		for key in JobTagDict.keys():
			if key in columns: #if we match a known TagName get name and value
				#X	#4a For each row create string for tagPath from equipment path
				EQPath = eqPath
				tagName = JobTagDict.get(key)
				currentTagPath =  EQPath + '/' + tagName
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
def copyJob(tagPath):
	try:
		currentJobPath = getJobPath(tagPath, 'currentJob')
		previousJobPath = getJobPath(tagPath, 'previousJob')
		currentJobTags = gpa.tag.browse(currentJobPath, recursive=True)
		previousJobTags = gpa.tag.replace(tags=currentJobTags, oldString=STR_CURRENT_JOB, newString=STR_PREVIOUS_JOB)
		gpa.tag.moveTagsValues(fromTags=currentJobTags, toTags=previousJobTags)
		return 1
	except Exception as e:
		raise e
		return 0
        
        
#@timeit
@error_log
#@dump_args
def getJobPath(tagPath, job):
	return tagPath + "/jobs/" + job

#@timeit
@error_log
#@dump_args
def getNextJobPath(tagPath):
	return tagPath + "/jobs/nextJob"


#@timeit
@error_log
#@dump_args
def getPreviousJobPath(tagPath):
	return tagPath + "/jobs/previousJob" 

	
#@timeit
@error_log
#@dump_args	
def getCurrentJobPath(tagPath):
	return tagPath + "/jobs/currentJob" 
    
 
#@timeit
@error_log
#@dump_args
def setNextJob(tagPath, opScheduleUuid, workOrderName):
	setWorkOrder(tagPath, workOrderName)
	setOperationsScheduleUuid(tagPath, opScheduleUuid)
	populateNextJob(tagPath, workOrderName)


#@timeit
@error_log
#@dump_args
def populateNextJob(tagPath, workOrderName):
	pass


#@timeit
@error_log
#@dump_args
def clearJob(jobPath):
	jobTags = gpa.tag.browse(path=jobPath,recursive=True)
	gpa.tag.clearTags(jobTags)
	return None


#@timeit
@error_log
#@dump_args
def clearNextJob(tagPath):
	jobPath = getNextJobPath(tagPath)
	clearJob(jobPath)
	return None


#@timeit
@error_log
#@dump_args
def clearCurrentJob(tagPath):
	jobPath = getCurrentJobPath(tagPath)
	clearJob(jobPath)
	return None


#@timeit
@error_log
#@dump_args
def clearPreviousJob(tagPath):
	jobPath = getPreviousJobPath(tagPath)
	clearJob(jobPath)
	return None	


#@timeit
@error_log
#@dump_args
def setPreviousJob(tagPath):
	currJobPath = getCurrentJobPath(tagPath)
	prevJobPath = getPreviousJobPath(tagPath)
	currJobTags = gpa.tag.browse(path=currJobPath,recursive=True)
	prevJobTags = gpa.tag.replace(tags=currJobTags, oldString=STR_CURRENT_JOB, newString=STR_PREVIOUS_JOB)
	gpa.tag.moveTagsValues(fromTags=currJobTags, toTags=prevJobTags)
	return None


#@timeit
@error_log
#@dump_args
def cleanJob(tagPath, tags):
	if 'Molding' not in tagPath: 
		cleanTags = []
		for tag in tags:
			tagPath = str(gpa.tag.getPath(tag))
			if 'productionCounts' not in tagPath:
				cleanTags.append(tag)
	else:
		cleanTags = tags
				
	return cleanTags


#@timeit
@error_log
#@dump_args
def setCurrentJob(tagPath):
	nextJobPath = getNextJobPath(tagPath)
	currJobPath = getCurrentJobPath(tagPath)
	nextJobTags = gpa.tag.browse(path=nextJobPath,recursive=True)
	
	nextJobTags = cleanJob(tagPath, nextJobTags)
	
	currJobTags = gpa.tag.replace(tags=nextJobTags, oldString=STR_NEXT_JOB, newString=STR_CURRENT_JOB)
	gpa.tag.moveTagsValues(fromTags=nextJobTags, toTags=currJobTags)
	return None


#@timeit
@error_log
#@dump_args
def isNextJobselected(tagPath):

	nextJobselected = True # Placeholder logic
	return nextJobselected


#@timeit
@error_log
#@dump_args	
def isJobRunning(tagPath):
	isRunning = True # Placeholder logic
	return isRunning
    
    
#@timeit
@error_log
#@dump_args
def endJob(tagPath, isWorkOrderComplete): # isWorkOrderComplete boolean param
	pass
    
#@timeit
@error_log
#@dump_args	
def startJob(tagPath):
	pass


#@timeit
@error_log
#@dump_args
def setWorkOrder(tagPath, workOrderName, job="nextJob"):
	workOrderPath = tagPath + "/Jobs/" + job + "/workOrder"
	result = gpa.tag.writeBlocking(tagPaths=[workOrderPath], values=[workOrderName])
	return result 	
	
#@timeit
@error_log
#@dump_args
def setOperationsScheduleUuid(tagPath, operationsScheduleUuid, job="nextJob"):
	operationsSchedulePath = tagPath + "/Jobs/" + job + "/opScheduleUuid"
	result = gpa.tag.writeBlocking(tagPaths=[operationsSchedulePath], values=[operationsScheduleUuid])
	return result

#@timeit
@error_log
#@dump_args
def endJobFromTag(tagPath, params):
	jobPath = tagPath + '/jobs/currentJob'
	runID = params.get('runID')

	mes.schedule.jobs.copyJob(tagPath)
	res = mes.schedule.sp.runEnd(params)
	#make sure to clear after namedquery		
	mes.schedule.jobs.clearJob(jobPath)	
	return res
	
#@timeit
@error_log
#@dump_args
def setNextRunFromTag(tagPath, params):
	workOrder = params.get('woName')
	lineID = params.get('lineID')
	jobPath = tagPath + '/jobs/currenJob'
	
	scheduleID = mes.schedule.sp.getScheduleID(workOrder, lineID)
	res = mes.schedule.sp.startRun(scheduleID)
	
	if res:
		mes.schedule.jobs.copyJob(tagPath)
		mes.schedule.jobs.clearJob(jobPath)
		mes.schedule.jobs.updateJob(scheduleID, tagPath, 'currentJob')
		return True
	else: raise Exception('Could not start run.')
	
	
	
