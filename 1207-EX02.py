# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:44:37 2023

@author: USER
"""

import cv2

#二值化

img = cv2.imread('lena.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

t,res = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

t,res2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

t,res3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)

t,res4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)

t,res5 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)

#THRESH_BINARY : 127為閾值－－>127:設為255，反之為0

#THRESH_BINARY_INV : 127為閾值－－>127:設為0，反之為255

#THRESH_TRUNC : 127為閾值－－>127:設為127，反之不變

#THRESH_TOZERO : 127為閾值－－>127:數值不便，反之為0

#THRESH_TOZERO_INV : 127為閾值－－>127:設為0，反之不變

print(gray)

print('-'*40)

print(res)

cv2.imshow('img',res)

cv2.imshow('img2',res2)

cv2.imshow('img3',res3)

cv2.imshow('img4',res4)

cv2.imshow('img5',res5)

cv2.imshow('i',img)

cv2.waitKey()

cv2.destroyAllWindows()