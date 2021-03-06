class Generator():

    def __init__(self, self.word):
        self.nouns = {}
        self.nounsPlural = {}
        self.pnouns = {}
        self.pnounsPlural = {}
        self.verbs = {}
        self.verbsPast = {}
        self.verbs3rdSingularPresent = {}
        self.verbsPastParticiples = {}
        self.verbsNon3rdSingularPresent = {}
        self.coordConjunctions ={}
        self.cardinalNum ={}
        self.determiners ={}
        self.foreignWords ={}
        self.prepositions ={}
        self.adjectives ={}
        self.adjComparatives ={}
        self.adjSuperlatives ={}
        self.predeterminers ={}
        self.possessiveEnds ={}
        self.possessivePronouns ={}
        self.personalPronouns ={}
        self.adverbs ={}
        self.adverbComparatives ={}
        self.adverbSuperlatives ={}
        self.interjections ={}

        self.listContainer = {}

        #List containing all dicitonaries
        self.posLists = [self.nouns,self.nounsPlural,self.pnouns,self.pnounsPlural,self.verbs,self.verbsPast, self.verbs3rdSingularPresent,self.verbsNon3rdSingularPresent,self.coordConjunctions,self.cardinalNum,self.determiners,self.foreignWords,self.prepositions,self.adjectives,self.adjComparatives,self.adjSuperlatives,self.predeterminers,self.possessiveEnds,self.possessivePronouns,self.personalPronouns,self.adverbs,self.adverbComparatives,self.adverbSuperlatives,self.interjections]

    #Returns list of words sorted by score, largest score at 0th index, smallest  at nth
    def sort(self):

        for dictionary in self.posLists:
            sorted_list = sorted(dictionary)
            self.listContainer.append(sorted_list)                                

        print(len(self.listContainer))

    #converts comment into TextBlob object, returns tags 
    def getSentencePOS(self,comment):
        sentencePOS = TextBlob(comment)
        return sentencePOS.tags #list of 2 element tuples [0] is word, [1] is pos

    def duplicate(self,wordStr,wordList):
        for word in wordList:
            if wordStr == word.word:
                word.addScore() #adds 1 to word score in list
                return True
        return False

    #sorts parts of speech into lists
    def sortPOS(self,posTags):
        for wordtag in posTags:
            word = Word(wordtag[0],wordtag[1])
            #if pos is noun based add to nouns list CANCER BELOW BEWARE
            if(word.pos=="NN" or word.pos=="NNS"): #part of speech check
                if(not(self.duplicate(word.word,self.nouns))): #check if word is already in list
                    self.nouns.append(word) #append to that list
            elif(word.pos=="NNS"):
                if(not(self.duplicate(word.word,self.nounsPlural))):
                    self.adjSuperlatives.append(word)

            elif(word.pos=="NNP"):
                if(not(self.duplicate(word.word,self.pnouns))):
                    self.pnouns.append(word)
            elif(word.pos=="NNPS"):
                if(not(self.duplicate(word.word,self.pnounsPlural))):
                    self.pnounsPlural.append(word)

            elif(word.pos=="VB" or word.pos=="VBG"):
                if(not(self.duplicate(word.word,self.verbs))):
                    self.verbs.append(word)

            elif(word.pos=="VBD"):
                if(not(self.duplicate(word.word,self.verbsPast))):
                    self.verbsPast.append(word)

            elif(word.pos=="VBN"):
                if(not(self.duplicate(word.word,self.verbsPastParticiples))):
                    self.verbsPastParticiples.append(word)

            elif(word.pos=="VBP"):
                if(not(self.duplicate(word.word,self.verbsNon3rdSingularPresent))):
                    self.verbsNon3rdSingularPresent.append(word)

            elif(word.pos=="VBZ"):
                if(not(self.duplicate(word.word,self.verbs3rdSingularPresent))):
                    self.verbs3rdSingularPresent.append(word)

            elif(word.pos=="CC"):
                if(not(self.duplicate(word.word,self.coordConjunctions))):
                    self.coordConjunctions.append(word)

            elif(word.pos=="CD"):
                if(not(self.duplicate(word.word,self.cardinalNum))):
                    self.cardinalNum.append(word)

            elif(word.pos=="DT"):
                if(not(self.duplicate(word.word,self.determiners))):
                    self.determiners.append(word)

            elif(word.pos=="FW"):
                if(not(self.duplicate(word.word,self.foreignWords))):
                    self.foreignWords.append(word)

            elif(word.pos=="IN"):
                if(not(self.duplicate(word.word,self.prepositions))):
                    self.prepositions.append(word)

            elif(word.pos=="JJ"):
                if(not(self.duplicate(word.word,self.adjectives))):
                    self.adjectives.append(word)

            elif(word.pos=="JJR"):
                if(not(self.duplicate(word.word,self.adjComparatives))):
                    self.adjComparatives.append(word)

            elif(word.pos=="JJS"):
                if(not(self.duplicate(word.word,self.adjSuperlatives))):
                    self.adjSuperlatives.append(word)

            elif(word.pos=="PDT"):
                if(not(self.duplicate(word.word,self.predeterminers))):
                    self.predeterminers.append(word)

            elif(word.pos=="POS"):
                if(not(self.duplicate(word.word,self.possessiveEnds))):
                    self.possessiveEnds.append(word)

            elif(word.pos=="PRP"):
                if(not(self.duplicate(word.word,self.personalPronouns))):
                    self.personalPronouns.append(word)

            elif(word.pos=="PRP$"):
                if(not(self.duplicate(word.word,self.possessivePronouns))):
                    self.possessivePronouns.append(word)

            elif(word.pos=="RB"):
                if(not(self.duplicate(word.word,self.adverbs))):
                    self.adverbs.append(word)

            elif(word.pos=="RBR"):
                if(not(self.duplicate(word.word,self.adverbComparatives))):
                    self.adverbComparatives.append(word)

            elif(word.pos=="RBS"):
                if(not(self.duplicate(word.word,self.adverbSuperlatives))):
                    self.adverbSuperlatives.append(word)

            elif(word.pos=="UH"):
                if(not(self.duplicate(word.word,self.interjections))):
                    self.interjections.append(word)

