from pymongo import MongoClient
import random

#Conexão com o banco Dados para puxar documentos
# Fornecedor 
# Cliente
# Empresa

mongoclient = MongoClient(
    host='mongodb://192.168.5.98:27017',
    authSource='admin'
)
#Recebendo a base e a collection
db_parceiro = mongoclient["parceiro_dev"]
coll_parceiro_fornecedor = db_parceiro["clienteFornecedor"]
coll_parceiro_cliente = db_parceiro["clienteFornecedor"]
coll_empresa = db_parceiro["empresa"]

#Criando a query e o cursor
contmaticId = 40180

queryDocForncedor = {"fornecedor": True, "_id.contmaticId": contmaticId}
queryDocCliente = {"cliente": True, "_id.contmaticId": contmaticId}

projection = {
    "_id": 1, 
} 

cursorFornecedor = coll_parceiro_fornecedor.find(queryDocForncedor, projection)
cursorCliente = coll_parceiro_cliente.find(queryDocCliente, projection)

#Criando a lista do cursor
parceiro_fornecedor = list(cursorFornecedor)
parceiro_cliente = list(cursorCliente)

cursorFornecedor.close()
cursorCliente.close()

documentosFornecedor = list(map(lambda fornecedorDoc: fornecedorDoc["_id"]["documento"], parceiro_fornecedor))
documentosCliente = list(map(lambda clienteDoc: clienteDoc["_id"]["documento"], parceiro_cliente))

documentos = documentosFornecedor + documentosCliente
listaDocumentos = set(documentos)



