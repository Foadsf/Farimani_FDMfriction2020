

import pandas as pd
import numpy as np
from scipy.signal import argrelextrema

import matplotlib.pyplot as plt

# import seaborn as sns
# sns.set(rc={'figure.figsize':(10,5)}, font_scale=1.5)
# sns.set_style({'axes.facecolor':'white', 'grid.color': '.8'})

# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')
fig = plt.gcf()
fig.set_size_inches(10, 5)

# font = {'family' : 'serif',
#         'weight' : 'bold',
#         'size'   : 20}

# plt.rc('font', **font)

# ax = fig.add_subplot(111)

plt.rc('text', usetex=True)
rc = {'figure.figsize':(10,5),
      'axes.facecolor':'white',
      'axes.grid' : True,
      'grid.color': '.8',
      'font.family':'serif',
      'font.size' : 20}
plt.rcParams.update(rc)




# mean absolute deviation function
def mad(data, axis=None):
    return np.mean(np.absolute(data - np.mean(data, axis)), axis)


j = 9
# for j in range(9,10):
#import data from xls
dfs = pd.read_excel("friction coeficient_232g.xls", sheet_name=j)
# print(j)

#clean up columns
dfs.columns=['time','strain','force','work']
dfs=dfs.drop(dfs.index[[0,1]])
maxmax=dfs['force'].max()
maxmax_strain=dfs[dfs['force']==maxmax].strain.values[0]

plt.plot(dfs['strain'], dfs['force'],label='data')

#clean up begining and end of data
dfs=dfs[dfs.strain>11]
# dfs=dfs[dfs.strain<29.975]

#find local minimum and maximum

n=7 # the bigger the more comparison width
dfs['max']=dfs.iloc[argrelextrema(dfs.force.values, np.greater_equal, order=n)[0],2]
dfs['min']=dfs.iloc[argrelextrema(dfs.force.values, np.less_equal, order=n)[0],2]


#removing the NaNs
dfs2=dfs.dropna(subset=['min'])
dfs3=dfs.dropna(subset=['max'])






#calculating the delta
pd.options.mode.chained_assignment = None  # default='warn'
dfs2['del']=dfs2.strain-dfs2.strain.shift(1)
dfs3['del']=dfs3.strain-dfs3.strain.shift(1)

#removing the too close points
dfs2=dfs2[dfs2['del']>0.5*dfs2['del'].mean()]
dfs3=dfs3[dfs3['del']>0.5*dfs3['del'].mean()]

# dfs2=dfs2[dfs2['del']<1.9*dfs2['del'].mean()]
# dfs3=dfs3[dfs3['del']<1.9*dfs3['del'].mean()]

#removing NaNs
dfs2=dfs2.dropna(subset=['del'])
dfs3=dfs3.dropna(subset=['del'])


dfs2=dfs2.drop(dfs2.index[[0]])

plt.scatter(dfs3['strain'], dfs3['max'],label='max', s=10, c='#d62728')
plt.scatter(dfs2['strain'], dfs2['min'],label='min', s=10, c='#2ca02c')

# print(dfs2.head())

#calculating mean frequency and mean absolute deviation
# print(dfs2['min'].mean(),dfs2['del'].mean(),mad(dfs2['del'].values))
# print(dfs3['max'].mean(),dfs3['del'].mean(),mad(dfs3['del'].values))
# max = dfs3['max'].mean()
# min = dfs2['min'].mean()

max = 0.39656458552493606
min = 0.22767364162774312

plt.plot([dfs3['strain'][dfs3.index[0]], dfs3['strain'][dfs3.index[-1]]], [max, max], c='#d62728', ls='--')
plt.plot([dfs2['strain'][dfs2.index[0]], dfs2['strain'][dfs2.index[-1]]], [min, min], c='#2ca02c', ls='--')



plt.text(20, max * 1.2, 'Local maxima', fontsize = 20, color = '#d62728' )
plt.text(20, min * 0.7, 'Local minima', fontsize = 20, color = '#2ca02c' )



plt.annotate("Break away",
            xy = (maxmax_strain, maxmax),
            xytext = (20, 0.7), 
            arrowprops = dict(arrowstyle = "->",
                            connectionstyle = "arc3", color = 'black'),
            )


plt.xlabel(r'Displacment $\mathrm{(mm)}$')
plt.ylabel(r'Force $\mathrm{(N)}$')
plt.grid(linestyle = '--', linewidth=0.4)
plt.legend(shadow = True, labelspacing = 0.2)

plt.tight_layout()

plt.show()
fig.savefig("20190426_232g.pdf", bbox_inches='tight')
