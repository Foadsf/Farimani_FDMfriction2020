#from here https://matplotlib.org/examples/pylab_examples/plotfile_demo.html

import numpy as np
#data = np.genfromtxt('maxs.csv', delimiter=',', skiprows=1)
data=np.loadtxt(open("maxs.csv", "rb"), delimiter=",", skiprows=1)
# print(data[:,2])

from scipy.optimize import curve_fit
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# n=8

#P0=[0.02396, 0.000794588, 0.155454546]#n=1,B,41 -->0.03723443	0.00360051	0.15656625
#P0=[0.08381, 0.001792,	0.133327365]#n=2,C,53 --> 0.09784458 0.00404954 0.14446505
#P0=[0.05331,0.002212,	0.169842482]#n=3,D,65 --> 0.09244309 0.00492094 0.17046051
#P0=[0.1309591,0.0050975,0.195314914]#n=4,E,77 --> 0.13733666 0.00424766 0.18342563
#P0=[0.05705,0.0018875,0.232683748]#n=5,F,89 --> 0.14811608 0.01251445 0.23405213
#P0=[0.0453551,0.00115650,0.421260208]#n=6,G,136 --> 0.07954604 0.00438339 0.41118772
#P0=[0.07944,0.001745,0.479017377]#n=7,H,184 -->0.22525899 0.04912453 0.51072018
# P0=[0.171245,0.00297755,0.59199059]#n=8,I,232 -->0.17245647 0.00082356 0.54810724
#
# popt, pcov = curve_fit(func, data[:,0], data[:,n],p0=P0)
# print(popt)


# import os #https://stackoverflow.com/a/22282935/4999991
# cwd = os.getcwd()  # Get the current working directory (cwd)

# import matplotlib.cbook as cbook

# data = cbook.get_sample_data('%s/maxs.csv'%(cwd), asfileobj=False)

popt=[[0.03723443,0.00360051, 0.15656625],
[0.09784458, 0.00404954, 0.14446505],
[0.09244309, 0.00492094, 0.17046051],
[0.13733666, 0.00424766, 0.18342563],
[0.14811608, 0.01251445, 0.23405213],
[0.07954604, 0.00438339, 0.41118772],
[0.22525899, 0.04912453, 0.51072018],
[0.17245647, 0.00082356, 0.54810724]]

# print(*(popt[0]))

import matplotlib.pyplot as plt

for i in range(1,data.shape[1]):
    plt.scatter(data[1:,0],data[1:,i],label=data[0,i])
    plt.plot(data[:,0], func(data[:,0],*popt[i-1]))

# plt.plotfile(data, (0, 1,2,3,4,5,6,7,8),subplots=False)
#plt.plotfile(data, (0, 1))
# plt.plot(data[:,0],data[:,n],label='data')
# plt.plot(data[:,0], func(data[:,0], *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))



plt.xlabel(r'$Speed (mm/min)$')
plt.ylabel(r'$Force (N)$')
plt.legend()

plt.show()
