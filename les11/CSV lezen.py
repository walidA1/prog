import csv

with open("gamers.csv", "r") as file:
    reader = csv.DictReader(file, delimiter=";")
    score = 0
    high = 0
    for i in reader:
        if int(i["punten"]) > score:
            score = int(i["punten"])
            high = i
    print("De hoogste score is: {} op {} behaald door {}".format(high["punten"],high["datum"],high["naam"]))