# %%
from faker import Faker
import random
import sys
import string

# %%
locales = 'pt-BR'
fake = Faker(locales)

# %%
status = ['Ativo', 'Inativo']
origem = ['0 - Nacional: exceto as indicadas nos códigos 3, 4, 5 e 8', '1 - Estrangeira: importação direta, exceto a indicada no código 6', '2 - Estrangeira: adquirida no mercado interno, exceto a indicada no código 7', '3 - Nacional: mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%', '4 - Nacional: produção em conformidade com processos básicos tratados na legislação dos Ajustes', '5 - Nacional: mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%', '6 - Estrangeira: importação direta, sem similar nacional, constante em lista da CAMEX', '7 - Estrangeira: adquirida no mercado interno, sem similar nacional, constante em lista da CAMEX', '8 - Nacional: mercadoria ou bem com Conteúdo de Importação superior a 70%']
tipoProduto = ['00 - Mercadoria para Revenda', '01 - Matéria Prima', '02 - Embalagens', '03 - Produto em Processo', '04 - Produto Acabado', '05 - Subproduto', '06 - Produto Intermediário', '07 - Material de uso e consumo', '08 - Ativo Imobilizado', '10 - Outros Insumos', '99 - Outros']
unidadeMedida = ['Ampola','Balde','Barra','Bobina','Bloco']
ncm = ['01012100','02011000', '12116000', '55094200', '90302010']
cest = ['0100100', '0200100', '0300100', '0400100', '2899900']


def generate_status():
    return random.choice(status)

def generate_codigoProduto():
    return fake.pyint()

def generate_nomeProduto():
    return fake.pystr()

def generate_codigoBarras():
    return fake.ean()

def generate_precoVenda():
    return round(random.uniform(0.00, 1000.00), 2)

def generate_marca():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

def generate_peso():
    return round(random.uniform(0.00, 90.00), 3)

def generate_unidadeMedida():
    return random.choice(unidadeMedida)

def generate_valorAtributo():
    return ''.join(random.choices(string.ascii_uppercase, k=2)) 

def generate_informacoesAdicionais():
    return fake.catch_phrase()

def generate_estoqueMinimo():
    return '1'

def generate_estoque():
    return fake.pyint()

def generate_origem():
    return random.choice(origem)

def generate_tipoProduto():
    return random.choice(tipoProduto)

def generate_NCM():
    return random.choice(ncm)

def generate_exTipi():
    return fake.pyint()

def generate_controleFCI():
    return random.getrandbits(105)

def generate_aliquotaTributosFederal():
    return fake.pyint()

def generate_aliquotaTributosEstadual():
    return fake.pyint()

def generate_CEST():
    return random.choice(cest)


def generate_codigoTributacao():
    return fake.pyint()

def generate_codigoBeneficioUF():
    return random.getrandbits(25)

def generate_documentoIdentificacao():
    return random.choice([fake.cpf(), fake.cnpj(), fake.ssn()])


