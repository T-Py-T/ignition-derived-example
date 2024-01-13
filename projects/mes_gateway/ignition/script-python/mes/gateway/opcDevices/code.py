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
logger = system.util.getLogger('gpa.opcDevices')



#StartingPath = '[GatewayHealth]Gateways/Tag1/Devices'
#params = {
#	"Server": "Tag1",
#	"Device": "201"
#}


#@timeit
@error_log
#@dump_args
def createOpcDevice(path, params):
	""" Creates a opc tag
		Args:
		  path (String): ......
		  params (Dictionary): {"Server": (String), "Device": (String)}
		Returns:
		  (int): 1 if passing......
		Testing:
			tagPath = 
			gpa.opcDevices.createOpcDevice(path, params)		
		TODO: 
	"""	
	# The provider and folder the Tag will be placed at.
	baseTagPath = path
	  
	# Properties that will be configured on that Tag.
	tagName = params["Device"]
	typeId = "GPA/Device"
	tagType = "UdtInstance"
	# Parameters to pass in.
	server = params["Server"]
	device = params["Device"]
	  
	# Configure the Tag.
	tag = {     "name": tagName,         
	            "typeId" : typeId,
	            "tagType" : tagType,
	            "parameters" : {
	            	"Server" : server,
	            	"Device": device
	            }
	       }
	collisionPolicy = "o"  # "a" == abort, "o" == overwrite
	# Create the Tag.
	system.tag.configure(baseTagPath, [tag], collisionPolicy)

#@timeit
@error_log
#@dump_args		
def getAllDevices(server):
	""" Gets all opc device names .........
			Args:
			  server (String): ......
			Returns:
			  (array): ["DeviceName"]
			Testing:
				server = 
				gpa.opcDevices.getAllDevices(server)		
			TODO: 
		"""		
	server = server
	tags = system.opc.browse(opcServer=server, folderPath='*/Devices/*')
	devicesArr = []

	for row in tags:
		displayName = row.getDisplayName()
		if displayName[0] == '[' and displayName[-1] == ']' and displayName != '[Controls]' and displayName != '[Diagnostics]':
		   devicesArr.append(displayName)

	return devicesArr
	
#@timeit
@error_log
#@dump_args			
def writeOpcDevicesScheduled(serverName):
	""" Writes OPC devices to the Device folder
			Args:
			  serverName (String): ......
			Returns:
			  (array): ["DeviceName"]
			Testing:
				server = 
				mes.gateway.opcDevices.writeOpcDevicesScheduled(serverName)		
			TODO: 
		"""		
	server = serverName
	opcServer = server + "_OPCUA"
	devicesArr = getAllDevices(opcServer)
	
	serverDevicePath = "[GatewayHealth]Gateways/"+serverName+"/Devices/"
	
	deletePath = [serverDevicePath]
	path = serverDevicePath
	
	system.tag.deleteTags(deletePath)
	
	for device in devicesArr:
		strippedName = str(device).replace("[", "").replace("]", "")
		params = {
			"Server": server,
			"Device": strippedName
		}
		
		mes.gateway.opcDevices.createOpcDevice(path, params)