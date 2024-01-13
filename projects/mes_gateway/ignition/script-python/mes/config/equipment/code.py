"""
This contains all event trigger functions


"""
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders
from java.awt import Color
#import json


sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.config.equipment')


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     EXAMPLE FUNCTION
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#@timeit
#@error_log
#@dump_args
#def exampleFunction(arg1):
#	""" Description of function purpose
#		Args:
#		  	data (data prop): description of argument
#		Returns:
#			(type): description of argument
#		Testing: (script console)
#			system.downtime.periodic.exampleFunction(arg1)
#		TODO:
#			_ - Finish adding ______
#	"""
#	# Write back to [MES] tag provider with equipment path
#	pass



#perspectiveTreeViewJSONModel = [
#  {
#    "label": "Enterpris",
#    "expanded": true,
#    "data": {},
#    "items": [
#      {
#        "label": "Site",
#        "expanded": true,
#        "data": {},
#        "items": [
#          {
#            "label": "Area",
#            "expanded": true,
#            "data": {},
#            "items": [
#              {
#                "label": "Line",
#                "expanded": false,
#                "data": {
#                  "eqObjectType": "Line",
#                  "eqPath": "Line",
#                  "eqUUID": "a289d6c8-6aa4-43de-89be-6d61dc3e9cbc"
#                },
#                "items": []
#              }
#            ]
#          },
#        ]
#      }
#    ]
#  }
#]

