# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:33:25 2023

@author: USER
"""

import matplotlib.pyplot as plt
import numpy as np

tom = [90,60,80]

mary = [100,99,92]

bill = [70,90,62]

level = np.arange(3)  #會出來索引直[0,1,2]
# print(level)

plt.bar(level,tom,0.2,label='Tom')

plt.bar(level+0.2,mary,0.2,label ='Mary')

plt.bar(level+0.4,bill,0.2,label ='Bill')

plt.legend(loc=0)

plt.grid(True)

plt.show()
