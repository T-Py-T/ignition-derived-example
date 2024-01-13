"""
This contains all event tagCreation functions
"""

from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.gateway.events')

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()
areas = sh.getAreas()


#@timeit
@error_log
#@dump_args
def getEndOfCalculations(timePeriod):
	""" Gets ................
		Args:
		  timeRangeType (String): ......		
		Returns:
		  (int): 1 if passing, else -1
		Testing:
			timePeriod = 'current shift'
			mes.gateway.events.getEndOfCalculations(timePeriod)		
		TODO: 
			- FIX updateAllSiteAreasOEE_AQP
	"""	
	#%%%%%%%%%%%%%%%%%%%%%%	(FAST) ALL LINES	%%%%%%%%%%%%%%%%%%%%%%
	fastUpdateOEEDT(timePeriod)

	#%%%%%%%%%%%%%%%%%%%	(SLOW) ALL AREAS/SITES	%%%%%%%%%%%%%%%%%%%%%%
	slowUpdateOEEDT(timePeriod)
	
	
#@timeit
@error_log
#@dump_args
def fastUpdateOEEDT(timePeriod):
	""" Gets ................
		Args:
		  timeRangeType (String): ......		
		Returns:
		  (int): 1 if passing, else -1
		Testing:
			timePeriod = 'current shift'
			mes.gateway.events.fastUpdateOEEDT(timePeriod)		
		TODO:
			X - Get All DTSummary
			X - Get All PlannedUnplannedDT
			X - Get All OEE_AQP Working
			X - Get All DowntimeEvents Working
			_ - Get All DowntimeTop5 Working
	"""	
	#OEE
	mes.oee.calcs.updateAllLinesOEE_AQP(timePeriod)
	
	#DOWNTIME
	mes.downtime.calcs.updateAllPlannedUnplannedDT(timePeriod)
	mes.downtime.calcs.updateAllDowntimeSummary(timePeriod)
	mes.downtime.calcs.updateAllDowntimeEvents(timePeriod)
	#mes.downtime.calcs.updateAllDowntimeEventsComposite(timePeriod)
	mes.downtime.calcs.updateAllLinesDTop5(timePeriod)
	mes.downtime.calcs.updateAllStateHistory(timePeriod)
	
	#ERP
	mes.quality.calcs.getScrapERP()

	#ADDED 9/8/23 by Noah
	mes.oee.periodic.updateOEETablePeriodic()

#@timeit
@error_log
#@dump_args
def slowUpdateOEEDT(timePeriod):
	""" Gets ................
		Args:
		  timeRangeType (String): ......		
		Returns:
		  (int): 1 if passing, else -1
		Testing:
			timePeriod = 'current shift'
			mes.gateway.events.slowUpdateOEEDT(timePeriod)		
		TODO:
			_ - Get All OEE_AQP Working
			_ - Get All OEE_Table Working
			_ - Get All DT Top5 Working
	"""	
	#OEE
	mes.oee.calcs.updateAllSiteAreasOEE_AQP(timePeriod)
	#mes.oee.calcs.updateAllAreaOEE_table(timePeriod)
	
	#DOWNTIME
	mes.downtime.calcs.updateAllSiteAreasDtTop5(timePeriod)



