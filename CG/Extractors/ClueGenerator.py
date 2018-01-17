from CG.CustomScripts.Utils import *
from CG.Extractors import ExtractFromDictionaryDotCom, ExtractFromWorkNet


class ClueGenerator:

    def getClues(self, word, output_file_name):
        try:
            writeToCSV(ExtractFromDictionaryDotCom.ExtractFromDictionaryDotCom().extractFromDictionaryDotCom(word), word, "dictionary.com", output_file_name)
            writeToCSV(ExtractFromWorkNet.ExtractFromWorkNet().extractFromWordnet(word), word, "wordnet", output_file_name)
            writeToCSV(ExtractFromWorkNet.ExtractFromWiki().extractFromWiki(word), word, "wiki", output_file_name)
        except:
            pass

