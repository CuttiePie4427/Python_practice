# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 19:19:21 2023

@author: USER
"""

import cv2 
import numpy as np 

img = cv2.imread('number.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0)

thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


#找邊緣>>迴圈

for c in contours:
        #矩形面積>50才要
    if cv2.contourArea(c) > 50:
         #找四邊框
        [x,y,w,h] = cv2.boundingRect(c)
          #高度>28才要 >>>28是老師用小畫家量的
        if h > 28:
            
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
               #畫矩形>>   檔案/ 起始點/ 終點 /  顏色(紅色)/粗細
            cv2.imshow('img',img)   
            
            cv2.waitKey()

cv2.waitKey()

cv2.destroyAllWindows()
