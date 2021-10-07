# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 11:30:27 2021

@author: ben
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
#############################################
##                  Part 1                 ##
#############################################

steps = 1.2e-5

print (steps)

t = np.arange(0, 0.0012, steps)

ht = 10000*np.e**(-5000*t)*np.cos(18584*t) - 2690.5*np.e**(-5000*t)*np.sin(18584*t)

R = 1000
L = 0.027
C = 100E-9
z = 1/(R*C)
al = -0.5*z
w = 0.5*np.sqrt(z**2 - 4/(L*C)+0*1j)
#w = 37168.3
p = al + w
g = p * z
#g = np.sqrt((-0.5*z**2)**2 + (z*w)**2)
g_abs = np.abs(g)
g_ang = np.angle(g)

ht2 = (g_abs/w)*np.e**(al*t)*np.sin(w*t + g_ang)

system = ([10000.0, 0.0], [1.0, 10000.0, 370370370.4])
t, hs = scipy.signal.impulse(system)
t, step = scipy.signal.step(system)



plt.figure(figsize = (10, 7))
plt.subplot(2,1,1)
plt.tight_layout()
plt.title('h(t)')
plt.plot(t, ht)
plt.subplot(2,1,2)
plt.tight_layout()
plt.title('H(s)')
plt.plot(t, hs)
plt.ylabel('h(t)')
plt.xlabel('t')

plt.figure(figsize = (10, 7))
plt.tight_layout()
plt.title('Step Response')
plt.plot(t, step)
plt.grid()
plt.ylabel('h(t)')
plt.xlabel('t')

print("done")
