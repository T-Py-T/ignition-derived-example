"""
This contains all event tagCreation functions
"""
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders

#sh = ScriptHeaders()
#NULL = sh.getNull()
#dbDateFormat = sh.getDateFormat()
#db = sh.getDb()



# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.config.tag')


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



@timeit
@error_log
#@dump_args
def createEquipmentFolder(path, name):
    """Creates a folder for equipment and its subfolders based on the specified path and name.
    Args:
        path (str): The base path where the folder will be created.
        name (str): The name of the folder to be created
    Returns:
        None
    Testing:
        print(mes.config.tag.createEquipmentFolder(path, name))
    """
    # Check tagPath length
    length = len(path.split('/'))
    if length > 4:
        pass  # Cell Level
    if length == 4:
        pass  # Line Level
    if length == 3:
        pass  # Area Level

    # 1- Create Folder to contain the Equipment (With Line Equiment)
    Tags = {
        'tagType': 'Folder',
        'name': name,
        'tags': [
            # other folders/UDTs
            {
                'name': 'anotherfolder',
                'tagType': 'Folder',
                'tags': [
                    # There aren't any objects defined here, so this will just be an empty folder.
                ]
            }
        ]
    }

    system.tag.configure(
        basePath=path,
        tags=Tags,
        collisionPolicy="o"
    )


#@timeit
@error_log
#@dump_args
def createAreaAnalysisTag(tagPath):
	""" 
		Creates Analysis tags in the [MES] provider
		Args:
		Returns: List of AreaIDs for iterating
		Testing:
			print(mes.config.tag.createEquipmentFolder(path, name))
	"""
	# 1- Create Folder to contain Analysis

	# The provider and folder the Tag will be placed at.
	baseTagPath = tagPath
	  
	# Properties that will be configured on that Tag.
	tagName = "Analysis"
	typeId = "[MES]_types_/GPA/AreaAnalysis"
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
	
#@timeit
@error_log
#@dump_args
def createLineAnalysisTag(tagPath):
	""" 
		Creates Analysis tags in the [MES] provider
		Args:
		Returns: List of AreaIDs for iterating
		Testing:
			print(mes.config.tag.createEquipmentFolder(path, name))
	"""
	# 1- Create Folder to contain Analysis

	# The provider and folder the Tag will be placed at.
	baseTagPath = tagPath
	  
	# Properties that will be configured on that Tag.
	tagName = "Analysis"
	typeId = "[MES]_types_/GPA/LineAnalysis"
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


#@timeit
@error_log
#@dump_args
def createEquipmentTag(tagPath):
	""" 
		Creates Equipment tags in the [MES] provider
		Args:
		Returns: List of AreaIDs for iterating
		Testing:
			print(mes.config.tag.createEquipmentFolder(path, name))
	"""
	# The provider and folder the Tag will be placed at.
	baseTagPath = tagPath
	  
	# Properties that will be configured on that Tag.
	tagName = "Analysis"
	typeId = "GPA/LineAnalysis"
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
	

	
#@timeit
@error_log
#@dump_args
def createAreaTags(tagPath):
	
	""" 
		Creates Line tags in the [default] provider
		Args:
			tagPath (string): defines the current selected path (parent)
		Returns: List of AreaIDs for iterating
		Testing:
			mes.config.tag.createAreaTags('[default]Aperture/SkullcrusherMountain/MonsterMasher')
	"""
	tagName = "calculatedValues"
	baseTagPath = tagPath
	typeId = "GPA/OEE/AreaCalculatedValues"
	tagType = "UdtInstance"
	
	# Properties that will be configured on that Tag.
	tag = { "name":tagName,
			"typeId" : typeId,
			"tagType" : tagType
		}
	
	collisionPolicy = "a"  # "a" == abort, "o" == overwrite
	# Create the Tag.
	system.tag.configure(baseTagPath, [tag], collisionPolicy)
	tagPath = "[MES]" + baseTagPath
	mes.config.tag.createAreaAnalysisTag(tagPath)
	
