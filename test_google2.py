import unittest
from selenium import webdriver

class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(20)
        inst.driver.maximize_window()

        inst.driver.get("http://www.google.com/")
        inst.driver.title

    def test_search_by_text(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        self.search_field.send_keys("Selenium Webdriver Interview questions")
        self.search_field.submit()

        lists = self.driver.find_elements_by_class_name("r")
        no = len(lists)
        self.assertEqual(15, no, msg = '15 not equal to {}. Failed Assertion!'.format(no))
        print(no)
        print(lists)


    def  test_search_by_name(self): 
        self.search_field = self.driver.find_element_by_name("q")

        self.search_field.send_keys("Python class")
        self.search_field.submit()

        list_new = self.driver.find_elements_by_class_name("r")
        no = len(list_new)
        self.assertEqual(11, no)
        print(no)
        print(list_new)

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.close()

if __name__ == '__main__':
        unittest.main()
