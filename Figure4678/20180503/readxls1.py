#from here https://stackoverflow.com/a/44125624/4999991

import pandas as pd

xls = pd.ExcelFile("friction coeficient_41g.xls")

sheetX = xls.parse(4) #2 is the sheet number

var1 = sheetX[2]

print(var1[1]) #1 is the row number...