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
    #times=[]
    content_words = ContentWords(text)
    #times.append(time.time())
    try:
        features['contentWord/functionWords'] = content_words.getContentWordsCount()/content_words.getFunctionWordsCount()
    except:
        features['contentWord/functionWords'] = 0

    #times.append(time.time())
    text_features = TextFeatures(text,annotator, bigrams_freq)
    #times.append(time.time())
    features['lexicon_count'] = text_features.lexicon_count()
    #times.append(time.time())
    features['syllable_count'] = text_features.syllable_count()
    #times.append(time.time())
    features['avg_word_legth'] = text_features.avg_letters_per_word_count()
    #times.append(time.time())
    features['stopword_count'] = text_features.stopword_count()
    #times.append(time.time())
    features['bi_gram_score'] = text_features.nGram(2)
    #times.append(time.time())
    #features['tri_gram_score'] = text_features.nGram(3)
    features['syntax_tree_height'] = text_features.syntax_tree_height()
    #times.append(time.time())
    features['syntax_tree_non_terminal_node_count'] = text_features.syntax_tree_non_terminal_node_count()
    #times.append(time.time())
    #features['avg_branching_factor_syntax_tree'] = text_features.avg_branching_factor_syntax_tree()
    #features['adjective_and_participle_count'] = text_features.avg_branching_factor_syntax_tree()
    features['dependency_complexity'] = text_features.dependency_complexity()
    #times.append(time.time())
    features['frame_count'] = text_features.frame_count()
    #features['preposition_count'] = text_features.avg_branching_factor_syntax_tree()
    #times.append(time.time())
    readability_test = readablility(text)
    features['flesch_reading_ease'] = readability_test.flesch_reading_ease()
    #times.append(time.time())
    #features['smog_index'] = readability_test.smog_index()
    features['flesch_kincaid_grade'] = readability_test.flesch_kincaid_grade()
    #times.append(time.time())
    features['coleman_liau_index'] = readability_test.coleman_liau_index()
    #times.append(time.time())
    features['automated_readability_index'] = readability_test.automated_readability_index()
    #times.append(time.time())
    features['dale_chall_readability_score'] = readability_test.dale_chall_readability_score()
    #times.append(time.time())
    features['gunning_fog'] = readability_test.gunning_fog()
    #times.append(time.time())
    features['NE_ALL_count'] = text_features.NER('ALL')
    #times.append(time.time())
    features['NE_ORGANIZATION_count'] = text_features.NER('ORGANIZATION')
    #times.append(time.time())
    features['NE_PERSON_count'] = text_features.NER('PERSON')
    #times.append(time.time())
    features['NE_LOCATION_count'] = text_features.NER('LOCATION') + text_features.NER('GPE')
    #times.append(time.time())
    features['NE_DATE_and_Time_count'] = text_features.NER('DATE') + text_features.NER('TIME')
    #times.append(time.time())
    count=0
    #print times
    '''for tim in times:
        if count>0:
            print "Count "+str(count)+":" +str(tim-last)
        count = count+1
        last = tim
    '''
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

    #pool = ThreadPool(2)
    count = 0
    anntator = Annotator()
    result = []

    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print count
            print row['rawClue']
            #try:
            features = getNumericValue(row['rawClue'], anntator)
            features['curID'] = row['curID']
            features['rawClue'] = row['rawClue']
            features['target'] = row['target']
            features['source'] = row['source']
            features['type'] = row['type']
            result.append(features)
            #pool.add_task(getNumericValue, features['rawClue'])
            count += 1
            if count%100 == 0:
                dicToCVS(result,"../Data/featureExtractedDic/new1.txt")



t0 = time.time()
readingClues("../Data/newDicToExcel.csv")
t1 = time.time()
total = t1-t0
print total