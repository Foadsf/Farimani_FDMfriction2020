
import matplotlib.pyplot as plt
import seaborn as sns

# sns.set(rc={'figure.figsize':(10,5)}, font_scale=1.5)
# sns.set_style({'axes.facecolor':'white', 'grid.color': '.8', 'font.family':'Times New Roman'})
# sns.set_style({'axes.facecolor':'white', 'grid.color': '.8', 'font.family':'Times New Roman'})

rc = {'figure.figsize':(10,5),
      'axes.facecolor':'white',
      'axes.grid' : True,
      'grid.color': '.8',
      'font.family':'serif',
      'font.size' : 15}
plt.rcParams.update(rc)

# plt.rc('text', usetex=True)
# plt.rc('font', family='serif', size=22)
# fig = plt.gcf()
# fig.set_size_inches(10, 5)
#
# font = {'family' : 'serif',
#         # 'weight' : 'bold',
#         'size'   : 15}
#
# plt.rc('font', **font)




Data = sns.load_dataset("tips")



g = sns.lmplot(x="total_bill", y="tip", hue="smoker", data = Data, legend_out = False, aspect = 2)
g.set(xlabel = "independent", ylabel = "dependent")
sns.despine(fig=None, ax=None, top=False, right=False, left=False, bottom=False, offset=None, trim=False)

plt.show()




