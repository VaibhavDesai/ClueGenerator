import pprint

import matplotlib.pyplot as plt
import numpy as np
import pandas
from scipy.stats import ttest_ind
# from pandas.tools.plotting import scatter_matrix
from sklearn import model_selection
from sklearn import svm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import RFECV
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import chi2
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


pp = pprint.PrettyPrinter(indent=4)
source = ['dictionary.com', 'wikipedia','wordnet', 'human', 'dict.com']
type = ['exampSent', 'syn', 'def', 'wiki', 'idiomPhrase']
names = ['dependency_complexity', 'NE_LOCATION_count', 'automated_readability_index', 'coleman_liau_index',
             'stopword_count', 'rawClue',
             'syllable_count', 'curID', 'source', 'contentWord/functionWords', 'syntax_tree_non_terminal_node_count',
             'gunning_fog', 'type', 'bi_gram_score', 'NE_PERSON_count', 'NE_ALL_count', 'syntax_tree_height',
             'flesch_reading_ease',
             'dale_chall_readability_score', 'NE_DATE_and_Time_count', 'flesch_kincaid_grade', 'result', 'target',
             'NE_ORGANIZATION_count', 'avg_word_legth','response',
             'frame_count', 'lexicon_count', 'POS_bigram', 'maxPMI', 'avgCOPMI']

exceptions = ['rawClue', 'curID', 'source', 'bi_gram_score', 'type', 'Class', 'target']

sub_names = ['dependency_complexity', 'NE_LOCATION_count',
             'stopword_count', 'syllable_count', 'contentWord/functionWords',
             'syntax_tree_non_terminal_node_count', 'NE_PERSON_count', 'NE_ALL_count',
             'syntax_tree_height', 'dale_chall_readability_score',
                'NE_ORGANIZATION_count', 'avg_word_legth',
             'frame_count', 'lexicon_count', 'maxPMI', 'avgCOPMI']


def getFeaturesForModels(df):

    # for col in names:
    #     if col not in sub_names:
    #         del df[col]

    del df['rawClue']
    del df['curID']
    del df['source']
    del df['type']
    #del df['target']
    del df['bi_gram_score']
    del df['POS_bigram']
    del df['response']


    return df

def models(df):

    df = getFeaturesForModels(df)
    array = df.values
    X = array[:, 0:22]
    Y = array[:, 23]
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,
                                                                                    random_state=seed)
    scoring = 'accuracy'
    models = []
    models.append(('LR', LogisticRegression()))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC()))

    # # evaluate each model in turn
    results = []
    names = []
    for name, model in models:
        kfold = model_selection.KFold(n_splits=10, random_state=seed)
        cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        print(msg)

    print "KNeighborsClassifier"
    knn = KNeighborsClassifier()
    knn.fit(X_train, Y_train)
    predictions = knn.predict(X_validation)
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation, predictions))
    print(classification_report(Y_validation, predictions))

    print "CART"
    CART = DecisionTreeClassifier()
    CART.fit(X_train, Y_train)
    predictions = CART.predict(X_validation)
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation, predictions))
    print(classification_report(Y_validation, predictions))

    print "LR"
    LR = LogisticRegression()
    LR.fit(X_train, Y_train)
    predictions = LR.predict(X_validation)
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation, predictions))
    print(classification_report(Y_validation, predictions))

    print "LDA"
    LDA = LinearDiscriminantAnalysis()
    LDA.fit(X_train, Y_train)
    predictions = LDA.predict(X_validation)
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation, predictions))
    print(classification_report(Y_validation, predictions))

    print "NB"
    NB = GaussianNB()
    NB.fit(X_train, Y_train)
    predictions = NB.predict(X_validation)
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation, predictions))
    print(classification_report(Y_validation, predictions))

    print "SVM"
    SVM = GaussianNB()
    SVM.fit(X_train, Y_train)
    predictions = SVM.predict(X_validation)
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation, predictions))
    precision = float(confusion_matrix(Y_validation, predictions)[1][1])/float((confusion_matrix(Y_validation, predictions)[1][1])+(confusion_matrix(Y_validation, predictions)[0][1]))
    print precision
    print(classification_report(Y_validation, predictions))


