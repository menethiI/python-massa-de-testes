import json
import random
from funcoes import *

with open("script-py/mapeamento_cadastros.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

with open("script-py/mapeamento_campos.json", encoding='utf-8') as meu_json:
    dadosJsonCamposObrigatorios = json.load(meu_json)

camposPrioritarios = dadosJsonCamposObrigatorios["simplifique"]["parceiros"]["camposPrioritarios"]

for campo in camposPrioritarios:
    print(campo["campos"])
    if "Documento de Identificação" in campo["campos"]:
        print("simm")


# def listaId(id):
#     for item in lista:
#         return item if item["id"] == id else ""

# print(listaId("Parceiro")["campos"])