import csv
import os
import sys
import urllib2
import json

date = '1900-01-05'
count = 0
rootdir = r'C:/Users/Megha/Desktop/SEM4/DDM/Course Project/Newspapers/urlNames.txt'
fin = open(rootdir,'r+')
for i in range(190):
    print date.strip(' \t\n\r');
    output = 'C:/Users/Megha/Desktop/SEM4/DDM/Course Project/Newspapers/RawOCRText/'+date.strip(' \t\n\r')+'.txt'
    print output
    fout = open(output,'ab')
    for lines in fin:
        count = count + 1
        if count/9 == 1:
            date = lines
            count = 0
            break
        line = lines
        try:
            response = urllib2.urlopen(line)
            html = response.read()
        except urllib2.HTTPError:
            continue
        print html    
        fout.write(html)        
fin.close()
fout.close()
