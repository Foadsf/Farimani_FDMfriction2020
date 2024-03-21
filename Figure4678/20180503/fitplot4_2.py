# import numpy as np
# data=np.loadtxt(open("maxs.csv", "rb"), delimiter=",")

#%%

import matplotlib.pyplot as plt
import seaborn as sns
# sns.set()
# sns.set(rc={'figure.figsize':(10,5)}, font_scale=1.5)
# sns.set_style({'axes.facecolor':'white', 'grid.color': '.8', 'font.family':'Times New Roman'})


# plt.rc('text', usetex=True)
# plt.rc('font', family='serif', size=22)
# fig = plt.gcf()
# fig.set_size_inches(10, 5)

# font = {'family' : 'serif',
#         # 'weight' : 'bold',
#         'size'   : 15}

# plt.rc('font', **font)
plt.rc('text', usetex=True)
rc = {'figure.figsize':(10,5),
      'axes.facecolor':'white',
      'axes.grid' : True,
      'grid.color': '.8',
      'font.family':'serif',
      'font.size' : 20}
plt.rcParams.update(rc)



import pandas as pd
Data = pd.read_csv("maxs.csv", index_col='0')

Data = Data.T.reset_index()
Data = Data.apply(pd.to_numeric)
Data = Data.iloc[:,[0,1,4,7,10,13]]
Data = Data.melt('index', var_name='cols',  value_name='vals')


# sns.jointplot(x="index", y="vals", data=Data, kind="kde")

g = sns.lmplot(x = "index", y = "vals", hue = 'cols', data = Data, legend_out = False, aspect = 2)
g.set(xlabel = r'$\mathrm{Mass \, (gram)}$', ylabel = r'$\mathrm{Force \, (N)}$')
sns.despine(fig=None, ax=None, top=False, right=False, left=False, bottom=False, offset=None, trim=False)
# plt.xlabel(r'$\mathrm{Mass \, (gram)}$')
# plt.ylabel(r'$\mathrm{Force \, (N)}$')
# plt.grid(linestyle='--',linewidth=0.4)
plt.legend(title = '$\mathrm{Velocity}$ \n $\mathrm{(mm/min)}$', shadow = True, prop = {'size': 15})#ncol=2)
plt.tight_layout()
plt.show()


# from scipy.optimize import curve_fit
# def func(x, a, b):
#     return a*x+b

# for i in range(1,data.shape[0]):
#     popt, pcov = curve_fit(func, data[0,1:], data[i,1:])
#     print(popt)
#more analysis here :https://docs.google.com/spreadsheets/d/1KxZ268BXiSBpQhtVChAXfHQH8Jp43F_6o21CKUT_vic/edit?usp=sharing

# import matplotlib.pyplot as plt
# plt.rc('text', usetex=True)
# plt.rc('font', family='serif', size=22)
# fig = plt.gcf()
# fig.set_size_inches(10, 5)



# for i in range(1,data.shape[0],3):
#     plt.scatter(data[0,1:],data[i,1:],label=data[i,0],s=8)
#     popt, pcov = curve_fit(func, data[0,1:], data[i,1:])
#     x=np.insert(data[0,1:],0,0.,axis=0)
#     plt.plot(x, func(x, *popt),'--',linewidth=1)#, 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt)

# #
# plt.xlabel(r'$\mathrm{Mass \, (gram)}$')
# plt.ylabel(r'$\mathrm{Force \, (N)}$')
# plt.grid(linestyle='--',linewidth=0.4)
# plt.legend(title='$\mathrm{Velocity}$ \n $\mathrm{(mm/min)}$',shadow=True,  prop={'size': 12})#ncol=2,

# plt.show()
g.savefig("20190306_F_mass.pdf", transparent=True, bbox_inches='tight')


#%%
