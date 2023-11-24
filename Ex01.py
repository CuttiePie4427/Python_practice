# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

data = [1,5,7,9,20,33,44,55]

point = [1,2,3,4,5,6,7,8]

plt.plot(point,data)

plt.title('Chart',fontsize=26)

plt.xlabel('Value')
plt.ylabel('Data',fontsize=18)

plt.show()