import csv

def modifySynonyms():

    excel_data = open("../Data/newDicToExcel.csv", 'a')

    writer = csv.writer(excel_data)
    header = ["curID", "rawClue", "procClue", "source", "dateExtracted", "target", "type", "targInflections", "length", "avgCOPMI", "maxPMI"]
    #writer.writerow(header)

    in_file = open("../Data/dicToExcel11.csv", "rb")
    reader = csv.reader(in_file)
    for row in reader:
        if row[6] == 'sys':
            clue = row[1].split(" ")
            if len(clue) > 1:
                row[6] = "synStudy"
        writer.writerow(row)

modifySynonyms()