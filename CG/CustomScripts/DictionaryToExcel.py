import csv
import os
import cPickle
import pandas


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


def numberOfTimesAns(key, playerDic):

    count = 0
    count_correct = 0
    for k in playerDic:
        for i in playerDic[k]:
            if str(key) in str(i['curId']):
                print key
                if i['responseLabel'] == True:
                    count_correct += 1
                count += 1

    if count == 0:
        return -1
    else:
        return (float(count_correct) / count), count_correct, (count-count_correct)

def dicToCVS(dic, file_path):

    employ_data = open(file_path, 'a')

    csvwriter = csv.writer(employ_data)

    if os.stat(file_path).st_size == 0:
        header = ["curID", "rawClue", "procClue", "source", "dateExtracted","target", "type", "targInflections", "length", "avgCOPMI","maxPMI", "Class", 'True', 'False']
        csvwriter.writerow(header)

    for key, value in dic.iteritems():
        # correct_ration, true, false = numberOfTimesAns(key, player)
        #if value.source == 'dictionary.com':
        #if abc > -1:
        vals = [key, value.rawClue,value.procClue,value.source,value.dateExtracted,value.target,value.type,value.targInflections,value.length,
                value.avgCOPMI,value.maxPMI,correct_ration, true, false]
        csvwriter.writerow(vals)

    employ_data.close()

# def parseClues():
#
#     clueFile = "../Data/clueDic/curInteractionLogTable.csv"
#     csv_reader = csv.reader(open(clueFile, "rb"))
#     player = {}
#     prev_val = None
#     i = 0
#
#     for row in csv_reader:
#
#         if row[3] == '-1L' and prev_val != '-1L':
#             i += 1
#             player['player'+str(i)] = []
#             prev_val = '-1L'
#
#         if row[3] != '-1L' and row[5] == "<PLAYER_GUESSER_ASR_SAID>":
#             responseLabel = False
#             if row[2] in row[4]:
#                 responseLabel = True
#             player['player' + str(i)].append({'curId': row[3][:-1], 'target': row[2], 'response': row[4], 'responseLabel':responseLabel})
#             prev_val = row[3]
#
#     return player

dic={}
file_path = "/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/clueDic/finDic_3_6_2018.dms"
# players = parseClues()
with open(file_path,"rb") as f:
        dic=cPickle.load(f)


# dicToCVS(dic, "/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/clueDic/latestFinDic.csv", players)
dicToCVS(dic, "/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/clueDic/latestFinDic.csv")


# def getTimes():
#     path = "/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/clueDic/curInteractionLogTable.csv"
#     df = pandas.read_csv(path)
#     print df.groupby('target')['abnormal']
#     #ax = df.groupby('target')
#     #print ax
#
# getTimes()
