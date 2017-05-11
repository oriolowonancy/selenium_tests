from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
try:
	assert "Python" in driver.title
	print(driver.title)
	elem = driver.find_element_by_name("q")
	elem.clear()
	elem.send_keys("pycon")
	elem.send_keys(Keys.RETURN)
	assert "No results found." not in driver.page_source
except AssertionError as e:
	print("I'm here")
driver.close()
