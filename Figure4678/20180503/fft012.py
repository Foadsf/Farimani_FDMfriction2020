import pandas as pd
from numpy import fft
import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt

for j in range(3,4):
    dfs = pd.read_excel("friction coeficient_41g.xls", sheet_name=j)
    #clean up columns
    dfs.columns=['time','strain','force','work']
    dfs=dfs.drop(dfs.index[[0,1]])
    plt.subplot(2, 1, 2)
    plt.plot(dfs['strain'], dfs['force'],label='data')
    # print(dfs.head())
    # sp = scipy.fftpack.fft(dfs['force'].values)
    # print(np.average(dfs['force'].values.astype(float)))
    sp = np.fft.fft(dfs['force'].values-np.average(dfs['force'].values.astype(float)))
    freq = np.fft.fftfreq(dfs.index.values.shape[-1])/0.01170106947
    # plt.plot(freq, sp)
    # plt.plot(freq, sp.real, freq, sp.imag)
    plt.subplot(2, 1, 1)
    plt.plot(freq, np.abs(sp),label=j)
    # print(freq[np.abs(sp).argsort()])
    print(np.sort(np.abs(sp))[::-1])
   


# plt.xlim(-10,10)
plt.grid()
plt.show()