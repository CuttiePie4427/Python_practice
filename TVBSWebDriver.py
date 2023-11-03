# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 20:04:54 2023

@author: USER
"""

from selenium import webdriver
from bs4 import BeautifulSoup

import time




driver = webdriver.Chrome()

driver.implicitly_wait(3)

driver.get('https://supertaste.tvbs.com.tw/food')

for i in range(5):
    driver.execute_script('latest_more.click()')
    time.sleep(1)
    
soup = BeautifulSoup(driver.page_source,'html.parser')   

food = soup.find('div',{'class':'article__content'})


a = food.find_all('a')

for row in a:
    img = row.find('img').get('data-original')
    title = row.find('h3').text.strip()
    post_time = row.find('span').text.strip()
    link = 'https://supertaste.tvbs.com.tw' + row.get('href')
    
    print(img)
    print(title)
    print(post_time)
    print(link)
    print()
 