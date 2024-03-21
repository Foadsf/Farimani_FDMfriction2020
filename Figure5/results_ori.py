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

df2  = pd.read_excel('ss parallel parallel/1700mm/1700mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('ss parallel parallel/1700mm/1700mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('ss parallel parallel/1700mm/1700mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('ss parallel parallel/1700mm/1700mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('ss parallel parallel/1700mm/1700mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('ss parallel parallel/1700mm/1700mm_800mm_min.xls' ,['Results'], header=0)
df8  = pd.read_excel('ss parallel parallel/1700mm/1700mm_600mm_min.xls' ,['Results'], header=0)
df9  = pd.read_excel('ss parallel parallel/1700mm/1700mm_400mm_min.xls' ,['Results'], header=0)
df10 = pd.read_excel('ss parallel parallel/1700mm/1700mm_300mm_min.xls' ,['Results'], header=0)
df11 = pd.read_excel('ss parallel parallel/1700mm/1700mm_200mm_min.xls' ,['Results'], header=0)
df12 = pd.read_excel('ss parallel parallel/1700mm/1700mm_150mm_min.xls' ,['Results'], header=0)
df13 = pd.read_excel('ss parallel parallel/1700mm/1700mm_100mm_min.xls' ,['Results'], header=0)
df14 = pd.read_excel('ss parallel parallel/1700mm/1700mm_50mm_min.xls'  ,['Results'], header=0)

BF1800 =  df2['Results']['Fmax'].iloc[1:]
BF1600 =  df3['Results']['Fmax'].iloc[1:]
BF1400 =  df4['Results']['Fmax'].iloc[1:]
BF1200 =  df5['Results']['Fmax'].iloc[1:]
BF1000 =  df6['Results']['Fmax'].iloc[1:]
BF800  =  df7['Results']['Fmax'].iloc[1:]
BF600  =  df8['Results']['Fmax'].iloc[1:]
BF400  =  df9['Results']['Fmax'].iloc[1:]
BF300  = df10['Results']['Fmax'].iloc[1:]
BF200  = df11['Results']['Fmax'].iloc[1:]
BF150  = df12['Results']['Fmax'].iloc[1:]
BF100  = df13['Results']['Fmax'].iloc[1:]
BF50   = df14['Results']['Fmax'].iloc[1:]

t = 4 # decides from which column the breakingforce is taken and thus the weight of the boxes during the tests
BF1800a = df2['Results']['Fmax'].iloc[1:][t]
BF1600a = df3['Results']['Fmax'].iloc[1:][t]
BF1400a = df4['Results']['Fmax'].iloc[1:][t]
BF1200a = df5['Results']['Fmax'].iloc[1:][t]
BF1000a = df6['Results']['Fmax'].iloc[1:][t]
BF800a  = df7['Results']['Fmax'].iloc[1:][t]
BF600a  = df8['Results']['Fmax'].iloc[1:][t]
BF400a  = df9['Results']['Fmax'].iloc[1:][t]
BF300a  = df10['Results']['Fmax'].iloc[1:][t]
BF200a  = df11['Results']['Fmax'].iloc[1:][t]
BF150a  = df12['Results']['Fmax'].iloc[1:][t]
BF100a  = df13['Results']['Fmax'].iloc[1:][t]
BF50a   = df14['Results']['Fmax'].iloc[1:][t]


Mass     = [51,87,135,195,243]
Velocity = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]

Breakingforce = np.matrix([BF50,BF100,BF150,BF200,BF300,BF400,BF600,BF800,BF1000,BF1200,BF1400,BF1600,BF1800])
print('Breakingforce')

df2  = pd.read_excel('ss parallel parallel/900mm/900mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('ss parallel parallel/900mm/900mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('ss parallel parallel/900mm/900mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('ss parallel parallel/900mm/900mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('ss parallel parallel/900mm/900mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('ss parallel parallel/900mm/900mm_800mm_min.xls' ,['Results'], header=0)
df8  = pd.read_excel('ss parallel parallel/900mm/900mm_600mm_min.xls' ,['Results'], header=0)
df9  = pd.read_excel('ss parallel parallel/900mm/900mm_400mm_min.xls' ,['Results'], header=0)
df10 = pd.read_excel('ss parallel parallel/900mm/900mm_300mm_min.xls' ,['Results'], header=0)
df11 = pd.read_excel('ss parallel parallel/900mm/900mm_200mm_min.xls' ,['Results'], header=0)
df12 = pd.read_excel('ss parallel parallel/900mm/900mm_150mm_min.xls' ,['Results'], header=0)
df13 = pd.read_excel('ss parallel parallel/900mm/900mm_100mm_min.xls' ,['Results'], header=0)
df14 = pd.read_excel('ss parallel parallel/900mm/900mm_50mm_min.xls'  ,['Results'], header=0)

BF18009 =  df2['Results']['Fmax'].iloc[1:]
BF16009 =  df3['Results']['Fmax'].iloc[1:]
BF14009 =  df4['Results']['Fmax'].iloc[1:]
BF12009 =  df5['Results']['Fmax'].iloc[1:]
BF10009 =  df6['Results']['Fmax'].iloc[1:]
BF8009  =  df7['Results']['Fmax'].iloc[1:]
BF6009  =  df8['Results']['Fmax'].iloc[1:]
BF4009  =  df9['Results']['Fmax'].iloc[1:]
BF3009  = df10['Results']['Fmax'].iloc[1:]
BF2009  = df11['Results']['Fmax'].iloc[1:]
BF1509  = df12['Results']['Fmax'].iloc[1:]
BF1009  = df13['Results']['Fmax'].iloc[1:]
BF509   = df14['Results']['Fmax'].iloc[1:]

BF18009a = df2['Results']['Fmax'].iloc[1:][t]
BF16009a = df3['Results']['Fmax'].iloc[1:][t]
BF14009a = df4['Results']['Fmax'].iloc[1:][t]
BF12009a = df5['Results']['Fmax'].iloc[1:][t]
BF10009a = df6['Results']['Fmax'].iloc[1:][t]
BF8009a  = df7['Results']['Fmax'].iloc[1:][t]
BF6009a  = df8['Results']['Fmax'].iloc[1:][t]
BF4009a  = df9['Results']['Fmax'].iloc[1:][t]
BF3009a  = df10['Results']['Fmax'].iloc[1:][t]
BF2009a  = df11['Results']['Fmax'].iloc[1:][t]
BF1509a  = df12['Results']['Fmax'].iloc[1:][t]
BF1009a  = df13['Results']['Fmax'].iloc[1:][t]
BF509a   = df14['Results']['Fmax'].iloc[1:][t]

Mass2            = [44,80,128,188,236]
Velocity2        = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
Breakingforce2   = np.matrix([BF509,BF1009,BF1509,BF2009,BF3009,BF4009,BF6009,BF8009,BF10009,BF12009,BF14009,BF16009,BF18009])

BF44  = Breakingforce2[:,0]
BF80  = Breakingforce2[:,1]
BF128 = Breakingforce2[:,2]
BF188 = Breakingforce2[:,3]
BF236 = Breakingforce2[:,4]

df2  = pd.read_excel('ss parallel parallel/2500mm/2500mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('ss parallel parallel/2500mm/2500mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('ss parallel parallel/2500mm/2500mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('ss parallel parallel/2500mm/2500mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('ss parallel parallel/2500mm/2500mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('ss parallel parallel/2500mm/2500mm_800mm_min.xls' ,['Results'], header=0)
df8  = pd.read_excel('ss parallel parallel/2500mm/2500mm_600mm_min.xls' ,['Results'], header=0)
df9  = pd.read_excel('ss parallel parallel/2500mm/2500mm_400mm_min.xls' ,['Results'], header=0)
df10 = pd.read_excel('ss parallel parallel/2500mm/2500mm_300mm_min.xls' ,['Results'], header=0)
df11 = pd.read_excel('ss parallel parallel/2500mm/2500mm_200mm_min.xls' ,['Results'], header=0)
df12 = pd.read_excel('ss parallel parallel/2500mm/2500mm_150mm_min.xls' ,['Results'], header=0)
df13 = pd.read_excel('ss parallel parallel/2500mm/2500mm_100mm_min.xls' ,['Results'], header=0)
df14 = pd.read_excel('ss parallel parallel/2500mm/2500mm_50mm_min.xls'  ,['Results'], header=0)

BF180025 =  df2['Results']['Fmax'].iloc[1:]
BF160025 =  df3['Results']['Fmax'].iloc[1:]
BF140025 =  df4['Results']['Fmax'].iloc[1:]
BF120025 =  df5['Results']['Fmax'].iloc[1:]
BF100025 =  df6['Results']['Fmax'].iloc[1:]
BF80025  =  df7['Results']['Fmax'].iloc[1:]
BF60025  =  df8['Results']['Fmax'].iloc[1:]
BF40025  =  df9['Results']['Fmax'].iloc[1:]
BF30025  = df10['Results']['Fmax'].iloc[1:]
BF20025  = df11['Results']['Fmax'].iloc[1:]
BF15025  = df12['Results']['Fmax'].iloc[1:]
BF10025  = df13['Results']['Fmax'].iloc[1:]
BF5025   = df14['Results']['Fmax'].iloc[1:]

BF180025a = df2['Results']['Fmax'].iloc[1:][t]
BF160025a = df3['Results']['Fmax'].iloc[1:][t]
BF140025a = df4['Results']['Fmax'].iloc[1:][t]
BF120025a = df5['Results']['Fmax'].iloc[1:][t]
BF100025a = df6['Results']['Fmax'].iloc[1:][t]
BF80025a  = df7['Results']['Fmax'].iloc[1:][t]
BF60025a  = df8['Results']['Fmax'].iloc[1:][t]
BF40025a  = df9['Results']['Fmax'].iloc[1:][t]
BF30025a  = df10['Results']['Fmax'].iloc[1:][t]
BF20025a  = df11['Results']['Fmax'].iloc[1:][t]
BF15025a  = df12['Results']['Fmax'].iloc[1:][t]
BF10025a  = df13['Results']['Fmax'].iloc[1:][t]
BF5025a   = df14['Results']['Fmax'].iloc[1:][t]


Mass3     = [47,83,131,191,239]
Velocity3 = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
Breakingforce3 = np.matrix([BF5025,BF10025,BF15025,BF20025,BF30025,BF40025,BF60025,BF80025,BF100025,BF120025,BF140025,BF160025,BF180025])
Mass3, Velocity3 = np.meshgrid(Mass3, Velocity3)


Breakparper     = np.matrix([BF1009,BF100,BF10025])#varying Weight and surface areas, same orientation and sliding speed
Surfacearea1 = [ 900, 1700, 2500]
Massavg     = [ 47, 83, 132, 192, 241]
Massavg, Surfacearea1,  = np.meshgrid(Massavg,Surfacearea1, )

test = pd.DataFrame({'1800':[BF18009a,BF1800a,BF180025a], '1600':[BF16009a,BF1600a,BF160025a], '1400':[BF14009a,BF1400a,BF140025a]
                     , '1200':[BF12009a,BF1200a,BF120025a], '1000':[BF10009a,BF1000a,BF100025a], '800':[BF8009a,BF800a,BF80025a]
                     , '600':[BF6009a,BF600a,BF60025a], '400':[BF4009a,BF400a,BF40025a], '300':[BF3009a,BF300a,BF30025a]
                     , '200':[BF2009a,BF200a,BF20025a], '150':[BF1509a,BF150a,BF20025a], '100':[BF1009a,BF100a,BF15025a]
                     , '50':[BF509a,BF50a,BF5025a]})
print('test')
print(test)
para1  = test['1800'].iloc[0:]
para2  = test['1600'].iloc[0:]
para3  = test['1400'].iloc[0:]
para4  = test['1200'].iloc[0:]
para5  = test['1000'].iloc[0:]
para6  = test['800'].iloc[0:]
para7  = test['600'].iloc[0:]
para8  = test['400'].iloc[0:]
para9  = test['300'].iloc[0:]
para10 = test['200'].iloc[0:]
para11 = test['150'].iloc[0:]
para12 = test['100'].iloc[0:]
para13 = test['50'].iloc[0:]
print('Breakingforce3')
print(Breakingforce3)
print('para2')
print(para2)
print(Mass3, Velocity3)
Surfacearea2= [900,1700,2500]
Velocity4 = [1800,1600,1400,1200,1000,800,600,400,300,200,150,100,50]
Surfacearea2,Velocity4 = np.meshgrid(Surfacearea2,Velocity4)
Break47= np.matrix([para1,para2,para3,para4,para5,para6,para7,para8,para9,para10,para11,para12,para13])

print('Break47')
print(Break47)
print(Surfacearea2,Velocity4)


df2  = pd.read_excel('ss parallel perpendicular/1700mm/1700mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('ss parallel perpendicular/1700mm/1700mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('ss parallel perpendicular/1700mm/1700mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('ss parallel perpendicular/1700mm/1700mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('ss parallel perpendicular/1700mm/1700mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('ss parallel perpendicular/1700mm/1700mm_800mm_min.xls' ,['Results'], header=0)
df8  = pd.read_excel('ss parallel perpendicular/1700mm/1700mm_600mm_min.xls' ,['Results'], header=0)
df9  = pd.read_excel('ss parallel perpendicular/1700mm/1700mm_400mm_min.xls' ,['Results'], header=0)
df10 = pd.read_excel('ss parallel perpendicular/1700mm/1700mm_300mm_min.xls' ,['Results'], header=0)
df11 = pd.read_excel('ss parallel perpendicular/1700mm/1700mm_200mm_min.xls' ,['Results'], header=0)
df12 = pd.read_excel('ss parallel perpendicular/1700mm/1700mm_150mm_min.xls' ,['Results'], header=0)
df13 = pd.read_excel('ss parallel perpendicular/1700mm/1700mm_100mm_min.xls' ,['Results'], header=0)
df14 = pd.read_excel('ss parallel perpendicular/1700mm/1700mm_50mm_min.xls'  ,['Results'], header=0)

BF1800b =  df2['Results']['Fmax'].iloc[1:]
BF1600b =  df3['Results']['Fmax'].iloc[1:]
BF1400b =  df4['Results']['Fmax'].iloc[1:]
BF1200b =  df5['Results']['Fmax'].iloc[1:]
BF1000b =  df6['Results']['Fmax'].iloc[1:]
BF800b  =  df7['Results']['Fmax'].iloc[1:]
BF600b  =  df8['Results']['Fmax'].iloc[1:]
BF400b  =  df9['Results']['Fmax'].iloc[1:]
BF300b  = df10['Results']['Fmax'].iloc[1:]
BF200b  = df11['Results']['Fmax'].iloc[1:]
BF150b  = df12['Results']['Fmax'].iloc[1:]
BF100b  = df13['Results']['Fmax'].iloc[1:]
BF50b   = df14['Results']['Fmax'].iloc[1:]

 # t decides from which column the breakingforce is taken and thus the weight of the boxes during the tests
BF1800ab = df2['Results']['Fmax'].iloc[1:][t]
BF1600ab = df3['Results']['Fmax'].iloc[1:][t]
BF1400ab = df4['Results']['Fmax'].iloc[1:][t]
BF1200ab = df5['Results']['Fmax'].iloc[1:][t]
BF1000ab = df6['Results']['Fmax'].iloc[1:][t]
BF800ab  = df7['Results']['Fmax'].iloc[1:][t]
BF600ab  = df8['Results']['Fmax'].iloc[1:][t]
BF400ab  = df9['Results']['Fmax'].iloc[1:][t]
BF300ab  = df10['Results']['Fmax'].iloc[1:][t]
BF200ab  = df11['Results']['Fmax'].iloc[1:][t]
BF150ab  = df12['Results']['Fmax'].iloc[1:][t]
BF100ab  = df13['Results']['Fmax'].iloc[1:][t]
BF50ab   = df14['Results']['Fmax'].iloc[1:][t]


Mass     = [51,87,135,195,243]
Velocity = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
print(Mass)
print(Velocity)

Breakingforce = np.matrix([BF50b,BF100b,BF150b,BF200b,BF300b,BF400b,BF600b,BF800b,BF1000b,BF1200b,BF1400b,BF1600b,BF1800b])
print('Breakingforce')
print(Breakingforce)

df2  = pd.read_excel('ss parallel perpendicular/900mm/900mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('ss parallel perpendicular/900mm/900mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('ss parallel perpendicular/900mm/900mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('ss parallel perpendicular/900mm/900mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('ss parallel perpendicular/900mm/900mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('ss parallel perpendicular/900mm/900mm_800mm_min.xls' ,['Results'], header=0)
df8  = pd.read_excel('ss parallel perpendicular/900mm/900mm_600mm_min.xls' ,['Results'], header=0)
df9  = pd.read_excel('ss parallel perpendicular/900mm/900mm_400mm_min.xls' ,['Results'], header=0)
df10 = pd.read_excel('ss parallel perpendicular/900mm/900mm_300mm_min.xls' ,['Results'], header=0)
df11 = pd.read_excel('ss parallel perpendicular/900mm/900mm_200mm_min.xls' ,['Results'], header=0)
df12 = pd.read_excel('ss parallel perpendicular/900mm/900mm_150mm_min.xls' ,['Results'], header=0)
df13 = pd.read_excel('ss parallel perpendicular/900mm/900mm_100mm_min.xls' ,['Results'], header=0)
df14 = pd.read_excel('ss parallel perpendicular/900mm/900mm_50mm_min.xls'  ,['Results'], header=0)

BF18009b =  df2['Results']['Fmax'].iloc[1:]
BF16009b =  df3['Results']['Fmax'].iloc[1:]
BF14009b =  df4['Results']['Fmax'].iloc[1:]
BF12009b =  df5['Results']['Fmax'].iloc[1:]
BF10009b =  df6['Results']['Fmax'].iloc[1:]
BF8009b  =  df7['Results']['Fmax'].iloc[1:]
BF6009b  =  df8['Results']['Fmax'].iloc[1:]
BF4009b  =  df9['Results']['Fmax'].iloc[1:]
BF3009b  = df10['Results']['Fmax'].iloc[1:]
BF2009b  = df11['Results']['Fmax'].iloc[1:]
BF1509b  = df12['Results']['Fmax'].iloc[1:]
BF1009b  = df13['Results']['Fmax'].iloc[1:]
BF509b   = df14['Results']['Fmax'].iloc[1:]

BF18009ab = df2['Results']['Fmax'].iloc[1:][t]
BF16009ab = df3['Results']['Fmax'].iloc[1:][t]
BF14009ab = df4['Results']['Fmax'].iloc[1:][t]
BF12009ab = df5['Results']['Fmax'].iloc[1:][t]
BF10009ab = df6['Results']['Fmax'].iloc[1:][t]
BF8009ab  = df7['Results']['Fmax'].iloc[1:][t]
BF6009ab  = df8['Results']['Fmax'].iloc[1:][t]
BF4009ab  = df9['Results']['Fmax'].iloc[1:][t]
BF3009ab  = df10['Results']['Fmax'].iloc[1:][t]
BF2009ab  = df11['Results']['Fmax'].iloc[1:][t]
BF1509ab  = df12['Results']['Fmax'].iloc[1:][t]
BF1009ab  = df13['Results']['Fmax'].iloc[1:][t]
BF509ab   = df14['Results']['Fmax'].iloc[1:][t]

Mass2            = [44,80,128,188,236]
Velocity2        = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
Breakingforce2   = np.matrix([BF509,BF1009,BF1509,BF2009,BF3009,BF4009,BF6009,BF8009,BF10009,BF12009,BF14009,BF16009,BF18009])

BF44b  = Breakingforce2[:,0]
BF80b  = Breakingforce2[:,1]
BF128b = Breakingforce2[:,2]
BF188b = Breakingforce2[:,3]
BF236b = Breakingforce2[:,4]

df2  = pd.read_excel('ss parallel perpendicular/2500mm/2500mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('ss parallel perpendicular/2500mm/2500mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('ss parallel perpendicular/2500mm/2500mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('ss parallel perpendicular/2500mm/2500mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('ss parallel perpendicular/2500mm/2500mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('ss parallel perpendicular/2500mm/2500mm_800mm_min.xls' ,['Results'], header=0)
df8  = pd.read_excel('ss parallel perpendicular/2500mm/2500mm_600mm_min.xls' ,['Results'], header=0)
df9  = pd.read_excel('ss parallel perpendicular/2500mm/2500mm_400mm_min.xls' ,['Results'], header=0)
df10 = pd.read_excel('ss parallel perpendicular/2500mm/2500mm_300mm_min.xls' ,['Results'], header=0)
df11 = pd.read_excel('ss parallel perpendicular/2500mm/2500mm_200mm_min.xls' ,['Results'], header=0)
df12 = pd.read_excel('ss parallel perpendicular/2500mm/2500mm_150mm_min.xls' ,['Results'], header=0)
df13 = pd.read_excel('ss parallel perpendicular/2500mm/2500mm_100mm_min.xls' ,['Results'], header=0)
df14 = pd.read_excel('ss parallel perpendicular/2500mm/2500mm_50mm_min.xls'  ,['Results'], header=0)

BF180025b =  df2['Results']['Fmax'].iloc[1:]
BF160025b =  df3['Results']['Fmax'].iloc[1:]
BF140025b =  df4['Results']['Fmax'].iloc[1:]
BF120025b =  df5['Results']['Fmax'].iloc[1:]
BF100025b =  df6['Results']['Fmax'].iloc[1:]
BF80025b  =  df7['Results']['Fmax'].iloc[1:]
BF60025b  =  df8['Results']['Fmax'].iloc[1:]
BF40025b  =  df9['Results']['Fmax'].iloc[1:]
BF30025b  = df10['Results']['Fmax'].iloc[1:]
BF20025b  = df11['Results']['Fmax'].iloc[1:]
BF15025b  = df12['Results']['Fmax'].iloc[1:]
BF10025b  = df13['Results']['Fmax'].iloc[1:]
BF5025b   = df14['Results']['Fmax'].iloc[1:]

BF180025ab = df2['Results']['Fmax'].iloc[1:][t]
BF160025ab = df3['Results']['Fmax'].iloc[1:][t]
BF140025ab = df4['Results']['Fmax'].iloc[1:][t]
BF120025ab = df5['Results']['Fmax'].iloc[1:][t]
BF100025ab = df6['Results']['Fmax'].iloc[1:][t]
BF80025ab  = df7['Results']['Fmax'].iloc[1:][t]
BF60025ab  = df8['Results']['Fmax'].iloc[1:][t]
BF40025ab  = df9['Results']['Fmax'].iloc[1:][t]
BF30025ab  = df10['Results']['Fmax'].iloc[1:][t]
BF20025ab  = df11['Results']['Fmax'].iloc[1:][t]
BF15025ab  = df12['Results']['Fmax'].iloc[1:][t]
BF10025ab  = df13['Results']['Fmax'].iloc[1:][t]
BF5025ab   = df14['Results']['Fmax'].iloc[1:][t]




df2  = pd.read_excel('ss perpendicular perpendicular/1700mm/1700mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('ss perpendicular perpendicular/1700mm/1700mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('ss perpendicular perpendicular/1700mm/1700mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('ss perpendicular perpendicular/1700mm/1700mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('ss perpendicular perpendicular/1700mm/1700mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('ss perpendicular perpendicular/1700mm/1700mm_800mm_min.xls' ,['Results'], header=0)
df8  = pd.read_excel('ss perpendicular perpendicular/1700mm/1700mm_600mm_min.xls' ,['Results'], header=0)
df10 = pd.read_excel('ss perpendicular perpendicular/1700mm/1700mm_300mm_min.xls' ,['Results'], header=0)
df11 = pd.read_excel('ss perpendicular perpendicular/1700mm/1700mm_200mm_min.xls' ,['Results'], header=0)
df12 = pd.read_excel('ss perpendicular perpendicular/1700mm/1700mm_150mm_min.xls' ,['Results'], header=0)
df13 = pd.read_excel('ss perpendicular perpendicular/1700mm/1700mm_100mm_min.xls' ,['Results'], header=0)
df14 = pd.read_excel('ss perpendicular perpendicular/1700mm/1700mm_50mm_min.xls'  ,['Results'], header=0)

BF1800c =  df2['Results']['Fmax'].iloc[1:]
BF1600c =  df3['Results']['Fmax'].iloc[1:]
BF1400c =  df4['Results']['Fmax'].iloc[1:]
BF1200c =  df5['Results']['Fmax'].iloc[1:]
BF1000c =  df6['Results']['Fmax'].iloc[1:]
BF800c  =  df7['Results']['Fmax'].iloc[1:]
BF600c  =  df8['Results']['Fmax'].iloc[1:]
BF400c  =  df9['Results']['Fmax'].iloc[1:]
BF300c  = df10['Results']['Fmax'].iloc[1:]
BF200c  = df11['Results']['Fmax'].iloc[1:]
BF150c  = df12['Results']['Fmax'].iloc[1:]
BF100c  = df13['Results']['Fmax'].iloc[1:]
BF50c   = df14['Results']['Fmax'].iloc[1:]

 # t decides from which column the breakingforce is taken and thus the weight of the boxes during the tests
BF1800ac = df2['Results']['Fmax'].iloc[1:][t]
BF1600ac = df3['Results']['Fmax'].iloc[1:][t]
BF1400ac = df4['Results']['Fmax'].iloc[1:][t]
BF1200ac = df5['Results']['Fmax'].iloc[1:][t]
BF1000ac = df6['Results']['Fmax'].iloc[1:][t]
BF800ac  = df7['Results']['Fmax'].iloc[1:][t]
BF600ac  = df8['Results']['Fmax'].iloc[1:][t]
BF400ac  = df9['Results']['Fmax'].iloc[1:][t]
BF300ac  = df10['Results']['Fmax'].iloc[1:][t]
BF200ac  = df11['Results']['Fmax'].iloc[1:][t]
BF150ac  = df12['Results']['Fmax'].iloc[1:][t]
BF100ac  = df13['Results']['Fmax'].iloc[1:][t]
BF50ac   = df14['Results']['Fmax'].iloc[1:][t]


Mass     = [51,87,135,195,243]
Velocity = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
print(Mass)
print(Velocity)

Breakingforce = np.matrix([BF50,BF100,BF150,BF200,BF300,BF400,BF600,BF800,BF1000,BF1200,BF1400,BF1600,BF1800])
print('Breakingforce')
print(Breakingforce)

df2  = pd.read_excel('ss perpendicular perpendicular/900mm/900mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('ss perpendicular perpendicular/900mm/900mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('ss perpendicular perpendicular/900mm/900mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('ss perpendicular perpendicular/900mm/900mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('ss perpendicular perpendicular/900mm/900mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('ss perpendicular perpendicular/900mm/900mm_800mm_min.xls' ,['Results'], header=0)
df8  = pd.read_excel('ss perpendicular perpendicular/900mm/900mm_600mm_min.xls' ,['Results'], header=0)
df9  = pd.read_excel('ss perpendicular perpendicular/900mm/900mm_400mm_min.xls' ,['Results'], header=0)
df10 = pd.read_excel('ss perpendicular perpendicular/900mm/900mm_300mm_min.xls' ,['Results'], header=0)
df11 = pd.read_excel('ss perpendicular perpendicular/900mm/900mm_200mm_min.xls' ,['Results'], header=0)
df12 = pd.read_excel('ss perpendicular perpendicular/900mm/900mm_150mm_min.xls' ,['Results'], header=0)
df13 = pd.read_excel('ss perpendicular perpendicular/900mm/900mm_100mm_min.xls' ,['Results'], header=0)
df14 = pd.read_excel('ss perpendicular perpendicular/900mm/900mm_50mm_min.xls'  ,['Results'], header=0)

BF18009c =  df2['Results']['Fmax'].iloc[1:]
BF16009c =  df3['Results']['Fmax'].iloc[1:]
BF14009c =  df4['Results']['Fmax'].iloc[1:]
BF12009c =  df5['Results']['Fmax'].iloc[1:]
BF10009c =  df6['Results']['Fmax'].iloc[1:]
BF8009c  =  df7['Results']['Fmax'].iloc[1:]
BF6009c  =  df8['Results']['Fmax'].iloc[1:]
BF4009c  =  df9['Results']['Fmax'].iloc[1:]
BF3009c  = df10['Results']['Fmax'].iloc[1:]
BF2009c  = df11['Results']['Fmax'].iloc[1:]
BF1509c  = df12['Results']['Fmax'].iloc[1:]
BF1009c  = df13['Results']['Fmax'].iloc[1:]
BF509c   = df14['Results']['Fmax'].iloc[1:]

BF18009ac = df2['Results']['Fmax'].iloc[1:][t]
BF16009ac = df3['Results']['Fmax'].iloc[1:][t]
BF14009ac = df4['Results']['Fmax'].iloc[1:][t]
BF12009ac = df5['Results']['Fmax'].iloc[1:][t]
BF10009ac = df6['Results']['Fmax'].iloc[1:][t]
BF8009ac  = df7['Results']['Fmax'].iloc[1:][t]
BF6009ac  = df8['Results']['Fmax'].iloc[1:][t]
BF4009ac  = df9['Results']['Fmax'].iloc[1:][t]
BF3009ac  = df10['Results']['Fmax'].iloc[1:][t]
BF2009ac  = df11['Results']['Fmax'].iloc[1:][t]
BF1509ac  = df12['Results']['Fmax'].iloc[1:][t]
BF1009ac  = df13['Results']['Fmax'].iloc[1:][t]
BF509ac   = df14['Results']['Fmax'].iloc[1:][t]

Mass2            = [44,80,128,188,236]
Velocity2        = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
Breakingforce2   = np.matrix([BF509,BF1009,BF1509,BF2009,BF3009,BF4009,BF6009,BF8009,BF10009,BF12009,BF14009,BF16009,BF18009])

BF44  = Breakingforce2[:,0]
BF80  = Breakingforce2[:,1]
BF128 = Breakingforce2[:,2]
BF188 = Breakingforce2[:,3]
BF236 = Breakingforce2[:,4]

df2  = pd.read_excel('ss perpendicular perpendicular/2500mm/2500mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('ss perpendicular perpendicular/2500mm/2500mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('ss perpendicular perpendicular/2500mm/2500mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('ss perpendicular perpendicular/2500mm/2500mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('ss perpendicular perpendicular/2500mm/2500mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('ss perpendicular perpendicular/2500mm/2500mm_800mm_min.xls' ,['Results'], header=0)
df8  = pd.read_excel('ss perpendicular perpendicular/2500mm/2500mm_600mm_min.xls' ,['Results'], header=0)
df9  = pd.read_excel('ss perpendicular perpendicular/2500mm/2500mm_400mm_min.xls' ,['Results'], header=0)
df10 = pd.read_excel('ss perpendicular perpendicular/2500mm/2500mm_300mm_min.xls' ,['Results'], header=0)
df11 = pd.read_excel('ss perpendicular perpendicular/2500mm/2500mm_200mm_min.xls' ,['Results'], header=0)
df12 = pd.read_excel('ss perpendicular perpendicular/2500mm/2500mm_150mm_min.xls' ,['Results'], header=0)
df13 = pd.read_excel('ss perpendicular perpendicular/2500mm/2500mm_100mm_min.xls' ,['Results'], header=0)
df14 = pd.read_excel('ss perpendicular perpendicular/2500mm/2500mm_50mm_min.xls'  ,['Results'], header=0)

BF180025c =  df2['Results']['Fmax'].iloc[1:]
BF160025c =  df3['Results']['Fmax'].iloc[1:]
BF140025c =  df4['Results']['Fmax'].iloc[1:]
BF120025c =  df5['Results']['Fmax'].iloc[1:]
BF100025c =  df6['Results']['Fmax'].iloc[1:]
BF80025c  =  df7['Results']['Fmax'].iloc[1:]
BF60025c  =  df8['Results']['Fmax'].iloc[1:]
BF40025c  =  df9['Results']['Fmax'].iloc[1:]
BF30025c  = df10['Results']['Fmax'].iloc[1:]
BF20025c  = df11['Results']['Fmax'].iloc[1:]
BF15025c  = df12['Results']['Fmax'].iloc[1:]
BF10025c  = df13['Results']['Fmax'].iloc[1:]
BF5025c   = df14['Results']['Fmax'].iloc[1:]

BF180025ac = df2['Results']['Fmax'].iloc[1:][t]
BF160025ac = df3['Results']['Fmax'].iloc[1:][t]
BF140025ac = df4['Results']['Fmax'].iloc[1:][t]
BF120025ac = df5['Results']['Fmax'].iloc[1:][t]
BF100025ac = df6['Results']['Fmax'].iloc[1:][t]
BF80025ac  = df7['Results']['Fmax'].iloc[1:][t]
BF60025ac  = df8['Results']['Fmax'].iloc[1:][t]
BF40025ac  = df9['Results']['Fmax'].iloc[1:][t]
BF30025ac  = df10['Results']['Fmax'].iloc[1:][t]
BF20025ac  = df11['Results']['Fmax'].iloc[1:][t]
BF15025ac  = df12['Results']['Fmax'].iloc[1:][t]
BF10025ac  = df13['Results']['Fmax'].iloc[1:][t]
BF5025ac   = df14['Results']['Fmax'].iloc[1:][t]


Mass3     = [47,83,131,191,239]
Velocity3 = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
Breakingforce3 = np.matrix([BF5025,BF10025,BF15025,BF20025,BF30025,BF40025,BF60025,BF80025,BF100025,BF120025,BF140025,BF160025,BF180025])
Mass3, Velocity3 = np.meshgrid(Mass3, Velocity3)


Breakparper     = np.matrix([BF1009,BF100,BF10025])#varying Weight and surface areas, same orientation and sliding speed
Surfacearea1 = [ 900, 1700, 2500]
Massavg     = [ 47, 83, 132, 192, 241]
Massavg, Surfacearea1,  = np.meshgrid(Massavg,Surfacearea1, )

df2  = pd.read_excel('bs perpendicular/1700mm/1700mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('bs perpendicular/1700mm/1700mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('bs perpendicular/1700mm/1700mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('bs perpendicular/1700mm/1700mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('bs perpendicular/1700mm/1700mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('bs perpendicular/1700mm/1700mm_800mm_min.xls' ,['Results'], header=0)
df8  = pd.read_excel('bs perpendicular/1700mm/1700mm_600mm_min.xls' ,['Results'], header=0)
df9  = pd.read_excel('bs perpendicular/1700mm/1700mm_400mm_min.xls' ,['Results'], header=0)
df10 = pd.read_excel('bs perpendicular/1700mm/1700mm_300mm_min.xls' ,['Results'], header=0)
df11 = pd.read_excel('bs perpendicular/1700mm/1700mm_200mm_min.xls' ,['Results'], header=0)
df12 = pd.read_excel('bs perpendicular/1700mm/1700mm_150mm_min.xls' ,['Results'], header=0)
df13 = pd.read_excel('bs perpendicular/1700mm/1700mm_100mm_min.xls' ,['Results'], header=0)
df14 = pd.read_excel('bs perpendicular/1700mm/1700mm_50mm_min.xls'  ,['Results'], header=0)

BF1800d =  df2['Results']['Fmax'].iloc[1:]
BF1600d =  df3['Results']['Fmax'].iloc[1:]
BF1400d =  df4['Results']['Fmax'].iloc[1:]
BF1200d =  df5['Results']['Fmax'].iloc[1:]
BF1000d =  df6['Results']['Fmax'].iloc[1:]
BF800d  =  df7['Results']['Fmax'].iloc[1:]
BF600d  =  df8['Results']['Fmax'].iloc[1:]
BF400d  =  df9['Results']['Fmax'].iloc[1:]
BF300d  = df10['Results']['Fmax'].iloc[1:]
BF200d  = df11['Results']['Fmax'].iloc[1:]
BF150d  = df12['Results']['Fmax'].iloc[1:]
BF100d  = df13['Results']['Fmax'].iloc[1:]
BF50d   = df14['Results']['Fmax'].iloc[1:]

 # decides from which column the breakingforce is taken and thus the weight of the boxes during the tests
BF1800ad = df2['Results']['Fmax'].iloc[1:][t]
BF1600ad = df3['Results']['Fmax'].iloc[1:][t]
BF1400ad = df4['Results']['Fmax'].iloc[1:][t]
BF1200ad = df5['Results']['Fmax'].iloc[1:][t]
BF1000ad = df6['Results']['Fmax'].iloc[1:][t]
BF800ad  = df7['Results']['Fmax'].iloc[1:][t]
BF600ad  = df8['Results']['Fmax'].iloc[1:][t]
BF400ad  = df9['Results']['Fmax'].iloc[1:][t]
BF300ad  = df10['Results']['Fmax'].iloc[1:][t]
BF200ad  = df11['Results']['Fmax'].iloc[1:][t]
BF150ad  = df12['Results']['Fmax'].iloc[1:][t]
BF100ad  = df13['Results']['Fmax'].iloc[1:][t]
BF50ad   = df14['Results']['Fmax'].iloc[1:][t]


Mass     = [51,87,135,195,243]
Velocity = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
print(Mass)
print(Velocity)

Breakingforce = np.matrix([BF50,BF100,BF150,BF200,BF300,BF400,BF600,BF800,BF1000,BF1200,BF1400,BF1600,BF1800])
print('Breakingforce')
print(Breakingforce)

df2  = pd.read_excel('bs perpendicular/900mm/900mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('bs perpendicular/900mm/900mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('bs perpendicular/900mm/900mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('bs perpendicular/900mm/900mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('bs perpendicular/900mm/900mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('bs perpendicular/900mm/900mm_800mm_min.xls' ,['Results'], header=0)
df8  = pd.read_excel('bs perpendicular/900mm/900mm_600mm_min.xls' ,['Results'], header=0)
df9  = pd.read_excel('bs perpendicular/900mm/900mm_400mm_min.xls' ,['Results'], header=0)
df10 = pd.read_excel('bs perpendicular/900mm/900mm_300mm_min.xls' ,['Results'], header=0)
df11 = pd.read_excel('bs perpendicular/900mm/900mm_200mm_min.xls' ,['Results'], header=0)
df12 = pd.read_excel('bs perpendicular/900mm/900mm_150mm_min.xls' ,['Results'], header=0)
df13 = pd.read_excel('bs perpendicular/900mm/900mm_100mm_min.xls' ,['Results'], header=0)
df14 = pd.read_excel('bs perpendicular/900mm/900mm_50mm_min.xls'  ,['Results'], header=0)

BF18009d =  df2['Results']['Fmax'].iloc[1:]
BF16009d =  df3['Results']['Fmax'].iloc[1:]
BF14009d =  df4['Results']['Fmax'].iloc[1:]
BF12009d =  df5['Results']['Fmax'].iloc[1:]
BF10009d =  df6['Results']['Fmax'].iloc[1:]
BF8009d  =  df7['Results']['Fmax'].iloc[1:]
BF6009d  =  df8['Results']['Fmax'].iloc[1:]
BF4009d  =  df9['Results']['Fmax'].iloc[1:]
BF3009d  = df10['Results']['Fmax'].iloc[1:]
BF2009d  = df11['Results']['Fmax'].iloc[1:]
BF1509d  = df12['Results']['Fmax'].iloc[1:]
BF1009d  = df13['Results']['Fmax'].iloc[1:]
BF509d   = df14['Results']['Fmax'].iloc[1:]

BF18009ad = df2['Results']['Fmax'].iloc[1:][t]
BF16009ad = df3['Results']['Fmax'].iloc[1:][t]
BF14009ad = df4['Results']['Fmax'].iloc[1:][t]
BF12009ad = df5['Results']['Fmax'].iloc[1:][t]
BF10009ad = df6['Results']['Fmax'].iloc[1:][t]
BF8009ad  = df7['Results']['Fmax'].iloc[1:][t]
BF6009ad  = df8['Results']['Fmax'].iloc[1:][t]
BF4009ad  = df9['Results']['Fmax'].iloc[1:][t]
BF3009ad  = df10['Results']['Fmax'].iloc[1:][t]
BF2009ad  = df11['Results']['Fmax'].iloc[1:][t]
BF1509ad  = df12['Results']['Fmax'].iloc[1:][t]
BF1009ad  = df13['Results']['Fmax'].iloc[1:][t]
BF509ad   = df14['Results']['Fmax'].iloc[1:][t]

Mass2            = [44,80,128,188,236]
Velocity2        = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
Breakingforce2   = np.matrix([BF509,BF1009,BF1509,BF2009,BF3009,BF4009,BF6009,BF8009,BF10009,BF12009,BF14009,BF16009,BF18009])

BF44  = Breakingforce2[:,0]
BF80  = Breakingforce2[:,1]
BF128 = Breakingforce2[:,2]
BF188 = Breakingforce2[:,3]
BF236 = Breakingforce2[:,4]

df2  = pd.read_excel('bs perpendicular/2500mm/2500mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('bs perpendicular/2500mm/2500mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('bs perpendicular/2500mm/2500mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('bs perpendicular/2500mm/2500mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('bs perpendicular/2500mm/2500mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('bs perpendicular/2500mm/2500mm_800mm_min.xls' ,['Results'], header=0)
df8  = pd.read_excel('bs perpendicular/2500mm/2500mm_600mm_min.xls' ,['Results'], header=0)
df9  = pd.read_excel('bs perpendicular/2500mm/2500mm_400mm_min.xls' ,['Results'], header=0)
df10 = pd.read_excel('bs perpendicular/2500mm/2500mm_300mm_min.xls' ,['Results'], header=0)
df11 = pd.read_excel('bs perpendicular/2500mm/2500mm_200mm_min.xls' ,['Results'], header=0)
df12 = pd.read_excel('bs perpendicular/2500mm/2500mm_150mm_min.xls' ,['Results'], header=0)
df13 = pd.read_excel('bs perpendicular/2500mm/2500mm_100mm_min.xls' ,['Results'], header=0)
df14 = pd.read_excel('bs perpendicular/2500mm/2500mm_50mm_min.xls'  ,['Results'], header=0)

BF180025d =  df2['Results']['Fmax'].iloc[1:]
BF160025d =  df3['Results']['Fmax'].iloc[1:]
BF140025d =  df4['Results']['Fmax'].iloc[1:]
BF120025d =  df5['Results']['Fmax'].iloc[1:]
BF100025d =  df6['Results']['Fmax'].iloc[1:]
BF80025d  =  df7['Results']['Fmax'].iloc[1:]
BF60025d  =  df8['Results']['Fmax'].iloc[1:]
BF40025d  =  df9['Results']['Fmax'].iloc[1:]
BF30025d  = df10['Results']['Fmax'].iloc[1:]
BF20025d  = df11['Results']['Fmax'].iloc[1:]
BF15025d  = df12['Results']['Fmax'].iloc[1:]
BF10025d  = df13['Results']['Fmax'].iloc[1:]
BF5025d   = df14['Results']['Fmax'].iloc[1:]

BF180025ad = df2['Results']['Fmax'].iloc[1:][t]
BF160025ad = df3['Results']['Fmax'].iloc[1:][t]
BF140025ad = df4['Results']['Fmax'].iloc[1:][t]
BF120025ad = df5['Results']['Fmax'].iloc[1:][t]
BF100025ad = df6['Results']['Fmax'].iloc[1:][t]
BF80025ad  = df7['Results']['Fmax'].iloc[1:][t]
BF60025ad  = df8['Results']['Fmax'].iloc[1:][t]
BF40025ad  = df9['Results']['Fmax'].iloc[1:][t]
BF30025ad  = df10['Results']['Fmax'].iloc[1:][t]
BF20025ad  = df11['Results']['Fmax'].iloc[1:][t]
BF15025ad  = df12['Results']['Fmax'].iloc[1:][t]
BF10025ad  = df13['Results']['Fmax'].iloc[1:][t]
BF5025ad   = df14['Results']['Fmax'].iloc[1:][t]


test = pd.DataFrame({'1800':[BF1800a,BF1800ab,BF1800ac], '1600':[BF1600a,BF1600ab,BF1600ac], '1400':[BF1400a,BF1400ab,BF1400ac]
                     , '1200':[BF1200a,BF1200ab,BF1200ac], '1000':[BF1000a,BF1000ab,BF1000ac], '800':[BF800a,BF800ab,BF800ac]
                     , '600':[BF600a,BF600ab,BF600ac], '400':[BF400a,BF400ab,BF400ac], '300':[BF300a,BF300ab,BF300ac]
                     , '200':[BF200a,BF200ab,BF200ac], '150':[BF150a,BF150ab,BF200ac], '100':[BF100a,BF100ab,BF150ac]
                     , '50':[BF50a,BF50ab,BF50ac]})
print('test')
print(test)
para1  = test['1800'].iloc[0:]
para2  = test['1600'].iloc[0:]
para3  = test['1400'].iloc[0:]
para4  = test['1200'].iloc[0:]
para5  = test['1000'].iloc[0:]
para6  = test['800'].iloc[0:]
para7  = test['600'].iloc[0:]
para8  = test['400'].iloc[0:]
para9  = test['300'].iloc[0:]
para10 = test['200'].iloc[0:]
para11 = test['150'].iloc[0:]
para12 = test['100'].iloc[0:]
para13 = test['50'].iloc[0:]
print('Breakingforce3')
print(Breakingforce3)
print('para2')
print(para2)
print(Mass3, Velocity3)
Ori= [1,2,3]
Velocity5 = [1800,1600,1400,1200,1000,800,600,400,300,200,150,100,50]
Ori,Velocity5 = np.meshgrid(Ori,Velocity5)
Break47= np.matrix([para1,para2,para3,para4,para5,para6,para7,para8,para9,para10,para11,para12,para13])

Mass5 = [51,87,135,195,243]
Ori2 = [1, 2, 3]
Mass5,Ori2 = np.meshgrid(Mass5,Ori2)
BFmassori = np.matrix([BF1800,BF1800b,BF1800c])
print(BFmassori)

print('Break47')
print(Break47)
print(Surfacearea2,Velocity4)

#fig = plt.figure(1)
#ax = fig.gca(projection='3d')
#surf = ax.plot_surface(Ori, Velocity5, Break47, cmap=cm.coolwarm,linewidth=0, antialiased=False)
plt.title('Breakforce as a function of sliding speed and orientation (weigth 47g +/-3g)')
plt.xlabel('orientation')
plt.ylabel('Velocity (mm/min)')
#plt.show(1)

Mass6 = [51,87,135,195,243]
plt.figure(2)
plt.plot(Mass6, BF1800, label = '1800mm/min')
plt.plot(Mass6, BF1600, label = '1600mm/min')
plt.plot(Mass6, BF1400, label = '1400mm/min')
plt.plot(Mass6, BF1200, label = '1200mm/min')
plt.plot(Mass6, BF1000, label = '1000mm/min')
plt.plot(Mass6, BF800, label  = '800mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
plt.show(2)
#plt.figure(3)
plt.plot(Mass6, BF600, label  = '600mm/min')
plt.plot(Mass6, BF400, label  = '400mm/min')
plt.plot(Mass6, BF300, label  = '300mm/min')
plt.plot(Mass6, BF200, label  = '200mm/min')
plt.plot(Mass6, BF150, label  = '150mm/min')
plt.plot(Mass6, BF100, label  = '100mm/min')
plt.plot(Mass6, BF50, label   = '50mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds (170')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(3)


Mass6 = [51,87,135,195,243]
#plt.figure(4)
plt.plot(Mass6, BF18009, label = '1800mm/min')
plt.plot(Mass6, BF16009, label = '1600mm/min')
plt.plot(Mass6, BF14009, label = '1400mm/min')
plt.plot(Mass6, BF12009, label = '1200mm/min')
plt.plot(Mass6, BF10009, label = '1000mm/min')
plt.plot(Mass6, BF8009, label  = '800mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(4)
#plt.figure(5)
plt.plot(Mass6, BF6009, label  = '600mm/min')
plt.plot(Mass6, BF4009, label  = '400mm/min')
plt.plot(Mass6, BF3009, label  = '300mm/min')
plt.plot(Mass6, BF2009, label  = '200mm/min')
plt.plot(Mass6, BF1509, label  = '150mm/min')
plt.plot(Mass6, BF1009, label  = '100mm/min')
plt.plot(Mass6, BF509, label   = '50mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(5)

Mass6 = [51,87,135,195,243]
#plt.figure(6)
plt.plot(Mass6, BF180025, label = '1800mm/min')
plt.plot(Mass6, BF160025, label = '1600mm/min')
plt.plot(Mass6, BF140025, label = '1400mm/min')
plt.plot(Mass6, BF120025, label = '1200mm/min')
plt.plot(Mass6, BF100025, label = '1000mm/min')
plt.plot(Mass6, BF80025, label  = '800mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(6)
#plt.figure(7)
plt.plot(Mass6, BF60025, label  = '600mm/min')
plt.plot(Mass6, BF40025, label  = '400mm/min')
plt.plot(Mass6, BF30025, label  = '300mm/min')
plt.plot(Mass6, BF20025, label  = '200mm/min')
plt.plot(Mass6, BF15025, label  = '150mm/min')
plt.plot(Mass6, BF10025, label  = '100mm/min')
plt.plot(Mass6, BF5025, label   = '50mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(7)

Mass6 = [51,87,135,195,243]
#plt.figure(8)
plt.plot(Mass6, BF1800b, label = '1800mm/min')
plt.plot(Mass6, BF1600b, label = '1600mm/min')
plt.plot(Mass6, BF1400b, label = '1400mm/min')
plt.plot(Mass6, BF1200b, label = '1200mm/min')
plt.plot(Mass6, BF1000b, label = '1000mm/min')
plt.plot(Mass6, BF800b, label  = '800mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(8)
#plt.figure(9)
plt.plot(Mass6, BF600b, label  = '600mm/min')
plt.plot(Mass6, BF400b, label  = '400mm/min')
plt.plot(Mass6, BF300b, label  = '300mm/min')
plt.plot(Mass6, BF200b, label  = '200mm/min')
plt.plot(Mass6, BF150b, label  = '150mm/min')
plt.plot(Mass6, BF100b, label  = '100mm/min')
plt.plot(Mass6, BF50b, label   = '50mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(9)


Mass6 = [51,87,135,195,243]
#plt.figure(10)
plt.plot(Mass6, BF18009b, label = '1800mm/min')
plt.plot(Mass6, BF16009b, label = '1600mm/min')
plt.plot(Mass6, BF14009b, label = '1400mm/min')
plt.plot(Mass6, BF12009b, label = '1200mm/min')
plt.plot(Mass6, BF10009b, label = '1000mm/min')
plt.plot(Mass6, BF8009b, label  = '800mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(10)
#plt.figure(11)
plt.plot(Mass6, BF6009b, label  = '600mm/min')
plt.plot(Mass6, BF4009b, label  = '400mm/min')
plt.plot(Mass6, BF3009b, label  = '300mm/min')
plt.plot(Mass6, BF2009b, label  = '200mm/min')
plt.plot(Mass6, BF1509b, label  = '150mm/min')
plt.plot(Mass6, BF1009b, label  = '100mm/min')
plt.plot(Mass6, BF509b, label   = '50mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(11)

Mass6 = [51,87,135,195,243]
#plt.figure(12)
plt.plot(Mass6, BF180025b, label = '1800mm/min')
plt.plot(Mass6, BF160025b, label = '1600mm/min')
plt.plot(Mass6, BF140025b, label = '1400mm/min')
plt.plot(Mass6, BF120025b, label = '1200mm/min')
plt.plot(Mass6, BF100025b, label = '1000mm/min')
plt.plot(Mass6, BF80025b, label  = '800mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(12)
#plt.figure(13)
plt.plot(Mass6, BF60025b, label  = '600mm/min')
plt.plot(Mass6, BF40025b, label  = '400mm/min')
plt.plot(Mass6, BF30025b, label  = '300mm/min')
plt.plot(Mass6, BF20025b, label  = '200mm/min')
plt.plot(Mass6, BF15025b, label  = '150mm/min')
plt.plot(Mass6, BF10025b, label  = '100mm/min')
plt.plot(Mass6, BF5025b, label   = '50mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(13)

Mass6 = [51,87,135,195,243]
#plt.figure(14)
plt.plot(Mass6, BF1800c, label = '1800mm/min')
plt.plot(Mass6, BF1600c, label = '1600mm/min')
plt.plot(Mass6, BF1400c, label = '1400mm/min')
plt.plot(Mass6, BF1200c, label = '1200mm/min')
plt.plot(Mass6, BF1000c, label = '1000mm/min')
plt.plot(Mass6, BF800c, label  = '800mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(14)
#plt.figure(15)
plt.plot(Mass6, BF600c, label  = '600mm/min')
plt.plot(Mass6, BF400c, label  = '400mm/min')
plt.plot(Mass6, BF300c, label  = '300mm/min')
plt.plot(Mass6, BF200c, label  = '200mm/min')
plt.plot(Mass6, BF150c, label  = '150mm/min')
plt.plot(Mass6, BF100c, label  = '100mm/min')
plt.plot(Mass6, BF50c, label   = '50mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(15)


Mass6 = [51,87,135,195,243]
#plt.figure(16)
plt.plot(Mass6, BF18009c, label = '1800mm/min')
plt.plot(Mass6, BF16009c, label = '1600mm/min')
plt.plot(Mass6, BF14009c, label = '1400mm/min')
plt.plot(Mass6, BF12009c, label = '1200mm/min')
plt.plot(Mass6, BF10009c, label = '1000mm/min')
plt.plot(Mass6, BF8009c, label  = '800mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(16)
#plt.figure(17)
plt.plot(Mass6, BF6009c, label  = '600mm/min')
plt.plot(Mass6, BF4009c, label  = '400mm/min')
plt.plot(Mass6, BF3009c, label  = '300mm/min')
plt.plot(Mass6, BF2009c, label  = '200mm/min')
plt.plot(Mass6, BF1509c, label  = '150mm/min')
plt.plot(Mass6, BF1009c, label  = '100mm/min')
plt.plot(Mass6, BF509c, label   = '50mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(17)

Mass6 = [51,87,135,195,243]
#plt.figure(18)
plt.plot(Mass6, BF180025c, label = '1800mm/min')
plt.plot(Mass6, BF160025c, label = '1600mm/min')
plt.plot(Mass6, BF140025c, label = '1400mm/min')
plt.plot(Mass6, BF120025c, label = '1200mm/min')
plt.plot(Mass6, BF100025c, label = '1000mm/min')
plt.plot(Mass6, BF80025c, label  = '800mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(18)
#plt.figure(19)
plt.plot(Mass6, BF60025c, label  = '600mm/min')
plt.plot(Mass6, BF40025c, label  = '400mm/min')
plt.plot(Mass6, BF30025c, label  = '300mm/min')
plt.plot(Mass6, BF20025c, label  = '200mm/min')
plt.plot(Mass6, BF15025c, label  = '150mm/min')
plt.plot(Mass6, BF10025c, label  = '100mm/min')
plt.plot(Mass6, BF5025c, label   = '50mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(19)


#plt.figure(20)
plt.plot(Mass6, BF1800d, label = '1800mm/min')
plt.plot(Mass6, BF1600d, label = '1600mm/min')
plt.plot(Mass6, BF1400d, label = '1400mm/min')
plt.plot(Mass6, BF1200d, label = '1200mm/min')
plt.plot(Mass6, BF1000d, label = '1000mm/min')
plt.plot(Mass6, BF800d, label  = '800mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(20)
#plt.figure(21)
plt.plot(Mass6, BF600d, label  = '600mm/min')
plt.plot(Mass6, BF400d, label  = '400mm/min')
plt.plot(Mass6, BF300d, label  = '300mm/min')
plt.plot(Mass6, BF200d, label  = '200mm/min')
plt.plot(Mass6, BF150d, label  = '150mm/min')
plt.plot(Mass6, BF100d, label  = '100mm/min')
plt.plot(Mass6, BF50d, label   = '50mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(21)


Mass6 = [51,87,135,195,243]
#plt.figure(22)
plt.plot(Mass6, BF18009d, label = '1800mm/min')
plt.plot(Mass6, BF16009d, label = '1600mm/min')
plt.plot(Mass6, BF14009d, label = '1400mm/min')
plt.plot(Mass6, BF12009d, label = '1200mm/min')
plt.plot(Mass6, BF10009d, label = '1000mm/min')
plt.plot(Mass6, BF8009d, label  = '800mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(22)
#plt.figure(23)
plt.plot(Mass6, BF6009d, label  = '600mm/min')
plt.plot(Mass6, BF4009d, label  = '400mm/min')
plt.plot(Mass6, BF3009d, label  = '300mm/min')
plt.plot(Mass6, BF2009d, label  = '200mm/min')
plt.plot(Mass6, BF1509d, label  = '150mm/min')
plt.plot(Mass6, BF1009d, label  = '100mm/min')
plt.plot(Mass6, BF509d, label   = '50mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(23)

Mass6 = [51,87,135,195,243]
#plt.figure(24)
plt.plot(Mass6, BF180025d, label = '1800mm/min')
plt.plot(Mass6, BF160025d, label = '1600mm/min')
plt.plot(Mass6, BF140025d, label = '1400mm/min')
plt.plot(Mass6, BF120025d, label = '1200mm/min')
plt.plot(Mass6, BF100025d, label = '1000mm/min')
plt.plot(Mass6, BF80025d, label  = '800mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(24)
#plt.figure(25)
plt.plot(Mass6, BF60025d, label  = '600mm/min')
plt.plot(Mass6, BF40025d, label  = '400mm/min')
plt.plot(Mass6, BF30025d, label  = '300mm/min')
plt.plot(Mass6, BF20025d, label  = '200mm/min')
plt.plot(Mass6, BF15025d, label  = '150mm/min')
plt.plot(Mass6, BF10025d, label  = '100mm/min')
plt.plot(Mass6, BF5025d, label   = '50mm/min')
plt.title('Breaking force as a funtion of the weigth for different speeds')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
#plt.show(25)

Breaking1 = np.array([BF5025a,BF10025a,BF15025a,BF20025a,BF30025a,BF40025a,BF60025a,BF80025a,BF100025a,BF120025a,BF140025a,BF160025a,BF180025a])
Breaking2 = np.array([BF5025ab,BF10025ab,BF15025ab,BF20025ab,BF30025ab,BF40025ab,BF60025ab,BF80025ab,BF100025ab,BF120025ab,BF140025ab,BF160025ab,BF180025ab])
Breaking3 = np.array([BF5025ac,BF10025ac,BF15025ac,BF20025ac,BF30025ac,BF40025ac,BF60025ac,BF80025ac,BF100025ac,BF120025ac,BF140025ac,BF160025ac,BF180025ac])
Breaking4 = np.array([BF5025ad,BF10025ad,BF15025ad,BF20025ad,BF30025ad,BF40025ad,BF60025ad,BF80025ad,BF100025ad,BF120025ad,BF140025ad,BF160025ad,BF180025ad])

Velocity3 = np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])
x = Velocity3
x.astype(int)
print(Velocity3)
def force(x, p1, p2, p3):
     return p1- p2 * np.exp(-(p3) * x)
p0 = [0.3, 0.31 , 0.0022]
pg = [0.35, -0.3, 0.0022]
pd1,cov = curve_fit(force,x,Breaking1,pg)
p1, p2, p3 = pd1
plt.figure(91)
plt.plot(x, force(x, p1, p2, p3), label = 'parallel parallel')
plt.plot(x,Breaking1)
pw = [ 0.26922704 ,-0.20206315 , 0.00280559]
pd2,cov = curve_fit(force,x,Breaking2,pw)
p1, p2, p3 = pd2
plt.plot(x, force(x, p1, p2, p3), label = 'parallel perpendicular')
plt.plot(x,Breaking2)
pd3,cov = curve_fit(force,x,Breaking3,p0)
p1, p2, p3 = pd3
plt.plot(x, force(x, p1, p2, p3), label = 'perpendicular perpendicular')
plt.plot(x,Breaking3)
pd4,cov = curve_fit(force,x,Breaking4,p0)
p1, p2, p3 = pd4
plt.plot(x, force(x, p1, p2, p3), label= 'bs perpendicular')
plt.plot(x,Breaking4)
plt.title('Breaking force as a funtion of speed for different orientations')
plt.xlabel('Weight (g)')
plt.ylabel('Breaking force (N)')
plt.legend()
plt.show(91)

print('orientatie')
print(pd1,pd2,pd3,pd4)

g1, g2, g3 =[ 0.14987452, -0.071362,    0.00205424]
v1, v2, v3 =[ 0.2746542,   0.03214562, -0.000724  ]
j1, j2, j3 =[ 0.11804538, -0.05379717,  0.00520327]
l1, l2 ,l3 =[ 0.07182545, -0.30217739,  0.00095059]

g4, g5, g6 = [ 0.19396973, -0.08302308,  0.00103861]
v4, v5, v6 = [ 0.26922483, -0.20206097,  0.00280539]
j4, j5, j6 = [ 0.14826899, -0.09118315,  0.00205384]
l4, l5, l6 = [ 0.05407612, -0.39573069,  0.00070127]

g7, g8, g9 = [ 2.82147551e-03, -3.66720369e-01,  1.17958897e-04]
v7, v8, v9 = [ 0.38071336,     -0.20403699,      0.00192417]
j7, j8, j9 = [ 0.25735808,     -0.13303312,      0.00799907]
l7, l8, l9 = [ 0.26856142,     -0.32926861,      0.00097778]

g10, g11, g12 = [ 0.53075078,  0.00173912, -0.00219641]
v10, v11, v12 = [ 0.48183618, -0.32319305,  0.0024146 ]
j10, j11, j12 = [ 0.38022978, -0.09899424,  0.00580286]
l10, l11, l12 = [ 0.43357273, -0.3113162,   0.00112157]

g13, g14, g15 = [ 0.59542086, -0.11211234,  0.00292167]
v13, v14, v15 = [ 0.66547877, -0.41287072,  0.00366416]
j13, j14, j15 = [ 0.47681993, -0.21275438,  0.01352713]
l13, l14, l15 = [ 0.57042853, -0.31464282,  0.00213377]

plt.figure(95)

plt.plot(x, force(x, g1, g2, g3),'g',  label = 'parallel parallel')
plt.plot(x, force(x, g4, g5, g6),'g',  label = 'parallel parallel')
plt.plot(x, force(x, g7, g8, g9),'g',  label = 'parallel parallel')
plt.plot(x, force(x, g10, g11, g12),'g',  label = 'parallel parallel')
plt.plot(x, force(x, g13, g14, g15),'g',  label = 'parallel parallel')

plt.plot(x, force(x, v1, v2, v3),'b', label = 'parallel perpendicular')
plt.plot(x, force(x, v4, v5, v6), 'b',label = 'parallel perpendicular')
plt.plot(x, force(x, v7, v8, v9), 'b',label = 'parallel perpendicular')
plt.plot(x, force(x, v10, v11, v12),'b', label = 'parallel perpendicular')
plt.plot(x, force(x, v13, v14, v15),'b', label = 'parallel perpendicular')

plt.plot(x, force(x, j1, j2, j3),'r', label = 'perpendicular perpendicular')
plt.plot(x, force(x, j4, j5, j6),'r', label = 'perpendicular perpendicular')
plt.plot(x, force(x, j7, j8, j9),'r', label = 'perpendicular perpendicular')
plt.plot(x, force(x, j10, j11, j12),'r', label = 'perpendicular perpendicular')
plt.plot(x, force(x, j13, j14, j15),'r', label = 'perpendicular perpendicular')

plt.plot(x, force(x, l1, l2, l3),'c', label= 'bs perpendicular')
plt.plot(x, force(x, l4, l5, l6),'c', label= 'bs perpendicular')
plt.plot(x, force(x, l7, l8, l9),'c', label= 'bs perpendicular')
plt.plot(x, force(x, l10, l11, l12),'c', label= 'bs perpendicular')
plt.plot(x, force(x, l13, l14, l15),'c', label= 'bs perpendicular')

plt.title('Breaking force as a funtion of speed for different orientations and weights')
plt.xlabel('Sliding speed(mm/min)')
plt.ylabel('Breaking force (N)')
plt.legend()
plt.show(95)

plt.figure(100)
plt.plot(x, force(x, g1, g2, g3),'g',  label = 'parallel parallel')
plt.plot(x, force(x, v1, v2, v3),'b', label = 'parallel perpendicular')
plt.plot(x, force(x, j1, j2, j3),'r', label = 'perpendicular perpendicular')
plt.plot(x, force(x, l1, l2, l3),'c', label= 'bs perpendicular')
plt.title('Breaking force as a funtion of speed for different orientations and weights (41g)')
plt.xlabel('Sliding speed(mm/min)')
plt.ylabel('Breaking force (N)')
plt.legend()
plt.show(100)

plt.figure(101)
plt.plot(x, force(x, g4, g5, g6),'g',  label = 'parallel parallel')
plt.plot(x, force(x, v4, v5, v6), 'b',label = 'parallel perpendicular')
plt.plot(x, force(x, j4, j5, j6),'r', label = 'perpendicular perpendicular')
plt.plot(x, force(x, l4, l5, l6),'c', label= 'bs perpendicular')
plt.title('Breaking force as a funtion of speed for different orientations and weights (85g) ')
plt.xlabel('Sliding speed(mm/min)')
plt.ylabel('Breaking force (N)')
plt.legend()
plt.show(101)

plt.figure(102)
plt.plot(x, force(x, g7, g8, g9),'g',  label = 'parallel parallel')
plt.plot(x, force(x, v7, v8, v9), 'b',label = 'parallel perpendicular')
plt.plot(x, force(x, j7, j8, j9),'r', label = 'perpendicular perpendicular')
plt.plot(x, force(x, l7, l8, l9),'c', label= 'bs perpendicular')
plt.title('Breaking force as a funtion of speed for different orientations and weights (134g)')
plt.xlabel('Sliding speed(mm/min)')
plt.ylabel('Breaking force (N)')
plt.legend()
plt.show(102)

plt.figure(103)
plt.plot(x, force(x, g10, g11, g12),'g',  label = 'parallel parallel')
plt.plot(x, force(x, v10, v11, v12),'b', label = 'parallel perpendicular')
plt.plot(x, force(x, j10, j11, j12),'r', label = 'perpendicular perpendicular')
plt.plot(x, force(x, l10, l11, l12),'c', label= 'bs perpendicular')
plt.title('Breaking force as a funtion of speed for different orientations and weights (191g)')
plt.xlabel('Sliding speed(mm/min)')
plt.ylabel('Breaking force (N)')
plt.legend()
plt.show(103)

plt.figure(104)
plt.plot(x, force(x, g13, g14, g15),'g',  label = 'parallel parallel')
plt.plot(x, force(x, v13, v14, v15),'b', label = 'parallel perpendicular')
plt.plot(x, force(x, j13, j14, j15),'r', label = 'perpendicular perpendicular')
plt.plot(x, force(x, l13, l14, l15),'c', label= 'bs perpendicular')
plt.title('Breaking force as a funtion of speed for different orientations and weights (241g)')
plt.xlabel('Sliding speed(mm/min)')
plt.ylabel('Breaking force (N)')
plt.legend()
plt.show(104)

gtot1 = (g1+g4+g7+g10+g13)/5
gtot2 = (g2+g5+g8+g11+g14)/5
gtot3 = (g3+g6+g9+g12+g15)/5

vtot1 = (v1+v4+v7+v10+v13)/5
vtot2 = (v2+v5+v8+v11+v14)/5
vtot3 = (v3+v6+v9+v12+v15)/5

jtot1 = (j1+j4+j7+j10+j13)/5
jtot2 = (j2+j5+j8+j11+j14)/5
jtot3 = (j3+j6+j9+j12+j15)/5

ltot1 = (l1+l4+l7+l10+l13)/5
ltot2 = (l2+l5+l8+l11+l14)/5
ltot3 = (l3+l6+l9+l12+l15)/5

plt.figure(96)
plt.plot(x, force(x, gtot1, gtot2, gtot3),'g',  label = 'parallel parallel')
plt.plot(x, force(x, vtot1, vtot2, vtot3),'b', label = 'parallel perpendicular')
plt.plot(x, force(x, jtot1, jtot2, jtot3),'r', label = 'perpendicular perpendicular')
plt.plot(x, force(x, ltot1, ltot2, ltot3),'c', label= 'bs perpendicular')
plt.title('Breaking force as a funtion of speed for different orientations and weights')
plt.xlabel('Sliding speed (mm/min)')
plt.ylabel('Breaking force (N)')
plt.legend()
plt.show(96)

ds
Breakingforce3 = np.array([BF5025a,BF10025a,BF15025a,BF20025a,BF30025a,BF40025a,BF60025a,BF80025a,BF100025a,BF120025a,BF140025a,BF160025a,BF180025a])
Velocity3 = np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])
print(Breakingforce3)

x = Velocity3
x.astype(int)
print(Velocity3)
def force(x, a1, a2, a3):
     return a1- a2 * np.exp(-(a3) * x)
p0 = [0.57, -0.31 , 0.0022]
a,cov = curve_fit(force,x,Breakingforce3,p0)
print('tst')
print(a)
plt.figure(91)
a1, a2,a3 = a
v_fit = force(x, a1, a2, a3)
plt.plot(x, force(x, a1, a2, a3))
plt.plot(x,Breakingforce3)
plt.show(91)

Breakingforce4 = np.array([BF509a,BF1009a,BF1509a,BF2009a,BF3009a,BF4009a,BF6009a,BF8009a,BF10009a,BF12009a,BF14009a,BF16009a,BF18009a])
Velocity4 = np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])

x = Velocity4
x.astype(int)
def force2(x, b1, b2, b3):
     return b1- b2 * np.exp(-(b3) * x)
p0= [ 0.17999241,      0.00095126,     -0.00213947]
b,cov = curve_fit(force2,x,Breakingforce4,p0)
print('tst1')
print(b)
b1, b2,b3 = b
v_fit = force2(x, b1, b2, b3)
plt.figure(92)
plt.plot(x, force2(x, b1, b2, b3))
plt.plot(x,Breakingforce4)
plt.show(92)

Breakingforce5 = np.array([BF50a,BF100a,BF150a,BF200a,BF300a,BF400a,BF600a,BF800a,BF1000a,BF1200a,BF1400a,BF1600a,BF1800a])
Velocity5 = np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])

x = Velocity5
x.astype(int)
def force3(x, c1, c2, c3):
     return c1- c2 * np.exp(-(c3) * x)
p0 = [ 0.3373534 , -0.21798016 , 0.01198338]
c,cov = curve_fit(force3,x,Breakingforce5,p0)
c1, c2, c3 = c
v_fit = force3(x, c1, c2, c3)
print('tst2')
print(c)
print(v_fit)
plt.figure(93)
plt.plot(x, force3(x, c1, c2, c3))
plt.plot(x,Breakingforce5)
plt.show(93)

a1, a2, a3 = [ 0.14987499,     -0.07136202,      0.0020543 ]
b1, b2, b3 = [ 0.17999241,      0.00095126,     -0.00213947]
c1, c2, c3 = [ 2.58199367e-01,  4.20099735e-08, -7.92758329e-03]

a11, a21, a31 = [ 0.19396925, -0.08302344,  0.00103859]
b11, b21, b31 = [ 0.2013529, -0.10495796,  0.00350803]
c11, c21, c31 = [-6.46261543e+01, -6.49707074e+01,  3.35034558e-07]

a12, a22, a32 = [ 2.81283277e-03, -3.66728987e-01,  1.17955844e-04]
b12, b22, b32 = [ 0.3373534,  -0.21798016,  0.01198338]
c12, c22, c32 = [ 4.42348020e-01,  5.45919472e-07, -6.32551374e-03]

a13, a23, a33 = [ 0.53075218,  0.00173971, -0.00219623]
b13, b23, b33 = [ 0.473215,   -0.0310636,   0.00123895]
c13, c23, c33 = [0.61373262,   0.04123219,  0.00329661]

a14, a24, a34 = [ 0.59542092,     -0.11211242,      0.00292169]
b14, b24, b34 = [ 0.57557092,     -0.11486162,      0.00229768]
c14, c24, c34 = [ 7.36114962e-01,  1.48453378e-04, -3.63200171e-03]


Coefficient1 = [a1,b1,c1]
Coefficient2 = [a2,b2,c2]
Coefficient3 = [a3,b3,c3]



Coefficient4 = [a11,b11,c11]
Coefficient5 = [a21,b21,c21]
Coefficient6 = [a31,b31,c31]



Coefficient7 = [a12,b12,c12]
Coefficient8 = [a22,b22,c22]
Coefficient9 = [a32,b32,c32]



Coefficient10 = [a13,b13,c13]
Coefficient11 = [a23,b23,c23]
Coefficient12 = [a33,b33,c33]



Coefficient13 = [a14,b14,c14]
Coefficient14 = [a24,b24,c24]
Coefficient15 = [a34,b34,c34]



surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc1,cov = curve_fit(force4,surface1,Coefficient1,p0)
print('tst3')
print(dc1)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc2,cov = curve_fit(force5,surface1,Coefficient2,p0)
print('tst4')
print(dc2)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc3,cov = curve_fit(force6,surface1,Coefficient3,p0)
print('tst5')
print(dc3)



d1  = -1.45104771e+02
d2  = 6.50548527e-02
d3  = 3.33705777e+02
d4  = 6.50308700e-02
d5  = 7.25824580e-02
d6  = 1.28374478e-06
d7  = -2.32065820e+01
d8  = -4.61063629e-06
d9  = -2.35473712e+01
d10 = 1.39297889e-05
d11 = 4.13967585e-03
d12 = -1.54350111e-06
d13 = 1.94803017e+02
d14 = -8.71590211e-02
d15 = 1.94393396e+02
d16 = -8.71501930e-02
d17 = 3.57487212e-03
d18 = 7.38939859e-08
d19 = 1.07344460e+02
d20 = -9.15637782e-02
d21 = 1.06841598e+02
d22 = -9.15844832e-02
d23 = 2.82802739e-03
d24 = -7.74125844e-07
d25 = -4.20826405e+01
d26 = 1.23931109e-05
d27 = -4.27789166e+01
d28 = 2.09244572e-06
d29 = 1.07602091e-03
d30 = 3.90368102e-07

ds1 = [d1, d7, d13, d19, d25]
ds2 = [d2, d8, d14, d20, d26]
ds3 = [d3, d9, d15, d21, d27]
ds4 = [d4, d10, d16, d22, d28]
ds5 = [d5, d11, d17, d23, d29]
ds6 = [d6, d12, d18, d24, d30]

Mass1     = [ 47, 83, 132, 192, 241]
def force14(Mass1, e1, e2):
     return e1+e2*Mass1
print(force14)
p0 = [0.0015, 0.0005]
dc11,cov = curve_fit(force14,Mass1,ds1,p0)
print('tst13')
print(dc11)

Mass1     = [ 47, 83, 132, 192, 241]
def force15(Mass1, e3, e4):
     return e3+e4*Mass1
print(force14)
p0 = [0.00015, 0.0005]
dc12,cov = curve_fit(force15,Mass1,ds2,p0)
print('tst14')
print(dc12)

Mass1     = [ 47, 83, 132, 192, 241]
def force16(Mass1, e5, e6):
     return e5+e6*Mass1

p0 = [0.0015, 0.0001]
dc13,cov = curve_fit(force16,Mass1,ds3,p0)
print('tst15')
print(dc13)

Mass1     = [ 47, 83, 132, 192, 241]
def force17(Mass1, e7, e8):
     return e7+e8*Mass1
print(force14)
p0 = [0.00015, 0.001]
dc14,cov = curve_fit(force17,Mass1,ds4,p0)
print('tst16')
print(dc14)

Mass1     = [ 47, 83, 132, 192, 241]
def force18(Mass1, e9, e10):
     return e9+e10*Mass1
p0 = [0.00015, 0.0001]
dc15,cov = curve_fit(force18,Mass1,ds5,p0)
print('tst17')
print(dc15)

Mass1     = [ 47, 83, 132, 192, 241]
def force19(Mass1, e11, e12):
     return e11+e12*Mass1
p0 = [0.00015, 0.00001]
dc16,cov = curve_fit(force19,Mass1,ds6,p0)
print('tst18')
print(dc16)

e1, e2   = dc11 
e3, e4   = dc12
e5, e6   = dc13
e7, e8   = dc14
e9, e10  = dc15
e11, e12 = dc16


m= 87
s=2500
v=1800
f = ((e1+e2*m)+(e3+e4*m)*s)- ((e5+e6*m)+(e7+e8*m)*s) * np.exp(-((e9+e10*m)+(e11+e12*m)*s) * v)
print('f')
print(f)
def force(x, a1, a2, a3):
     return ((e1+e2m)+(e3+e4m)*s)- ((e5+e6m)+(e7+e8m)*s) * np.exp(-((e9+e10m)+(e11+e12m)*s) * x)

m = np.arange(40, 280, 40)
print(m)
fm =((0.08769709+ 0.00235336*m) + (2.88489580e-06+3.35703447e-08*m)*900) + ((1.56811452e-05-4.15449470e-08*m)-(4.70280025e-09-3.25670068e-12*m)*900)*50
def fml(m):
    return ((0.08769709+ 0.00235336*m) + (2.88489580e-06+3.35703447e-08*m)*900) + ((1.56811452e-05-4.15449470e-08*m)-(4.70280025e-09-3.25670068e-12*m)*900)*900
#plt.figure(30)
plt.plot(m, fm)
plt.plot(Mass1, BF509)
#plt.show(30)

v = np.arange(50,1850,50)
fv =((0.08769709+ 0.00235336*241) + (2.88489580e-06+3.35703447e-08*241)*2500) + ((1.56811452e-05-4.15449470e-08*241)-(4.70280025e-09-3.25670068e-12*241)*2500)*v
#plt.figure(31)
plt.plot(v,fv)
plt.plot(Velocity3, Breakingforce5)
#plt.show(31)
w = dc3[0]
print(w)


print('ss parallel perpendicular')

Breakingforce3 = np.array([BF5025ab,BF10025ab,BF15025ab,BF20025ab,BF30025ab,BF40025ab,BF60025ab,BF80025ab,BF100025ab,BF120025ab,BF140025ab,BF160025ab,BF180025ab])
Velocity3 = np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])
print(Breakingforce3)

x = Velocity3
x.astype(int)
print(Velocity3)
def force(x, a1, a2, a3):
     return a1- a2 * np.exp(-(a3) * x)
p0 = [0.2,-0.2 , 0.003]
a,cov = curve_fit(force,x,Breakingforce3,p0)
print('tst')
print(a)
#plt.figure(91)
a1, a2,a3 = a
v_fit = force(x, a1, a2, a3)
plt.plot(x, force(x, a1, a2, a3))
plt.plot(x,Breakingforce3)
#plt.show(91)

Breakingforce4 = np.array([BF509ab,BF1009ab,BF1509ab,BF2009ab,BF3009ab,BF4009ab,BF6009ab,BF8009ab,BF10009ab,BF12009ab,BF14009ab,BF16009ab,BF18009ab])
Velocity4 = np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])

x = Velocity4
x.astype(int)
def force2(x, b1, b2, b3):
     return b1- b2 * np.exp(-(b3) * x)
p0 = [0.6, 1, 0.003]
b,cov = curve_fit(force2,x,Breakingforce4,p0)
print('tst1')
print(b)
b1, b2,b3 = b
v_fit = force2(x, b1, b2, b3)
#plt.figure(92)
plt.plot(x, force2(x, b1, b2, b3))
plt.plot(x,Breakingforce4)
#plt.show(92)

Breakingforce5 = np.array([BF50ab,BF100ab,BF150ab,BF200ab,BF300ab,BF400ab,BF600ab,BF800ab,BF1000ab,BF1200ab,BF1400ab,BF1600ab,BF1800ab])
Velocity5 = np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])

x = Velocity5
x.astype(int)
def force3(x, c1, c2, c3):
     return c1- c2 * np.exp(-(c3) * x)
#p0 = [0.6, 0.04, 0.003]
c,cov = curve_fit(force3,x,Breakingforce5,p0)
c1, c2, c3 = c
v_fit = force3(x, c1, c2, c3)
print('tst2')
print(c)
print(v_fit)
#plt.figure(93)
plt.plot(x, force3(x, c1, c2, c3))
plt.plot(x,Breakingforce5)
#plt.show(93)

a1, a2, a3 = [ 0.27468861,  0.03217685,  -0.0007236]
b1, b2, b3 = [ 0.23442368, -0.0737431,   0.00285248]
c1, c2, c3 = [ 0.22416081, -0.13629093,  0.00292692]

a11, a21, a31 = [ 0.26922392, -0.20206006,  0.00280531]
b11, b21, b31 = [ 0.28461209, -0.10985617,  0.00116631]
c11, c21, c31 = [ 0.27562352, -0.18047179,  0.00203912]

a12, a22, a32 = [ 0.38070778, -0.20403595,  0.00192391]
b12, b22, b32 = [ 0.40559308, -0.16218136,  0.00245121]
c12, c22, c32 = [ 0.43843721, -0.24194755,  0.00400048]

a13, a23, a33 = [ 0.48183644, -0.32319318,  0.00241461]
b13, b23, b33 = [ 0.59903641, -0.41534053,  0.0038918 ]
c13, c23, c33 = [ 0.61719584, -0.4862073,   0.00554382]

a14, a24, a34 = [ 0.66547923, -0.41287175,  0.0036642 ]
b14, b24, b34 = [ 0.67193788, -0.41096116,  0.00436219]
c14, c24, c34 = [ 0.69448788, -0.280341,    0.00176412]


Coefficient1 = [a1,b1,c1]
Coefficient2 = [a2,b2,c2]
Coefficient3 = [a3,b3,c3]



Coefficient4 = [a11,b11,c11]
Coefficient5 = [a21,b21,c21]
Coefficient6 = [a31,b31,c31]



Coefficient7 = [a12,b12,c12]
Coefficient8 = [a22,b22,c22]
Coefficient9 = [a32,b32,c32]



Coefficient10 = [a13,b13,c13]
Coefficient11 = [a23,b23,c23]
Coefficient12 = [a33,b33,c33]



Coefficient13 = [a14,b14,c14]
Coefficient14 = [a24,b24,c24]
Coefficient15 = [a34,b34,c34]


surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc1,cov = curve_fit(force4,surface1,Coefficient1,p0)
print('tst3')
print(dc1)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc2,cov = curve_fit(force5,surface1,Coefficient2,p0)
print('tst4')
print(dc2)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc3,cov = curve_fit(force6,surface1,Coefficient3,p0)
print('tst5')
print(dc3)

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc4,cov = curve_fit(force4,surface1,Coefficient4,p0)
print('tst6')
print(dc4)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc5,cov = curve_fit(force5,surface1,Coefficient5,p0)
print('tst7')
print(dc5)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc6,cov = curve_fit(force6,surface1,Coefficient6,p0)
print('tst8')
print(dc6)

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc1,cov = curve_fit(force4,surface1,Coefficient7,p0)
print('tst9')
print(dc1)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc2,cov = curve_fit(force5,surface1,Coefficient8,p0)
print('tst10')
print(dc2)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc3,cov = curve_fit(force6,surface1,Coefficient9,p0)
print('tst11')
print(dc3)

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc1,cov = curve_fit(force4,surface1,Coefficient10,p0)
print('tst12')
print(dc1)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc2,cov = curve_fit(force5,surface1,Coefficient11,p0)
print('tst13')
print(dc2)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc3,cov = curve_fit(force6,surface1,Coefficient12,p0)
print('tst14')
print(dc3)

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc1,cov = curve_fit(force4,surface1,Coefficient13,p0)
print('tst15')
print(dc1)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc2,cov = curve_fit(force5,surface1,Coefficient14,p0)
print('tst16')
print(dc2)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc3,cov = curve_fit(force6,surface1,Coefficient15,p0)
print('tst17')
print(dc3)

d1, d2   = [2.03581021e-01, 2.42977563e-05]
d3, d4   = [-1.84581998e-01,  7.19117559e-05]
d5, d6   = [ 7.61116647e-03, -3.18713126e-06]
d7, d8   = [ 2.92836441e-01, -9.61760625e-06]
d9, d10  = [-6.61627072e-02, -5.76274310e-05]
d11, d12 = [2.62142501e-04, 1.02437500e-06]
d13, d14 = [ 4.34686650e-01, -1.55533097e-05]
d15, d16 = [-1.58251119e-01, -2.61591183e-05]
d17, d18 = [ 3.35212292e-03, -3.29562500e-07]
d19, d20 = [ 6.90547861e-01, -7.32499792e-05]
d21, d22 = [-5.06153563e-01,  5.75920938e-05]
d23, d24 = [ 5.51959104e-03, -9.23243750e-07]
d25, d26 = [ 6.84163979e-01, -4.03665625e-06]
d27, d28 = [-3.66027786e-01, -1.19422564e-06]
d29, d30 = [ 4.00511777e-03, -4.36243789e-07]

ds1 = [d1, d7, d13, d19, d25]
ds2 = [d2, d8, d14, d20, d26]
ds3 = [d3, d9, d15, d21, d27]
ds4 = [d4, d10, d16, d22, d28]
ds5 = [d5, d11, d17, d23, d29]
ds6 = [d6, d12, d18, d24, d30]

Mass1     = [ 47, 83, 132, 192, 241]
def force14(Mass1, e1, e2):
     return e1+e2*Mass1
print(force14)
p0 = [0.0015, 0.0005]
dc11,cov = curve_fit(force14,Mass1,ds1,p0)
print('tst21')
print(dc11)

Mass1     = [ 47, 83, 132, 192, 241]
def force15(Mass1, e3, e4):
     return e3+e4*Mass1
print(force14)
p0 = [0.015, 0.05]
dc12,cov = curve_fit(force15,Mass1,ds2,p0)
print('tst22')
print(dc12)

Mass1     = [ 47, 83, 132, 192, 241]
def force16(Mass1, e5, e6):
     return e5+e6*Mass1

p0 = [0.15, 0.01]
dc13,cov = curve_fit(force16,Mass1,ds3,p0)
print('tst23')
print(dc13)

Mass1     = [ 47, 83, 132, 192, 241]
def force17(Mass1, e7, e8):
     return e7+e8*Mass1
print(force14)
p0 = [0.00015, 0.001]
dc14,cov = curve_fit(force17,Mass1,ds4,p0)
print('tst24')
print(dc14)

Mass1     = [ 47, 83, 132, 192, 241]
def force18(Mass1, e9, e10):
     return e9+e10*Mass1
p0 = [0.00015, 0.01]
dc15,cov = curve_fit(force18,Mass1,ds5,p0)
print('tst25')
print(dc15)

Mass1     = [ 47, 83, 132, 192, 241]
def force19(Mass1, e11, e12):
     return e11+e12*Mass1
p0 = [0.015, 0.01]
dc16,cov = curve_fit(force19,Mass1,ds6,p0)
print('tst26')
print(dc16)

e1, e2   = [0.07979565, 0.00274365]
e3, e4   = [ 1.7253542e-05, -2.36582829e-07]
e5, e6   = [-0.01936986, -0.00170407]
e7, e8   = [ 1.04424467e-05, -1.10635459e-08]
e9, e10  = [ 4.35863234e-03, -1.50074967e-06]
e11, e12 = [-1.57952234e-06,  5.82130267e-09]
d
m= np.array([51, 87, 135, 195, 243])
m.astype(int)
s=1700
v=1000
f = ((e1+e2*m)+(e3+e4*m)*s)- ((e5+e6*m)+(e7+e8*m)*s) * np.exp(-((e9+e10*m)+(e11+e12*m)*s) * v)
print('f')
print(f)

print('perpendicular perpendicular')


Breakingforce3 = np.array([BF5025ac,BF10025ac,BF15025ac,BF20025ac,BF30025ac,BF40025ac,BF60025ac,BF80025ac,BF100025ac,BF120025ac,BF140025ac,BF160025ac,BF180025ac])
Velocity3 = np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])

x = Velocity3
x.astype(int)
print(Velocity3)
def force(x, a1, a2, a3):
     return a1- a2 * np.exp(-(a3) * x)
p0 = [0.2,-0.2 , 0.003]
a,cov = curve_fit(force,x,Breakingforce3,p0)
print('tst')
print(a)
#plt.figure(91)
a1, a2,a3 = a
v_fit = force(x, a1, a2, a3)
plt.plot(x, force(x, a1, a2, a3))
plt.plot(x,Breakingforce3)
#plt.show(91)

Breakingforce4 = np.array([BF509ac,BF1009ac,BF1509ac,BF2009ac,BF3009ac,BF4009ac,BF6009ac,BF8009ac,BF10009ac,BF12009ac,BF14009ac,BF16009ac,BF18009ac])
Velocity4 = np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])

x = Velocity4
x.astype(int)
def force2(x, b1, b2, b3):
     return b1- b2 * np.exp(-(b3) * x)
p0 = [0.3, -0.03,  -1.56509123e-04]
b,cov = curve_fit(force2,x,Breakingforce4,p0)
print('tst1')
print(b)
b1, b2,b3 = b
v_fit = force2(x, b1, b2, b3)
#plt.figure(92)
plt.plot(x, force2(x, b1, b2, b3))
plt.plot(x,Breakingforce4)
#plt.show(92)

Breakingforce5 = np.array([BF50ac,BF100ac,BF150ac,BF200ac,BF300ac,BF400ac,BF600ac,BF800ac,BF1000ac,BF1200ac,BF1400ac,BF1600ac,BF1800ac])
Velocity5 = np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])

x = Velocity5
x.astype(int)
def force3(x, c1, c2, c3):
     return c1- c2 * np.exp(-(c3) * x)
p0 = [ 3.59826140e-01, -3.10702541e-01,  2.15036373e-04]
c,cov = curve_fit(force3,x,Breakingforce5,p0)
c1, c2, c3 = c
v_fit = force3(x, c1, c2, c3)
print('tst2')
print(c)
print(v_fit)
#plt.figure(93)
plt.plot(x, force3(x, c1, c2, c3))
plt.plot(x,Breakingforce5)
#plt.show(93)

a1, a2, a3 = [ 0.1180453,      -0.05379676,      0.00520317]
b1, b2, b3 = [ 2.12282188e-01,  5.10270036e-02, -1.56509123e-04]
c1, c2, c3 = [ 0.16111148,     -0.07918228,      0.00210525]

a11, a21, a31 = [ 0.14826932, -0.09118317,  0.00205387]
b11, b21, b31 = [ 0.22898281, -0.2101787,   0.04111213]
c11, c21, c31 = [ 0.22417241, -0.06617056,  0.00111414]

a12, a22, a32 = [ 0.25735809,     -0.13303314,      0.00799908]
b12, b22, b32 = [ 0.32124352,     -0.05497819,      0.0012281 ]
c12, c22, c32 = [-3.51446666e-02, -4.66226197e-01,  1.63032439e-04]

a13, a23, a33 = [ 0.3802309,  -0.09900091,  0.00580376]
b13, b23, b33 = [ 0.46652687, -0.03656948,  0.00342571]
c13, c23, c33 = [ 0.58978635,  0.02741042, -0.001033  ]

a14, a24, a34 = [ 0.47681962,     -0.21274697,      0.01352654]
b14, b24, b34 = [ 0.56503928,     -0.10361786,      0.0041526 ]
c14, c24, c34 = [ 3.59826140e-01, -3.10702541e-01,  2.15036373e-04]

Coefficient1 = [a1,b1,c1]
Coefficient2 = [a2,b2,c2]
Coefficient3 = [a3,b3,c3]



Coefficient4 = [a11,b11,c11]
Coefficient5 = [a21,b21,c21]
Coefficient6 = [a31,b31,c31]



Coefficient7 = [a12,b12,c12]
Coefficient8 = [a22,b22,c22]
Coefficient9 = [a32,b32,c32]



Coefficient10 = [a13,b13,c13]
Coefficient11 = [a23,b23,c23]
Coefficient12 = [a33,b33,c33]



Coefficient13 = [a14,b14,c14]
Coefficient14 = [a24,b24,c24]
Coefficient15 = [a34,b34,c34]

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc1,cov = curve_fit(force4,surface1,Coefficient1,p0)
print('tst3')
print(dc1)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc2,cov = curve_fit(force5,surface1,Coefficient2,p0)
print('tst4')
print(dc2)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
p0 = [0.0002, 0.00001]
dc3,cov = curve_fit(force6,surface1,Coefficient3,p0)
print('tst5')
print(dc3)

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc4,cov = curve_fit(force4,surface1,Coefficient4,p0)
print('tst6')
print(dc4)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc5,cov = curve_fit(force5,surface1,Coefficient5,p0)
print('tst7')
print(dc5)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc6,cov = curve_fit(force6,surface1,Coefficient6,p0)
print('tst8')
print(dc6)

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc1,cov = curve_fit(force4,surface1,Coefficient7,p0)
print('tst9')
print(dc1)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc2,cov = curve_fit(force5,surface1,Coefficient8,p0)
print('tst10')
print(dc2)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc3,cov = curve_fit(force6,surface1,Coefficient9,p0)
print('tst11')
print(dc3)

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc1,cov = curve_fit(force4,surface1,Coefficient10,p0)
print('tst12')
print(dc1)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc2,cov = curve_fit(force5,surface1,Coefficient11,p0)
print('tst13')
print(dc2)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc3,cov = curve_fit(force6,surface1,Coefficient12,p0)
print('tst14')
print(dc3)

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc1,cov = curve_fit(force4,surface1,Coefficient13,p0)
print('tst15')
print(dc1)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc2,cov = curve_fit(force5,surface1,Coefficient14,p0)
print('tst16')
print(dc2)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc3,cov = curve_fit(force6,surface1,Coefficient15,p0)
print('tst17')
print(dc3)

d1, d2   = [ 2.63939683e-01, -5.88980550e-05]
d3, d4   = [ 8.40579038e-02, -6.55148525e-05]
d5, d6   = [-3.31068878e-03,  3.34979945e-06]
d7, d8   = [ 2.86232930e-01, -5.04459313e-05]
d9, d10  = [-2.48943559e-01,  7.43722051e-05]
d11, d12 = [ 5.62594477e-02, -2.44114124e-05]
d13, d14 = [ 2.49030582e-01, -3.99283927e-05]
d15, d16 = [-1.35145789e-01, -4.87843452e-05]
d17, d18 = [-4.06409545e-03,  4.23186251e-06]
d19, d20 = [ 5.70537508e-01, -5.39349812e-05]
d21, d22 = [ 3.02800695e-02, -3.90196429e-05]
d23, d24 = [2.05480663e-04, 1.48628016e-06]
d25, d26 = [ 5.60961735e-01, -5.51372875e-05]
d27, d28 = [-9.30727805e-02, -6.82056918e-05]
d29, d30 = [-3.99508576e-03,  5.85871250e-06]

ds1 = [d1, d7, d13, d19, d25]
ds2 = [d2, d8, d14, d20, d26]
ds3 = [d3, d9, d15, d21, d27]
ds4 = [d4, d10, d16, d22, d28]
ds5 = [d5, d11, d17, d23, d29]
ds6 = [d6, d12, d18, d24, d30]

Mass1     = [ 47, 83, 132, 192, 241]
def force14(Mass1, e1, e2):
     return e1+e2*Mass1
print(force14)
p0 = [0.0015, 0.0005]
dc11,cov = curve_fit(force14,Mass1,ds1,p0)
print('tst21')
print(dc11)

Mass1     = [ 47, 83, 132, 192, 241]
def force15(Mass1, e3, e4):
     return e3+e4*Mass1
print(force14)
p0 = [0.00015, 0.0005]
dc12,cov = curve_fit(force15,Mass1,ds2,p0)
print('tst22')
print(dc12)

Mass1     = [ 47, 83, 132, 192, 241]
def force16(Mass1, e5, e6):
     return e5+e6*Mass1

p0 = [0.0015, 0.0001]
dc13,cov = curve_fit(force16,Mass1,ds3,p0)
print('tst23')
print(dc13)

Mass1     = [ 47, 83, 132, 192, 241]
def force17(Mass1, e7, e8):
     return e7+e8*Mass1
print(force14)
p0 = [0.00015, 0.001]
dc14,cov = curve_fit(force17,Mass1,ds4,p0)
print('tst24')
print(dc14)

Mass1     = [ 47, 83, 132, 192, 241]
def force18(Mass1, e9, e10):
     return e9+e10*Mass1
p0 = [0.00015, 0.0001]
dc15,cov = curve_fit(force18,Mass1,ds5,p0)
print('tst25')
print(dc15)

Mass1     = [ 47, 83, 132, 192, 241]
def force19(Mass1, e11, e12):
     return e11+e12*Mass1
p0 = [0.00015, 0.00001]
dc16,cov = curve_fit(force19,Mass1,ds6,p0)
print('tst26')
print(dc16)

e1, e2   = [0.13230488,       0.00182616]
e3, e4   = [-5.18955487e-05,  1.63035358e-09]
e5, e6   = [-6.84552434e-02, -2.95652336e-05]
e7, e8   = [ 8.70484942e-06, -2.74354781e-07]
e9, e10  = [ 0.02698863,     -0.00012928]
e11, e12 = [-1.14327027e-05,  6.86025265e-08]

m= np.array([52, 88, 136, 196, 244])
m.astype(int)
s=1700
v=1800
f = ((e1+e2*m)+(e3+e4*m)*s)- ((e5+e6*m)+(e7+e8*m)*s) * np.exp(-((e9+e10*m)+(e11+e12*m)*s) * v)
print('f')
print(f)

print('bs perpendicular')


Breakingforce3 = np.array([BF5025ad,BF10025ad,BF15025ad,BF20025ad,BF30025ad,BF40025ad,BF60025ad,BF80025ad,BF100025ad,BF120025ad,BF140025ad,BF160025ad,BF180025ad])
Velocity3 = np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])

x = Velocity3
x.astype(int)
print(Velocity3)
def force(x, a1, a2, a3):
     return a1- a2 * np.exp(-(a3) * x)
p0 = [ 0.07182605, -0.30217692,  0.0009506 ]
a,cov = curve_fit(force,x,Breakingforce3,p0)
print('tst')
print(a)
#plt.figure(91)
a1, a2,a3 = a
v_fit = force(x, a1, a2, a3)
plt.plot(x, force(x, a1, a2, a3))
plt.plot(x,Breakingforce3)
#plt.show(91)

Breakingforce4 = np.array([BF509ad,BF1009ad,BF1509ad,BF2009ad,BF3009ad,BF4009ad,BF6009ad,BF8009ad,BF10009ad,BF12009ad,BF14009ad,BF16009ad,BF18009ad])
Velocity4 = np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])

x = Velocity4
x.astype(int)
def force2(x, b1, b2, b3):
     return b1- b2 * np.exp(-(b3) * x)
p0 = [1.96332439e-01,  7.12974887e-02, -0.002]
b,cov = curve_fit(force2,x,Breakingforce4,p0)
print('tst1')
print(b)
b1, b2,b3 = b
v_fit = force2(x, b1, b2, b3)
print(v_fit)
#plt.figure(92)
plt.plot(x, force2(x, b1, b2, b3))
plt.plot(x,Breakingforce4)
#plt.show(92)

Breakingforce5 = np.array([BF50ad,BF100ad,BF150ad,BF200ad,BF300ad,BF400ad,BF600ad,BF800ad,BF1000ad,BF1200ad,BF1400ad,BF1600ad,BF1800ad])
Velocity5 = np.array([50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800])

x = Velocity5
x.astype(int)
def force3(x, c1, c2, c3):
     return c1- c2 * np.exp(-(c3) * x)
p0 = [ 2.58199366e-01,  4.20097511e-03, 0.002]
c,cov = curve_fit(force3,x,Breakingforce5,p0)
c1, c2, c3 = c
v_fit = force3(x, c1, c2, c3)
print('tst2')
print(c)
#plt.figure(93)
plt.plot(x, force3(x, c1, c2, c3))
plt.plot(x,Breakingforce5)
#plt.show(93)

a1, a2, a3 = [ 0.07182605, -0.30217692,  0.0009506 ]
b1, b2, b3 = [ 1.96332439e-01,  7.12974887e-05, -3.04445303e-03]
c1, c2, c3 = [ 2.58199366e-01,  4.20097511e-08, -7.92758632e-03]

a11, a21, a31 = [ 0.05407881, -0.39572829,  0.00070128]
b11, b21, b31 =[0.29391967, 0.16993783, 0.01456376]
c11, c21, c31 = [ 0.2892882,  -0.05023111,  0.01033896]

a12, a22, a32 = [ 0.26853812, -0.32928685,  0.00097763]
b12, b22, b32 = [0.39463062, 0.05805503, 0.00672774]
c12, c22, c32 = [0.42766441, 0.04524228, 0.00731654]

a13, a23, a33 = [ 0.43357286, -0.3113161,   0.00112157]
b13, b23, b33 = [ 0.53444017,  0.06005035,  0.00450679]
c13, c23, c33 = [ 0.55967517, -0.04160704,  0.00375273]

a14, a24, a34 = [ 0.57042869, -0.31464284,  0.00213378]
b14, b24, b34 = [ 0.69305115,  0.02276442, -0.00073813]
c14, c24, c34 = [ 0.69354062, -0.09407566,  0.02369574]

Coefficient1 = [a1,b1,c1]
Coefficient2 = [a2,b2,c2]
Coefficient3 = [a3,b3,c3]



Coefficient4 = [a11,b11,c11]
Coefficient5 = [a21,b21,c21]
Coefficient6 = [a31,b31,c31]



Coefficient7 = [a12,b12,c12]
Coefficient8 = [a22,b22,c22]
Coefficient9 = [a32,b32,c32]



Coefficient10 = [a13,b13,c13]
Coefficient11 = [a23,b23,c23]
Coefficient12 = [a33,b33,c33]



Coefficient13 = [a14,b14,c14]
Coefficient14 = [a24,b24,c24]
Coefficient15 = [a34,b34,c34]

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc1,cov = curve_fit(force4,surface1,Coefficient1,p0)
print('tst3')
print(dc1)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc2,cov = curve_fit(force5,surface1,Coefficient2,p0)
print('tst4')
print(dc2)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
p0 = [0.0002, 0.00001]
dc3,cov = curve_fit(force6,surface1,Coefficient3,p0)
print('tst5')
print(dc3)

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc4,cov = curve_fit(force4,surface1,Coefficient4,p0)
print('tst6')
print(dc4)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc5,cov = curve_fit(force5,surface1,Coefficient5,p0)
print('tst7')
print(dc5)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc6,cov = curve_fit(force6,surface1,Coefficient6,p0)
print('tst8')
print(dc6)

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc1,cov = curve_fit(force4,surface1,Coefficient7,p0)
print('tst9')
print(dc1)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc2,cov = curve_fit(force5,surface1,Coefficient8,p0)
print('tst10')
print(dc2)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc3,cov = curve_fit(force6,surface1,Coefficient9,p0)
print('tst11')
print(dc3)

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc1,cov = curve_fit(force4,surface1,Coefficient10,p0)
print('tst12')
print(dc1)


surface1 = [2500,900,1700]
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [0.001, 0.0001]
dc2,cov = curve_fit(force5,surface1,Coefficient11,p0)
print('tst13')
print(dc2)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc3,cov = curve_fit(force6,surface1,Coefficient12,p0)
print('tst14')
print(dc3)

surface1 = [2500,900,1700]
def force4(surface1, d1, d2):
     return d1+d2*surface1
print(force)
p0 = [0.001, 0.0001]
dc1,cov = curve_fit(force4,surface1,Coefficient13,p0)
print('tst15')
print(dc1)


surface1 = np.array([2500,900,1700])
surface1.astype(int)
def force5(surface1, d3, d4):
     return d3+d4*surface1
print(force)
p0 = [-0.000008, 0.0001]
dc2,cov = curve_fit(force5,surface1,Coefficient14,p0)
plt.figure(93)
plt.plot(surface1, force5(surface1,d3,d4))
plt.plot(surface1, Coefficient14)
plt.show(93)
print('tst16')
print(dc2)

surface1 = [2500,900,1700]
def force6(surface1, d5, d6):
     return d5+d6*surface1
print(force)
p0 = [0.0002, 0.00001]
dc3,cov = curve_fit(force6,surface1,Coefficient15,p0)
print('tst17')
print(dc3)

d1, d2   = [ 3.07740659e-01, -7.78164947e-05]
d3, d4   = [ 2.20436870e-01, -1.88905135e-04]
d5, d6   = [-7.58522363e-03,  2.49690814e-06]
d7, d8   = [ 4.67259806e-01, -1.49900537e-04]
d9, d10  = [ 5.09013063e-01, -3.53541325e-04]
d11, d12 = [ 2.32635517e-02, -8.66405001e-06]
d13, d14 = [ 4.97584331e-01, -7.88078125e-05]
d15, d16 = [ 3.36220900e-01, -2.42088675e-04]
d17, d18 = [ 1.11167952e-02, -3.59381875e-06]
d19, d20 = [ 6.16400913e-01, -6.30420664e-05]
d21, d22 = [ 2.96952589e-01, -2.32104031e-04]
d23, d24 = [ 6.72382626e-03, -2.11576251e-06]
d25, d26 = [ 7.82626521e-01, -7.66390401e-05]
d27, d28 = [ 2.29843854e-01, -2.10879538e-04]
d29, d30 = [ 5.31239207e-03,  1.79494392e-06]

ds1 = [d1, d7, d13, d19, d25]
ds2 = [d2, d8, d14, d20, d26]
ds3 = [d3, d9, d15, d21, d27]
ds4 = [d4, d10, d16, d22, d28]
ds5 = [d5, d11, d17, d23, d29]
ds6 = [d6, d12, d18, d24, d30]

Mass1     = [ 47, 83, 132, 192, 241]
def force14(Mass1, e1, e2):
     return e1+e2*Mass1
print(force14)
p0 = [0.0015, 0.0005]
dc11,cov = curve_fit(force14,Mass1,ds1,p0)
print('tst21')
print(dc11)

Mass1     = [ 47, 83, 132, 192, 241]
def force15(Mass1, e3, e4):
     return e3+e4*Mass1
print(force14)
p0 = [0.00015, 0.0005]
dc12,cov = curve_fit(force15,Mass1,ds2,p0)
print('tst22')
print(dc12)

Mass1     = [ 47, 83, 132, 192, 241]
def force16(Mass1, e5, e6):
     return e5+e6*Mass1

p0 = [0.0015, 0.0001]
dc13,cov = curve_fit(force16,Mass1,ds3,p0)
print('tst23')
print(dc13)

Mass1     = [ 47, 83, 132, 192, 241]
def force17(Mass1, e7, e8):
     return e7+e8*Mass1
print(force14)
p0 = [0.00015, 0.001]
dc14,cov = curve_fit(force17,Mass1,ds4,p0)
print('tst24')
print(dc14)

Mass1     = np.array([ 47, 83, 132, 192, 241])
Mass1.astype(int)
def force18(Mass1, e9, e10):
     return e9+e10*Mass1
p0 = [0.00015, 0.0001]
dc15,cov = curve_fit(force18,Mass1,ds5,p0)
plt.figure(95)
plt.plot(Mass1, force18(Mass1,e9,e10))
plt.plot(Mass1, ds5)
plt.show(95)
print('tst25')
print(dc15)

Mass1     = np.array([ 47, 83, 132, 192, 241])
Mass1.astype(int)
def force19(Mass1, e11, e12):
     return e11+e12*Mass1
p0 = [-0.01, 0.001]
dc16,cov = curve_fit(force19,Mass1,ds6,p0)
plt.figure(94)
plt.plot(Mass1, force19(Mass1,e11,e12))
plt.plot(Mass1, ds6)
plt.show(94)
print('tst26')
print(dc16)

e1, e2   = dc11
e3, e4   = dc12
e5, e6   = dc13
e7, e8   = dc14
e9, e10  = dc15
e11, e12 = dc16
print('e_values')
print(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12)

m= np.array([52, 88, 136, 196, 244])
m.astype(int)
s=900
v=100
f = ((e1+e2*m)+(e3+e4*m)*s)- ((e5+e6*m)+(e7+e8*m)*s) * np.exp(-((e9+e10*m)+(e11+e12*m)*s) * v)
print('f')
print(f)
