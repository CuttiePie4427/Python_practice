# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

img = cv2.imread('lena.jpg')#預設是彩色，0是灰階

# cv2.IMREAD_COLOR
# 此為預設值，這種格式會讀取 RGB 三個 channels 的彩色圖片，而忽略透明度的 channel
# cv2.IMREAD_GRAYSCALE
# 以灰階的格式來讀取圖片
# cv2.IMREAD_UNCHANGED
# 讀取圖片中所有的 channels，包含透明度的 channel

print(img.shape)
print(img)

cv2.imshow('img',img)#打開圖片

cv2.waitKey()

cv2.destroyAllWindows()
#按任意鍵關閉