# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

def f(x,t):
    return x**2 -t*x + t**2 -3*t +5

x = np.linspace(-50,50,1000)

# x,yの表示範囲を設定
ymin =-0
ymax = 25
xmin = 0
xmax = 8
v = [xmin, xmax, ymin, ymax]

parameters = np.linspace(0,5,12)
for parameter in parameters:
    y = f(x, t=parameter)
    plt.plot(x, y, 'b-')
plt.axis(v)
plt.axvline(linewidth=2, color='k') #x軸の設定
plt.axhline(linewidth=2, color='k') #y軸の設定
plt.show()

# <codecell>


# <codecell>


