'''
Created on Sep 5, 2020

@author: artathon
'''

########### ########### ########### ########### ########### ########### ########
#  
#  Text:  is a class to handle text processing, including cleaining, tokenization, 
#         reading in list, list of list, dect and so on in preperation to list all 
#         major valid concepts in the language.
#                    
########### ########### ########### ########### ########### ########### ########

class Text:

  size = 0
  def __init__(self):
    self.size       = 0
  


  def clean(self, t):
      w = ""
      vowels = [ 
          u'\u0640', u'\u064B', u'\u064C', u'\u064D', u'\u064E', u'\u064F', u'\u0650', u'\u0651', u'\u0652', u'\u0653']
      validChar = [ 
          u"ا",  u"أ",  u"إ",  u"آ",  u"ء",  u"ئ",  u"ؤ",  u"ب",  \
          u"ت",  u"ة",  u"ث",  u"ج",  u"ح",  u"خ",  u"د",  u"ذ",  \
          u"ر",  u"ز",  u"س",  u"ش",  u"ص",  u"ض",  u"ط",  u"ظ",  \
          u"ع",  u"غ",  u"ف",  u"ق",  u"ك",  u"ل",  u"م",  u"ن",  \
          u"ه",  u"و",  u"ى",  u"ي",   " ", "\n"]
      
      for char in t:
          if char in validChar:
              w = w + char
          else:
              if char in vowels:
                  #print("char in vowels")
                  w = w + ""
              else:
                  w = w + " "
      return w


  def tokenize(self, line):
      tokens = self.clean(line).split()
      #print("tokenz", len(tokens))
      return (tokens)

  # in a list of list, each para in a list of token
  def readFileTextAsListOfTokens(self, fn):  
    fileTokens = []
    fh = open(fn, 'r')
    for line in fh:
        if(len(line)) < 2:
            continue
        fileTokens.extend(self.tokenize(line))
    fh.close()
    return fileTokens


  # in a list of list, each para in a list of token
  def readFileTextAsListOfLists(self, fn, max):  
    fileTokens = []
    tknsz = 0
    fh = open(fn, 'r')
    for line in fh:
        max -= 1
        if max == 0:
            break
        if(len(line)) < 2:
            continue
        tkns = self.tokenize(line)
        tknsz += len(tkns)
        fileTokens.append(tkns)
    fh.close()
    print("tknsz: ", tknsz)
    return fileTokens

  def readCorpusAsListOfLists(self, path, ext, max):   # in a list of list, each para in a list of token
    fl = listAllFiles(path, ext)
    fileText = []
    print("path: ", path, "flz: ", len(fl))
  
    cnt = 0
    for fn in fl:
        print(fn)
        ftxt = self.readFileTextAsListOfLists(fn, max)
        for l in ftxt:
            fileText.append(l)
            # cnt += 1
            # if cnt > max:
            #     break
    print("cz: ", len(fileText))
    return fileText