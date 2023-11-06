# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:40:46 2023

@author: USER
"""

import MySQLdb
                                                                            #MySQL的port(連接埠)預設是3306
conn = MySQLdb.connect(host='127.0.0.1', user='root', password='1234567890',db='myweb',port=3306)

cursor = conn.cursor()

