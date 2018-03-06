import csv
import time

import os
from nltk.corpus import brown
from practnlptools.tools import Annotator

from ContentWords import ContentWords
from ReadabilityTest import readablility
from TextFeatures import TextFeatures
from nltk.util import ngrams
from collections import Counter

brown_words = brown.words()
bigrams = ngrams(brown_words, 2)
bigrams_freq = Counter(bigrams)
result = []

def getNumericValue(text, annotator):
    features = {}
    content_words = ContentWords(text)
    try:
        features['contentWord/functionWords'] = content_words.getContentWordsCount()/content_words.getFunctionWordsCount()
    except:
        features['contentWord/functionWords'] = 0

    text_features = TextFeatures(text,annotator, bigrams_freq)
    features['lexicon_count'] = text_features.lexicon_count()
    features['syllable_count'] = text_features.syllable_count()
    features['avg_word_legth'] = text_features.avg_letters_per_word_count()
    features['stopword_count'] = text_features.stopword_count()
    features['bi_gram_score'] = text_features.nGram(2)
    features['syntax_tree_height'] = text_features.syntax_tree_height()
    features['syntax_tree_non_terminal_node_count'] = text_features.syntax_tree_non_terminal_node_count()
    #features['avg_branching_factor_syntax_tree'] = text_features.avg_branching_factor_syntax_tree()
    #features['adjective_and_participle_count'] = text_features.avg_branching_factor_syntax_tree()
    features['dependency_complexity'] = text_features.dependency_complexity()
    features['frame_count'] = text_features.frame_count()
    #features['preposition_count'] = text_features.avg_branching_factor_syntax_tree()
    readability_test = readablility(text)
    features['flesch_reading_ease'] = readability_test.flesch_reading_ease()
    features['smog_index'] = readability_test.smog_index()
    features['flesch_kincaid_grade'] = readability_test.flesch_kincaid_grade()
    features['coleman_liau_index'] = readability_test.coleman_liau_index()
    features['automated_readability_index'] = readability_test.automated_readability_index()
    features['dale_chall_readability_score'] = readability_test.dale_chall_readability_score()
    features['gunning_fog'] = readability_test.gunning_fog()
    features['NE_ALL_count'] = text_features.NER('ALL')
    features['NE_ORGANIZATION_count'] = text_features.NER('ORGANIZATION')
    features['NE_PERSON_count'] = text_features.NER('PERSON')
    features['NE_LOCATION_count'] = text_features.NER('LOCATION') + text_features.NER('GPE')
    features['NE_DATE_and_Time_count'] = text_features.NER('DATE') + text_features.NER('TIME')
    features['POS_bigram'] = text_features.getPosBigram()

    print features
    return features

def dicToCVS(result, file_path):

    employ_data = open(file_path, 'a')

    csvwriter = csv.writer(employ_data, delimiter="\t")

    if os.stat(file_path).st_size == 0:
        dic = result[0]
        header = []
        header += dic.keys()
        csvwriter.writerow(header)

    for dic in result:
        vals = []
        for key, value in dic.iteritems():
            vals.append(value)
        csvwriter.writerow(vals)

    employ_data.close()

def readingClues(file_path):

    count = 0
    anntator = Annotator()
    result = []
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print count
            print row['rawClue']
            try:
                features = getNumericValue(row['rawClue'], anntator)
                features['curID'] = row['curID']
                features['rawClue'] = row['rawClue']
                features['target'] = row['target']
                features['source'] = row['source']
                features['type'] = row['type']
                features['result'] = row['result']
                features['response'] = row['response']
                features['avgCOPMI'] = row['avgCOPMI']
                features['maxPMI'] = row['maxPMI']
                #features['class'] = row['class']
                result.append(features)
                count += 1
                if count%100 == 0:
                    dicToCVS(result, "../Data/featureExtractedDic/conversationparserWithAllFeatures.txt")
                    result = []

            except:
                continue

         #write the remaining results into the file.
        dicToCVS(result, "../Data/featureExtractedDic/testing.txt")



t0 = time.time()
readingClues("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/conversationparserWithSourceAndTpye.csv")
t1 = time.time()
total = t1-t0
print total