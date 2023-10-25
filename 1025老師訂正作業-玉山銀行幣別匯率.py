# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 21:06:18 2023

@author: USER
"""

from bs4 import BeautifulSoup
import requests

header = {    
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }

url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'

data = requests.get(url,headers=header).text #header 用來加上標頭
# print(data) #先印是用來確認有沒有抓到
soup = BeautifulSoup(data,'html.parser')

rates = soup.find(id = 'exchangeRate')

# print(rates) #用來確認，有抓到就可註解掉
tbody = rates.find('tbody')
# print(tbody)

trs = tbody.find_all('tr')
# print(trs)

for row in trs:
    tds = row.find_all('td',recursive=False)#遞迴搜尋,預設是True->=False是關閉內迴圈的搜尋 
    if len(tds) == 4: 
        print(tds[0].text.strip().split()[0])
        print(tds[1].text.strip())
        print(tds[2].text.strip())     
        print(tds[3].text.strip())
         #.split()用來切割，預設是空白
    


    