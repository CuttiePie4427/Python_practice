# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 20:09:00 2023

@author: USER
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time

driverPath ="C:\chrome\chromedriver.exe"
driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://www.kkday.com/zh-tw/city/taitung')

for i in range(5):
    driver.execute_script('latest_more.click()')
    time.sleep(1)
    
soup = BeautifulSoup(driver.page_source,'html.parser')