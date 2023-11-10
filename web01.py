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
    return "新聞"

app.run()  #執行