def getPrecision(X, Y, type):
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,
                                                                                    random_state=seed)
    if type == 'NB':
        NB = GaussianNB()
        NB.fit(X_train, Y_train)
        predictions = NB.predict(X_validation)

        precision_1 = float(confusion_matrix(Y_validation, predictions)[1][1]) / float(
            (confusion_matrix(Y_validation, predictions)[1][1]) + (confusion_matrix(Y_validation, predictions)[0][1]))

        #precision_0 = float(confusion_matrix(Y_validation, predictions)[0][0]) / float(
        #    (confusion_matrix(Y_validation, predictions)[0][0]) + (confusion_matrix(Y_validation, predictions)[1][0]))

        recall_1 = float(confusion_matrix(Y_validation, predictions)[1][1]) / float(
            (confusion_matrix(Y_validation, predictions)[1][1]) + (confusion_matrix(Y_validation, predictions)[1][0]))

        print "TP", float(confusion_matrix(Y_validation, predictions)[1][1]), "FN", float(confusion_matrix(Y_validation, predictions)[0][1])
        #print precision_1, recall_1

def getDFFeatures(df, indices):

    array = df.values
    Y = array[:, 16]
    output = []
    for i in indices:
        output.append(array[:, i])

    return output, Y


def getFeatureList(names, exceptions):

    feature_list = []
    for feature in names:
        if feature in exceptions:
            continue
        else:
            feature_list.append(feature)
    print feature_list
    return feature_list

def histogramPlots(df,feature_list, group_by):


    for feature in feature_list:
        # red = class value 0, blue class value 1
        ax = df.groupby(group_by)[str(feature)].hist(alpha=0.9)

        std = df.groupby(group_by)[feature].std()
        median = df.groupby(group_by)[feature].median()
        mean = df.groupby(group_by)[feature].mean()

        ax[0].set_title(feature)
        ax[0].set(xlabel="value", ylabel="frequency")
        ax[0].text(0.87, 1, "median-False:"+str(median[0]) +"\nmedian-True:"+str(median[1]) +"\nmean-False:"+str(mean[0]) +"\nmean-True:"+str(mean[1])
                   +"\nstd-False:"+str(std[0])+"\nstd-True:"+str(std[1]), horizontalalignment='center',verticalalignment='center',transform = ax[0].transAxes)

        if feature == 'contentWord/functionWords':
            feature = 'contentWord_functionWords'

        plt.savefig("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Output/gameClues/" + feature + ".png")
        plt.show()

def independent_t_test(df, feature_list, group_by):

    t_test_results = {}
    for feature in feature_list:
        grouped =df.groupby(group_by)[str(feature)].apply(list)
        t_test_results[feature] = ttest_ind(grouped[0], grouped[1], equal_var=False)

    return t_test_results

