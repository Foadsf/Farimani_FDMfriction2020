#from here https://stackoverflow.com/a/16896091/4999991

import pandas as pd
# dfs = pd.read_excel("friction coeficient_41g.xls", sheet_name="Specimen 1")
dfs = pd.read_excel("friction coeficient_53g.xls", sheet_name=4)


dfs.columns=['time','strain','force','work']
dfs=dfs.drop(dfs.index[[0,1]])
# dfs['min'] = dfs.force[(dfs.force.shift(1) > dfs.force) & (dfs.force.shift(-1) > dfs.force)]

# dfs['max'] = dfs.force[(dfs.force.shift(1) < dfs.force) & (dfs.force.shift(-1) < dfs.force)]
# dfs['locex'] = dfs.force[((dfs.force.shift(1) < dfs.force) & (dfs.force.shift(-1) < dfs.force)) | ((dfs.force.shift(1) < dfs.force) & (dfs.force.shift(-1) < dfs.force))]

# dfs.plot()
# print(dfs.iloc[2:10,[1,2]])

from scipy.signal import lfilter

n = 15  # the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 1
dfs['fil'] = lfilter(b,a,dfs.iloc[0:,2])
# print(dfs.head(10))


# n=1
dfs2=dfs
# for i in range(n):
dfs2 = dfs2.drop(dfs2[~(((dfs2.fil.shift(1) < dfs2.fil) & (dfs2.fil.shift(-1) < dfs2.fil)))].index)
#
#
#
dfs3=dfs
# for i in range(n):
dfs3 = dfs3.drop(dfs3[~(((dfs3.fil.shift(1) > dfs3.fil) & (dfs3.fil.shift(-1) > dfs3.fil)))].index)
#
# # dfs4 = pd.concat([dfs2, dfs3]) #, ignore_index=True
#
# # dfs4=dfs4.sort_values('strain')
dfs2['del']=dfs2.strain-dfs2.strain.shift(1)
dfs3['del']=dfs3.strain-dfs3.strain.shift(1)

print(dfs2['del'].mean())
print(dfs3['del'].mean())
# print(dfs4.strain[0:])

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
# plt.scatter(dfs4.iloc[:,1], dfs4.iloc[:,2],label='locex')
plt.scatter(dfs2.iloc[:,1], dfs2.iloc[:,4],label='max')
plt.scatter(dfs3.iloc[:,1], dfs3.iloc[:,4],label='min')
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
