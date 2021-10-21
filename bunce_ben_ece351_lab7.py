# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:11:12 2021

@author: ben
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

steps = 2e-2

t = np.arange(0, 2, steps)
s = np.arange(0, 2, steps)

def stepFunc(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        if t[i] < 0:
            y[i] = 0
        else:
            y[i] = 1
    return y

#############################################
##                  Part 1                 ##
#############################################



G = (s+9)/((s-8)*(s+2)*(s+4))
A = (s+4)/((s+3)*(s+1))
B = (s+14)*(s+12)

zeros, poles, gain = sig.tf2zpk([1,9], sig.convolve([1,-6,-16],[1,4]))
print("G(s) Results:")
print(zeros)
print(poles)
print(gain)

zeros, poles, gain = sig.tf2zpk([1,4], [1,4,3])
print("A(s) Results:")
print(zeros)
print(poles)
print(gain)

roots = np.roots([1,26,168])
print("B(s) Results:")
print(roots)

print()
print()

system_open = [1,9],sig.convolve([1,4,3],[1,-6,-16])
print(sig.convolve([1,4,3],[1,-6,-16]))
t, step = sig.step(system_open)

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, step)
plt.grid()
plt.ylabel('Step')
plt.xlabel('t')
plt.title('f1(t) Plot')


#############################################
##                  Part 2                 ##
#############################################

steps = 2e-2

t = np.arange(0, 2, steps)

numG = [1,9]
denG = sig.convolve([1,-6,-16],[1,4])
numA = [1,4]
denA = [1,4,3]
numB = [1,26,168]
denB = [1]


print(sig.convolve(denA, denG))
print(sig.convolve(sig.convolve(denA, numB), numG))

numTotal = sig.convolve(numG, numA)
denTotal = sig.convolve(denA, denG) + sig.convolve(sig.convolve(denA, numB), numG)

print(numTotal)
print(denTotal)

transfer_closed = numTotal, denTotal
t, step_closed = sig.step(transfer_closed)

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, step_closed)
plt.grid()
plt.ylabel('Step')
plt.xlabel('t')
plt.title('f1(t) Plot')