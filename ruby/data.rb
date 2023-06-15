require 'csv'

# Lê o arquivo CSV com opções de codificação e análise liberal
CSV.foreach('/home/senai/Downloads/K3241.K03200Y1.D30513.ESTABELE', encoding: "ISO8859-1:UTF-8", headers: true, liberal_parsing: true) do |row|
  # Acessa os valores de cada coluna usando os cabeçalhos
  puts row['Nome da Coluna1']
  puts row['Nome da Coluna2']
  # ...
end
