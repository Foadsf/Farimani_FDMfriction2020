import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import fft



speeds=[10,30,50,100,150,200,300,400,600,800,1000,1400,1800]
weights=[41,53,65,77,89,136,184,232]




# for w in weights[0]:
j=3
# for j in range(0,2):#16
dfs = pd.read_excel("friction coeficient_"+str(41)+"g.xls", sheet_name=j+3)

#clean up columns
dfs.columns=['time','strain','force','work']
dfs=dfs.drop(dfs.index[[0,1]])

        
#removing anytheing before the max
dfs.drop(dfs.index[:dfs['force'].astype(float).idxmax()],inplace=True)
#removing anything after the strain is constant
dfs=dfs[(dfs['strain'].iloc[-1]-dfs['strain'])>0.001]
# print(dfs['force'].values.shape[0])
n=dfs['force'].values.shape[0]
result=np.empty(n)
result[:]=np.nan
for i in range(1,n+1):
    # print(dfs['force'].values[:i].shape[0],' , ',dfs['force'].values[-i:].shape[0])
    result[i-1] = np.average(np.abs(dfs['force'].values[:i].astype(float)-dfs['force'].values[-i:].astype(float)))
    # result[i-1] = np.average(dfs['force'].values[:i].astype(float)-dfs['force'].values[-i:].astype(float))
    # print((dfs['force'].values[:i].astype(float)-dfs['force'].values[-i:].astype(float)).shape)

# result2=np.empty(n)
# result2[:]=np.nan
# for i in range(1,n+1):
#     # print(dfs['force'].values[:i].shape[0],' , ',dfs['force'].values[-i:].shape[0])
#     result2[i-1] = np.average(np.abs(result[:i]-result[-i:]))

# print(result)
plt.subplot(2, 1, 1)
plt.plot(dfs['strain']-dfs['strain'].values[0], dfs['force']-dfs['force'].mean())
plt.plot(dfs['strain']-dfs['strain'].values[0], (result-np.average(result))*4, label=str(speeds[j]))
# plt.plot(dfs['strain']-dfs['strain'].values[0], result2-np.average(result2))

sp = np.abs(np.fft.fft(4*(result-result.mean())))
sp2 = np.abs(np.fft.fft(dfs['force']-dfs['force'].mean()))
# freq = np.fft.fftfreq(n)
plt.subplot(2, 1, 2)
# # plt.plot((dfs['strain']-dfs['strain'].values[0])/dfs['strain'].values[-1], sp, label=str(speeds[j]))
plt.plot(dfs['strain']-dfs['strain'].values[0],sp2)
plt.plot(dfs['strain']-dfs['strain'].values[0],sp, label=str(speeds[j]))

# plt.xlim(0,300)
# plt.legend()
plt.show()


