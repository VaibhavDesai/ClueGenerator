from textstat.textstat import textstat
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class TextFeatures:

    text = ""
    def __int__(self,text):
        self.text = text

    def lexicon_count(self):
        return textstat.lexicon_count(self.text)

    def syllable_count(self):
        return textstat.syllable_count(self.text)

    def word_count(self):
        return len(self.text.split(" "))

    def avg_letters_count(self):
        return textstat.avg_letter_per_word

    def avg_letters_word(self):
        textstat.avg
        return textstat.avg_letter_per_word

    def stopword_count(self):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(self.text)
        count = 0
        for w in word_tokens:
            if w in stop_words:
                count +=1

        return count

