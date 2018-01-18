import csv
import time

import os
from nltk.corpus import brown
from practnlptools.tools import Annotator

from CG.Utils.ThreadPool import ThreadPool
from ContentWords import ContentWords
from ReadabilityTest import readablility
from TextFeatures import TextFeatures

brown_words = brown.words()
result = []

def getNumericValue(text, annotator):
    features = {}

    content_words = ContentWords(text)
    try:
        features['contentWord/functionWords'] = content_words.getContentWordsCount()/content_words.getFunctionWordsCount()
    except:
        features['contentWord/functionWords'] = 0
    text_features = TextFeatures(text,annotator, brown_words)
    features['lexicon_count'] = text_features.lexicon_count()
    features['syllable_count'] = text_features.syllable_count()
    features['avg_word_legth'] = text_features.avg_letters_per_word_count()
    features['stopword_count'] = text_features.stopword_count()
    features['bi_gram_score'] = text_features.nGram(2)

    #features['tri_gram_score'] = text_features.nGram(3)
    features['syntax_tree_height'] = text_features.syntax_tree_height()
    features['syntax_tree_non_terminal_node_count'] = text_features.syntax_tree_non_terminal_node_count()
    #features['avg_branching_factor_syntax_tree'] = text_features.avg_branching_factor_syntax_tree()
    #features['adjective_and_participle_count'] = text_features.avg_branching_factor_syntax_tree()
    features['dependency_complexity'] = text_features.dependency_complexity()
    features['frame_count'] = text_features.frame_count()
    #features['preposition_count'] = text_features.avg_branching_factor_syntax_tree()

    readability_test = readablility(text)
    features['flesch_reading_ease'] = readability_test.flesch_reading_ease()
    #features['smog_index'] = readability_test.smog_index()
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

    vals = []
    for dic in result:
        vals = []
        for key, value in dic.iteritems():
            vals.append(value)
        csvwriter.writerow(vals)

    employ_data.close()

def readingClues(file_path):

    pool = ThreadPool(2)
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
                features['ID'] = count
                features['rawClue'] = row['rawClue']
                features['target'] = row['target']
                features['source'] = row['source']
                features['type'] = row['type']
                result.append(features)
                #pool.add_task(getNumericValue, features['rawClue'])
                count += 1
                if count%100 == 0:
                    dicToCVS(result,"../Data/new4.txt")
                    result = []
            except:
                continue
        #pool.wait_completion()

t0 = time.time()
readingClues("../Data/dicToExcel.csv")
t1 = time.time()
total = t1-t0
print total