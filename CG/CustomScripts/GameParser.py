class Conversation:

    target = ""
    clue = []
    response = []
    agent = ""
    result = []
    id = ""


def parser():
    f = open("../Data/test.txt", "r")
    actors = ['<PLAYER_GIVER_ASR_SAID>','<SEND_ROBOT>', '<WIZARD_ASR_SAID>']

    c = Conversation()

    responsed = True
    for lines in f.readlines():

        line = lines.split(",")
        #print line
        c.target = line[2]
        #print line[5]
        str = line[5]
        #print str
        if actors[0] in str:
            print line[4]
            if responsed == False:
                c.clue[-1] += " " +line[4]
                c.clue[-1] = c.clue[-1].replace("'", "")
            else:
                c.clue.append(line[4][1:])
                responsed = False

        elif actors[2] in line[5]:
            responsed = True
            c.response.append(line[4])

            if c.target in line[4]:
                c.result.append(True)
            else:
                c.result.append(False)



    print c.clue
    print c.response
    print c.result

parser()