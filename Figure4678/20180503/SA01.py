import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import fft



speeds=[10,30,50,100,150,200,300,400,600,800,1000,1400,1800]
weights=[41,53,65,77,89,136,184,232]


# for w in weights[0]:
for j in range(3,11):#16
    dfs = pd.read_excel("friction coeficient_"+str(41)+"g.xls", sheet_name=j)

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

    # print(result)

    # plt.plot(dfs['strain'], dfs['force'])
    # plt.plot(dfs['strain']-dfs['strain'].values[0], result-np.average(result))

    sp = np.abs(np.fft.fft(result-np.average(result)))
    # freq = np.fft.fftfreq(n)
    plt.plot(sp, label=str(speeds[j]))

plt.xlim(0,300)
plt.legend()
plt.show()


