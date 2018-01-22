import csv
import time

import os


from ContentWords import ContentWords
from ReadabilityTest import readablility
from TextFeatures import TextFeatures
from threading import Thread
from pymongo import MongoClient
from Queue import Queue
result = []
from nltk.corpus import brown
from nltk.corpus import stopwords

class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""

    def __init__(self, tasks):
        client = MongoClient(port=27017)
        self.db = client.test
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):

        while True:
            func, args, kargs = self.tasks.get()
            try:
                feature = func(*args, **kargs)
                print self.db.reviews.insert_one(feature)
                
            except Exception, e:
                print e
            finally:
                self.tasks.task_done()


class ThreadPool:
    """Pool of threads consuming tasks from a queue"""
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    '''def add_task(self, fe):
        """Add a task to the queue"""
        self.tasks.put(fe)'''


    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()


def getNumericValue(row, brown, stop_words ):

    features = {}
    features['curID'] = row['curID']
    features['rawClue'] = row['rawClue']
    features['target'] = row['target']
    features['source'] = row['source']
    features['type'] = row['type']

    content_words = ContentWords(features['rawClue'])

    try:
        features['contentWord/functionWords'] = content_words.getContentWordsCount()/content_words.getFunctionWordsCount()
    except:
        features['contentWord/functionWords'] = 0

    text_features = TextFeatures(features['rawClue'], brown, stop_words )
    features['lexicon_count'] = text_features.lexicon_count()
    features['syllable_count'] = text_features.syllable_count()
    features['avg_word_legth'] = text_features.avg_letters_per_word_count()
    features['stopword_count'] = text_features.stopword_count()
    features['bi_gram_score'] = text_features.nGram(2)
    features['syntax_tree_height'] = text_features.syntax_tree_height()
    features['syntax_tree_non_terminal_node_count'] = text_features.syntax_tree_non_terminal_node_count()

    ####features['dependency_complexity'] = text_features.dependency_complexity()

    features['frame_count'] = text_features.frame_count()
    features['NE_ALL_count'] = text_features.NER('ALL')
    features['NE_ORGANIZATION_count'] = text_features.NER('ORGANIZATION')
    features['NE_PERSON_count'] = text_features.NER('PERSON')
    features['NE_LOCATION_count'] = text_features.NER('LOCATION') + text_features.NER('GPE')
    features['NE_DATE_and_Time_count'] = text_features.NER('DATE') + text_features.NER('TIME')
    
    readability_test = readablility(features['rawClue'])
    features['flesch_reading_ease'] = readability_test.flesch_reading_ease()

    features['flesch_kincaid_grade'] = readability_test.flesch_kincaid_grade()
    features['coleman_liau_index'] = readability_test.coleman_liau_index()
    features['automated_readability_index'] = readability_test.automated_readability_index()
    features['dale_chall_readability_score'] = readability_test.dale_chall_readability_score()
    features['gunning_fog'] = readability_test.gunning_fog()

    # features['avg_branching_factor_syntax_tree'] = text_features.avg_branching_factor_syntax_tree()
    # features['adjective_and_participle_count'] = text_features.avg_branching_factor_syntax_tree()
    # features['preposition_count'] = text_features.avg_branching_factor_syntax_tree()
    # features['tri_gram_score'] = text_features.nGram(3)
    # features['smog_index'] = readability_test.smog_index()

    return features

class FeatureExtractor:

    text = ""
    features = {}

    def __init__(self, text):

        self.text = text


    def getFeatures(self):
        return self.features

    def getNumericValue(self):
        print self.text
        self.features['rawClue'] = self.text

        content_words = ContentWords(self.text)
        try:
            self.features['contentWord/functionWords'] = content_words.getContentWordsCount()/content_words.getFunctionWordsCount()
        except:
            self.features['contentWord/functionWords'] = 0
        #text_features = TextFeatures(text, annotator, brown_words)
        #features['lexicon_count'] = text_features.lexicon_count()
        #features['syllable_count'] = text_features.syllable_count()
        #features['avg_word_legth'] = text_features.avg_letters_per_word_count()
        #features['stopword_count'] = text_features.stopword_count()
        #features['bi_gram_score'] = text_features.nGram(2)
        '''
        #features['tri_gram_score'] = text_features.nGram(3)
        features['syntax_tree_height'] = text_features.syntax_tree_height()
        features['syntax_tree_non_terminal_node_count'] = text_features.syntax_tree_non_terminal_node_count()
        #features['avg_branching_factor_syntax_tree'] = text_features.avg_branching_factor_syntax_tree()
        #features['adjective_and_participle_count'] = text_features.avg_branching_factor_syntax_tree()
        features['dependency_complexity'] = text_features.dependency_complexity()
        features['frame_count'] = text_features.frame_count()
        #features['preposition_count'] = text_features.avg_branching_factor_syntax_tree()
        features['NE_ALL_count'] = text_features.NER('ALL')
        features['NE_ORGANIZATION_count'] = text_features.NER('ORGANIZATION')
        features['NE_PERSON_count'] = text_features.NER('PERSON')
        features['NE_LOCATION_count'] = text_features.NER('LOCATION') + text_features.NER('GPE')
        features['NE_DATE_and_Time_count'] = text_features.NER('DATE') + text_features.NER('TIME')
        '''
        readability_test = readablility(self.text)
        self.features['flesch_reading_ease'] = readability_test.flesch_reading_ease()
        #features['smog_index'] = readability_test.smog_index()
        self.features['flesch_kincaid_grade'] = readability_test.flesch_kincaid_grade()
        self.features['coleman_liau_index'] = readability_test.coleman_liau_index()
        self.features['automated_readability_index'] = readability_test.automated_readability_index()
        self.features['dale_chall_readability_score'] = readability_test.dale_chall_readability_score()
        self.features['gunning_fog'] = readability_test.gunning_fog()

        return self.features

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

    pool = ThreadPool(20)
    count = 0
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        brown.ensure_loaded()
        stopwords.ensure_loaded()
        stop_words = set(stopwords.words('english'))

        for row in reader:
            print count
            print row['rawClue']
            try:
                pool.add_task(getNumericValue, row, brown, stop_words)
                count += 1
            except:
                continue
        pool.wait_completion()

t0 = time.time()
readingClues("../Data/newDicToExcel.csv")
t1 = time.time()
total = t1-t0
print total