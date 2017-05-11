from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://facebook.com")

firstname = driver.find_element_by_name("firstname")
firstname.send_keys("myfirstname")

surname = driver.find_element_by_name("lastname")
surname.send_keys("mysurname")

mobile_number = driver.find_element_by_name("reg_email__")
mobile_number.send_keys("myphonenumber")

new_password = driver.find_element_by_name("reg_passwd__")
new_password.send_keys("mypassword!")

birthday = driver.find_element_by_name("birthday_day")
birthday.send_keys("2")

birthmonth = driver.find_element_by_name("birthday_month")
birthmonth.send_keys("Mar")

birthyear = driver.find_element_by_name("birthday_year")
birthyear.send_keys("1997")

sex = driver.find_element_by_xpath("//input[@value='1']").click()

create_account = driver.find_element_by_name("websubmit").click()