#@timeit
@error_log
#@dump_args
def buildProductionModel():
	""" 
		Gets Top5 DT DS for each line and returns it as larger dataset
		Args:
		Returns: List of AreaIDs for iterating
		Testing:
			print(mes.config.equipment.buildProductionModel())
	"""
	
	headers = [
	    'path', 'text', 'icon', 'background', 'foreground', 'tooltip',
	    'border', 'selectedText', 'selectedIcon', 'selectedBackground',
	    'selectedForeground', 'selectedToolTip', 'selectedBorder'
	]
	
	query = '''
			SELECT * FROM config.vw_productionModel
			'''
	
	#data = system.db.runQuery(query, db)
	
	#Convert Query into JSON
	jsonDataset = gpa.data.datasetToJson(system.db.runQuery(query, db))
	
	print(jsonDataset)
	
	result = []
	
	for data in jsonDataset:
	    enterprise = data['enterprise']
	    enterpriseEnabled = data['enterpriseEnabled']
	    enterpriseID = data['enterpriseID']
	    site = data['site']
	    sitePath = data['sitePath']
	    siteID = data['siteID']
	    siteEnabled = data['siteEnabled']
	    area = data['area']
	    areaPath = data['areaPath']
	    areaID = data['areaID']
	    areaEnabled = data['areaEnabled']
	    line = data['line']
	    linePath = data['linePath']
	    lineID = data['lineID']
	    lineEnabled = data['lineEnabled']
	    cellID = data['cellID']
	    cell = data['cell']
	    cellEnabled = data['cellEnabled'] # only use this if the cell ID is not null
	
	    # Check if enterprise exists in the result
	    enterprise_dict = next((item for item in result if item['label'] == enterprise), None)
	    
	    #if not enterpriseEnabled: pass #Do stuff
	
	    if enterprise_dict is None:
	    	if enterpriseEnabled:
		        enterprise_dict = {
		            "label": enterprise,
		            "icon": {"path": "material/business","color": "","style": {}},
	                "data": {"EqType": "enterprise","EqName":enterprise, "EqPath": enterprise,"EqID": enterpriseID,"EqEnabled":enterpriseEnabled},
		            "expanded": True,
		            "items": []
		        }
	        else:
	        	enterprise_dict = {
		            "label": enterprise,
		            "icon": {"path": "material/block","color": "var(--error)","style": {}},
	                "data": {"EqType": "enterprise","EqName":enterprise, "EqPath": enterprise,"EqID": enterpriseID,"EqEnabled":enterpriseEnabled},
		            "expanded": True,
		            "items": []
		        }
	        result.append(enterprise_dict)
	
	    # Find or create the site dictionary
	    site_dict = next((item for item in enterprise_dict['items'] if item['label'] == site), None)
	
	    if site_dict is None:
	    	if siteEnabled:
		        site_dict = {
		            "label": site,
		            "icon": {"path": "material/location_city","color": "","style": {}},
	                "data": {"EqType": "site","EqName":site, "EqPath": sitePath,"EqID": siteID,"EqEnabled":siteEnabled},
		            "expanded": True,
		            "items": []
		        }
	        else:
		        site_dict = {
		            "label": site,
		            "icon": {"path": "material/block","color": "var(--error)","style": {}},
	                "data": {"EqType": "site","EqName":site, "EqPath": sitePath,"EqID": siteID,"EqEnabled":siteEnabled},
		            "expanded": False,
		            "items": []
		        }
	        enterprise_dict['items'].append(site_dict)
	
	    # Find or create the area dictionary
	    area_dict = next((item for item in site_dict['items'] if item['label'] == area), None)
	
	    if area_dict is None:
	    	if areaEnabled:
		        area_dict = {
		            "label": area,
		            "icon": {"path": "material/business_center","color": "","style": {}},
		            "data": {"EqType": "area","EqName":area,"EqPath": areaPath,"EqID": areaID,"EqEnabled":areaEnabled},
		            "expanded": True,
		            "items": []
		    	}
	    	else:
	        	area_dict = {
		            "label": area,
		            "icon": {"path": "material/block","color": "var(--error)","style": {}},
		            "data": {"EqType": "area","EqName":area, "EqPath": areaPath,"EqID": areaID,"EqEnabled":areaEnabled},
		            "expanded": False,
		            "items": []
		        }
        	site_dict['items'].append(area_dict)
	
	    # Find or create the line dictionary
	    line_dict = next((item for item in area_dict['items'] if item['label'] == line), None)
	
	    if line_dict is None:
	    	if lineEnabled:
		        line_dict = {
		            "label": line,
		            "icon": {"path": "material/line_style","color": "","style": {}},
		          	"data": {"EqType": "line","EqName":line, "EqPath": linePath,"EqID": lineID,"EqEnabled":lineEnabled},
		            "expanded": False,
		            "items": []
		        }
	        else:
	        	line_dict = {
		            "label": line,
		            "icon": {"path": "material/block","color": "var(--error)","style": {}},
		          	"data": {"EqType": "line","EqName":line, "EqPath": linePath,"EqID": lineID,"EqEnabled":lineEnabled},
		            "expanded": False,
		            "items": []
		        }
	        area_dict['items'].append(line_dict)
	
	    # Add cell dictionary if cell is not None
	    if cell is not None:
	    	if cellEnabled:
		        cell_dict = {
		            "label": cell,
		            "icon": {"path": "material/apartment","color": "","style": {}},
		            "data": {"EqType": "cell","EqName":cell, "EqPath": linePath+'/'+cell,"EqID": cellID,"EqEnabled":cellEnabled},
		            "expanded": False,
		            "items": []
		        }
	        elif not cellEnabled and cellEnabled is not None:
	        	cell_dict = {
		            "label": cell,
		            "icon": {"path": "material/block","color": "var(--error)","style": {}},
		            "data": {"EqType": "cell","EqName":cell, "EqPath": linePath+'/'+cell,"EqID": cellID,"EqEnabled":cellEnabled},
		            "expanded": False,
		            "items": []
		        }
	        line_dict['items'].append(cell_dict)
	#print result
	return result

 #material/vpn_key
######################################################### Add Item ########################################################


#@timeit
@error_log
#@dump_args
def assetAdd(params):
	""" 
	    Adds a new asset to the system under a specific parent.
	    Args:
	        params (dict): A dictionary with the following keys:
	            - EqEnabled (bool): Whether the asset is enabled.
	            - EqID (int): The ID of the parent of the asset being created.
	            - EqPath (str): The path to the parent of the asset being created.
	            - EqType (str): The type of the parent of the asset being created. Should be one of ('site', 'area', 'line', 'cell').
	            - AssetName (str): The name of the asset to be created.
	    Returns: 
	        True if the asset is successfully created. 
	        If an exception occurs, it returns the string representation of the exception.
	    Usage: 
	        Call this function in the Ignition script console using the following syntax:
	        print(mes.config.sp.assetAdd(params))
    """
