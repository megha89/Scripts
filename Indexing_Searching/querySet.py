import random
import os
import re
i = 0
words = []
CorrectedFiles = 'C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Raw+CorrectedCorpus\CorrectedOCRText'
newFile = r'C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Raw+CorrectedCorpus\QuerySet\query1.txt'
fout = open(newFile, 'w+')
for root, subFolder, files in os.walk(CorrectedFiles):
    for filename in files:
        filePath = os.path.join(root, filename)
        with open( filePath, 'r' ) as fin:
            words = [line.split() for line in fin]
            while i < 190 :
                x = random.choice(words)
                if len(x) > 1 :
                    y = x.pop(random.randint(0,len(x)-1))
                    y = re.sub('^[^a-zA-z]*|[^a-zA-Z]*$','',y)
                    if (len(y) > 3):
                        print y
                        fout.write((y))
                        fout.write("\n")
                        i = i + 1
                        break
                    else :
                        continue
                else :
                    continue             
fout.close()
