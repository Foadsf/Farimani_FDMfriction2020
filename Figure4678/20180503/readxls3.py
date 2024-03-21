#from here https://stackoverflow.com/a/16896091/4999991

import pandas as pd
# dfs = pd.read_excel("friction coeficient_41g.xls", sheet_name="Specimen 1")
dfs = pd.read_excel("friction coeficient_41g.xls", sheet_name=3)


dfs.columns=['time','strain','force','work']
dfs=dfs.drop(dfs.index[[0,1,2]])
# dfs['min'] = dfs.force[(dfs.force.shift(1) > dfs.force) & (dfs.force.shift(-1) > dfs.force)]
dfs2=dfs
dfs2 = dfs2.drop(dfs2[~((dfs2.force.shift(1) > dfs2.force) & (dfs2.force.shift(-1) > dfs2.force))].index)
# dfs['max'] = dfs.force[(dfs.force.shift(1) < dfs.force) & (dfs.force.shift(-1) < dfs.force)]
# dfs['locex'] = dfs.force[((dfs.force.shift(1) < dfs.force) & (dfs.force.shift(-1) < dfs.force)) | ((dfs.force.shift(1) < dfs.force) & (dfs.force.shift(-1) < dfs.force))]
# print(dfs.head(10))
# dfs.plot()
# print(dfs.iloc[2:10,[1,2]])



# import numpy as np
# from scipy.signal import argrelextrema
# print(dfs.loc[argrelextrema(dfs.iloc[2:,2].values, np.less)])
# dfs2=dfs.loc[argrelextrema(dfs.iloc[2:,2].values, np.less)]
#
# dfs3=dfs.loc[argrelextrema(dfs.iloc[2:,2].values, np.greater)]
# dfs4=dfs2.loc[argrelextrema(dfs2.iloc[:,2].values, np.less)]
# print(dfs4.head(30))


# sp = np.fft.fft(dfs.iloc[2:,2]-dfs.iloc[2:,2].mean())
# # sp = np.fft.fft(dfs.iloc[2:,2])
# freq = np.fft.fftfreq(dfs.iloc[2:,2].shape[-1])

# sp = np.fft.fft(dfs2.iloc[2:,2])
# freq = np.fft.fftfreq(dfs2.iloc[2:,2].shape[-1])

import matplotlib.pyplot as plt
plt.plot(dfs.iloc[:,1], dfs.iloc[:,2],label='data')
plt.scatter(dfs2.iloc[:,1], dfs2.iloc[:,2],label='data')
# plt.plot(dfs.iloc[2:,1], dfs.iloc[2:,2]-dfs.iloc[2:,2].mean())
# plt.plot(dfs2.iloc[2:,1], dfs2.iloc[2:,2], dfs3.iloc[2:,1], dfs3.iloc[2:,2])
# plt.scatter(dfs.iloc[:,1], dfs.iloc[:,4],label='min')
# plt.scatter(dfs.iloc[:,1], dfs.iloc[:,5],label='max')
# plt.plot(dfs2.iloc[2:,1], dfs2.iloc[2:,2])

# plt.plot(freq, sp.real, freq, sp.imag)
# plt.plot(freq, np.abs(sp),freq, np.angle(sp))
# plt.plot(freq, np.abs(sp))
plt.legend()
plt.show()
