#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
import scipy.fftpack
import xlsxwriter

def func_lin(x,a,b):
    return a*x+b

#%%
speeds=[50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
#weights=['44','80','128','188','236']
weights=[44,80,128,188,236]
# weights=[51,87,135,195,243]
areas=[900,1700,2500]
surcons=('bs perpendicular','ss parallel parallel','ss parallel perpendicular','ss perpendicular perpendicular')
surcon='ss parallel parallel'

#%%
def Xlim(s):
    return (6-3)*(s)/(1800)+3

A = areas[0]
# for A in areas:
# s = speeds[4]
writer = pd.ExcelWriter((surcon + '\\' + str(A) + 'mm\\' +'spectral_FFT_scipy.xlsx'), engine='xlsxwriter')
dfs2=pd.DataFrame(columns=['mean', 'per','mag'],index=speeds)
for w in weights:
    for s in speeds:
        file = surcon + '\\' + str(A) + 'mm\\' + str(A) + 'mm_' + str(s) + 'mm_min.xls'
        # xls = pd.ExcelFile(file)
        # weights = [int(w[:-1]) for w in xls.sheet_names[3:]]
        # w = weights[0]
        dfs = pd.read_excel(file, sheet_name=str(w) + 'g')
        dfs.columns=['time','strain','force','work']
        dfs=dfs.drop(dfs.index[[0,1]])

        #removing anytheing before the max
        dfs.drop(dfs.index[:dfs['force'].astype(float).idxmax()],inplace=True)
        #removing anything after the strain is constant
        dfs=dfs[(dfs['strain'].iloc[-1]-dfs['strain'])>0.001]

        force=dfs['force'].values.astype(float)
        mean = force.mean()
        # dfs2['mean'][s] = mean
        force -= mean
        strain=dfs['strain'].values.astype(float)
        strain -= strain[0]
        # time=dfs['time'].values.astype(float)*60

        #number of sample points
        N=force.size

        #sample spacing
        popt, pcov = curve_fit(func_lin, np.arange(N), strain)
        L=popt[0]

        # plt.subplot(2, 1, 1)
        # plt.plot(strain, force)
        # plt.grid()

        force_f = 2.0/N *np.abs(scipy.fftpack.fft(force))
        freq = np.linspace(0.0, 1.0/(2.0*L), N//2) 

        x = 1/freq[1:]
        xlim = Xlim(s)
        # xlim = 6
        xp = x[x<xlim]
        y = force_f[1:N//2]
        yp = y[x<xlim]

        dfs2['mean'][s] = mean
        dfs2['per'][s]=xp[yp.argmax()]
        dfs2['mag'][s]=yp.max()
        # dfs2['per'][s]=x[y.argmax()]
        # dfs2['mag'][s]=y.max()
        

        # plt.subplot(2, 1, 2)
        # plt.semilogx(x, spl(x))
        # plt.semilogx(xp,  yp)
# plt.grid()
    dfs2.to_excel(writer, sheet_name=str(w))

# plt.show()
writer.save()


#%%
A = areas[0]
for j, w in enumerate(weights):
    dfs = pd.read_excel(surcon + '\\' + str(A) + 'mm\\' + "spectral_FFT_scipy.xlsx", sheet_name=j)
    plt.plot(dfs.index, dfs['per'], label = str(w))

plt.plot(dfs.index, [Xlim(s) for s in dfs.index])

plt.legend()
plt.show()


#%%
for j, w in enumerate(weights):
    dfs = pd.read_excel(surcon + '\\' + str(A) + 'mm\\' + "spectral_FFT_scipy.xlsx", sheet_name=j)
    mean = dfs['mean'].values.astype(float)
    plt.plot(dfs.index, mean, label = str(w))
    # popt, pcov = curve_fit(func_arm, dfs.index, mean, p0=[mean[-1],mean[0]-mean[-1],100])
    # print(popt)
    # plt.plot(dfs.index, func_arm(dfs.index, *popt))

plt.legend()
plt.show()

#%%
for j, w in enumerate(weights):
    dfs = pd.read_excel(surcon + '\\' + str(A) + 'mm\\' + "spectral_FFT_scipy.xlsx", sheet_name=j)
    plt.plot(dfs.index, dfs['mag'], label = str(w))

plt.legend()
plt.show()