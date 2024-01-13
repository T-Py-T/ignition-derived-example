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


# @timeit
@error_log
# @dump_args
def validateAllPackages():
    """ Run periodically to validate that all of the mes scripts are working
    Args: None
    Returns:
            (int): 1 if passing, else -1
            WILL TRIGGER ERROR IN LOGS
    Testing:
      print(mes.unitTests.validateAllPackages())		
    """
    # Set comparison bit
    working = 1

    config = mes.unitTests.mesConfigPackage()
    if config != working:
        pass  # logger.error('mes.config failed') #RAISE THE ALARM

    oee = mes.unitTests.mesOEEPackage()
    if oee != working:
        pass  # logger.error('mes.oee failed') #RAISE THE ALARM

    logger.tracef('mes.config passed')
    print('all mes packages passed')
    return 1


# @timeit
@error_log
# @dump_args
def mesConfigPackage():
    """ Checking all functions in the config library
    Args: None
    Returns:
            (int): 1 if passing, else -1
    Testing:
      print(mes.unitTests.mesConfigPackage())		
    """

    # ****************  KNOWN GOOD RETURN  ***********************

    # equipment

    # getConfig

    # sp
    assert mes.config.sp.getCellID(
        'SFN1', 'M1000') > 0, 'Cell ID should be greater than 0'
    assert mes.config.sp.getCellOrder(
        'SFN1', 'M1000') > 0, 'Cell Order should be greater than 0'
    assert mes.config.sp.getLineConfig(
        'SFN1') > 0, 'LineConfig DS should not be empty'
    assert mes.config.sp.getLineCellConfig(
        'SFN1') > 0, 'LineCellConfig DS should not be empty'
    assert mes.config.sp.getLineID(
        'SFN1') > 0, 'Line ID should be greater than 0'

    # tag
    # Testing
    logger.tracef('mes.config passed')
    print('mes.config passed')
    return 1


# @timeit
@error_log
# @dump_args
def mesOEEPackage():
    """ Checking all functions in the config library
    Args: None
    Returns:
            (int): 1 if passing, else -1
    Testing:
      print(mes.unitTests.mesOEEPackage())		
    """

    # ****************  KNOWN GOOD RETURN  ***********************

    # equipment

    # getConfig

    # sp
    assert mes.oee.sp.getPeriodAllLinesOEE_AQP(
        'yesterday', 1) > 0, 'Cell ID should be greater than 0'
    assert mes.oee.sp.getPeriodAreaOEETable(
        'yesterday', 2) > 0, 'Cell Order should be greater than 0'
    assert mes.oee.sp.getPeriodAreaOEE_AQP(
        'yesterday', 1) > 0, 'LineConfig DS should not be empty'


# 	getGroupOEE_AQP(StartDateTime, EndDateTime, GroupID):
# 	getPeriodAllLinesOEE_AQP(TimePeriod, SiteID):
# getPeriodAreaOEE_AQP(TimePeriod, AreaID):
# getPeriodAreaOEETable(TimePeriod, AreaID):

    # tag

    logger.tracef('mes.oee passed')
    print('mes.oee passed')
    return 1