#params={
#  "EqEnabled": true,
#  "EqID": 4,
#  "EqPath": "Enterprise/Site/Area",
#  "EqType": "line",
#  "EqName": "Line"
#}

	# EqPath is the parent path of the object that we need to create 
	#	IE we need to make a child object, If EqPath

	try:
		if params["EqPath"] == "": 
#			system.perspective.print('Enterprise')
			mes.config.tag.createEnterpriseTags(params['AssetName']) #Passing new Name for Top level Tag
			mes.config.sp.addEnterprise(params['AssetName']) #Passing new Name for Top level asset
			return True
		else: # We have a Enterprise use EqType
			if params["EqType"] == "enterprise": #Create Site 
				# Generate DB entry for the item
#				system.perspective.print('Site')
				mes.config.sp.addSite(params['EqID'], params['AssetName']) #EqID being selected Enterprise ID here
				mes.config.tag.createSiteTags(params['EqPath'] + '/' + params['AssetName'])
				return True
			elif params["EqType"] == "site": #Create Area
				# Generate DB entry for the item
#				system.perspective.print('Area')
				res = mes.config.sp.addArea(params['EqID'], params['AssetName']) #EqID being selected Site ID here
				if res != 'Success':
					return res
				else: 	
					mes.config.tag.createAreaTags(params['EqPath'] + '/' + params['AssetName'])
					return True
			elif params["EqType"] == "area": 
				# Generate DB entry for the item
#				system.perspective.print('Line')
				mes.config.sp.addLine(params['EqID'], params['AssetName']) #EqID being selected Area ID here
				mes.config.tag.createLineTags(params['EqPath'] + '/' + params['AssetName'])
				return True
			elif params["EqType"] == "line": 
				# Generate DB entry for the item
#				system.perspective.print('Cell')
				mes.config.sp.addCell(params['EqID'], params['AssetName']) #EqID being selected Line ID here
				mes.config.tag.createCellTags(params['EqPath'], params['AssetName'])
				return True
	except Exception as e:
		return str(e)


##@timeit
#@error_log
##@dump_args
#def assetDelete(selectedPath, assetName, params):
#	""" 
#		Gets Top5 DT DS for each line and returns it as larger dataset
#		Args:
#			selectedPath (string): path to parent item
#			assetName (string): name of asset to create
#			params (dicitonary): list of items from selected parent
#		Returns: List of AreaIDs for iterating
#		Testing:
#			print(mes.config.tag.createEquipmentFolder(path, name))
#	"""
#
#	if params["EqPath"] == "": mes.config.tag.createEnterpriseTags("") #No Enterprise Exists
#	else: # We have a Enterprise use EqType
#		if params["EqType"] == "site": 
#			# Generate DB entry for the item
#			# mes.config.sp.createSite(selectedPath, assetName)
#			mes.config.tag.createSiteTags(selectedPath, assetName)
#		elif params["EqType"] == "area": 
#			# Generate DB entry for the item
#			# mes.config.sp.createArea(selectedPath, assetName)
#			mes.config.tag.createAreaTags(selectedPath, assetName)
#		elif params["EqType"] == "line": 
#			# Generate DB entry for the item
#			# mes.config.sp.createLine(selectedPath, assetName)
#			mes.config.tag.createLineTags(selectedPath, assetName)
#		elif params["EqType"] == "cell": 
#			# Generate DB entry for the item
#			# mes.config.sp.createCell(selectedPath, assetName)
#			mes.config.tag.createCellTags(selectedPath, assetName)

