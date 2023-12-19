# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:07:31 2023

@author: USER
"""

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('img/006.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.021,5)

for (x,y,w,h) in faces:
    
    im = cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),3)
    
cv2.imshow('im',im)

cv2.waitKey()

cv2.destroyAllWindows()


