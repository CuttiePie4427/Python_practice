# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np

img = cv2.imread('car.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

img_blur = cv2.GaussianBlur(binary, (5,5), 0)

contours, herarachy = cv2.findContours(img_blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# RETR_EXTERNAL :只偵測外層輪廓邊緣
#     _LIST     :偵測所有輪廓邊緣，沒有層級
#     _CCOMP    :偵測所有輪廓邊緣，但建立兩層級結構，內層與外層
#     _TREE     :真測所有輪廓邊緣，並建立所有(完整)層級(一層一層建立)

#               _CHAIN_APPROX_NONE :抓取輪廓的位置，不規則形狀可用(圓形適用)
#               _CHAIN_APPROX_SIMPLE :抓取矩形的四點位置 >>水平垂直端點都可，多邊形都可








# print(contours)

# x,y,w,h = cv2.boundingRect(contours[0])
# 確認邊框大小
# print('x =',x)
# print('y =',y)
# print('w =',w)
# print('h =',h)

n = len(contours)

contoursImg = list()

for item in range(n):
    
    temp = np.zeros(img.shape,np.uint8)
    
    contoursImg.append(temp)
    
    print(cv2.contourArea(contours[item])) #邊框面積
    
    if cv2.contourArea(contours[item]) > 300:
        #畫邊框 >>(0,0,255)是紅色
        ret = cv2.drawContours(contoursImg[item], contours, item, (0,0,255),3)
        
        cv2.imshow('img'+str(item),ret)
        
cv2.waitKey()

cv2.destroyAllWindows()        
    
    
    

