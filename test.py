
import csv
import sys


#read csv, and split on "," the line
csv_file = csv.reader(open('stat.csv', "r"), delimiter=",")

nom = 'soso'

#loop through the csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if nom == row[2]:
        print (row)

    # print(row[2])


def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))