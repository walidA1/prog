import xml_tools

xml = xml_tools.processXML("artikelen.xml")

for i in xml["artikelen"]["artikel"]:
    print(i['naam'])