import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import norm
from scipy.stats import ttest_ind
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectPercentile

import pprint


def beeSwarnPlotForDifferentSourceDifferentType(df, source, feature):
    sns.set_style("whitegrid")

    sns.set()
    #input()
    sns.swarmplot(x="type", y=feature, data=data)
    if feature == "contentWord/functionWords":
        feature = "contentWord_functionWords"
    plt.savefig("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/"+source +"_"+ feature + ".png")


def beeSwarnPlotForWordNetAndDictExampleSentences(data,feature):
    sns.set_style("whitegrid")

    sns.set()

    sns.swarmplot(x="type", y=feature, data=data)
    if feature == "contentWord/functionWords":
        feature = "contentWord_functionWords"
    #plt.savefig("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/beeSwarnPlotForWordNetAndDictExampleSentences/" + feature + ".png")

def t_test(machine_data, human_data, feature_list):

    #machine clues:
    t_test_results = {}
    for feature in feature_list:
        print feature
        t_test_results[feature] = ttest_ind(machine_data[feature], human_data[feature], equal_var=False)

    pp = pprint.PrettyPrinter(depth=6)
    pp.pprint(t_test_results)

def BeeSwarnPlots():
    sns.set_style("whitegrid")
    sns.set()

    tips = pd.read_csv("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/new.csv")
    ax = sns.boxplot(x="source", y="stopword_count", data=tips)
    #_ = plt.hist(tips['stopword_count'])

    ax = sns.swarmplot(x="source", y="stopword_count", data=tips, color=".2")
    #ax = sns.boxplot(x="source", y="stopword_count", data=tips, showcaps=False, boxprops={'facecolor': 'None'}, showfliers=False, whiskerprops={'linewidth': 0})

def histogramPlot():
    data = pd.read_csv("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/new.csv")
    (mu, sigma) = norm.fit(data['stopword_count'])
    (mu1, sigma1) = norm.fit(data['stopword_count'])
    n, bins1, patches = plt.hist(data['stopword_count'], normed=1, histtype='step', color='r', label="dic")
    n, bins, patches = plt.hist(data['syntax_tree_height'], normed=1, histtype='step', color='b',
                                label="syntax_tree_height")
    print bins
    # y = mlab.normpdf(bins, mu, sigma)
    # y1 = mlab.normpdf(bins1, mu1, sigma1)
    # l = plt.plot(bins, y, 'r--', linewidth=2)
    # l = plt.plot(bins, y1, 'g--', linewidth=2)
    plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=%.3f,\ \sigma=%.3f$' % (mu, sigma))
    plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=%.3f,\ \sigma=%.3f$' % (mu1, sigma1))
    plt.grid(True)
    plt.xlabel("number of stop words")
    plt.ylabel("percentage of clues")

def automatic_feature_selection_select_percentile(data):
    #print data
    x_train, x_test, y_train, y_test = train_test_split(data.drop(['target', 'bi_gram_score', 'type', 'source', 'curID', 'rawClue'], axis=1),
                                                        data.target_label, random_state=0, test_size=0.5)
    select = SelectPercentile(percentile=50)
    select.fit(x_train, y_train)
    x_train_selected = select.transform(x_train)
    for k,v in enumerate(select.get_support()):
        if v == True:
            print x_train.columns[k]

    print x_train_selected.shape


feature_list = ['contentWord/functionWords',
                'lexicon_count',
                'syllable_count',
                'avg_word_legth',
                'stopword_count',
                'bi_gram_score',
            'syntax_tree_height',
                'syntax_tree_non_terminal_node_count',
                'avg_branching_factor_syntax_tree',
            'adjective_and_participle_count',
                'dependency_complexity',
                'flesch_reading_ease',
            'flesch_kincaid_grade',
                'coleman_liau_index',
                'automated_readability_index',
                'dale_chall_readability_score',
            'gunning_fog', 'NE_ALL_count', 'NE_ORGANIZATION_count', 'NE_PERSON_count',
            'NE_LOCATION_count', 'NE_DATE_and_Time_count']
feature_list1 = ['contentWord/functionWords',
                'lexicon_count',
                'syllable_count',
                'avg_word_legth',
                'stopword_count',
            'syntax_tree_height',
                'syntax_tree_non_terminal_node_count',
                'dependency_complexity',
                'flesch_reading_ease',
            'flesch_kincaid_grade',
                'coleman_liau_index',
                'automated_readability_index',
                'dale_chall_readability_score',
            'gunning_fog']



source = ['dict.com', 'wikipedia','wordnet', 'humans']
type = ['exampSent', 'syn', 'def', 'wiki', 'idiomPhrase']
df = pd.read_csv("../Data/featureExtractedDic/feature_dic1.csv")
#df = pd.read_csv("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/new6.csv")

machine_type_list = ['exampSent', 'def', 'syn', 'idiomPhrase', 'ant', 'wiki','wnVerbTropos', 'wnVerbVerbGroups',
                     'wnVerbUsageExample', 'wnVerbDef', 'wnVerbSyn','wnVerbPhrase', 'wnVerbAnt','wnVerbHyper', 'wnNounUsageExample',
                     'wnNounDef', 'wnNounHyper', 'wnNounSyn', 'wnNounHypo', 'wnNounPartMero', 'wnNounPartHolo', 'wnNounTopicMembers']

machine_data = df.loc[(df['type'].isin(machine_type_list))]

human_data = df.loc[df['type'] == 'human']

t_test(machine_data, human_data, feature_list1)
#automatic_feature_selection_select_percentile(machine_data)
#automatic_feature_selection_select_percentile(human_data)

#print machine_data['stopword_count'].describe()

'''
dic_data = df.loc[(df['source'] == 'dict.com')]
wordnet_data = df.loc[df['source'] == 'wordnet']

dic_data = dic_data.loc[dic_data['type'] == "exampSent"]
word_data = wordnet_data.loc[wordnet_data['type'].isin(['wnVerbUsageExample','wnNounUsageExample'])]
data = pd.concat([dic_data, word_data])
#for feature in features:
    #beeSwarnPlotForWordNetAndDictExampleSentences(data, feature)
data = df.loc[(df['source'].isin(['wordnet','dict.com','wikipedia','human'])) & df['type'].isin(['wnVerbUsageExample','wnNounUsageExample','wnNounDef','exampSent',
                                                                                    'wiki', 'def','idiomPhrase', 'human'])]

data.replace('wnVerbUsageExample', 'machine')
data.replace('wnNounUsageExample', 'machine')
data.replace('wnNounDef', 'machine')

#for feature in features:
#beeSwarnPlotForDifferentSourceDifferentType(data,'human','NE_ALL_count')
#BeeSwarnPlots()
#histogramPlot()
#plt.show()

'''