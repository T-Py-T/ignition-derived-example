'''
This contains all mode functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders
import os

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.oee.mode')


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



#@timeit
@error_log
#@dump_args
def getMode(tagPath):
	modePath = tagPath + "/scadaControlled/mode"
	qualifiedValues = gpa.tag.readBlocking(tagPaths=[modePath])
	qualifiedValue = qualifiedValues[0]
	mode = qualifiedValue.value
	return mode


#@timeit
@error_log
#@dump_args
def setMode(tagPath, mode=0):
	modePath = tagPath + "/scadaControlled/mode"
	gpa.tag.writeBlocking(tagPaths=[modePath],values=[mode])
	return None


#@timeit
@error_log
#@dump_args
def setModeProduction(tagPath):
	setMode(tagPath, MODE_PRODUCTION)
	return None


#@timeit
@error_log
#@dump_args
def setModeChangeover(tagPath):
	setMode(tagPath, MODE_CHANGEOVER)
	return None


#@timeit
@error_log
#@dump_args
def setModeDisabled(tagPath):
	setMode(tagPath, MODE_DISABLED)
	return None


#@timeit
@error_log
#@dump_args
def setModeIdle(tagPath):
	setMode(tagPath, MODE_IDLE)
	return None

	
#@timeit
@error_log
#@dump_args
def setModeMaintenance(tagPath):
	setMode(tagPath, MODE_MAINTENANCE)
	return None


#@timeit
@error_log
#@dump_args
def setModeMaintenanceCalled(tagPath):
	setMode(tagPath, MODE_MAINTENANCE_CALLED)
	return None


#@timeit
@error_log
#@dump_args
def setModeMaintenanceInProgress(tagPath):
	setMode(tagPath, MODE_MAINTENANCE_IN_PROGRESS)
	return None

	
#@timeit
@error_log
#@dump_args	
def setModeMaintenanceLeft(tagPath):
	setMode(tagPath, MODE_MAINTENANCE_LEFT)
	return None


#@timeit
@error_log
#@dump_args
def setModeQualityCalled(tagPath):
		"""
		Sets the mode of this line to quality called
		
		Original Author: Taylor Turner
		Created Date: 2/26/2022
			
		Args:
			tagPath (str): Equipment path of the line
		Returns:
			None: Sets the current mode of this line
		"""
		setMode(tagPath, MODE_QUALITY_CALLED)
		return None


#@timeit
@error_log
#@dump_args
def setModeQualityInProgress(tagPath):
		"""
		Sets the mode of this line to maintenance called
		
		Original Author: Taylor Turner
		Created Date: 2/26/2022
				
		Args:
			tagPath (str): Equipment path of the line
		Returns:
			None: Sets the current mode of this line
		"""
		setMode(tagPath, MODE_QUALITY_IN_PROGRESS)
		return None


#@timeit
@error_log
#@dump_args
def setModeTeamLeadCalled(tagPath):
		"""
		Sets the mode of this line to quality called
		
		Original Author: Taylor Turner
		Created Date: 2/26/2022
			
		Args:
			tagPath (str): Equipment path of the line
		Returns:
			None: Sets the current mode of this line
		"""
		setMode(tagPath, MODE_TEAM_LEAD_CALLED)
		return None


#@timeit
@error_log
#@dump_args
def setModeTeamLeadInProgress(tagPath):
		"""
		Sets the mode of this line to maintenance called
		
		Original Author: Taylor Turner
		Created Date: 2/26/2022
				
		Args:
			tagPath (str): Equipment path of the line
		Returns:
			None: Sets the current mode of this line
		"""
		setMode(tagPath, MODE_TEAM_LEAD_IN_PROGRESS)
		return None