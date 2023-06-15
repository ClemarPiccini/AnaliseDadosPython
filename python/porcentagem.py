from pymongo import MongoClient

# Conectar ao banco de dados MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco_de_dados']
collection = db['meu_colecao']

# Recuperar os dados da coleção
data = collection.find()
print (collection)
# Contar o número total de documentos
total_empresas = collection.count_documents({})
print(total_empresas)
# Contar o número de empresas ativas (SITUAÇÃO CADASTRAL igual a "Ativa")
empresas_ativas = collection.count_documents({"DATA SITUAÇÃO CADASTRAL": 2})
print (empresas_ativas)
# Calcular a porcentagem de empresas ativas
porcentagem_ativas = (empresas_ativas / total_empresas) * 100

# Exibir o resultado
print(f"Porcentagem de empresas ativas: {porcentagem_ativas:.2f}%")
