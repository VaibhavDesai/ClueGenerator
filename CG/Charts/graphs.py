import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import csv
from scipy.stats import norm

def BeeSwarnPlots():
    sns.set_style("whitegrid")
    sns.set()
    tips = pd.read_csv("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/new.csv")
    #_ = plt.hist(tips['stopword_count'])

    ax = sns.swarmplot(x="source", y="stopword_count", data=tips)
    #ax = sns.boxplot(x="source", y="stopword_count", data=tips, showcaps=False, boxprops={'facecolor': 'None'}, showfliers=False, whiskerprops={'linewidth': 0})

    plt.show()

def histogramPlot():

    data = pd.read_csv("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/new.csv")
    (mu, sigma) = norm.fit(data['stopword_count'])
    n, bins, patches = plt.hist(data['stopword_count'],normed=1, histtype='step',color='r', label="dic")
    n, bins, patches = plt.hist(data['syntax_tree_height'], normed=1, histtype='step', color='b', label="syntax_tree_height")
    print bins
    y = mlab.normpdf(bins, mu, sigma)
    l = plt.plot(bins, y, 'r--', linewidth=2)
    plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=%.3f,\ \sigma=%.3f$' % (mu, sigma))
    plt.grid(True)
    plt.xlabel("number of stop words")
    plt.ylabel("percentage of clues")


#BeeSwarnPlots()
histogramPlot()
plt.show()
