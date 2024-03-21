import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import ExcelWriter
from pandas import ExcelFile
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from collections import OrderedDict

df1 = pd.read_excel('1700mm/1700mm_1800mm_min.xls',['52g','88g','136g','196g','244g'], header=1)
print(df1)  
SF52  = df1['52g']['Standard force'].iloc[1:]
SF88  = df1['88g']['Standard force'].iloc[1:]
SF136 = df1['136g']['Standard force'].iloc[1:]
SF196 = df1['196g']['Standard force'].iloc[1:]
SF244 = df1['244g']['Standard force'].iloc[1:]
#Standardforce = np.column_stack((SF51,SF87,SF135,SF195,SF243))
#print(Standardforce)
D52  = df1['52g']['Strain'].iloc[1:]
D88  = df1['88g']['Strain'].iloc[1:]
D136 = df1['136g']['Strain'].iloc[1:]
D196 = df1['196g']['Strain'].iloc[1:]
D244 = df1['244g']['Strain'].iloc[1:]
#print(Displacement)

plt.figure(1)
plt.plot(D52 ,SF52 ,label = '52')
plt.plot(D88 ,SF88 ,label = '88g')
plt.plot(D136,SF136,label = '136g')
plt.plot(D196,SF196,label= '196g')
plt.plot(D244,SF244,label='244g')
plt.title('Friction force as a funtion of the displacement for different weights')
plt.xlabel('Displacement (mm)')
plt.ylabel('Friction force (N)')
plt.legend()

plt.show(1)

