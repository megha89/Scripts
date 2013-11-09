import os
import sys
import csv
import time
import editdist
import difflib
import string


'''check if char is punctuation char'''
def is_punct_char(char):
    if char in string.punctuation:
        #print 'THe character is a punctuation:',char
        return 1
    else:
        #print'String not Punctuation:',char
        return 0

old = 'abc}'
new = 'abcQ'


print difflib.SequenceMatcher(None,old,new).ratio()

#print 'Differ method of difflib'
#d = difflib.Differ()
#diff = d.compare(old, new)

#print '\n'.join(diff)

print 'THe punctuations are :', string.punctuation

flag = 0

for char1 in new:
    for char2 in old:
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
    print 'Punctuation difference'
else:
    print 'No punctuation difference'



            
