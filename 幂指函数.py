# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 12:59:57 2018

@author: haoyu
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
mpl.rcParams['font.sans-serif']=[u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

plt.figure(facecolor='w')
x=np.linspace(-1.3,1.3,101)
y=x**x
plt.plot(x,y,'g',label='x^x,',linewidth=2)
plt.grid()
plt.legend(loc='upper left')
plt.show()