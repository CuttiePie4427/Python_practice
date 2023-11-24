# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 21:07:34 2023

@author: USER
"""

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,10))#(圖片大小，英吋)

with open('yrborn.txt') as f:
    
    populations = f.readlines()
    

yrborn = dict()
    
for p in populations:
    yr,total,boy,girl = p.split()    
    
    yrborn[yr] = {'boy':int(boy),'girl':int(girl)}
    
index = np.arange(len(yrborn))

yrlist = sorted(list(yrborn.keys()))

bp = list()

bp_b = list()

bp_g = list()

for y in yrlist:
    
    boys = yrborn[y]['boy']
    
    girls = yrborn[y]['girl']
    
    bp.append(boys + girls)
    
    bp_b.append(boys)
    
    bp_g.append(girls)
    
#畫圖

plt.subplot(2,1,1)

plt.plot(bp)

plt.xlabel(0,len(bp)-1)
    
plt.title('Total Born')

plt.subplot(2,1,2)

plt.plot(bp_b)

plt.plot(bp_g)

plt.xlim(0,len(bp_b)-1)

plt.title('Boy:Girl')

plt.show()
    
    
    
    
    
    
    
    
    

    