import numpy as np
data=np.loadtxt(open("maxs.csv", "rb"), delimiter=",")


from scipy.optimize import curve_fit
def func(x, a, b):
    return a*x+b

# for i in range(1,data.shape[0]):
#     popt, pcov = curve_fit(func, data[0,1:], data[i,1:])
#     print(popt)
#more analysis here :https://docs.google.com/spreadsheets/d/1KxZ268BXiSBpQhtVChAXfHQH8Jp43F_6o21CKUT_vic/edit?usp=sharing


# masses=[41, 53, 65, 77, 89, 136, 184, 232]

import matplotlib.pyplot as plt

fig = plt.gcf()
fig.set_size_inches(10, 5)
# plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


for i in range(1,data.shape[1]):
    plt.plot(data[1:,0],data[1:,i],label=data[0,i])
    # plt.plot(data[:,0], func(data[:,0], popt[i-1]), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))


plt.xlabel(r'$\mathrm{Speed \, (mm/min)}$')
plt.ylabel(r'$\mathrm{Force \, (N)}$')
plt.grid(linestyle='--',linewidth=0.4)
plt.legend(title='$\mathrm{Mass \, (gram)}$', shadow=True)

plt.show()
fig.savefig("20180614_staticforce.pdf", bbox_inches='tight')
