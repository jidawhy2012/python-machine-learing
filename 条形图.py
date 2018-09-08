# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 14:05:07 2018

@author: haoyu
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

x=np.arange(0,10,0.1)
y=np.sin(x)
plt.bar(x,y,width=0.04,linewidth=0.2)
plt.title(u'sin曲线')
plt.xticks(rotation=-60)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()

