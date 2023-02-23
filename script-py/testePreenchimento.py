import openpyxl
import json
from faker import Faker
from funcoes import *

# main(projName, TelaCadastro, quantidadeCadastros, contmaticID)

planilha = openpyxl.load_workbook('excel/planilhas/importar-parceiro.xlsx')
paginaParceiro = planilha['importar-parceiros']


with open("script-py/mapeamento_cadastros.json", encoding='utf-8') as meu_json:
    dadosJson = json.load(meu_json)

camposPlanilha = dadosJson["simplifique"]["clientes"]["campos"]

def preencherPlanilhaCamposObrigatorios(argQuantidadeCadastro):
    for linhaPlanilha in range (POSICAO_PRIMEIRA_LINHA_PREENCHIMENTO, calcQuantidadeCadastro(argQuantidadeCadastro) ):
        infDadoCriado = {}
        for colunaPlanilha, campo in [(y + 1, campo) for (y, campo) in enumerate(camposPlanilha)]:
            if campo["obrigatorio"]:
                paginaParceiro.cell(row = linhaPlanilha, column = colunaPlanilha , value = checkValor(infDadoCriado, campo['algoritmo'], campo['cabecalho']))
            else:
                paginaParceiro.cell(row = linhaPlanilha, column = colunaPlanilha, value = "")

def preencherPlanilhaTodosCampos(argQuantidadeCadastro): 
    for linhaPlanilha in range (POSICAO_PRIMEIRA_LINHA_PREENCHIMENTO, calcQuantidadeCadastro(argQuantidadeCadastro) ):
        infDadoCriado = {}
        for colunaPlanilha, campo in [(y + 1, campo) for (y, campo) in enumerate(camposPlanilha)]:
            paginaParceiro.cell(row = linhaPlanilha, column = colunaPlanilha , value = checkValor(infDadoCriado, campo['algoritmo'],  campo['cabecalho']))

preencherPlanilhaCamposObrigatorios(15)
planilha.save('excel/planilhasGerada/importar-parceiros-teste3.xlsx')