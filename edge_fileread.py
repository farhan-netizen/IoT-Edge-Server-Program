# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:24:58 2021

@author: ashra
"""
import csv
import itertools

# Current row starts at 1 becaues row 0 is header
currentRowCount = 0

def readCSV(filename, rowPosition):
    with open(filename, "r") as csvfile:
        datareader = csv.reader(csvfile)
        print(datareader)
        count = -1
        item = {}
        for row in datareader:
            count = count + 1
            if count == 0:
                item = { 'sNo': 'S. No.', 'timestamp': 'Timestamp', 'data': 'Value', 'deviceID': 'Device Id'}
       
            elif count == rowPosition:
                # If the current count is 0 then we have already created the dictionary object with headers else, for the rest of rows we are create creating dict here
                if count > 0:
                    item = { 'sNo': count, 'timestamp': row[0], 'data': row[1], 'deviceID': row[2]}
                return item
        #This will return the first header row, it will be the case when rowPosition deos not match or exceeds row count
        return item
        
def getRowFromCSV():
    global currentRowCount
    print(currentRowCount)
    item = readCSV(r'C:\Users\ashra\OneDrive\Desktop\Farhan\dataset.csv', currentRowCount)
    
    #In case sNo is not same as currentRowCount this means the loop did not find our specified row number
    #This will happen only when our specified row number is more than CSV row count
    #In this case the readCSV function would return the first row, so lets set the currentRowCount to 1 so that next iteration it looks for 2nd record in CSV

    if not item['sNo'] == currentRowCount:
        currentRowCount = 1
    # Send this item to Server
    currentRowCount = currentRowCount + 1
    return item