import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


dfs = pd.read_excel("friction coeficient_41g.xls", sheet_name=4)
#clean up columns
dfs.columns=['time','strain','force','work']
dfs=dfs.drop(dfs.index[[0,1]])


plt.subplot(2, 1, 2)

plt.plot(dfs['strain'], dfs['force'])

autocorrelation = np.correlate(dfs['force'].values.astype(float),dfs['force'].values.astype(float),'same')[round(len(dfs['force'].values.astype(float))/2):]
plt.subplot(2, 1, 1)
plt.plot(autocorrelation)

plt.grid()
plt.show()