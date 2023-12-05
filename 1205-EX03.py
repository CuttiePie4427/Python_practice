# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:51:07 2023

@author: USER
"""

import cv2
import numpy as np

img = np.zeros((200,200),dtype = np.uint8)
# img = np.zeros((200,200,3),dtype = np.uint8) >>會變成3channel＝彩色圖，再改內容就可
print(img)
print(img.shape)

# img[50,50] = 255
# img[100,100] = 255

cv2.imshow('zeros',img)#全0顯示圖片是全黑<->全255是白

cv2.waitKey()

cv2.destroyAllWindows()