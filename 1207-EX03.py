# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:32:42 2023

@author: USER
"""

import cv2

img = cv2.imread('car2.jpg',0)

_,res = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#自適應二值化

img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,15,3)

img3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,3)

cv2.imshow('img',res)

cv2.imshow('img2',img2)

cv2.imshow('img3',img3)

cv2.waitKey()

cv2.destroyAllWindows()
