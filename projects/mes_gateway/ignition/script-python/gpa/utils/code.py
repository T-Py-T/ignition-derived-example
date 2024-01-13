from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders
import re

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()


htmlPatternBR = re.compile('\<br\>', re.I)
htmlPatternGeneric = re.compile('\<.*?\>', re.I)




#@timeit
@error_log
#@dump_args
def stripHTML(string, handleBreaks=False):
	"""This removes the HTML markup tags from a string.
	Not to be confused with parsing, of which this does *NONE*.
	https://stackoverflow.com/a/1732454
	"""
	if handleBreaks:
		# line breaks are line feeds
		string = htmlPatternBR.sub('\n', string)
		
	# everything else can be stripped
	string = htmlPatternGeneric.sub('', string)
 
	return string


#@timeit
@error_log
#@dump_args	
def clipboard(imagePath):
	from java.awt.datatransfer import StringSelection
	from java.awt.datatransfer import Clipboard
	from java.awt import Toolkit
	from java.awt.datatransfer import DataFlavor
	toolkit = Toolkit.getDefaultToolkit()
	clipboard = toolkit.getSystemClipboard()
	clipboard.setContents(StringSelection(imagePath), None)
	contents = clipboard.getContents(None)
	logger = system.util.getLogger('IntellicInfo')
	content = contents.getTransferData(DataFlavor.stringFlavor)
	logger.infof('Image %s copied to clipboard.  Content = %s',imagePath,content)


#@timeit
@error_log
#@dump_args
def retarget(project):
	system.util.retarget(project)


#@timeit
@error_log
#@dump_args
def translateTable(component, translateColumns = [], locale=None, rawTablePropertyName = 'rawdata', destinationTablePropertyName = 'data'):
	# translate the defect descriptions
	data = getattr(component, rawTablePropertyName)
	
	if not locale:
		locale = system.util.getLocale()
	
	header = [h for h in data.getColumnNames()]
	
	translateColumnIX = [data.getColumnIndex(column) for column in translateColumns]
	
	if data.getRowCount() > 0:
		for rix in range(data.getRowCount()):
			for cix in translateColumnIX:
				entry = data.getValueAt(rix, cix)
				translatedEntry = system.util.translate(entry, locale, False)
				data.setValueAt(rix, cix, translatedEntry)
		
		setattr(component, destinationTablePropertyName, data)
	