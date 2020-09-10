'''
Created on Sep 5, 2020

@author: artathon
'''
from File import File
import numpy as np 
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt 
 
 
class Rriwayati:
    
    validArabicWordList = []
    arabicWordFrequency = {}

    path = "/content/gdrive/My Drive/data/Rewaytik/txt"

    def __init__(self):
        self.size       = 0
        print("Hello Riwayati")

    #readWordFrequency

    def readArabicWordFrequency(self, fn):
        f = File()
        arabicWordFrequency = f.readWordFrequency(fn)
        print(arabicWordFrequency)


    def getFileList(self):
        fl = f.listAllFiles(self.path, '.txt')
        for fn in fl:
            print(fn)

    def readValidArabicWordList(self, fn):
        with open(fn) as f:
            self.validArabicWordList = f.read().splitlines()
        print('validArabicWordListz: ', len(validArabicWordList))

    def fasih(self, fileName):
        print('Fasih')

    def listAllWordFreq(self, path, ext, riwayatiWordList, riwayatiWordFrequency):
          allWords = {}
          f = File()
    
          fl = f.listAllFiles(path, ext)
          cnt = 1
          for fn in fl:
            print(cnt, fn)
            cnt += 1
            wf = f.fileText2WordFrequency(fn)
            for w in wf:
              if w in allWords:
                  allWords[w] = allWords[w] + wf[w]
              else:
                  allWords[w] = wf[w]
    
          #allWordsSorted = {k: v for k, v in sorted(allWords.items(), key=lambda x: x[1], reverse=True)}
          allWordsSorted = {k: v for k, v in sorted(allWords.items(), key=lambda x: x[1], reverse=False)}
    
          ofh = open(riwayatiWordList, "w")
          for w in allWordsSorted:
              ofh.write(w + "\n") 
          ofh.close()
          
          ofh = open(riwayatiWordFrequency, "w")
          for w in allWordsSorted:
              ofh.write(w + "\t" + str(allWordsSorted[w]) + "\n") 
          ofh.close()

          return allWords

    def commonConceptWord(self, riwayatiWordFrequency, corpusWordFrequency, conceptsWords, novelConcepts):
        f = File()

        allCommonWords = {}
        allNovelWords  = f.readWordFrequency(riwayatiWordFrequency, 1)
        allCorpusWords = f.readWordFrequency(corpusWordFrequency, 1)
        concepts       = f.readWordFrequency(conceptsWords, 1)        
        
        for v in allNovelWords:
            if v in allCorpusWords:
                if v in concepts:
                    allCommonWords[v] = (allNovelWords[v], allCorpusWords[v], concepts[v])
                    #print(v, allNovelWords[v], allCorpusWords[v], concepts[v])
        #array = np.arange(numberOfNoverls**NumberOfWOrds).reshape(numberOfNoverls,NumberOfWOrds)
        
        print('allNovelWords: ', len(allNovelWords))
        print('allCorpusWords:  ', len(concepts))
        print('concepts: ', len(concepts))
        print('allCommonWords: ', len(allCommonWords))
        
        ofh = open(novelConcepts, "w")
 
        for w in allCommonWords:
            ofh.write(w + '\t' + allNovelWords[w].strip() + '\t' + allCorpusWords[w].strip() + '\t' + concepts[w].strip()+ "\n")
            #print(w + '\t' + allNovelWords[w].strip() + '\t' + allCorpusWords[w].strip() + '\t' + concepts[w].strip()+ "\n")
                         
        ofh.close()
        allNovelWords.clear()
        allCorpusWords.clear()
        concepts.clear()
        return len(allCommonWords)

    def readCommonConceptWord(self, novelConcepts):
        
        allCommonWords = {}
        ofh = open(novelConcepts, "r")
        for line in ofh:
            tkns = line.split()
            if len(tkns) < 4:
                continue
            
            allCommonWords[tkns[0]] = (tkns[1], tkns[2], tkns[3])
                
        return(allCommonWords)

    def plotFileConceps(self):

        data = [23, 45, 56, 78, 213]
        plt.bar(["1",2,3,4,5], data)
        plt.show()
        
        

    def generateNovelConcepts(self, path, ext, novelConcepts, outputPath):
        f = File()

        allCommonWords = self.readCommonConceptWord(novelConcepts)
        print(len(allCommonWords))
        
        fl = f.listAllFiles(path, ext)
        cnt = 1
        for fn in fl:
            print(cnt, fn)
            cnt += 1
            fnum = f.getFileNumber(fn)
            #wf = f.fileText2WordFrequency(fn)
            wf = f.readFileTextAsListOfTokens(fn)
            print('fileID:' , fnum)
            outfh  = open(outputPath+ fnum+'.cpt', "w")
            print(len(wf))
            print(wf[0:5])
            skepWords = 0
            wcnt = 0
            for w in wf:
                if w in allCommonWords:
                    print(w, skepWords, allCommonWords[w][2])
                    outfh.write(w + '\t' + str(skepWords) + '\t' + str(allCommonWords[w][2]) + "\n")
                    skepWords = 0
                    wcnt += 1
#                     if wcnt > 10:
#                         break
                else:
                    skepWords += 1  #print(w)
#             if cnt > 3: 
#                 break
            
            outfh.close()

