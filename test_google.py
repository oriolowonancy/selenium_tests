import unittest
from selenium import webdriver

class SearchText(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()

		self.driver.get("http://www.google.com/")

	def test_search_by_text(self):
		self.search_field = self.driver.find_element_by_name("q")

		self.search_field.send_keys("Selenium Webdriver Interview questions")
		self.search_field.submit()

		lists = self.driver.find_elements_by_class_name("r")
		no = len(lists)
		self.assertEqual(10, len(lists))
		print(no)
		print(lists)


	def  test_search_by_name(self):	
		self.search_field = self.driver.find_element_by_name("q")

		self.search_field.send_keys("Python class")
		self.search_field.submit()

		list_new = self.driver.find_elements_by_class_name("r")
		no = len(list_new)
		self.assertEqual(11, len(list_new))
		print(no)
		print(list_new)
	
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
		unittest.main()
