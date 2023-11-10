# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:59:09 2023

@author: USER
"""

import db

startp = int(input('初始價格:'))

endp = int(input('終止價格:'))

p = input('商品名稱:')

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
    
    
    