"""
This contains all event tagCreation functions
"""
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.gateway.health')

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()

@timeit
@error_log
#@dump_args
def getTagHistory(timeLength):
		# The following example will return a dataset with one row detailing last value of a Tag for the past 30 minutes.
		timeLength *= -1
		#print('timeLength: ',timeLength)
		endTime = system.date.now()
		startTime = system.date.addMinutes(endTime, timeLength)
		#tagEndingList = ['Performance/CPU Usage','Performance/Disk Utilization', 'Performance/Memory Utilization']
		values = []
		
		tagList = ['[GatewayHealth]Gateways/Script/Performance/CPU Usage','[GatewayHealth]Gateways/Script/Performance/Disk Utilization', '[GatewayHealth]Gateways/Script/Performance/Memory Utilization', 
					'[GatewayHealth]Gateways/Tag1/Performance/CPU Usage','[GatewayHealth]Gateways/Tag1/Performance/Disk Utilization', '[GatewayHealth]Gateways/Tag1/Performance/Memory Utilization',
					'[GatewayHealth]Gateways/App1/Performance/CPU Usage','[GatewayHealth]Gateways/App1/Performance/Disk Utilization', '[GatewayHealth]Gateways/App1/Performance/Memory Utilization'
				  ]
		writeTagList = ['[GatewayHealth]Gateways/Script/_History/CPU', '[GatewayHealth]Gateways/Script/_History/Disk', '[GatewayHealth]Gateways/Script/_History/Memory',
						'[GatewayHealth]Gateways/Tag1/_History/CPU', '[GatewayHealth]Gateways/Tag1/_History/Disk','[GatewayHealth]Gateways/Tag1/_History/Memory',
						'[GatewayHealth]Gateways/App1/_History/CPU', '[GatewayHealth]Gateways/App1/_History/Disk','[GatewayHealth]Gateways/App1/_History/Memory',
						]
			
		#Check lengths are equal
		if len(writeTagList) == len(tagList):
			for tagPath in tagList:
				dataSet = system.tag.queryTagHistory(paths=[tagPath], startDate=startTime, endDate=endTime, aggregationMode="LastValue", returnFormat='Wide')
				#pyDS = system.dataset.toPyDataSet(dataSet)
				values.append(dataSet) # update values list, one DS for each path.
				
			#Check lengths are equal
			if len(writeTagList) == len(values): system.tag.writeBlocking(writeTagList, values)#write DS back to tags
			else: print('List lengths are not equal len(writeTagList) != len(values)') #Log length mismatch
		else: print('List lengths are not equal len(writeTagList) != len(tagList)') #Log length mismatch
	