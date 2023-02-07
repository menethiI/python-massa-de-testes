# %%
from faker import Faker
import random
import sys

# %%
locales = 'pt-BR'
fake = Faker(locales)

# %%
status = ['Ativo']
tipoCadastro = ['Cliente', 'Fornecedor', 'Transportadora', 'Cliente | Fornecedor', 'Cliente | Fornecedor | Transportadora', 'Cliente | Transportadora', 'Fornecedor | Transportadora']
perfilParceiro = ['Pessoa Física', 'Pessoa Jurídica', 'Estrangeiro']
tipoInscricaoEstadual = ['Isento', 'Contribuinte', 'Não contribuinte']
cnae = ['3250706','4530702','4530706','4613300']
suframa = ['82252918', '87866990', '24794329', '50230069']
tipoTelefone = ['Celular', 'Comercial', 'Residencial', 'FAX', 'Outros']
tipoEndereco = ['Comercial', 'Residencial', 'Cobrança', 'Entrega', 'Outros']

# %%
def generate_status():
    return random.choice(status)

# %%
def generate_tipoCadastro():  
    return random.choice(tipoCadastro)

# %%
def generate_perfilParceiro():   
    return random.choice(perfilParceiro)

# %%
def generate_documentoIdentificacao():  
    return random.choice([fake.cpf(), fake.cnpj(), fake.ssn()])

# %%
def generate_razaoSocial():
    return fake.company()

# %%
def generate_nome():
    return fake.nome()

# %%
def generate_nomeFantasia():
    return fake.bs()

# %%
def generate_dataAniversario():
    return fake.date_of_birth()

# %%
def generate_CNAE():
    return random.choice(cnae)

# %%
def generate_inscricaoMunicipal():
    return fake.pyint()

# %%
def generate_tipoInscricaoEstadual():
    return random.choice(tipoInscricaoEstadual)

# %%
def generate_inscricaoEstadual():
    return fake.pyint()

# %%
def generate_SUFRAMA():
    return random.choice(suframa)

# %%
def generate_documento():
    return random.choice([fake.cpf(), fake.cnpj()])

# %%
def generate_areaResponsavel():
    return fake.bs()

# %%
def generate_recebeXML():
    return random.choice(['Sim', 'Não'])

# %%
def gerenate_tipoTelefone():
    return random.choice(tipoTelefone)

# %%
def generate_telefone():
    return fake.phone_number()

# %%
def generate_email():
    return fake.ascii_free_email()

# %%
def generate_tipoEndereco():
    return random.choice(tipoEndereco)

# %%
def generate_CEP():
    return fake.postcode()

# %%
def generate_logradouro():
    return fake.street_name()

# %%
def generate_numeroImovel():
    return fake.building_number()

# %%
def generate_complemento():
    return fake.address()

# %%
def generate_municipio():
    return fake.neighborhood()

# %%
def generate_bairro():
    return fake.bairro()

# %%
def generate_UF():
    return fake.estado_sigla()


