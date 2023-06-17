from pymongo import MongoClient

# Conectar ao banco de dados MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco_de_dados']
collection = db['meu_colecao']

# Definir o prefixo do CNAE PRINCIPAL para empresas de restaurantes
prefixo_cnae_restaurantes = "56.1"

# Agregação para contar a quantidade de empresas de restaurantes abertas em cada ano
pipeline = [
    # Filtrar as empresas com prefixo do CNAE PRINCIPAL de restaurantes
    {"$match": {"CNAE-FISCAL": {"$regex": f"^{prefixo_cnae_restaurantes}"}}},
    # Extrair o ano da data de início de atividade
    {"$addFields": {"ANO": {"$substr": ["DATA-INICIO-ATIVIDADE", 0, 4]}}},
    # Agrupar por ano e contar a quantidade de documentos em cada grupo
    {"$group": {"_id": "$ANO", "count": {"$sum": 1}}},
    # Ordenar por ano em ordem crescente
    {"$sort": {"_id": 1}}
]

# Executar a agregação
result = list(collection.aggregate(pipeline))

# Exibir o resultado
for doc in result:
    ano = doc["_id"]
    quantidade = doc["count"]
    print(f"Ano: {ano}, Quantidade: {quantidade}")

#restaurante ativos nao ta funcionando #