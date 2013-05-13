#!/usr/bin/env python
from lucene import \
    QueryParser, IndexSearcher, StandardAnalyzer, SimpleFSDirectory, File, \
    VERSION, initVM, Version

queryFile = 'C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Raw+CorrectedCorpus\QuerySet\query.txt'
fread = open(queryFile, 'r')
newFile = 'C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Raw+CorrectedCorpus\SearchResults\CorrectedSearchResults.txt'
fwrite = open(newFile, 'w+')
"""
This script is loosely based on the Lucene (java implementation) demo class 
org.apache.lucene.demo.SearchFiles.  It will prompt for a search query, then it
will search the Lucene index in the current directory called 'index' for the
search query entered against the 'contents' field.  It will then display the
'path' and 'name' fields for each of the hits it finds in the index.  Note that
search.close() is currently commented out because it causes a stack overflow in
some cases.
"""
def run(searcher, analyzer):
    i = 0
    while i < 190:
        command = fread.readline()
        #command = raw_input("Query:")
        if command == '':
            return

        print "Searching for:", command
        fwrite.write("\n")
        fwrite.write("Searching for:"+command+"\n")
        query = QueryParser(Version.LUCENE_CURRENT, "contents",
                            analyzer).parse(command)
        scoreDocs = searcher.search(query, 10).scoreDocs
        score = len(scoreDocs)
        print "%s total matching documents." % score
        fwrite.write(str(score))
        fwrite.write(" matching Documents \n")

        for scoreDoc in scoreDocs:
            doc = searcher.doc(scoreDoc.doc)
            #print 'path:', doc.get("path"), 'name:', doc.get("name")
            print 'name:', doc.get("name")
            fwrite.write('name:'+ doc.get('name')+"\n")
            #fwrite.close()
        i = i + 1


if __name__ == '__main__':
    STORE_DIR = "C:\Users\Megha\Desktop\SEM4\DDM\Course Project\Raw+CorrectedCorpus\CorrectedOCRText_INDEX"
    initVM()
    #print 'lucene', VERSION
    directory = SimpleFSDirectory(File(STORE_DIR))
    searcher = IndexSearcher(directory, True)
    analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)
    run(searcher, analyzer)
    searcher.close()
    fwrite.close()
