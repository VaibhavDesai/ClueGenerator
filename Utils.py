from bs4 import BeautifulSoup
import urllib2

import csv
import datetime
import os

def mergeTwoDicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def getWebContent(searchString):
    response = urllib2.urlopen(searchString)
    return BeautifulSoup(response.read(), 'html.parser')


def writeToCSV(data, word, source, output_file_name):

    file_path = "/Users/vaibhavdesai/Documents/research/"+output_file_name+".csv"
    employ_data = open(file_path, 'a')
    csvwriter = csv.writer(employ_data)
    today = datetime.date.today()
    clue_types = ['idiomPhrase', 'def', 'exampSent', 'syn', 'ant']

    cov_clue_types = {}
    cov_clue_types['idiomPhrase'] = "Idioms"
    cov_clue_types['ant'] = "antonyms"
    cov_clue_types['def'] = "noun"
    cov_clue_types['exampSent'] = "example_sentences"
    cov_clue_types['syn'] = "synonyms"

    if os.stat(file_path).st_size == 0:
        header = ["rawClue", "source", "dateExtracted", "targetword", "cluetype"]
        csvwriter.writerow(header)

    for types in clue_types:
        if cov_clue_types[types] in data:
            for clue in data[cov_clue_types[types]]:
                vals = [clue.encode("utf-8"), source, str(today.ctime()), word, types]

                csvwriter.writerow(vals)

    employ_data.close()


def readFile():
    file_path = "/Users/vaibhavdesai/Documents/research/" + "abc" + ".csv"
    employ_data = open(file_path, 'a')
    csvwriter = csv.writer(employ_data)
    header = ["rawClue", "source", "dateExtracted", "targetword", "cluetype"]
    csvwriter.writerow(header)
    f = open("Data/wordNetNewClues.txt","r")
    while True:
        line = f.readline()
        print line
        if line == None:
            break
        line.split(",")
        vals = [line[1], line[2], line[4], line[0], line[3]]
        csvwriter.writerow(vals)

#readFile()