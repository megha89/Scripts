import lucene
import os, re, sys
from subprocess import *
from lucene import IndexWriter, StandardAnalyzer, Document, Field
from lucene import SimpleFSDirectory, File, initVM, Version



def indexDirectory(dir):

    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            indexFile(dir, name)

def indexFile(dir,filename):

    path = os.path.join(dir, filename)
    file = open(path)
    #print "  File: ", filename
    doc = Document()
    doc.add(lucene.Field(FIELD_NAME, filename, lucene.Field.Store.YES, lucene.Field.Index.NOT_ANALYZED))
    doc.add(lucene.Field(FIELD_PATH, path, lucene.Field.Store.YES, lucene.Field.Index.NOT_ANALYZED))
    contents = file.read()
    if len(contents) > 0:
        doc.add(lucene.Field(FIELD_CONTENTS, contents, lucene.Field.Store.YES, lucene.Field.Index.ANALYZED))
        #print "Document Ready"
    else:
        print "warning: no content in %s" % filename

    writer.addDocument(doc)
   

if __name__ == '__main__':
    INDEX_DIR = "C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Newspapers\Test"
    manpath = "C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Newspapers\RawOCRText"
    FIELD_NAME = "name"
    FIELD_PATH = "path"
    FIELD_CONTENTS = "contents"
    
# Initialize lucene and JVM
lucene.initVM()
analyzer = lucene.StandardAnalyzer(lucene.Version.LUCENE_CURRENT)
store = lucene.SimpleFSDirectory(lucene.File(INDEX_DIR))
writer = lucene.IndexWriter(store, analyzer, True, lucene.IndexWriter.MaxFieldLength.LIMITED)

indexDirectory(manpath)
writer.optimize()
writer.close()