#@timeit
@error_log
#@dump_args
def createSiteTags(tagPath):
	
	""" 
		Creates Line tags in the [default] provider
		Args:
			tagPath (string): defines the current selected path (parent)
		Returns: List of AreaIDs for iterating
		Testing:
			mes.config.tag.createSiteTags('[default]Aperture/SkullcrusherMountain')
	"""
	tagName = "calculatedValues"
	baseTagPath = tagPath
	typeId = "GPA/OEE/SiteCalculatedValues"
	tagType = "UdtInstance"
	
	# Properties that will be configured on that Tag.
	tag = { "name":tagName,
			"typeId" : typeId,
			"tagType" : tagType
		}
	
	collisionPolicy = "a"  # "a" == abort, "o" == overwrite
	# Create the Tag.
	system.tag.configure(baseTagPath, [tag], collisionPolicy)
	tagPath = "[MES]" + baseTagPath
	mes.config.tag.createAreaAnalysisTag(tagPath)

#@timeit
@error_log
#@dump_args
def createEnterpriseTags(tagPath):
	
	""" 
		Creates Line tags in the [default] provider
		Args:
			tagPath (string): defines the current selected path (parent)
		Returns: List of AreaIDs for iterating
		Testing:
			mes.config.tag.createSiteTags('[default]Apature')
	"""
	tagName = "calculatedValues"
	baseTagPath = tagPath
	typeId = "GPA/OEE/SiteCalculatedValues"
	tagType = "UdtInstance"
	
	# Properties that will be configured on that Tag.
	tag = { "name":tagName,
			"typeId" : typeId,
			"tagType" : tagType
		}
	
	collisionPolicy = "a"  # "a" == abort, "o" == overwrite
	# Create the Tag.
	system.tag.configure(baseTagPath, [tag], collisionPolicy)
	tagPath = "[MES]" + baseTagPath
	mes.config.tag.createAreaAnalysisTag(tagPath)
		
#@timeit
@error_log
#@dump_args
def createLineTags(tagPath):
	
	""" 
		Creates Line tags in the [default] provider
		Args:
			tagPath (string): defines the current selected path (parent)
			tagName (string): defines the desired line name to be created
		Returns: List of AreaIDs for iterating
		Testing:
			mes.config.tag.createLineTags(TagPath)
	"""
	# The provider and folder the Tag will be placed at
	baseTagPath = tagPath# + '/' + tagName
	
	# Properties that will be configured on that Tag.
	tags = [
		{
			"tagName" : "calculatedValues",
			"typeId" : "GPA/OEE/LineCalculatedValues",
			"tagType" : "UdtInstance"
		},
		{
			"tagName" : "config",
			"typeId" : "GPA/OEE/LineConfig",
			"tagType" : "UdtInstance"
		},
		{
			"tagName" : "jobs",
			"typeId" : "GPA/Schedule/Jobs",
			"tagType" : "UdtInstance"
		},
		{
			"tagName" : "machineInput",
			"typeId" : "GPA/OEE/MachineInput_OPC_FB",
			"tagType" : "UdtInstance"
		},#{
		#	"tagName" : "machineOutput",
		#	"typeId" : "GPA/OEE/MachineOutput",
		#	"tagType" : "UdtInstance"
		#},
		{
			"tagName" : "OEE_Events",
			"typeId" : "GPA/OEE/OEE_Events_Line",
			"tagType" : "UdtInstance"
		},{
			"tagName" : "output",
			"typeId" : "GPA/OEE/LineOutput",
			"tagType" : "UdtInstance"
		},{
			"tagName" : "scadaControlled",
			"typeId" : "GPA/OEE/ScadaControlled",
			"tagType" : "UdtInstance"
		}
	]
	# Parameters to pass in.
	#motorNum = "1"
	  
	# Configure the Tag.  WRITE NEW TAGS FOR [DEFAULT]
	for udt in tags:
	       	tag = {     
	       		"name": udt["tagName"],         
	       		"typeId" : udt["typeId"],
	       		"tagType" : udt["tagType"]
	       		#"parameters" : 
	       		#{"motorNum" : motorNum
	       		#}
	      	}
		collisionPolicy = "a"  # "a" == abort, "o" == overwrite
		# Create the Tag.
		system.tag.configure(baseTagPath, [tag], collisionPolicy)
	
	
	# Configure the Tag.  WRITE NEW TAGS FOR [DEFAULT]
	tagPath = "[MES]" + baseTagPath
	mes.config.tag.createLineAnalysisTag(tagPath)


