# Conectar ao banco de dados MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco_de_dados']
collection = db['meu_colecao']

# Inserir os dados no MongoDB
collection.insert_one(data_dict)

print("Dados inseridos no MongoDB com sucesso!")
