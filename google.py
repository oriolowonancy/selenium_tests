from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")

search = driver.find_element_by_xpath("//input[@title='Search']")
search.send_keys('Selenium')
#search.send_keys(Keys.RETURN)
search.submit()

driver.close()
