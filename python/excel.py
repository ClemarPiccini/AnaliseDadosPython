import pandas as pd
from db import conectar_banco_dados

db = conectar_banco_dados()
collection = db['meu_colecao']
# Recuperar todos os documentos da coleção
documentos = collection.find()

# Converter os documentos para um DataFrame do pandas
df = pd.DataFrame(documentos)

# Especificar o nome do arquivo Excel
nome_arquivo = 'dadosss.xlsx'

# Salvar o DataFrame no arquivo Excel
df.to_excel(nome_arquivo, index=False)

print("Dados exportados para Excel com sucesso!")
