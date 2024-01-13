"""
This holds the testing for the scripting to catch any errors.

******  Needs to be put in the save project script to catch before saving. ************
"""
import unittest
# import pytest  # Not available in jython.


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


def testCasesConfig(verboseSetting=2):
    """
    A function used to run the testcases for this library.
    Testresults will be returned to caller
    Parameters
            testcases: A list of the testcases to be executed.
            verboseSetting: Integervalue to be passed on to TextTestRunner
    Raises
            Not implemented
    testing:
            unittesting.config.testCasesConfig(2)
    """

    testCases = [unittesting.config.TestConfigPackage]

    return unittesting.unitTest.unitTestConfig(testCases, verboseSetting)


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
        result = mes.config.sp.getLineCellConfig(
            self.cell_name, self.line_name)
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
