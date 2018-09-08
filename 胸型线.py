# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:15:22 2018

@author: haoyu
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
mpl.rcParams['font.sans-serif']=[u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

x=np.arange(1,0,-0.001)
y=(-3*x*np.log(x)+np.exp(-(40*(x-1/np.e))**4)/25)/2
plt.figure(figsize=(5,7),facecolor='w')
plt.plot(y,x,'r-',linewidth=2)
plt.grid(True)
plt.title(u'胸形线',fontsize=20)
plt.show()