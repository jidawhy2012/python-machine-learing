# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:24:14 2018

@author: haoyu 
"""
t=np.linspace(0,2*np.pi,100)
x=16*np.sin(t)**3
y=13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
plt.plot(x,y,'r-',linewidth=2)
plt.grid(True)
plt.show()