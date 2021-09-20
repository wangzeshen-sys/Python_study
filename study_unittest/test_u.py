import unittest
from study_unittest.test_1.test_1 import *

suite = unittest.TestSuite()

suite.addTest(test_1("test_2"))

runner = unittest.TestRunner()
runner.run()
