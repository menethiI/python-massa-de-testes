import json

with open('mapeamento.json') as mapFile:
    mapJson = json.load(mapFile)

print(mapJson)
print(mapJson['teste']['teste2'])