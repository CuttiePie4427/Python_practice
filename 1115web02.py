# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:25:09 2023

@author: USER
"""

from flask import Flask,render_template
import db
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/news')
def news():
    
    page = request.args.get('page','1')
    
    sql = "select count(*) as c from news"
    
    db.cursor.execute(sql)
    
    datacount = db.cursor.fetchone()
    
    count = int(datacount[0])
       
    if page == 1:
        
        sql = "select platform,title,link_url,photo_url from news limit 36"
        
    else:
        
        startp = page - 1
        
        sql = "select platform,title,link_url,photo_url from news limit {},{}".format(startp * 36,36)
        
        
    db.cursor.execute(sql)    
    result = db.cursor.fetchall()
    return render_template('news.html',**locals())
    
    
    
    
@app.route('/goods')    
def goods():
    p= request.args.get('p','')
    startp = request.args.get('startp','')
    endp = request.args.get('endp','')
    
    if len(p) == 0 and len(startp) == 0 and len(endp) == 0:
        
        sql = "select title,price,link_url,description,photo_url from goods order by price"
    
    elif len(p) > 0 and len(startp) == 0 and len(endp) == 0:
        
        sql = "select title,price,link_url,description,photo_url from goods where title like '%{}%'".format(p)
    
    elif len(p) == 0 and len(startp) > 0 and len(endp) > 0:
        
        sql = "select title,price,link_url,description,photo_url from goods where price between {} and {} ".format(startp,endp)
    
    else:
       
        sql = "select title,price,link_url,description,photo_url from goods where price between {} and {} and title like '%{}%' ".format(startp,endp,p)
        
        
    db.cursor.execute(sql)
    
    result = db.cursor.fetchall()
    
    return render_template('product.html',**locals())


@app.route('/product/<string:p>')
def product(p):
    
    sql = "select title,price,link_url,description,photo_url from goods where title like '%{}%'".format(p)

    db.cursor.execute(sql)
    
    result = db.cursor.fetchall()
    
    return render_template('product.html',**locals())





app.run()