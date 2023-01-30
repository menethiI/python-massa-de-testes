import json

x = '{ "cabecalho":"Status", "algoritmo": "generate_status", "obrigatorio": true}'
y = json.loads(x)

print(y["obrigatorio"])


