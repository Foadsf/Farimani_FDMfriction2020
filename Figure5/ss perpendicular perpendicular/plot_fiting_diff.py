# you need to have xlrd installed

import os
os.chdir(os.getcwd())

import pandas as pd
# import numpy as np

import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle
# extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

# import seaborn as sns
# sns.set(rc={'figure.figsize':(10,5)}, font_scale=1)
# sns.set_style({'axes.facecolor':'white', 'grid.color': '.8'})
# # sns.set_context("paper")
# sns.set_style({'axes.facecolor':'ghostwhite', 'grid.color': '.8'})
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig = plt.gcf()
# ax = fig.add_subplot(111)
fig.set_size_inches(10, 5)

font = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 20}

plt.rc('font', **font)

# plt.grid( linestyle='-', linewidth=0.5)

areas = [900, 1700, 2500]

file = "analysis_20190207_kinematic_fit.xlsx"

colors = ["b", "g", "r"]

for k, a in enumerate(areas):
    df1 = pd.read_excel(file, sheet_name = str(a))
    plt.plot(df1.index, df1["a"] * 1000 / 9.81, label = str(a) + r" $\mu_k$ CA", marker = 'o', linewidth=2, color = colors[k])
    plt.plot(df1.index, df1["b"] * 1000 / 9.81, label = str(a) + r" $\mu_k$ Ex", linestyle = ':', linewidth=2, color = colors[k])
    plt.plot(df1.index, df1["d"] * 1000 / 9.81, label = str(a) + r" $\alpha_k$ TB", linestyle = "-.", linewidth=2, color = colors[k])

plt.xlabel(r'Velocity (mm/min)')
plt.ylabel(r'Coefficients')


plt.grid(linestyle = '--', linewidth=0.4)
plt.legend(shadow = True, ncol = 3, loc = 'upper right', labelspacing = 0.2, columnspacing = 0.2, borderpad = 0.2, prop={'size': 15})

plt.tight_layout()



plt.show()

fig.savefig("20190305_kinematic_fitDiff.pdf", bbox_inches='tight')
