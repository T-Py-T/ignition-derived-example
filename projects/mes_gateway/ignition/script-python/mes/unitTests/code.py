"""
This holds the testing for the scripting to catch any errors.

******  Needs to be put in the save project script to catch before saving. ************
 
"""
from decorators import error_log, timeit, dump_args
from scriptHeaders import ScriptHeaders
import unittest
# import pytest  # Not available in jython.

sh = ScriptHeaders()
NULL = sh.getNull()
dbDateFormat = sh.getDateFormat()
db = sh.getDb()


# %%%%%%% MAIN LOGGER FOR THIS SCRIPT %%%%%%%%%%%
logger = system.util.getLogger('mes.unitTests')

'''
Set global test variables. ********   NEEDS TO BE UPDATED PER SITE *****

'''
g_timePeriod, g_success_int = 'current shift', 1
g_site_name, g_site_id = 'Fiberon', 9
g_area_name, g_area_id = 'PE Extrusion', 9
g_line_name, g_line_id = 'Line 11', 9
g_cell_name, g_cell_id = 'Extruder', 9


def RunAllMESTesting():
    """
    This function is used to run the MES unit tests.

    Use with project save to test MES packages.
    """
    unittest.main()


class TestConfigPackage(unittest.TestCase):
    """
    A test case for the ConfigPackage module.

    This test case includes various test methods to verify the functionality
    of the ConfigPackage module.
    """

    def setUp(self):
        """Set up test fixtures"""
        self.site_name, self.site_id = g_site_name, g_site_id
        self.area_name, self.area_id = g_area_name, g_area_id
        self.line_name, self.line_id = g_line_name, g_line_id
        self.cell_name, self.cell_id = g_cell_name, g_cell_id
        self.timePeriod, self.success_int = g_timePeriod, g_success_int
        # Start of SP section

    def test_getAllCells(self):
        result = mes.config.sp.getAllCells()
        self.assertIsInstance(result, system.dataset.Dataset,
                              'Result should be a Dataset')

    def test_getProductCodes(self):
        result = mes.config.sp.getProductCodes()
        self.assertIsInstance(result, system.dataset.Dataset,
                              'Result should be a Dataset')

    def test_getCellID(self):
        result = mes.config.sp.getCellID(self.cell_name, self.line_name)
        self.assertGreater(result, 0, 'Cell ID should be greater than 0')

    def test_getCellOrder(self):
        result = mes.config.sp.getCellOrder(self.cell_name, self.line_name)
        self.assertGreater(result, 0, 'Cell Order should be greater than 0')

    def test_getLineConfig(self):
        result = mes.config.sp.getLineConfig(self.cell_name, self.line_name)
        self.assertGreater(result, 0, 'LineConfig DS should not be empty')

    def test_getLineCellConfig(self):
        result = mes.config.sp.getLineCellConfig(self.cell_name, self.line_name)
        self.assertGreater(result, 0, 'LineCellConfig DS should not be empty')

    def test_getLineID(self):
        result = mes.config.sp.getLineID(self.cell_name, self.line_name)
        self.assertGreater(result, 0, 'Line ID should be greater than 0')

    def test_getShiftTimes(self):
        result = mes.config.sp.getShiftTimes(self.timePeriod)
        self.assertIsNotNone(result, 'Current Shift should not be None')

    def tearDown(self):
        """Clean up test fixtures"""
        # If there's anything you need to clean up after your tests, do it here
        pass

