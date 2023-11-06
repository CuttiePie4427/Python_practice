# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:16:24 2023

@author: USER
"""

from PIL import Image

import pytesseract

fileName = 'car2.jpg'

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open(fileName)

text = pytesseract.image_to_string(img,lang='eng',config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz --psm 12')

print(text.strip())