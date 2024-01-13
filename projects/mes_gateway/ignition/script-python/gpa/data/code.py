'''
This contains all data conversion functions
'''
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()

logger = system.util.getLogger('gpa.data')


#@timeit
@error_log
#@dump_args
def datasetToJson(dataset):
	# Get the headers from the dataset
	headers = dataset.getColumnNames()
	data = []
	for row in range(dataset.getRowCount()):
		# Initialize each list item, which are dictionaries
		data.append({}) # 
		# Loop over the dataset columns
		for col in range(dataset.getColumnCount()):
			# Get the key or column name
			key = headers[col]
			# Get the value in the cell specified by the row and key
			value = dataset.getValueAt(row,key)
			# Add the value to the json
			data[row][key] = value
	# Return the data in json format
	return data


#@timeit
@error_log
#@dump_args
def jsonToDataset(data,mapping=None):
	if mapping is None:
		mapping = {}
	numHeaders = len(mapping)
	numRows = len(data)
	numCols = 0
	
	keys = []
	if numRows > 1:
		numCols = len(data[0])
		keys = [key for key in data[0]]
	
	newData = []
	for row in data:
		dataRow = []
		for key in keys:
			dataRow.append(row[key])
		newData.append(dataRow)

	for index, key in enumerate(keys):
		keys[index] = mapping.get(key, key)
	
	dataset = system.dataset.toDataSet(keys, newData)
	return dataset

				
#@timeit
@error_log
#@dump_args		
def swapDataKeys(data, mapping):
	newData = []
	for index, row in enumerate(data):
		newData.append({})
		for key in row:
			# Swap the key name with a mapping
			newData[index][mapping.get(key, key)] = row[key]
	# Return the data in json format
	return newData


#@timeit
@error_log
#@dump_args
def swapKeys(data,mapping):
	newData = []
	for index, row in enumerate(data):
		newData.append({})
		for key in row:
			# Swap the key name with a mapping
			newData[index][mapping.get(key, key)] = row[key]
	# Return the data in json format
	return newData


#@timeit
@error_log
#@dump_args
def swapKey(data, oldKey, newKey):
	newData = []
	mapping = {oldKey:newKey}
	for index, row in enumerate(data):
		newData.append({})
		for key in row:
			# Swap the key name with a mapping
			newData[index][mapping.get(oldKey, oldKey)] = row[oldKey]
	# Return the data in json format
	return newData	
