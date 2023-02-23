import openpyxl
from faker import Faker
from funcoes_parceiros import *
import json

locales = 'pt-BR'
fake = Faker(locales)

with open("mapeamento_cadastros.json", 'r', encoding='utf-8') as mapeamento_json:
    dadosJson = json.load(mapeamento_json)

planilha = openpyxl.load_workbook('planilhas/importar-parceiro.xlsx')

paginaParceiro = planilha['importar-parceiros']

todosCampos = dadosJson["simplifique"]["clientes"]["campos"]

def preencherPlanilhaCamposObrigatorios(argQuantidadeCadastro):
    for linhaPlanilha in range (POSICAO_PRIMEIRA_LINHA_PREENCHIMENTO, calcQuantidadeCadastro(argQuantidadeCadastro) ):
        infDadoCriado = {}
        for colunaPlanilha, campo in [(y + 1, campo) for (y, campo) in enumerate(todosCampos)]:
            if campo["obrigatorio"]:
                campoAlgoritmo = campo['algoritmo']
                campoCabecalho =  campo['cabecalho']
                paginaParceiro.cell(row = linhaPlanilha, column = colunaPlanilha , value = checkValor(infDadoCriado, campoAlgoritmo, campoCabecalho))

preencherPlanilhaCamposObrigatorios(5)
planilha.save('planilhasTeste/importar-parceiros-teste001.xlsx')