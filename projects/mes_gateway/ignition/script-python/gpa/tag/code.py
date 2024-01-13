from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders
import os
import copy

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()


TAG_TYPE_FOLDER 		= "Folder"
TAG_TYPE_UDT			= "UdtInstance"
TAG_TYPE_TAG			= "AtomicTag"
TAG_TYPE_PROPERTY		= "Property"
DATA_TYPE_STRING		= "String"
DATA_TYPE_BOOLEAN		= "Boolean"
DATA_TYPE_SHORT			= "Int2"
DATA_TYPE_FLOAT			= "Float4"
DATA_TYPE_INT			= "Int4"
DATA_TYPE_DOUBLE		= "Float8"
DATA_TYPE_LONG			= "Int8"
DATA_TYPE_DATASET		= "DataSet"
VALUE_SOURCE_MEMORY		= "memory"
VALUE_SOURCE_OPC		= "opc"
STR_TAGS				= "tags"
STR_TAG_TYPE			= "tagType"
STR_DATA_TYPE			= "dataType"
STR_FULL_PATH			= "fullPath"
STR_PATH				= "path"
STR_ATTRIBUTES			= "attributes"
STR_NAME				= "name"
STR_VALUE				= "value"
STR_VALUE_SOURCE		= "valueSource"
STR_TYPE_ID				= "typeId"
STR_HAS_CHILDREN		= "hasChildren"


#@timeit
@error_log
#@dump_args
def browse(path, recursive=False, writeProperties=True):
	tags = []
	browseResults = system.tag.browse(path=path)
	results = list(browseResults.getResults())
	for index, tag in enumerate(results):
		tagPath = getPath(tag)
		tags.append(tag)
		if isFolder(tag) or isUDT(tag):
			if recursive and (hasChildren(tag) or isProperty(tag)):
				childTags = browse(tagPath, recursive)
				tags += childTags
		elif writeProperties and isTag(tag):
			childTags = browse(tagPath, recursive)
			tags += childTags	
	return tags

#@timeit
@error_log
#@dump_args
def isFolder(tag): return str(getType(tag)) == TAG_TYPE_FOLDER

#@timeit
@error_log
#@dump_args
def isUDT(tag): return str(getType(tag)) == TAG_TYPE_UDT

#@timeit
@error_log
#@dump_args
def isTag(tag):	return str(getType(tag)) == TAG_TYPE_TAG

#@timeit
@error_log
#@dump_args
def isProperty(tag): return str(getType(tag)) == TAG_TYPE_PROPERTY

#@timeit
@error_log
#@dump_args
def getType(tag): return tag.get(STR_TAG_TYPE, None)

	
#@timeit
@error_log
#@dump_args	
def setType(tag, tagType): 
	tag[STR_TAG_TYPE] = tagType
	return None
	
	
#@timeit
@error_log
#@dump_args
def getDataType(tag):	return str(tag.get(STR_DATA_TYPE, None))


#@timeit
@error_log
#@dump_args
def setDataType(tag, dataType):
	tag[STR_DATA_TYPE] = dataType
	return None


#@timeit
@error_log
#@dump_args
def getPath(tag):
	return str(tag.get(STR_FULL_PATH, None))


#@timeit
@error_log
#@dump_args	
def setPath(tag, tagPath):
	tag[STR_FULL_PATH] = tagPath
	return None


#@timeit
@error_log
#@dump_args
def getAttributes(tag): return tag.get(STR_ATTRIBUTES, None)


#@timeit
@error_log
#@dump_args
def setAttributes(tag, attributes):
	tag[STR_ATTRIBUTES] = attributes
	return None


#@timeit
@error_log
#@dump_args
def getName(tag): return str(tag.get(STR_NAME, None))


#@timeit
@error_log
#@dump_args
def setName(tag, name):
	tag[STR_NAME] = name
	return None


#@timeit
@error_log
#@dump_args
def checkValue(tag):
	if STR_VALUE not in tag:
		tag[STR_VALUE] = None
	return None


#@timeit
@error_log
#@dump_args
def getValue(tag): return tag.get(STR_VALUE, None)


#@timeit
@error_log
#@dump_args
def setValue(tag, value):
	tag[STR_VALUE] = value 
	return None


#@timeit
@error_log
#@dump_args
def getValueSource(tag): return tag.get(STR_VALUE_SOURCE, None)


#@timeit
@error_log
#@dump_args
def setValueSource(tag, valueSource):
	tag[STR_VALUE_SOURCE] = valueSource
	return None


#@timeit
@error_log
#@dump_args				
def getTypeId(tag):	return tag.get(STR_TYPE_ID, None)


