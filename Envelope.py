# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

# 包絡線の式
def f(x, t):
    return t * x - t**2

# xの定義域を設定
x = np.linspace(-50,50,1000)

# x,yの表示範囲を設定
ymin =-15
ymax =20
xmin =-10
xmax =10
v = [xmin, xmax, ymin, ymax]

slopes = np.linspace(-4,4,15)#パラメータを動かす範囲と回数
for slope in slopes:
    y = f(x, t=slope)
    plt.plot(x, y, 'b-')
plt.axis(v)
plt.axvline(linewidth=2, color='k') #x軸の設定
plt.axhline(linewidth=2, color='k') #y軸の設定
plt.show()

# <codecell>


# <codecell>


