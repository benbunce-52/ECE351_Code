# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:28:46 2021

@author: ben
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.fftpack
import pandas as pd

#### Definitions ####

def fftfunc(x, fs):
    N = len(x)
    X_fft = scipy.fftpack.fft(x)
    X_fft_shifted = scipy.fftpack.fftshift(X_fft)
    
    freq = np.arange(-N/2, N/2)*fs/N
    
    X_mag = np.abs(X_fft_shifted)/N
    X_phi = np.angle(X_fft_shifted)
    return freq, X_mag, X_phi

def make_stem(ax, x, y, color='k', style='solid', label='', linewidths=2.5, **kwargs):
    ax.axhline(x[0], x[-1],0, color='r')
    ax.vlines(x,0,y,color=color,linestyles=style,label=label,linewidths=linewidths)
    ax.set_ylim([1.05*y.min(), 1.05*y.max()])
    
####################

#### Common Variables ####

fs = 1000000
steps = 1
hz = np.arange(0, 10e6, steps)

####################

#### Read in Values ####

df = pd.read_csv('NoisySignal.csv')

t = df['0'].values
sensor_sig = df['1'].values

####################

#### Original Plot ####

plt.figure(figsize = (10,7))
plt.plot (t, sensor_sig)
plt.grid()
plt.title('Noisy Input Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [V]')
plt.show()

####################

#### Filtered output ####

num = [1256, 0]
den = [1, 1256.6, 1579043]

z, p = sig.bilinear(num, den, 100000)

outputSig = sig.lfilter(z, p, sensor_sig)

plt.figure(figsize = (10,7))
plt.plot (t, outputSig)
plt.grid()
plt.title('Clean Output Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [V]')
plt.show()

####################

#### Bode Plots Magnitude and Phase ####

sys = sig.TransferFunction(num,den)
w2, mag2, phase2 = sig.bode(sys, hz)

fig, ax = plt.subplots(2)
fig.suptitle("Bode Plot Full Range Hz")
plt.tight_layout()
ax[0].semilogx(hz, mag2)
#ax[0].set_xlabel("Frequency (Hz)")
ax[0].set_ylabel("Decibel (dB)")
ax[0].set_title("magnitude")
ax[0].grid()

ax[1].semilogx(hz,phase2)
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Phase (degrees)")
ax[1].set_title("phase")
ax[1].grid()

fig, ax = plt.subplots(2)
fig.suptitle("Bode Plot 0 < f < 1780Hz")
plt.tight_layout()
ax[0].semilogx(hz, mag2)
ax[0].set_xlim([0,1780])
#ax[0].set_xlabel("Frequency (Hz)")
ax[0].set_ylabel("Decibel (dB)")
ax[0].set_title('magnitude')
ax[0].grid()

ax[1].semilogx(hz,phase2)
ax[1].set_xlim([0,1780])
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Phase (degrees)")
ax[1].set_title('phase')
ax[1].grid()

fig, ax = plt.subplots(2)
fig.suptitle("Bode Plot 2010 < f < 100000Hz")
plt.tight_layout()
ax[0].semilogx(hz, mag2)
ax[0].set_xlim([2010,100000])
#ax[0].set_xlabel("Frequency (Hz)")
ax[0].set_ylabel("Decibel (dB)")
ax[0].set_title('magnitude')
ax[0].grid()

ax[1].semilogx(hz,phase2)
ax[1].set_xlim([2010,100000])
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Phase (degrees)")
ax[1].set_title('phase')
ax[1].grid()

fig, ax = plt.subplots(2)
fig.suptitle("Bode Plot 1800 < f < 2000Hz")
plt.tight_layout()
ax[0].semilogx(hz, mag2)
ax[0].set_xlim([1800,2000])
#ax[0].set_xlabel("Frequency (Hz)")
ax[0].set_ylabel("Decibel (dB)")
ax[0].set_title('magnitude')
ax[0].grid()

ax[1].semilogx(hz,phase2)
ax[1].set_xlim([1800,2000])
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Phase (degrees)")
ax[1].set_title('phase')
ax[1].grid()


#### FFT Plots Filtered and Unfiltered ####

fullFreq, fullXMag, fullXPhi = fftfunc(sensor_sig, fs)
freqFiltered, X_magFiltered, X_phiFiltered = fftfunc(outputSig, fs)

fig, ax = plt.subplots(figsize=(10,7))
make_stem(ax, fullFreq, fullXMag)
plt.title('Full Range FFT (Unfiltered)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

fig, ax = plt.subplots(figsize=(10,7))
ax.set_xlim([0,1780])
make_stem(ax, fullFreq, fullXMag)
plt.title('0Hz < f < 1780Hz FFT (Unfiltered)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

fig, ax = plt.subplots(figsize=(10,7))
ax.set_xlim([2010, 100000])
make_stem(ax, fullFreq, fullXMag)
plt.title('2010Hz < f < 100000Hz FFT (Unfiltered)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

fig, ax = plt.subplots(figsize=(10,7))
ax.set_xlim([1800, 2000])
make_stem(ax, fullFreq, fullXMag)
plt.title('1800Hz < f < 2000Hz FFT (Unfiltered)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
    
fig, ax = plt.subplots(figsize=(10,7))
make_stem(ax, freqFiltered, X_magFiltered)
plt.title('Full Range FFT (Filtered)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

fig, ax = plt.subplots(figsize=(10,7))
ax.set_xlim([0, 1780])
make_stem(ax, freqFiltered, X_magFiltered)
plt.title('0Hz < f < 1780Hz FFT (Filtered)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

fig, ax = plt.subplots(figsize=(10,7))
ax.set_xlim([2010, 100000])
make_stem(ax, freqFiltered, X_magFiltered)
plt.title('2010Hz < f < 100000Hz FFT (Filtered)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

fig, ax = plt.subplots(figsize=(10,7))
ax.set_xlim([1800, 2000])
make_stem(ax, freqFiltered, X_magFiltered)
plt.title('1800Hz < f < 2000Hz FFT (Filtered)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
