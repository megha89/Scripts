# -*- coding: utf-8 -*-
# Labels are NOCORRECTION - 0, SPELLCHECK - 1, ADDITION - 2, CAPITALIZATION - 3, TYPO - 4, PUNCTUATION - 5
import os
import sys
import csv
import time
import editdist
import string
import difflib

'''check if char is punctuation char'''
def is_punct_char(char):
    if char in string.punctuation:
        #print 'THe character is a punctuation:',char
        return 1
    else:
        #print'String not Punctuation:',char
        return 0

csv_file = "/Users/meghagupta/Documents/Github/Scripts/Analysis/errorClassificationNew.csv"
csv_out = "/Users/meghagupta/Documents/Github/Scripts/Analysis/prepFinal.csv"

fin = open(csv_file, 'rb')
reader = csv.reader(fin)
fout = open(csv_out,'wb')
writer = csv.writer(fout)
writer.writerow(['oldText','newText','sameLength','editDist_0','editDistAbove1','editDistBelow3','editDist_1andcaseChange','punct_diff','ERROR_TYPE'])
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
            row[3] = 1
            row[4] = 0
            #print  "NOT CORRECTION",NOCORRECTION
            row[5]=0
            row[6]=0
            row[7] = 0
            ERRORTYPE = 0
            row[8]= ERRORTYPE
            
    
            writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
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
                    for char1 in newText:
                        for char2 in oldText:
                            if char1 != char2:
                                if is_punct_char(char1) or is_punct_char(char2):
                                #print 'Punctuation',char1
                                    flag =1
                                    exit
                                else:
                                    #print 'No punctuation',char1
                                    flag = 0
                            else:
                                flag = 0
    
                    if flag == 1:
                        row[2] = 1
                        row[3] = 0
                        row[4] = 1
                        row[5] = 1
                        row[6] = 0
                        row[7] = 1
                        ERRORTYPE = 5 #Punctuation error
                        row[8] = ERRORTYPE

                        writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])

                    else: 
                        row[2] = 1
                        row[3] = 0
                        row[4] = 1
                        row[5] = 1
                        row[6] = 0
                        row[7] = 0
                        ERRORTYPE = 1   #Spellcheck
                        row[8] = ERRORTYPE
         
                        writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])

                else:
                    for char1 in newText:
                        for char2 in oldText:
                            if char1 != char2:
                                if is_punct_char(char1) or is_punct_char(char2):
                                #print 'Punctuation',char1
                                    flag =1
                                    exit
                                else:
                                    #print 'No punctuation',char1
                                    flag = 0
                            else:
                                flag = 0
    
                    if flag == 1:
                        row[2] = 1
                        row[3] = 0
                        row[4] = 1
                        row[5] = 0
                        row[6] = 0
                        row[7] = 1
                        ERRORTYPE = 5 #Punctuation error
                        row[8] = ERRORTYPE

                        writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
                    else:                       
                        row[2] = 1
                        row[3] = 0
                        row[4] = 1
                        row[5] = 0
                        row[6] = 0
                        row[7] = 0
                        ERRORTYPE = 2
                        row[8] = ERRORTYPE   #Addition of new word
                        writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])

            else:
  
                if editdist.distance(oldText[0],newText[0]) == 1 and (oldText[0].upper() == newText[0]or oldText[0].lower() == newText[0]):
                    row[2] = 1
                    row[3] = 0
                    row[4] = 0
                    row[5] = 0
                    row[6] = 1
                    row[7] = 0
                    ERRORTYPE = 3     #Capitalization Error
                    row[8] = ERRORTYPE
                    writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
                    
                else:
                    for char1 in newText:
                        for char2 in oldText:
                            if char1 != char2:
                                if is_punct_char(char1) or is_punct_char(char2):
                                #print 'Punctuation',char1
                                    flag =1
                                    exit
                                else:
                                    #print 'No punctuation',char1
                                    flag = 0
                            else:
                                flag = 0
    
                    if flag == 1:
                        row[2] = 1
                        row[3] = 0
                        row[4] = 0
                        row[5] = 0
                        row[6] = 1
                        row[7] = 1
                        ERRORTYPE = 5 #Punctuation error
                        row[8] = ERRORTYPE
                        writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
                    else:
                        row[2] = 1
                        row[3] = 0
                        row[4] = 0
                        row[5] = 0
                        row[6] = 0
                        row[7] = 0
                        ERRORTYPE = 4   #Typo 
                        row[8] = ERRORTYPE                
                        writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
            
    else:
        row[2] = 0
        row[3] = 0

        if editdist.distance(oldText,newText) >= 1 and editdist.distance(oldText,newText) < 3:      #Check if difference between 1 amd 3
            for char1 in newText:
                for char2 in oldText:
                    if char1 != char2:
                        if is_punct_char(char1) or is_punct_char(char2):
                            #print 'Punctuation',char1
                            flag =1
                            exit
                        else:
                            #print 'No punctuation',char1
                            flag = 0
                    else:
                        flag = 0

            if flag == 1:
 #               print 'Punctuation difference'
                row[4] = 1
                row[5] = 1
                row[6] = 0
                ERRORTYPE = 5 #Punctuation error
                row[7] = 1
                row[8] = ERRORTYPE
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
            else:
#                print 'No punctuation difference'
            
                row[4] = 1
                row[5] = 1
                row[6] = 0
                row[7] = 0
                ERRORTYPE = 1
                row[8] = ERRORTYPE  #Spellcheck
    
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
        else:
            for char1 in newText:
                for char2 in oldText:
                    if char1 != char2:
                        if is_punct_char(char1) or is_punct_char(char2):
                            #print 'Punctuation',char1
                            flag =1
                            exit
                        else:
                            #print 'No punctuation',char1
                            flag = 0
                    else:
                        flag = 0

            if flag == 1:
#                print 'Punctuation difference'
                row[4] = 0
                row[5] = 0
                row[6] = 0
                row[7] = 1
                ERRORTYPE = 5 #Punctuation error
                row[8] = ERRORTYPE
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
            else:
#                print 'No punctuation difference'
                row[4] = 0
                row[5] = 0
                row[6] = 0
                row[7] = 0
                ERRORTYPE = 2   #Addition of new word
                row[8] = ERRORTYPE
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])

fin.close()
fout.close()