#@timeit
@error_log
#@dump_args
def createCellTags(tagPath, tagName):
	""" 
		Creates Cell tags in the [default] provider
		Args: 
			tagpath(the line the cell is apart of), 
			params(dictionary of cell parameters)
		Returns: List of AreaIDs for iterating
		Testing:
			print(mes.config.tag.createEquipmentFolder(path, name))
	"""
	baseTagPath = tagPath # we dont want to make a new folder
#	baseTagPath = tagPath
#	tagName = baseTagPath.split("/")[-1]
#	baseTagPath = baseTagPath.replace(tagName,"")

	# for testing with out passing
	params = {
		"device": {
			"dataType":"String",
			"value":tagName
		},
		"fault": {
			"dataType":"String",
			"value":None
		},
		"server":{
			"dataType":"String",
			"value":"Tag1_OPCUA"
		},
		"state":{
			"dataType":"String",
			"value":"State"
		}	
	}

# Properties that will be configured on that Tag.
	#tagName = params["device"]["value"]
	typeId = "GPA/OEE/OEE_Events_Cell_REF"
	tagType = "UdtInstance"
	# Parameters to pass in.
	#motorNum = "1"
	  
	# Configure the Tag.
	tag = {     "name": tagName,         
	            "typeId" : typeId,
	            "tagType" : tagType,
	            "parameters" : params
        }
	collisionPolicy = "a"  # "a" == abort, "o" == overwrite
	# Create the Tag.
	system.tag.configure(baseTagPath, [tag], collisionPolicy)
	#return tagName
	
	
#@timeit
@error_log
#@dump_args	
def deleteEq(tagPath):
	""" Deletes the selected tag path
		TODO: None
		Args: tagPath as string
		Returns: None    
		Testing: (script console)
			mes.config.tag.deleteEq(tagPath)
	"""
	system.tag.deleteTags([tagPath])
	
#@timeit
@error_log
#@dump_args	
def disableEq(tagPath, setEnabled, recurse=False):
	""" Disables equipment in [default] tag provider
		TODO: None
		Args: tagPath as string, setEnabled as bit, recurse as bool
		Returns: None    
		Testing: (script console)
			mes.config.tag.disableEq(tagPath, setEnabled, recurse=False)
		Runtime: 1.2 recursive, VPN
	"""
	collisionPolicy = "o" # "a" == abort, "o" == overwrite
	configs = system.tag.getConfiguration(tagPath, True)
	for tag in configs[0]['tags']:
		if str(tag['tagType']) != 'Folder':	    
			system.tag.writeAsync(tagPath+'/'+tag['name']+".Enabled", setEnabled)
		elif str(tag['tagType']) == 'Folder' and recurse ==True:
			mes.config.tag.disableEq(tagPath+'/'+ tag['name'],setEnabled, recurse = True)
	
	