df2  = pd.read_excel('1700mm/1700mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('1700mm/1700mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('1700mm/1700mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('1700mm/1700mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('1700mm/1700mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('1700mm/1700mm_800mm_min.xls',['Results'], header=0)
df8  = pd.read_excel('1700mm/1700mm_600mm_min.xls',['Results'], header=0)
df9  = pd.read_excel('1700mm/1700mm_400mm_min.xls',['Results'], header=0)
df10 = pd.read_excel('1700mm/1700mm_300mm_min.xls',['Results'], header=0)
df11 = pd.read_excel('1700mm/1700mm_200mm_min.xls',['Results'], header=0)
df12 = pd.read_excel('1700mm/1700mm_150mm_min.xls',['Results'], header=0)
df13 = pd.read_excel('1700mm/1700mm_100mm_min.xls',['Results'], header=0)
df14 = pd.read_excel('1700mm/1700mm_50mm_min.xls',['Results'], header=0)

BF1800 = df2['Results']['Fmax'].iloc[1:]
BF1600 = df3['Results']['Fmax'].iloc[1:]
BF1400 = df4['Results']['Fmax'].iloc[1:]
BF1200 = df5['Results']['Fmax'].iloc[1:]
BF1000 = df6['Results']['Fmax'].iloc[1:]
BF800  = df7['Results']['Fmax'].iloc[1:]
BF600  = df8['Results']['Fmax'].iloc[1:]
BF400  = df9['Results']['Fmax'].iloc[1:]
BF300  = df10['Results']['Fmax'].iloc[1:]
BF200  = df11['Results']['Fmax'].iloc[1:]
BF150  = df12['Results']['Fmax'].iloc[1:]
BF100  = df13['Results']['Fmax'].iloc[1:]
BF50   = df14['Results']['Fmax'].iloc[1:]

t = 0 # decides from which column the breakingforce is taken and thus the weight of the boxes during the tests
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

Mass     = [52,88,136,196,244]
Velocity = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
print(Mass)
print(Velocity)

Breakingforce = np.matrix([BF50,BF100,BF150,BF200,BF300,BF400,BF600,BF800,BF1000,BF1200,BF1400,BF1600,BF1800])
print(Breakingforce)

Mass, Velocity = np.meshgrid(Mass, Velocity)
plt.figure(2)
cp = plt.contour(Mass,Velocity,Breakingforce)
plt.clabel(cp, inline=True, fontsize=10)
plt.xlabel('Mass (g)')
plt.ylabel('Velocity (mm/min)')
plt.title('Contourplot of Breakingforce as a function of the sliding speed and weigth (1700mm)')
plt.show(2)

fig = plt.figure(3)
ax = fig.gca(projection='3d')
surf = ax.plot_surface(Mass, Velocity, Breakingforce, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Breakingforce as a function of sliding speed and weight (1700mm')
plt.xlabel('Mass (g)')
plt.ylabel('Velocity (mm/min)')
plt.show(3)

df2  = pd.read_excel('900mm/900mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('900mm/900mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('900mm/900mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('900mm/900mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('900mm/900mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('900mm/900mm_800mm_min.xls',['Results'], header=0)
df8  = pd.read_excel('900mm/900mm_600mm_min.xls',['Results'], header=0)
df9  = pd.read_excel('900mm/900mm_400mm_min.xls',['Results'], header=0)
df10 = pd.read_excel('900mm/900mm_300mm_min.xls',['Results'], header=0)
df11 = pd.read_excel('900mm/900mm_200mm_min.xls',['Results'], header=0)
df12 = pd.read_excel('900mm/900mm_150mm_min.xls',['Results'], header=0)
df13 = pd.read_excel('900mm/900mm_100mm_min.xls',['Results'], header=0)
df14 = pd.read_excel('900mm/900mm_50mm_min.xls',['Results'], header=0)

BF18009 = df2['Results']['Fmax'].iloc[1:]
BF16009 = df3['Results']['Fmax'].iloc[1:]
BF14009 = df4['Results']['Fmax'].iloc[1:]
BF12009 = df5['Results']['Fmax'].iloc[1:]
BF10009 = df6['Results']['Fmax'].iloc[1:]
BF8009  = df7['Results']['Fmax'].iloc[1:]
BF6009  = df8['Results']['Fmax'].iloc[1:]
BF4009  = df9['Results']['Fmax'].iloc[1:]
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
Mass2, Velocity2 = np.meshgrid(Mass2, Velocity2)
print(Breakingforce2)
fig  = plt.figure(4)
ax   = fig.gca(projection='3d')
surf = ax.plot_surface(Mass2, Velocity2, Breakingforce2, cmap=cm.coolwarm,linewidth=0, antialiased=False)
plt.title('Breakingforce as a function of sliding speed and weight (900mm)')
plt.xlabel('Mass (g)')
plt.ylabel('Velocity (mm/min)')
plt.show(4)

BF44  = np.array(Breakingforce2[:,0])
BF80  = np.array(Breakingforce2[:,1])
BF128 = np.array(Breakingforce2[:,2])
BF188 = np.array(Breakingforce2[:,3])
BF236 = np.array(Breakingforce2[:,4])
plt.figure(5)
#plt.plot(Velocity2, Breakingforce2)
plt.plot(Velocity2, BF44 ,'b', label= '44g')
plt.plot(Velocity2, BF80 ,'g', label= '80g')
plt.plot(Velocity2, BF128,'r', label= '128g')
plt.plot(Velocity2, BF188,'m', label= '188g')
plt.plot(Velocity2, BF236,'c', label= '236g')
plt.title('Breakingforce as a function of sliding speed for different weights (900mm)')
plt.ylabel('Breakingforce (N)')
plt.xlabel('Velocity (mm/min)')
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())
plt.show(5)

df2  = pd.read_excel('2500mm/2500mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('2500mm/2500mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('2500mm/2500mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('2500mm/2500mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('2500mm/2500mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('2500mm/2500mm_800mm_min.xls',['Results'], header=0)
df8  = pd.read_excel('2500mm/2500mm_600mm_min.xls',['Results'], header=0)
df9  = pd.read_excel('2500mm/2500mm_400mm_min.xls',['Results'], header=0)
df10 = pd.read_excel('2500mm/2500mm_300mm_min.xls',['Results'], header=0)
df11 = pd.read_excel('2500mm/2500mm_200mm_min.xls',['Results'], header=0)
df12 = pd.read_excel('2500mm/2500mm_150mm_min.xls',['Results'], header=0)
df13 = pd.read_excel('2500mm/2500mm_100mm_min.xls',['Results'], header=0)
df14 = pd.read_excel('2500mm/2500mm_50mm_min.xls',['Results'], header=0)

BF180025 = df2['Results']['Fmax'].iloc[1:]
BF160025 = df3['Results']['Fmax'].iloc[1:]
BF140025 = df4['Results']['Fmax'].iloc[1:]
BF120025 = df5['Results']['Fmax'].iloc[1:]
BF100025 = df6['Results']['Fmax'].iloc[1:]
BF80025  = df7['Results']['Fmax'].iloc[1:]
BF60025  = df8['Results']['Fmax'].iloc[1:]
BF40025  = df9['Results']['Fmax'].iloc[1:]
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

fig = plt.figure(6)
ax = fig.gca(projection='3d')
surf = ax.plot_surface(Mass3, Velocity3, Breakingforce3, cmap=cm.coolwarm,linewidth=0, antialiased=False)
plt.title('Breakforce as a function of sliding speed and weight (2500mm)')
plt.ylabel('Velocity (mm/min)')
plt.xlabel('Mass (g)')
plt.show(6)


Breakf1751      = Breakingforce[:,0]
Breakf17135     = Breakingforce[:,2]
Breakf944       = Breakingforce2[:,0]
Breakf9128      = Breakingforce2[:,2]
Breakf2547      = Breakingforce3[:,0]
Breakf25131     = Breakingforce3[:,2]

plt.figure(7)
plt.plot(Velocity2,Breakf944  ,'r',label='900mm, 44g'  )
plt.plot(Velocity, Breakf1751 ,'b',label='1700mm, 51g' )
plt.plot(Velocity3,Breakf2547 ,'g',label='2500mm, 47g' )
plt.plot(Velocity2,Breakf9128 ,'m',label='900mm, 128g' )
plt.plot(Velocity, Breakf17135,'c',label='1700mm, 135g')
plt.plot(Velocity3,Breakf25131,'k',label='2500mm, 131g')
plt.ylabel('Breakingforce (N)')
plt.xlabel('Velocity (mm/min)')
plt.title('Breakforce as a function of sliding speed for different surface areas')
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())
plt.show(7)

Breakparper     = np.matrix([BF1009,BF100,BF10025])#varying Weight and surface areas, same orientation and sliding speed
Surfacearea1 = [ 900, 1700, 2500]
Massavg     = [ 48, 84, 133, 193, 242]
Massavg, Surfacearea1,  = np.meshgrid(Massavg,Surfacearea1, )

fig = plt.figure(8)
ax = fig.gca(projection='3d')
surf = ax.plot_surface(Massavg, Surfacearea1, Breakparper, cmap=cm.coolwarm,linewidth=0, antialiased=False)
plt.title('Breakforce as a function of weight and surfacearea (Sliding speed 100mm/min)')
plt.ylabel('Surfacearea (mm^2)')
plt.xlabel('Weight (g)')
plt.show(8)

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


Surfacearea2= [900,1700,2500]
Velocity4 = [1800,1600,1400,1200,1000,800,600,400,300,200,150,100,50]
Surfacearea2,Velocity4 = np.meshgrid(Surfacearea2,Velocity4)
Break47= np.matrix([para1,para2,para3,para4,para5,para6,para7,para8,para9,para10,para11,para12,para13])

print('Break47')
print(Break47)
print(Surfacearea2,Velocity4)

fig = plt.figure(9)
ax = fig.gca(projection='3d')
surf = ax.plot_surface(Surfacearea2, Velocity4, Break47, cmap=cm.coolwarm,linewidth=0, antialiased=False)
plt.title('Breakforce as a function of sliding speed and surfacearea (weigth 47g +/-3g)')
plt.xlabel('Surfacearea (mm^2)')
plt.ylabel('Velocity (mm/min)')
plt.show(9)