#@timeit
@error_log
#@dump_args
def setTypeId(tag, typeId):
	tag[STR_TYPE_ID] = typeId
	return None


#@timeit
@error_log
#@dump_args
def hasChildren(tag): return tag.get(STR_HAS_CHILDREN, False)


#@timeit
@error_log
#@dump_args	
def getTags(tag): return tag.get(STR_TAGS, None)


#@timeit
@error_log
#@dump_args
def getTagPaths(tags):
	tagPaths = []
	for tag in tags:
		tagPath = getPath(tag)
		if isProperty(tag):
			index = tagPath.rfind('/')
			tagPath = tagPath[:index] + '.' + tagPath[index+1:]
			
		tagPaths.append(tagPath)
	return tagPaths


#@timeit
@error_log
#@dump_args
def clearTag(tag):
	dataType = getDataType(tag)
	tagPath = getPath(tag)
	checkValue(tag)
	value = None
	
	if dataType in [DATA_TYPE_STRING]:
		value = ''
		setValue(tag, value)
	elif dataType in [DATA_TYPE_INT, DATA_TYPE_FLOAT]:
		value = 0
		setValue(tag, value)
	elif dataType in [DATA_TYPE_BOOLEAN]:
		value = False
		setValue(tag, value)
	elif dataType in [DATA_TYPE_DATASET]:
		oldValue = getValue(tag).value
		if oldValue is not None:
			headers = list(oldValue.getColumnNames())
			data = []
			dataset = system.dataset.toDataSet(headers, data)
			value = dataset
			setValue(tag, value)
	else: 
		value = ''
		setValue(tag, value)
	writeBlocking([tagPath], [value])
	return tag


#@timeit
@error_log
#@dump_args
def clearTags(tags):
	for tag in tags:
		if isTag(tag):
			tag = clearTag(tag)
	return tags


#@timeit
@error_log
#@dump_args
def swapTags(tags1, tags2):
	tagPaths1 = getTagPaths(tags1)
	tagPaths2 = getTagPaths(tags2)
	values1 = readBlocking(tagPaths1)
	values2 = readBlocking(tagPaths2)
	qualities2 = writeBlocking(tagPaths2, values1)
	qualities1 = writeBlocking(tagPaths1, values2)
	return None


#@timeit
@error_log
#@dump_args
def moveTags(fromTags, toTags):
	tagPaths = getTagPaths(fromTags)
	values = readBlocking(tagPaths)
	tagPaths = getTagPaths(toTags)
	qualities = writeBlocking(tagPaths, values)
	return None


#@timeit
@error_log
#@dump_args
def moveTagsValues(fromTags, toTags):
	tagPaths = getTagPaths(fromTags)
	values = readValuesBlocking(tagPaths)
	tagPaths = getTagPaths(toTags)
	qualities = writeBlocking(tagPaths, values)
	return None


#@timeit
@error_log
#@dump_args
def replace(tags, oldString, newString):
    newTags = []
    for tag in tags:
        newTag = dict(tag)  # Make a copy of the tag dictionary
        tagPath = getPath(newTag)
        tagPath = tagPath.replace(oldString, newString)
        setPath(newTag, tagPath)
        newTags.append(newTag)
    return newTags


#@timeit
@error_log
#@dump_args
def makePath(parentPath, tagName): return "/".join([parentPath, tagName])


#@timeit
@error_log
#@dump_args
def exists(tagPath): return system.tag.exists(tagPath)


#@timeit
@error_log
#@dump_args
def callback(values): return values


#@timeit
@error_log
#@dump_args
def readAsync(tagPaths=[], callback=callback): return system.tag.readAsync(tagPaths=tagPaths, callback=callback)


#@timeit
@error_log
#@dump_args
def readBlocking(tagPaths=[], timeout=45000): return system.tag.readBlocking(tagPaths=tagPaths,timeout=timeout)	 


#@timeit
@error_log
#@dump_args
def readValuesBlocking(tagPaths=[], timeout=45000):
	qvs = system.tag.readBlocking(tagPaths=tagPaths,timeout=timeout)
	values = [qv.value for qv in qvs]
	return values


#@timeit
@error_log
#@dump_args
def writeAsync(tagPaths=[], values=[], callback=callback): return system.tag.writeAsync(tagPaths=tagPaths, values=values, callback=callback)


#@timeit
@error_log
#@dump_args
def writeBlocking(tagPaths=[], values=[], timeout=45000): return system.tag.writeBlocking(tagPaths=tagPaths, values=values, timeout=timeout)