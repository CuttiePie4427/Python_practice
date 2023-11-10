# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import requests

from bs4 import BeautifulSoup

import db

url =  'https://tw.buy.yahoo.com/search/product'


header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    
    
param = {}

p = input('請輸入查詢的商品：')

param['p'] = p


data = requests.get(url,params=param,headers=header).text

soup = BeautifulSoup(data,'html.parser')

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
        
        sql = "select * from goods where platform = 'Yahoo' and title ='{}'".format(title)
        
        db.cursor.execute(sql)
        
        
        
        
        # print('商品：',title)
        # print('價格：',price)
        # print('連結：',link)
        # print()




