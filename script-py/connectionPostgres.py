#   CAMPOS
#   Atributo
#   Grupo
#   Código tributação

import pandas as pd
import psycopg2
from sqlalchemy import create_engine,text


def connectionPostgres(contmaticId):
    conn = create_engine('postgresql+psycopg2://postgres@192.168.5.27/erp')
    queryNomeAtributo = f'''
        SELECT nome
        FROM atributo
        WHERE contmatic_id = {contmaticId}
    '''
    queryNomeGrupo = f'''
        SELECT nome
        FROM grupo
        WHERE contmatic_id = {contmaticId}
    '''
    queryTributacao = f'''
        SELECT codigo
        FROM tributacao 
        WHERE contmatic_id = {contmaticId};
    '''

    resultAtributo = conn.connect().execute(text(queryNomeAtributo))
    resultGrupo = conn.connect().execute(text(queryNomeGrupo))
    resultTributacao = conn.connect().execute(text(queryTributacao))

    listaAtributos = list(map(lambda e: e[0], list(resultAtributo)))
    listaGrupos = list(map(lambda e: e[0], list(resultGrupo)))
    listaCodigoTributacao = list(map(lambda e: e[0], list(resultTributacao)))

    return listaAtributos, listaGrupos, listaCodigoTributacao