##@timeit
#@error_log
##@dump_args	
#def disableArea(tagPath, setEnabled, recurse=False):
#	""" Disables area in [default] tag provider
#		TODO: None
#		Args: tagPath as string, setEnabled as bit, recurse as bool
#		Returns: None    
#		Testing: (script console)
#			mes.config.tag.disableArea(tagPath, setEnabled, recurse=False)
#		Runtime: .124
#	"""
#	tagPath = tagPath
#	collisionPolicy = "o" # "a" == abort, "o" == overwrite
#	configs = system.tag.getConfiguration(tagPath, True)
#	for tag in configs[0]['tags']:
#		if str(tag['tagType']) != 'Folder':	    
#			system.tag.writeAsync(tagPath+'/'+tag['name']+".Enabled", setEnabled)
#		elif str(tag['tagType']) == 'Folder' and recurse ==True:
#			mes.config.tag.disableLine(tagPath+'/'+ tag['name'],setEnabled)
#
#
#
#@timeit
@error_log
#@dump_args
def disableCell(tagPath,setEnabled, recurse=False):
	""" Disables cell in [default] tag provider
		TODO: None
		Args: tagPath as string, tagName as string
		Returns: None    
		Testing: (script console)
			mes.config.sp.disableCell(tagPath, tagName)
		Runtime: .001
	"""
	system.tag.writeAsync(tagPath+".Enabled", setEnabled)
#
#
##@timeit
#@error_log
##@dump_args
#def disableEnterprise(tagPath,setEnabled, recurse=False):
#	""" Disables a enterprise in [default] tag provider
#		TODO: None
#		Args: tagPath as string, setEnabled as bit, recurse as bool
#		Returns: None    
#		Testing: (script console)
#			mes.config.sp.disableSite(tagPath, recurse)
#		Runtime: .439 (recursion)
#	"""
#	tagPath = tagPath
#	collisionPolicy = "o" # "a" == abort, "o" == overwrite
#	configs = system.tag.getConfiguration(tagPath, True)
#	for tag in configs[0]['tags']:
#		if str(tag['tagType']) != 'Folder':	      
#			system.tag.writeAsync(tagPath+'/'+tag['name']+".Enabled", setEnabled)
#		elif str(tag['tagType']) == 'Folder' and recurse == True:
#			mes.config.tag.disableSite(tagPath+'/'+ tag['name'],setEnabled,True)
#
#
#
#
#@timeit
#@error_log
##@dump_args
#def disableLine(tagPath, setEnabled,recurse=False):
#	""" Disables line in [default] tag provider
#		TODO: None
#		Args: tagPath as string, setEnabled as bit, recurse as bool (unused)
#		Returns: None    
#		Testing: (script console)
#			mes.config.sp.disableLine(tagPath, setEnabled,recurse=False)
#		Runtime: .122
#	"""
#	collisionPolicy = "o" # "a" == abort, "o" == overwrite
#	configs = system.tag.getConfiguration(tagPath, True)
#	for tag in configs[0]['tags']:
#		if str(tag['tagType']) != 'Folder':	      
#			system.tag.writeAsync(tagPath+'/'+tag['name']+".Enabled", setEnabled)
#
#
#
#
##@timeit
#@error_log
##@dump_args
#def disableSite(tagPath, setEnabled, recurse=False):
#	""" Disables a site in [default] tag provider
#		TODO: None
#		Args: tagPath as string, setEnabled as bit, recurse as bool
#		Returns: None    
#		Testing: (script console)
#			mes.config.sp.disableSite(tagPath, recurse)
#		Runtime: .373 (recursion)
#	"""
#	collisionPolicy = "o" # "a" == abort, "o" == overwrite
#	configs = system.tag.getConfiguration(tagPath, True)
#	for tag in configs[0]['tags']:
#		if str(tag['tagType']) != 'Folder':
#			system.tag.writeAsync(tagPath+'/'+tag['name']+".Enabled", setEnabled)
#		elif str(tag['tagType']) == 'Folder' and recurse == True:
#			mes.config.tag.disableArea(tagPath+'/'+ tag['name'],setEnabled,True)

