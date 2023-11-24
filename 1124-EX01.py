# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

#折線圖
data = [1,5,9,20,25,33,40,72]

point = [1,2,3,4,5,6,7,8]

#第一項是X軸座標
plt.plot(point,data,linewidth=3,color = 'red')

plt.title('chart',fontsize=26)

plt.xlabel('value')

plt.ylabel('Data',fontsize=18)

plt.show()
