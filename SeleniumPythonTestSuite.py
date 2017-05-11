import unittest
from test_google2 import SearchText
from SeleniumPythonMultipleTests import HomePageTest

#this gets all tests from SearchText and HomePageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

#this creates a test suite that combines search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text])

#run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)