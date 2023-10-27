# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:08:19 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup
url = 'https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystation'
header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
      }
param = {'_csrf':'5ac2173a-dbc2-4f14-8f48-95095b16afd7',
         'rideDate':'2023/10/27',
         'station':'3300-臺中'
         }
data = requests.post(url,data = param,headers = header).text
# print(data)
soup = BeautifulSoup(data,'html.parser')

stn = soup.find(id = 'tab1') #tab1僅順行
# print(stn)
items = stn.find_all('tr')[1:]
print('順行:')
print()
for row in items:
    car = row.find('a').text
    tds = row.find_all('td')
    sp = row.find_all('span')
    print('車次:',car)
    print(sp[2].text,sp[3].text,sp[4].text)
    print('出發時間',tds[1].text)
    print('終點站',tds[2].text)
    print('-'*30)



