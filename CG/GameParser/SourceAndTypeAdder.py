import csv
import cPickle
import pandas as pd
class clue:
    def __init__(self, curID, rawClu, procClu, sour, dateExtract, targ, typ, targInfl, leng, avgCO, curMaxPMI, blan,
                 oldClueQual, finClueQual):
        self.id = curID
        self.rawClue = rawClu
        self.procClue = procClu
        self.source = sour
        self.dateExtracted = dateExtract
        self.target = targ
        self.type = typ
        self.targInflections = targInfl
        self.length = leng
        self.avgCOPMI = avgCO
        self.maxPMI = curMaxPMI
        self.blank = blan
        self.oldQual = oldClueQual
        self.finQual = finClueQual


def getSourceAndType():

    dic = {}
    file_path = "/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/clueDic/combinedFinDic.dms"
    with open(file_path, "rb") as f:
        dic = cPickle.load(f)

    clueFile = "/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/conversationparserWithSourceAndTpye.csv"

    csv_input = pd.read_csv(clueFile)

    #print dic.keys()
    print type(dic.keys()[1])
    for i in range(len(csv_input['curID'])):
        if long(csv_input['curID'][i]) in dic.keys():
            print "Here ", csv_input['curID'][i]
            key = long(csv_input['curID'][i])
            csv_input['source'][i] = dic[key].source
            csv_input['type'][i] = dic[key].type
            csv_input['targInflections'][i] = dic[key].targInflections
            csv_input['avgCOPMI'][i] = dic[key].avgCOPMI
            csv_input['maxPMI'][i] = dic[key].maxPMI


    csv_input.to_csv(clueFile, index=False)

getSourceAndType()