import csv
import os
import cPickle


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



def dicToCVS(dic, file_path):

    employ_data = open(file_path, 'a')

    csvwriter = csv.writer(employ_data)

    if os.stat(file_path).st_size == 0:
        header = ["curID", "rawClue", "procClue", "source", "dateExtracted","target", "type", "targInflections", "length", "avgCOPMI","maxPMI", "blank"]
        csvwriter.writerow(header)

    for key, value in dic.iteritems():
        vals = [key, value.rawClue,value.procClue,value.source,value.dateExtracted,value.target,value.type,value.targInflections,value.length,value.avgCOPMI,value.maxPMI]
        csvwriter.writerow(vals)

    employ_data.close()

dic={}
file_path = "../Data/combinedFinDic.dms"
with open(file_path,"rb") as f:
        dic=cPickle.load(f)

dicToCVS(dic, "../Data/dicToExcel.csv")

