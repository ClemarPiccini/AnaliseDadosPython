require 'csv'

# Lê o arquivo CSV
CSV.foreach('dados.csv') do |row|
  nome = row[0]
  idade = row[1]
  
  # Faça algo com os dados
  puts "Nome: #{nome}, Idade: #{idade}"
end
