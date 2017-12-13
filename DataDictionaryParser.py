import pprint
import csv
import os
from ClueGenerator import *

pp = pprint.PrettyPrinter(indent=4)
f = open("Data/curInteractionLogTable.txt", "r")
dic = {}
skip_list = [
'Here is a clue for the first target.',
'I do not want to chat. I want to play the game.  Say start to begin',
'Ok, You are the clue giver this round.',
'Ok, You are the guesser this round.',
'Please say start to play another round.',
'You have run out of time.',
'I enjoyed the game; take care.',
'You have run out of time.  You have played all the required rounds.  If you would like to play another round please pick a role.  If you want to be clue giver say giver. if you want to be the guesser say guesser.  If you want to quit say quit.',
'skip','New Target. ',
'Please wait for the experimenter to direct you to the survey.',
'If you would like to play another round please pick a role.  If you want to be clue giver say giver. if you want to be the guesser say receiver.  If you want to quit say quit.',
'You have run out of time.  Please wait for the experimenter to direct you to the survey.',
'can you speak please speak louder',
"that's right.  New Target.",
"yes, that's right.  New Target.",
'right.  New Target.'
]

def writeToCSV(dic):

    file_path = "./Output/extractData.csv"
    employ_data = open(file_path, 'a')
    csvwriter = csv.writer(employ_data)

    if os.stat(file_path).st_size == 0:
        header = ["target_word", "clues"]
        csvwriter.writerow(header)

    for key, value in dic.iteritems():
        for val in value:
            csvwriter.writerow([key, val])

    employ_data.close()

def extractPLAYER_GIVER_ASR_SAID():
    dic = {}
    skip_list = [
        'no',
        'not correctly',
        'Ok',
        'Okay',
        'can you repeat that',
    ]

    for line in f.readlines():
        tup = eval(line)
        target_word = tup[2]

        if (target_word != '<NOTSET>') and (tup[5] == '<PLAYER_GIVER_ASR_SAID>'):
            if tup[4] in skip_list:
                continue
            if target_word in dic:
                dic[target_word].update(([tup[4]]))
            else:
                dic[target_word] = set()
                dic[target_word].update([tup[4]])
    pp.pprint(dic)
    print "yes"
    for word in dic.keys():
        ClueGenerator().getClues(word, "crawledCluesForPLAYER_GIVER_ASR_SAIDTargetWords")


extractPLAYER_GIVER_ASR_SAID()



