# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:45:55 2013

@author: meghagupta
"""

import os
import sys
import csv

in_file = '/Users/meghagupta/Downloads/libsvm-3.17/matlab/UJITEST.csv'
fin = open(in_file,'r')
reader = csv.reader(fin)
out_file = '/Users/meghagupta/Downloads/libsvm-3.17/matlab/ujiTest.dat'
fout = open(out_file,'w')
writer = csv.writer(fout)
#next(reader)
for row in reader:
    col1 = row[0]
    col2 = row[1]
    col3 = row[2]
#    col4 = row[3]
#    col5 = row[4]
#    col6 = row[5]
#    col7 = row[6]
   # print col1,' 1:',col2,' 2:',col3,' 3:',col4,' 4:',col5,' 5:',col6,' 6:',col7
    writer.writerow([col1,' 1:'+col2,' 2:'+col3])
#    writer.writerow(row)



