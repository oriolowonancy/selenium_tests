#test to make facebook posts 
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
#print(driver.username)
time.sleep(35)

statusbox = driver.find_element_by_name("xhpc_message")
statusbox.send_keys("Hi guys!!!")

postbutton = driver.find_element_by_xpath("//*[text()='Post']")
postbutton.click()

driver.close()