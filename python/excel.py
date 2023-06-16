import pandas as pd
from pymongo import MongoClient

# Conectar ao banco de dados MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco_de_dados']
collection = db['meu_colecao']

# Recuperar todos os documentos da coleção
documentos = collection.find()

# Converter os documentos para um DataFrame do pandas
df = pd.DataFrame(documentos)

# Especificar o nome do arquivo Excel
nome_arquivo = 'dadoss.xlsx'

# Salvar o DataFrame no arquivo Excel
df.to_excel(nome_arquivo, index=False)

print("Dados exportados para Excel com sucesso!")
