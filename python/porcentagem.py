from pymongo import MongoClient

# Conectar ao banco de dados MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco_de_dados']
collection = db['meu_colecao']

documento_ativo = collection.find_one()

# Verificar se o documento existe
if documento_ativo:
    # Recuperar os dados da coluna 'DATA_SITUACAO_CADASTRAL'
    data_situacao_cadastral = documento_ativo.get('DATA_SITUACAO_CADASTRAL', [])

    # Contar a frequência de cada valor
    frequencia = {}
    for valor in data_situacao_cadastral:
        frequencia[valor] = frequencia.get(valor, 0) + 1

    # Exibir a frequência de cada valor
    for valor, count in frequencia.items():
        print(f"{valor}: {count}")
    print("legenda:\n01 - NULA\n02 - ATIVA\n03 - SUSPENSA\n04 - INAPTA\n08 - BAIXADA" )
else:
    print("Não foi encontrado nenhum documento ativo.")