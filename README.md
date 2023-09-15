# Tugas Kelas PSO-D

ini merupakan beberapa rangkuman dari tugas yang saya kerjakan.

## Author
![profil](https://github.com/RizkiAkbar12/Tugas-SPO/assets/108193209/21ab33f9-27fe-4a37-bd3b-f407f6f2d123)
![identitas](https://github.com/RizkiAkbar12/Tugas-SPO/assets/108193209/2775a751-b563-4e38-bef8-b62069ada416)




## Isi Konten
- A. Nama dan NRP
- B. Source Code Pemrosesan Sinyal
- C. Commit Logs

---

## A. Nama dan NRP

![source code identitas](https://github.com/RizkiAkbar12/Tugas-SPO/assets/108193209/b6157fc4-724a-4880-983a-21cd0c3461b3)
```py
print("Nama: M Rizki Akbar")
print("NRP: 5009211128")
```
---

## B. Source Code Pemrosesan Sinyal

```py
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
plt.plot(ts, y_lfilter, alpha=0.8, lw=3, label="SciPy lfilter")

plt.xlabel("Time / s")
plt.ylabel("Amplitude")
plt.legend(loc="lower center", bbox_to_anchor=[0.5, 1],
           ncol=2, fontsize="smaller")

```
Ini merupakan hasil dari Signal Filter:

![hasil filter](https://github.com/RizkiAkbar12/Tugas-SPO/assets/108193209/a30f44fd-de0d-464f-b446-e03f049391cb)

---

## C. Commit Logs
![commit logs](https://github.com/RizkiAkbar12/Tugas-SPO/assets/108193209/1f07042f-ea18-4806-9e82-749d93425bd4)

