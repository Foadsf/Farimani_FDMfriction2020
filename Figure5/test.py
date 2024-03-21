import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
import math
import scipy as scipy
from pandas import ExcelWriter
from pandas import ExcelFile
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from math import exp
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from collections import OrderedDict
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

def func(x, a, b, c):
     return -a * np.exp(-b * x) + c

#xdata = np.linspace(50, 1800, 50)
xdata= np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])

gdata = np.array([0.71046543 ,0.60083622, 0.6807211 , 0.73851013, 0.65947509 ,0.57109183
 ,0.62038249 ,0.62888092 ,0.54729635 ,0.59063816 ,0.6356796 , 0.58808863
, 0.60848475])
y = func(xdata, -0.112108,  0.00292102, 0.5954171)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, gdata, 'b-', label='data')

popt, pcov = curve_fit(func, xdata, ydata)
popt=np.array([ -0.112108,  0.00292102,  0.5954171])
plt.plot(xdata, func(xdata, *popt), 'r-',
       label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
print(popt)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

a11 = 2.67455104e-01
a21 = -3.80891209e-05
b11 = 2.62039280e-01 
b21 = -4.42995077e-05
c11 = 3.44552925e-01
c21 = -2.17642606e-05

Coefficient3 = [a11,b11,c11]
Coefficient4 = [a21,b21,c21]

a12 = 3.68606360e-01
a22 = -3.90905404e-05
b12 = 3.83671707e-01
b22 = -3.67406309e-05
c12 = 4.41603551e-01
c22 = -5.97006986e-06
Coefficient5 = [a12, b12,c12]
Coefficient6 = [a22, b22,c22]

a13 = 5.3740813e-01
a23 = -3.6095127e-05
b13 = 4.99240321e-01
b23 = -1.41539119e-05
c13 = 6.00332326e-01
c23 = 2.61008515e-06
Coefficient7 = [a13, b13,c13]
Coefficient8 = [a23, b23,c23]

a14 = 6.64527272e-01
a24 = -4.77399834e-05
b14 = 6.51927722e-01
b24 = -4.85601191e-05
c14 = 7.43516507e-01
c24 = -3.07895212e-05
Coefficient9  = [a14, b14, c14]
Coefficient10 = [a24, b24, c24]

surface1 = [2500,900,1700]
def force7(surface1, d7, d8):
     return d7+d8*surface1
print(force)
p0 = [0.2, 0.1]
dc4,cov = curve_fit(force7,surface1,Coefficient4,p0)
print('tst6')
print(dc4)

surface1 = [2500,900,1700]
def force8(surface1, d9, d10):
     return d9+d10*surface1
print(force)
p0 = [0.2, 0.1]
dc5,cov = curve_fit(force8,surface1,Coefficient5,p0)
print('tst7')
print(dc5)

surface1 = [2500,900,1700]
def force9(surface1, d11, d12):
     return d11+d12*surface1
print(force)
p0 = [0.2, 0.1]
dc6,cov = curve_fit(force9,surface1,Coefficient6,p0)
print('tst8')
print(dc6)

surface1 = [2500,900,1700]
def force10(surface1, d13, d14):
     return d13+d14*surface1
print(force)
p0 = [0.2, 0.1]
dc7,cov = curve_fit(force10,surface1,Coefficient7,p0)
print('tst9')
print(dc7)

surface1 = [2500,900,1700]
def force11(surface1, d15, d16):
     return d15+d16*surface1
print(force)
p0 = [0.2, 0.1]
dc8,cov = curve_fit(force11,surface1,Coefficient8,p0)
print('tst10')
print(dc8)

surface1 = [2500,900,1700]
def force12(surface1, d17, d18):
     return d17+d18*surface1
print(force)
p0 = [0.2, 0.1]
dc9,cov = curve_fit(force12,surface1,Coefficient9,p0)
print('tst11')
print(dc9)

surface1 = [2500,900,1700]
def force13(surface1, d19, d20):
     return d19+d20*surface1
print(force)
p0 = [0.2, 0.1]
dc10,cov = curve_fit(force13,surface1,Coefficient10,p0)
print('tst12')
print(dc10)

d1  = 1.96129900e-01
d2  = 1.20572227e-05
d3  = -5.39128789e-06
d4  = -1.04627164e-08
d5  = 2.85594829e-01
d6  = 3.38486712e-06
d7  = -4.13161648e-05
d8  = 3.88149124e-09
d9  = 4.13967471e-01
d10 = -9.41584187e-06
d11 = -2.47702996e-05
d12 = -1.46869460e-09
d13 = 5.05106962e-01
d14 = 2.38548806e-05
d15 = 7.43288985e-06
d16 = -1.37132594e-08
d17 = 6.73270109e-01
d18 = 7.87473977e-06
d19 = -4.32346018e-05
d20 = 5.12584677e-10
