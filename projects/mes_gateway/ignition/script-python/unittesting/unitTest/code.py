import unittest as ut


def unitTestConfig(testCases, verboseSetting):
    """
    Function:
            Run the unit test as passed in the testcases parameter
            All the unit-tests defined for this library can be run using this function.
            The output will be returned.

    Parameters
            testcases: A list of the testcases to be executed.
            verboseSetting: Integervalue to be passed on to TextTestRunner
    Testing:

    """

    suites = []
    for testcase in testCases:
        suites.append(ut.TestLoader().loadTestsFromTestCase(testcase))
    suite = ut.TestSuite(suites)

    output = ut.TextTestRunner(verbosity=verboseSetting).run(suite)

    return output
