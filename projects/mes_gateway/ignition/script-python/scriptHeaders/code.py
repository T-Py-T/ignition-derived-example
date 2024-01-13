"""
This contains project level variables for ALL script headers
"""
db = "MSSQL_MES"
#db = "MES" #(PostgreSQL)

class ScriptHeaders():
#	Global Variables
	_NULL = None
	_dbDateFormat = "yyyy-MM-dd HH:mm:ss" #common DB date format
	_db = ""
	_micro = 60
	_siteId = 0
	_areas, _lines = [], []
	
	#Dictionarys for common mapping (time intervals, UDT folders, etc.)
	# Period->Folder Mapping {DBColumnName : TagName}
	_TimePeriodDict={
		'current shift':'Shift/Current',
		'last shift':'Shift/Previous',
		'today':'Day/Current',
		'yesterday':'Day/Previous',
		'this week':'Week/Current',
		'last week':'Week/Previous',
		'this month':'Month/Current',
		'last month':'Month/Previous',
		'this quarter':'Quarter/Current',
		'last quarter':'Quarter/Previous',
		'this year':'Year/Current',
		'last year':'Year/Previous'
		}
		
	_AggregateDict={
		'Pod':'Group',
		'Cell':'Group',
		'Group':'Group',
		'Area':'Area',
	 	'Site':'Site'}
	 	
#	Getters
	def __init__(self):
		self._db = db
	
	def getNull(self):
		return self._NULL
	
	def getDateFormat(self):
		return self._dbDateFormat
		
	def getAllThresholds(self):
		ds = mes.config.sp.getThresholds()
		return system.dataset.toPyDataSet(ds)
		
	def getDb(self):
		return self._db
		
	def getMicro(self):
		#micro =  mes.config.sp.getMicroDefinition()
		micro = 60
		self._micro = micro
		return self._micro
		
	def getTimePeriodDict(self):
		return self._TimePeriodDict
		
	def getAggregateDict(self):
		return self._AggregateDict
		
	def getSiteId(self):
		siteId = mes.config.getAssets.getSiteID()
		self._siteId = siteId
		return siteId
		
	def getAreas(self):
		siteId = self.getSiteConfigId()
		areaDS = ""
		areasList = []
		if siteId != 0:
			try: areasDS = mes.config.getAssets.getAllAreasForSite(self._siteId)
			except: raise Exception("Error getting all areas")
		else: raise Exception("Site ID has not been selected please run `getSiteConfigId` first.")
		
		for area in areasDS: areasList.append(area[0])
		return areasList
		
		
	def getLines(self):
		siteId = self.getSiteConfigId()
				
		linesDS = ""
		lineList = []
		
		if self._siteId != 0:
			try: linesDS = mes.config.getAssets.getAllLinesForSite(self._siteId)
			except: raise Exception("Error getting all lines")
		else: raise Exception("Site ID has not been selected please run `getSiteConfigId` first.")
		
		for line in linesDS: lineList.append(line[0])
		return lineList
	
#	Setters
	def setMicro(self, value):
		self._micro = value
	
#	Methods
	def getSiteConfigId(self):
		siteId = mes.config.getAssets.getSiteID()
		self._siteId = siteId
		return siteId