from textstat.textstat import textstat
'''

References https://pypi.python.org/pypi/textstat/

'''
class readablility:

    text = ""
    def __init__(self,text):
        self.text = text

    def flesch_reading_ease(self):
        return textstat.flesch_reading_ease(self.text)

    def smog_index(self):
        return textstat.smog_index(self.text)

    def flesch_kincaid_grade(self):
        return textstat.flesch_kincaid_grade(self.text)

    def coleman_liau_index(self):
        return textstat.coleman_liau_index(self.text)

    def automated_readability_index(self):
        return textstat.automated_readability_index(self.text)

    def dale_chall_readability_score(self):
        return textstat.dale_chall_readability_score(self.text)

    def gunning_fog(self):
        return textstat.gunning_fog(self.text)
