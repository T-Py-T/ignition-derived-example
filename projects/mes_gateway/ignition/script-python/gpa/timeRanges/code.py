'''
This contains all OEE calculation functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders
import time

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()



#@timeit
@error_log
#@dump_args
def getCurrentShiftTimes(timePeriod,db=db):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
		Returns: List of AreaIDs for iterating
		Testing:
			mes.timeRanges.getCurrentShift('currentShift')
	"""
	#build a query to retrieve lineID and linePath
	shiftTimesQuery = """
		-- SET @timePeriod = ?
		SELECT StartTime, EndTime
		FROM GetTimeRange(?, NULL)
	"""
	# 'SELECT @timeStart = StartTime, @timeEnd = EndTime FROM GetTimeRange(@timePeriod, NULL);'
	
	data = system.db.runPrepQuery(shiftTimesQuery,[timePeriod],db)
	return data


#@timeit
@error_log
#@dump_args
def secondsToDateString(timeInSeconds,dbFormat=False):
	""" Gets Top5 DT DS for each line and returns it as larger dataset
	Args:
	  timeRangeType (Integer):
	Returns:
	  (String): fromatted to '__h __m __s'
	Testing:
	    print(gpa.timeRanges.secondsToDateString(15660)) # == 04:21:00
	 	
	TODO: Function takes "elapsed time: 0._____"
	"""
	formattedDuration = time.strftime("%H:%M:%S", time.gmtime(timeInSeconds))
	if dbFormat: return formattedDuration
	else:
		splitTime = formattedDuration.split(":")
		if len(splitTime) == 3: durationString = splitTime[0] + "h " + splitTime[1] + "m " + splitTime[2] + "s"
		elif len(splitTime) == 2: durationString = splitTime[0] + "m " + splitTime[1] + "s"
		else: durationString = splitTime[0] + "s"
		return durationString

#@timeit
@error_log
#@dump_args
def minutesTohms(minutes):
    """
    Converts a given number of minutes to "hh:mm:ss" format.
    """
    hours = minutes / 60
    minutes = minutes % 60
    seconds = minutes * 60
    return "%02d:%02d:%02d" % (hours, minutes, seconds)












































#Default
	#not set as defualt yet
def getDefault(currentTime):
	'''Calculates start and end time of the current full day given the currentTime which is the "now" inside of the function.
	
	Returns: 
		dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	midnight = system.date.midnight(currentTime)
	return {'timeStart': midnight, 'timeEnd': currentTime}

#Historical

def getLastHour(currentTime):
	'''Calculates start and end time of the last full day given the current time.
		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisHour = system.date.getHour24(currentTime)
	timeEnd = system.date.setTime(currentTime, thisHour, 0, 0)
	timeStart = system.date.addHours(timeEnd,-1)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}

	
def getLast3Hour(currentTime):
	'''Calculates start and end time of the last 3 full hours given the current time.
		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisHour = system.date.getHour24(currentTime)
	timeEnd = system.date.setTime(currentTime, thisHour, 0, 0)
	timeStart = system.date.addHours(timeEnd,-3)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	

def getLastShift(currentTime):
	'''Calculates start and end time of the last full shift given the current time.

		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	midnight = system.date.midnight(currentTime)
	if system.date.getHour24(currentTime) in range(0,6):
		timeEnd = system.date.addHours(midnight,-5)
		timeStart = system.date.addHours(timeEnd, -12)
	elif  system.date.getHour24(currentTime) in range(7,19):
		timeEnd = system.date.addHours(midnight,+7)
		timeStart = system.date.addHours(timeEnd, -12)	
	elif system.date.getHour24(currentTime) in range(20,24):
		timeEnd = system.date.addHours(midnight,+19)
		timeStart = system.date.addHours(timeEnd,-12)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	
	
def getLastDay(currentTime):
	'''Calculates start and end time of the last full day (7am to 7am) given the current time.
		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	midnight = system.date.midnight(currentTime)
	if system.date.getHour24(currentTime) in range(0,6):
		timeEnd = system.date.addHours(midnight,-15)
		timeStart = system.date.addHours(timeEnd, -24)
	elif  system.date.getHour24(currentTime) in range(7,24):
		timeEnd = system.date.addHours(midnight,+7)
		timeStart = system.date.addHours(timeEnd, -24)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	
	
