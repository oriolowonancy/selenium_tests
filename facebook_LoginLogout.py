#test to login and logout of facebook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://facebook.com")

email = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")

#replace myemail with your original email address
email.send_keys("myemail.com")

#replace mypassword with your original password
password.send_keys("mypassword")

login = driver.find_element_by_id("loginbutton").click()
print(driver.title)
print("Log in successful")

logout1=driver.find_element_by_css_selector("#userNavigationLabel").click()
time.sleep(35)

logout2=driver.find_element_by_xpath("//li[12]/a/span/span").click()
#logout2=driver.find_element_by_id("show_me_how_logout_1").submit()

print("You are logged out")
driver.close()
