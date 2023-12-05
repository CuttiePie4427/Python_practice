# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:17:22 2023

@author: USER
"""

import cv2

img = cv2.imread('lena.jpg')

face = img[220:400,220:360]  #座標軸: Y:Y+H / X: X+W
#透過指定座標>>可以換臉，但是大小必須相同

cv2.imshow('Face', face) #顯示指定位置>>這邊算好是臉部

cv2.waitKey()

cv2.destroyAllWindows()