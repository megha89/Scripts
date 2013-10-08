import sys
import os
output = 'C:/Users/Megha/Desktop/SEM4/DDM/Course Project/Newspapers/urlNames1.txt'
fout = open(output,'w+')
rootdir = r'C:/Users/Megha/Desktop/SEM4/DDM/Course Project/Newspapers/NamesNewsppr.txt'
fin = open(rootdir,'r')
for file in fin:
    newsppr = file
    index = newsppr.find(',')
    date = newsppr[index+2:]
    date = date.rstrip()
    #print date
    #print "http://chroniclingamerica.loc.gov/lccn/sn93052980/"+date+"/ed-1/seq-1/ocr.txt"
    #print "http://chroniclingamerica.loc.gov/lccn/sn93052980/"+date+"/ed-1/seq-2/ocr.txt"
    #print "http://chroniclingamerica.loc.gov/lccn/sn93052980/"+date+"/ed-1/seq-3/ocr.txt"
    #print "http://chroniclingamerica.loc.gov/lccn/sn93052980/"+date+"/ed-1/seq-4/ocr.txt" 
    #fout.write (date+'\n')
    fout.write ("http://chroniclingamerica.loc.gov/lccn/sn93052980/"+date+"/ed-1/seq-1/ocr.txt"+"\n")
    fout.write ("http://chroniclingamerica.loc.gov/lccn/sn93052980/"+date+"/ed-1/seq-2/ocr.txt"+"\n")
    fout.write ("http://chroniclingamerica.loc.gov/lccn/sn93052980/"+date+"/ed-1/seq-3/ocr.txt"+"\n")
    fout.write ("http://chroniclingamerica.loc.gov/lccn/sn93052980/"+date+"/ed-1/seq-4/ocr.txt"+"\n")
    fout.write ("http://chroniclingamerica.loc.gov/lccn/sn93052980/"+date+"/ed-1/seq-5/ocr.txt"+"\n")
    fout.write ("http://chroniclingamerica.loc.gov/lccn/sn93052980/"+date+"/ed-1/seq-6/ocr.txt"+"\n")
    fout.write ("http://chroniclingamerica.loc.gov/lccn/sn93052980/"+date+"/ed-1/seq-7/ocr.txt"+"\n")
    fout.write ("http://chroniclingamerica.loc.gov/lccn/sn93052980/"+date+"/ed-1/seq-8/ocr.txt"+"\n")
    
fout.close()
