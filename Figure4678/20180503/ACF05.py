#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlsxwriter

from scipy.interpolate import spline
from scipy.interpolate import splev, splrep

from interpacf import interpolated_acf, dominant_period

#%%
speeds=[10,30,50,100,150,200,300,400,600,800,1000,1400,1800]
weights=[41,53,65,77,89,136,184,232]

#%%
dfs2= pd.DataFrame(columns=['mean', 'per', 'mag'],index=speeds)
# writer = pd.ExcelWriter('spectral_autocor_interpacf.xlsx', engine='xlsxwriter')
# j=3
# w=weights[0]
for w in [41, 53, 65, 77, 136]:
    for j in range(3,16):
        dfs = pd.read_excel("friction coeficient_"+str(w)+"g.xls", sheet_name=j)

        #clean up columns
        dfs.columns=['time','strain','force','work']
        dfs=dfs.drop(dfs.index[[0,1]])


        dfs.drop(dfs.index[:dfs['force'].astype(float).idxmax()],inplace=True)
        dfs=dfs[(dfs['strain'].iloc[-1]-dfs['strain'])>0.001]
        # dfs.sort_values(by=['strain'],inplace=True)

        force=dfs['force'].values.astype(float)
        mean = force.mean()
        force -= mean
        strain=dfs['strain'].values.astype(float)
        strain -= strain[0]
        # time=dfs['time'].values.astype(float)*60


        # plt.subplot(2, 1, 1)
        # plt.plot(strain, force)
        # plt.grid()



        lag, acf = interpolated_acf(strain, force)
        # plt.subplot(2, 1, 2)
        # plt.plot(lag,acf,label=str(j))
        period = dominant_period(lag, acf, fwhm=1, plot=False)
        itemindex = np.where(lag==period)
        # print(speeds[j-3],',',period,',',acf[itemindex[0][0]])
        dfs2['per'][speeds[j-3]]=period
        dfs2['mag'][speeds[j-3]]=acf[itemindex[0][0]]
        dfs2['mean'][speeds[j-3]] = mean
    # dfs2.to_excel(writer, sheet_name=str(w))
    # print(w,',',dfs2['mag']/dfs2['mag'].max())
    x=dfs2.index
    # y= dfs2['mag']/dfs2['mag'].max()
    y=dfs2['per']
    # xnew=np.linspace(x.min(),x.max(),1000)
    # spl = splrep(x, y)
    # ynew=splev(xnew, spl)
    # plt.scatter(x,y,label=str(w))
    # plt.plot(xnew,ynew)
    plt.plot(x,y, label=str(w))
    # plt.plot(speeds,dfs2[w],label=str(w))

# print(dfs2)

# plt.xlim(0,100)
# plt.ylim(0,3)

# plt.xlim(0,2)
plt.legend(title="Normal force (gram)")
plt.show()

# writer.save()



