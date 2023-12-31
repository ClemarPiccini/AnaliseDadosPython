import csv
from db import conectar_banco_dados

db = conectar_banco_dados()
collection = db['meu_colecao']

# Recuperar todos os documentos da coleção
documentos = collection.find()

# Especificar o nome do arquivo CSV
nome_arquivo = 'dadosss.csv'

# Abrir o arquivo CSV em modo de gravação
with open(nome_arquivo, 'w', newline='') as csvfile:
    # Criar um objeto escritor CSV
    writer = csv.writer(csvfile)

    # Escrever o cabeçalho do CSV com base nas chaves do primeiro documento
    primeiro_documento = documentos[0]
    header = primeiro_documento.keys()
    writer.writerow(header)

    # Escrever os dados de cada documento no arquivo CSV
    for documento in documentos:
        writer.writerow(documento.values())

print("Dados exportados para CSV com sucesso!")
