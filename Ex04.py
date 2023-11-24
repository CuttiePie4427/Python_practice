# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:34:21 2023

@author: USER
"""

import matplotlib.pyplot as plt

Toyota = [4122,5400,2100]
Lexus = [3000,4300,1900]
Bmw= [4000,5213,2099]

year = [2021,2022,2023]

plt.xticks(year)

lineToyota ,= plt.plot(year,Toyota,'-*',label='Toyota')
lineLexus ,= plt.plot(year,Lexus,'-o',label='Lexus')
lineBmw ,= plt.plot(year,Bmw,'-^',label='BMW')


plt.legend(handles=[lineToyota,lineLexus,lineBmw],loc=0)

plt.title('Car Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.savefig('carsales.jpg')
plt.show()