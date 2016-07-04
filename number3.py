__author__ = 'may'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver =webdriver.Chrome()
driver.get("http://yunpan.360.cn")
right_click=driver.find_element_by_name("password")
ActionChains(driver).context_click(right_click).perform()