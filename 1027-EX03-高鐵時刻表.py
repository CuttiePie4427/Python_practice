# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:16:16 2023

@author: USER
"""

import json
import requests
#Json格式>>不用美湯解
#從search的Network>>response 的資料拿去 Json Parser online解

url = 'https://www.thsrc.com.tw/TimeTable/Search' #從search的header找
header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
      }
param = {'SearchType':'S',                 #這段param從Network的payload抓
'Lang':'TW',
'StartStation':'NanGang',
'EndStation':'ZuoYing',
'OutWardSearchDate':'2023/10/27',
'OutWardSearchTime':'21:30',
'ReturnSearchDate':'2023/10/27',
'ReturnSearchTime':'21:30',
         }

data = requests.post(url,data = param,headers = header)

thrsc = json.loads(data)

items = thrsc['data']['DepartureTable']['TrainItem']
# print(items)
for row in items:    
    print(row['TrainNumber'])
    print(row['DepartureTime'])
    print(row['DestinationTime'])
    print(row['Duration'])
    print()
#作業<一>:列出停靠站
    stn = row['StationInfo']
    for sn in stn:
        if sn['Show'] == True:
            print(sn['StationName'])
    
    print()
    
    
    
    
    
    
    
    
    
