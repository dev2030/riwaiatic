########### ########### ########### ########### ########### ########### ########
#
#   File Class
#
########### ########### ########### ########### ########### ########### ########
import os
import sys
from Text import Text

class File:
    def __init__(self):
        print("hello File")
    ########### ########### ########### ########### ########### ########### ########
    #  
    #  constructFileName:  genrate a file name by affixing an file extention to the
    #                      fle name
    ########### ########### ########### ########### ########### ########### ########
    def constructFileName(self, fn, sfx):
       
        p = fn.rfind('/')
        nfn =  fn[:p+1] + str(sfx) + '-' + fn[p+1:]
        return nfn

    ########### ########### ########### ########### ########### ########### ########
    #  
    #  constructFileName:  genrate a file name by affixing an file extention to the
    #                      fle name
    ########### ########### ########### ########### ########### ########### ########
    def affexSqeNumberToFileList(self, path, ext, width):
       
        allFiles = self.listAllFiles(path, ext)
        cnt = 1
        for f in allFiles:
          num = format(cnt, '04d')
          cnt += 1
          nfn = self.constructFileName(f, num)
          print(f)
          print(nfn)
          os.rename(f,nfn)
        return 

    ########### ########### ########### ########### ########### ########### ########
    #  
    #  listAllFiles:  Recursivly ists all file with given ext in a directory
    #                    
    ########### ########### ########### ########### ########### ########### ########
    def listAllFiles(self, path, ext):    
        allfiles = []
        for root, subdirs, files in os.walk(path):
       
            for filename in files:
                file_path = os.path.join(root, filename)
                if file_path.endswith(ext):
                    if '.git' not in file_path:
                        allfiles.append(file_path)
    
        return allfiles

    def getFileNumber(self, fn):
        lastSlash = fn.rfind('/')+1
        fnum = fn[lastSlash:lastSlash+4]
        return(fnum)

    ########### ########### ########### ########### ########### ########### ########
    #  
    #  readWordFrequency:  in a dict
    #                    
    ########### ########### ########### ########### ########### ########### ########
    def readWordFrequency(self, fn, minFreq):   # in a dict
        wfDict = {}
        cnt = 0
        fh = open(fn, 'r')
        for line in fh:
            cnt += 1
            if(len(line) < 2):
                continue
            wf = line.split('\t')
            if(len(wf) < 2):
                continue
            if int(wf[1]) < minFreq:
                continue
            wfDict[wf[0]] = wf[1]
