from pymongo import MongoClient
from main import data_dict

# Função para estabelecer a conexão com o banco de dados MongoDB
def conectar_banco_dados():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['meu_banco_de_dados']
    return db

db = conectar_banco_dados()
collection = db['meu_colecao']

# Separar os dados do dicionário em colunas
cnpj = data_dict.get('CNPJ')
identificador_matriz_filial = data_dict.get('IDENTIFICADOR MATRIZ/FILIAL')
razao_social = data_dict.get('RAZÃO SOCIAL/NOME EMPRESARIAL')
nome_fantasia = data_dict.get('NOME FANTASIA')
situacao_cadastral = data_dict.get('SITUAÇÃO CADASTRAL')
data_sit_cadastral = data_dict.get('DATA SITUACAO CADASTRAL')
motivo_sit_cadastral = data_dict.get('MOTIVO SITUAÇÃO CADASTRAL')
nm_cidade_exterior = data_dict.get('NM-CIDADE EXTERIOR')
co_pais = data_dict.get('CO-PAIS')
nm_pais = data_dict.get('NM-PAIS')
codigo_nat_juridica = data_dict.get('CODIGO NATUREZA JURIDICA')
data_ini_atividade = data_dict.get('DATA INICIO ATIVIDADE')
cnae_fiscal = data_dict.get('CNAE-FISCAL')
desc_logradouro = data_dict.get('DESCRIÇÃO TIPO LOGRADOURO')
logradouro = data_dict.get('LOGRADOURO')
numero = data_dict.get('NUMERO')
complemento = data_dict.get('COMPLEMENTO')
bairro = data_dict.get('BAIRRO')
cep = data_dict.get('CEP')
uf = data_dict.get('UF')
cod_municipio = data_dict.get('CODIGO MUNICIPIO')
municipio = data_dict.get('MUNICIPIO')
ddd = data_dict.get('DDD-1')
telefone = data_dict.get('TELEFONE-1')
ddd_2 = data_dict.get('DDD-2')
telefone_2 = data_dict.get('TELEFONE-2')
nu_ddd_fax = data_dict.get('NU-DDD-FAX')
nu_fax = data_dict.get('NU-FAX')
email = data_dict.get('CORREIO ELETRONICO')
qualificacao_resp = data_dict.get('QUALIFICAÇÃO DO RESPONSÁVEL')
capital_social = data_dict.get('CAPITAL SOCIAL DA EMPRESA')

# Criar um novo documento com as colunas separadas
novo_documento = {
    "CNPJ": cnpj,
    "IDENTIFICADOR_MATRIZ_FILIAL": identificador_matriz_filial,
    "RAZAO_SOCIAL": razao_social,
    "NOME_FANTASIA": nome_fantasia,
    "SITUACAO_CADASTRAL": situacao_cadastral,
    "DATA_SITUACAO_CADASTRAL": data_sit_cadastral,
    "MOTIVO_SITUACAO_CADASTRAL": motivo_sit_cadastral,
    "NM_CIDADE_EXTERIOR": nm_cidade_exterior,
    "CO_PAIS": co_pais,
    "NM_PAIS": nm_pais,
    "CODIGO_NATUREZA_JURIDICA": codigo_nat_juridica,
    "DATA_INICIO_ATIVIDADE": data_ini_atividade,
    "CNAE_FISCAL": cnae_fiscal,
    "DESCRICAO_TIPO_LOGRADOURO": desc_logradouro,
    "LOGRADOURO": logradouro,
    "NUMERO": numero,
    "COMPLEMENTO": complemento,
    "BAIRRO": bairro,
    "CEP": cep,
    "UF": uf,
    "CODIGO_MUNICIPIO": cod_municipio,
    "MUNICIPIO": municipio,
    "DDD_1": ddd,
    "TELEFONE_1": telefone,
    "DDD_2": ddd_2,
    "TELEFONE_2": telefone_2,
    "NU_DDD_FAX": nu_ddd_fax,
    "NU_FAX": nu_fax,
    "CORREIO_ELETRONICO": email,
    "QUALIFICACAO_RESPONSAVEL": qualificacao_resp,
    "CAPITAL_SOCIAL": capital_social
}

# Armazenar o novo documento no banco de dados
collection.insert_one(novo_documento)

print("Dados inseridos no MongoDB com sucesso!")
print (novo_documento)


