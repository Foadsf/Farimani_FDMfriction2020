#from here https://matplotlib.org/examples/pylab_examples/plotfile_demo.html

import numpy as np
#data = np.genfromtxt('maxs.csv', delimiter=',', skiprows=1)
data=np.loadtxt(open("maxs.csv", "rb"), delimiter=",", skiprows=1)
# print(data[:,2])

from scipy.optimize import curve_fit
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

n=5

#P0=[0.02396, 0.000794588, 0.155454546]#n=1
#P0=[0.08381, 0.001792,	0.133327365]#n=2
#P0=[0.05331,0.002212,	0.169842482]#n=3
#P0=[0.1309591,0.0050975,0.195314914]#n=4
P0=[0.05705,0.0018875,0.232683748]#n=5

popt, pcov = curve_fit(func, data[:,0], data[:,n],p0=P0)
print(popt)


# import os #https://stackoverflow.com/a/22282935/4999991
# cwd = os.getcwd()  # Get the current working directory (cwd)

# import matplotlib.cbook as cbook

# data = cbook.get_sample_data('%s/maxs.csv'%(cwd), asfileobj=False)

import matplotlib.pyplot as plt

# plt.plotfile(data, (0, 1,2,3,4,5,6,7,8),subplots=False)
#plt.plotfile(data, (0, 1))
plt.plot(data[:,0],data[:,n],label='data')
plt.plot(data[:,0], func(data[:,0], *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))


plt.xlabel(r'$Speed (mm/min)$')
plt.ylabel(r'$Force (N)$')
plt.legend()

plt.show()
