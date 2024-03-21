import numpy as np
data=np.loadtxt(open("maxs.csv", "rb"), delimiter=",")


from scipy.optimize import curve_fit
def func(x, a, b):
    return a*x+b

# for i in range(1,data.shape[0]):
#     popt, pcov = curve_fit(func, data[0,1:], data[i,1:])
#     print(popt)
#more analysis here :https://docs.google.com/spreadsheets/d/1KxZ268BXiSBpQhtVChAXfHQH8Jp43F_6o21CKUT_vic/edit?usp=sharing

import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=22)
fig = plt.gcf()
fig.set_size_inches(10, 5)

# import seaborn as sns
# sns.set()

for i in range(1,data.shape[0],3):
    plt.scatter(data[0,1:],data[i,1:],label=data[i,0],s=8)
    popt, pcov = curve_fit(func, data[0,1:], data[i,1:])
    x=np.insert(data[0,1:],0,0.,axis=0)
    plt.plot(x, func(x, *popt),'--',linewidth=1)#, 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt)

#
plt.xlabel(r'$\mathrm{Mass \, (gram)}$')
plt.ylabel(r'$\mathrm{Force \, (N)}$')
plt.grid(linestyle='--',linewidth=0.4)
plt.legend(title='$\mathrm{Velocity}$ \n $\mathrm{(mm/min)}$',shadow=True,  prop={'size': 12})#ncol=2,

plt.show()
# fig.savefig("20181005_F_mass.pdf", bbox_inches='tight')
