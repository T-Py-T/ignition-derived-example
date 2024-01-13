"""
This contains all mes config functions
"""
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.config.getAssets')

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     EXAMPLE FUNCTION
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#@timeit
#@error_log
#@dump_args
#def exampleFunction(arg1):
#	""" Description of function purpose
#		Args:
#		  	arg1 (type): description of argument
#		Returns:
#			(type): description of argument
#		Testing: (script console)
#			system.downtime.periodic.exampleFunction(arg1)
#		TODO:
#			_ - Finish adding ______
#	"""
#	# Write back to [MES] tag provider with equipment path
#	pass


#@timeit
@error_log
#@dump_args
def getSiteID():
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
		Returns: integer ID for site
		Testing: print(mes.config.getAssets.getSiteID())
	"""
	#build a query to retrieve lineID and linePath
	getSiteQuery = """
		SELECT DISTINCT SiteID
		FROM [MES].[config].[vw_productionmodel]
		WHERE SiteID <> 0
			AND EnterpriseID <> 0
		"""
	scalar = system.db.runQuery(getSiteQuery,db)
	#scalar = system.db.runQuery(getSiteQuery,[],db) #someone broke this and didnt say anything - TNT20230429
	return scalar[0][0]


#@timeit
@error_log
#@dump_args
def getAllLinesForSite(SiteID):
	""" Gets all currently enabled lines for the current site
		Args:
		Returns: List of LineIDs for iterating
		Testing:
			print(mes.config.getAssets.getAllLinesForSite(1))
	"""
	#build a query to retrieve lineID and linePath
	AllLinesQuery = """
		SELECT DISTINCT lineID
		FROM [MES].[config].[vw_productionmodel]
		where SiteID = ?
		AND LineID <> 0
	"""
	data = system.db.runPrepQuery(AllLinesQuery,[SiteID],db)
	return data


#@timeit
@error_log
#@dump_args
def getAllAreasForSite(SiteID):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
		Returns: List of AreaIDs for iterating
		Testing:
	"""
	#build a query to retrieve lineID and linePath
	AllAreasQuery = """
		SELECT DISTINCT AreaID
			FROM config.vw_productionmodel
			where SiteID = ?
			AND AreaID <> 0
	"""
	data = system.db.runPrepQuery(AllAreasQuery,[SiteID],db)
	return data


#@timeit
@error_log
#@dump_args
def getAllGroupsForArea(AreaID):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
		Returns: List of AreaIDs for iterating
		Testing:
	"""
	# Write back to [MES] tag provider with equipment path
	pass
	
	
#@timeit
@error_log
#@dump_args
def getAllLinesForArea(AreaID):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
		Returns: List of LineIDs for iterating
		Testing:
	"""
	# Write back to [MES] tag provider with equipment path
	pass