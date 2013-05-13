import os
import sys
import csv
import time

csv_file = 'C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Scripts\error_classification.csv'
logfile = 'C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Dataset'
fout = open(csv_file, 'wb')
fout1 = csv.writer(fout, delimiter=',')
fout1.writerow(('Old Text Tokens','New Text Tokens','Label'))
transposed = []
count = 0           
#fin = open(logfile,'r')
the_list = []
str1 = ""
for root, subFolders, files in os.walk(logfile):
    for filename in files:
        filePath = os.path.join(root, filename)
        with open( filePath, 'r' ) as fin:
            #for lines in fin:
                    line = 
                    line = line.lstrip()
                    print line
                    if line.startswith('<OldTextValue>') or line.startswith('<NewTextValue>'):
                        
                        count = count+1
                        length = len(line)
                        line = line[14:length-16]
                        fields = line.split()
                        the_list.append(fields)
                        if count == 2:
                            print the_list
                            for i in range(len(fields)):
                                transposed.append([row[i] for row in the_list])
                            count = 0
                            the_list.pop(1)
                            the_list.pop(0)
                        else :
                            print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                            print line
                            continue
                    else:
                        continue
print transposed
fout1.writerows(transposed)
fout.close()
fin.close()
   #for root, subFolders, files in os.walk(logfile):
#    for filename in files:
#        filePath = os.path.join(root, filename)
#        with open( filePath, 'r' ) as fin:
