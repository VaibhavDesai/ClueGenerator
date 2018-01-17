import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import csv
from scipy.stats import norm


def beeSwarnPlotForDifferentSourceDifferentType(df, source, feature):
    sns.set_style("whitegrid")

    sns.set()
    print data
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
    n, bins1, patches = plt.hist(data['stopword_count'],normed=1, histtype='step',color='r', label="dic")
    n, bins, patches = plt.hist(data['syntax_tree_height'], normed=1, histtype='step', color='b', label="syntax_tree_height")
    print bins
    #y = mlab.normpdf(bins, mu, sigma)
    #y1 = mlab.normpdf(bins1, mu1, sigma1)
    #l = plt.plot(bins, y, 'r--', linewidth=2)
    #l = plt.plot(bins, y1, 'g--', linewidth=2)
    plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=%.3f,\ \sigma=%.3f$' % (mu, sigma))
    plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=%.3f,\ \sigma=%.3f$' % (mu1, sigma1))
    plt.grid(True)
    plt.xlabel("number of stop words")
    plt.ylabel("percentage of clues")


features = ['contentWord/functionWords', 'lexicon_count', 'syllable_count', 'avg_word_legth', 'stopword_count','bi_gram_score',
            'syntax_tree_height','syntax_tree_non_terminal_node_count','avg_branching_factor_syntax_tree',
            'adjective_and_participle_count','dependency_complexity', 'flesch_reading_ease',
            'flesch_kincaid_grade', 'coleman_liau_index', 'automated_readability_index', 'dale_chall_readability_score',
            'gunning_fog', 'NE_ALL_count', 'NE_ORGANIZATION_count', 'NE_PERSON_count',
            'NE_LOCATION_count', 'NE_DATE_and_Time_count']

source = ['dict.com', 'wikipedia','wordnet', 'humans']
type = ['exampSent', 'syn', 'def', 'wiki', 'idiomPhrase']
df = pd.read_csv("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/new6.csv")


dic_data = df.loc[df['source'] == 'dict.com']
word_data = df.loc[df['source'] == 'wordnet']
dic_data = dic_data.loc[dic_data['type'] == "exampSent"]
word_data = word_data.loc[word_data['type'].isin(['wnVerbUsageExample','wnNounUsageExample'])]
data = pd.concat([dic_data, word_data])
#for feature in features:
    #beeSwarnPlotForWordNetAndDictExampleSentences(data, feature)
data = df.loc[(df['source'].isin(['wordnet','dict.com','wikipedia','human'])) & df['type'].isin(['wnVerbUsageExample','wnNounUsageExample','wnNounDef','exampSent',
                                                                                    'wiki', 'def','idiomPhrase', 'human'])]
#for feature in features:
beeSwarnPlotForDifferentSourceDifferentType(data,'human','NE_ALL_count')
#BeeSwarnPlots()
#histogramPlot()
plt.show()
