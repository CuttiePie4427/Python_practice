# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:22:16 2023

@author: USER
"""

import matplotlib.pyplot as plt


data1 = [10,2,3,4,5,6,7,8]

data2 = [1,3,5,7,9,11,13,15]

data3 = [1,5,10,15,20,25,30,35]

point = [1,2,3,4,5,6,7,8]

# plt.subplot(1,3,1)

# plt.plot(point,data1,'-*')

# plt.subplot(1,3,2)

# plt.plot(point,data2,'-s')

# plt.subplot(1,3,3)

# plt.plot(point,data3,'-^')


plt.subplot(3,1,1)

plt.plot(point,data1,'-*')

plt.subplot(3,1,2)

plt.plot(point,data2,'-s')

plt.subplot(3,1,3)

plt.plot(point,data3,'-^')



plt.title('Chart2')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()





