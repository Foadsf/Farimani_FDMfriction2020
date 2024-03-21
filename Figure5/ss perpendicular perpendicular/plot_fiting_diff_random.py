import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(10,5), "lines.linewidth": 2.5}, font_scale=0.8)
sns.set_style({'axes.facecolor':'ghostwhite', 'grid.color': '.8'})
fig = plt.gcf()
fig.set_size_inches(10, 5)
font = {'family' : 'serif',
        'size'   : 19}
plt.rc('font', **font)
areas = [900, 1700, 2500]
n = 10
x = np.linspace(0.0, 3.0, num = n)

colors = ["b", "g", "r"]

for k, a in enumerate(areas):
    np.random.seed(1 * k * a)
    y1 = np.random.rand(n)
    plt.plot(x, y1, label = str(a) + r" $\mu_k$ CA", marker = 'o', color = colors[k])
    np.random.seed(2 * k * a)
    y2 = np.random.rand(n)
    plt.plot(x, y2, label = str(a) + r" $\mu_k$ CA_Ex", linestyle = ':', color = colors[k])
    np.random.seed(3 * k * a)
    y3 = np.random.rand(n)
    plt.plot(x, y3, label = str(a) + r" $\alpha_k$ TB", linestyle = "-.", color = colors[k])

plt.xlabel(r'Velocity $\mathrm{(mm/min)}$')
plt.legend(shadow = True, ncol = 3)
plt.tight_layout()
plt.show()
