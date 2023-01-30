import openpyxl
from faker import Faker
from funcoes import *
import json

locales = 'pt-BR'
fake = Faker(locales)

with open("mapeamento_cadastros.json", 'r', encoding='utf-8') as mapeamento_json:
    dados = json.load(mapeamento_json)

def gerarlistaCadastroCamposObrigatorios():
    listaCadastroObrigatorio = [ '00', generate_status(), generate_tipoCadastro(), generate_perfilParceiro(), generate_documentoIdentificacao(), "razao social", "nome fantasia", "data", "cnae", "inscricao", generate_tipoInscricaoEstadual()]
    return listaCadastroObrigatorio

planilha = openpyxl.load_workbook('importar-parceiro.xlsx')

cadastro_parceiros_page = planilha['importar-parceiros']

for x in range(3,5):
    for y in range (1, 11):
        cadastro = gerarlistaCadastroCamposObrigatorios()
        caminho = dados["simplifique"]["clientes"]["campos"]
        for i in caminho:
            if(i["obrigatorio"] == False):
                cadastro_parceiros_page.cell(row = x, column = y, value = "teste")
            else:
                print("entrei aqui como true")


planilha.save('importar-parceiros-teste.xlsx')
