# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:36:35 2023

@author: USER
"""

import cv2

import numpy as np

img = cv2.imread('lena.jpg')

img[:,:,0] = 0
img[:,:,1] = 0

#會變成紅色 FF0000
b = img[:,:,0]

g = img[:,:,1]

r = img[:,:,2]

cv2.imshow('lena',img)

cv2.imshow('img',np.concatenate((b,g,r),axis = 1))

cv2.waitKey()

cv2.destroyAllWindows()