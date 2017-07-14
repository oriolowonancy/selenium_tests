from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://demo.secapay.com')
time.sleep(15)

form_input = driver.find_elements_by_tag_name("input")
for input in form_input:
	input_name = input.get_attribute('name')
	if input_name == "first_name" or input_name == "first-name" or input_name == "firstname" or input_name == "f_name" or input_name == "fname" or input_name == "f-name": 
		input.send_keys("Nancy")

	if input_name == "last_name" or input_name == "last-name" or input_name == "lastname" or input_name == "l_name" or input_name == "lname" or input_name == "f-name": 
		input.send_keys("Oriolowo")

	if input_name == "email" or input_name == "e-mail" or input_name == "username": 
		input.send_keys("myemailadd@gmail.com") 

	if input_name == "passwordClone0" or input_name == "password": 
		input.send_keys("nancy123!")

	if input_name == "agree":
		input.click()

	submit = driver.find_element_by_xpath("//button[@type='submit']").click()