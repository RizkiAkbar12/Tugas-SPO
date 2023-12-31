import numpy as np
import scipy.signal

# Identitas diri
print("Nama: M Rizki Akbar")
print("NRP: 5009211128")

np.random.seed(42) 
fs = 30  # sampling rate, Hz
ts = np.arange(0, 5, 1.0 / fs)  
ys = np.sin(2*np.pi * 1.0 * ts)  # signal @ 1.0 Hz, tanpa Noise
yerr = 0.5 * np.random.normal(size=len(ts))  # Gaussian noise
yraw = ys + yerr

b, a = scipy.signal.iirfilter(4, Wn=2.5, fs=fs, btype="low", ftype="butter")
print(b, a, sep="\n")
y_lfilter = scipy.signal.lfilter(b, a, yraw)

from matplotlib import pyplot as plt

plt.figure(figsize=[6.4, 2.4])

plt.plot(ts, yraw, label="Raw signal")
plt.plot(ts, y_lfilter, alpha=0.8, lw=3, label="Signal filter")

plt.xlabel("Time / s")
plt.ylabel("Amplitude")
plt.legend(loc="lower center", bbox_to_anchor=[0.5, 1],
                            ncol=2, fontsize="smaller")
