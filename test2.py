__author__ = 'may'
#/usr/bin/env python
# coding =utf-8
from selenium import webdriver
from time import *

driver =webdriver.Chrome()
driver.get("http://www.yudao.com")

driver.find_element_by_id("query").send_keys("hello")
driver.find_element_by_id("query").submit()