from pymongo import MongoClient
from pymongo import GEOSPHERE

# Conectar ao banco de dados MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco_de_dados']
collection = db['meu_colecao']

# Criar um índice geoespacial na coleção
collection.create_index([("CEP", GEOSPHERE)])

# Definir o ponto de referência (CEP 01422000)
cep_referencia = {"type": "Point", "coordinates": [-46.673398, -23.569359]}

# Definir a distância máxima em metros (5 km = 5000 metros)
distancia_maxima = 5000

# Consulta para contar a quantidade de empresas próximas ao CEP de referência
query = {
    "CEP": {
        "$near": {
            "$geometry": cep_referencia,
            "$maxDistance": distancia_maxima
        }
    }
}

# Executar a consulta
quantidade_empresas = collection.count_documents(query)

# Exibir o resultado
print(f"Quantidade de empresas no raio de 5 km do CEP 01422000: {quantidade_empresas}")