def featureSelection(df, type, k):

    if type == 'tree':

        features = list(df.columns.values)
        array = df.values
        X = array[:, 0:10]
        Y = array[:, 10]

        forest = ExtraTreesClassifier(n_estimators=250,
                              random_state=0)
        forest.fit(X, Y)
        importances = forest.feature_importances_

        std = np.std([tree.feature_importances_ for tree in forest.estimators_],
                     axis=0)

        indices = np.argsort(importances)[::-1]

        # Print the feature ranking
        print("Feature List:")
        text = ""
        for i, v in enumerate(features):
            text += str(i)+":"+v+"\n"
        print text

        # for f in range(X.shape[1]):
        #     print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))


        # Plot the feature importances of the forest
        plt.figure()
        plt.title("Feature importances")
        plt.bar(range(X.shape[1]), importances[indices],
                color="r")

        plt.xticks(range(X.shape[1]), indices)
        plt.xlim([-1, X.shape[1]])
        plt.show()

    if type == 'selectKBest':
        array = df.values
        X = array[:, 0:16]
        y = array[:, 16]
        selector = SelectKBest(chi2, k=k).fit(X, y)
        x_new = selector.transform(X)  # not needed to get the score
        importances = selector.scores_

        indices = np.argsort(importances)[::-1]
        #for i in indices:
        #    print sub_names[i]

        # for f in range(X.shape[1]):
        #     print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))


        # Plot the feature importances of the forest
        # plt.figure()
        # plt.title("Feature importances")
        # plt.bar(range(X.shape[1]), importances[indices], color="r")
        #
        # plt.xticks(range(X.shape[1]), indices)
        # plt.xlim([-1, X.shape[1]])
        # plt.show()
        return indices

    if type == 'RFE':
        df = getFeaturesForModels(df)
        features = list(df.columns.values)
        array = df.values
        X = array[:, 0:10]
        y = array[:, 10]
        print("Feature List:")
        text = ""
        for i, v in enumerate(features):
            text += str(i) + ":" + v + "\n"
        print text

        # Create the RFE object and rank each pixel
        # Create the RFE object and compute a cross-validated score.
        svc = SVC(kernel="linear")
        # The "accuracy" scoring is proportional to the number of correct
        # classifications
        rfecv = RFECV(estimator=svc, step=1, cv=StratifiedKFold(2),
                      scoring='accuracy')
        rfecv.fit(X, y)

        print("Optimal number of features : %d" % rfecv.n_features_)

        # Plot number of features VS. cross-validation scores
        plt.figure()
        plt.xlabel("Number of features selected")
        plt.ylabel("Cross validation score (nb of correct classifications)")
        plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
        plt.show()
        # svm = LinearSVC()
        # rfe = RFE(svm, 5)
        # rfe = rfe.fit(X, y)
        # # print summaries for the selection of attributes
        # print(rfe.support_)
        # print(rfe.ranking_)

    if type == 'L1':
        df = getFeaturesForModels(df)
        features = list(df.columns.values)
        array = df.values
        X = array[:, 0:10]
        y = array[:, 10]
        print("Feature List:")
        text = ""
        for i, v in enumerate(features):
            text += str(i) + ":" + v + "\n"
        print text
        lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(X, y)
        model = SelectFromModel(lsvc, prefit=True)
        X_new = model.transform(X)
        print X_new.shape
        print(lsvc.coef_)

def pipeLine(df):

    df = getFeaturesForModels(df)
    features = list(df.columns.values)
    array = df.values
    X = array[:, 0:10]
    y = array[:, 10]

    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, y, test_size=validation_size,
                                                                                    random_state=seed)
    anova_filter = SelectKBest(f_regression, k=5)

    clf = svm.SVC(kernel='linear')
    anova_svm = Pipeline([('anova', anova_filter), ('svc', clf)])
    anova_svm.set_params(anova__k=10, svc__C=.1).fit(X_train, Y_train)

    prediction = anova_svm.predict(X_validation)
    print(classification_report(Y_validation, prediction))

    # getting the selected features chosen by anova_filter
    print anova_svm.named_steps['anova'].get_support()




def newGivenCluesDataSet():
    path = "/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/featureExtractedDic/conversationparserWithAllFeatures.csv"
    df = pandas.read_csv(path)
    # changing all the true and false into 1/0
    df.loc[df['result'] == 'CORRECT', 'result'] = 1
    df.loc[df['result'] == 'NO_RESPONSE', 'result'] = 0
    df.loc[df['result'] == 'SKIP', 'result'] = 0
    df.loc[df['result'] == 'OUT_OF_TIME', 'result'] = 0
    df.loc[df['result'] == 'WRONG', 'result'] = 0
    #models(df)
    k = 0
    #try:
    df = getFeaturesForModels(df)
    indices = featureSelection(df, 'selectKBest', 3)
    print indices
    for i in indices:
        print sub_names[i]

    for k in range(3,16):
        print k,
        indices = featureSelection(df, 'selectKBest', k)
        X_values,Y_values = getDFFeatures(df, indices[:k])

        X_values = pandas.DataFrame(X_values)
        X_values = X_values.transpose()
        getPrecision(X_values, Y_values, 'NB')
#except:
    #    print k, "error"

def oldGivenCluesDataSet():
    path = "/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/featureExtractedDic/OnlyGivenCluesfeaturesWithClass.csv"
    df = pandas.read_csv(path)
    # changing all the true and false into 1/0
    df.loc[df['class'] == True, 'class'] = 1
    df.loc[df['class'] == False, 'class'] = 0
    #models(df)

    #Plotting hist on all the featuers and group by Class(True/False)
    #histogramPlots(df, getFeatureList(names,exceptions), 'Class')

    #Independent T Test on all the features grouped by Class(True/False)
    #pp.pprint(independent_t_test(df, getFeatureList(names,exceptions), 'Class'))

    featureSelection(df, 'RFE')

    #pipeLine(df)


newGivenCluesDataSet()