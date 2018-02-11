import csv
import shlex
import cPickle
import pprint

pp = pprint.PrettyPrinter(indent=4)

def createCSVFile():
    f = "../Data/clueDic/curInteractionLogTable.txt"
    out_csv = csv.writer(open("../Data/clueDic/curInteractionLogTable.csv", 'a'))
    header = ['curID', 'uk0', 'target', 'uk1', 'rawClue', 'player', 'uk2', 'uk3', 'score', 'time', 'agent', 'uk4', 'uk5' ,'uk6']
    with open(f) as clueFile:
        out_csv.writerow(header)
        for line in clueFile:
            my_splitter = shlex.shlex(line[1:-2], posix=True)
            my_splitter.whitespace += ','
            my_splitter.whitespace_split = True
            print my_splitter
            out_csv.writerow(list(my_splitter))


def parseClues():
    clueFile = "../Data/clueDic/curInteractionLogTable.csv"
    csv_reader = csv.reader(open(clueFile, "rb"))
    player = {}
    prev_val = None
    i = 0
    for row in csv_reader:

        if row[3] == '-1L' and prev_val != '-1L':
            i += 1
            player['player'+str(i)] = []
            prev_val = '-1L'

        if row[3] != '-1L' and row[5] == "<PLAYER_GUESSER_ASR_SAID>":
            responseLabel = False
            if row[2] in row[4]:
                responseLabel = True
            player['player' + str(i)].append({'curId': row[3][:-1], 'target': row[2], 'response': row[4], 'responseLabel':responseLabel})
            prev_val = row[3]

    pp.pprint(player)


def getCorrectGuesses():
    clueFile = "../Data/clueDic/curInteractionLogTable.csv"
    csv_reader = csv.reader(open(clueFile, "rb"))
    prev_row = ['curID', 'uk0', 'target', 'uk1', 'rawClue', 'player', 'uk2', 'uk3', 0, 'time', 'agent', 'uk4', 'uk5', 'uk6']
    correct_guess = []
    for row in csv_reader:
        print row
        if row[8] > prev_row[8]:
            correct_guess.append({'target': row[2], 'curID': row[0], 'rawClue': row[4]})
        prev_row = row

    print correct_guess



#createCSVFile()
parseClues()
