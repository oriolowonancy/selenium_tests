import unittest
import HTMLTestRunner
import os
from test_google2 import SearchText
from SeleniumPythonMultipleTests import HomePageTest

#this gets the directory part to output report file
dir = os.getcwd()

#this gets all tests from SearchText and HomePageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

#this creates a test suite that combines search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text])

#open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "wb")

#configure HTMLTESTRUNNER options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Acceptance Tests')
#runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Acceptance Tests')

#run the suite using HTMLTestRunner
runner.run(test_suite)