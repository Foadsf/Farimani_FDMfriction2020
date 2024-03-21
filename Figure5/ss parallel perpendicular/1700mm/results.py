import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import ExcelWriter
from pandas import ExcelFile
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


df1 = pd.read_excel('1700mm_1800mm_min.xls',['51g','87g','135g','195g','243g'], header=1)
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

df2  = pd.read_excel('1700mm_1800mm_min.xls',['Results'], header=0)
df3  = pd.read_excel('1700mm_1600mm_min.xls',['Results'], header=0)
df4  = pd.read_excel('1700mm_1400mm_min.xls',['Results'], header=0)
df5  = pd.read_excel('1700mm_1200mm_min.xls',['Results'], header=0)
df6  = pd.read_excel('1700mm_1000mm_min.xls',['Results'], header=0)
df7  = pd.read_excel('1700mm_800mm_min.xls',['Results'], header=0)
df8  = pd.read_excel('1700mm_600mm_min.xls',['Results'], header=0)
df9  = pd.read_excel('1700mm_400mm_min.xls',['Results'], header=0)
df10 = pd.read_excel('1700mm_300mm_min.xls',['Results'], header=0)
df11 = pd.read_excel('1700mm_200mm_min.xls',['Results'], header=0)
df12 = pd.read_excel('1700mm_150mm_min.xls',['Results'], header=0)
df13 = pd.read_excel('1700mm_100mm_min.xls',['Results'], header=0)
df14 = pd.read_excel('1700mm_50mm_min.xls',['Results'], header=0)

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
