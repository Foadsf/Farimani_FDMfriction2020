import numpy as np
data=np.loadtxt(open("maxs.csv", "rb"), delimiter=",", skiprows=1)
error=data
# print(data[:,2])

import matplotlib.pyplot as plt

# plt.plotfile(data, (0, 1,2,3,4,5,6,7,8),subplots=False)
#plt.plotfile(data, (0, 1))
plt.plot(data[:,0],data[:,n],label='data')
plt.plot(data[:,0], func(data[:,0], *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))


plt.xlabel(r'$Speed (mm/min)$')
plt.ylabel(r'$Force (N)$')
plt.legend()

plt.show()
