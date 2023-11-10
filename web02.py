# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:20:54 2023

@author: USER
"""

from flask import Flask


app = Flask(__name__)  #初始化flask的物件

@app.route('/')    #根目錄

def index():
    return "首頁"

@app.route('/news')

def news():
    
    sql = "select platform, title, link_url from news"

    db.cursor.execute(sql)
    
    result = db.cursor.fetchall()
    
    for item in result:
        
        print(item[0])
        print(item[1])
        print(item[2])
        print()
    
@app.route('/goods')

def goods():
    
    p = ''
    startp = 0
    endp = 0
    
    if p == '':
   
    sql = "select title, price, link_url, description from goods where price between {} and {}".format(startp,endp)
    
    else:
        sql = "select title, price, link_url, description from goods where price between {} and {} and title like '%{}%'".format(startp,endp,p)    
        
        
        
    db.cursor.execute(sql)
    
    result = db.cursor.fetchall()
    
    for item in result:
        
        print(item[0])
        print(item[1])
        print(item[2])
        print(item[3])
        print()
    

app.run()  #執行

