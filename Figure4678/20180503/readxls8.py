

import pandas as pd
# import numpy as np


import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig = plt.gcf()
fig.set_size_inches(10, 5)





dfs = pd.read_excel("friction coeficient_232g.xls", sheet_name=9)


#clean up columns
dfs.columns=['time','strain','force','work']
dfs=dfs.drop(dfs.index[[0,1]])

plt.plot(dfs['strain'], dfs['force'],label='data')







plt.xlabel(r'$Diplacment (mm)$')
plt.ylabel(r'$Force (N)$')
plt.grid()
plt.show()
