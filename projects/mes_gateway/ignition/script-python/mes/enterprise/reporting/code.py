""" ========================================================================
Library contains functions for reporting analysis 
============================================================================"""
from gpa.data import swapDataKeys
from gpa.data import datasetToJson
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()

logger = system.util.getLogger('mes.analysis.reporting')


def getShiftAnalysis(equipmentPath, startDate, endDate):
	pass


def getShiftAnalysisMolding(equipmentPath, startDate, endDate):
	pass

	
def getRunAnalysis(equipmentPath, startDate, endDate):
	pass


def getRunAnalysisMolding(equipmentPath, startDate, endDate):
	pass

def getDaysFromEpoch(date):
	return system.date.daysBetween( system.date.getDate(1900,0,1), date)

def getUTCOffset(date):
	return system.date.getTimezoneOffset(date) * 3600


def getRunData(equipmentPath, startDate, endDate):
	pass


	# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	#	GETS IntervalStream Data
	# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def getShiftData(equipmentPath, startDate, endDate):
	pass

	
def getData(equipmentPath, startDate, endDate, analysisData):
	pass
	

# MODIFIED BY AUDREY THATCHER (2023-03-28)
def insertIntervalStreamData(EquipmentPath = None, StartTime = None, EndTime = None, TimePeriod = None, Type = 'Unknown'):
	'''
		Inserts data into erp.interval_stream
	'''
	
	call = system.db.createSProcCall('erp.stp_insertIntervalStreamData', db)
	
	call.registerInParam('equipmentPath', system.db.VARCHAR, EquipmentPath)
	call.registerInParam('timeStart', system.db.DATETIME, StartTime)
	call.registerInParam('timeEnd', system.db.DATETIME, EndTime)
	call.registerInParam('timePeriod', system.db.VARCHAR, TimePeriod)
	call.registerInParam('type', system.db.VARCHAR, Type)
	
	try:
		system.db.execSProcCall(call)
		return True
	except:
		return False
	
	return True



'''
Timeline Stream table 
'''
def getLastStreamInsertForDevice(deviceKey):
	selectQuery =	'''
					SELECT MAX("end_time") 
					FROM enterprisereporting.timeline_stream
					WHERE "deviceKey" = ?
					'''	
	lastInsert = system.db.runScalarPrepQuery(selectQuery, [deviceKey], 'application')
	return lastInsert
		

def getLineStateHistory(equipmentPath, startDate, endDate = None):
	pass

def getLineStateHistoryAnalysis(equipmentPath, startDate, endDate = None):
	pass
		
		
def getTimeLineStreamData(equipmentPath, startDate = None, endDate = None):
	pass
	

def insertTimeLineStreamData(data):
	pass