def getLastWeek(currentTime):
	'''Calculates start and end time of the last full week given the current time.
		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisDay = system.date.getDayOfYear(currentTime)
	dayOfWeek = system.date.getDayOfWeek(currentTime)
	thisYear = system.date.getYear(currentTime)
	startOfYear = system.date.getDate(thisYear, 0, 1)
	daysToAdd = thisDay - dayOfWeek + 1 # puts us back to sunday, we want monday work week start
	startOfThisWeek = system.date.addDays(startOfYear, daysToAdd)
	previousWeek = system.date.addWeeks(startOfThisWeek,-1)
	timeEnd = system.date.addHours(startOfThisWeek,+7)
	timeStart = system.date.addHours(previousWeek,+7)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	
	
def getLast4Weeks(currentTime):
	'''Calculates start and end time of the last full 4 weeks given the current time.
	
		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisDay = system.date.getDayOfYear(currentTime)
	dayOfWeek = system.date.getDayOfWeek(currentTime)
	thisYear = system.date.getYear(currentTime)
	startOfYear = system.date.getDate(thisYear, 0, 1)
	daysToAdd = thisDay - dayOfWeek + 1 # puts us back to sunday, we want monday work week start
	startOfThisWeek = system.date.addDays(startOfYear, daysToAdd)
	previous4Weeks = system.date.addWeeks(startOfThisWeek,-4)
	timeEnd = system.date.addHours(startOfThisWeek,+7)
	timeStart = system.date.addHours(previous4Weeks,+7)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	
def getLastMonth(currentTime):
	'''Calculates start and end time of the last full month given the current time.
	
		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisMonth = system.date.getMonth(currentTime)
	thisYear = system.date.getYear(currentTime)
	monthStartAsDate = system.date.getDate(thisYear, thisMonth, 1)
	timeEnd = system.date.addHours(monthStartAsDate,+7)
	timeStart = system.date.addMonths(timeEnd,-1)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}


def getLastQuater(currentTime):
	'''Calculates start and end time of the last full quater given the current time.
	
		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	#daylights saving time setting timeStart at 6 am vs 7 am 
	thisMonth = system.date.getMonth(currentTime)
	thisYear = system.date.getYear(currentTime)
	
	if thisMonth in range(0,2): 
		startQuaterMonth = 9
		endQuaterMonth = 0
		thisYear = thisYear-1
	elif thisMonth in range(3,5): 
		startQuaterMonth = 0
		endQuaterMonth = 3
	elif thisMonth in range(6,8): 
		startQuater = 3
		endQuater = 6
	elif thisMonth in range(9,11): 
		startQuaterMonth = 6
		endQuaterMonth = 9
		
	startOfQuaterDate = system.date.getDate(thisYear, startQuaterMonth, 1)
	endOfQuaterDate = system.date.getDate(thisYear, endQuaterMonth, 1)
	timeEnd = system.date.setTime(endOfQuaterDate, 7, 0, 0) 
	timeStart = system.date.setTime(startOfQuaterDate, 7, 0, 0) 
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	
	
def getLast6Months(currentTime):
	'''Calculates start and end time of the last full 6 months given the current time.
		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisMonth = system.date.getMonth(currentTime)
	thisYear = system.date.getYear(currentTime)
	thisMonthAsDate = system.date.getDate(thisYear, thisMonth, 1)
	timeEnd = system.date.addHours(thisMonthAsDate,+7)
	timeStart = system.date.addMonths(timeEnd,-6)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	
def getLastYear(currentTime):
	'''Calculates start and end time of the last full year given the current time.
	
		Original Author: Andrew Cecola
		
		Created Date: 05/05/2020
		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisYear = system.date.getYear(currentTime)
	startOfYear = system.date.getDate(thisYear, 0, 1)
	timeEnd = system.date.setTime(startOfYear, 7, 0, 0)
	timeStart = system.date.addYears(timeEnd,-1)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
		
	

#Current 

def getCurrentHour(currentTime):
	'''Calculates start and end time of the last hour up to the current time given the current time.
		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisHour = system.date.getHour24(currentTime)
	timeEnd = currentTime
	if thisHour == 7:
		timeStart = system.date.setTime(currentTime, 7, 0, 0)
	elif thisHour == 19:
		timeStart = system.date.setTime(currentTime, 19, 0, 0)
	else:
		timeStart = system.date.addHours(timeEnd,-1)
		
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	
def getCurrent3hours(currentTime):
	'''Calculates start and end time of the last 3 hours up to current time given up to the current time.
		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisHour = system.date.getHour24(currentTime)
	timeEnd = currentTime
	if thisHour in range(7,9):
		timeStart = system.date.setTime(currentTime, 7, 0, 0)
	elif thisHour in range(19,21):
		timeStart = system.date.setTime(currentTime, 19, 0, 0)
	else:
		timeStart = system.date.addHours(timeEnd,-3)

	return {'timeStart': timeStart, 'timeEnd': timeEnd}

