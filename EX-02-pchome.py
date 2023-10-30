# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:43:28 2023

@author: USER
"""

import requests
import json

url = 'https://ecshweb.pchome.com.tw/search/v4.3/all/results' 

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
      }
for i in range(1,6):
    param = {
        'q':'登機箱',
    'page':i,
    'sort':'rnk/dc'
            }
    data = requests.get(url,params = param, headers = header).text
    
    pchome = json.loads(data)
    
    goods = pchome['Prods']
    
    for item in goods:
        title = item['Name']
        photo = "https://cs-a.ecimg.tw/" + item['PicB'] 
        price = item['Price']
        info = item['Describe']  
        print()
        print(title)
        print(photo)
        print(price)
        print(info)
        print('-'*40)       