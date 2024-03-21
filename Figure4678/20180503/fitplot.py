#from here https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/

import csv

x = []
y = []

with open('maxs.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)


import matplotlib.pyplot as plt
