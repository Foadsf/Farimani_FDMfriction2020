#from here: https://stackoverflow.com/a/43257810/4999991

import xlrd
workbook = xlrd.open_workbook('friction coeficient_41g.xls')
worksheet = workbook.sheet_by_name('Specimen 1')
print(worksheet.cell(0, 0).value)