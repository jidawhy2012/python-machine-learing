# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:57:17 2018

@author: Administrator
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

t=np.linspace(0,50,num=1000)
x=t*np.sin(t)+np.cos(t)
y=np.sin(t)-t*np.cos(t)
plt.plot(x,y,'r-',linewidth=2)
plt.grid()
plt.show()