import csv
import cPickle
def cluesFromExcel():

    f = open("processedClues.csv", "w")
    reader = csv.reader(f)
    rowcount = 0
    listOfDic = []

    dic = {}
    file_path = "Data/combinedFinDic.dms"
    with open(file_path, "rb") as f:
        dic = cPickle.load(f)

    for key, value in dic.iteritems():
        print key, value.target


    for row in reader:
        rowcount += 1
        if rowcount == 0:
            continue
        else:
            dic = {}
            dic["rawClue"] = row[0]
            dic["clueType"] = row[4]
            listOfDic.append(dic)

    print rowcount
    return listOfDic

cluesFromExcel()