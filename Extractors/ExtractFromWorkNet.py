from nltk.corpus import wordnet

class ExtractFromWordnet:

    def __init__(self):
        pass

    def extractFromWordnet(self, word):
        types = {}
        types['synonyms'] = []
        types['antonyms'] = []
        types['noun'] = []
        types['example_sentences'] = []

        for syn in wordnet.synsets(word, pos=wordnet.NOUN):

            types['example_sentences'] += syn.examples()
            types['noun'].append(syn.definition())
            for l in syn.lemmas():
                if word not in l.name():
                    types['synonyms'].append(l.name())
                if l.antonyms():
                    types['antonyms'].append(l.antonyms()[0].name())

        return types
