
import time
import csv
import os
import sys
import datetime
import calendar
fout = open('C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Newspapers\NamesNewsppr.txt','w+')

rootdir =r'C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Dataset'
dirs = os.listdir(rootdir)
for file in dirs:
    filename = file
    index = filename.find('-')
    filename = filename[:index]
    #print "Actual file",filename
    date = filename[-2:]
    #print "date",date
    filename = filename[:-2]
    #print "remaining filename",filename
    month = filename[-2:]
    #month = int(month)
    #month = calendar.month_name[month]
    #print "month",month
    filename = filename[:-2]
    #print "remaining filename",filename
    year = filename[-4:]
    #print "year",year
    filename = filename[:-4]
    #print "remaining filename",filename
    if filename =='AL':
        print "Amador Ledger, "+ year+"-"+ str(month) +"-"+ date
        fout.write("Amador Ledger, "+ year +"-"+ str(month) +"-"+ date+"\n")
    else:
        print "Californian, "+ year +"-"+ str(month) +"-"+date
        fout.write("Californian, "+ year +"-"+ str(month) +"-"+date+"\n")
fout.close()