#@timeit
@error_log
#@dump_args
def assetDisable(params):
    """
        Disables/Enables equipment
        Args:
            params (dict): A dictionary with the following keys:
                - EqEnabled (bool): current enabled value of the equipment
                - EqID (int): equipment ID of the selected equipment
                - EqPath (str): the path of the selected equipment
                - EqType (str): type that determines which version of disable to run
                - EqName (str): name of the equipment to be modified (unused)
                - Enable (bit): Toggles the enabled property of the equipment
                - recurse (bool): determines whether child components are to be disabled.
        Returns: 
            True if the asset is successfully Edited.
            False if the asset is unsupported for editing or any error occurs
    """
    try:
        eq_path = params["EqPath"]
        
        if eq_path == "": 
            mes.config.sp.setEquipmentEnable(params["EqID"], 'enterprise', params['Enable'])
            mes.config.tag.disableEnterprise(params['EqPath'], params['Enable'])
            return True
        else: 
            eq_type = params["EqType"]
            valid_types = {"site", "area", "line", "enterprise"}

            if eq_type == 'cell':
                mes.config.sp.setEquipmentEnable(params["EqID"], eq_type, params['Enable'])
                mes.config.tag.disableCell(params['EqPath'], params['Enable'])
                return True
            elif eq_type in valid_types:
                mes.config.sp.setEquipmentEnable(params["EqID"], eq_type, params['Enable'])
                mes.config.tag.disableEq(params['EqPath'], params['Enable'], params)
                return True
            else:
                return "Unsupported EqType: " + str(eq_type)
    except KeyError as key_error:
        return "KeyError: {}. Please ensure 'params' dictionary contains correct keys.".format(key_error)
    except ValueError as value_error:
        return "ValueError: {}. Please ensure 'EqType' is one of the following: 'site', 'area', 'line', 'cell'.".format(value_error)
    except Exception as e:
        return "Unexpected error occurred: {}".format(e)
       

#@timeit
@error_log
#@dump_args
def assetEdit(params):
    """ 
        Edits an existing asset's parameters.
        Args:
            params (dict): A dictionary with the following keys:
                - EqPath (str): The path of the asset being updated.
                - EqType (str): Possible values: 'cell', 'line', 'area'
                - EqName (str): The device name
                - parameters (dict): A dictionary with the following keys:
                    - server (str): Server the tag is to be stored on
                    - fault (str): Only used for 'machineInput' and 'cell'
                    - state (str): Only used for 'machineOutput' and 'cell'
                    - mode (str): Only used for 'machineOutput'
                    - infeed (str): Only used for 'machineInput'
                    - outfeed (str): Only used for 'machineInput'
                    - reject (str): Only used for 'machineInput'
        Returns: 
            True if the asset is successfully edited.
            An error message if the asset is unsupported for editing or an error occurred.
    """
    eqType = params['EqType']
    
    if eqType == 'cell':
        return mes.config.tag.editCell(params)
    elif eqType == 'line' and params['SelectedUDT'] == 'machineInput':
        mes.config.tag.editInput(params)
        return True
    elif eqType == 'line' and params['SelectedUDT'] == 'machineOutput':
        mes.config.tag.editOutput(params)
        return True
    else:
    	raise ValueError("Unsupported EqType: " + eqType)


#@timeit
@error_log
#@dump_args
def deleteEquipment(params):
	eqType = params['EqType']
	
	




