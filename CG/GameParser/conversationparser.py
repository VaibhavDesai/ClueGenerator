import pprint
import string
import re
from difflib import SequenceMatcher

import csv
import cPickle

#prev_row = ['curID', 'uk0', 'target', 'uk1', 'rawClue', 'player', 'uk2', 'uk3', 0, 'time', 'agent', 'uk4', 'uk5', 'uk6']


class CoversationParser:

    csv_reader = None

    def __init__(self, file_path):
        self.csv_reader = csv.reader(open(file_path, "rb"))


    def parseClues(self):
        masterDic = {}
        dic = {}
        last_speaker = ""
        skipNext = False
        giverRound = 0
        masterDic[str('guesser ' + str(0))] = []
        for row in self.csv_reader:
            row[2] = row[2].translate(None, string.whitespace)
            row[2] = row[2].strip("'")
            #row[4] = row[4].strip("'")


            if '<NOTSET>' not in str(row[2]) and '<ROBOT_END>' not in str(row[5]) and '<TIMER_DECREMENT>' not in str(row[5]) \
                    and '<PLAYER_GIVER_ASR_SAID>' not in str(row[5]):

                if '<WIZARD_ASR_SAID>' in str(row[5]):
                    skipNext = True
                    continue

                if skipNext:
                    skipNext = False
                    continue

                if '<SEND_ROBOT>' in row[5] and 'You are the clue giver this round.' in row[4]:
                    continue

                if '<SEND_ROBOT>' in row[5] and "Ok " in str(row[4]):
                    print "here"
                    giverRound += 1
                    masterDic[str('guesser '+str(giverRound))] = []
                    masterDic[str('guesser ' + str(giverRound-1))].append(dic)
                    dic = {}
                    continue

                if row[2] not in dic:
                    dic[row[2]] = []

                current_speaker = row[5]

                if '<OUT_TIME>' in current_speaker:
                    if '<OUT_TIME>' in last_speaker:
                        continue
                    if len(dic[row[2]]) > 0:
                        dic[row[2]][-1]['response'] = "OUT_OF_TIME"

                elif '<SEND_ROBOT>' in current_speaker:
                    dic[row[2]].append({"clueId":row[3], "rawClue":str(row[4]), "response":""})

                elif '<SEND_ROBOT>' in last_speaker and ('<PLAYER_GUESSER_ASR_SAID>' in current_speaker
                                                       or '<USER_REPEAT_SAID>' in current_speaker
                                                       or '<USER_CORRECT_STORED_SAID>' in current_speaker
                                                       or '<PLAYER_GUESSER_SKIP_SAID>' in current_speaker
                                                       or '<USER_SKIP_STORED_SAID>' in current_speaker
                                                       or '<USER_IDLE_TRIGGER>' in current_speaker):

                    if '<USER_IDLE_TRIGGER>' in current_speaker:
                        dic[row[2]][-1]['response'] = "NO_RESPONSE"
                    else:
                        dic[row[2]][-1]['response'] = row[4]



                last_speaker = row[5]

        return dic


def removeExtraCharactersFromTheString(str):
    str = str.strip("'")
    str = re.sub('[ \t\n]+', ' ', str)
    if " '" in str:
        str = str.strip(" '")
    if "New Target." in str:
        str = re.sub("New Target. ", '', str)

    if "no ." in str:
        str = re.sub("no . ", '', str)

    if "wrong ." in str:
        str = re.sub("wrong . ", '', str)

    if "not right ." in str:
        str = re.sub("not right . ", '', str)

    return str


def postProcessing(dic):

    new_dic = {}
    exception = ["skip", "You have run out of time", "Please wait for the experimenter to direct you to the survey",
                 "I do not want to chat.", "Please say start to play another round.",
                 "I enjoyed the game; take care.", "If you would like to play another round please pick a role",
                 'right.  New Target.',
                 "that\'s right.  New Target.", "that\'s right!"]

    for k,v in dic.iteritems():
        if len(v) != 0:
            new_dic[k] = []
            for item in v:


                if " 'New Target. '" == item['rawClue']:
                    continue

                if item['response'] == '':
                    continue

                if not any(st in item['rawClue'] for st in exception):
                    new_dic[k].append(item)

                item['clueId'] = removeExtraCharactersFromTheString(item['clueId'])
                item['rawClue'] = removeExtraCharactersFromTheString(item['rawClue'])
                item['response'] = removeExtraCharactersFromTheString(item['response'])

                if k in item['response']:
                    item['result'] = 'CORRECT'
                elif 'OUT_OF_TIME' in item['response']:
                    item['result'] = 'OUT_OF_TIME'
                elif 'NO_RESPONSE' in item['response']:
                    item['result'] = 'NO_RESPONSE'
                elif 'skip' in item['response']:
                    item['result'] = 'SKIP'
                else:
                    item['result'] = 'WRONG'


            if len(new_dic[k]) == 0:
                del new_dic[k]

    return new_dic

def combiningIds(v):

    for i in range(len(v)):

        for j in range(i+1, len(v)):
            s = SequenceMatcher(None, v[i]['rawClue'], v[j]['rawClue'])
            if s.ratio() > 0.90:

                v[j]['clueId'] = v[i]['clueId']
    return v


def writeToCSV(dictionary, output_file_name):

    csvwriter = csv.writer(open(output_file_name, 'a'))

    header = ["target", "clueId", "rawClue", "response", "result"]
    csvwriter.writerow(header)

    for k, v in dictionary.iteritems():

        for i in v:
            vals = [k, i["clueId"], i['rawClue'], i['response'], i['result']]
            csvwriter.writerow(vals)






pp = pprint.PrettyPrinter(indent=4)
cp = CoversationParser("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/log/curInteractionLogTable.txt")
res = cp.parseClues()
res = postProcessing(res)

count = 0
for k,v in res.iteritems():
    v = combiningIds(v)
    count += len(v)

print count

pp.pprint(res)

writeToCSV(res, "/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/conversationparser.csv")




