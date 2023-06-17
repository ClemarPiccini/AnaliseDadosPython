import numpy as np
import pandas as pd
import requests

headers = ['CNPJ', 'IDENTIFICADOR MATRIZ/FILIAL', 'RAZÃO SOCIAL/NOME EMPRESARIAL', 'NOME FANTASIA',
'SITUAÇÃO CADASTRAL', 'DATA SITUACAO CADASTRAL', 'MOTIVO SITUAÇÃO CADASTRAL',
'NM-CIDADE EXTERIOR', 'CO-PAIS', 'NM-PAIS', 'CODIGO NATUREZA JURIDICA',
'DATA INICIO ATIVIDADE', 'CNAE-FISCAL', 'DESCRIÇÃO TIPO LOGRADOURO', 'LOGRADOURO',
'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'CEP', 'UF', 'CODIGO MUNICIPIO', 'MUNICIPIO',
'DDD-1', 'TELEFONE-1', 'DDD-2', 'TELEFONE-2', 'NU-DDD-FAX', 'NU-FAX',
'CORREIO ELETRONICO', 'QUALIFICAÇÃO DO RESPONSÁVEL', 'CAPITAL SOCIAL DA EMPRESA']

data_dict = {}

df_reader = pd.read_csv('/Users/Junior/Downloads/Estabelecimentos0/K3241.K03200Y0.D30513.ESTABELE',
                        encoding='latin1', sep=';',
                        dtype='string', header=None, names=headers, chunksize=100)

df = next(df_reader)

for i, row in df.iterrows():
    for header in headers:
        value = row[header]
        if pd.notna(value):
            data_dict.setdefault(header, []).append(value)

print(data_dict)
