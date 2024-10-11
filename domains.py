import csv
import pytz
import datetime

with open('domains.csv') as myfile:
    myreader = csv.reader(myfile)
    for row in myreader:
        print(row)