def getCurrentShift(currentTime):
	'''Calculates start and end time of the current shift up to current time given the current time.
		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	timeEnd = currentTime
	midnight = system.date.midnight(currentTime)
	
	if system.date.getHour24(currentTime) in range(0,6):
		timeStart = system.date.addHours(midnight,-5)
	elif  system.date.getHour24(currentTime) in range(7,19):
		timeStart = system.date.addHours(midnight,+7)
	elif system.date.getHour24(currentTime) in range(20,24):
		timeStart = system.date.addHours(midnight,+19)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}

def getCurrentDay(currentTime):
	'''Calculates start and end time of the current day up the current time given the current time. 
		
		Args: 
			currentTime (datetime): the "now" passed in
		Returns: 
			dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	midnight = system.date.midnight(currentTime)
	timeEnd = currentTime
	timeStart = system.date.addHours(midnight,+7)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	
def getCurrentWeek(currentTime):
	'''Calculates start and end time of the current Week up the current time given the current time.
	
	Args: 
		currentTime (datetime): the "now" passed in
	Returns: 
		dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisDay = system.date.getDayOfYear(currentTime)
	dayOfWeek = system.date.getDayOfWeek(currentTime)
	thisYear = system.date.getYear(currentTime)
	startOfYear = system.date.getDate(thisYear, 0, 1)
	daysToAdd = thisDay - dayOfWeek + 1 # puts us back to sunday, we want monday work week start
	startOfThisWeek = system.date.addDays(startOfYear, daysToAdd)
	timeEnd = currentTime	
	timeStart = system.date.addHours(startOfThisWeek,+7)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	
def getCurrent4Weeks(currentTime):
	'''Calculates start and end time of the current 4 weeks up the current time given the current time.

	Args: 
		currentTime (datetime): the "now" passed in
	Returns: 
		dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	dayOfMonth = system.date.getDayOfMonth(currentTime)
	thisMonth = system.date.getMonth(currentTime)
	thisYear = system.date.getYear(currentTime)
	thisDayAsDate = system.date.getDate(thisYear, thisMonth, dayOfMonth)
	previous4WeekDate = system.date.addWeeks(thisDayAsDate, -4)

	timeEnd = currentTime	
	timeStart = system.date.addHours(previous4WeekDate,+7)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	
def getCurrentMonth(currentTime):
	'''Calculates start and end time of the current 4 weeks up the current time given the current time.

	
	Args: 
		currentTime (datetime): the "now" passed in
	Returns: 
		dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisMonth = system.date.getMonth(currentTime)
	thisYear = system.date.getYear(currentTime)
	thisMonthAsDate = system.date.getDate(thisYear, thisMonth, 1)
	
	timeEnd = currentTime	
	timeStart = system.date.addHours(thisMonthAsDate,+7)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	
def getCurrentQuater(currentTime):
	'''Calculates start and end time of the current Quater up the current time given the current time.
	
	Args: 
		currentTime (datetime): the "now" passed in
	Returns: 
		dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisMonth = system.date.getMonth(currentTime)
	thisYear = system.date.getYear(currentTime)
	
	if thisMonth in range(0,2): 
		startQuaterMonth = 0
	elif thisMonth in range(3,5): 
		startQuaterMonth = 3
	elif thisMonth in range(6,8): 
		startQuaterMonth = 6
	elif thisMonth in range(9,11): 
		startQuaterMonth = 9
		
	startDate = system.date.getDate(thisYear, startQuaterMonth, 1)
	timeEnd = currentTime	
	timeStart = system.date.addHours(startDate,+7)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	
def getCurrent6Months(currentTime):
	'''Calculates start and end time of the current 6 months up to the current time given the current time.
	
	Args: 
		currentTime (datetime): the "now" passed in
	Returns: 
		dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisMonth = system.date.getMonth(currentTime)
	thisYear = system.date.getYear(currentTime)
	thisMonthAsDate = system.date.getDate(thisYear, thisMonth, 1)
	previous6MonthsAsDate = system.date.addMonths(thisMonthAsDate,-6)
	
	
	timeEnd = currentTime	
	timeStart = system.date.addHours(previous6MonthsAsDate,+7)
	return {'timeStart': timeStart, 'timeEnd': timeEnd}
	
def getCurrentYear(currentTime): #	auto subtracks 1 hour to timeStart and endTime due to day lighs saving time
	'''Calculates start and end time of the current year up to the current time given the current time.
	
	Args: 
		currentTime (datetime): the "now" passed in
	Returns: 
		dict object containing two values: 'timeStart' and 'timeEnd'
	'''
	thisYear = system.date.getYear(currentTime)
	startOfYear = system.date.getDate(thisYear, 0, 1)
	
	timeEnd = currentTime
	timeStart = system.date.addHours(startOfYear,+7)  # maybe should add 1 hour here to account for auto datelight saveing
	return {'timeStart': timeStart, 'timeEnd': timeEnd}