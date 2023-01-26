import openpyxl
from faker import Faker

locales = 'pt-BR'
fake = Faker(locales)

import random

statusParceiro = ['Ativo', 'Inativo']
a = random.choice(statusParceiro)

tipoParceiro = ['Fornecedor', 'Transportadora', 'Cliente']
b = random.choice(tipoParceiro)

perfilParceiro = ['Pessoa Física', 'Pessoa Jurídica', 'Estrangeiro']
c = random.choice(perfilParceiro)

tipoInscricaoEstadual = ['Isento', 'Contribuinte', 'Não Contribuinte']
d = random.choice(tipoInscricaoEstadual)

lista = ["01", a, b, c, fake.cnpj(), fake.company(), d]

planilha = openpyxl.load_workbook('importar-parceiro.xlsx')

cadastro_parceiros_page = planilha['importar-parceiros']

for x in range(3,20):
    for y in range (1,6):
        cadastro_parceiros_page.cell(row = x, column = y, value = lista[y])

planilha.save('importar-parceiros-teste.xlsx')        