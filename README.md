### Automação de Cadastro de Produtos
Automação de cadastro de produtos em sistemas online utilizando Python e PyAutoGUI. Este projeto foi desenvolvido para agilizar o processo de inserção de dados a partir de uma planilha CSV.

✨ Funcionalidades

🌐 Acessa automaticamente o navegador e realiza login no sistema da empresa.

📊 Importa uma base de dados (produtos.csv) com informações de cada produto:

Código

Marca

Tipo

Categoria

Preço unitário

Custo

Observações

🤖 Cadastra automaticamente todos os produtos no sistema.

🛠 Tecnologias Utilizadas

Python

PyAutoGUI
 → automação de cliques e digitação

Pandas
 → leitura e manipulação da base de dados

Time
 → controle de pausas e sincronização do processo

📂 Estrutura do Projeto
projeto-automacao-cadastro/
├── produtos.csv       # Base de dados com os produtos
├── automacao.py       # Script principal de automação
└── README.md          # Documentação do projeto

⚡ Como Executar

Instale as dependências:

pip install pyautogui pandas


Ajuste as coordenadas de clique no script (x, y) de acordo com a resolução da sua tela.

Execute o script:

python automacao.py


⚠️ Atenção: Durante a execução, evite usar o mouse ou teclado, pois o PyAutoGUI controla o computador.

🎯 Objetivo

Este projeto é um exercício prático de automação de processos, simulando um cenário real de cadastro em sistemas corporativos.
Ideal para aprender Python, manipulação de dados e automação de tarefas repetitivas de forma prática.
