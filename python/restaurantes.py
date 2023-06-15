from pymongo import MongoClient

# Conectar ao banco de dados MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco_de_dados']
collection = db['meu_colecao']

# Definir o prefixo do CNAE PRINCIPAL para empresas de restaurantes
prefixo_cnae_restaurantes = "561"

# Agregação para contar a quantidade de empresas de restaurantes abertas em cada ano
pipeline = [
    # Filtrar as empresas com prefixo do CNAE PRINCIPAL de restaurantes
    {"$match": {"CNAE PRINCIPAL": {"$regex": f"^{prefixo_cnae_restaurantes}.*"}}},
    # Agrupar por ano e contar a quantidade de documentos em cada grupo
    {"$group": {"_id": {"$substr": ["$DATA DE INÍCIO ATIVIDADE", 0, 4]}, "count": {"$sum": 1}}},
    # Ordenar por ano em ordem crescente
    {"$sort": {"_id": 1}}
]

# Executar a agregação
result = collection.aggregate(pipeline)
print(result)
# Exibir o resultado
for doc in result:
    ano = doc["_id"]
    quantidade = doc["count"]
    print(f"Ano: {ano}, Quantidade: {quantidade}")
