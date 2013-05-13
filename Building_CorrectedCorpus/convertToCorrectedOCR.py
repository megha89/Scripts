import sys
import time
import os

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

logfile = "C:\Users\Megha\Desktop\SEM4\DDM\Course Project\WorkingDataset"
fileToReplace = "C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Newspapers\CorrectedOCRText"
count = 0
the_list = []
flag = False
root, subFolders, files  = os.walk(fileToReplace).next()
logroot,logsb, logfile = os.walk(logfile).next()
while count < 190:
    filePath = os.path.join(root, files[count])
    logpath = os.path.join(logroot,logfile[count])
    #fout = open(filePath, 'r+')
    lout = open(logpath, 'r')
    for lines in lout:
        line = lines
        line = line.lstrip()
        if line.startswith('<OldTextValue>') or line.startswith('<NewTextValue>'):
            if flag == True :
                flag = False
                continue
            if line.startswith('<OldTextValue>'):
                length = len(line)
                line = line[14:length-16]
                if len(line) == 0 :
                    flag = True
                    print "The line with oldtext and zero size"
                    continue
                else :
                    the_list.append(line)           
            else :
                length = len(line)
                line = line[14:length-16]
                the_list.append(line)
    #print the_list
    from itertools import izip
    i = iter(the_list)
    dic = dict(izip(i, i))
    #print dic
    fout = open(filePath, 'r+')
    text = fout.read()            
    CorrectedText = replace_all(text, dic)
    print CorrectedText
    fout.seek(0)
    fout.write(CorrectedText)
    print "Text Corrected for file %s" % filePath
    lout.close()
    fout.close()
    count = count + 1
