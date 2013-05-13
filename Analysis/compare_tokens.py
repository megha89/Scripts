import os
import sys
import csv
import time

csv_file = "C:/Users/Megha/Desktop/SEM4/DDM/Course Project/Scripts/error_classification.csv"
csv_out = "C:/Users/Megha/Desktop/SEM4/DDM/Course Project/Scripts/error_classification_label.csv"
fout = open(csv_file, 'rb')
reader = csv.reader(fout)
fout1 = open(csv_out,'wb')
writer = csv.writer(fout1)
#reader.next()
next(reader)
for row in reader:
    if row[0] == row[1]:
        row[2] = "Not corrected"
        writer.writerow(row)
    else:
        row[2] = "Corrected"
        writer.writerow(row)
fout.close()
fout1.close()
