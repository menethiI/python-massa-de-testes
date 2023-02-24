import json
from faker import Faker
import random
import string
from listaValoresPreenchimento import *

locales = 'pt-BR'
fake = Faker(locales)

POSICAO_PRIMEIRA_LINHA_PREENCHIMENTO = 3
valorPreenchido = ""

with open("mapeamento_parceiros.json", encoding='utf-8') as meu_json:
    dadosJsonCampos = json.load(meu_json)

camposPrioritarios = dadosJsonCampos["simplifique"]["parceiros"]["camposPrioritarios"]


def checkValor(infDadoCriado, campoAlgoritmo, campoCabecalho):
    valor = eval(f'{campoAlgoritmo}({checkInfDadoCriado(infDadoCriado, campoCabecalho, valorPreenchido)})')
    checkCamposPrioritario(infDadoCriado, campoCabecalho, valor)
    return valor


def checkInfDadoCriado(infDadoCriado, campoCabecalho, valorPreenchido):
    for campo in camposPrioritarios:
        if campo["cabecalho"] in infDadoCriado and checkCamposValidar(campoCabecalho):
            campoPrioritario = campo["cabecalho"]
            valorPreenchido = f"'{infDadoCriado[campoPrioritario]}'"
            return valorPreenchido
    return valorPreenchido


def checkCamposValidar(campoCabecalho):
    for campoValidar in camposPrioritarios:
        for campo in campoValidar["campos"]:
            if campoCabecalho in campo["cabecalho"]:
                return True
    return False


def checkCamposPrioritario(infDadoCriado, campoCabecalho, valor):
    for campo in camposPrioritarios:
        if campoCabecalho in campo["cabecalho"]:
            infDadoCriado[campoCabecalho] = valor


def calcQuantidadeCadastro(argQuantidadeCadastro):
    return POSICAO_PRIMEIRA_LINHA_PREENCHIMENTO + argQuantidadeCadastro


def generate_status():
    return random.choice(status)


def generate_tipoCadastro():
    return random.choice(tipoCadastro)


def generate_perfilParceiro():
    return random.choice(perfilParceiro)


def generate_documentoIdentificacao(tipoPessoa):
    return checkTipoPessoa(tipoPessoa)


def generate_razaoSocial_or_name(tipoPessoa):
    if tipoPessoa == "Pessoa Física" or "Estrangeiro":
        return fake.name()
    if tipoPessoa == "Pessoa Jurídica":
        return fake.company()


def generate_nome(recebeXML):
    return fake.name()


def generate_nomeFantasia(tipoPessoa):
    return fake.bs() if tipoPessoa == "Pessoa Jurídica" else ''


def generate_dataAniversario(tipoPessoa):
    return format(fake.date_of_birth(), "%d/%m/%Y") if tipoPessoa == "Pessoa Física" else ''


def generate_CNAE(tipoPessoa):
    return random.choice(cnae) if tipoPessoa == "Pessoa Jurídica" else ''


def generate_inscricaoMunicipal():
    return fake.pyint()


def generate_tipoInscricaoEstadual():
    return random.choice(tipoInscricaoEstadual)


def generate_inscricaoEstadual(inscricaoEstadual):
    return fake.pyint() if inscricaoEstadual != "Isento" else ''


def generate_SUFRAMA(inscricaoEstadual):
    return random.choice(suframa) if inscricaoEstadual != "Isento" else ''


def generate_documento_contato(tipoPessoa):
    return checkTipoPessoa(tipoPessoa)


def generate_areaResponsavel():
    return fake.bs()


def generate_recebeXML():
    return random.choice(['Sim', 'Não'])


def generate_tipoTelefone(recebeXml):
    return random.choice(tipoTelefone)


def generate_telefone(recebeXml):
    return random.getrandbits(32)


def generate_email(recebeXml):
    return fake.ascii_free_email()


def generate_tipoEndereco(arg):
    return random.choice(tipoEndereco)


def generate_CEP():
    return fake.postcode().replace("-", "")


def generate_logradouro(arg):
    return fake.street_name()


def generate_numeroPropriedade(arg):
    return fake.building_number()


def generate_complemento():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


def generate_municipio():
    return fake.neighborhood()


def generate_bairro(arg):
    return fake.bairro()


def generate_UF(arg):
    return fake.estado_sigla()


def generate_pais():
    return "Brasil"


def checkTipoPessoa(tipoPessoa):
    if tipoPessoa == "Pessoa Física":
        return fake.cpf()
    if tipoPessoa == "Pessoa Jurídica":
        return fake.cnpj()
    if tipoPessoa == "Estrangeiro":
        return fake.ssn()