import csv

def cluesFromExcel():

    f = open("crawledCluesForPLAYER_GIVER_ASR_SAIDTargetWords.csv", "rb")
    reader = csv.reader(f)
    rowcount = 0
    listOfDic = []
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