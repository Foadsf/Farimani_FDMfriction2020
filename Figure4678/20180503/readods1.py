import pandas as pd
import ezodf

import matplotlib.pyplot as plt

# import seaborn as sns
# sns.set(rc={'figure.figsize':(10,5)}, font_scale=1.5)
# sns.set_style({'axes.facecolor':'white', 'grid.color': '.8'})

# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')

from scipy.optimize import curve_fit
import numpy as np

def read_ods(filename, sheet_no=0, header=0):
    tab = ezodf.opendoc(filename=filename).sheets[sheet_no]
    return pd.DataFrame({col[header].value:[x.value for x in col[header+1:]]
                         for col in tab.columns()})
masses=[41, 53, 65, 77, 89, 136, 184, 232]

plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=22)
fig = plt.gcf()
fig.set_size_inches(10, 5)

font = {'family' : 'serif',
        # 'weight' : 'bold',
        'size'   : 20}

plt.rc('font', **font)

def func(x, a, b, c):
    return a * np.exp(-b * x) + c
# j=0
for j in range(0,8):
    df = read_ods(filename='analysis_20180613.ods',sheet_no=j)
    df=df.drop(df.columns[[4]], axis=1).drop(df.index[[13,14]])
    # P0=[df.iloc[0,1]-df.iloc[-1,1],1,df.iloc[-1,1]]
    P0=[df.iloc[0,1]-df.iloc[-1,1],0.003,df.iloc[-1,1]]
    # print(P0)
    popt, pcov = curve_fit(func, df['v(mm/min)'].values, df['max average'].values,p0=P0)
#     print(popt)



    plt.scatter(df['v(mm/min)'], df['max average'], label=masses[j])
    # plt.plot(df['v(mm/min)'].values, func(df['v(mm/min)'].values, *popt), label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
    plt.plot(df['v(mm/min)'].values, func(df['v(mm/min)'].values, *popt), linewidth=2)
    # plt.plot(df['v(mm/min)'], df['min average'])


plt.xlabel(r'Velocity $\mathrm{(mm/min)}$')
plt.ylabel(r'Force $\mathrm{(N)}$')
# plt.grid(linestyle='--',linewidth=0.4)
plt.legend(title = r'Mass $\mathrm{(gram)}$', shadow=True, ncol=2, labelspacing = 0.2, columnspacing = 0.2, borderpad = 0.2, prop={'size': 15})
plt.grid(linestyle = '--', linewidth=0.4)
plt.tight_layout()
plt.show()
fig.savefig("20190305_kineticforce.pdf", bbox_inches='tight')
