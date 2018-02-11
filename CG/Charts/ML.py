import pandas
#from pandas.tools.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from scipy.stats import norm
from scipy.stats import ttest_ind
import pprint


source = ['dictionary.com', 'wikipedia','wordnet', 'human', 'dict.com']
type = ['exampSent', 'syn', 'def', 'wiki', 'idiomPhrase']
names = ['dependency_complexity', 'NE_LOCATION_count', 'automated_readability_index', 'coleman_liau_index',
             'stopword_count', 'rawClue',
             'syllable_count', 'curID', 'source', 'contentWord/functionWords', 'syntax_tree_non_terminal_node_count',
             'gunning_fog', 'type', 'bi_gram_score', 'NE_PERSON_count', 'NE_ALL_count', 'syntax_tree_height',
             'flesch_reading_ease',
             'dale_chall_readability_score', 'NE_DATE_and_Time_count', 'flesch_kincaid_grade', 'Class', 'target',
             'NE_ORGANIZATION_count', 'avg_word_legth',
             'frame_count', 'lexicon_count']

exceptions = ['rawClue', 'curID', 'source', 'bi_gram_score', 'type', 'Class', 'target']

def loadDataSet():
    path = "../Data/featureExtractedDic/feature_dic1.csv"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = pandas.read_csv(path, names=names)
    return dataset

def getMachineClueDataSet(dataframe):

    machine_type_list = ['exampSent', 'def', 'syn', 'idiomPhrase', 'ant', 'wiki', 'wnVerbTropos', 'wnVerbVerbGroups',
                         'wnVerbUsageExample', 'wnVerbDef', 'wnVerbSyn', 'wnVerbPhrase', 'wnVerbAnt', 'wnVerbHyper',
                         'wnNounUsageExample',
                         'wnNounDef', 'wnNounHyper', 'wnNounSyn', 'wnNounHypo', 'wnNounPartMero', 'wnNounPartHolo',
                         'wnNounTopicMembers']

    return dataframe.loc[(dataframe['type'].isin(machine_type_list))]

def getHumanClueDataSet(dataframe):
    return dataframe.loc[dataframe['type'] == 'human']

def t_test(machine_df, human_df, feature_list):

    #machine clues:
    t_test_results = {}
    for feature in feature_list:
        t_test_results[feature] = ttest_ind(machine_df[feature], human_df[feature], equal_var=False)

    #pp = pprint.PrettyPrinter(depth=6)
    #pp.pprint(t_test_results)
    return t_test_results

def UnivariatePlots(df):
    # box and whisker plots
    df.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)















def MultivariatePlots(df):
    scatter_matrix(df)