# @timeit
@error_log
# @dump_args
def editCell(params):
	""" 
	    Edits an existing Cell's parameters
	    Args:
	        params (dict): A dictionary with the following keys:
	            - EqPath (str): The path of the asset being updated.
	            - parameters (dict): a dictionary with the following keys:
	            	- server (str): server the tag is to be stored on
		            - fault (str): 
		            - state (str): 
		            - device (str):		            
	    Returns: 
	        True if the asset is successfully Edited.
	        Raises an exception on error
	    Usage: 
	        Call this function in the Ignition script console using the following syntax:
	        mes.config.tag.editCell(params)
    """
	try:
		tagPath = params['EqPath']
		paths = [
		    '{}/Parameters/server'.format(tagPath),
		    '{}/Parameters/line'.format(tagPath),
		    '{}/Parameters/fault'.format(tagPath),
		    '{}/Parameters/state'.format(tagPath)
		]
		values = [
		    params['Parameters']['server'],
		    params['Parameters']['line'],
		    params['Parameters']['fault'],
		    params['Parameters']['state']
		]
		system.tag.writeBlocking(paths, values)
		return True
	except Exception as e:
		raise ValueError("Unexpected error occurred: {}".format(e))

# @timeit
@error_log
# @dump_args
def editInput(params):
	""" 
	    Edits an existing machineInput's parameters
	    Args:
	        params (dict): A dictionary with the following keys:
	            - EqPath (str): The path of the asset being updated.
	            - parameters (dict): a dictionary with the following keys:
	            	- server (str): server the tag is to be stored on
		            - fault (str): 
		            - infeed (str): 
		            - outfeed (str):
		            - reject (str): 
		            - device (str):
	    Returns: 
	        True if the asset is successfully Edited.
	        Raises an exception on error
	    Usage: 
	        Call this function in the Ignition script console using the following syntax:
	        mes.config.tag.editInput(params)
    """
	try:
		tagPath = params['EqPath']
		paths = [
		    '{}/machineInput/Parameters/server'.format(tagPath),
		    '{}/machineInput/Parameters/device'.format(tagPath),
		    '{}/machineInput/Parameters/fault'.format(tagPath),
		    '{}/machineInput/Parameters/infeed'.format(tagPath),
		    '{}/machineInput/Parameters/outfeed'.format(tagPath),
		    '{}/machineInput/Parameters/reject'.format(tagPath)
		]
		values = [
		    params['Parameters']['server'],
		    params['Parameters']['device'],
		    params['Parameters']['fault'],
		    params['Parameters']['infeed'],
		    params['Parameters']['outfeed'],
		    params['Parameters']['reject']
		]
		system.perspective.print(paths)
		system.perspective.print(values)
		system.tag.writeBlocking(paths, values)
		return True
	except Exception as e:
		raise ValueError("Unexpected error occurred: {}".format(e))

# @timeit
@error_log
# @dump_args
def editOutput(params):
	""" 
	    Edits an existing machineOutput's parameters
	    Args:
	        params (dict): A dictionary with the following keys:
	            - EqPath (str): The path of the asset being updated.
	            - parameters (dict): a dictionary with the following keys:
	            	- server (str): server the tag is to be stored on
		            - mode (str): 
		            - state (str): 
		            - device (str):		            
	    Returns: 
	        True if the asset is successfully Edited.
	        Raises an exception on error
	    Usage: 
	        Call this function in the Ignition script console using the following syntax:
	        mes.config.tag.editOutput(params)
	"""
	try:
		tagPath = params['tagPath']
		paths = [
		    '{}/server'.format(tagPath),
		    '{}/device'.format(tagPath),
		    '{}/mode'.format(tagPath),
		    '{}/state'.format(tagPath)
		]
		values = [
		    params['Parameters']['server'],
		    params['Parameters']['device'],
		    params['Parameters']['mode'],
		    params['Parameters']['state']
		]
		system.tag.writeBlocking(paths, values)
		return True
	except Exception as e:
		raise ValueError("Unexpected error occurred: {}".format(e))