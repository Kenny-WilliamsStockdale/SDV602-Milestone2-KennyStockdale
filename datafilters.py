import datacontroller as dc
import csv
import pandas as pd

def readLocation(file_path):
    data = pd.read_csv(file_path,
                       usecols=['decimalLatitude', 'decimalLongitude'])
    return data


def merge(newFile, currentFile):
    dc.append(newFile, currentFile)


def fishAmountYear():  
    data = dc.data
    dictline = {}
    for row in data:
        if row[19] != "":
            # if row[19] in dictline.keys():
            #     dictline[row[19]].append(row[10])
            # else:
            #     dictline[row[19]] = [row[10]]
            if row[19] in dictline.keys():
                dictline[row[19]] += int(row[10])
            else:
                dictline[row[19]] = int(row[10])
            
    # labels = list(dictline.keys())
    # values = list(dictline.values())
    
    return (dictline)


def sizeFish(): # piechart data
    data = dc.data
    barData = {
        '1-50': 0,
        '51-100': 0,
        '101-150': 0,
        '151-200': 0,
        '201-250': 0,
        '251+': 0
    }
    for row in data:
        size = int(row[6].split(' ')[0]) if row[6] != '' else 0

        if size in range(1, 51):
            barData['1-50'] += 1
        elif size in range(51, 101):
            barData['51-100'] += 1
        elif size in range(101, 151):
            barData['101-150'] += 1
        elif size in range(151, 201):
            barData['151-200'] += 1
        elif size in range(201, 251):
            barData['201-250'] += 1
        elif size > 251:
            barData['251+'] += 1
    labels = list(barData.keys())
    values = list(barData.values())
    return labels, values
    

if __name__ == '__main__':
    print(readLocation('./data/test_data_1.csv'))
    