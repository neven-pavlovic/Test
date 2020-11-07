import logging
import unittest

from Package_Cheese.tests.test_cheese import CheeseTest
from Package_DemoQA.tests.test_demoqa import DemoQATest
from Package_OrangeHRM.tests.test_orangehrm import OrangeHRMTest

# loading demo qa test
test1 = unittest.TestLoader().loadTestsFromTestCase(DemoQATest)

# loading cheese test
test2 = unittest.TestLoader().loadTestsFromTestCase(CheeseTest)

# loading orange hrm test
test3 = unittest.TestLoader().loadTestsFromTestCase(OrangeHRMTest)

# you can change the parameter of unittest.TestSuite() to list of tests you want to run
testsToRun = unittest.TestSuite([test1, test2, test3])

# setting up how and what to log
# you can change the path to log file, format, date format, and level
logging.basicConfig(filename=r"C:\\Logs\test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d.%m.%Y %I:%M:%S %p')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# running all the tests you want
unittest.TextTestRunner().run(testsToRun)
