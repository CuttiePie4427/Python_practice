# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:34:45 2023

@author: USER
"""
import matplotlib.pyplot as plt
Toyota = [1234,2345,3456]

Lexus = [1324,2435,3546]

BMW = [1432,2543,3654]

year = [2021,2022,2023]


plt.xticks(year)

lineToyota ,= plt.plot(year,Toyata,'-*',label ='Toyota')

lineLexus ,= plt.plot(year,Lexus,'-o',lable ='Lexus')

lineBMW ,= plt.plot(year,BMW,'-^',lable ='Lexus')

plt.legend = (handles=[lineToyota,lineLexus,lineBMW],loc=0)

plt.title = ('Car sale',fontsize = 16)

plt.xlabel=('Year',fotsize=16)

plt.ylabel=('Sales',fotsize=16)

plt.savefig('carsales.jpg') #一定要先存檔才能show，先show的話檔案會被洗掉，會存到白圖

plt.show()