# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
url = 'https://tw.buy.yahoo.com/search/product'
header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

param = {}
p = input('輸入欲查詢的商品:')
param['p'] = p 

param = {'p':'longchamp'}

data = requests.get(url,params=param,headers=header).text
# print(data)

soup = BeautifulSoup(data,'html.parser')

goods = soup.find('div',{'class':'ResultList_resultList_IpWJt'})

items = goods.find_all('a')
# print(items)

for row in items:
    link = row.get('href')
    
    title = row.find('span',class_ = 'sc-1d7r8jg-0 sc-dp9751-0 sc-1drl28c-5 czfCFU fUBIAU biZSHp')
    if title != None:
        title = title.text
        
        price = row.find('span',class_='sc-1d7r8jg-0 sc-dp9751-0 eLSRyH eEsfHX').text
        
        price = price.replace('$','') #價格的$跟,是文字，取代掉$跟,->這樣才是純數值，才能存進資料庫尋找
        price = price.replace(',','')
        print()
        print('商品名:',title)
        print('價格:',price)
        print('連結:',link)
        print()
    print('-'*30)
    
