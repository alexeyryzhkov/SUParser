# coding: utf8

import csv
from sys import argv

script, filename = argv


csvfile = open(filename)
csvreader = csv.reader(csvfile)
csvdata = list(csvreader)

cut_head_fut = csvdata[4:-1]


mnt = filename[:2]


outputFile = open('output' + mnt + '.csv', 'wb')
outputWriter = csv.writer(outputFile)
for row in cut_head_fut:
    row = row [1:]
    row = row + [mnt]
    if row[6] == '55':
        row = row + ['SabreIX']
    elif row[6] == '62':
        row = row + ['Голосовая платформа']
    elif row[6] == '8001':
        row = row + ['Голосовая платформа']
    elif row[6] == '8003':
        row = row + ['Голосовая платформа']
    elif row[6] == '7128':
        row = row + ['ID90T']
    elif row[6] == '7129':
        row = row + ['Сайт']
    elif row[6] == '7130':
        row = row + ['Сайт']
    elif row[6] == '555002':
        row = row + ['Сайт']
    elif row[6] == '555001':
        row = row + ['Сайт']
    elif row[6] == '8002':
        row = row + ['ЕПР']
    elif row[6] == '8006':
        row = row + ['ЕПР']
    elif row[6] == '970007':
        row = row + ['ЕПР']
    elif row[6] == '970008':
        row = row + ['ЕПР']
    elif row[6] == '8010':
        row = row + ['NetLine']
    elif row[6] == '851176':
        row = row + ['TAIS']
    elif row[6] == '851177':
        row = row + ['TAIS']
    elif row[6] == '970011':
        row = row + ['ПЭК']
    elif row[6] == '970010':
        row = row + ['ПЭК']



    outputWriter.writerow(row)

outputFile.close()
