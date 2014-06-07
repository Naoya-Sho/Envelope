# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

# ����̎�
def f(x, t):
    return t * x - t**2

#�O���t�̎��Ȃǂ̐ݒ�
def subplots():
    fig, ax = plt.subplots()

    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
        
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none') 

    ax.set_xticks([])
    ax.set_yticks([]) 
    
    return (fig, ax)

fig, ax = subplots() 

# x�̒�`���ݒ�
x = np.linspace(-50,50,1000)

# x,y�̕\���͈͂�ݒ�
ymin =-15
ymax =20
xmin =-10
xmax =10
v = [xmin, xmax, ymin, ymax]

switch = 0 #�@����̖{����ݒ� 

if switch == 0:
	slopes = np.linspace(-4,4,15)#�p�����[�^�𓮂����͈͂Ɖ�
if switch == 1:
	slopes = np.linspace(-5,5,30)

for slope in slopes:
    y = f(x, t=slope)
    plt.plot(x, y, 'k-')
plt.axis(v)
plt.axvline(linewidth=2, color='k') #x���̐ݒ�
plt.axhline(linewidth=2, color='k') #y���̐ݒ�
for FORMAT in ['.png', '.pdf']:
	plt.savefig('envelope'+ str(switch) +FORMAT,transparent=True, bbox_inches='tight', pad_inches=0)
plt.close()