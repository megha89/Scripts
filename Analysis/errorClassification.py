# -*- coding: utf-8 -*-
import os
import sys
import csv
import time
import editdist


csv_file = "/Users/meghagupta/Documents/Github/Scripts/Analysis/tokens.csv"
csv_out = "/Users/meghagupta/Documents/Github/Scripts/Analysis/dataset.csv"

fout = open(csv_file, 'rb')
reader = csv.reader(fout)
fout1 = open(csv_out,'wb')
writer = csv.writer(fout1)
next(reader)

for row in reader:
    word1 = row[0]
    print word1
    word2 = row[1]
    print word2
    if editdist.distance(word1,word2) == 0 : 
        row[2] = "Not corrected"
        print word1, word2 + " Not corrected"
        writer.writerow(row)
        
    else:
        if (word1[0].upper() == word2[0]or word1[0].lower()==word2[0]) and editdist.distance(word1[0],word2[0]) == 1 and editdist.distance(word1,word2) == 1:
            print word1, word2 + " Corrected, Capitalization Error"
            row[2] = "Corrected, Capitalization Error"
            writer.writerow(row)

        elif editdist.distance(word1,word2) < 3 :
            row[2] = "Corrected, Spellcheck Error"
            print word1, word2 + " Corrected, Spellcheck Error"
            writer.writerow(row)
            
        elif editdist.distance(word1,word2) > 3:
            row[2] = "Additon of words"
            print word1, word2 + " Addition of words"
            writer.writerow(row)
            
        else:
            row[2] = "Others"
            print word1, word2 + "Others"
            writer.writerow(row)        
fout.close()
fout1.close()


