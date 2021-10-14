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

steps = 2e-2

#print (steps)

t = np.arange(0, 2, steps)

def stepFunc(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        if t[i] < 0:
            y[i] = 0
        else:
            y[i] = 1
    return y

yt = (0.5-0.5*np.e**(-4*t)+np.e**(-6*t))*stepFunc(t)
yx = (0.5*np.e**(-4*t)+0.5*np.e**(-6*t))*stepFunc(t)

system = ([1.0,6.0, 12.0], [1.0, 10.0, 24])
t, hs = scipy.signal.impulse(system)
t, step = scipy.signal.step(system)

resid, poles, const = scipy.signal.residue([-4,-12], [1,10,24,0])
print(resid)
print(poles)
print(const)

##Task2

resid2, poles2, const2 = scipy.signal.residue([25250], [1,18,218,2036,9085,25250,0])
print(resid2)
print(poles2)
print(const2)

#tdc = (0.88*np.exp(-3*t)*np.cos(4*t+123.9) + 
#       0.88*np.exp(-3*t)*np.cos(-4*t-123.9) + 
#       -0.21*np.exp(-10*t) + 
#       0.1*np.exp(-1*t)*np.cos(10*t-29.1) + 
#       0.1*np.exp(-1*t)*np.cos(-10*t+29.1))*stepFunc(t)

tdc = 0

for j in range(len(resid2)):
    kabs = np.abs(resid2[j])
    eat = np.exp((np.real(poles2[j]))*t)
    cos = np.cos((np.imag(poles2[j]))*t + np.angle(resid2[j]))
    tdc += kabs*eat*cos*stepFunc(t)
    
systemp2 = ([25250], [1,18,218,2036,9085,25250])
t, stepp2 = scipy.signal.step(systemp2)

plt.figure(figsize = (10, 7))
plt.subplot(2,1,1)
plt.tight_layout()
plt.title('y(t)')
plt.plot(t, yt)
plt.subplot(2,1,2)
plt.tight_layout()
plt.title('H(s)')
plt.plot(t, step)
plt.ylabel('h(t)')
plt.xlabel('t')

plt.figure(figsize = (10, 7))
plt.subplot(2,1,1)
plt.tight_layout()
plt.title('y(t)')
plt.plot(t, tdc)
plt.subplot(2,1,2)
plt.tight_layout()
plt.title('H(s)')
plt.plot(t, stepp2)
plt.ylabel('h(t)')
plt.xlabel('t')

print("done")
