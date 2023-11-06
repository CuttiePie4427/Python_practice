# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 20:32:45 2023

@author: USER
"""

import db
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url ='https://www.setn.com/ViewAll.aspx?PageGroupID=0&utm_source=setn.com&utm_medium=menu&utm_campaign=hotnews'

header ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'    
    }
data = requests.get(url,headers = header).text
# print(data)

soup = BeautifulSoup(data,'html.parser')

content = soup.find(id='NewsList')

news = content.find_all('div',{'class':'newsItems'})

for item in news:
    
    h3 = item.find('h3')
    
    link = h3.find('a').get('href')
    
    if not('https' in link):
        
        link = 'https://www.setn.com' + link
        
        sort = item.find('a').text
        
        title = h3.text
        
        post_date = item.find('time').text
        
        year = datetime.today().year
        
        post_date = str(year) + '/' + post_date
        
        # print(post_date)
        
        ### 下面匯進資料庫 ###
        sql ="select * from news where title = '{}' and platform = 'setn'".format(title)
        
        db.cursor.execute(sql)
        
        if db.cursor.rowcount == 0:  #表示在資料表中沒有此筆資料
        
            sql="insert into news(title,link_url,post_date,platform) values('{}','{}','{}','{}')".format(title,link,post_date,'setn')
            
            db.cursor.execute(sql)
            
            db.conn.commit() #絕對要有執行這行指令
            
db.conn.close()
            
        
        
        
        
        
        
    
       
