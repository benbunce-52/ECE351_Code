# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


#############################################
##                  Part 1                 ##
#############################################

plt.rcParams.update({'font.size':14})

steps = 1e-2

t = np.arange(0, 10 + steps, steps)

def cosPlot(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        y[i] = np.cos(t[i])
    return y

y = cosPlot(t)

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('cos(t) Plot')

#############################################
##                  Part 2                 ##
#############################################

#x = 0

t = np.arange(0, 10 + steps, steps)
def rampFunc(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        if t[i] < 0:
            y[i] = 0
        else:
            y[i] = t[i]
    return y

y = rampFunc(t)

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Ramp Plot')

t = np.arange(0, 10 + steps, steps)
def stepFunc(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        if t[i] < 0:
            y[i] = 0
        else:
            y[i] = 1
    return y

y = stepFunc(t)

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Step Plot')

t = np.arange(-5, 10 + steps, steps)
def Fig2Func(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        y = rampFunc(t) - rampFunc(t-3) + 5*stepFunc(t-3) - 2*stepFunc(t-6) - 2*rampFunc(t-6) + 2*rampFunc(t-10)
    return y

y = Fig2Func(t)

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Fig 2 Plot')

#############################################
##                  Part 3                 ##
#############################################

##Task 1
t = np.arange(-10, 5 + steps, steps)
y = Fig2Func(-t)

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Time Reversal Plot')


##Task 2
t = np.arange(0, 15 + steps, steps)
y = Fig2Func(t-4)

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('f(t-4) Plot')


##Task 3
t = np.arange(-15, 0 + steps, steps)
y = Fig2Func(-t-4)

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('f(-t-4) Plot')


##Task 4
t = np.arange(-5, 20 + steps, steps)
y = Fig2Func(t/2)

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('f(t/2) Plot')


#Task 5
t = np.arange(-5, 10 + steps, steps)
y = Fig2Func(2*t)

plt.figure(figsize = (10, 7))
#plt.subplot(2,1,1)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('f(2t) Plot')

##Diff
#print("test")
steps = 1
t = np.arange(-5, 10 + steps, steps)
arr = np.array(Fig2Func(t))
dt = np.diff(arr)
#print(dt)
plt.figure(figsize = (10, 7))
plt.plot(t, dt[t])
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('diff Plot')



    



