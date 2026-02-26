#  Simuilador de Grig de largada da Formula 1

Descrição
Pequeno projeto em Python que simula o Grid de largada da Formula 1 


## Recursos utilizados:
- Python 3
- biblioteca Rando para geração de tepos aleatórios

## Conceitos praticados neste projeto

- Uso de funçoes para reutilização do código.
- Listas para cadastro dos Pilotos e tempos de volta
- Uso do randint para gerar tempos aleatórios


## Motivação

Criar simuiladores para treinar lógica de programação, manipulação de dados, loops e validação de entrada de dados.


## Como o programa funciona

1. O programa:
   - Gera tempos aleatórios baseado na lista de pilotos.
   - Ordena a lista e exibe as posições em ordem crescente
   - Gera novas listas com:
     - Classificados para a proxima sessão de treino (com 16 e 10 pilotos)
     - Eliminados das sessões (Q1 e Q2)
     - Lista ordenada com os 10 primeiros colocados
     - Gera uma nova lista com os 10 primeiros e os eliminados do Q2 e Q1 		
   
## Estrutura das funções principais

- `gerar_tempo()`: Gera tempo aleatório com minutos, segundos e milesimos.
- `simular_treino()`: Atualiza as listas Q1, Q2 e Q3 com os tempos da funcao gerar_tempo.
- `exibe_sessao()`: Mostra o resultado de cada sessão destacando os eliminados.

##  Como executar

1. Clone o repositório ou baixe os arquivos.
2. Instale o Python 3, se ainda não tiver.
3. No terminal, dentro da pasta do projeto, execute: python formula1.py


Contatos:

[![Gmail](https://img.shields.io/badge/Gmail-333333?style=for-the-badge&logo=gmail&logoColor=red)](mailto:wanderrbrito@gmail.com)


[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/wanderlei-rbrito/)


[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/wanderrbrito/)
