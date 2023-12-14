# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

img = cv2.imread('car.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 1)

thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 3)

contours,hierachey = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,0,255),1)

cv2.imshow('img',img)

cv2.waitKey()

cv2.destroyAllWindows()
