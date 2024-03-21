import numpy as np
data=np.loadtxt(open("maxs.csv", "rb"), delimiter=",")
error=data

for i in range(1,data.shape[0]):
    for j in range(1,data.shape[1]):
        error[i,j]=np.abs((0.03069111+0.002409869*data[0,j] +0.060945130*np.exp(0.00537238*data[0,j]-data[i,0]*(0.001118531+data[0,j]*8.5195/10**5))-data[i,j])/data[i,j])

error2=np.delete(error,(0),axis=0)
#print(error2[:,1:])


import matplotlib.pyplot as plt

for k in range(1,error2.shape[1]):
    plt.plot(error2[:,0],error2[:,k])

plt.xlabel(r'$Speed (mm/min)$')
plt.ylabel(r'$error (N)$')
#plt.legend()

# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# V,M=np.meshgrid(data[1:,0],data[0,1:])
# ax.scatter(V,M,error2[:,1:])



plt.show()
