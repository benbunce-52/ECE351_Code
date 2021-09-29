# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:12:08 2021

@author: ben
"""

import numpy as np
import matplotlib.pyplot as plt
import math

#############################################
##                  Part 1                 ##
#############################################

steps = 1e-2

t = np.arange(-10, 10 + steps, steps)
def rampFunc(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        if t[i] < 0:
            y[i] = 0
        else:
            y[i] = t[i]
    return y

t = np.arange(-10, 10 + steps, steps)
def stepFunc(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        if t[i] < 0:
            y[i] = 0
        else:
            y[i] = 1
    return y

w = 2*np.pi*0.25
h1 = (np.e**(-2*t))*(stepFunc(t)-stepFunc(t-3))
h2 = stepFunc(t-2) - stepFunc(t-6)
h3 = (np.cos(w*t))*stepFunc(t)

plt.figure(figsize = (10, 7))
plt.subplot(3,1,1)
plt.tight_layout()
plt.title('h1(t)')
plt.plot(t, h1)
plt.subplot(3,1,2)
plt.tight_layout()
plt.title('h2(t)')
plt.plot(t, h2)
plt.subplot(3,1,3)
plt.tight_layout()
plt.title('h3(t)')
plt.plot(t, h3)
plt.grid()
plt.ylabel('h(t)')
plt.xlabel('t')

#############################################
##                  Part 2                 ##
#############################################

ut = stepFunc(t)

steps2 = 1e-2
textended = np.arange(2*t[0], 2*t[len(t)-1]+steps, steps2)

def conv(f1, f2):
    nf1 = len(f1)
    nf2 = len(f2)
    f1extend = np.append(f1, np.zeros((1, nf2-1)))
    f2extend = np.append(f2, np.zeros((1, nf1-1)))
    result = np.zeros(f1extend.shape)
    for i in range(nf2+nf1-2):
        result[i] = 0
        for j in range(nf1):
            if(i-j+1>0):
                try:
                    result[i] += f1extend[j]*f2extend[i-j+1]
                except:
                    print(i,j)
    return result
    
conv1 = conv(h1, ut)*steps
conv2 = conv(h2, ut)*steps
conv3 = conv(h3, ut)*steps

plt.figure(figsize = (10, 7))
plt.subplot(3,1,1)
plt.tight_layout()
plt.title('Conv h1(t)')
plt.plot(textended, conv1)
plt.subplot(3,1,2)
plt.tight_layout()
plt.title('Conv h2(t)')
plt.plot(textended, conv2)
plt.subplot(3,1,3)
plt.tight_layout()
plt.title('Conv h3(t)')
plt.plot(textended, conv3)
plt.grid()
plt.ylabel('h(t)')
plt.xlabel('t')

conv1_2 = 0.5*(1-np.e**(-2*textended))*stepFunc(textended) - 0.5*(1-np.e**(-2*(textended-3)))*stepFunc(textended-3)
conv2_2 = (textended-2)*stepFunc(textended-2) - (textended-6)*stepFunc(textended-6)
conv3_2 = (1/(0.5*np.pi))*np.sin(0.5*np.pi*textended)*stepFunc(textended)

plt.figure(figsize = (10, 7))
plt.subplot(3,1,1)
plt.tight_layout()
plt.title('Conv h1(t)')
plt.plot(textended, conv1_2)
plt.subplot(3,1,2)
plt.tight_layout()
plt.title('Conv h2(t)')
plt.plot(textended, conv2_2)
plt.subplot(3,1,3)
plt.tight_layout()
plt.title('Conv h3(t)')
plt.plot(textended, conv3_2)
plt.grid()
plt.ylabel('h(t)')
plt.xlabel('t')


