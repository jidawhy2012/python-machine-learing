# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 14:24:39 2018

@author: haoyu
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

t=1000
a=np.zeros(10000)
for i in range(t):
    a+=np.random.uniform(-5,5,10000)
a/=t
plt.hist(a,bins=30,color='g',alpha=0.5,normed=True,label=u'均匀分布叠加')
plt.legend(loc='upper left')
plt.grid()
plt.show()
