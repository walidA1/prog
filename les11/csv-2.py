import csv

with open("art.csv") as file:
    reader = csv.DictReader(file, delimiter=";")
    prijs=0
    kleine_voorraad=2**64
    duurste = 0
    kleinste = 0
    totaal = 0
    for i in reader:
        if eval(i["Prijs"]) > prijs:
            prijs = eval(i["Prijs"])
            duurste = i

        if eval(i["Voorraad"]) < kleine_voorraad:
            kleine_voorraad = eval(i["Voorraad"])
            kleinste = i

        totaal += int(i["Voorraad"])

    print("Het duurste artikel is {} en die kost {} Euro".format(duurste["Naam"],duurste['Prijs']))
    print("Er zijn slechts {} exemplaren in voorraad van het product met nummer {}".format(kleinste["Voorraad"],kleinste["Artikelnummer"]))
    print("In totaal hebben wij {} producten in ons magazijn liggen".format(totaal))