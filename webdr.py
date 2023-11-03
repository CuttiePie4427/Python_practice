# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from bs4 import BeautifulSoup

import time

driverPath = f"C:\chrome\chromedriver.exe"



driver = webdriver.Chrome()

driver.implicitly_wait(3)

driver.get('https://tw.buy.yahoo.com/search/product?p=iphone')

for i in range(1):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    
soup = BeautifulSoup(driver.page_source,'html.parser')    

goods = soup.find('div',{'class':'ResultList_resultList_IpWJt'})


items = goods.find_all('a')

for row in items:
    link = row.get('href')
    title = row.find('span',class_='sc-1d7r8jg-0 sc-dp9751-0 sc-1drl28c-5 czfCFU fUBIAU biZSHp')
    if title != None:
        title = title.text
        price = row.find('span',class_='sc-1d7r8jg-0 sc-dp9751-0 eLSRyH eEsfHX').text
        
        price = price.replace('$','')
        price = price.replace(',','')
        print('商品：',title)
        print('價格：',price)
        print('連結：',link)
        print()
