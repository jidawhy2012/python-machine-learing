# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 12:20:54 2018

@author: haoyu 
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
mpl.rcParams['font.sans-serif']=[u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10,8))
x=np.linspace(start=2,stop=3,num=1001,dtype=np.float)
y_logit=np.log(1+np.exp(-x))/math.log(2)
y_boost=np.exp(-x)
y_01=x<0
y_hinge=1.0-x
y_hinge[y_hinge<0]=0
plt.plot(x,y_logit,'r-',label='Logistic Loss',linewidth=2)
plt.grid()
plt.legend(loc='upper right')
plt.show()

plt.plot(x,y_01,'g-',label='0/1 Loss',linewidth=2)
plt.grid()
plt.legend(loc='upper right')
plt.show()
plt.plot(x,y_hinge,'b-',label='Hinge Loss',linewidth=2)
plt.grid()
plt.legend(loc='upper right')
plt.show()
plt.plot(x,y_boost,'m--',label='Adaboost Loss',linewidth=2)
plt.grid()
plt.legend(loc='upper right')
plt.savefig('1.png')
plt.show()


