# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 16:25:00 2018

@author: Administrator
"""

import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from scipy.optimize import leastsq
from scipy import stats
import scipy.optimize as opt
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import CubicSpline
import scipy as sp

x, y = np.mgrid[-3:3:7j, -3:3:7j]
print(x)
print(y)
u = np.linspace(-3, 3, 101)
x, y = np.meshgrid(u, u)
print(x)
print(y)
z = x*y*np.exp(-(x**2 + y**2)/2) / math.sqrt(2*math.pi)
# z = x*y*np.exp(-(x**2 + y**2)/2) / math.sqrt(2*math.pi)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap=cm.coolwarm, linewidth=0.1)  #
ax.plot_surface(x, y, z, rstride=3, cstride=3, cmap=cm.gist_heat, linewidth=0.5)
plt.show()
cmaps = [('Perceptually Uniform Sequential',
              ['viridis', 'inferno', 'plasma', 'magma']),
             ('Sequential', ['Blues', 'BuGn', 'BuPu',
                             'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
                             'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
                             'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']),
             ('Sequential (2)', ['afmhot', 'autumn', 'bone', 'cool',
                                 'copper', 'gist_heat', 'gray', 'hot',
                                 'pink', 'spring', 'summer', 'winter']),
             ('Diverging', ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
                            'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral',
                            'seismic']),
             ('Qualitative', ['Accent', 'Dark2', 'Paired', 'Pastel1',
                              'Pastel2', 'Set1', 'Set2', 'Set3']),
             ('Miscellaneous', ['gist_earth', 'terrain', 'ocean', 'gist_stern',
                                'brg', 'CMRmap', 'cubehelix',
                                'gnuplot', 'gnuplot2', 'gist_ncar',
                                'nipy_spectral', 'jet', 'rainbow',
                                'gist_rainbow', 'hsv', 'flag', 'prism'])]
