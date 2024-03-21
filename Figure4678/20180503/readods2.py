
#%%
import pandas as pd
import ezodf

import matplotlib.pyplot as plt

import seaborn as sns
sns.set()
# sns.set(rc={'figure.figsize':(10,5)}, font_scale=1.5, style="darkgrid")

# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')

# from scipy.optimize import curve_fit
# import numpy as np
#%%
def read_ods(filename, sheet_no=0, header=0):
    tab = ezodf.opendoc(filename=filename).sheets[sheet_no]
    return pd.DataFrame({col[header].value:[x.value for x in col[header+1:]]
                         for col in tab.columns()})
masses=[41, 53, 65, 77, 89, 136, 184, 232]

# fig = plt.gcf()
# fig.set_size_inches(10, 5)

# def func(x, a, b, c):
#     return a * np.exp(-b * x) + c

#%%


# dfs = pd.DataFrame({'v(mm/min)':[],  'max average':[],  'mass':[]})
dfs = pd.DataFrame()
# j=0
for j,m in enumerate(masses):
    df = read_ods(filename='analysis_20180613.ods',sheet_no=j)
    df = df.drop(df.columns[[4]], axis=1).drop(df.index[[13,14]])
    df = df.iloc[:,[0, 1]]
    df['mass']=m
    dfs = dfs.append(df)



sns.lineplot(x="v(mm/min)", y="max average",
             hue="mass", 
             style="mass",
            #  markers=True,
             data=dfs,
             dashes=False,
             err_style='bars',
             aspect=2)

#     
    # P0=[df.iloc[0,1]-df.iloc[-1,1],1,df.iloc[-1,1]]
    # P0=[df.iloc[0,1]-df.iloc[-1,1],0.003,df.iloc[-1,1]]
    # print(P0)
    # popt, pcov = curve_fit(func, df['v(mm/min)'].values, df['max average'].values,p0=P0)
    # print(popt)



    # plt.scatter(df['v(mm/min)'], df['max average'], label=masses[j])
    # plt.plot(df['v(mm/min)'].values, func(df['v(mm/min)'].values, *popt), label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
    # plt.plot(df['v(mm/min)'].values, func(df['v(mm/min)'].values, *popt))
    # plt.plot(df['v(mm/min)'], df['min average'])


# plt.xlabel(r'$\mathrm{Speed \, (mm/min)}$')
# plt.ylabel(r'$\mathrm{Force \, (N)}$')
# plt.grid(linestyle='--',linewidth=0.4)
# plt.legend(title='$\mathrm{Mass \, (gram)}$', shadow=True, ncol=2)
# plt.tight_layout()
# plt.show()
# fig.savefig("20180614_kineticforce.pdf", bbox_inches='tight')
