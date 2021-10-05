import csv

data = []


def upload(file_path):
    global data
    with open(file_path, newline='') as csvFile:
        rows = csv.reader(csvFile, delimiter=',')
        data = []
        for row in rows:
            data.append(row)
    headers = data.pop(0)
    return data


def merge(file_path):
    global data
    with open(file_path, newline='') as csvFile:
        rows = csv.reader(csvFile, delimiter=',')
        merge = []
        for row in rows:
            merge.append(row)
    headers = merge.pop(0)
    for row in merge:
        data.append(row)
    return data


def check_app_has_data():
    import datacontroller as dc
    import PySimpleGUI as sg
    from logging import error
    import sys
    if dc.data == []:
        file_name = sg.PopupGetFile('Please select file to upload (the file to add to or merge in)',
                                    file_types=(("Comma separated value", "*.csv"),))
        if not file_name:
            error("No file provided. Exiting application.")
            sys.exit()
        dc.upload(file_name)
        if dc.data == []:
            error("App did not receive data. Exiting application.")
            sys.exit()

# def readLocation(file_path):
#     global data2
#     data2 = pd.read_csv(file_path,
#                        usecols=['decimalLatitude', 'decimalLongitude'])
#     return data2