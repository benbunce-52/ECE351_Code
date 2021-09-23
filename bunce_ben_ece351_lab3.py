# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:31:16 2021

@author: ben
"""
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.signal as sig

steps = 1e-2

t = np.arange(0, 20 + steps, steps)
def rampFunc(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        if t[i] < 0:
            y[i] = 0
        else:
            y[i] = t[i]
    return y

t = np.arange(0, 20 + steps, steps)
def stepFunc(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        if t[i] < 0:
            y[i] = 0
        else:
            y[i] = 1
    return y

y1 =  stepFunc(t-2) - stepFunc(t-9)

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, y1)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('f1(t) Plot')

y2 = (math.e**-t)*(stepFunc(t))

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, y2)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('f2(t) Plot')

y3 = (rampFunc(t-2))*(stepFunc(t-2)-stepFunc(t-3)) + (rampFunc(4-t))*(stepFunc(t-3) - stepFunc(t-4))

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, y3)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('f3(t) Plot')

y5 = sig.convolve(y1, y2, mode='full')

steps2 = 0.5e-2
textended = np.arange(0, 20 + 3*steps2, steps2)

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
    

y4 = conv(y1, y2)*steps
plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(textended, y4)
plt.plot(textended, (sig.convolve(y1, y2, mode='full')*steps))
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Concolve f1, f2 Plot')

y4 = conv(y1, y3)*steps
plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(textended, y4)
plt.plot(textended, (sig.convolve(y1, y3, mode='full')*steps))
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Concolve f1, f3 Plot')

y4 = conv(y2, y3)*steps
plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(textended, y4)
plt.plot(textended, (sig.convolve(y2, y3, mode='full')*steps))
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Concolve f2, f3 Plot')



    