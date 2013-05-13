import os
import sys
import re

newfile = r'C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Raw+CorrectedCorpus\QuerySet\query.txt'
fread = open(newfile)
writeFile = r'C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Raw+CorrectedCorpus\QuerySet\query1.txt'
fwrite = open(writeFile, 'w+')
for line in fread:
    line = line.lstrip()
    line = line.rstrip()
    line = re.sub('^[^a-zA-z]*|[^a-zA-Z]*$','',line)
    print line
    fwrite.write(line)
    fwrite.write("\n")
fread.close()
fwrite.close()
    
