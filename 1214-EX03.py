# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:02:14 2023

@author: USER
"""

import cv2 
import numpy as np

def load_digit_file(imgfile):
    
    im = cv2.imread(imgfile)
    
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    kernel = np.ones((5,5),np.uint8)
    
    ret,threshold = cv2.threshold(gray,127,255,0)
    
    threshold = cv2.erode(threshold,kernel,1) #先侵蝕，將白邊移除
    
    threshold = cv2.dilate(threshold,kernel,1)  #再膨脹，消除小白點
      #找邊緣>>抓四邊
    contours, hierachy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        
        if cv2.contourArea(c) > 20000 and cv2.contourArea(c) < 130000:
            
            [x,y,w,h] = cv2.boundingRect(c)
            
            cv2.rectangle(im, (x,y), (x+w,y+h),(0,0,255),20)
            
            cv2.imshow('img',im)
            
            cv2.waitKey()
            
            #裁車牌
            
            newimg = threshold[y:y+h,x:x+w]
            
            cv2.imshow('new',newimg)
            
            cv2.imwrite('newimg.jpg',newimg)
            
            break
            
    cv2.destroyAllWindows()
    

load_digit_file('car4.jpg')
            
            
            
            
            
            
            

                          


