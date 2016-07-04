__author__ = 'may'
#/usr/bin/env python
# coding =utf-8
from selenium import webdriver
from time import *

driver =webdriver.Chrome()
driver.get("http://mail.163.com")

driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("jhm20009")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("4061738han")
driver.find_element_by_id("dologin").click()
driver.quit()