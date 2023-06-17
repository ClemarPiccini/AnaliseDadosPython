from pymongo import MongoClient

# Conectar ao banco de dados MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco_de_dados']
collection = db['meu_colecao']

# Definir os limites dos CEPs (01422000 ± 5000)
cep_central = '01422000'
raio = 5000

# Calcular os limites inferior e superior
cep_inferior = str(int(cep_central) - raio)
cep_superior = str(int(cep_central) + raio)

# Consultar o banco de dados para obter as empresas dentro do intervalo
companies = collection.find({
    'CEP': {
        '$gte': cep_inferior,
        '$lte': cep_superior
    }
})

# Contador de empresas
count = 0

# Exibir os nomes das empresas encontradas
for company in companies:
    count += 1
    print(f"documento {count}: ")

# Exibir o total de empresas encontradas
print(f"Total de empresas dentro do intervalo de CEPs 51")
