import xml_tools

xml = xml_tools.processXML("stations.xml")

stations_codes = []
synoniem = {}
lange_naam = []
for i in xml["Stations"]['Station']:
    stations_codes.append([i['Code'],i['Type']])
    if i['Synoniemen'] is not None:
        synoniem[i['Code']] = {}
        synoniem[i['Code']]['naam']=i["Namen"]['Lang']
        synoniem[i['Code']]['Syn']=[]

        for x in i["Synoniemen"]["Synoniem"]:
            synoniem[i['Code']]['Syn'].append(x)

    lange_naam.append([i["Code"],i["Namen"]["Lang"]])

print("Dit zijn de codes en types van de 4 stations:")
for i in stations_codes:
    print('{:4} - {}'.format(i[0],i[1]))

print("\nDit zijn alle stations met één of meer synoniemen:")
for i in synoniem:
    print("Code: {:3} - Volledige naam: {} - Synoniemen: {}".format(i,synoniem[i]["naam"],synoniem[i]["Syn"]))

print("\nDit is de lange naam van elk station:")
for i in lange_naam:
    print("{:4} - {}".format(i[0],i[1]))

