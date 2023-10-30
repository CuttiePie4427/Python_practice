# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:29:29 2023

@author: USER
"""

import requests
import json

url = 'https://ecapi-cdn.pchome.com.tw/fsapi/cms/onsale' 

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
      }
data = requests.get(url,headers = header).text

goods = json.loads(data)

pchome = goods['data']
# print(pchome)


allitem = pchome['products']
print(allitem)
# for row in allitem:        
#     title = row['name']
#     photo = row['image']            
#     p = row['price']            
#     print(title)            
#     print(photo)         
#     print(p['onsale'])            
    
    