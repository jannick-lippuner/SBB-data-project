import json

with open("./json-files/ist-daten-sbb.json") as json_file:
    data = json.load(json_file)
    print(data)