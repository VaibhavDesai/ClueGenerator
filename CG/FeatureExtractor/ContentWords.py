from nltk import word_tokenize
import nltk

'''
    >>>nltk.help.upenn_tagset()
    
    JJ: adjective or numeral, ordinal
    JJR: adjective, comparative
    JJS: adjective, superlative

    NN: noun, common, singular or mass
    NNP: noun, proper, singular
    NNPS: noun, proper, plural
    NNS: noun, common, plural

    RB: adverb
    RBR: adverb, comparative
    RBS: adverb, superlative
    WRB: Wh-adverb

    VB: verb, base form
    VBD: verb, past tense
    VBG: verb, present participle or gerund
    VBN: verb, past participle
    VBP: verb, present tense, not 3rd person singular
    VBZ: verb, present tense, 3rd person singular
'''

class ContentWords:

    pos_list_tuple = {}

    def __init__(self, inp):
        text = word_tokenize(inp)
        self.pos_list_tuple = nltk.pos_tag(text)

    def getContentWordsCount(self):
        contentLambdaFunc = lambda a: a[1] in ['NN', 'NNP', 'NNPS', 'NNS',  'VB', 'VBD', 'VBG', 'VBN','VBP', 'VBZ', 'JJ','JJR','JJS', 'RB', 'RBR', 'RBS']
        return len(filter(contentLambdaFunc, self.pos_list_tuple))

    def getVerbsCount(self):
        verbsLambdaFunc = lambda a: a[1] in ['VB', 'VBD', 'VBG', 'VBN','VBP', 'VBZ']
        return len(filter(verbsLambdaFunc), self.pos_list_tuple)

    def getNounsCount(self):
        nounsLambdaFunc = lambda a: a[1] in ['NN','NNP', 'NNPS', 'NNS']
        return len(filter(nounsLambdaFunc, self.pos_list_tuple))

    def getAdjectivesCount(self):
        adjectivesLambdaFunc = lambda a: a[1] in ['JJ','JJR','JJS']
        return len(filter(adjectivesLambdaFunc, self.pos_list_tuple))

    def getAdverbsCount(self):
        adverbsLambdaFunc = lambda a: a[1] in ['RB', 'RBR', 'RBS','WRB']
        return len(filter(adverbsLambdaFunc, self.pos_list_tuple))

    def getFunctionWordsCount(self):
        FunctionLambdaFunc = lambda a: a[1] in ['IN', 'CC', 'PRP', 'PRP$',  'WDT', 'WP', 'WP$', 'UH','PDT']
        return len(filter(FunctionLambdaFunc, self.pos_list_tuple))
