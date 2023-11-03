# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:16:24 2023

@author: USER
"""

from PIL import Image

import pytesseract

fileName = 'number01.jpg'

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open(fileName)

text = pytesseract.image_to_string(img,lang='eng')

print(text.strip())