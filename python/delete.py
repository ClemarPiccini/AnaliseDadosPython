from pymongo import MongoClient

# Conectar ao banco de dados MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco_de_dados']
collection = db['meu_colecao']

# Excluir todos os documentos da coleção
resultado = collection.delete_many({})

# Exibir o número de documentos excluídos
print(f"Número de documentos excluídos: {resultado.deleted_count}")
