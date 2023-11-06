# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:16:24 2023

@author: USER
"""

from PIL import Image

import pytesseract


fileName = 'car.jpg'

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open(fileName)
                                                   #白名單--只有在名單上的才能辨識
text = pytesseract.image_to_string(img,config='-c tessdit_char_whitelist=0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz --psm 6')
                                       #--oem : 有四種,0-Lagacy/1-LSTM/2/3(最常用) 
                                       #--psm : 自動頁面分割--有13種(1-13)，10/9單字/8單字/7單行文字/6區段
print(text.strip())