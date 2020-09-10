'''
Created on Sep 5, 2020

@author: artathon
'''
from Rriwayati import Rriwayati
from File import File
def main():
    ###############
    r = Rriwayati()
    #r.getFileList()
    corpusWordFrequency       = '/home/artathon/data/artathon/Rewaytik-20200905/Rewaytik/results/Corpus.frq'
    #riwayatiPath             = '/content/gdrive/My Drive/data/Rewaytik/TextFiles'
    riwayatiPath              = '/home/artathon/data/artathon/Rewaytik-20200905/Rewaytik/final' # '/content/gdrive/My Drive/data/Rewaytik/final'
    riwayatiPatht3            = '/content/gdrive/My Drive/data/t3'

    riwayatiWordList          = '/content/gdrive/My Drive/data/Rewaytik/results/rWrds3a.lst'
    riwayatiWordFrequency     = '/home/artathon/data/artathon/Rewaytik-20200905/Rewaytik/results/rWrds3a.frq'
    conceptsWords             = '/home/artathon/data/artathon/Rewaytik-20200905/Rewaytik/results/conceptsExpaned-88-20200622Clean.txt'
    novelConcepts             = '/home/artathon/data/artathon/Rewaytik-20200905/Rewaytik/results/novelConcepts.txt'
    outputPath                = '/home/artathon/data/artathon/Rewaytik-20200905/Rewaytik/results/novelConcepts/'
    riwayatiWordFrequencyAll  = '/content/gdrive/My Drive/data/Rewaytik/results/rWrdFreqAll.frq'
    f = File()
    # fl = f.listAllFiles(path, '.frq')
    # print(fl)
    
    #f.affexSqeNumberToFileList(riwayatiPath, '.txt', 4)
    #r.readArabicWordFrequency(corpusWordFrequency)
    #r.readValidArabicWordList('/content/gdrive/My Drive/resources/Corpus.frq')

    #r.commonConceptWord(riwayatiWordFrequency, corpusWordFrequency, conceptsWords, novelConcepts)

    ###r.generateNovelConcepts(riwayatiPath, '.txt', novelConcepts, outputPath)

    r.plotFileConceps();
    #wfAll = r.listAllWordFreq(riwayatiPath, '.txt', riwayatiWordList, riwayatiWordFrequency)
#     wfAll = r.fileWordFreqMatrix(riwayatiPath, '.txt', 
#                                  riwayatiWordFrequency, 
#                                  corpusWordFrequency, 
#                                  conceptsWords,
#                                  riwayatiWordFrequencyAll)

#     concepts88ExpandCleanFileName   = "/content/gdrive/My Drive/resources/conceptsExpaned-88-20200622Clean.txt"


if __name__ == "__main__": main()