class TestOEEPackage(unittest.TestCase):
    """
    Test case for the OEEPackage class.
    """

    def setUp(self):
        """Set up test fixtures"""
        self.site_name, self.site_id = g_site_name, g_site_id
        self.area_name, self.area_id = g_area_name, g_area_id
        self.line_name, self.line_id = g_line_name, g_line_id
        self.cell_name, self.cell_id = g_cell_name, g_cell_id
        self.timePeriod, self.success_int = g_timePeriod, g_success_int

    # *************   Start of Calcs section  *************
    def test_getGroupOEE_AQP(self):
        result = mes.oee.calcs.updateAllAreaOEE_table(g_timePeriod)
        self.assertEqual(result, self.success_int,
                         'update all area oee failed')

    def test_getGroupOEE_AQP(self):
        result = mes.oee.calcs.updateAllLinesOEE_AQP(g_timePeriod)
        self.assertEqual(result, self.success_int,
                         'update all lines oee failed')

    def test_getGroupOEE_AQP(self):
        result = mes.oee.calcs.updateAllAreaOEE_table(g_timePeriod)
        self.assertEqual(result, self.success_int,
                         'update all area oee table failed')

    def test_getGroupOEE_AQP(self):
        result = mes.oee.calcs.updateAllSiteAreasOEE_AQP(g_timePeriod)
        self.assertEqual(result, self.success_int,
                         'update all sitesareas oee failed')

    # *************   Start of Periodic section  *************
    def test_getAllLinesOEE_AQP(self):
        result = mes.oee.periodic.getAllLinesOEE_AQP(g_timePeriod, g_site_id)
        self.assertEqual(result, self.success_int,
                         'getAllLinesOEE_AQP failed')

    def test_getOEE_AQP(self):
        result = mes.oee.periodic.getOEE_AQP(g_timePeriod, g_site_id)
        self.assertEqual(result, self.success_int,
                         'getOEE_AQP failed')

    def test_getOEETable(self):
        result = mes.oee.periodic.getOEETable(g_timePeriod, g_site_id)
        self.assertEqual(result, self.success_int,
                         'getOEETable failed')

    def test_writeOEE_AQP(self):
        result = mes.oee.periodic.writeOEE_AQP(g_timePeriod, g_site_id)
        self.assertEqual(result, self.success_int,
                         'writeOEE_AQP failed')

    def test_writeGetOEETable(self):
        result = mes.oee.periodic.writeOEETable(g_timePeriod, g_site_id)
        self.assertEqual(result, self.success_int,
                         'writegetOEETable failed')

    # *************   Start of SP section  *************
    # def test_getGroupOEE_AQP(self):
    #     result = mes.oee.sp.getGroupOEE_AQP()
    #     self.assertIsInstance(result, system.dataset.Dataset, 'Result should be a Dataset')

    def test_getPeriodAllLinesOEE_AQP(self):
        result = mes.oee.sp.getPeriodAllLinesOEE_AQP('current shift', g_site_id)
        self.assertIsInstance(result, system.dataset.Dataset,
                              'Result should be a Dataset')

    def test_getPeriodAreaOEE_AQP(self):
        result = mes.oee.sp.getPeriodAreaOEE_AQP(
            'current shift', g_area_id, g_site_id)
        self.assertIsInstance(result, system.dataset.Dataset,
                              'Result should be a Dataset')

    def test_getPeriodAreaOEETable(self):
        result = mes.oee.sp.getPeriodAreaOEETable(
            'current shift', g_area_id, g_site_id)
        self.assertIsInstance(result, system.dataset.Dataset,
                              'Result should be a Dataset')

    def test_getPeriodSiteOEE_AQP(self):
        result = mes.oee.sp.getPeriodSiteOEE_AQP('current shift', g_site_id)
        self.assertIsInstance(result, system.dataset.Dataset,
                              'Result should be a Dataset')

    def tearDown(self):
        """Clean up test fixtures"""
        # If there's anything you need to clean up after your tests, do it here
        pass
        


# *** WE DONT USE "MAIN" in Jython has to be called manually (event)
# if __name__ == '__main__':
#     unittest.main()

""" 
******* ORIGINAL CODE KEPT FOR CONTINUITY ********


"""


# class TestAllPackages(unittest.TestCase):
#     @error_log
#     def test_validateAllPackages(self):
#         """ Run periodically to validate that all of the mes scripts are working
#         Args: None
#         Returns:
#             (int): 1 if passing, else -1
#             WILL TRIGGER ERROR IN LOGS
#         Testing:
#           print(mes.unitTests.validateAllPackages())
#         """
#         # Set comparison bit
#         working = 1

#         config = mesConfigPackage()
#         self.assertEqual(config, working, 'mes.config failed')

#         logger.tracef('mes.config passed')
#         oee = mesOEEPackage()
#         self.assertEqual(oee, working, 'mes.oee failed')


#         logger.tracef('All mes packages passed')
#         print('All mes packages passed')

# #@timeit
# @error_log
# #@dump_args
# def mesConfigPackage():
# 	""" Checking all functions in the config library
# 	Args: None
# 	Returns:
# 		(int): 1 if passing, else -1
# 	Testing:
# 	  print(mes.unitTests.mesConfigPackage())
# 	"""

# 	# ****************  KNOWN GOOD RETURN  ***********************

#  	# sp
# 	assert mes.config.sp.getCellID('SFN1','M1000') > 0, 'Cell ID should be greater than 0'
# 	assert mes.config.sp.getCellOrder('SFN1','M1000') > 0, 'Cell Order should be greater than 0'
# 	assert mes.config.sp.getLineConfig('SFN1') > 0, 'LineConfig DS should not be empty'
# 	assert mes.config.sp.getLineCellConfig('SFN1') > 0, 'LineCellConfig DS should not be empty'
# 	assert mes.config.sp.getLineID('SFN1') > 0, 'Line ID should be greater than 0'

# 	#Testing
# 	logger.tracef('mes.config passed')
# 	print('mes.config passed')
# 	return 1


# #@timeit
# @error_log
# #@dump_args
# def mesOEEPackage():
# 	""" Checking all functions in the config library
# 	Args: None
# 	Returns:
# 		(int): 1 if passing, else -1
# 	Testing:
# 	  print(mes.unitTests.mesOEEPackage())
# 	"""

# 	# ****************  KNOWN GOOD RETURN  ***********************

#  	# sp
# 	assert mes.oee.sp.getPeriodAllLinesOEE_AQP('yesterday', 1) > 0, 'Cell ID should be greater than 0'
# 	assert mes.oee.sp.getPeriodAreaOEETable('yesterday', 2) > 0, 'Cell Order should be greater than 0'
# 	assert mes.oee.sp.getPeriodAreaOEE_AQP('yesterday', 1) > 0, 'LineConfig DS should not be empty'

# 	logger.tracef('mes.oee passed')
# 	print('mes.oee passed')
# 	return 1