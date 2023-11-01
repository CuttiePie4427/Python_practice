# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Beauty/index.html"

g = 1

for i in range(5):
    header ={
        'cookie':'over18=1'  
        }
       
    data = requests.get(url,headers = header).text
    # print(data)
    soup = BeautifulSoup(data,'html.parser')
    area = soup.find_all('div',class_='r-ent')
    # print(area)
    url = 'https://www.ptt.cc'+ soup.find_all('a',class_='btn wide')[1].get('href')
    #抓上一頁的網址來做迴圈，抓出前五頁的資料
    for item in area:
        if item.find('a') != None:
            date = item.find('div',class_='date').text
            link = 'https://www.ptt.cc' + item.find('a').get('href')
            title = item.find('a').text
            
            print()
            print(title)
            print(link)
            print(date)
            #抓出網頁裡面的照片+把圖片下載到資料夾
            data = requests.get(link,headers = header).text
    
            soup = BeautifulSoup(data,'html.parser')
            
            img = soup.find(id = 'main-container')
            
            imgs = img.find_all('a')
            
            for im in imgs:
                photo = im.get('href')
                if 'jpg' in photo:
                    w = requests.get(photo)
                    file = str(g) + '.jpg'
                    with open(file,'wb') as fObj:
                        fObj.write(w.content)
                    g += 1
                    print(photo)         
                       
            
            
            
            
            