# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:58:20 2023

@author: USER
"""

import cv2

img = cv2.imread('lena.jpg')

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#換顏色

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#變灰階

cv2.imshow('img',img)#要先打開圖檔

key = cv2.waitKey()

if key == ord('A'):
    
    cv2.imshow('img',rgb) #按大寫A會變換顏色
    
elif key == ord('B'):
    
    cv2.imshow('img',gray)  #按大寫B會換灰階
    
cv2.waitKey()

cv2.destroyAllWindows()
