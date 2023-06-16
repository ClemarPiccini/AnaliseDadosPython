Desafio Técnico - Data Pipeline
Período de entrega: sábado 


Objetivo: 
Construir um data pipeline completo, desde a extração até o processamento e exibição dos dados da Receita Federal.


Entrega:
Coloque o código em um repositório PRIVADO e compartilhe o acesso com o e-mail desafio@speedio.com.br

Grave um vídeo da tela do aplicativo explicando as funcionalidades implementadas e eventuais features que ficaram de fora. Utilize uma extensão do Chrome chamada "Vidyard" para gravar a tela. Coloque o link do vídeo no README do projeto no repositório.

Desafio:
Escolha da linguagem de programação: Você pode utilizar a linguagem de sua escolha para implementar o data pipeline. (Python, Node, Ruby) 
Se optar por Ruby, receberá pontuação extra.


Leitura dos dados: Utilize uma biblioteca ou módulo adequado para ler os arquivos CSV fornecidos. Se possível, leia todos os arquivos ESTABELECIMENTO disponíveis. O layout dos dados está incluso no link.
https://dadosabertos.rfb.gov.br/CNPJ/

*Organização dos dados: Armazene os dados extraídos em uma estrutura de dicionário, facilitando o acesso e manipulação posterior.*

*Banco de dados: Salve os dados no MongoDB localmente ou utilize o serviço gratuito MongoAtlas para armazená-los em um banco de dados na nuvem. Opte pela solução mais simples para esta etapa.*

Leitura e processamento dos dados: Recupere os dados do banco de dados e realize as seguintes tarefas:
 a) *Calcule a porcentagem de empresas ativas (SITUAÇÃO CADASTRAL).*
 b)**Conte a quantidade de empresas do setor de restaurantes abertas em cada ano, considerando o prefixo do CNAE PRINCIPAL e a DATA DE INÍCIO ATIVIDADE. O prefixo para empresas de restaurantes é 56.1xxxxx, por exemplo, 5611-2/03 representa um restaurante.**

BONUS POINTS: 
c)**Determine a quantidade de empresas localizadas em um raio de 5 km do CEP 01422000.**
d)**Crie uma tabela de correlação entre o CNAE FISCAL PRINCIPAL e o CNAE FISCAL SECUNDÁRIA.**

*Exportação dos dados: Exporte os resultados obtidos no passo anterior para um arquivo CSV. Para ganhar pontos extras, exporte os dados para um formato Excel.*


Atente-se para:
Validação dos dados: Inclua validações nos dados extraídos para garantir sua integridade.
Testes automatizados: Implemente testes automatizados para verificar a corretude do pipeline.
Tratamento de erros e exceções: Adicione tratamento de erros e exceções ao longo do pipeline, garantindo que o sistema seja robusto e resiliente a falhas.
Otimização do código: Melhore a eficiência do código, otimizando as operações e estruturas de dados utilizadas.
Boas práticas de programação: Utilize boas práticas
