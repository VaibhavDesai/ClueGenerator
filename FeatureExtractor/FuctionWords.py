from nltk import word_tokenize
import nltk

'''
    >>>nltk.help.upenn_tagset()
    
    Pronouns, prepositions, conjunctions, determiners, qualifiers/intensifiers, and interrogatives 
    
    IN: preposition or conjunction, subordinating
    CC: conjunction, coordinating
    PRP: pronoun, personal
    PRP$: pronoun, possessive
    WDT: WH-determiner
    WP: WH-pronoun
    WP$: WH-pronoun, possessive
    UH: interjection
    PDT: pre-determiner
    
'''

class FunctionWords:

    pos_list_tuple = {}

    def __init__(self, inp):

        text = word_tokenize(inp)
        self.pos_list_tuple = nltk.pos_tag(text)
        print self.pos_list_tuple

    def getFunctionWordsCount(self):
        FunctionLambdaFunc = lambda a: a[1] in ['IN','CC', 'PRP', 'PRP$',  'WDT', 'WP', 'WP$', 'UH','PDT']
        return len(filter(FunctionLambdaFunc, self.pos_list_tuple))

f = FunctionWords("My name is Vaibhav")
print f.getFunctionWordsCount()