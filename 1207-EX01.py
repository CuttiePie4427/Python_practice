# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

import numpy as np

def crop_img(img):
    
    print('圖:',img.shape)
    
    # cv2.imshow('img',img)
    
    half = int(img.shape[0]/2) #把圖"寬"裁一半>>[0]是高 / [2]是通道
    
    crop = img[:,half:half+399,:]
    
    cv2.imshow('cropimg',crop)
    
    cv2.waitKey()
    
    cv2.destroyAllWindows()
    
    
    
def resize_img(img):  #縮圖

    print(img.shape)

    imgresize = cv2.resize(img,(200,200)) #把圖片縮成200X200>>也可以放大

    cv2.imshow('resize',imgresize)

    print('change',imgresize.shape)

    cv2.waitKey()

    cv2.destroyAllWindows()    


    

def change_bright(img,bright):  #調明暗
    
    rows,cols,channels = img.shape  #這樣寫就不用索引值
    
    dst = img.copy()
    
    for i in range(rows):
        
        for x in range(cols):
            
            for c in range(channels):
                
                color = img[i,x][c] + bright
                
                if color > 255:  #亮度不超過極限>>避免像素越界
                    
                    dst[i,x][c] = 255
                    
                elif color <0:   #也不要太暗到變黑>>避免像素越界
                    
                    dst[i,x][c] = 0
                    
                else:   
                    
                    dst[i,x][c] = color
                
    return dst            
    
#調對比>>跟明暗一樣，只是把+ bright 改成 * contrast

def change_contrast(img,contrast):    
    
    rows,cols,channels = img.shape  #這樣寫就不用索引值
    
    dst = img.copy()
    
    for i in range(rows):
        
        for x in range(cols):
            
            for c in range(channels):
                
                color = img[i,x][c] * contrast
                
                if color > 255:  #亮度不超過極限>>避免像素越界
                    
                    dst[i,x][c] = 255
                    
                elif color <0:   #也不要太暗到變黑>>避免像素越界
                    
                    dst[i,x][c] = 0
                    
                else:   
                    
                    dst[i,x][c] = color
                
    return dst            

    
    

if __name__ == '__main__':
    
    img = cv2.imread('lena.jpg')
    
    # crop_img(img) #切割
    
    # resize_img(img)  #縮放
    
      #明暗

    resize = cv2.resize(img,(200,200))
    
    up = change_bright(resize,100)
    
    down = change_bright(resize,-100)
    
    cv2.imshow('bright',np.concatenate((up,resize,down),axis=1))
    
    # cv2.waitKey()
    
    # cv2.destroyAllWindows()
        
        #對比 >> 改成contrast >>係數改成 EX:1.5倍之類的
        
    # resize = cv2.resize(img,(200,200))
    
    up = change_contrast(resize,3)
    
    down = change_contrast(resize,0.1)
    
    cv2.imshow('contrast',np.concatenate((up,resize,down),axis=1))
    
    cv2.waitKey()
    
    cv2.destroyAllWindows()
