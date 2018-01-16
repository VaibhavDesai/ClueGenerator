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


