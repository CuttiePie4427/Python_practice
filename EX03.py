# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:16:16 2023

@author: USER
"""

import json
import requests

url = 'https://www.thsrc.com.tw/ArticleContent/a3b630bb-1066-4352-a1ef-58c7b4e8ef7c?search=f03JL80+mmAuu/IkmM0KUfOVuVgoIcBklIxs89NGvo1Et/ri48Yxj4ZQopwa+wqwDi8PS0KxNMhkikGDM0+U8CG0Jw5Sr7z2bQEjEUyZHaxw6gZ4LbPGZS9GaoqFX3ZPjJ2EcmrJAoTa0LCxTHws+KI5OPlj01njzpDidrmFwTKm85M3Zav/2JREx3xS7oN6mvcEFTwcLpb+TTROvDRP7A=='

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
      }
param = {'SearchType':'S',
'Lang':'TW',
'StartStation':'NanGang',
'EndStation':'ZuoYing',
'OutWardSearchDate':'2023/10/27',
'OutWardSearchTime':'21:30',
'ReturnSearchDate':'2023/10/27',
'ReturnSearchTime':'21:30',
         }

data = requests.post(url,data = param,headers = header)

thrsc = json.load(data)

items = thrsc['data']['DepartureTable']['TrainItem']
print(items)

# for row in items:
#     print(items['TrainNumber'])
    
    
    
    
    
    
    
    
    