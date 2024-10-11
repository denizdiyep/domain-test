import csv
import pytz
import datetime

with open('domains.csv') as myfile:
    myreader = csv.reader(myfile)
    for row in myreader:
        # gelen satırı sutunlara böl
        mycolumns = row[0].split('|')

        # bolunen sutunları ayrı degiskenlere ata
        domain = mycolumns[0]
        startdateStr = mycolumns[1]
        enddateStr = mycolumns[2]
        statusStr = mycolumns[3]
        
        # domain buyuk halini degiskene ata
        bigDomain = domain.upper()
        
        # ihtiyaımız olan timezonelar degiskenlere atanır
        utcTimezone = pytz.timezone('UTC')
        turkeyTimezone = pytz.timezone('Europe/Istanbul')

        # string tarih datetime nesnesine cevrilir
        startdate = datetime.datetime.strptime(startdateStr, '%Y-%m-%d %H:%M')
        enddate = datetime.datetime.strptime(enddateStr, '%Y-%m-%d %H:%M')

        # string tarihi Türkiye zaman diliminde oldugunu soyledik
        startdateTurkey = turkeyTimezone.localize(startdate)
        enddateTurkey = turkeyTimezone.localize(enddate)

        # Turkiye zaman diliminde olan deger UTC olarak cevrildi
        startdateTurkey = startdateTurkey.astimezone(utcTimezone)
        enddateTurkey = enddateTurkey.astimezone(utcTimezone)
        
        if statusStr == 'Aktif':
            status = 'ayşe'
        else:
            status = 'fatma'

        print(status)