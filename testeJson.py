import json

x = '{ "cabecalho":"Status", "algoritmo": "generate_status", "obrigatorio": true}'
y = json.loads(x)

# the result is a Python dictionary:
print(y["obrigatorio"])


