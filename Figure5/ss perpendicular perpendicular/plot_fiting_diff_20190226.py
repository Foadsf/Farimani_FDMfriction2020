# you need to have xlrd installed 

import os
os.chdir(os.getcwd())

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

font = {'family' : 'serif',
        # 'weight' : 'bold',
        'size'   : 15}

plt.rc('font', **font)

# import seaborn as sns
# sns.set(rc={'figure.figsize':(10,5), "lines.linewidth": 2.5}, font_scale=0.8)
# # sns.set_context("paper")
# sns.set_style({'axes.facecolor':'ghostwhite', 'grid.color': '.8'})
# # plt.rc('text', usetex=True)
# # # plt.rc('font', family='serif')
fig = plt.gcf()
ax = fig.add_subplot(111)
fig.set_size_inches(10, 5)



ax.grid( linestyle='-', linewidth=0.5)

areas = [900, 1700, 2500]

file = "analysis_20190207_kinematic_fit.xlsx"

im = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

colors = ["b", "g", "r"]

for k, a in enumerate(areas):
    df1 = pd.read_excel(file, sheet_name = str(a))
    im[k][0] ,= ax.plot(df1.index, df1["a"] * 1000 / 9.81, label = str(a) + r" $\mu_k$ CA", marker = 'o', linewidth=2, color = colors[k])
    im[k][1] ,= ax.plot(df1.index, df1["b"] * 1000 / 9.81, label = str(a) + r" $\mu_k$ CA_Ex", linestyle = ':', linewidth=2, color = colors[k])
    im[k][2] ,= ax.plot(df1.index, df1["d"] * 1000 / 9.81, label = str(a) + r" $\alpha_k$ TB", linestyle = "-.", linewidth=2, color = colors[k])

plt.xlabel(r'Velocity (mm/min)')
plt.ylabel(r'Coefficients')

extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
legend_handle = [extra, extra, extra, extra, extra, im[0][0], im[0][1], im[0][1], extra, im[1][0], im[1][1], im[1][2], extra, im[2][0], im[2][1], im[2][2]]
label_row_1 = ["", "900", "1700", "2500"]
label_j_1 = [r"$\mu_k$ CA"]
label_j_2 = [r"$\mu_k$ Ex"]
label_j_3 = [r"$\alpha_k$ TB"]
label_empty = [""]

legend_labels = np.concatenate([label_row_1, label_j_1, label_empty * 3, label_j_2, label_empty * 3, label_j_3, label_empty * 3])
ax.legend(legend_handle, legend_labels, 
          loc = 3, ncol = 4, shadow = True, handletextpad = -2)


# plt.legend(shadow = True, ncol = 3)

plt.tight_layout()



plt.show()

fig.savefig("2 0190226_kinematic_fitDiff.pdf", bbox_inches='tight')
