
class Concepts:
    concepts = {}

    ########### ########### ########### ########### ########### ########### ########### 
    #
    #    __init__(self, conceptsFile):  reads the seed concepts from "conceptsFile" and
    #                                    store it in "concepts = {}" in-memory structure. 
    #      input file format:    cncptId  cncpEngName    color    RGB        Arabic    English
    #                            1        Love           red      255-0-0    حب        Love
    #                            1        Love           red      255-0-0    عشق       Love
    #                            4        Sorrow         Brown    153-51-51  الحزن     Sorrow
    #                            ..       ..             ....     ..         ..        ..
    #                            45       Illness        Yellow   0-255-255  مرض       Illness
    #
    #     "concepts = {}" format:
    #        An entry for each concept cluster.
    #
    #
    #         cncptId, [cncpEngName, color,    RGB],       [[Ar ,            En], [Ar ,   En] ..., [..]]
    #         1,       ["Love",      "Red",   "255-0-0"],  [["حب",       "love"], ["شغف", "passion"] ... [..]]
    #         4,       ["Sorrow",    "Brown", "153-51-51"], [["الحزن", "Sorrow"], ["دمع", "tear"],  .... []]
    #
    ########### ########### ########### ########### ########### ########### ########### 
    def __init__(self, conceptsFile):
        text = Text()
        cnpts = open(conceptsFile,'r').read().split('\n')
        for c in cnpts:
            #print(c)
            if len(c) < 5 or c[0] == '#':
              continue
            cp = c.split('\t')
            if len(cp) < 6:
                continue
            cp[4] = text.clean(cp[4]).strip()
            cp[5] = cp[5].strip()
            if cp[0] not in self.concepts:
                self.concepts[cp[0]] = [cp[1], [cp[2], cp[3]],    [cp[4], cp[5]] ]
            else:
                pct = self.concepts[cp[0]]
                nm  =  pct[0]     # concept name
                clr =  pct[1]     # color
                tkn =  pct[2]  +  [cp[4], cp[5]]
                self.concepts[cp[0]] = [nm, clr, tkn]
        #print(len(self.concepts))

                
    def writeFormated(self, conceptsOutFile):

        ofh = open(conceptsOutFile, "w")
        cnt = 0
        for cp in self.concepts:
            print(cp, self.concepts[cp])
            cnt += 1
            pct = self.concepts[cp]

            nm    = pct[0]
            clr   = pct[1]
            tkn   = pct[2]

            ofh.write(str(cp) + "\t" + nm + "\t" + str(clr) + "\t" + str(tkn) + "\n")
                      
                      
        ofh.close()
        print("concept count: ", cnt)

    ########### ########### ########### ########### ########### ########### ########### 
    #
    #   dump(self):  display all concepts for debugging
    #
    ########### ########### ########### ########### ########### ########### ########### 

    def dump(self):
        for c in self.concepts:
            print(c, self.concepts[c])


    ########### ########### ########### ########### ########### ########### ########### 
    #
    #   size(self):  return number of unique concepts in the concept list
    #
    ########### ########### ########### ########### ########### ########### ########### 

    def size(self):
        return(len(self.concepts))

    ########### ########### ########### ########### ########### ########### ########### 
    #
    #   getConceptTokens(self, tid):  returns list of Arabic tokens related to a given
    #                                 concept tid
    #
    ########### ########### ########### ########### ########### ########### ########### 

    def getConceptTokens(self, tid):

        c = self.concepts[str(tid)][2]
        ac = []
        for x in range(0, len(c)):
            if x%2 == 0:
                ac.append(c[x])
        return ac

    ########### ########### ########### ########### ########### ########### ########### 
    #
    #   getIds(self, tid):  returns list of concepts ids
    #
    ########### ########### ########### ########### ########### ########### ########### 
    def getIds(self):
        ids = []
        for c in self.concepts:
            ids.append(c)
        return ids

    ########### ########### ########### ########### ########### ########### ########### 
    #
    #   cleanExpaned:  clean list of expaned concept list (inecifn file) and sore 
    #                  cleaned copy in ecofn file.  Cleaning process involves 
    #                  removing duplicate and stopwords.
    #
    ########### ########### ########### ########### ########### ########### ########### 

    def cleanExpaned(self, ecifn, ecofn, stopwordsFile):

        text = Text()
        # read stopwords as list of tokens
        stopwords = text.readFileTextAsListOfTokens(stopwordsFile)
        ec = {}
        ecnpts = open(ecifn,'r').read().split('\n')
        for c in ecnpts:
            cp = c.split('\t')
            if len(cp) < 3:
                continue
            else:
                token = cp[0]
                cid   = cp[1]
                freq  = cp[2]
                if token not in ec:    # token as a key
                    ec[token] = [cid, freq]
                else:
                    xfreq = ec[token][1]
                    if freq > xfreq:
                      ec[token] = [ec[token][0], freq]
        ofh = open(ecofn, "w")
        for c in ec:
          if c not in stopwords:
            ofh.write(c + "\t" + ec[c][0] + "\n")
        ofh.close()

    ########### ########### ########### ########### ########### ########### ########### 
    #
    #   markNovel:  Read throug the text of a given novel and mark majore concepts
    #               associated with novel phrases.   expandedCleanConceptsFile is  
    #               used in this process and resules will be stored in markedNovelFile
    #               All found concelts will be attached as a header to the novel file.
    #               Each entry in the  list refers to a sigle concept.
    #               The follwing information are recoded:
    #               word id in the novel, associated concept id, its current density
    #
    ########### ########### ########### ########### ########### ########### ########### 

    def markNovel(self, novelFile, markedNovelFile, expandedCleanConceptsFile):
        text = Text()
        # read novel text as list of tokens
        novelTokens = text.readFileTextAsListOfTokens(novelFile)
        print("novelTokenz:", len(novelTokens))
        print(novelTokens[0:20])

        ec = {}
        cids = {}
        ecnpts = open(expandedCleanConceptsFile,'r').read().split('\n')
        for c in ecnpts:
            cp = c.split('\t')
            if len(cp) < 2:
                continue
            else:
                token = cp[0]
                cid   = cp[1]
                ec[token] = cid
                if cid not in cids:
                    cids[cid] = 0
        print("ec:", len(ec))
        conceptCount   = len(cids)
        print("conceptCountz: ", conceptCount)
        print(cids)
        tid            = 0
        cidCounter     = [0]*conceptCount
        cidIncCounter  = [0]*conceptCount

        novelConcepts  = []
        totalFoundConcepts = 0
        for nt in novelTokens:
          if nt in ec:
              # print("nt: ", nt)
              totalFoundConcepts += 1
              cid = int(ec[nt]) - 1
              # print("cid: ", cid)
              cidCounter[int(cid)] += 1
              novelConcepts.append([tid, cid])
              # print(tid, cid)
              # print(cidCounter)
          tid += 1
        precNovelMax = 0

        novelFinalConcepts  = []
        for nc in novelConcepts:
          tid = nc[0]
          cid = nc[1]
          cidIncCounter[cid]  += 1
          precConcept = cidIncCounter[cid] * 100 / cidCounter[cid]
          precNovel   = cidIncCounter[cid] * 100 / totalFoundConcepts
          if precNovel > precNovelMax:
            precNovelMax = precNovel
          oneConcept = [tid, cid, precConcept, precNovel]
          novelFinalConcepts.append(oneConcept)
        ofh = open(markedNovelFile, "w")
        for i in range(0, len(novelFinalConcepts)-1):
            novelFinalConcepts[i][3] = int(novelFinalConcepts[i][3]*100/precNovelMax)
            novelFinalConcepts[i][2] = int(novelFinalConcepts[i][2])
            
            ofh.write(str(novelFinalConcepts[i])+ "\n")
            print(novelFinalConcepts[i]) 

        for nt in novelTokens:
          ofh.write(nt + "\n")
        ofh.close()

    #  capture only token id and concept id
    def markNovelSlim(self, novelFile, markedNovelFile, expandedCleanConceptsFile):
        text = Text()
        # read novel text as list of tokens
        novelTokens = text.readFileTextAsListOfTokens(novelFile)
        print("novelTokenz:", len(novelTokens))
        print(novelTokens[0:20])

        ec = {}
        cids = {}
        ecnpts = open(expandedCleanConceptsFile,'r').read().split('\n')
        for c in ecnpts:
            cp = c.split('\t')
            if len(cp) < 2:
                continue
            else:
                token = cp[0]
                cid   = cp[1]
                ec[token] = cid
                if cid not in cids:
                    cids[cid] = 0
        print("cids: ", len(cids))
        print(cids)
        tid            = 0
        ofh = open(markedNovelFile, "w")

        for nt in novelTokens:
          if nt in ec:
              #cid = int(ec[nt]) - 1
              cid = int(ec[nt]) 
              tokenConcept = [tid, cid]
              ofh.write(nt + "  " + str(cid)+ "\n")
          else:
              ofh.write(nt+ "\n")
        ofh.close()

