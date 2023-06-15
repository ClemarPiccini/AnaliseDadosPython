from pymongo import MongoClient
from main import data_dict

# Conectar ao banco de dados MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco_de_dados']
collection = db['meu_colecao']

# Armazenar o data_dict no banco de dados
collection.insert_one(data_dict)

print("Dados inseridos no MongoDB com sucesso!")
