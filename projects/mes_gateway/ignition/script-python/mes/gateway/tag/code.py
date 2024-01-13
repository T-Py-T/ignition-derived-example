"""
This contains all event tagCreation functions
"""
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()
#micro = mes.config._scriptHeaders.micro
#siteID = mes.config._scriptHeaders.siteID
#areas = mes.config._scriptHeaders.areas
#lines = mes.config._scriptHeaders.lines
#TimePeriodDict = mes.config._scriptHeaders.TimePeriodDict
#AggregateDict = mes.config._scriptHeaders.AggregateDict

# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.gateway.tag')


StartingPath = '[GatewayHealth]Gateways/Tag1/Devices'
# 1. MAke folders
# 2. Make 4 tags with passed in data from your OPC server browse devices



EXAMPLE_JSON ={
  "valueSource": "opc",
  "opcItemPath": "nsu\u003durn:inductiveautomation:ignition:opcua:tags;s\u003d[System]/Gateway/Devices/ACCT1/Status",
  "dataType": "String",
  "name": "Status",
  "tagType": "AtomicTag",
  "opcServer": "Tag1_OPCUA"
}


#@timeit
@error_log
#@dump_args
def createEquipmentFolder(path,name):
	""" Gets ................
		Args:
		  timeRangeType (String): ......		
		Returns:
		  (int): 1 if passing, else -1
		Testing:
			ptah, name = '', ''
			mes.gateway.tag.createEquipmentFolder(path,name)			
		TODO: 
	"""	
	#Check tagPath length
	length = len(path.split('/'))
	if len > 4: pass #cell Level
	if len == 4: pass # Line level
	if len == 3: pass # Area Level


	# 1- Create Folder to contain the Equipment (With Line Equiment)
	Tags={'tagType': 'Folder',
	        'name': name,
	        'tags' : [ #other folders/UDTs
	                    {
	                    'name': 'anotherfolder',
	                    'tagType': 'Folder',
	                    'tags': [{}]            # There aren't any objects defined here, so this will just be an empty folder.                 
	                    }
	                ]
	        }
	 
	system.tag.configure(   basePath = '',
	                        tags = Tags,
	                        collisionPolicy = "o"
	                    )


#def createAnalysisTag(tagPath):
#	# 1- Create Folder to contain Analysis
#
#	# The provider and folder the Tag will be placed at.
#	baseTagPath = tagPath
#	  
#	# Properties that will be configured on that Tag.
#	tagName = "Analysis"
#	typeId = "Analysis"
#	tagType = "UdtInstance"
#	# Parameters to pass in.
#	#motorNum = "1"
#	  
#	# Configure the Tag.
#	tag = {     "name": tagName,         
#	            "typeId" : typeId,
#	            "tagType" : tagType
#	            #"parameters" : 
#	            #{"motorNum" : motorNum
#	            #}
#	       }
#	collisionPolicy = "a"  # "a" == abort, "o" == overwrite
#	# Create the Tag.
#	system.tag.configure(baseTagPath, [tag], collisionPolicy)



#'[GatewayHealth]Gateways/Tag1/Devices' + DeviceName

#@timeit
@error_log
#@dump_args
def createEquipmentTag(tagPath):
	""" Gets .........
		Args:
		  timeRangeType (String): ......
		Returns:
		  (int): 1 if passing......
		Testing:
			tagPath = 
			mes.gateway.tag.createEquipmentTag(tagPath)		
		TODO: 
	"""	
	# The provider and folder the Tag will be placed at.
	baseTagPath = tagPath
	  
	# Properties that will be configured on that Tag.
	tagName = "Analysis"
	typeId = "Analysis"
	tagType = "UdtInstance"
	# Parameters to pass in.
	#motorNum = "1"
	  
	# Configure the Tag.
	tag = {     "name": tagName,         
	            "typeId" : typeId,
	            "tagType" : tagType
	            #"parameters" : 
	            #{"motorNum" : motorNum
	            #}
	       }
	collisionPolicy = "a"  # "a" == abort, "o" == overwrite
	# Create the Tag.
	system.tag.configure(baseTagPath, [tag], collisionPolicy)