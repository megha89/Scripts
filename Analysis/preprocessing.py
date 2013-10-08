# -*- coding: utf-8 -*-
import os
import sys
import csv
import time
import editdist

csv_file = "/Users/meghagupta/Documents/Github/Scripts/Analysis/errorClassificationNew.csv"
csv_out = "/Users/meghagupta/Documents/Github/Scripts/Analysis/prep2.csv"

fin = open(csv_file, 'rb')
reader = csv.reader(fin)
fout = open(csv_out,'wb')
writer = csv.writer(fout)
writer.writerow(['oldText','newText','sameLength','editDist_0','NOCORRECTION','editDistAbove1','editDistBelow3','editDist_1andcaseChange','SPELLCHECK','ADDITION','CAPITALIZATION','TYPO'])
next(reader)
for row in reader:
#    print row
    oldText =  row[0]
#    print oldText
#    oldText =  'largest'
    newText = row[1]
#    print newText
#    newText = 'largest'

    if len(oldText) == len(newText):
        sameLength = 1
        row[2] = sameLength
 #       print "Length is same",row[2]
        
        if oldText == newText:
            editDist_0 = 1
            row[3] = editDist_0
            #print  oldText,"and",newText,"are equal",editDist_0
            NOCORRECTION = 1
            row[4] = NOCORRECTION
            #print  "NOT CORRECTION",NOCORRECTION
            row[5]=0
            row[6]=0
            row[7]=0
            row[8]=0
            row[9]=0
            row[10]=0
            row[11]=0
            writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
        else:
            editDist_0 = 0
            row[3] = editDist_0
            #print  oldText,"and",newText,"are not equal",editDist_0
            NOCORRECTION = 0
            row[4] = NOCORRECTION
            #print  "NO CORRECTION",NOCORRECTION

            if editdist.distance(oldText,newText) > 1:
                editDistAbove1 = 1
                row[5] = editDistAbove1
#                print "Edit Distance > 1",editDistAbove1

                if editdist.distance(oldText,newText) < 3:
                    sameLength = 1
                    row[2] = sameLength
                    editDist_0 = 0
                    row[3] = editDist_0
                    NOCORRECTION = 0
                    row[4] = NOCORRECTION
                    editDistAbove1 = 1
                    row[5] = editDistAbove1
                    editDistBelow3 = 1
                    row[6] = editDistBelow3
                    row[7] = 0
                    SPELLCHECK = 1
                    row[8] = SPELLCHECK
                    row[9] = 0
                    row[10] = 0
                    row[11] = 0
 #                   print "SPELLCHECK ERROR",SPELLCHECK
                    writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])

                else:
                    sameLength = 1
                    row[2] = sameLength
                    editDist_0 = 0
                    row[3] = editDist_0
                    NOCORRECTION = 0
                    row[4] = NOCORRECTION
                    editDistAbove1 = 1
                    row[5] = editDistAbove1
                    editDistBelow3 = 0
                    row[6] = editDistBelow3
                    row[7] = 0
#                    print "Difference < 3",editDistBelow3
                    row[8] = 0
 #                   print "SPELLCHECK ERROR",SPELLCHECK
                    ADDITION = 1
                    row[9] = ADDITION
                    row[10] = 0
                    row[11] = 0
#                    print "ADDITION OF WORDS",ADDITION
                    writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])

            else:
                #if oldText[0].upper() == newText[0] or oldText[0].lower() == newText[0]:
               
#                print "Edit Distance <=1",editDistAbove1
                if editdist.distance(oldText[0],newText[0]) == 1 and (oldText[0].upper() == newText[0]or oldText[0].lower() == newText[0]):
                    sameLength = 1
                    row[2] = sameLength
                    editDist_0 = 0
                    row[3] = editDist_0
                    NOCORRECTION = 0
                    row[4] = NOCORRECTION
                    editDistAbove1 = 0
                    row[5] = editDistAbove1
                    editDistBelow3 = 0
                    row[6] = editDistBelow3
                    editDist_1andcaseChange = 1
                    row[7] = editDist_1andcaseChange = 1
                    row[8] = 0
                    row[9] = 0
                    CAPITALIZATION = 1
                    row[10] = CAPITALIZATION
                    row[11] = 0
#                    print 'edit Distance of first letter is 1 and its change of case',editDist_1andcaseChange    
#                    print 'CAPITALIZATION ERROR',CAPITALIZATION
                    writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
                else:
                    sameLength = 1
                    row[2] = sameLength
                    editDist_0 = 0
                    row[3] = editDist_0
                    NOCORRECTION = 0
                    row[4] = NOCORRECTION
                    editDistAbove1 = 0
                    row[5] = editDistAbove1
                    editDistBelow3 = 0
                    row[6] = editDistBelow3
                    editDist_1andcaseChange = 0
                    row[7] = editDist_1andcaseChange
                    row[8] = 0
                    row[9] = 0
 #                   print 'edit Distance AND CASE CHANGE is 0',editDist_1andcaseChange
                    row[10] =0
 #                   print 'CAPITALIZATION ERROR',CAPITALIZATION
                    TYPO = 1
                    row[11] = TYPO
#                    print "TYPO ",TYPO
                    writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
            
    else:
        sameLength = 0
        row[2] = sameLength
#        print "Length is different",sameLength
        editDist_0 = 0
        row[3] = editDist_0
#        print  oldText,"and",newText,"are not equal",row[3]
        NOCORRECTION = 0
        row[4] = NOCORRECTION

#        print  "NO CORRECTION",NOCORRECTION
        if editdist.distance(oldText,newText) >= 1 and editdist.distance(oldText,newText) < 3:
            row[5] = 1
            row[6] = 1
            row[7] = 0
            SPELLCHECK = 1
            row[8] = SPELLCHECK
            row[9] = 0
            row[10] = 0
            row[11] = 0
 #           print "SPELLCHECK ERROR",SPELLCHECK
            writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
        else:
            row[5] = 0
            row[6] = 0
            row[7] = 0
            row[8] = 0
            ADDITION = 1
            row[9] = ADDITION
            row[10] = 0
            row[11] = 0
#            print "ADDITION OF WORDS",ADDITION
            writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])

fin.close()
fout.close()
