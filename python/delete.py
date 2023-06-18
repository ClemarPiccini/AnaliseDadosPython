from db import conectar_banco_dados

db = conectar_banco_dados()
collection = db['meu_colecao']

# Excluir todos os documentos da coleção
resultado = collection.delete_many({})

# Exibir o número de documentos excluídos
print(f"Número de documentos excluídos: {resultado.deleted_count}")
