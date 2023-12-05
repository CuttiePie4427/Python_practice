# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:21:54 2023

@author: USER
"""

import cv2

import numpy as np

img = cv2.imread('lena.jpg')

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img',np.concatenate((img,rgb),axis = 1)) #axis=0是水平/1是垂直
    #把兩張圖並排顯示>>要channel一樣才能，灰階只有1個就不能合併
cv2.waitKey()

cv2.destroyAllWindows()





