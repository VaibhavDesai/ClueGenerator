import csv
from datetime import date

def readFile():
    file_path = "/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/Desserts.csv"
    employ_data = open(file_path, 'a')
    csvwriter = csv.writer(employ_data)
    header = ["rawClue", "source", "dateExtracted", "targetword", "cluetype"]
    csvwriter.writerow(header)
    f = open("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/wordNetThemeNewClues.csv","r")
    today = date.today()
    while True:
        lines = f.readline()
        print lines
        if lines == None:
            break
        line = lines.split(",")

        vals = [line[1], line[2], today.ctime(), line[0], line[3]]
        csvwriter.writerow(vals)

readFile()