#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import random
from matplotlib import pyplot as plt
from matplotlib import rcParams
import matplotlib
import numpy as np

# Use TeX
rcParams['text.usetex'] = True
rcParams['text.latex.unicode'] = True


"""
Parametric equation of the circle:
- x = a + r * cost
- y = a + r * sint
"""
r1 = 10
r2 = 1
a = 10
b = 10

x = []
y = []

for i in range(360):
    x.append(r1 * np.cos(i) + random.random() + a)
    y.append(r1 * np.sin(i) + random.random() + b)

x2 = []
y2 = []

for i in range(100):
    x2.append(r2 * np.cos(i) + random.randrange(-1, 1) + a)
    y2.append(r2 * np.sin(i) + random.randrange(-1, 1) + b)

plt.figure(1)
plt.subplot(121)
cur_axes = plt.gca()
cur_axes.axes.get_xaxis().set_ticks([])
cur_axes.axes.get_yaxis().set_ticks([])
plt.plot(x, y, ' bo')
plt.plot(x2, y2, 'yo')
plt.xlabel('x', fontsize=22)
plt.ylabel('y', fontsize=22)
plt.title(u'Cartesian Coordinate System')

plt.subplot(122)
cur_axes = plt.gca()
cur_axes.axes.get_xaxis().set_ticks([])
cur_axes.axes.get_yaxis().set_ticks([])

x = []
y = []

for i in range(10):
    for j in range(10):
        x.append(random.randrange(0, 1) + i)
        y.append(random.randrange(0, 11) + j)

x2 = []
y2 = []

for i in range(10):
    for j in range(10):
        x2.append(random.randrange(0, 1) + i + 15)
        y2.append(random.randrange(0, 11) + j)

plt.plot(x, y, 'yo')
plt.plot(x2, y2, 'bo')
plt.plot([(r1 + 2) for i in range(100)], [i/5 for i in range(100)],
         color='r', linestyle='-', linewidth=4)
plt.xlabel('r', fontsize=22)
plt.ylabel(r'$\theta$', fontsize=22)
plt.title(u'Polar Coordinate System')

plt.savefig('plot1.png')

plt.show()
