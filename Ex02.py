# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:20:47 2023

@author: USER
"""

import matplotlib.pyplot as plt


data1 = [10,2,3,4,5,6,7,8]

data2 = [1,3,5,7,9,11,13,15]

data3 = [1,5,10,15,20,25,30,35]

point = [1,2,3,4,5,6,7,8]

plt.plot(point,data1,point,data2,point,data3)

plt.show()