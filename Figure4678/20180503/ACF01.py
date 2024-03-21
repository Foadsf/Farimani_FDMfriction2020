import pandas as pd
# import numpy as np

from matplotlib import pyplot

from  statsmodels.graphics.tsaplots import plot_acf
from	statsmodels.tsa.stattools	import	acf 

# for j in range(3,5):
dfs = pd.read_excel("friction coeficient_41g.xls", sheet_name=5)
#clean up columns
dfs.columns=['time','strain','force','work']
dfs=dfs.drop(dfs.index[[0,1]])

print(acf(dfs['force'].values.astype(float)))

# plot_acf(dfs['force'].values.astype(float), lags=200)

# pyplot.grid()
# pyplot.show()