# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 14:43:45 2018

@author: haoyu
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
from scipy import stats
import scipy.optimize as opt
from scipy.stats import norm, poisson
mpl.rcParams['font.sans-serif']=[u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

lamda=7
p=stats.poisson(lamda)
y=p.rvs(size=1000)
mx=30
r=(0,mx)
bins=r[1]-r[0]
plt.figure(figsize=(15,8),facecolor='w')
plt.subplot(121)
plt.hist(y,bins=bins,range=r,color='g',alpha=0.8,normed=True)
t=np.arange(0,mx+1)
plt.plot(t,p.pmf(t),'ro-',lw=2)
plt.grid(True)


N=1000
M=10000
plt.subplot(122)
a=np.zeros(M,dtype=np.float)
p=stats.poisson(lamda)
for i in np.arange(N):
    a+=p.rvs(size=M)
a/=N
plt.hist(a,bins=20,color='g',alpha=0.8,normed=True)
plt.grid(b=True)
plt.show()
    
