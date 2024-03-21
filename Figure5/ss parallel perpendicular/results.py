import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import ExcelWriter
from pandas import ExcelFile
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


df1 = pd.read_excel('1700mm/1700mm_1800mm_min.xls',['51g','87g','135g','195g','243g'], header=1)
print(df1)  
SF51  = df1['51g']['Standard force'].iloc[1:]
SF87  = df1['87g']['Standard force'].iloc[1:]
SF135 = df1['135g']['Standard force'].iloc[1:]
SF195 = df1['195g']['Standard force'].iloc[1:]
SF243 = df1['243g']['Standard force'].iloc[1:]
#Standardforce = np.column_stack((SF51,SF87,SF135,SF195,SF243))
#print(Standardforce)
D51  = df1['51g']['Strain'].iloc[1:]
D87  = df1['87g']['Strain'].iloc[1:]
D135 = df1['135g']['Strain'].iloc[1:]
D195 = df1['195g']['Strain'].iloc[1:]
D243 = df1['243g']['Strain'].iloc[1:]
#print(Displacement)

plt.figure(1)
plt.plot(D51,SF51,D87,SF87,D135,SF135,D195,SF195,D243,SF243)
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

Mass     = [51,87,135,195,243]
Velocity = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
print(Mass)
print(Velocity)

Breakingforce = np.matrix([BF50,BF100,BF150,BF200,BF300,BF400,BF600,BF800,BF1000,BF1200,BF1400,BF1600,BF1800])
print(Breakingforce)

Mass, Velocity = np.meshgrid(Mass, Velocity)
plt.figure(2)
cp = plt.contour(Mass,Velocity,Breakingforce)
plt.clabel(cp, inline=True, 
          fontsize=10)
plt.xlabel('x (grams)')
plt.ylabel('y (mm/min)')
plt.show(2)

fig = plt.figure(3)
ax = fig.gca(projection='3d')
surf = ax.plot_surface(Mass, Velocity, Breakingforce, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
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

Mass2            = [44,80,128,188,236]
Velocity2        = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
Breakingforce2   = np.matrix([BF509,BF1009,BF1509,BF2009,BF3009,BF4009,BF6009,BF8009,BF10009,BF12009,BF14009,BF16009,BF18009])
Mass2, Velocity2 = np.meshgrid(Mass2, Velocity2)
print(Breakingforce2)
fig  = plt.figure(4)
ax   = fig.gca(projection='3d')
surf = ax.plot_surface(Mass2, Velocity2, Breakingforce2, cmap=cm.coolwarm,linewidth=0, antialiased=False)
plt.show(4)

plt.figure(5)
plt.plot(Velocity2, Breakingforce2)
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

Mass3     = [44,80,128,188,236]
Velocity3 = [50,100,150,200,300,400,600,800,1000,1200,1400,1600,1800]
Breakingforce3 = np.matrix([BF5025,BF10025,BF15025,BF20025,BF30025,BF40025,BF60025,BF80025,BF100025,BF120025,BF140025,BF160025,BF180025])
Mass3, Velocity3 = np.meshgrid(Mass3, Velocity3)

fig = plt.figure(6)
ax = fig.gca(projection='3d')
surf = ax.plot_surface(Mass3, Velocity3, Breakingforce3, cmap=cm.coolwarm,linewidth=0, antialiased=False)
plt.show(6)

Breakf1     = np.array(Breakingforce[:,0])
print(Breakf1)
Breakf2     = np.array(Breakingforce2[:,0])
print(Breakf2)
Breakf3     = np.array(Breakingforce3[:,0])
print(Breakf3)
Breakparper = np.column_stack((Breakf1,Breakf2,Breakf3))         #varying speeds and surface areas, same orientation and about the same weihght
print(Breakparper)
plt.figure(7)
plt.plot(Velocity, Breakf1,'--b',Velocity2,Breakf2,'--r',Velocity3,Breakf3,'--g')
plt.show(7)
