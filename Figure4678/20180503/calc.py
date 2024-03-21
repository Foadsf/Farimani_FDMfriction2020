#surfdrive\sync\MyPhD\papers\firstjournal\20181102\actualFriction
# calculating the actual friction force from equations above

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline, InterpolatedUnivariateSpline # https://stackoverflow.com/questions/40226357/second-derivative-in-python-scipy-numpy-pandas

k = 10 ** 1.5
l0 = 0.3
d0 = 0.1
mp = 0.01
m = 0.041

# for i in range(5):
# k = 10 ** i

j = 0
dfs = pd.read_excel("friction coeficient_" + str(41) + "g.xls", sheet_name = j + 3)


#clean up columns
dfs.columns=['time','strain','force','work']
# print(dfs.head())
dfs=dfs.drop(dfs.index[[0,1]])
dfs = dfs.apply(pd.to_numeric)
dfs = dfs.groupby('time')['strain','force'].mean().reset_index()
# dfs = dfs.reindex()
# print(dfs.head())

t = dfs['time'].values.astype(float) * 60
F1 = dfs['force'].values.astype(float)
d = d0 + dfs['strain'].values.astype(float)/1000
del1 = F1 * d / (k + F1)
l1 = d - del1
l2 = l0 - l1
F2 = ((1 - (2 * mp - mp ** 2) ** 0.5) / (1 - mp)) * F1
del2 = F2 * l2 / k

# plt.plot(t, F2, label='F2')
# plt.plot(t, F1, label='F1')

x = - (del2 + l2)
x2 = np.maximum.accumulate(x)
x_spl = UnivariateSpline(t, x2, s = 0)

plt.plot(t, x, label = 'original')
plt.plot(t, x2, label = 'monotonic')
plt.plot(t, x_spl(t), label = 'smoothed')


# x_spl.set_smoothing_factor(0.5)
# x_spl = InterpolatedUnivariateSpline(t,x)
# x_spl_1d =  x_spl.derivative(n=1)
# plt.plot(t, x_spl_1d(t))

# x_spl_2d =  x_spl.derivative(n=2)
# Ff = F2 - m * x_spl_2d(t)
# plt.plot(d, Ff, label = 'actual')
# plt.plot(d, F1, label = 'measured')

# plt.plot(t, x_spl_2d(t))

plt.legend()
plt.show()



