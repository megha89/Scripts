import os
import sys
import time
import csv

csv_file = "C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Scripts\count_csv.csv"
logfile = "C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Dataset"
fout = csv.writer(open(csv_file, 'wb'))
fout.writerow(('Logfile Name','No. of Lines'))
for root, subFolders, files in os.walk(logfile):
    for filename in files:
        filePath = os.path.join(root, filename)
        with open( filePath, 'r' ) as fin:
            count = 0
            for lines in fin:
                lines = lines.lstrip()
                if lines.startswith("<NewTextValue>"):
                    count = count + 1
            print filename
            print count
            fout.writerow((filename,count ))
            


