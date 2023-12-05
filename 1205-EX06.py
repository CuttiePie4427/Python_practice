# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:37:47 2023

@author: USER
"""

import cv2

img = cv2.imread('lena.jpg')
img2 = cv2.imread('photo.jpg')

# img2[120:300,340:480] = img[220:400,220:360] >>圖片部分更換，大小要一樣
img[220:400,220:360] = img2[120:300,340:480]
cv2.imshow('img', img) 

cv2.imwrite('new.jpg', img) #存檔

cv2.waitKey()

cv2.destroyAllWindows()