#def assetDisable(params):
#	""" 
#		Gets Top5 DT DS for each line and returns it as larger dataset
#		Args:
#			selectedPath (string): path to parent item
#			assetName (string): name of asset to create
#			params (dicitonary): list of items from selected parent
#		Returns: List of AreaIDs for iterating
#		Testing:
#			print(mes.config.tag.createEquipmentFolder(path, name))
#	"""
#
#	try:
#		eq_path = params["EqPath"]
#		#print("EqPath: ", eq_path)  # Debugging line
#		
#		if eq_path == "": 
#			#print("Disabling Enterprise")  # Debugging line
#			mes.config.sp.disableEnterprise(params["EqID"])
#			mes.config.tag.disableEnterprise(params['EqPath'])
#		else: 
#			eq_type = params["EqType"]
#			#print("EqType: ", eq_type)  # Debugging line
#			valid_types = {"site", "area", "line", "cell"}
#			if eq_type in valid_types:
#			#	print("Disabling {}".format(eq_type.capitalize()))  # Debugging line
#				getattr(mes.config.sp, 'disable' + eq_type.capitalize())(params["EqID"])
#				getattr(mes.config.tag, 'disable' + eq_type.capitalize())(params['EqPath'])
#				return True
#			else:
#				raise ValueError("Unsupported EqType: " + eq_type)
#				return False
#	except KeyError as key_error:
#	    print("KeyError: {}. Please ensure 'params' dictionary contains correct keys.".format(key_error))
#	except ValueError as value_error:
#		print("ValueError: {}. Please ensure 'EqType' is one of the following: 'site', 'area', 'line', 'cell'.".format(value_error))
#	except Exception as e:
#		print("Unexpected error occurred: {}".format(e))

#
##@timeit
#@error_log
##@dump_args
#def assetMove(selectedPath, assetName, params):
#	""" 
#		Gets Top5 DT DS for each line and returns it as larger dataset
#		Args:
#			selectedPath (string): path to parent item
#			assetName (string): name of asset to create
#			params (dicitonary): list of items from selected parent
#		Returns: List of AreaIDs for iterating
#		Testing:
#			print(mes.config.tag.createEquipmentFolder(path, name))
#	"""
#
#	if params["EqPath"] == "": mes.config.tag.createEnterpriseTags("") #No Enterprise Exists
#	else: # We have a Enterprise use EqType
#		if params["EqType"] == "site": 
#			# Generate DB entry for the item
#			# mes.config.sp.createSite(selectedPath, assetName)
#			mes.config.tag.createSiteTags(selectedPath, assetName)
#		elif params["EqType"] == "area": 
#			# Generate DB entry for the item
#			# mes.config.sp.createArea(selectedPath, assetName)
#			mes.config.tag.createAreaTags(selectedPath, assetName)
#		elif params["EqType"] == "line": 
#			# Generate DB entry for the item
#			# mes.config.sp.createLine(selectedPath, assetName)
#			mes.config.tag.createLineTags(selectedPath, assetName)
#		elif params["EqType"] == "cell": 
#			# Generate DB entry for the item
#			# mes.config.sp.createCell(selectedPath, assetName)
#			mes.config.tag.createCellTags(selectedPath, assetName)
#
#
#
##@timeit
#@error_log
##@dump_args
#def assetUpdate(selectedPath, assetName, params):
#	""" 
#		Gets Top5 DT DS for each line and returns it as larger dataset
#		Args:
#			selectedPath (string): path to parent item
#			assetName (string): name of asset to create
#			params (dicitonary): list of items from selected parent
#		Returns: List of AreaIDs for iterating
#		Testing:
#			print(mes.config.tag.createEquipmentFolder(path, name))
#	"""
#
#	if params["EqPath"] == "": mes.config.tag.createEnterpriseTags("") #No Enterprise Exists
#	else: # We have a Enterprise use EqType
#		if params["EqType"] == "site": 
#			# Generate DB entry for the item
#			# mes.config.sp.createSite(selectedPath, assetName)
#			mes.config.tag.createSiteTags(selectedPath, assetName)
#		elif params["EqType"] == "area": 
#			# Generate DB entry for the item
#			# mes.config.sp.createArea(selectedPath, assetName)
#			mes.config.tag.createAreaTags(selectedPath, assetName)
#		elif params["EqType"] == "line": 
#			# Generate DB entry for the item
#			# mes.config.sp.createLine(selectedPath, assetName)
#			mes.config.tag.createLineTags(selectedPath, assetName)
#		elif params["EqType"] == "cell": 
#			# Generate DB entry for the item
#			# mes.config.sp.createCell(selectedPath, assetName)
#			mes.config.tag.createCellTags(selectedPath, assetName)
#