#             if cnt > 20:
#                 break
        fh.close()
        return wfDict

    ########### ########### ########### ########### ########### ########### ########
    #  
    #  fileText2WordFrequency:  in a dict
    #                    
    ########### ########### ########### ########### ########### ########### ########
    def fileText2WordFrequency(self, fn):   # in a dict
        t = Text()
        wfDict = {}
        cnt = 0
        fh = open(fn, 'r')
        for l in fh:
          cnt += 1
          # print(l)
          line = t.clean(l)
          # print(line)
          if(len(line) < 2):
              continue
          words = line.split()
          for w in words:
              if w in wfDict:
                 wfDict[w] = wfDict[w] + 1
              else:
                 wfDict[w] = 1

        fh.close()
        return wfDict

    ########### ########### ########### ########### ########### ########### ########
    #  
    #  readFileText:  in one var
    #                    
    ########### ########### ########### ########### ########### ########### ########
    def readFileText(self, fn, size):   # in a list
        fileText = []
        fh = open(fn, 'r')
        for line in fh:
            size -= 1
            if size == 0:
                break
            if(len(line)) < 2:
                continue
            fileText.append(line.strip())
        fh.close()
        return fileText


      # in a list of list, each para in a list of token
    def readFileTextAsListOfLines(self, fn, maxLines):  

        fileLines = []
        fh = open(fn, 'r')
        text = Text()
        for line in fh:
            if(len(line)) < 2:
                continue
            if line[0:1] == '#':
                print(line)
                continue
            fileLines.extend([text.tokenize(line)])
        fh.close()
        return fileLines

        # in a list of list, each para in a list of token
    def readFileTextAsListOfTokens(self, fn):  

        text = Text()

        fileTokens = []
        fh = open(fn, 'r')
        for line in fh:
            if(len(line)) < 2:
                continue
            fileTokens.extend(text.tokenize(line))
        fh.close()
        return fileTokens

    # in a list of list, each para in a list of token
    def readFileTextAsListOfLists(self, fn, maxm):  

        fileTokens = []
        tknsz = 0
        fh = open(fn, 'r')
        for line in fh:
            maxm -= 1
            if maxm == 0:
                break
            if(len(line)) < 2:
                continue
            tkns = self.tokenize(line)
            tknsz += len(tkns)
            fileTokens.append(tkns)
        fh.close()
        print("tknsz: ", tknsz)
        return fileTokens

    def readCorpusAsListOfLines(self, path, ext, maxLines):   # in a list of list, each para in a list of token
    
        fl = self.listAllFiles(path, ext)
        fileText = []
        #print("path: ", path, "flz: ", len(fl))
      
        cnt = 0
        for fn in fl:
            #print(fn)
            ftxt = self.readFileTextAsListOfLines(fn, maxLines)
            for l in ftxt:
                fileText.append(l)
                # cnt += 1
                # if cnt > max:
                #     break
        print("cz: ", len(fileText))
        return fileText

    def readCorpusAsListOfLists(self, path, ext, maxLines):   # in a list of list, each para in a list of token
    
        fl = self.listAllFiles(path, ext)
        fileText = []
        print("path: ", path, "flz: ", len(fl))
      
        cnt = 0
        for fn in fl:
            print(fn)
            ftxt = self.readFileTextAsListOfLists(fn, maxLines)
            for l in ftxt:
                fileText.append(l)
                # cnt += 1
                # if cnt > max:
                #     break
        print("cz: ", len(fileText))
        return fileText
    
    def sortDict(self, infn, outfn):  

        kvs   = {}
        tknsz  = 0
        cnt    = 0
        fh = open(infn, 'r')
        for line in fh:
            kv = line.split()
            if len(kv) < 2:
                continue

            if kv[1] == '1':

                continue
            cnt += 1
            if kv[0] not in kvs:
                kvs[kv[0]] = int(kv[1])

        fh.close()
        kvsSorted = {k: v for k, v in sorted(kvs.items(), key=lambda x: x[1], reverse=True)}
        print(type(kvsSorted))
        outfh  = open(outfn, "w")
        for k in kvsSorted:
            outfh.write(k + '\t' + str(kvsSorted[k]) + "\n")
        outfh.close()
        return kvs
    
    
    def ngram(self, infn, outfn, n):  

        kvs   = {}
        tknsz  = 0
        cnt    = 0
        fh = open(infn, 'r')
        for line in fh:
            kv = line.split()
            if len(kv) < 2:
                continue
            if kv[1] == '1':
                continue
            cnt += 1
            if kv[0] not in kvs:
                kvs[kv[0]] = int(kv[1])

        fh.close()
        #         kvsSorted = {k: v for k, v in sorted(kvs.items(), key=lambda x: x[1], reverse=True)}
        ngramx = {}

        for k in kvs:
            # print("k:", k)
            ek = ' ' + k + ' '
            for i in range(0, (len(ek))):
                ss = ek[i: i+n]
                if len(ss) < n:
                    continue
                #print("ss: ", ss, kvs[k])
                if ss in ngramx:
                    v = ngramx[ss]
                    v = v + kvs[k]
                    ngramx[ss] = v
                else:
                    ngramx[ss] = kvs[k]
                
             #print(ngramx)
        
        ngSorted = {k: v for k, v in sorted(ngramx.items(), key=lambda x: x[1], reverse=True)}

        outfh  = open(outfn, "w")
        for k in ngSorted:
            outfh.write(k + '\t' + str(ngSorted[k]) + "\n")
        outfh.close()
